"""Auditable frontier-campaign laboratory, not a Soulstorm battle emulator.

Run: python balance_sim.py --seeds 24 --cycles 36 --out balance-results
All random generators are private to a trial. Planning never sees the trial RNG.
"""
from dataclasses import dataclass, field
from itertools import combinations, product
from pathlib import Path
import argparse, copy, csv, hashlib, json, math, random, statistics

TIERS = {1: 2, 2: 4, 3: 8, 4: 12}
PROFILES = {'depot': (3,2,0), 'forge': (5,5,0), 'training': (3,0,2), 'academy': (5,0,5)}

@dataclass
class Fleet:
    strength: int
    maximum: int = 5
    system: int = 0
    used: bool = False
    mobile: bool = False

@dataclass
class World:
    tier: int
    defence: int
    maximum: int
    system: int
    owned: bool = False
    attacked: bool = False
    # A frontier system is one static Minor faction, with its own original maxima.

@dataclass
class Project:
    profile: str
    host: int  # world index; -1 is the Mobile Capital
    integrity: int = 1
    maximum: int = 5
    completed: bool = False
    upgraded: bool = False

    @property
    def active(self):
        return self.completed and self.integrity == self.maximum

@dataclass
class State:
    supply: int = 20
    manpower: int = 20
    trait: str = 'siege'
    cycle: int = 0
    event: int = 0
    deficits: dict = field(default_factory=dict)
    fleets: list = field(default_factory=list)
    worlds: list = field(default_factory=list)
    enemies: dict = field(default_factory=dict)
    enemy_max: dict = field(default_factory=dict)
    projects: list = field(default_factory=list)
    engaged: set = field(default_factory=set)
    fleet_battled: set = field(default_factory=set)
    counts: dict = field(default_factory=dict)
    spent: dict = field(default_factory=lambda: {'supply':0,'manpower':0})
    trace: list = field(default_factory=list)
    captures: int = 0
    first_capture: int = 0
    stop: str = ''
    # Sensitivity switches, never adopted rules.
    expand_mp: int = 0
    create_mp: int = 1
    defender_supply_cost: bool = False
    ties: str = 'defender'

    def record(self, action, **values):
        self.counts[action] = self.counts.get(action,0)+1
        self.trace.append({'cycle':self.cycle,'action':action,**values})

    def change(self, resource, delta):
        if resource in self.deficits:
            return
        value = min(100, getattr(self, resource)+delta)
        setattr(self, resource, max(0,value))
        if value <= 0:
            self.deficits[resource] = 0
            self.record('deficit_'+resource)
            for i,f in enumerate(self.fleets):
                if f.strength > 0:
                    damage = 1 if resource == 'supply' else min(1,f.strength-1)
                    self.hit_fleet(i,damage)

    def afford(self, supply=0, manpower=0):
        return self.supply>=supply and self.manpower>=manpower and not (supply and 'supply' in self.deficits) and not (manpower and 'manpower' in self.deficits)

    def pay(self, supply=0, manpower=0):
        assert self.afford(supply,manpower), (self.supply,self.manpower,supply,manpower)
        self.spent['supply']+=supply; self.spent['manpower']+=manpower
        if supply: self.change('supply',-supply)
        if manpower: self.change('manpower',-manpower)

    def hit_host(self, host, damage):
        for p in self.projects:
            if p.host==host and p.integrity>0:
                p.integrity=max(0,p.integrity-damage)

    def hit_fleet(self, index, damage):
        f=self.fleets[index]
        before=f.strength
        f.strength=max(0,before-damage)
        if f.mobile:
            self.hit_host(-1, min(before,damage))
        if before and not f.strength:
            self.record('fleet_destroyed',mobile=f.mobile)
            if f.mobile:
                self.stop='Mobile Capital destroyed: capital relocation outside frontier model'
                for p in self.projects:
                    if p.host==-1:p.integrity=0
            self.change('manpower',-1)

    def full_host(self, host):
        if host==-1:
            return any(f.mobile and f.strength==f.maximum for f in self.fleets)
        w=self.worlds[host]
        return w.owned and w.defence==w.maximum

    def yards(self):
        return {w.system for w in self.worlds if w.owned and w.tier==4} | {f.system for f in self.fleets if f.mobile and f.strength>0}

    def income(self):
        worlds=sum(w.tier for w in self.worlds if w.owned)
        capitals=4*sum(f.mobile and f.strength>0 for f in self.fleets)
        si=mi=worlds+capitals
        for p in self.projects:
            if p.active:
                _,sp,mp=PROFILES[p.profile]; factor=2 if p.upgraded else 1
                si+=sp*factor;mi+=mp*factor
        upkeep=sum(f.strength>0 and not f.mobile for f in self.fleets)
        return si,mi,upkeep

    def opening(self,rng):
        self.cycle+=1;self.engaged.clear();self.fleet_battled.clear()
        for f in self.fleets:f.used=False
        for w in self.worlds:w.attacked=False
        if self.cycle%3==0:
            si,mi,up=self.income()
            self.change('supply',si);self.change('manpower',mi)
            self.change('supply',-up);self.change('manpower',-up)
            self.record('logistics',income=[si,mi],upkeep=up)
        check=rng.randint(1,6)
        self.event=rng.randint(1,6) if check in (1,6) else 0
        self.record('event',check=check,table=self.event)
        if self.event==1:
            for i,f in enumerate(self.fleets):
                if f.strength:self.hit_fleet(i,1)
            for system,values in self.enemies.items():
                self.enemies[system]=[max(0,x-1) for x in values]
        elif self.event in (3,4):
            for resource in ('supply','manpower'):
                self.change(resource, -5 if self.event==3 else 5)

    def closing(self):
        for system,values in self.enemies.items():
            if system in self.engaged:continue
            eligible=[i for i,x in enumerate(values) if 0<x<self.enemy_max[system][i]]
            if eligible:
                i=max(eligible,key=lambda i:(values[i],-i));values[i]+=1
        for w in self.worlds:
            if not w.owned and not w.attacked:w.defence=min(w.maximum,w.defence+1)
        self.validate()

    def validate(self):
        assert 0<=self.supply<=100 and 0<=self.manpower<=100
        assert all(getattr(self,k)==0 and 0<=v<3 for k,v in self.deficits.items())
        assert all(0<=f.strength<=f.maximum for f in self.fleets)
        assert all(0<w.defence<=w.maximum for w in self.worlds)
        assert all(0<=p.integrity<=p.maximum for p in self.projects)

