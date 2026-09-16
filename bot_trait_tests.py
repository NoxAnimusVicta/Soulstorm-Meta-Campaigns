"""Trait checks through the production controller and public action interface."""
import random,unittest
from sim_scenarios import campaign_fixture
from operational_bots import select,budget,plan_for
from balance_sim import Fleet,Project

class TraitBotTests(unittest.TestCase):
 def test_endurance_respects_upgraded_maximum(self):
  class NoEvent:
   def randint(self,a,b):return 2
  a=campaign_fixture(('endurance','efficient','siege'));a.players[0].fleets=[Fleet(7,maximum=10,system=0)];a.cycle=2
  a.opening(NoEvent());self.assertEqual(a.players[0].fleets[0].strength,8)
 def test_industrial_discount_cannot_voluntarily_trigger_deficit(self):
  a=campaign_fixture(('industrial','efficient','siege'));s=a.players[0];s.supply=4
  self.assertNotIn(('start','depot',0),a.actions(0,'construction'))
  s.supply=5;self.assertIn(('start','depot',0),a.actions(0,'construction'))
 def test_swift_and_upgraded_shipyard_use_best_not_additive_bonus(self):
  a=campaign_fixture(('swift','efficient','siege'));s=a.players[0];s.projects=[Project('grand_shipyard',0,10,10,True,True)]
  a.submit(0,'faction',('create',0),random.Random(0));self.assertEqual(s.fleets[-1].strength,5)
 def test_void_does_not_waive_test_variant_manpower_cost(self):
  a=campaign_fixture(('void','efficient','siege'),initial_strength=3);s=a.players[0];s.expand_mp=1;s.manpower=1
  self.assertNotIn(('expand',0),a.actions(0,'fleet'))
 def test_free_expansion_during_locked_supply(self):
  a=campaign_fixture(('void','efficient','siege'),initial_strength=3);s=a.players[0];s.change('supply',-20)
  order=select(a,0,'fleet','balanced',0)
  self.assertEqual(order,('expand',0));a.submit(0,'fleet',order,random.Random(0))
  self.assertEqual((s.supply,s.fleets[0].strength),(0,4))
 def test_efficient_bot_collects_four(self):
  a=campaign_fixture(('efficient','siege','mobile'));s=a.players[0];s.supply=2;s.manpower=30
  order=select(a,0,'faction','balanced',0);self.assertEqual(order,('reinforce',))
  a.submit(0,'faction',order,random.Random(0));self.assertEqual(s.supply,6)
 def test_swift_bot_commissions_three_strength(self):
  a=campaign_fixture(('swift','efficient','siege'));s=a.players[0];s.supply=s.manpower=40
  order=select(a,0,'faction','fleet_control',0);self.assertEqual(order[0],'create')
  a.submit(0,'faction',order,random.Random(0));self.assertEqual(s.fleets[-1].strength,3)
 def test_industrial_bot_uses_discount(self):
  a=campaign_fixture(('industrial','efficient','siege'));s=a.players[0];s.supply=s.manpower=40
  order=select(a,0,'construction','industrial',0);self.assertEqual(order[0],'start')
  a.submit(0,'construction',order,random.Random(0));self.assertEqual(s.supply,36)
 def test_fortification_bot_restores_project_host(self):
  a=campaign_fixture(('fortification','efficient','siege'));s=a.players[0];s.supply=s.manpower=40
  a.holdings[0].defence=4;s.projects=[Project('forge',0,integrity=4,maximum=5)]
  order=select(a,0,'faction','conservative',0);self.assertEqual(order,('defend',0))
  a.submit(0,'faction',order,random.Random(0));self.assertEqual(a.holdings[0].defence,10)
 def test_mobile_has_capital_instead_of_extra_starting_fleet(self):
  a=campaign_fixture(('mobile','efficient','siege'));s=a.players[0]
  self.assertEqual(len(s.fleets),1);self.assertEqual((s.fleets[0].strength,s.income()),(12,(4,4,0)))
  self.assertEqual(sum(w.owner==0 for w in a.holdings),0)
 def test_income_traits_enter_bot_budget(self):
  for trait,expected in [('war_economy',(7,4,1)),('martial',(4,9,1))]:
   a=campaign_fixture((trait,'efficient','siege'));self.assertEqual(a.players[0].income(),expected)
   self.assertGreater(budget(a,0,'balanced',plan_for(a,0,'balanced')['target'])['capacity'],0)
 def test_endurance_restores_before_bot_decides(self):
  class NoEvent:
   def randint(self,a,b):return 2
  a=campaign_fixture(('endurance','efficient','siege'),initial_strength=4);a.cycle=2
  a.opening(NoEvent());self.assertEqual(a.players[0].fleets[0].strength,5)
  self.assertNotEqual(select(a,0,'fleet','balanced',0)[0],'expand')
 def test_siege_applies_to_legal_ground_assault(self):
  a=campaign_fixture(('siege','efficient','mobile'));s=a.players[0];s.supply=s.manpower=60
  # Forced resolver losses verify the trait, with a legal order chosen from
  # actual available assaults. Decisions themselves never receive forced dice.
  order=next(o for o in a.actions(0,'fleet') if o[0]=='ground')
  wi=order[2];before=a.holdings[wi].defence
  a.submit(0,'fleet',order,random.Random(0),(1,20))
  self.assertLess(a.holdings[wi].defence,before)
 def test_dread_changes_defender_supply_returns(self):
  totals=[]
  for trait in ('dread','none'):
   a=campaign_fixture((trait,'efficient','siege'));a.players[0].fleets[0].system=1
   a.submit(0,'fleet',('ground',(0,),1),random.Random(0),(1,20))
   totals.append(a.players[1].supply)
  self.assertEqual(totals[1]-totals[0],1)
 def test_salvager_receives_battle_income(self):
  a=campaign_fixture(('salvagers','efficient','mobile'));s=a.players[0]
  order=next(o for o in a.actions(0,'fleet') if o[0]=='ground');tier=a.holdings[order[2]].tier;before=s.supply
  a.submit(0,'fleet',order,random.Random(0),(1,20))
  self.assertGreaterEqual(s.supply,before-tier+1)

if __name__=='__main__':unittest.main()
