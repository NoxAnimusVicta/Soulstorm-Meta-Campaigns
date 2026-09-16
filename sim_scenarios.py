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
