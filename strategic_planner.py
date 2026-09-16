"""Bounded rollout planning. Private future samples; no realised RNG access.
This is a search improvement, not a claim of expert or optimal play.
"""
import copy, random
from shared_sim import choose, utility

def clone(a):
    memo={id(a.log):[]}
    for s in a.players:memo[id(s.trace)]=[]
    return copy.deepcopy(a,memo)

def score(a,p,policy):
    # Relative position values slowing opponents as well as own holdings.
    return utility(a,p,policy)-.15*sum(utility(a,q,policy) for q in range(len(a.players)) if q!=p and q not in a.eliminated)

def finish_turn(a,p,phase,policies,rng,decision):
    if a.stop or p in a.eliminated:return
    if phase=='fleet':
        for n in range(len(a.players[p].fleets)+1):
            order=choose(a,p,'fleet',policies[p],decision+n)
            if order[0]=='none':break
            a.submit(p,'fleet',order,rng)
            if a.stop:return
    remaining=['faction','social','construction']
    phases=remaining if phase=='fleet' else remaining[remaining.index(phase):] if phase in remaining else []
    for n,ph in enumerate(phases):
        if a.stop:return
        a.submit(p,ph,choose(a,p,ph,policies[p],decision+100+n),rng)

def rollout(a,p,phase,order,policies,seed,horizon):
    t=clone(a);combat=random.Random(seed);events=random.Random(seed+10000000)
    t.submit(p,phase,order,combat)
    nextphase={'fleet':'fleet' if order[0]!='none' else 'faction','faction':'social','social':'construction','construction':None}[phase]
    if nextphase:finish_turn(t,p,nextphase,policies,combat,seed)
    turnorder=t.turn_order[t.rotation:]+t.turn_order[:t.rotation]
    for q in turnorder[turnorder.index(p)+1:]:
        if t.stop:break
        t.begin_turn(q);finish_turn(t,q,'fleet',policies,combat,seed+1000+q)
    for k in range(horizon):
        if t.stop:break
        t.closing()
        t.opening(events)
        for q in turnorder:
            if t.stop:break
            t.begin_turn(q);finish_turn(t,q,'fleet',policies,combat,seed+10000*(k+1)+q*1000)
    return score(t,p,policies[p]),t

def candidates(a,p,phase,policy,decision,beam):
    actions=a.actions(p,phase)
    if len(actions)<=beam:return actions
    ranked=[]
    for order in actions:
        t=clone(a);t.act(p,order,random.Random(decision+700000),(10,10))
        ranked.append((score(t,p,policy),order))
    ranked.sort(key=lambda x:x[0],reverse=True)
    result=[x[1] for x in ranked[:beam]]
    # Retain investment/withdrawal options that immediate utility otherwise prunes.
    for kind in ('none','create','move','expand','start','build','repair','defend','ration','establish'):
        option=next((order for _,order in ranked if order[0]==kind),None)
        if option is not None and option not in result:result.append(option)
    return result

def plan(a,p,phase,policies,decision,horizon=1,beam=2,samples=2):
    actions=candidates(a,p,phase,policies[p],decision,beam)
    if len(actions)==1:return actions[0]
    best=(-float('inf'),actions[0])
    for order in actions:
        scores=[rollout(a,p,phase,order,policies,800000+decision*11+j,horizon)[0] for j in range(samples)]
        value=sum(scores)/len(scores)-.2*(max(scores)-min(scores))
        if value>best[0]+1e-9:best=value,order
    return best[1]
