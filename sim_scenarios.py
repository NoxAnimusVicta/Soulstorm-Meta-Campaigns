"""Explicit synthetic scenarios for mechanics/strategy tests, not campaign saves."""
from shared_sim import Arena,SharedState,Holding
from balance_sim import Fleet,Project

def from_spec(spec):
 if spec.get('classification')!='synthetic test scenario':raise ValueError('Scenario must declare its test provenance')
 a=Arena();a.players=[];a.holdings=[];a.capitals=[];a.provisional=[];a.turn_order=[]
 for player in spec['players']:
  s=SharedState(supply=player.get('supply',20),manpower=player.get('manpower',20),trait=player['trait'])
  s.alignment=player['alignment'];s.role=player.get('role','major')
  s.fleets=[Fleet(**f) for f in player.get('fleets',[])]
  s.projects=[];a.players.append(s);a.capitals.append(player.get('capital'));a.provisional.append(None)
  if s.role=='major':a.turn_order.append(len(a.players)-1)
 a.holdings=[Holding(**h) for h in spec['holdings']]
 for p in range(len(a.players)):a.refresh(p)
 a.check()
 return a

def campaign_fixture(traits=('siege','efficient','mobile'),initial_strength=5,minor_tier=2):
 """Symmetric declared fixture, not an approved random-generation preset."""
 players=[];holdings=[]
 for p,trait in enumerate(traits):
  capital=None
  if trait!='mobile':
   capital=len(holdings);holdings.append(dict(tier=4,defence=12,maximum=12,system=p,owner=p))
  else:capital=-1
  players.append(dict(trait=trait,alignment='Independent',capital=capital,fleets=[dict(strength=12 if trait=='mobile' else initial_strength,maximum=12 if trait=='mobile' else 5,system=p,mobile=trait=='mobile')]))
 a=from_spec(dict(classification='synthetic test scenario',players=players,holdings=holdings))
 for p in range(len(players)):
  maximum={1:2,2:4,3:8}[minor_tier]
  a.add_minor([(minor_tier,maximum,maximum,p,False),(1,2,2,p,False)])
 return a
