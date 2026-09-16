import unittest,random
from sim_scenarios import from_spec
from strategic_planner import plan

class ScenarioTests(unittest.TestCase):
 def test_four_major_scenario_is_not_locked_to_three_players(self):
  spec={'classification':'synthetic test scenario','players':[], 'holdings':[]}
  for p in range(4):
   spec['players'].append(dict(trait='none',alignment='Independent',capital=p,fleets=[dict(strength=5,system=p)]))
   spec['holdings'].append(dict(tier=4,defence=12,maximum=12,system=p,owner=p))
  a=from_spec(spec)
  self.assertEqual(a.turn_order,[0,1,2,3])
  order=plan(a,3,'faction',['raider']*4,0,horizon=0,beam=1,samples=1)
  self.assertIn(order,a.actions(3,'faction'))
  a.submit(3,'faction',order,random.Random(0))

 def test_live_campaign_input_is_not_silently_treated_as_synthetic(self):
  with self.assertRaises(ValueError):from_spec({'classification':'live campaign'})
