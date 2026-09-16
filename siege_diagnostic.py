"""Independent diagnostic challenger, not the production bot or a balance change.
Persistent target; clear orbit, soften defences, then land. Bounded force budget.
Uses visible state and exact two-d20 odds, never the game's random stream.
"""
import random,math
from shared_sim import choose,search_clone

def probability(arena,p,order):
 t=search_clone(arena);t.act(p,order,random.Random(712345),(10,10,10),_validated=True)
 row=next((r for r in reversed(t.log) if r.get('combat') in ('ground','naval')),None)
 if row is None:return 0
 if row['combat']=='naval':margin=row['margin'];return sum(i-j+margin>0 for i in range(1,21) for j in range(1,21))/400
 av,dv=[n-10 for n in row['totals']]
 if arena.event!=5:return sum(i+av>j+dv for i in range(1,21) for j in range(1,21))/400
 raid=sum(arena.raid_profile[k] for k in ('strength','supply','manpower'))
 return sum(max(0,min(20,math.ceil(i+av-raid)-1)) for i in range(1,21) for j in range(1,21) if i+av>j+dv)/8000

class SiegeDiagnostic:
 def __init__(self):self.targets={}
 def target(self,a,p):
  current=self.targets.get(p)
  if current is not None and a.holdings[current].owner!=p and not a.allied(p,a.holdings[current].owner):return current
  targets=[i for i,w in enumerate(a.holdings) if a.may_attack(p,w.owner)]
  if not targets:return None
  # Prefer a nearby inexpensive holding. Fixed target prevents movement churn.
  current=min(targets,key=lambda i:(0 if a.strength(p,a.holdings[i].system)>0 else 1,a.holdings[i].defence,a.holdings[i].tier,i))
  self.targets[p]=current;return current
 def select(self,a,p,phase,policy,decision):
  s=a.players[p];target=self.target(a,p);orders=a.actions(p,phase,search=True)
  if phase=='fleet':
   if target is None:return choose(a,p,phase,policy,decision)
   w=a.holdings[target]
   assaults=[o for o in orders if o[0]=='ground' and o[2]==target]
   ranked=[(probability(a,p,o),a.participating_strength(p,o[1]),o) for o in assaults]
   feasible=[x for x in ranked if x[0]>=.65]
   if feasible:
    # Prefer sufficient strength, not needless commitment above target defence.
    feasible.sort(key=lambda x:(-min(w.defence,x[1]//5),x[1],-x[0]))
    return feasible[0][2]
   bombard=[o for o in orders if o[0]=='bombard_shared' and o[2]==target]
   if bombard:return max(bombard,key=lambda o:min(w.defence-1,max(1,a.participating_strength(p,o[1])//5)))
   naval=[o for o in orders if o[0]=='naval' and o[2]==w.system]
   ranked=[(probability(a,p,o),o) for o in naval]
   if ranked:
    win,order=max(ranked,key=lambda x:x[0])
    if win>=.65:return order
   expands=[o for o in orders if o[0]=='expand']
   if expands and s.supply>max(4,s.income()[2]+2):return max(expands,key=lambda o:s.fleets[o[1]].maximum-s.fleets[o[1]].strength)
   moves=[o for o in orders if o[0]=='move' and o[2]==w.system]
   if moves:return max(moves,key=lambda o:s.fleets[o[1]].strength)
   return ('none',)
  if phase=='faction':
   if a.capitals[p] is None or s.deficits:return choose(a,p,phase,policy,decision)
   # Three ordinary fleet equivalents is an explicit diagnostic budget,
   # not a proposed game cap or a claim of optimal force sizing.
   create=[o for o in orders if o[0]=='create']
   if create and sum(f.maximum for f in s.fleets if f.strength)<15 and min(s.supply,s.manpower)>6:return create[0]
   if ('reinforce',) in orders and (s.supply<=s.manpower or ('muster',) not in orders):return ('reinforce',)
   if ('muster',) in orders:return ('muster',)
  return choose(a,p,phase,policy,decision)
