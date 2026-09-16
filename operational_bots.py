"""Stateful operational policies for synthetic campaign experiments.

Plans use public state only. Every chosen order must still pass Arena.submit.
Thresholds express bot preferences, never campaign rules. Memory lives in Arena
so snapshots and hypothetical rollouts preserve it without global state.
"""
import math,random
from dataclasses import dataclass
from shared_sim import search_clone,choose as tactical_choose
from construction_rules import cost as build_cost,CATALOG

@dataclass(frozen=True)
class Strategy:
    confidence:float=.65
    reserve:int=7
    force_bias:int=0
    consolidate:bool=False
    invest:bool=False
    opportunistic:bool=False

STRATEGIES={
 'raider':Strategy(.55,5,0,False,False,True),
 'industrial':Strategy(.70,10,0,False,True,False),
 'fleet_control':Strategy(.65,7,5,False,False,False),
 'conservative':Strategy(.80,12,0,True,True,False),
 'opportunist':Strategy(.60,6,0,False,False,True),
 'balanced':Strategy(.65,8,0,True,False,False),
}

def odds(a,p,order):
    """Exact d20 victory chance from the resolver's committed combat totals.
    No realised RNG or future events are inspected. Probe is isolated.
    """
    t=search_clone(a);t.act(p,order,random.Random(713654),(10,10,10),_validated=True)
    row=next((r for r in reversed(t.log) if r.get('combat') in ('ground','naval','structure')),None)
    if row is None:return 0.
    if row['combat']!='ground':
        margin=row['margin']
        return sum(i-j+margin>0 for i in range(1,21) for j in range(1,21))/400
    av,dv=[n-10 for n in row['totals']]
    if a.event!=5:return sum(i+av>j+dv for i in range(1,21) for j in range(1,21))/400
    raid=sum(a.raid_profile[k] for k in ('strength','supply','manpower'))
    return sum(max(0,min(20,math.ceil(i+av-raid)-1)) for i in range(1,21) for j in range(1,21) if i+av>j+dv)/8000

def useful_damage(a,p,order):
    """Check actual effects, including shields, rather than assuming a win hurts."""
    inner=order[3] if order[0]=='scout_attack' else order
    t=search_clone(a);t.act(p,order,random.Random(713654),(20,1,1),_validated=True)
    if inner[0] in ('ground','bombard_shared'):
        before=a.holdings[inner[2]];after=t.holdings[inner[2]]
        return before.defence if after.owner==p and before.owner!=p else max(0,before.defence-after.defence)
    if inner[0]=='ground_mobile':
        q,i=inner[2:];return max(0,a.players[q].fleets[i].strength-t.players[q].fleets[i].strength)
    return 0

def enemy_strength(a,p,system,attackable=False):
    return sum(a.strength(q,system) for q in range(len(a.players)) if (a.may_attack(p,q) if attackable else not a.allied(p,q)))

def incoming_strength(a,p,system):
    # Static Minor fleets defend but cannot launch operations against the bot.
    return sum(a.strength(q,system) for q,s in enumerate(a.players) if s.role=='major' and a.may_attack(p,q))

def strongest_defending_group(a,p,system):
    # Unallied rivals do not pool their fleets into a single defending side.
    return max((a.participating_strength(q,a.defenders(q,system)) for q in range(len(a.players)) if not a.allied(p,q)),default=0)

def target_info(a,target):
    if target is None:return None
    if target[0]=='holding':
        w=a.holdings[target[1]]
        return w.owner,w.system,w.defence,w.maximum,w.tier
    _,q,i=target;f=a.players[q].fleets[i]
    return q,f.system,f.strength,f.maximum,4

def candidates_targets(a,p):
    result=[('holding',i) for i,w in enumerate(a.holdings) if not a.allied(p,w.owner)]
    result += [('mobile',q,i) for q,s in enumerate(a.players) if not a.allied(p,q) for i,f in enumerate(s.fleets) if f.mobile and f.strength>0]
    return result

def plan_for(a,p,policy):
    if not hasattr(a,'bot_plans'):a.bot_plans={}
    plan=a.bot_plans.setdefault(p,dict(target=None,chosen_cycle=a.cycle,last_progress=a.cycle,signature=None))
    targets=candidates_targets(a,p);current=plan['target']
    if current not in targets:current=None
    if current is not None:
        q,system,defence,_,_=target_info(a,current)
        signature=(defence,enemy_strength(a,p,system))
        if plan['signature'] is None or signature<tuple(plan['signature']):
            plan['last_progress']=a.cycle;plan['signature']=signature
        # Reconsider stale operations; do not switch targets every individual move.
        if a.cycle-plan['last_progress']>=8:current=None
    if current is None and targets:
        profile=STRATEGIES[policy]
        def rank(target):
            q,system,defence,maximum,tier=target_info(a,target)
            own=a.strength(p,system);enemy=enemy_strength(a,p,system)
            nearby=0 if own else 6
            # Low remaining defence is valuable; capitals are costly sieges.
            return nearby+defence+max(0,enemy-own)*.3+ (0 if a.may_attack(p,q) else 8)-tier*(.7 if profile.opportunistic else .3)
        current=min(targets,key=rank)
        # Reconsideration resets the observation window, even if the same
        # holding remains the best target. Repair loops cannot masquerade as
        # fresh progress by bouncing between the same two defence values.
        plan.update(chosen_cycle=a.cycle,last_progress=a.cycle,signature=None)
    plan['target']=current;plan['policy']=policy
    return plan

