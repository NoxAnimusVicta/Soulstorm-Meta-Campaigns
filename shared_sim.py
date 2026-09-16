"""Shared-Major integration laboratory. Experimental, incomplete rules coverage.
Run python shared_sim.py --seeds 4 --cycles 18 --out shared-results
"""
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import argparse, copy, hashlib, json, math, random
from balance_sim import State, Fleet, World, Project, legal, apply, fleet_losses
from construction_rules import PLANETARY, active, magnitude, legal_construction

@dataclass
class Holding:
    tier: int
    defence: int
    maximum: int
    system: int
    owner: int
    attacked: bool = False
    defended: bool = False

class SharedState(State):
    def yards(self):
        built={self.worlds[p.host].system for p in self.projects if p.host>=0 and p.profile=='shipyard' and p.active and self.worlds[p.host].owned}
        return self.established_yards | built | {f.system for f in self.fleets if f.mobile and f.strength>0}

    def income(self):
        si=mi=sum(w.tier for w in self.worlds if w.owned)+4*sum(f.mobile and f.strength>0 for f in self.fleets)
        for p in self.projects:
            if p.active:
                income={'depot':(2,0),'training':(0,2),'forge':(5,0),'academy':(0,5)}.get(p.profile,(0,0))
                factor=2 if p.upgraded else 1;si+=income[0]*factor;mi+=income[1]*factor
        return si,mi,sum(f.strength>0 and not f.mobile for f in self.fleets)

    def creation_strength(self,system):
        result=1
        for p in self.projects:
            if p.profile!='grand_shipyard' or not p.active:continue
            location=self.worlds[p.host].system if p.host>=0 else next((f.system for f in self.fleets if f.mobile and f.strength),None)
            if location==system:result=max(result,5 if p.upgraded else 3)
        return result

