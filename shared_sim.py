"""Shared-Major integration laboratory. Experimental, incomplete rules coverage.
Run python shared_sim.py --seeds 4 --cycles 18 --out shared-results
"""
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import argparse, copy, hashlib, json, math, random
from balance_sim import State, Fleet, World, Project, legal, apply, fleet_losses

@dataclass
class Holding:
    tier: int
    defence: int
    maximum: int
    system: int
    owner: int
    attacked: bool = False
    defended: bool = False

class Arena:
    def __init__(self, start=20, expand_mp=0, create_mp=1, rotation=0):
        self.players=[State(supply=start,manpower=start,trait=t,expand_mp=expand_mp,create_mp=create_mp) for t in ('siege','efficient','mobile')]
        self.holdings=[Holding(4,12,12,0,0),Holding(2,4,4,0,0),Holding(4,12,12,1,1),Holding(2,4,4,1,1),Holding(2,4,4,2,2),Holding(1,2,2,2,2)]
        self.players[0].fleets=[Fleet(5,system=0),Fleet(5,system=0)]
        self.players[1].fleets=[Fleet(5,system=1),Fleet(5,system=1)]
        self.players[2].fleets=[Fleet(12,12,2,mobile=True),Fleet(5,system=2)]
        self.cycle=0;self.event=0;self.log=[];self.stop='';self.rotation=rotation
        self.defender_supply_cost=False
        for p in range(3):self.refresh(p)

    def refresh(self,p):
        s=self.players[p]
        s.worlds=[World(w.tier,w.defence,w.maximum,w.system,w.owner==p,w.attacked) for w in self.holdings]
        s.event=self.event;s.cycle=self.cycle

    def commit_owned(self,p):
        for w,v in zip(self.holdings,self.players[p].worlds):
            if w.owner==p:w.defence=v.defence

    def strength(self,p,system):
        return sum(f.strength for f in self.players[p].fleets if f.system==system)

    def opening(self,rng):
        self.cycle+=1
        for w in self.holdings:w.attacked=False
        # One shared event roll, after every player's Logistics. No player turn intervenes.
        for p,s in enumerate(self.players):
            self.refresh(p)
            for f in s.fleets:f.used=False
            if self.cycle%3==0:
                si,mi,up=s.income();s.change('supply',si);s.change('manpower',mi)
                s.change('supply',-up);s.change('manpower',-up)
                self.log.append(dict(cycle=self.cycle,player=p,action='logistics',income=[si,mi],upkeep=up))
        check=rng.randint(1,6);self.event=rng.randint(1,6) if check in (1,6) else 0
        self.log.append(dict(cycle=self.cycle,action='event',check=check,table=self.event))
        for s in self.players:
            s.event=self.event
            if self.event==1:
                for i,f in enumerate(s.fleets):
                    if f.strength:s.hit_fleet(i,1)
            elif self.event in (3,4):
                for r in ('supply','manpower'):s.change(r,-5 if self.event==3 else 5)
        self.check()

    def begin_turn(self,p):
        self.players[p].fleet_battled.clear()
        for w in self.holdings:
            if w.owner==p:w.defended=False
        self.refresh(p)

    def actions(self,p,phase):
        self.refresh(p);s=self.players[p]
        if self.stop:return [('none',)]
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
                for wi,w in enumerate(self.holdings):
                    if w.system!=system or w.owner==p:continue
                    if not hostile and w.defence>1 and s.afford(w.tier*2):actions.append(('bombard_shared',group,wi))
                    if self.event!=5 and s.afford(w.tier,damage):actions.append(('ground',group,wi))
        return actions

    def act(self,p,a,rng,forced=None):
        if a[0]=='none':return
        self.refresh(p);s=self.players[p];kind=a[0]
        self.log.append(dict(cycle=self.cycle,player=p,action=kind,order=a))
        if kind not in ('naval','ground','bombard_shared'):
            apply(s,a,rng);self.commit_owned(p)
            if kind=='defend' and a[1]>=0:self.holdings[a[1]].defended=True
            self.check();return
        group=a[1]
        for i in group:s.fleets[i].used=True
        if kind=='naval':
            system,q=a[2:];d=self.players[q]
            s.fleet_battled.add(system)
            defenders=[i for i,f in enumerate(d.fleets) if f.strength>0 and f.system==system]
            initiator=max((i for i in group if s.fleets[i].strength>1),key=lambda i:(not s.fleets[i].mobile,s.fleets[i].strength,-i))
            s.fleets[initiator].strength-=1
            rolls=forced or (rng.randint(1,20),rng.randint(1,20))
            margin=rolls[0]+sum(s.fleets[i].strength for i in group)-rolls[1]-sum(d.fleets[i].strength for i in defenders)
            if margin>0:
                for i in defenders:d.hit_fleet(i,fleet_losses(margin))
            elif margin<0:
                for i in group:s.hit_fleet(i,fleet_losses(-margin))
            self.log.append(dict(cycle=self.cycle,combat='naval',attacker=p,defender=q,rolls=rolls,margin=margin))
        else:
            wi=a[2];w=self.holdings[wi];q=w.owner;d=self.players[q]
            damage=max(1,sum(s.fleets[i].strength for i in group)//5);w.attacked=True
            if kind=='bombard_shared':
                s.pay(2*w.tier);actual=min(w.defence-1,damage)
            else:
                s.pay(w.tier,damage)
                # Inherited AI defender commitment convention; Supply ambiguity is a switch.
                commitment=damage//2
                isolated='manpower' in d.deficits or d.manpower<commitment
                if isolated:
                    commitment=0
                    self.log.append(dict(cycle=self.cycle,player=q,action='isolated_defense'))
                elif commitment:d.change('manpower',-commitment)
                if self.defender_supply_cost:d.change('supply',-min(d.supply,w.tier))
                av=sum(s.fleets[i].strength for i in group)+s.supply+s.manpower+(10 if self.event==6 else 0)
                dv=self.strength(q,w.system)+d.supply+d.manpower+(10 if self.event==2 else 0)+(15 if w.defended else 0)-(15 if isolated else 0)
                rolls=forced or (rng.randint(1,20),rng.randint(1,20));won=rolls[0]+av>rolls[1]+dv
                if won or isolated:s.change('manpower',math.floor(damage*.6))
                if not won:d.change('manpower',math.floor(commitment*.6))
                actual=damage if won else (1 if s.trait=='siege' else 0)
                self.log.append(dict(cycle=self.cycle,combat='ground',attacker=p,defender=q,rolls=rolls,totals=[rolls[0]+av,rolls[1]+dv],won=won))
            d.hit_host(wi,min(w.defence,actual));w.defence-=actual
            if w.defence<=0:
                w.defence=1;w.owner=p;w.defended=False;s.captures+=1
                for project in list(d.projects):
                    if project.host==wi and project.integrity>0:d.projects.remove(project);s.projects.append(project)
                for _ in range(actual):
                    eligible=[i for i,f in enumerate(d.fleets) if f.strength>0 and f.system==w.system]
                    if not eligible:break
                    i=max(eligible,key=lambda i:(d.fleets[i].strength,-i));d.hit_fleet(i,1)
                if w.tier==4:self.stop='Capital relocation is not implemented; captured capital terminates this integration scenario'
                if not any(h.owner==q for h in self.holdings) and not any(f.mobile and f.strength for f in d.fleets):
                    for i,f in enumerate(d.fleets):
                        if f.strength:d.hit_fleet(i,f.strength)
        self.check()

    def check(self):
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
        for roll in draws if a[0] in ('ground','naval') else draws[:1]:
            t=copy.deepcopy(arena);t.log=[]
            t.act(p,a,random.Random(0),roll);scores.append(utility(t,p,policy))
        score=sum(scores)/len(scores)-.15*(max(scores)-min(scores))
        if score>best[0]+1e-9:best=(score,a)
    return best[1]

def run(seed,cycles=18,start=20,rotation=0,expand_mp=0,create_mp=1):
    a=Arena(start,expand_mp,create_mp,rotation);events=random.Random(seed);combat=random.Random(seed+1000000)
    policies=['raider','industrial','fleet_control'];decision=0
    for _ in range(cycles):
        a.opening(events)
        if a.stop:break
        for p in [(i+rotation)%3 for i in range(3)]:
            a.begin_turn(p)
            for _ in range(len(a.players[p].fleets)+1):
                order=choose(a,p,'fleet',policies[p],decision);decision+=1
                if order[0]=='none':break
                a.act(p,order,combat)
                if a.stop:break
            if a.stop:break
            for phase in ('faction','construction'):
                order=choose(a,p,phase,policies[p],decision);decision+=1;a.act(p,order,combat)
                if a.stop:break
            if a.stop:break
        if a.stop:break
    counts={}
    for e in a.log:
        if 'action' in e:counts[e['action']]=counts.get(e['action'],0)+1
    return dict(seed=seed,cycles=a.cycle,rotation=rotation,start=start,stop=a.stop,actions=counts,
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
