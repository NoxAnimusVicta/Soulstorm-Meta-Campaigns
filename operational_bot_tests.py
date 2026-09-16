import unittest,random
from sim_scenarios import campaign_fixture
from sim_replay import snapshot
from shared_sim import Arena
from balance_sim import Fleet,Project
from operational_bots import select,plan_for,odds,budget,accepts_pact,STRATEGIES
from operational_search import rollout

class OperationalTests(unittest.TestCase):
 def test_void_expands_at_low_supply(self):
  a=campaign_fixture(('void','siege','mobile'));s=a.players[0];s.supply=1;s.fleets[0].strength=1
  self.assertEqual(select(a,0,'fleet','balanced',0)[0],'expand')
 def test_trait_matrix_has_every_strategy_and_seat(self):
  from trait_qualification import cases
  from strategy_validation import TRAITS,POLICIES
  rows=list(cases((0,)))
  self.assertEqual(len(rows),12*6*3)
  self.assertEqual(len({(r['trait'],r['policy'],r['seat']) for r in rows}),len(rows))
  self.assertTrue(all(r['setup']['traits'][r['seat']]==r['trait'] for r in rows))
 def test_repair_loop_does_not_reset_progress_timer(self):
  a=campaign_fixture();target=plan_for(a,0,'balanced')['target'];wi=target[1]
  a.cycle=1;plan_for(a,0,'balanced')
  a.cycle=2;a.holdings[wi].defence=1;plan_for(a,0,'balanced')
  a.cycle=3;a.holdings[wi].defence=2;plan_for(a,0,'balanced')
  a.cycle=4;a.holdings[wi].defence=1
  self.assertEqual(plan_for(a,0,'balanced')['last_progress'],2)
 def test_defended_target_demands_damage_beyond_repairs(self):
  a=campaign_fixture();target=('holding',1);a.holdings[1].defended=True
  required=budget(a,0,'balanced',target)['capacity']
  self.assertGreaterEqual(required,25)
 def test_human_orders_never_generated(self):
  a=campaign_fixture();a.human_players.add(0)
  with self.assertRaises(ValueError):select(a,0,'fleet','balanced',0)
 def test_target_persists_after_a_single_move(self):
  a=campaign_fixture();before=plan_for(a,0,'balanced')['target'];a.players[0].fleets[0].system=2
  self.assertEqual(plan_for(a,0,'balanced')['target'],before)
 def test_captured_target_is_replaced(self):
  a=campaign_fixture();t=plan_for(a,0,'balanced')['target'];a.holdings[t[1]].owner=0;a.check()
  self.assertNotEqual(plan_for(a,0,'balanced')['target'],t)
 def test_depleted_fleet_returns_to_yard(self):
  a=campaign_fixture(('efficient','siege','mobile'));a.players[0].fleets=[Fleet(1,system=1)];a.check()
  self.assertEqual(select(a,0,'fleet','balanced',0),('move',0,0))
 def test_maintenance_and_threat_change_force_budget(self):
  a=campaign_fixture();t=plan_for(a,0,'balanced')['target'];first=budget(a,0,'balanced',t)
  a.players[1].fleets=[Fleet(25,maximum=25,system=0)];second=budget(a,0,'balanced',t)
  self.assertGreater(second['capacity'],first['capacity'])
 def test_supply_lock_rations_instead_of_building(self):
  a=campaign_fixture();s=a.players[0];s.change('supply',-s.supply)
  self.assertEqual(select(a,0,'faction','balanced',0),('ration','supply'))
 def test_capital_replacement_precedes_rationing(self):
  a=campaign_fixture();a.capitals[0]=None;a.players[0].change('supply',-100)
  self.assertEqual(select(a,0,'faction','balanced',0)[0],'establish')
 def test_mobile_defend_enables_repair(self):
  a=campaign_fixture();s=a.players[2];s.fleets[0].strength=11;s.supply=s.manpower=30
  s.projects=[Project('forge',-1,integrity=4,maximum=5,completed=True)];a.check()
  self.assertEqual(select(a,2,'faction','balanced',0),('defend',-1))
  a.submit(2,'faction',('defend',-1),random.Random(0))
  self.assertEqual(select(a,2,'construction','balanced',1)[:2],('repair',0))
 def test_finishes_project_before_another_start(self):
  a=campaign_fixture();s=a.players[0];s.supply=40;s.projects=[Project('forge',0,integrity=4,maximum=5)];a.check()
  self.assertEqual(select(a,0,'construction','industrial',0),('build',0))
 def test_declines_pact_that_blocks_viable_target(self):
  a=campaign_fixture();a.players[0].fleets=[Fleet(5,system=0),Fleet(5,system=0)]
  a.players[1].fleets=[Fleet(3,system=0)];a.check()
  self.assertFalse(accepts_pact(a,0,1,'industrial'))
 def test_accepts_recovery_pact_when_broke(self):
  a=campaign_fixture();a.players[0].supply=2
  self.assertTrue(accepts_pact(a,0,1,'raider'))
 def test_odds_probe_leaves_live_state_unchanged(self):
  a=campaign_fixture();o=next(o for o in a.actions(0,'fleet',search=True) if o[0]=='ground');before=snapshot(a)
  self.assertTrue(0<=odds(a,0,o)<=1);self.assertEqual(snapshot(a),before)
 def test_dangerous_resource_advantage_can_justify_a_pact(self):
  a=campaign_fixture();a.players[0].fleets=[Fleet(10,maximum=10,system=0)]
  a.players[1].fleets=[Fleet(5,system=0)];a.players[1].supply=a.players[1].manpower=90;a.check()
  self.assertTrue(accepts_pact(a,0,1,'industrial'))
 def test_supply_pressure_prioritises_supply_income(self):
  a=campaign_fixture(('war_economy','martial','salvagers'));s=a.players[0];s.supply=40;s.manpower=80;a.check()
  o=select(a,0,'construction','industrial',0)
  self.assertEqual(o[:2],('start','forge'))
 def test_no_rollout_turn_for_eliminated_faction(self):
  from operational_search import finish
  a=campaign_fixture();a.eliminated.add(0);before=snapshot(a)
  finish(a,0,'fleet',['balanced']*3,random.Random(3),0)
  self.assertEqual(snapshot(a),before)
 def test_does_not_assume_winning_roll_penetrates_planetary_shield(self):
  from operational_bots import useful_damage
  a=Arena();s=a.players[0];d=a.players[1]
  s.fleets=[Fleet(10,maximum=10,system=1)];s.supply=s.manpower=100
  d.fleets=[Fleet(20,maximum=20,system=1)];d.projects=[Project('planetary_shield',3,integrity=5,maximum=5,completed=True)]
  a.check()
  self.assertEqual(useful_damage(a,0,('ground',(0,),3)),0)
 def test_rollout_keeps_live_plan_and_game_unchanged(self):
  a=campaign_fixture();a.bot_controller_modes={p:'operational' for p in range(3)}
  a.opening(random.Random(4));a.begin_turn(0)
  o=select(a,0,'fleet','balanced',0);before=snapshot(a)
  rollout(a,0,'fleet',o,['balanced']*3,123,1)
  self.assertEqual(snapshot(a),before)

if __name__=='__main__':unittest.main()
