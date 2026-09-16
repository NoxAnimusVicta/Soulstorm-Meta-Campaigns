"""Shared-Major integration laboratory. Experimental, incomplete rules coverage.
Run python shared_sim.py --seeds 4 --cycles 18 --out shared-results
"""
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import argparse, copy, hashlib, json, math, random
from balance_sim import State, Fleet, World, Project, legal, apply, fleet_losses
from construction_rules import PLANETARY, CATALOG, active, magnitude, legal_construction, construct
from battle_setup import BattleSide, setup as soulstorm_setup

class PendingBattle(Exception):
    def __init__(self,setup):
        self.setup=setup
        super().__init__('Awaiting reported Soulstorm battle result')

class PendingAllocation(Exception):
    def __init__(self,point,candidates):
        self.point=point;self.candidates=candidates
        super().__init__('Attacker must choose tied Major fleet damage allocation')

@dataclass
class Holding:
    tier: int
    defence: int
    maximum: int
    system: int
    owner: int
    attacked: bool = False
    defended: bool = False
    station: bool = False
    capacity_bonus: int = 0

class SharedState(State):
    role='major'
    alignment='Independent'

    def change(self,resource,delta):
        if self.role=='minor':return
        super().change(resource,delta)

    def full_host(self,host):
        if isinstance(host,tuple):
            kind,i=host
            if kind=='system':return i in self.present_systems
            f=self.fleets[i];return f.strength>0 and f.strength==f.maximum
        return super().full_host(host)

    def host_system(self,host):
        if isinstance(host,tuple):return host[1] if host[0]=='system' else self.fleets[host[1]].system
        if host==-1:return next((f.system for f in self.fleets if f.mobile and f.strength>0),None)
        return self.worlds[host].system

    def hit_fleet(self,index,damage):
        before=self.fleets[index].strength
        super().hit_fleet(index,damage)
        self.hit_host(('fleet',index),min(before,damage))
        if self.fleets[index].strength==0:
            for p in self.projects:
                if p.host==('fleet',index):p.integrity=0

    def hit_host(self,host,damage):
        for project in self.projects:
            if project.host!=host or project.integrity<=0:continue
            # Completed strength conversions remain part of the fleet.
            # An unfinished upgrade can lose only its new progress.
            floor=getattr(project,'permanent_integrity',0)
            project.integrity=max(floor,project.integrity-damage)

    def yards(self):
        built={self.host_system(p.host) for p in self.projects if p.profile in ('shipyard','grand_shipyard') and p.active}
        return self.established_yards | built | {f.system for f in self.fleets if f.mobile and f.strength>0}

    def income(self):
        si=mi=sum(w.tier for w in self.worlds if w.owned)+4*sum(f.mobile and f.strength>0 for f in self.fleets)
        for p in self.projects:
            if p.active:
                income={'depot':(2,0),'training':(0,2),'forge':(5,0),'academy':(0,5)}.get(p.profile,(0,0))
                factor=2 if p.upgraded else 1;si+=income[0]*factor;mi+=income[1]*factor
        if self.trait=='war_economy':si+=3
        if self.trait=='martial':mi+=5
        return si,mi,sum(f.strength>0 and not f.mobile for f in self.fleets)

    def creation_strength(self,system):
        result=3 if self.trait=='swift' else 1
        for p in self.projects:
            if p.profile!='grand_shipyard' or not p.active:continue
            location=self.host_system(p.host)
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
        self.defender_supply_cost=True
        self.capitals=[0,2,-1];self.provisional=[None,None,None]
        self.eliminated=set();self.mobile_loss_handled=set()
        self.mobile_defended=set()
        self.mobile_attacked=set();self.last_closed=-1
        self.fleet_combat=set();self.engaged_factions=set()
        self.alliances=set();self.consents=set();self.turn_order=list(range(len(self.players)))
        self.phase_spent=set();self.phase_position={}
        self.defence_choices={}
        self.human_players=set();self.reported_outcomes={}
        self.intel_choices={}
        self.planetfall_choices={}
        self.messages=[]
        for p in range(3):self.refresh(p)

    def refresh(self,p):
        s=self.players[p]
        s.worlds=[World(w.tier,w.defence,w.maximum,w.system,w.owner==p,w.attacked) for w in self.holdings]
        s.event=self.event;s.cycle=self.cycle
        c=self.capitals[p]
        s.established_yards={self.holdings[c].system} if c is not None and c>=0 and self.holdings[c].owner==p else set()
        s.capital_hosts={c} if c is not None else set()
        s.present_systems={w.system for w in s.worlds if w.owned}|{f.system for f in s.fleets if f.strength>0}

    @property
    def systems(self):return sorted({w.system for w in self.holdings}|{f.system for s in self.players for f in s.fleets})

    def allied(self,p,q):
        alignment=self.players[p].alignment
        return p==q or frozenset((p,q)) in self.alliances or (alignment!='Independent' and alignment==self.players[q].alignment)

    def void(self,p,system):
        friendly=sum(self.strength(q,system) for q in range(len(self.players)) if self.allied(p,q))
        hostile=sum(self.strength(q,system) for q in range(len(self.players)) if not self.allied(p,q))
        return friendly>hostile

    def fleet_effect(self,p,group,name,base=1):
        return sum(magnitude(self.players[q],('fleet',i),name,base) for q,i in (self.fleet_ref(p,x) for x in group))

    def fleet_ref(self,p,reference):return reference if isinstance(reference,tuple) else (p,reference)

    def participating_strength(self,p,group):
        return sum(self.players[q].fleets[i].strength for q,i in (self.fleet_ref(p,x) for x in group))

    def grant_support(self,owner,beneficiary,indices):
        if owner==beneficiary or not self.allied(owner,beneficiary):raise ValueError('Support requires distinct allied factions')
        for fi in indices:
            fleet=self.players[owner].fleets[fi]
            if fleet.strength<=0 or fleet.used:raise ValueError('Fleet action unavailable for support')
        self.consents.update((owner,fi,beneficiary) for fi in indices)

    def ground_strength(self,p,group):
        return self.participating_strength(p,group)+self.fleet_effect(p,group,'assault_boats',2)+self.fleet_effect(p,group,'carrier',5)

    def assault_affordable(self,p,group,defender,host,tier):
        damage=magnitude(self.players[defender],host,'orbital_cannons')
        projected=self
        if damage:
            projected=copy.deepcopy(self)
            owner,fi=max((self.fleet_ref(p,x) for x in group),key=lambda ref:self.players[ref[0]].fleets[ref[1]].strength)
            projected.players[owner].hit_fleet(fi,damage)
        if projected.participating_strength(p,group)==0:return True
        return projected.players[p].afford(tier,max(1,projected.ground_strength(p,group)//5))

    def commit_owned(self,p):
        for w,v in zip(self.holdings,self.players[p].worlds):
            if w.owner==p:w.defence=v.defence

    def strength(self,p,system):
        return sum(f.strength for f in self.players[p].fleets if f.system==system)

    def minor_resources(self,wi):
        w=self.holdings[wi]
        if self.players[w.owner].role!='minor':raise ValueError('Not a Minor holding')
        base={1:40,2:60,3:80}[w.tier]
        value=base*w.defence/w.maximum
        return value,value

    def add_minor(self,worlds,alignment='Independent'):
        """Add static holdings (tier, defence, maximum, system, station)."""
        if not worlds or any(w[0] not in (1,2,3) for w in worlds):raise ValueError('Minor requires non-capital holdings')
        p=len(self.players);s=SharedState(trait='none');s.role='minor';s.alignment=alignment
        s.fleets=[];self.players.append(s);self.capitals.append(None);self.provisional.append(None)
        for tier,defence,maximum,system,station in worlds:
            self.holdings.append(Holding(tier,defence,maximum,system,p,station=station))
        for system in sorted({w[3] for w in worlds}):
            remaining=sum(w[1] for w in worlds if w[3]==system)
            while remaining:
                strength=min(5,remaining);s.fleets.append(Fleet(strength,strength,system));remaining-=strength
        self.refresh(p)
        return p

    def opening(self,rng):
        self.cycle+=1
        self.mobile_attacked.clear()
        self.fleet_combat.clear();self.engaged_factions.clear();self.consents.clear()
        self.phase_spent.clear();self.phase_position.clear()
        for w in self.holdings:w.attacked=False
        # One shared event roll, after every player's Logistics. No player turn intervenes.
        for p,s in enumerate(self.players):
            if p in self.eliminated:continue
            self.refresh(p)
            for f in s.fleets:f.used=False
            if self.cycle%3==0 and s.role=='major':
                si,mi,up=s.income();s.change('supply',si);s.change('manpower',mi)
                s.change('supply',-up);s.change('manpower',-up)
                self.log.append(dict(cycle=self.cycle,player=p,action='logistics',income=[si,mi],upkeep=up))
                if s.trait=='endurance':
                    for f in s.fleets:
                        if f.strength>0:f.strength=min(f.maximum,f.strength+1)
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
        # Snapshot active emplacements before applying simultaneous system fire.
        system_fire=[]
        for q,s in enumerate(self.players):
            for fi,f in enumerate(s.fleets):
                damage=sum(magnitude(other,('system',f.system),'system_defence') for p,other in enumerate(self.players) if not self.allied(p,q))
                if f.strength and damage:system_fire.append((q,fi,damage))
        for q,fi,damage in system_fire:self.players[q].hit_fleet(fi,damage)
        self.check()
        for wi,w in enumerate(self.holdings):
            if w.attacked:continue
            s=self.players[w.owner]
            regen=magnitude(s,wi,'automated_defences')+magnitude(s,wi,'regenerative_fortifications',2)
            if s.role=='minor':regen+=1
            regen+=sum(magnitude(other,('system',w.system),'logistics_anchorage') for q,other in enumerate(self.players) if self.allied(w.owner,q))
            if regen:w.defence=min(w.maximum,w.defence+regen)
        for p,s in enumerate(self.players):
            if s.role=='minor' and p not in self.engaged_factions:
                eligible=[f for f in s.fleets if 0<f.strength<f.maximum]
                if eligible:max(eligible,key=lambda f:f.strength).strength+=1
            for i,f in enumerate(s.fleets):
                if not f.strength:continue
                repair=sum(magnitude(other,('system',f.system),'system_repair') for q,other in enumerate(self.players) if self.allied(p,q))
                if (p,i) not in self.fleet_combat:repair+=magnitude(s,('fleet',i),'repair_tender')
                f.strength=min(f.maximum,f.strength+repair)
            if p in self.mobile_attacked:continue
            regen=magnitude(s,-1,'automated_defences')+magnitude(s,-1,'regenerative_fortifications',2)
            for f in s.fleets:
                if f.mobile and f.strength>0 and regen:f.strength=min(f.maximum,f.strength+regen)
        self.check()

    def actions(self,p,phase,allow_scout=True):
        self.refresh(p);s=self.players[p]
        if self.stop or p in self.eliminated or s.role=='minor':return [('none',)]
        if phase=='social':
            options=[('none',)]
            for q in range(len(self.players)):
                if q==p or q in self.eliminated:continue
                self.refresh(q)
                if s.present_systems & self.players[q].present_systems:options.append(('communique',q,'Request a diplomatic exchange.'))
            return options
        if phase=='faction' and self.capitals[p] is None:
            # User ruling, 16 September: establish capital before rationing.
            host=self.provisional[p]
            return [('establish',i) for i,w in enumerate(self.holdings) if w.owner==p and not w.station and (host is None or i==host)]
        if phase=='construction':return legal_construction(s)
        if phase=='faction':
            options=legal(s,phase)
            if not s.deficits:
                for ri,recipient in enumerate(self.holdings):
                    if recipient.owner!=p or recipient.defence==recipient.maximum:continue
                    plan=[];remaining=recipient.maximum-recipient.defence
                    for di,donor in enumerate(self.holdings):
                        if donor.owner!=p or di==ri or donor.system!=recipient.system or donor.defence<=1:continue
                        if donor.defence!=donor.maximum and not active(s,ri,'landing_zones'):continue
                        for amount in range(1,min(donor.defence-1,recipient.maximum-recipient.defence)+1):
                            options.append(('garrison',((di,ri,amount),)))
                        amount=min(donor.defence-1,remaining)
                        if amount:plan.append((di,ri,amount));remaining-=amount
                    if len(plan)>1:options.append(('garrison',tuple(plan)))
                for i,project in enumerate(s.projects):
                    cost=1 if CATALOG[project.profile].stages==3 else 3
                    if project.completed and 0<project.integrity<project.maximum and s.full_host(project.host) and s.afford(cost,cost):options.append(('defend_structure',i))
            return options
        if phase!='fleet':return legal(s,phase)
        actions=[('none',)]
        available=[i for i,f in enumerate(s.fleets) if f.strength>0 and not f.used]
        for i in available:
            f=s.fleets[i]
            if not f.mobile:
                actions.extend(('merge',i,j) for j,other in enumerate(s.fleets) if j!=i and not other.mobile and other.strength>0 and other.system==f.system)
            if self.void(p,f.system):actions.append(('scuttle',i))
            if not f.mobile and f.maximum==5 and self.void(p,f.system):
                for j,recipient in enumerate(s.fleets):
                    if i==j or recipient.mobile or recipient.maximum!=5 or recipient.strength<=0 or recipient.system!=f.system:continue
                    actions.extend(('transfer',i,j,n) for n in range(1,min(f.strength-1,5-recipient.strength)+1))
            if not f.mobile and f.strength<f.maximum and f.system in s.yards() and s.afford(0 if s.trait=='void' else 1,s.expand_mp):actions.append(('expand',i))
            if self.event!=1:
                actions.extend(('move',i,k) for k in self.systems if k!=f.system)
                if allow_scout and active(s,('fleet',i),'scout'):
                    for destination in self.systems:
                        if destination==f.system:continue
                        hypothetical=copy.deepcopy(self)
                        hypothetical.players[p].fleets[i].system=destination
                        for attack in hypothetical.actions(p,'fleet',allow_scout=False):
                            if attack[0] in ('ground','ground_mobile','bombard_shared') and i in attack[1]:
                                actions.append(('scout_attack',i,destination,attack))
        for system in self.systems:
            here=[i for i in available if s.fleets[i].system==system]
            here.extend((q,fi) for q,fi,beneficiary in sorted(self.consents) if beneficiary==p and self.allied(p,q) and self.players[q].fleets[fi].strength>0 and not self.players[q].fleets[fi].used and self.players[q].fleets[fi].system==system)
            groups=[g for n in range(1,len(here)+1) for g in combinations(here,n)]
            hostile=[q for q in range(len(self.players)) if not self.allied(p,q) and self.strength(q,system)>0]
            for group in groups:
                fs=self.ground_strength(p,group);damage=max(1,fs//5)
                for q,d in enumerate(self.players):
                    if any(isinstance(i,tuple) for i in group):continue
                    if self.allied(p,q):continue
                    for pi,project in enumerate(d.projects):
                        if project.integrity<=0 or d.host_system(project.host)!=system:continue
                        if project.completed and getattr(project,'permanent_integrity',0):continue
                        guarded=self.strength(q,system)>0
                        if (guarded and any(s.fleets[i].strength>1 for i in group)) or (not hostile and s.afford(2)):
                            actions.append(('structure_assault',group,q,pi))
                if all(isinstance(i,int) for i in group) and system not in s.fleet_battled and any(s.fleets[i].strength>1 for i in group):
                    actions.extend(('naval',group,system,q) for q in hostile)
                if self.event!=5:
                    for q in hostile:
                        for fi,f in enumerate(self.players[q].fleets):
                            if f.mobile and f.strength>0 and f.system==system and self.assault_affordable(p,group,q,-1,4):
                                actions.append(('ground_mobile',group,q,fi))
                for wi,w in enumerate(self.holdings):
                    if w.system!=system or self.allied(p,w.owner):continue
                    if not hostile and w.defence>1 and s.afford(w.tier*2):actions.append(('bombard_shared',group,wi))
                    if self.event!=5 and self.assault_affordable(p,group,w.owner,wi,w.tier):actions.append(('ground',group,wi))
        return actions

    def submit(self,p,phase,a,rng,forced=None):
        """Validated public turn entry point; act remains a hypothetical resolver."""
        phases={'fleet':2,'faction':3,'social':4,'construction':5}
        if phase not in phases:raise ValueError('Unknown phase')
        if p in self.eliminated or self.players[p].role=='minor':raise ValueError('No active Major turn')
        if phases[phase]<self.phase_position.get(p,2):raise ValueError('Cannot return to an earlier phase')
        if (p,phase) in self.phase_spent:raise ValueError('Phase action already spent')
        options=self.actions(p,phase)
        if a[0]=='communique' and phase=='social':
            if not isinstance(a[2],str) or not a[2].strip():raise ValueError('Communique requires a message')
            if not any(x[0]=='communique' and x[1]==a[1] for x in options):raise ValueError('No shared system presence')
            options=options+[a]
        if a[0]=='garrison' and phase=='faction' and self.capitals[p] is not None and not self.players[p].deficits:
            self.validate_garrison(p,a[1])
        elif a not in options:raise ValueError('Illegal order for current phase and state')
        checkpoint=copy.deepcopy(self.__dict__)
        random_state=rng.getstate() if hasattr(rng,'getstate') else None
        try:self.act(p,a,rng,forced)
        except Exception:
            self.__dict__.clear();self.__dict__.update(checkpoint)
            if random_state is not None:rng.setstate(random_state)
            raise
        self.phase_position[p]=phases[phase]
        if phase!='fleet' or a[0]=='none':self.phase_spent.add((p,phase))

    def reply(self,recipient,message_id,text):
        message=self.messages[message_id]
        if message['recipient']!=recipient or message['cycle']!=self.cycle or message['reply'] is not None:raise ValueError('Reply unavailable')
        if not isinstance(text,str) or not text.strip():raise ValueError('Reply requires text')
        message['reply']=text
        self.log.append(dict(cycle=self.cycle,action='communique_reply',player=recipient,message_id=message_id))

    def validate_garrison(self,p,transfers):
        if not transfers:raise ValueError('Empty Garrison Transfer')
        totals={};outgoing={}
        for di,ri,amount in transfers:
            donor=self.holdings[di];recipient=self.holdings[ri]
            if di==ri or not isinstance(amount,int) or amount<=0:raise ValueError('Invalid garrison amount')
            if donor.owner!=p or recipient.owner!=p or donor.system!=recipient.system:raise ValueError('Garrison requires own holdings in the same system')
            if donor.defence!=donor.maximum and not active(self.players[p],ri,'landing_zones'):raise ValueError('Donor not fully defended')
            outgoing[di]=outgoing.get(di,0)+amount
            totals[di]=totals.get(di,0)-amount;totals[ri]=totals.get(ri,0)+amount
        for di,amount in outgoing.items():
            if self.holdings[di].defence-amount<1:raise ValueError('Donor must retain one defence')
        for wi,delta in totals.items():
            if not 1<=self.holdings[wi].defence+delta<=self.holdings[wi].maximum:raise ValueError('Garrison capacity exceeded')
        return totals

    def act(self,p,a,rng,forced=None):
        if a[0]=='none':return
        self.refresh(p);s=self.players[p];kind=a[0]
        self.log.append(dict(cycle=self.cycle,player=p,action=kind,order=a))
        if kind=='communique':
            self.messages.append(dict(sender=p,recipient=a[1],text=a[2],reply=None,cycle=self.cycle))
            return
        if kind=='garrison':
            for wi,delta in self.validate_garrison(p,a[1]).items():self.holdings[wi].defence+=delta
            self.check();return
        if kind=='merge':
            if a not in self.actions(p,'fleet'):raise ValueError('Illegal Fleet Merge')
            _,survivor,absorbed=a;target=s.fleets[survivor];donor=s.fleets[absorbed]
            bonus=sum(getattr(project,'granted_capacity',0) for project in s.projects if project.host==('fleet',absorbed))
            target.maximum+=bonus;target.strength=min(target.maximum,target.strength+donor.strength)
            target.used=True;donor.strength=0
            for project in s.projects:
                if project.host==('fleet',absorbed):project.host=('fleet',survivor)
            self.check();return
        if kind=='transfer':
            if a not in self.actions(p,'fleet'):raise ValueError('Illegal Fleet Transfer')
            _,donor,recipient,amount=a
            s.fleets[donor].strength-=amount;s.fleets[recipient].strength+=amount
            s.fleets[donor].used=True
            self.check();return
        if kind=='scuttle':
            if a not in self.actions(p,'fleet'):raise ValueError('Illegal Scuttle')
            fi=a[1];refund=s.fleets[fi].strength//2;s.fleets[fi].used=True
            s.hit_fleet(fi,s.fleets[fi].strength)
            s.change('supply',refund)
            self.check();return
        if kind=='scout_attack':
            if a not in self.actions(p,'fleet'):raise ValueError('Illegal Scout movement/attack')
            _,fi,destination,attack=a
            s.fleets[fi].system=destination
            self.act(p,attack,rng,forced)
            return
        if kind=='structure_assault':
            if a not in self.actions(p,'fleet'):raise ValueError('Illegal Structure Assault')
            group,q,pi=a[1:];d=self.players[q];project=d.projects[pi]
            system=d.host_system(project.host)
            defenders=[i for i,f in enumerate(d.fleets) if f.strength>0 and f.system==system]
            for i in group:s.fleets[i].used=True
            self.fleet_combat.update((p,i) for i in group);self.engaged_factions.add(p)
            if defenders:
                self.fleet_combat.update((q,i) for i in defenders);self.engaged_factions.add(q)
                initiator=max((i for i in group if s.fleets[i].strength>1),key=lambda i:(not s.fleets[i].mobile,s.fleets[i].strength,-i))
                s.fleets[initiator].strength-=1
                rolls=forced or (rng.randint(1,20),rng.randint(1,20))
                margin=rolls[0]+sum(s.fleets[i].strength for i in group)+self.fleet_effect(p,group,'escort',3)-rolls[1]-self.strength(q,system)-self.fleet_effect(q,defenders,'escort',3)-magnitude(d,('system',system),'defence_platform',5)
                if margin>0:project.integrity=max(getattr(project,'permanent_integrity',0),project.integrity-fleet_losses(margin))
                elif margin<0:
                    for i in group:s.hit_fleet(i,fleet_losses(-margin))
                self.log.append(dict(cycle=self.cycle,combat='structure',attacker=p,defender=q,rolls=rolls,margin=margin))
            else:
                s.pay(2)
                damage=max(1,sum(s.fleets[i].strength for i in group)//5)
                project.integrity=max(getattr(project,'permanent_integrity',0),project.integrity-damage)
            self.check();return
        if kind=='defend_structure':
            if a not in self.actions(p,'faction'):raise ValueError('Illegal structure Defend')
            project=s.projects[a[1]];cost=1 if CATALOG[project.profile].stages==3 else 3
            s.pay(cost,cost)
            if not s.full_host(project.host) or project.integrity<=0:
                s.stop='Unresolved timing: structure Defend payment damaged host through deficit'
            else:project.integrity=min(project.maximum,project.integrity+cost)
            self.check();return
        if kind in ('start','build','repair','upgrade'):
            if a not in self.actions(p,'construction'):raise ValueError('Illegal construction action')
            construct(s,a)
            project=s.projects[-1] if kind=='start' else s.projects[a[1]]
            if project.active and project.profile in ('assault_cruiser','flagship'):
                f=s.fleets[project.host[1]]
                capacity=(2 if project.profile=='assault_cruiser' else 5)*(2 if project.upgraded else 1)
                extra=capacity-getattr(project,'granted_capacity',0)
                f.maximum+=extra;f.strength+=extra
                project.granted_capacity=capacity;project.permanent_integrity=project.maximum
            if project.active and project.profile=='consolidation':
                w=self.holdings[project.host]
                w.tier+=1;w.defence*=2;w.maximum*=2
                s.projects.remove(project)
                self.log.append(dict(cycle=self.cycle,player=p,action='consolidated',holding=project.host,tier=w.tier))
            elif project.active and project.profile=='void_station':
                system=s.host_system(project.host)
                self.holdings.append(Holding(1,2,2,system,p,station=True))
                s.projects.remove(project)
                self.log.append(dict(cycle=self.cycle,player=p,action='station_completed',holding=len(self.holdings)-1))
            self.check();return
        if kind=='establish':
            wi=a[1];w=self.holdings[wi];self.provisional[p]=wi
            w.maximum=min(12,w.maximum*2);w.defence=min(w.maximum,w.defence*2)
            if w.maximum==12:
                w.tier=4;self.capitals[p]=wi;self.provisional[p]=None
            self.check();return
        if kind not in ('naval','ground','ground_mobile','bombard_shared'):
            if kind=='expand':
                f=s.fleets[a[1]];f.used=True;s.pay(0 if s.trait=='void' else 1,s.expand_mp)
                if f.strength:f.strength=min(f.maximum,f.strength+2)
                self.check();return
            creation_strength=s.creation_strength(a[1]) if kind=='create' else None
            apply(s,a,rng);self.commit_owned(p)
            if creation_strength is not None:s.fleets[-1].strength=creation_strength
            if kind=='defend' and a[1]>=0:self.holdings[a[1]].defended=True
            if kind=='defend' and a[1]==-1:self.mobile_defended.add(p)
            if kind=='defend' and s.trait=='fortification':
                if a[1]>=0:
                    w=self.holdings[a[1]];w.defence=min(w.maximum,w.defence+2)
                else:
                    for f in s.fleets:
                        if f.mobile and f.strength:f.strength=min(f.maximum,f.strength+2)
            self.check();return
        group=a[1]
        for owner,i in (self.fleet_ref(p,x) for x in group):self.players[owner].fleets[i].used=True
        if kind!='bombard_shared':
            participants=[self.fleet_ref(p,x) for x in group]
            self.engaged_factions.update(owner for owner,i in participants);self.fleet_combat.update(participants)
        if kind=='naval':
            system,q=a[2:];d=self.players[q]
            s.fleet_battled.add(system)
            defenders=[i for i,f in enumerate(d.fleets) if f.strength>0 and f.system==system]
            self.engaged_factions.add(q);self.fleet_combat.update((q,i) for i in defenders)
            if any(d.fleets[i].mobile for i in defenders):self.mobile_attacked.add(q)
            initiator=max((i for i in group if s.fleets[i].strength>1),key=lambda i:(not s.fleets[i].mobile,s.fleets[i].strength,-i))
            s.fleets[initiator].strength-=1
            rolls=forced or (rng.randint(1,20),rng.randint(1,20))
            margin=rolls[0]+sum(s.fleets[i].strength for i in group)+self.fleet_effect(p,group,'escort',3)-rolls[1]-sum(d.fleets[i].strength for i in defenders)-self.fleet_effect(q,defenders,'escort',3)-magnitude(d,('system',system),'defence_platform',5)
            if margin>0:
                if any(d.fleets[i].mobile for i in defenders):self.mobile_attacked.add(q)
                for i in defenders:d.hit_fleet(i,fleet_losses(margin))
            elif margin<0:
                if any(s.fleets[i].mobile for i in group):self.mobile_attacked.add(p)
                for i in group:s.hit_fleet(i,fleet_losses(-margin))
            self.log.append(dict(cycle=self.cycle,combat='naval',attacker=p,defender=q,rolls=rolls,margin=margin))
            if margin>0:s.change('supply',self.fleet_effect(p,group,'salvage_wing',3))
            elif margin<0:d.change('supply',self.fleet_effect(q,defenders,'salvage_wing',3))
            for owner in (p,q):
                if self.players[owner].trait=='salvagers':self.players[owner].change('supply',1)
        else:
            mobile_target=kind=='ground_mobile'
            if mobile_target:
                q,fi=a[2:];d=self.players[q];target=d.fleets[fi];wi=-1
                self.mobile_attacked.add(q)
                w=Holding(4,target.strength,target.maximum,target.system,q,defended=q in self.mobile_defended)
            else:
                wi=a[2];w=self.holdings[wi];q=w.owner;d=self.players[q]
            shield_network=bool(active(d,wi,'planetary_shield'))
            shield_invulnerable=shield_network and self.void(q,w.system)
            cannon_damage=magnitude(d,wi,'orbital_cannons')
            if cannon_damage:
                target_owner,target_i=max((self.fleet_ref(p,x) for x in group),key=lambda ref:self.players[ref[0]].fleets[ref[1]].strength)
                self.players[target_owner].hit_fleet(target_i,cannon_damage)
                self.log.append(dict(cycle=self.cycle,action='orbital_cannons',player=q,target_player=target_owner,target_fleet=target_i,damage=cannon_damage))
                if self.participating_strength(p,group)==0:
                    w.attacked=True;self.check();return
            base_damage=max(1,self.ground_strength(p,group)//5)
            damage=base_damage+self.fleet_effect(p,group,'bombardment_bay')+self.fleet_effect(p,group,'siege_platform',2)
            human_battle=p in self.human_players or q in self.human_players
            intel=self.intel_choices.get(p) if self.event==6 and human_battle else None
            if intel not in (None,'difficulty','damage'):raise ValueError('Invalid Intel Breakthrough choice')
            if intel=='damage':damage+=1
            if kind=='bombard_shared':damage=max(1,self.participating_strength(p,group)//5)
            w.attacked=True
            if kind=='bombard_shared':
                s.pay(2*w.tier);actual=min(w.defence-1,max(0,damage-magnitude(d,wi,'void_shield')))
            else:
                s.pay(w.tier,base_damage)
                self.engaged_factions.add(q)
                defenders=[i for i,f in enumerate(d.fleets) if f.strength>0 and f.system==w.system]
                self.fleet_combat.update((q,i) for i in defenders)
                # Inherited AI defender commitment convention; Supply ambiguity is a switch.
                militia=bool(active(d,wi,'militia'))
                commitment=0 if militia else damage if human_battle else damage//2
                defender_supply,defender_manpower=self.minor_resources(wi) if d.role=='minor' else (d.supply,d.manpower)
                isolated=not militia and ('manpower' in d.deficits or defender_manpower<commitment)
                conscription=self.defence_choices.pop((q,wi),None)
                conscripted=False
                if isolated and commitment and conscription is not None:
                    if sum(amount for di,amount in conscription)!=commitment:raise ValueError('Conscription must meet the exact commitment')
                    if len({di for di,amount in conscription})!=len(conscription):raise ValueError('Duplicate conscription donor')
                    for di,amount in conscription:
                        donor=self.holdings[di]
                        if di==wi or donor.owner!=q or donor.defence!=donor.maximum or not isinstance(amount,int) or not 0<amount<donor.defence:
                            raise ValueError('Invalid conscription donor')
                    for di,amount in conscription:self.holdings[di].defence-=amount
                    isolated=False;conscripted=True
                    self.log.append(dict(cycle=self.cycle,player=q,action='forced_conscription',donors=conscription,commitment=commitment))
                if isolated:
                    commitment=0
                    self.log.append(dict(cycle=self.cycle,player=q,action='isolated_defense'))
                elif commitment and not conscripted:d.change('manpower',-commitment)
                defender_supply_paid=min(defender_supply,w.tier) if self.defender_supply_cost else 0
                if defender_supply_paid:d.change('supply',-defender_supply_paid)
                if d.role=='major':defender_supply,defender_manpower=d.supply,d.manpower
                else:
                    defender_manpower-=commitment
                    defender_supply-=defender_supply_paid
                av=self.ground_strength(p,group)+s.supply+s.manpower+(10 if self.event==6 else 0)
                dv=self.strength(q,w.system)+defender_supply+defender_manpower+(10 if self.event==2 else 0)+(15 if w.defended or shield_network else 0)-(15 if isolated else 0)+magnitude(d,wi,'bunker',5)
                if human_battle:
                    if (p,wi) not in self.reported_outcomes:
                        attacker=BattleSide(s.supply,s.manpower,self.ground_strength(p,group),str(p))
                        defender=BattleSide(defender_supply,defender_manpower,self.strength(q,w.system),str(q))
                        attacking=p in self.human_players
                        setup=soulstorm_setup(attacker if attacking else defender,defender if attacking else attacker,
                            player_attacking=attacking,defended=w.defended or shield_network,
                            siege=s.trait=='siege',bunker_levels=magnitude(d,wi,'bunker'),
                            ambush=self.event==2,intel_difficulty=intel=='difficulty',isolated=isolated,
                            raider='Iron Warriors' if self.event==5 else None)
                        if self.event==6:setup['intel_choice_required']=intel is None;setup['intel_options']=['difficulty','damage'];setup['intel_choosing_faction']=p
                        raise PendingBattle(setup)
                    if self.event==6 and intel is None:raise ValueError('Choose Intel Breakthrough effect before resolving')
                    won=self.reported_outcomes.pop((p,wi))
                    if type(won) is not bool:raise ValueError('Reported outcome must explicitly identify attacker victory or defeat')
                    rolls=None
                else:
                    rolls=forced or (rng.randint(1,20),rng.randint(1,20));won=rolls[0]+av>rolls[1]+dv
                transport=self.fleet_effect(p,group,'troop_transport',10)
                if won or isolated:s.change('manpower',math.floor(base_damage*min(.8,.6+transport/100)))
                defence_return=.6 if not human_battle or s.trait=='dread' else .8
                if not won:d.change('manpower',math.floor(commitment*defence_return))
                if not won:d.change('supply',math.floor(defender_supply_paid*(.6 if human_battle and s.trait=='dread' else .8)))
                actual=damage if won else (1 if s.trait=='siege' else 0)
                self.log.append(dict(cycle=self.cycle,combat='ground',attacker=p,defender=q,rolls=rolls,totals=None if human_battle else [rolls[0]+av,rolls[1]+dv],won=won,reported=human_battle))
                for owner in (p,q):
                    if self.players[owner].trait=='salvagers':self.players[owner].change('supply',1)
            if kind!='bombard_shared':actual=max(0,actual-magnitude(d,wi,'void_shield'))
            if shield_invulnerable:actual=0
            if mobile_target:
                d.hit_fleet(fi,actual)
                if target.strength==0 and kind!='bombard_shared':
                    # check() applies the Capital loss; replace ordinary Supply
                    # expenditure rather than charging both in the final ledger.
                    d.change('supply',defender_supply_paid)
                self.check();return
            d.hit_host(wi,min(w.defence,actual));w.defence-=actual
            if w.defence<=0:
                capital_lost=self.capitals[q]==wi
                penalty=4 if w.tier==4 else 2
                # Replace the already committed defender Supply with Planet Fall.
                d.change('supply',(defender_supply_paid if kind!='bombard_shared' else 0)-penalty);d.change('manpower',-penalty)
                w.defence=1;w.owner=p;w.defended=False;s.captures+=1
                if s.trait=='salvagers':s.change('supply',2)
                if capital_lost:self.capitals[q]=None
                if self.provisional[q]==wi:self.provisional[q]=None
                for project in list(d.projects):
                    if project.host==wi and project.integrity>0:d.projects.remove(project);s.projects.append(project)
                allocation=self.planetfall_choices.get((p,wi),())
                for point in range(actual):
                    eligible=[i for i,f in enumerate(d.fleets) if f.strength>0 and f.system==w.system]
                    if not eligible:break
                    strongest=max(d.fleets[i].strength for i in eligible)
                    tied=[i for i in eligible if d.fleets[i].strength==strongest]
                    if point<len(allocation):
                        i=allocation[point]
                        if i not in tied:raise ValueError('Planet Fall damage must hit a strongest surviving fleet')
                    elif len(tied)>1 and p in self.human_players and d.role=='major':raise PendingAllocation(point,tied)
                    else:
                        i=max(tied,key=lambda fi:(sum(project.integrity for project in d.projects if project.host==('fleet',fi)),-fi))
                    d.hit_fleet(i,1)
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
        # System structures change hands only when one faction owns every
        # planetary body and also has void superiority. Stations are excluded.
        for system in self.systems:
            owners={w.owner for w in self.holdings if w.system==system and not w.station}
            if len(owners)!=1:continue
            captor=next(iter(owners))
            if not self.void(captor,system):continue
            for q,other in enumerate(self.players):
                if q==captor:continue
                for project in list(other.projects):
                    if project.host!=('system',system) or project.integrity<=0:continue
                    if CATALOG[project.profile].stages==3:
                        other.projects.remove(project);self.players[captor].projects.append(project)
                    else:project.integrity=0
                    self.log.append(dict(cycle=self.cycle,action='system_construction_control',player=captor,previous=q,profile=project.profile))
        for p,s in enumerate(self.players):
            for wi,w in enumerate(self.holdings):
                if w.owner!=p:continue
                bonus=magnitude(s,wi,'fortification_network',2)
                w.maximum+=bonus-w.capacity_bonus;w.capacity_bonus=bonus
                w.defence=min(w.defence,w.maximum)
            for f in s.fleets:
                if not f.mobile or f.strength<=0:continue
                bonus=magnitude(s,-1,'fortification_network',2)
                f.maximum+=bonus-getattr(f,'capacity_bonus',0);f.capacity_bonus=bonus
                f.strength=min(f.strength,f.maximum)
            self.refresh(p);s.validate()
            if s.stop:self.stop=s.stop
        assert all(w.owner in range(len(self.players)) for w in self.holdings)
        assert len(self.capitals)==len(self.provisional)==len(self.players)
        assert len(self.turn_order)==len(set(self.turn_order))
        for p,s in enumerate(self.players):
            capital=self.capitals[p]
            if capital is not None and capital>=0:
                assert self.holdings[capital].owner==p and not self.holdings[capital].station
            for project in s.projects:
                assert project.profile in CATALOG
                if project.integrity<=0:continue
                if isinstance(project.host,tuple):
                    kind,i=project.host
                    assert kind in ('fleet','system')
                    if kind=='fleet':assert 0<=i<len(s.fleets) and s.fleets[i].strength>0
                    else:assert i in self.systems
                elif project.host==-1:assert any(f.mobile and f.strength>0 for f in s.fleets)
                else:assert self.holdings[project.host].owner==p

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
    for system in arena.systems:
        own=arena.strength(p,system);enemy=sum(arena.strength(q,system) for q in range(len(arena.players)) if not arena.allied(p,q))
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
        for p in a.turn_order[rotation:]+a.turn_order[:rotation]:
            if p in a.eliminated:continue
            a.begin_turn(p)
            for _ in range(len(a.players[p].fleets)+1):
                order=select(p,'fleet')
                if order[0]=='none':break
                a.submit(p,'fleet',order,combat)
                if a.stop:break
            if a.stop:break
            for phase in ('faction','social','construction'):
                order=select(p,phase);a.submit(p,phase,order,combat)
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
    parser=argparse.ArgumentParser();parser.add_argument('--diagnostic',action='store_true');parser.add_argument('--seeds',type=int,default=4);parser.add_argument('--cycles',type=int,default=18);parser.add_argument('--out',default='shared-results');args=parser.parse_args()
    if not args.diagnostic:raise SystemExit('Balance studies locked: mechanics and strategy validation are incomplete. Use --diagnostic only for implementation checks.')
    out=Path(args.out);out.mkdir(exist_ok=True);rows=[]
    for start in (6,20):
        for rotation in range(3):
            for seed in range(args.seeds):
                row,trace=run(seed,args.cycles,start,rotation);rows.append(row)
                (out/f'trace-{start}-{rotation}-{seed}.json').write_text(json.dumps(trace,indent=2))
        print('Starting resources',start,'finished',flush=True)
    (out/'trials.json').write_text(json.dumps(rows,indent=2))
    (out/'manifest.json').write_text(json.dumps(dict(engine_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),core_sha256=hashlib.sha256(Path('balance_sim.py').read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path('Source_Rules.md').read_bytes()).hexdigest(),seeds=args.seeds,cycles=args.cycles,classification='integration experiments, not balance certification',limitations=['Synthetic asymmetrical Major-only map','Three heuristic policies, no multi-turn search yet','No diplomacy or consent model; all opponents hostile','Raid assaults omitted: this alone invalidates balance conclusions','Construction catalogue incomplete; see coverage register','Defender Supply debit enabled per 16 September ruling; AI tie favours defender','Turn order rotated, but policy/trait/map assignments not rotated','No human Soulstorm outcome model']),indent=2))
    print('Trials',len(rows),'stopped',sum(bool(r['stop']) for r in rows),flush=True)

if __name__=='__main__':main()