class Arena:
    def __init__(self, start=20, expand_mp=0, create_mp=1, rotation=0):
        self.players=[SharedState(supply=start,manpower=start,trait=t,expand_mp=expand_mp,create_mp=create_mp) for t in ('siege','efficient','mobile')]
        self.holdings=[Holding(4,12,12,0,0),Holding(2,4,4,0,0),Holding(4,12,12,1,1),Holding(2,4,4,1,1),Holding(2,4,4,2,2),Holding(1,2,2,2,2)]
        self.players[0].fleets=[Fleet(5,system=0),Fleet(5,system=0)]
        self.players[1].fleets=[Fleet(5,system=1),Fleet(5,system=1)]
        self.players[2].fleets=[Fleet(12,12,2,mobile=True),Fleet(5,system=2)]
        self.cycle=0;self.event=0;self.log=[];self.stop='';self.rotation=rotation
        self.defender_supply_cost=False
        self.capitals=[0,2,-1];self.provisional=[None,None,None]
        self.eliminated=set();self.mobile_loss_handled=set()
        self.mobile_defended=set()
        self.mobile_attacked=set();self.last_closed=-1
        for p in range(3):self.refresh(p)

    def refresh(self,p):
        s=self.players[p]
        s.worlds=[World(w.tier,w.defence,w.maximum,w.system,w.owner==p,w.attacked) for w in self.holdings]
        s.event=self.event;s.cycle=self.cycle
        c=self.capitals[p]
        s.established_yards={self.holdings[c].system} if c is not None and c>=0 and self.holdings[c].owner==p else set()
        s.capital_hosts={c} if c is not None else set()

    def commit_owned(self,p):
        for w,v in zip(self.holdings,self.players[p].worlds):
            if w.owner==p:w.defence=v.defence

    def strength(self,p,system):
        return sum(f.strength for f in self.players[p].fleets if f.system==system)

    def opening(self,rng):
        self.cycle+=1
        self.mobile_attacked.clear()
        for w in self.holdings:w.attacked=False
        # One shared event roll, after every player's Logistics. No player turn intervenes.
        for p,s in enumerate(self.players):
            if p in self.eliminated:continue
            self.refresh(p)
            for f in s.fleets:f.used=False
            if self.cycle%3==0:
                si,mi,up=s.income();s.change('supply',si);s.change('manpower',mi)
                s.change('supply',-up);s.change('manpower',-up)
                self.log.append(dict(cycle=self.cycle,player=p,action='logistics',income=[si,mi],upkeep=up))
        check=rng.randint(1,6);self.event=rng.randint(1,6) if check in (1,6) else 0
        self.log.append(dict(cycle=self.cycle,action='event',check=check,table=self.event))
        for p,s in enumerate(self.players):
            if p in self.eliminated:continue
            s.event=self.event
            if self.event==1:
                for i,f in enumerate(s.fleets):
                    if f.strength:s.hit_fleet(i,1)
            elif self.event in (3,4):
                for r in ('supply','manpower'):s.change(r,-5 if self.event==3 else 5)
        self.check()

    def begin_turn(self,p):
        self.players[p].fleet_battled.clear()
        self.mobile_defended.discard(p)
        for w in self.holdings:
            if w.owner==p:w.defended=False
        self.refresh(p)

    def closing(self):
        if self.last_closed==self.cycle:raise ValueError('Cycle already closed')
        self.last_closed=self.cycle
        for wi,w in enumerate(self.holdings):
            if w.attacked:continue
            s=self.players[w.owner]
            regen=magnitude(s,wi,'automated_defences')+magnitude(s,wi,'regenerative_fortifications',2)
            if regen:w.defence=min(w.maximum,w.defence+regen)
        for p,s in enumerate(self.players):
            if p in self.mobile_attacked:continue
            regen=magnitude(s,-1,'automated_defences')+magnitude(s,-1,'regenerative_fortifications',2)
            for f in s.fleets:
                if f.mobile and f.strength>0 and regen:f.strength=min(f.maximum,f.strength+regen)
        self.check()

    def actions(self,p,phase):
        self.refresh(p);s=self.players[p]
        if self.stop or p in self.eliminated:return [('none',)]
        if phase=='faction' and self.capitals[p] is None:
            # User ruling, 16 September: establish capital before rationing.
            host=self.provisional[p]
            return [('establish',i) for i,w in enumerate(self.holdings) if w.owner==p and (host is None or i==host)]
        if phase=='construction':return legal_construction(s,legal(s,phase))
        if phase=='faction':
            options=legal(s,phase)
            if not s.deficits:
                for i,project in enumerate(s.projects):
                    cost=1 if PLANETARY[project.profile].stages==3 else 3
                    if project.completed and 0<project.integrity<project.maximum and s.full_host(project.host) and s.afford(cost,cost):options.append(('defend_structure',i))
            return options
        if phase!='fleet':return legal(s,phase)
        actions=[('none',)]
        available=[i for i,f in enumerate(s.fleets) if f.strength>0 and not f.used]
        for i in available:
            f=s.fleets[i]
            if not f.mobile and f.strength<f.maximum and f.system in s.yards() and s.afford(1,s.expand_mp):actions.append(('expand',i))
            if self.event!=1:
                actions.extend(('move',i,k) for k in range(3) if k!=f.system)
        for system in range(3):
            here=[i for i in available if s.fleets[i].system==system]
            groups=[g for n in range(1,min(6,len(here))+1) for g in combinations(here[:6],n)]
            if len(here)>6:groups.append(tuple(here))
            hostile=[q for q in range(3) if q!=p and self.strength(q,system)>0]
            for group in groups:
                fs=sum(s.fleets[i].strength for i in group);damage=max(1,fs//5)
                if system not in s.fleet_battled and any(s.fleets[i].strength>1 for i in group):
                    actions.extend(('naval',group,system,q) for q in hostile)
                if self.event!=5 and s.afford(4,damage):
                    for q in hostile:
                        for fi,f in enumerate(self.players[q].fleets):
                            if f.mobile and f.strength>0 and f.system==system:
                                actions.append(('ground_mobile',group,q,fi))
                for wi,w in enumerate(self.holdings):
                    if w.system!=system or w.owner==p:continue
                    if not hostile and w.defence>1 and s.afford(w.tier*2):actions.append(('bombard_shared',group,wi))
                    if self.event!=5 and s.afford(w.tier,damage):actions.append(('ground',group,wi))
        return actions

    def act(self,p,a,rng,forced=None):
        if a[0]=='none':return
        self.refresh(p);s=self.players[p];kind=a[0]
        self.log.append(dict(cycle=self.cycle,player=p,action=kind,order=a))
        if kind=='defend_structure':
            if a not in self.actions(p,'faction'):raise ValueError('Illegal structure Defend')
            project=s.projects[a[1]];cost=1 if PLANETARY[project.profile].stages==3 else 3
            s.pay(cost,cost)
            if not s.full_host(project.host) or project.integrity<=0:
                s.stop='Unresolved timing: structure Defend payment damaged host through deficit'
            else:project.integrity=min(project.maximum,project.integrity+cost)
            self.check();return
        if kind=='start' and a[1] not in ('depot','training','forge','academy'):
            _,name,host=a
            if a not in self.actions(p,'construction'):raise ValueError('Illegal construction start')
            s.pay(5)
            if not s.full_host(host):
                s.stop='Unresolved timing: construction payment damaged its host through a deficit'
            else:s.projects.append(Project(name,host,maximum=PLANETARY[name].stages))
            self.check();return
        if kind=='establish':
            wi=a[1];w=self.holdings[wi];self.provisional[p]=wi
            w.maximum=min(12,w.maximum*2);w.defence=min(w.maximum,w.defence*2)
            if w.maximum==12:
                w.tier=4;self.capitals[p]=wi;self.provisional[p]=None
            self.check();return
        if kind not in ('naval','ground','ground_mobile','bombard_shared'):
            creation_strength=s.creation_strength(a[1]) if kind=='create' else None
            apply(s,a,rng);self.commit_owned(p)
            if creation_strength is not None:s.fleets[-1].strength=creation_strength
            if kind=='defend' and a[1]>=0:self.holdings[a[1]].defended=True
            if kind=='defend' and a[1]==-1:self.mobile_defended.add(p)
            self.check();return
        group=a[1]
        for i in group:s.fleets[i].used=True
        if kind=='naval':
            system,q=a[2:];d=self.players[q]
            s.fleet_battled.add(system)
            defenders=[i for i,f in enumerate(d.fleets) if f.strength>0 and f.system==system]
            if any(d.fleets[i].mobile for i in defenders):self.mobile_attacked.add(q)
            initiator=max((i for i in group if s.fleets[i].strength>1),key=lambda i:(not s.fleets[i].mobile,s.fleets[i].strength,-i))
            s.fleets[initiator].strength-=1
            rolls=forced or (rng.randint(1,20),rng.randint(1,20))
            margin=rolls[0]+sum(s.fleets[i].strength for i in group)-rolls[1]-sum(d.fleets[i].strength for i in defenders)
            if margin>0:
                if any(d.fleets[i].mobile for i in defenders):self.mobile_attacked.add(q)
                for i in defenders:d.hit_fleet(i,fleet_losses(margin))
            elif margin<0:
                if any(s.fleets[i].mobile for i in group):self.mobile_attacked.add(p)
                for i in group:s.hit_fleet(i,fleet_losses(-margin))
            self.log.append(dict(cycle=self.cycle,combat='naval',attacker=p,defender=q,rolls=rolls,margin=margin))
        else:
            mobile_target=kind=='ground_mobile'
            if mobile_target:
                q,fi=a[2:];d=self.players[q];target=d.fleets[fi];wi=-1
                self.mobile_attacked.add(q)
                w=Holding(4,target.strength,target.maximum,target.system,q,defended=q in self.mobile_defended)
            else:
                wi=a[2];w=self.holdings[wi];q=w.owner;d=self.players[q]
            damage=max(1,sum(s.fleets[i].strength for i in group)//5);w.attacked=True
            if kind=='bombard_shared':
                s.pay(2*w.tier);actual=min(w.defence-1,max(0,damage-magnitude(d,wi,'void_shield')))
            else:
                s.pay(w.tier,damage)
                # Inherited AI defender commitment convention; Supply ambiguity is a switch.
                militia=bool(active(d,wi,'militia'))
                commitment=0 if militia else damage//2
                isolated=not militia and ('manpower' in d.deficits or d.manpower<commitment)
                if isolated:
                    commitment=0
                    self.log.append(dict(cycle=self.cycle,player=q,action='isolated_defense'))
                elif commitment:d.change('manpower',-commitment)
                if self.defender_supply_cost:d.change('supply',-min(d.supply,w.tier))
                av=sum(s.fleets[i].strength for i in group)+s.supply+s.manpower+(10 if self.event==6 else 0)
                dv=self.strength(q,w.system)+d.supply+d.manpower+(10 if self.event==2 else 0)+(15 if w.defended else 0)-(15 if isolated else 0)+magnitude(d,wi,'bunker',5)
                rolls=forced or (rng.randint(1,20),rng.randint(1,20));won=rolls[0]+av>rolls[1]+dv
                if won or isolated:s.change('manpower',math.floor(damage*.6))
                if not won:d.change('manpower',math.floor(commitment*.6))
                actual=damage if won else (1 if s.trait=='siege' else 0)
                self.log.append(dict(cycle=self.cycle,combat='ground',attacker=p,defender=q,rolls=rolls,totals=[rolls[0]+av,rolls[1]+dv],won=won))
            if kind!='bombard_shared':actual=max(0,actual-magnitude(d,wi,'void_shield'))
            if mobile_target:
                d.hit_fleet(fi,actual)
                self.check();return
            d.hit_host(wi,min(w.defence,actual));w.defence-=actual
            if w.defence<=0:
                capital_lost=self.capitals[q]==wi
                penalty=4 if w.tier==4 else 2
                # Baseline AI defender Supply debit is zero; Planet Fall replaces it.
                d.change('supply',-penalty);d.change('manpower',-penalty)
                w.defence=1;w.owner=p;w.defended=False;s.captures+=1
                if capital_lost:self.capitals[q]=None
                if self.provisional[q]==wi:self.provisional[q]=None
                for project in list(d.projects):
                    if project.host==wi and project.integrity>0:d.projects.remove(project);s.projects.append(project)
                for _ in range(actual):
                    eligible=[i for i,f in enumerate(d.fleets) if f.strength>0 and f.system==w.system]
                    if not eligible:break
                    i=max(eligible,key=lambda i:(d.fleets[i].strength,-i));d.hit_fleet(i,1)
                if not any(h.owner==q for h in self.holdings) and not any(f.mobile and f.strength for f in d.fleets):
                    for i,f in enumerate(d.fleets):
                        if f.strength:d.hit_fleet(i,f.strength)
        self.check()

    def check(self):
        # Resolve mobile-capital loss once, including losses caused by deficits.
        for p,s in enumerate(self.players):
            if p not in self.mobile_loss_handled and any(f.mobile and f.strength==0 for f in s.fleets):
                self.mobile_loss_handled.add(p);self.capitals[p]=None;s.trait='none'
                if s.stop.startswith('Mobile Capital destroyed:'):s.stop=''
                s.change('supply',-4);s.change('manpower',-4)
                self.log.append(dict(cycle=self.cycle,player=p,action='mobile_capital_lost'))
            if p not in self.eliminated and not any(w.owner==p for w in self.holdings) and not any(f.mobile and f.strength for f in s.fleets):
                self.eliminated.add(p);self.capitals[p]=None
                for i,f in enumerate(s.fleets):
                    if f.strength:s.hit_fleet(i,f.strength)
                self.log.append(dict(cycle=self.cycle,player=p,action='eliminated'))
        for p,s in enumerate(self.players):
            self.refresh(p);s.validate()
            if s.stop:self.stop=s.stop
        assert all(w.owner in range(3) for w in self.holdings)

# Distinct tactical priorities, still heuristic bots, not validated human substitutes.
# Each compares sampled consequences and threat to its own holdings.
def utility(arena,p,policy):
    s=arena.players[p];si,mi,up=s.income()
    capture_weight={'raider':28,'industrial':14,'fleet_control':18}[policy]
    score=2*math.sqrt(s.supply)+2*math.sqrt(s.manpower)-25*len(s.deficits)
    score+=capture_weight*sum(w.tier for w in arena.holdings if w.owner==p)
    score+=sum(f.strength for f in s.fleets)*1.4
    score+=(3 if policy=='industrial' else 1)*(si+mi-2*up)
    for project in s.projects:
        score+=project.integrity*(2 if policy=='industrial' else .5)
    for system in range(3):
        own=arena.strength(p,system);enemy=sum(arena.strength(q,system) for q in range(3) if q!=p)
        holdings=[w for w in arena.holdings if w.system==system and w.owner==p]
        targets=[w for w in arena.holdings if w.system==system and w.owner!=p]
        score-=max(0,enemy-own)*(.7 if holdings else .1)
        if targets:
            score+=sum(w.maximum-w.defence for w in targets)*(4 if policy=='raider' else 1)
            score+=min(own,enemy+10)*(.9 if policy=='raider' else .5)
            if policy=='fleet_control':score-=enemy*1.2
    if arena.stop:score-=20 # Terminal unsupported paths are reported, not assigned a win.
    return score

def choose(arena,p,phase,policy,decision):
    actions=arena.actions(p,phase)
    best=(-float('inf'),actions[0])
    rng=random.Random(900000+decision);draws=[(rng.randint(1,20),rng.randint(1,20)) for _ in range(3)]
    for a in actions:
        scores=[]
        for roll in draws if a[0] in ('ground','ground_mobile','naval') else draws[:1]:
            t=copy.deepcopy(arena);t.log=[]
            t.act(p,a,random.Random(0),roll);scores.append(utility(t,p,policy))
        score=sum(scores)/len(scores)-.15*(max(scores)-min(scores))
        if score>best[0]+1e-9:best=(score,a)
    return best[1]

def run(seed,cycles=18,start=20,rotation=0,expand_mp=0,create_mp=1,planner_depth=0,policy_rotation=0):
    a=Arena(start,expand_mp,create_mp,rotation);events=random.Random(seed);combat=random.Random(seed+1000000)
    base=['raider','industrial','fleet_control'];policies=base[policy_rotation:]+base[:policy_rotation];decision=0
    def select(p,phase):
        nonlocal decision
        if planner_depth:
            from strategic_planner import plan
            order=plan(a,p,phase,policies,decision,planner_depth)
        else:order=choose(a,p,phase,policies[p],decision)
        decision+=1
        return order
    for _ in range(cycles):
        a.opening(events)
        if a.stop:break
        for p in [(i+rotation)%3 for i in range(3)]:
            if p in a.eliminated:continue
            a.begin_turn(p)
            for _ in range(len(a.players[p].fleets)+1):
                order=select(p,'fleet')
                if order[0]=='none':break
                a.act(p,order,combat)
                if a.stop:break
            if a.stop:break
            for phase in ('faction','construction'):
                order=select(p,phase);a.act(p,order,combat)
                if a.stop:break
            if a.stop:break
        if a.stop:break
        a.closing()
    counts={}
    for e in a.log:
        if 'action' in e:counts[e['action']]=counts.get(e['action'],0)+1
    return dict(seed=seed,cycles=a.cycle,rotation=rotation,policy_rotation=policy_rotation,planner_depth=planner_depth,start=start,stop=a.stop,actions=counts,
        players=[dict(supply=s.supply,manpower=s.manpower,holdings=sum(w.owner==p for w in a.holdings),strength=sum(f.strength for f in s.fleets),deficits=s.deficits,deficit_entries=sum(v for k,v in s.counts.items() if k.startswith('deficit_'))) for p,s in enumerate(a.players)]),a.log

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--seeds',type=int,default=4);parser.add_argument('--cycles',type=int,default=18);parser.add_argument('--out',default='shared-results');args=parser.parse_args()
    out=Path(args.out);out.mkdir(exist_ok=True);rows=[]
    for start in (6,20):
        for rotation in range(3):
            for seed in range(args.seeds):
                row,trace=run(seed,args.cycles,start,rotation);rows.append(row)
                (out/f'trace-{start}-{rotation}-{seed}.json').write_text(json.dumps(trace,indent=2))
        print('Starting resources',start,'finished',flush=True)
    (out/'trials.json').write_text(json.dumps(rows,indent=2))
    (out/'manifest.json').write_text(json.dumps(dict(engine_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),core_sha256=hashlib.sha256(Path('balance_sim.py').read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path('Source_Rules.md').read_bytes()).hexdigest(),seeds=args.seeds,cycles=args.cycles,classification='integration experiments, not balance certification',limitations=['Synthetic asymmetrical Major-only map','Three heuristic policies, no multi-turn search yet','No diplomacy or consent model; all opponents hostile','No direct mobile capital ground targeting','Four economic construction profiles only','Raid assaults omitted','Capital loss explicitly stops trial','Defender Supply debit disabled; AI tie favours defender','Turn order rotated, but policy/trait/map assignments not rotated','No human Soulstorm outcome model']),indent=2))
    print('Trials',len(rows),'stopped',sum(bool(r['stop']) for r in rows),flush=True)

if __name__=='__main__':main()