def fleet_losses(margin):
    return 99 if margin>=16 else (margin+4)//5

def win_probability(a,b,ties='defender'):
    return sum((x+a>y+b) or (ties=='attacker' and x+a==y+b) for x in range(1,21) for y in range(1,21))/400

def fixture(trait='siege',start=20,layout='matched',**switches):
    # Matched frontiers isolate traits from map; Dessica-style cases vary local targets.
    s=State(supply=start,manpower=start,trait=trait,**switches)
    if trait=='mobile':s.fleets=[Fleet(12,12,0,mobile=True)]
    else:
        s.fleets=[Fleet(5)];s.worlds=[World(4,12,12,0,True)]
    local=[2] if layout=='matched' else ([2,1,1] if trait=='mobile' else [2])
    for system,tiers in enumerate([local,[3,2,1],[2,1,1]]):
        for tier in tiers:s.worlds.append(World(tier,TIERS[tier],TIERS[tier],system))
        strength=sum(TIERS[t] for t in tiers)
        s.enemies[system]=[5]*(strength//5)+([strength%5] if strength%5 else [])
        s.enemy_max[system]=s.enemies[system].copy()
    return s

def legal(s,phase):
    if s.stop:return [('none',)]
    actions=[('none',)]
    if phase=='fleet':
        available=[i for i,f in enumerate(s.fleets) if f.strength>0 and not f.used]
        for i in available:
            f=s.fleets[i]
            if not f.mobile and f.strength<f.maximum and f.system in s.yards() and s.afford(1,s.expand_mp):actions.append(('expand',i))
            if s.event!=1:
                for system in s.enemies:
                    if system!=f.system:actions.append(('move',i,system))
        for system in s.enemies:
            here=[i for i in available if s.fleets[i].system==system]
            # Every subset up to 8 assets, plus all assets. Deliberate bounded branching.
            groups=[g for n in range(1,min(len(here),8)+1) for g in combinations(here[:8],n)]
            if len(here)>8:groups.append(tuple(here))
            for group in groups:
                fs=sum(s.fleets[i].strength for i in group); damage=max(1,fs//5)
                enemy=sum(s.enemies[system])
                if enemy and system not in s.fleet_battled and any(s.fleets[i].strength>1 for i in group):actions.append(('battle',group,system))
                for wi,w in enumerate(s.worlds):
                    if w.system!=system or w.owned:continue
                    if not enemy and w.defence>1 and s.afford(2*w.tier):actions.append(('bombard',group,wi))
                    # No fabricated three-way adjudication: bots defer assaults on raid cycles.
                    if s.event!=5 and s.afford(w.tier,damage):actions.append(('assault',group,wi))
    elif phase=='faction':
        if s.deficits:return [('ration',k) for k in sorted(s.deficits)]
        actions+=[('reinforce',),('muster',)]
        if s.afford(1,s.create_mp):
            actions += [('create',system) for system in sorted(s.yards())]
        for i,w in enumerate(s.worlds):
            if w.owned and w.defence<w.maximum and s.afford(w.tier,w.tier):actions.append(('defend',i))
        if any(f.mobile and 0<f.strength<f.maximum for f in s.fleets) and s.afford(4,4):actions.append(('defend',-1))
    elif phase=='construction':
        for i,p in enumerate(s.projects):
            if p.integrity<=0 or not s.full_host(p.host):continue
            if p.completed and p.integrity<p.maximum and s.afford(min(3,p.maximum-p.integrity)):actions.append(('repair',i))
            if not p.completed and s.afford(5):actions.append(('build',i))
            if p.active and not p.upgraded and s.afford(5):actions.append(('upgrade',i))
        hosts=[i for i,w in enumerate(s.worlds) if s.full_host(i)]
        if s.full_host(-1):hosts.append(-1)
        if s.afford(5):
            for host in hosts:
                for profile in PROFILES:
                    if not any(p.host==host and p.profile==profile and p.integrity>0 for p in s.projects):actions.append(('start',profile,host))
    return actions

def apply(s,action,rng,forced=None):
    kind=action[0]
    if kind=='none':return
    s.record(kind,order=action)
    if kind=='expand':
        i=action[1];s.fleets[i].used=True;s.pay(1,s.expand_mp)
        if s.fleets[i].strength:s.fleets[i].strength=min(5,s.fleets[i].strength+2)
    elif kind=='move':s.fleets[action[1]].system=action[2];s.fleets[action[1]].used=True
    elif kind in ('battle','bombard','assault'):
        group=action[1]
        for i in group:s.fleets[i].used=True
        if kind=='battle':
            system=action[2];s.fleet_battled.add(system);s.engaged.add(system)
            initiator=max((i for i in group if s.fleets[i].strength>1),key=lambda i:(not s.fleets[i].mobile,s.fleets[i].strength,-i))
            s.fleets[initiator].strength-=1 # initiation is not host damage
            fs=sum(s.fleets[i].strength for i in group)
            rolls=forced or (rng.randint(1,20),rng.randint(1,20))
            margin=rolls[0]+fs-rolls[1]-sum(s.enemies[system])
            s.trace.append({'cycle':s.cycle,'rolls':rolls,'margin':margin,'combat':'fleet'})
            # Explicit tie convention: no fleet damage to either side; initiation still paid.
            if margin>0:
                loss=fleet_losses(margin);s.enemies[system]=[max(0,x-loss) for x in s.enemies[system]]
            elif margin<0:
                for i in group:s.hit_fleet(i,fleet_losses(-margin))
            return
        w=s.worlds[action[2]];system=w.system;w.attacked=True
        fs=sum(s.fleets[i].strength for i in group);damage=max(1,fs//5)
        if kind=='bombard':
            s.pay(w.tier*2);w.defence=max(1,w.defence-damage);return
        s.engaged.add(system);s.pay(w.tier,damage)
        # Upfront deficit degradation changes surviving participating strength for rolls.
        fs=sum(s.fleets[i].strength for i in group)
        resource={1:40,2:60,3:80}[w.tier]*w.defence/w.maximum
        dc=damage//2
        a=fs+s.supply+s.manpower+(10 if s.event==6 else 0)
        b=sum(s.enemies[system])+2*resource-dc+(10 if s.event==2 else 0)
        if s.defender_supply_cost:b-=w.tier
        rolls=forced or (rng.randint(1,20),rng.randint(1,20))
        won=rolls[0]+a>rolls[1]+b or (s.ties=='attacker' and rolls[0]+a==rolls[1]+b)
        s.trace.append({'cycle':s.cycle,'rolls':rolls,'totals':[rolls[0]+a,rolls[1]+b],'combat':'ground','won':won})
        if won:s.change('manpower',math.floor(damage*.6))
        actual=damage if won else (1 if s.trait=='siege' else 0)
        w.defence-=actual
        if w.defence<=0:
            w.owned=True;w.defence=1;s.captures+=1
            if not s.first_capture:s.first_capture=s.cycle
            s.record('capture',world=action[2],won=won)
            # Point-by-point, deterministic listed-order tie allocation for Minor factions.
            for _ in range(actual):
                values=s.enemies[system];live=[i for i,x in enumerate(values) if x>0]
                if not live:break
                i=max(live,key=lambda i:(values[i],-i));values[i]-=1
            if all(x.owned for x in s.worlds if x.system==system):s.enemies[system]=[0 for _ in s.enemies[system]]
    elif kind=='ration':
        resource=action[1];s.deficits[resource]+=1
        if s.deficits[resource]==3:del s.deficits[resource];setattr(s,resource,10)
    elif kind in ('reinforce','muster'):
        s.change('supply' if kind=='reinforce' else 'manpower',4 if s.trait=='efficient' else 3)
    elif kind=='create':
        s.pay(1,s.create_mp);s.fleets.append(Fleet(1,system=action[1],used=True))
    elif kind=='defend':
        host=action[1]
        if host==-1:
            s.pay(4,4)
            for f in s.fleets:
                if f.mobile and f.strength:f.strength=min(12,f.strength+4)
        else:
            w=s.worlds[host];s.pay(w.tier,w.tier);w.defence=min(w.maximum,w.defence+w.tier)
    elif kind in ('build','repair','upgrade','start'):
        if kind=='start':
            name,host=action[1:];s.pay(5)
            if not s.full_host(host):
                s.stop='Unresolved timing: construction payment damaged its host through a deficit'
                s.record('unsupported_construction_timing');return
            s.projects.append(Project(name,host,maximum=PROFILES[name][0]))
        else:
            p=s.projects[action[1]]
            if kind=='repair':
                n=min(3,p.maximum-p.integrity);s.pay(n)
                if not s.full_host(p.host) or p.integrity<=0:
                    s.stop='Unresolved timing: repair payment damaged its host through a deficit'
                    s.record('unsupported_construction_timing');return
                p.integrity+=n
            else:
                s.pay(5)
                if not s.full_host(p.host) or p.integrity<=0:
                    s.stop='Unresolved timing: construction payment damaged its host through a deficit'
                    s.record('unsupported_construction_timing');return
                if kind=='upgrade':p.upgraded=True;p.completed=False;p.maximum*=2
                p.integrity+=1
                if p.integrity==p.maximum:p.completed=True
    s.validate()

# Policies are preferences within a shared planner, not fixed action scripts.
POLICIES={
 'adaptive':(1.,1.,1.,1.),
 'ground_doctrine':(1.5,.7,1.,.8),
 'naval_doctrine':(.9,1.6,.8,.9),
 'industrial':(.7,.8,1.5,1.2),
 'personnel_preservation':(.8,1.,1.,1.8),
 'opportunist':(1.5,1.2,.6,.8),
}

def value(s,policy,remaining):
    aggression,naval,economy,caution=POLICIES[policy]
    si,mi,up=s.income();future=min(5,max(0,remaining)/3)
    # Diminishing resource value, increasing scarcity cost near deficit; both military units valued.
    resource=2.5*math.sqrt(s.supply)+2.5*math.sqrt(s.manpower)
    shortage=caution*(max(0,7-s.supply)*1.8+max(0,5-s.manpower)*1.3+16*len(s.deficits))
    fs=sum(f.strength for f in s.fleets)
    score=resource-shortage+naval*fs*1.2+aggression*s.captures*16
    score+=economy*future*((si-up)*1.1+(mi-up)*.8)
    for p in s.projects:
        if p.integrity>0 and not p.active:
            _,sp,mp=PROFILES[p.profile]
            score+=economy*(sp+mp)*p.integrity/p.maximum*min(future,3)
    # Threat, deployment and target progress are evaluated against current enemy state.
    for system,enemy in s.enemies.items():
        targets=[w for w in s.worlds if w.system==system and not w.owned]
        own=sum(f.strength for f in s.fleets if f.system==system)
        if targets:
            progress=sum(w.maximum-w.defence for w in targets)
            score+=aggression*progress*3
            score-=naval*sum(enemy)*.65
            score+=min(own, sum(enemy)+5)*.7
            if own>sum(enemy):score+=naval*2
            # Remaining resource thresholds affect exact AI combat chance, not raw stocks alone.
            w=min(targets,key=lambda w:w.defence/w.maximum)
            if own:
                res={1:40,2:60,3:80}[w.tier]*w.defence/w.maximum
                score+=aggression*8*win_probability(own+s.supply+s.manpower, sum(enemy)+2*res)
    if s.stop:score-=150
    return score

def choose(s,phase,policy,remaining,decision,depth=2):
    actions=legal(s,phase)
    if len(actions)==1:return actions[0]
    # Common private planning draws across alternatives; no access to realised future dice.
    rng=random.Random(910000+decision)
    draws=[(rng.randint(1,20),rng.randint(1,20)) for _ in range(4)]
    ranked=[]
    for action in actions:
        scores=[]
        for roll in (draws if action[0] in ('battle','assault') else [draws[0]]):
            trial=copy.deepcopy(s,{id(s.trace):[]});trial.trace=[]
            apply(trial,action,random.Random(0),forced=roll)
            scores.append(value(trial,policy,remaining))
        mean=statistics.mean(scores)
        # Risk preference penalises downside, not only mean.
        score=mean-POLICIES[policy][3]*.12*(max(scores)-min(scores))
        ranked.append((score,action))
    ranked.sort(key=lambda x:x[0],reverse=True)
    if depth<=1:return ranked[0][1]
    # Beam lookahead considers a second action/next phase and next Logistics solvency.
    best=None
    for initial,action in ranked[:4]:
        trial=copy.deepcopy(s,{id(s.trace):[]});trial.trace=[];apply(trial,action,random.Random(0),forced=draws[0])
        next_phase='faction' if phase=='fleet' else ('construction' if phase=='faction' else None)
        if phase=='fleet' and action[0]!='none' and len(legal(trial,'fleet'))>1:next_phase='fleet'
        if next_phase:
            reply=choose(trial,next_phase,policy,remaining,decision+100000,1)
            apply(trial,reply,random.Random(0),forced=draws[1])
        score=.6*initial+.4*value(trial,policy,remaining)
        if best is None or score>best[0]:best=(score,action)
    return best[1]

def run_trial(seed,policy,trait,cycles=36,start=20,layout='matched',**switches):
    s=fixture(trait,start,layout,**switches)
    events=random.Random(seed) # identical event tape across variants despite differing combat counts
    combat=random.Random(seed+1000000)
    stocks=[];decision=0
    for _ in range(cycles):
        s.opening(events)
        if s.stop:break
        for _ in range(len(s.fleets)+1):
            a=choose(s,'fleet',policy,cycles-s.cycle,decision);decision+=1
            if a[0]=='none':break
            apply(s,a,combat)
            if s.stop:break
        if s.stop:break
        for phase in ('faction','construction'):
            a=choose(s,phase,policy,cycles-s.cycle,decision);decision+=1;apply(s,a,combat)
        s.closing();stocks.append((s.supply,s.manpower))
        if all(w.owned for w in s.worlds):break
    row={'seed':seed,'policy':policy,'trait':trait,'cycles':s.cycle,'captures':s.captures,'first_capture':s.first_capture or None,'supply':s.supply,'manpower':s.manpower,'supply_spent':s.spent['supply'],'manpower_spent':s.spent['manpower'],'supply_range':max((x[0] for x in stocks),default=0)-min((x[0] for x in stocks),default=0),'manpower_range':max((x[1] for x in stocks),default=0)-min((x[1] for x in stocks),default=0),'deficits':sum(v for k,v in s.counts.items() if k.startswith('deficit_')),'active_buildings':sum(p.active for p in s.projects),'stopped':s.stop,'actions':s.counts}
    return row,s.trace

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--seeds',type=int,default=8);parser.add_argument('--cycles',type=int,default=24);parser.add_argument('--out',default='balance-results');args=parser.parse_args()
    out=Path(args.out);out.mkdir(exist_ok=True)
    variants={'baseline':{},'expand_mp1':{'expand_mp':1},'create_mp2_expand_mp1':{'create_mp':2,'expand_mp':1}}
    rows=[]
    for variant,switches in variants.items():
        for policy,trait,seed in product(POLICIES,('siege','efficient','mobile'),range(args.seeds)):
            row,trace=run_trial(seed,policy,trait,args.cycles,**switches);row['variant']=variant;rows.append(row)
            if seed==0:(out/f'{variant}-{policy}-{trait}-trace.json').write_text(json.dumps(trace,indent=2))
        print(variant,'complete',flush=True)
    (out/'trials.json').write_text(json.dumps(rows,indent=2))
    keys=[k for k in rows[0] if k!='actions']
    with (out/'trials.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows({k:r[k] for k in keys} for r in rows)
    manifest={'seeds':args.seeds,'cycles':args.cycles,'policies':list(POLICIES),'variants':variants,'scenario':'matched three-system static-Minor frontier; 20/20 start','engine_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path('Source_Rules.md').read_bytes()).hexdigest(),'limitations':['No Major-vs-Major strategy or diplomacy','No Soulstorm outcome prediction','Raid-cycle ground assaults deferred, not adjudicated','Four economic construction profiles only; no combat structures','Stops on Mobile Capital loss rather than fabricating relocation','One static Minor faction per system; synthetic matched map','AI ground tie favours defender; fleet tie no damage','AI defender no Supply debit baseline; alternative switch available','Planning utility/preferences and bounded lookahead are modelling assumptions']}
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print('Trials:',len(rows),flush=True)

if __name__=='__main__':main()
