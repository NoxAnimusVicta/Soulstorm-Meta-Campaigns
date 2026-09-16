"""Planetary construction effects currently integrated in the shared rules engine.
Unimplemented profiles are deliberately absent from legal actions.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Profile:
    stages:int
    upgrade:bool=True

PLANETARY={
 'depot':Profile(3),'training':Profile(3),'forge':Profile(5),'academy':Profile(5),
 'shipyard':Profile(3,False),'grand_shipyard':Profile(5),
 'bunker':Profile(3),'void_shield':Profile(5),'militia':Profile(5,False),
 'automated_defences':Profile(3),'regenerative_fortifications':Profile(5),
}

def active(state,host,name):
    return [p for p in state.projects if p.host==host and p.profile==name and p.active]

def magnitude(state,host,name,base=1):
    return sum(base*(2 if p.upgraded else 1) for p in active(state,host,name))

def has_yard(state,host):
    return host in state.capital_hosts or bool(active(state,host,'shipyard'))

def legal_construction(state,existing):
    result=[a for a in existing if not(a[0]=='upgrade' and not PLANETARY[state.projects[a[1]].profile].upgrade)]
    if not state.afford(5):return result
    hosts=[i for i in range(len(state.worlds)) if state.full_host(i)]
    if state.full_host(-1):hosts.append(-1)
    for host in hosts:
        for name,profile in PLANETARY.items():
            if name in ('depot','training','forge','academy'):continue
            if name=='grand_shipyard' and not has_yard(state,host):continue
            if any(p.host==host and p.profile==name and p.integrity>0 for p in state.projects):continue
            result.append(('start',name,host))
    return result
