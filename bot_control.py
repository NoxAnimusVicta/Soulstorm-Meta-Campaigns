"""Explicit synthetic bot decisions. Never grants consent for human factions."""
import random
from shared_sim import policy_for


def coordinate(arena,beneficiary,policies):
    """Allied bots offer defence, and spare available fleets for this turn."""
    for owner,state in enumerate(arena.players):
        if owner in arena.human_players or owner in arena.eliminated or state.role!='major':continue
        for ally in range(len(arena.players)):
            if ally==owner or not arena.allied(owner,ally):continue
            live=[i for i,f in enumerate(state.fleets) if f.strength>0]
            arena.grant_defence(owner,ally,live)
        if owner==beneficiary or not arena.allied(owner,beneficiary):continue
        available=[]
        for i,f in enumerate(state.fleets):
            if f.used or f.strength<=0:continue
            if policy_for(arena,owner,policies)=='conservative' and f.strength<f.maximum:continue
            if any(w.system==f.system and arena.may_attack(beneficiary,w.owner) for w in arena.holdings):available.append(i)
        arena.grant_support(owner,beneficiary,available)


def accepts(arena,recipient,sender,policies):
    if recipient in arena.human_players or arena.players[recipient].role!='major':return False
    state=arena.players[recipient]
    if arena.allied(recipient,sender):return False
    policy=policy_for(arena,recipient,policies)
    if getattr(arena,'bot_controller_modes',{}).get(recipient)=='operational':
        from operational_bots import accepts_pact
        return accepts_pact(arena,recipient,sender,policy)
    own=sum(f.strength for f in state.fleets)
    other=sum(f.strength for f in arena.players[sender].fleets)
    pressured=bool(state.deficits) or min(state.supply,state.manpower)<5 or own<other
    return pressured or policy in ('industrial','conservative')


def social(arena,p,policies,rng):
    """Short explicit ceasefire; policy choice, not a universal campaign rule."""
    if p in arena.human_players:raise ValueError('Human diplomacy must be supplied')
    opportunities=[x[1] for x in arena.actions(p,'social') if x[0]=='communique' and arena.may_attack(p,x[1])]
    for q in opportunities:
        if accepts(arena,p,q,policies) and q not in arena.human_players:
            message=arena.propose_pact(p,q,arena.cycle+1,rng)
            arena.answer_pact(q,message,accepts(arena,q,p,policies))
            return
    arena.submit(p,'social',('none',),rng)

def conscription(arena,p,target,commitment,damage):
    """Trade remote defence for an endangered holding without consulting dice."""
    if not commitment:return None
    current=next((f.strength for f in arena.players[p].fleets if f.mobile),0) if target==-1 else arena.holdings[target].defence
    if damage<current and commitment>damage:return None
    donors=[i for i,w in enumerate(arena.holdings) if i!=target and w.owner==p and w.defence==w.maximum and w.defence>1]
    donors.sort(key=lambda i:(sum(pr.integrity for pr in arena.players[p].projects if pr.host==i),arena.holdings[i].tier,i))
    remaining=commitment;plan=[]
    for i in donors:
        amount=min(remaining,arena.holdings[i].defence-1)
        if amount:plan.append((i,amount));remaining-=amount
        if not remaining:return tuple(plan)
    return None
