import itertools,json,math
from collections import Counter
from pathlib import Path
def stats(delta,two=False):
 faces=Counter(sum(x) for x in itertools.product(range(1,11),repeat=2)) if two else Counter(range(1,21))
 total=sum(faces.values())**2
 margins=Counter()
 for a,na in faces.items():
  for b,nb in faces.items():margins[a-b+delta]+=na*nb
 return dict(attacker_win=sum(n for m,n in margins.items() if m>0)/total,
  tie=margins[0]/total,defender_win=sum(n for m,n in margins.items() if m<0)/total,
  either_extreme=sum(n for m,n in margins.items() if abs(m)>=16)/total)
out=dict(fleet={str(d):dict(d20=stats(d),two_d10=stats(d,True)) for d in (-1,0,4,8)},
 ground_examples={str(d):stats(d) for d in (-77,-74,-37,-34,7,0)},
 construction_payback=dict(depot_supply_cost=15,depot_logistics_to_repay=8,forge_supply_cost=25,forge_logistics_to_repay=5),
 transports=[dict(committed=n,normal=math.floor(.6*n),base=math.floor(.7*n),upgraded=math.floor(.8*n)) for n in range(1,11)],
 event=dict(each_event_probability=1/18,expected_per100=100/18,warp_during5_build_actions=1-(17/18)**5))
Path('Balance_Microtests_20260917.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
