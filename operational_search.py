"""Optional look-ahead with operational opponents and private event samples."""
import random
from shared_sim import search_clone,policy_for
from bot_dispatch import select_order
from bot_control import coordinate,social
from operational_bots import select,plan_for,target_info

def outcome(a,p):
    if p in a.eliminated:return -10000
    s=a.players[p];si,mi,up=s.income()
    # Public state outcomes, with diminishing surplus and maintenance burden.
    return (30*sum(w.tier for w in a.holdings if w.owner==p)
            +sum(min(f.strength,10) for f in s.fleets)
            +.3*(min(s.supply,50)+min(s.manpower,50))
            +2*(si+mi-2*up)-25*len(s.deficits)+8*sum(s.deficits.values())
            +sum(pr.integrity*.5 for pr in s.projects if pr.integrity>0))

def finish(a,p,phase,policies,rng,decision):
    if p in a.eliminated or a.stop:return
    phases=('fleet','faction','social','construction')
    for ph in phases[phases.index(phase):]:
        if ph=='social':social(a,p,policies,rng);continue
        for n in range(sum(len(s.fleets) for s in a.players)+1 if ph=='fleet' else 1):
            order=select_order(a,p,ph,policies,decision+n,0)
            a.submit(p,ph,order,rng)
            if p in a.eliminated or a.stop:return
            if order[0]=='none':break

def rollout(a,p,phase,order,policies,seed,horizon):
    t=search_clone(a);rng=random.Random(seed);events=random.Random(seed+10000000)
    t.submit(p,phase,order,rng)
    nextphase={'fleet':'fleet' if order[0]!='none' else 'faction','faction':'social','construction':None}[phase]
    if nextphase:finish(t,p,nextphase,policies,rng,seed)
    for q in t.turns(after=p):
        t.begin_turn(q);coordinate(t,q,policies);finish(t,q,'fleet',policies,rng,seed+q*100)
    for k in range(horizon):
        t.closing();t.opening(events)
        for q in t.turns():
            t.begin_turn(q);coordinate(t,q,policies);finish(t,q,'fleet',policies,rng,seed+1000*(k+1)+q*100)
    return outcome(t,p),t

def plan(a,p,phase,policies,decision,horizon=1,samples=3):
    policy=policy_for(a,p,policies)
    primary=select(a,p,phase,policy,decision)
    # Retain the operational proposal, a tactical alternative, and waiting.
    # Then compare stronger/weaker commitments to the same combat target.
    from shared_sim import choose
    choices=[primary,choose(a,p,phase,policy,decision),('none',)]
    legal=a.actions(p,phase,search=True)
    if primary[0] in ('ground','ground_mobile','naval'):
        same=[o for o in legal if o[0]==primary[0] and o[2:]==primary[2:]]
        if same:choices += [min(same,key=lambda o:a.participating_strength(p,o[1])),max(same,key=lambda o:a.participating_strength(p,o[1]))]
    choices=list(dict.fromkeys(o for o in choices if o in legal))
    ranked=[]
    for order in choices:
        scores=[rollout(a,p,phase,order,policies,1800000+decision*13+j,horizon)[0] for j in range(samples)]
        ranked.append((sum(scores)/len(scores)-.15*(max(scores)-min(scores)),order))
    return max(ranked,key=lambda x:x[0])[1]
