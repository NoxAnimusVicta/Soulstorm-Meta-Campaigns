import unittest
from siege_diagnostic import SiegeDiagnostic,probability
from sim_replay import snapshot
from sim_scenarios import campaign_fixture
from balance_sim import Fleet

class DiagnosticTests(unittest.TestCase):
 def test_rebuild_after_entire_ordinary_force_lost(self):
  a=campaign_fixture();s=a.players[0];s.fleets=[];s.supply=s.manpower=20;a.check()
  self.assertEqual(SiegeDiagnostic().select(a,0,'faction','balanced',0)[0],'create')
 def test_odds_probe_does_not_mutate_live_state(self):
  a=campaign_fixture()
  order=next(o for o in a.actions(0,'fleet',search=True) if o[0]=='ground')
  before=snapshot(a)
  chance=probability(a,0,order)
  self.assertTrue(0<=chance<=1);self.assertEqual(snapshot(a),before)
 def test_force_budget_preserves_resources_for_operations(self):
  a=campaign_fixture();s=a.players[0];s.fleets=[Fleet(5,system=0) for _ in range(3)];s.supply=10;s.manpower=20;a.check()
  self.assertEqual(SiegeDiagnostic().select(a,0,'faction','balanced',0),('reinforce',))
 def test_target_persists_between_turns(self):
  a=campaign_fixture();bot=SiegeDiagnostic();target=bot.target(a,0)
  a.players[0].fleets[0].system=2
  self.assertEqual(bot.target(a,0),target)

if __name__=='__main__':unittest.main()
