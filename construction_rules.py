"""Construction catalogue and shared-engine action generation.
Integer hosts are holdings (-1 mobile capital); tuple hosts are explicit fleet/system references.
"""
from dataclasses import dataclass
from balance_sim import Project

@dataclass(frozen=True)
class Profile:
    stages:int
    upgrade:bool=True
    domain:str='planet'
    repeatable:bool=False

PLANETARY={
 'depot':Profile(3),'training':Profile(3),'forge':Profile(5),'academy':Profile(5),
 'shipyard':Profile(3,False),'grand_shipyard':Profile(5),'bunker':Profile(3),
 'void_shield':Profile(5),'militia':Profile(5,False),'automated_defences':Profile(3),
 'regenerative_fortifications':Profile(5),'orbital_cannons':Profile(3),
 'fortification_network':Profile(5),'landing_zones':Profile(5,False),
 'planetary_shield':Profile(5,False),'consolidation':Profile(5,False,repeatable=True),
}
FLEET={name:Profile(stages,up,'fleet') for name,stages,up in [
 ('troop_transport',3,True),('repair_tender',3,True),('escort',3,True),
 ('assault_boats',3,True),('bombardment_bay',3,True),('assault_cruiser',3,True),
 ('flagship',5,True),('carrier',5,True),('siege_platform',5,True),
 ('salvage_wing',5,True),('scout',5,False)]}
SYSTEM={name:Profile(stages,up,'system') for name,stages,up in [
 ('defence_platform',3,True),('system_defence',5,True),('system_repair',5,True),
 ('logistics_anchorage',5,True),('void_station',5,False)]}
CATALOG=PLANETARY|FLEET|SYSTEM
# Catalogue coverage is not implementation coverage. Never let a bot purchase a
# profile whose effect has not yet been implemented and verified.
UNIMPLEMENTED=set()

def active(state,host,name):
    return [p for p in state.projects if p.host==host and p.profile==name and p.active]

def magnitude(state,host,name,base=1):
    return sum(base*(2 if p.upgraded else 1) for p in active(state,host,name))

def has_yard(state,host):
    return host in state.capital_hosts or bool(active(state,host,'shipyard'))

def cost(state):return 4 if state.trait=='industrial' else 5

def legal_construction(state,existing=None):
    result=[('none',)]
    for i,p in enumerate(state.projects):
        if p.integrity<=0 or not state.full_host(p.host):continue
        spec=CATALOG[p.profile]
        if p.profile in UNIMPLEMENTED:continue
        if p.completed and p.integrity<p.maximum and state.afford(min(3,p.maximum-p.integrity)):result.append(('repair',i))
        if p.completed:
            result.extend(('repair',i,amount) for amount in range(1,min(3,p.maximum-p.integrity)+1) if state.afford(amount))
        if not p.completed and state.afford(cost(state)):result.append(('build',i))
        if p.active and not p.upgraded and spec.upgrade and state.afford(cost(state)):result.append(('upgrade',i))
    if not state.afford(cost(state)):return result
    hosts=[i for i in range(len(state.worlds)) if state.full_host(i)]
    if state.full_host(-1):hosts.append(-1)
    hosts += [('fleet',i) for i,f in enumerate(state.fleets) if f.strength>0 and f.strength==f.maximum]
    hosts += [('system',s) for s in state.present_systems]
    for host in hosts:
        domain=host[0] if isinstance(host,tuple) else 'planet'
        for name,spec in CATALOG.items():
            if name in UNIMPLEMENTED:continue
            # In-progress stations are attached to their building fleet.
            if name=='void_station':
                if domain!='fleet':continue
            elif spec.domain!=domain:continue
            if name=='grand_shipyard' and not has_yard(state,host):continue
            if name=='consolidation' and (not isinstance(host,int) or host<0 or state.worlds[host].tier>=3):continue
            if not spec.repeatable and any(p.host==host and p.profile==name and p.integrity>0 for p in state.projects):continue
            if spec.repeatable and any(p.host==host and p.profile==name and p.integrity>0 and not p.completed for p in state.projects):continue
            result.append(('start',name,host))
    return result

def construct(state,action):
    kind=action[0]
    name=action[1] if kind=='start' else state.projects[action[1]].profile
    if name in UNIMPLEMENTED:raise ValueError('Construction effect not implemented: '+name)
    if kind=='start':
        _,name,host=action;state.pay(cost(state))
        if not state.full_host(host):
            state.stop='Unresolved timing: construction payment damaged its host through a deficit';return
        state.projects.append(Project(name,host,maximum=CATALOG[name].stages))
    else:
        p=state.projects[action[1]]
        amount=min(3,p.maximum-p.integrity) if kind=='repair' else 1
        if kind=='repair' and len(action)==3:
            amount=action[2]
            if type(amount) is not int or not 1<=amount<=min(3,p.maximum-p.integrity):raise ValueError('Invalid Repair amount')
        state.pay(amount if kind=='repair' else cost(state))
        if not state.full_host(p.host) or p.integrity<=0:
            state.stop='Unresolved timing: construction payment damaged its host through a deficit';return
        if kind=='upgrade':p.upgraded=True;p.completed=False;p.maximum*=2
        p.integrity=min(p.maximum,p.integrity+amount)
        if p.integrity==p.maximum:p.completed=True
