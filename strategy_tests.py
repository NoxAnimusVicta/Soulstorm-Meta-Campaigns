"""Competence fixtures test strategically necessary decisions, not win rates."""
import random, unittest
from shared_sim import Arena,choose,POLICY_WEIGHTS
from balance_sim import Fleet,Project
from bot_control import coordinate,social

class StrategyTests(unittest.TestCase):
 def test_every_policy_recovers_a_locked_supply_track(self):
  for policy in POLICY_WEIGHTS:
   a=Arena();s=a.players[0];s.change('supply',-s.supply)
   self.assertEqual(choose(a,0,'faction',policy,0),('ration','supply'),policy)
 def test_policies_take_obvious_unopposed_capture(self):
  for policy in POLICY_WEIGHTS:
   a=Arena();s=a.players[0];s.supply=60;s.manpower=60
   for f in s.fleets:f.system=1
   a.players[1].supply=1;a.players[1].manpower=1;a.players[1].fleets=[]
   a.holdings[3].defence=1
   self.assertEqual(choose(a,0,'fleet',policy,0)[0],'ground',policy)
 def test_industrial_bot_finishes_income_project(self):
  a=Arena();a.players[0].projects=[Project('forge',0,integrity=4,maximum=5)]
  self.assertEqual(choose(a,0,'construction','industrial',0),('build',0))
 def test_industrial_bot_repairs_income_before_new_build(self):
  a=Arena();a.players[0].projects=[Project('forge',0,integrity=4,maximum=5,completed=True)]
  self.assertEqual(choose(a,0,'construction','industrial',0)[0],'repair')
 def test_low_resource_bot_does_not_voluntarily_enter_deficit(self):
  a=Arena();s=a.players[0];s.supply=1;s.manpower=1
  for policy in POLICY_WEIGHTS:
   self.assertEqual(choose(a,0,'construction',policy,0),('none',))
 def test_human_consent_never_automated(self):
  a=Arena();a.alliances.add(frozenset((0,1)));a.human_players.add(1)
  coordinate(a,0,['balanced']*3)
  self.assertFalse(any(o==1 for o,i,b in a.consents|a.defensive_consents))
 def test_bot_diplomacy_generates_and_accepts_offer(self):
  a=Arena();a.players[0].fleets[0].system=1
  social(a,0,['industrial']*3,random.Random(0))
  self.assertFalse(a.may_attack(0,1));self.assertEqual(a.messages[0]['reply'],'Accepted')
 def test_capital_replacement_precedes_recovery(self):
  a=Arena();a.capitals[0]=None;a.players[0].change('supply',-20)
  for policy in POLICY_WEIGHTS:self.assertEqual(choose(a,0,'faction',policy,0)[0],'establish')

if __name__=='__main__':unittest.main()

class LateCampaignStrategyTests(unittest.TestCase):
 def test_wealthy_depleted_force_returns_to_repairs(self):
  a=Arena();s=a.players[0];s.supply=s.manpower=90;s.fleets=[Fleet(1,system=1)]
  for policy in POLICY_WEIGHTS:
   self.assertEqual(choose(a,0,'fleet',policy,0),('move',0,0),policy)
 def test_wealthy_understrength_force_invests_in_fleet(self):
  a=Arena();s=a.players[0];s.supply=s.manpower=90;s.fleets=[Fleet(1,system=0)]
  for policy in POLICY_WEIGHTS:
   self.assertEqual(choose(a,0,'faction',policy,0)[0],'create',policy)