def budget(a,p,policy,target):
    s=a.players[p];profile=STRATEGIES[policy];si,mi,up=s.income()
    desired=10+profile.force_bias
    attack_cost=2;commitment=2;combat_pool=0
    if target is not None:
        q,system,defence,maximum,tier=target_info(a,target)
        desired=max(desired,5*min(3,max(1,defence)),strongest_defending_group(a,p,system)+4)
        if target[0]=='holding' and a.holdings[target[1]].defended:
            desired=max(desired,5*(tier+1))
        remote_threat=max((incoming_strength(a,p,w.system) for w in a.holdings if w.owner==p and w.system!=system),default=0)
        if remote_threat:desired+=min(10,math.ceil(remote_threat/2))
        attack_cost=tier;commitment=max(1,int(desired)//5)
        if a.players[q].role=='minor':
            ds,dm=a.minor_resources(target[1])
            # The operation includes bombardment where orbit can be cleared;
            # do not budget a frontal attack against permanently full defence.
            if defence>1:ds/=defence;dm/=defence
        else:ds,dm=a.players[q].supply,a.players[q].manpower
        combat_pool=max(0,ds+dm+enemy_strength(a,p,system)-sum(f.strength for f in s.fleets)+7+attack_cost+commitment)
    home_threat=max((strongest_defending_group(a,p,w.system) for w in a.holdings if w.owner==p),default=0)
    desired=max(desired,home_threat+5 if home_threat else 0)
    # Sustainable capacity grows with economy; no universal fleet-count cap.
    sustain=max(2,int(min(si,mi))+3)
    desired=min(desired,5*sustain)
    # A home-system attacker can turn stockpiles into battle strength too.
    home_systems={w.system for w in a.holdings if w.owner==p}|{f.system for f in s.fleets if f.mobile and f.strength>0}
    for q,other in enumerate(a.players):
        if other.role!='major' or not a.may_attack(p,q):continue
        if any(a.strength(q,k)>0 for k in home_systems):
            combat_pool=max(combat_pool,other.supply+other.manpower+sum(a.strength(q,k)-a.strength(p,k) for k in home_systems)+3)
    reserve_s=max(profile.reserve+attack_cost,combat_pool*.5)+max(0,2*(up-si))
    reserve_m=max(profile.reserve+commitment,combat_pool*.5)+max(0,2*(up-mi))
    return dict(capacity=desired,supply=reserve_s,manpower=reserve_m)

def target_matches(order,target):
    if target is None:return False
    if order[0] in ('ground','bombard_shared'):return target==('holding',order[2])
    if order[0]=='ground_mobile':return target==('mobile',order[2],order[3])
    return False

def defensive_emergency(a,p):
    systems={w.system for w in a.holdings if w.owner==p}
    systems.update(f.system for f in a.players[p].fleets if f.mobile and f.strength>0)
    return any(incoming_strength(a,p,k)>a.strength(p,k)+5 for k in systems)

def select(a,p,phase,policy,decision):
    if p in a.human_players:raise ValueError('Human orders cannot be generated')
    profile=STRATEGIES[policy];orders=a.actions(p,phase,search=True)
    if len(orders)==1:return orders[0]
    plan=plan_for(a,p,policy);target=plan['target'];info=target_info(a,target)
    limits=budget(a,p,policy,target);s=a.players[p]
    if phase=='faction':return faction(a,p,policy,orders,limits,info,decision)
    if phase=='construction':return construction(a,p,policy,orders,limits,decision)
    if phase!='fleet':return tactical_choose(a,p,phase,policy,decision)

    # Captures and useful attrition are resolved before optional maintenance.
    attacks=[o for o in orders if o[0] in ('ground','ground_mobile') and (target_matches(o,target) or profile.opportunistic)]
    feasible=[]
    for order in attacks:
        if a.ground_strength(p,order[1])<5 and s.trait!='siege':continue
        if not useful_damage(a,p,order):continue
        chance=odds(a,p,order)
        defence=a.holdings[order[2]].defence if order[0]=='ground' else a.players[order[2]].fleets[order[3]].strength
        damage=a.ground_strength(p,order[1])//5
        attrition=s.trait=='siege' and s.supply>limits['supply'] and damage>=1
        if chance>=profile.confidence or attrition:
            value=chance*min(defence,damage)+(1-chance)*(1 if attrition else 0)
            capture=chance if damage>=defence else 0
            feasible.append((capture*8+value-damage*.08,chance,order))
    if feasible:return max(feasible,key=lambda x:(x[0],x[1]))[2]
    bombard=[o for o in orders if o[0]=='bombard_shared' and target_matches(o,target) and useful_damage(a,p,o)>0]
    if bombard:return max(bombard,key=lambda o:min(info[2]-1,max(1,a.participating_strength(p,o[1])//5)))

    strikes=[]
    for order in orders:
        if order[0]!='structure_assault':continue
        q,pi=order[2:];project=a.players[q].projects[pi];system=a.players[q].host_system(project.host)
        if info is None or system!=info[1]:continue
        guarded=bool(a.defenders(q,system));chance=odds(a,p,order) if guarded else 1.
        if chance>=profile.confidence:
            priority=3 if project.profile in ('planetary_shield','void_shield','orbital_cannons','defence_platform') else 1
            strikes.append((priority*chance,order))
    if strikes:return max(strikes,key=lambda x:x[0])[1]
    scouts=[o for o in orders if o[0]=='scout_attack' and target_matches(o[3],target) and useful_damage(a,p,o)>0]
    scouts=[o for o in scouts if o[3][0]=='bombard_shared' or odds(a,p,o)>=profile.confidence]
    if scouts:return scouts[0]

    naval=[o for o in orders if o[0]=='naval' and (info is not None and o[2]==info[1] or any(w.owner==p and w.system==o[2] for w in a.holdings))]
    ranked=[(odds(a,p,o),a.participating_strength(p,o[1]),o) for o in naval]
    feasible=[x for x in ranked if x[0]>=profile.confidence]
    if feasible:return max(feasible,key=lambda x:(x[0],x[1]))[2]

    moves=[o for o in orders if o[0]=='move']
    yards=sorted(s.yards(),key=lambda k:enemy_strength(a,p,k))
    # Withdraw battered ordinary ships for actual repairs, not endless shuffling.
    retreat=[]
    for order in moves:
        f=s.fleets[order[1]]
        battered=not f.mobile and f.strength<f.maximum*.6 and f.system not in s.yards()
        overwhelmed=incoming_strength(a,p,f.system)>a.strength(p,f.system)*1.6
        safe=incoming_strength(a,p,order[2])<a.strength(p,order[2])+f.strength
        if safe and (battered and order[2] in yards or overwhelmed and order[2] in yards):retreat.append(order)
    if retreat:return min(retreat,key=lambda o:(enemy_strength(a,p,o[2]),s.fleets[o[1]].strength))
    expands=[o for o in orders if o[0]=='expand']
    if expands and (s.trait=='void' or s.supply>max(3,limits['supply']//2)):return max(expands,key=lambda o:s.fleets[o[1]].maximum-s.fleets[o[1]].strength)
    # Consolidate damaged fragments only when no strength is thrown away.
    merges=[o for o in orders if o[0]=='merge' and s.fleets[o[1]].strength+s.fleets[o[2]].strength<=s.fleets[o[1]].maximum+max(0,s.fleets[o[2]].maximum-5)]
    if merges and (s.income()[2]>min(s.income()[:2]) or s.deficits):return max(merges,key=lambda o:s.fleets[o[1]].strength+s.fleets[o[2]].strength)
    if info is not None:
        assembly=[]
        for order in moves:
            if order[2]!=info[1]:continue
            f=s.fleets[order[1]]
            if not f.mobile and f.strength<f.maximum*.6:continue
            owns=any(w.owner==p and w.system==f.system for w in a.holdings)
            exposed=incoming_strength(a,p,f.system)>a.strength(p,f.system)-f.strength
            if owns and exposed and not profile.opportunistic:
                remaining=a.strength(p,f.system)-f.strength
                own_defence=s.supply+s.manpower+remaining
                attacking=max((other.supply+other.manpower+a.strength(q,f.system) for q,other in enumerate(a.players) if other.role=='major' and a.may_attack(p,q) and a.strength(q,f.system)>0),default=0)
                if remaining<5 or own_defence<attacking+10:continue
            assembly.append(order)
        if assembly:return max(assembly,key=lambda o:s.fleets[o[1]].strength)
    return ('none',)

def faction(a,p,policy,orders,limits,info,decision):
    s=a.players[p];profile=STRATEGIES[policy]
    if a.capitals[p] is None or s.deficits:return tactical_choose(a,p,'faction',policy,decision)
    defend=[o for o in orders if o[0]=='defend']
    # Restore capital hosts before repairs/building aboard them.
    mobile=next((f for f in s.fleets if f.mobile and f.strength>0),None)
    if mobile and mobile.strength<mobile.maximum and ('defend',-1) in defend:return ('defend',-1)
    for order in defend:
        if order[1]<0:continue
        w=a.holdings[order[1]]
        host_projects=any(pr.host==order[1] and pr.integrity>0 for pr in s.projects)
        if w.defence<w.maximum and (host_projects or w.tier==4 and incoming_strength(a,p,w.system)>a.strength(p,w.system)):return order
    capacity=sum(f.maximum for f in s.fleets if f.strength>0)
    create=[o for o in orders if o[0]=='create']
    if create and capacity<limits['capacity'] and s.supply>max(6,limits['supply']//2) and s.manpower>max(6,limits['manpower']//2):
        return min(create,key=lambda o:(0 if info and o[1]==info[1] else 1,enemy_strength(a,p,o[1])))
    if profile.consolidate and min(s.supply,s.manpower)>max(limits['supply'],limits['manpower']):
        damaged=[o for o in defend if o[1]>=0 and a.holdings[o[1]].defence<a.holdings[o[1]].maximum]
        if damaged:return min(damaged,key=lambda o:a.holdings[o[1]].defence/a.holdings[o[1]].maximum)
    # Funding choices account for upkeep shortfalls and construction preference.
    need_s=limits['supply']+(build_cost(s) if profile.invest or any(not pr.completed and pr.integrity>0 for pr in s.projects) else 0)
    need_m=limits['manpower']
    if ('reinforce',) in orders and s.supply/need_s<=s.manpower/need_m:return ('reinforce',)
    if ('muster',) in orders:return ('muster',)
    return tactical_choose(a,p,'faction',policy,decision)

def construction(a,p,policy,orders,limits,decision):
    s=a.players[p];profile=STRATEGIES[policy]
    repairs=[o for o in orders if o[0]=='repair']
    if repairs and s.supply>limits['supply']//2:
        return max(repairs,key=lambda o:(s.projects[o[1]].profile in ('forge','academy','depot','training'),min(3,s.projects[o[1]].maximum-s.projects[o[1]].integrity)))
    if s.supply<=limits['supply']+build_cost(s):return ('none',)
    builds=[o for o in orders if o[0]=='build']
    if builds:return max(builds,key=lambda o:s.projects[o[1]].integrity/s.projects[o[1]].maximum)
    starts=[o for o in orders if o[0]=='start']
    if not starts:return ('none',)
    # Income, reinforcement and protection investments differ by strategy.
    si,mi,up=s.income()
    supply_pressure=s.supply/max(1,limits['supply'])<=s.manpower/max(1,limits['manpower'])
    wanted=['forge' if supply_pressure else 'academy','depot' if supply_pressure else 'training']
    if policy=='fleet_control':wanted=['escort','system_repair']+wanted
    if profile.consolidate and defensive_emergency(a,p):wanted=['orbital_cannons','defence_platform']+wanted
    if profile.opportunistic and min(si,mi)>up+4:wanted=['assault_boats','troop_transport']+wanted
    for name in wanted:
        choices=[o for o in starts if o[1]==name]
        if choices:
            return min(choices,key=lambda o:enemy_strength(a,p,s.host_system(o[2])))
    # All remaining construction profiles remain available to the tactical
    # evaluator; never invent an unavailable effect or alter construction costs.
    return tactical_choose(a,p,'construction',policy,decision)

def accepts_pact(a,recipient,sender,policy):
    s=a.players[recipient]
    if recipient in a.human_players or s.role!='major' or a.allied(recipient,sender):return False
    if s.deficits or min(s.supply,s.manpower)<4:return True
    plan=plan_for(a,recipient,policy);info=target_info(a,plan['target'])
    shared={w.system for w in a.holdings if w.owner==recipient and a.strength(sender,w.system)>0}
    shared.update(f.system for f in s.fleets if f.mobile and f.strength>0 and a.strength(sender,f.system)>0)
    other=a.players[sender]
    if any(other.supply+other.manpower+a.strength(sender,k)>s.supply+s.manpower+a.strength(recipient,k)+10 for k in shared):
        return True
    if info and (info[0]==sender or a.strength(sender,info[1])>0):
        # Do not freeze the orbit needed by a viable operation; a clearly
        # superior enemy is still a reason to buy recovery time.
        return a.strength(sender,info[1])>1.5*max(1,a.strength(recipient,info[1]))
    return STRATEGIES[policy].consolidate or STRATEGIES[policy].invest or defensive_emergency(a,recipient)
