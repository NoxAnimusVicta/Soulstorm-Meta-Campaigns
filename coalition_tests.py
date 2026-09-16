import random, unittest
from shared_sim import Arena
from balance_sim import Fleet, Project

class CoalitionTests(unittest.TestCase):
 def arena(self):
  a=Arena();a.alliances.add(frozenset((0,2)))
  a.players[2].fleets=[Fleet(5,system=1)]
  for f in a.players[0].fleets:f.system=1
  return a
 def test_allied_naval_participation_and_action_budget(self):
  a=self.arena();a.grant_support(2,0,[0]);order=('naval',(0,(2,0)),1,1)
  self.assertIn(order,a.actions(0,'fleet'))
  a.submit(0,'fleet',order,random.Random(0),(10,10))
  self.assertTrue(a.players[2].fleets[0].used)
  self.assertFalse(a.players[0].fleets[1].used)
  self.assertFalse(a.players[1].fleets[0].used)
  self.assertEqual(a.players[2].fleets[0].strength,4)
 def test_defensive_support_accepts_used_fleets_without_spending(self):
  a=Arena();a.alliances.add(frozenset((1,2)));a.players[2].fleets=[Fleet(5,system=1,used=True)]
  for f in a.players[0].fleets:f.system=1
  a.grant_defence(2,1,[0]);a.submit(0,'fleet',('naval',(0,1),1,1),random.Random(0),(10,10))
  self.assertEqual(a.log[-1]['margin'],-6)
  self.assertTrue(a.players[2].fleets[0].used)
  self.assertFalse(a.players[1].fleets[0].used)
 def test_support_is_never_assumed(self):
  a=self.arena()
  self.assertNotIn(('naval',(0,(2,0)),1,1),a.actions(0,'fleet'))
  a.players[2].fleets[0].used=True
  with self.assertRaises(ValueError):a.grant_support(2,0,[0])
 def test_guarded_structure_victory_hits_only_structure(self):
  a=self.arena();a.grant_support(2,0,[0])
  a.players[1].projects=[Project('defence_platform',('system',1),integrity=3,maximum=3,completed=True)]
  before=[f.strength for f in a.players[1].fleets]
  a.submit(0,'fleet',('structure_assault',(0,(2,0)),1,0),random.Random(0),(20,1))
  self.assertEqual([f.strength for f in a.players[1].fleets],before)
  self.assertLess(a.players[1].projects[0].integrity,3)
 def test_defensive_ground_strength_includes_approved_ally(self):
  a=Arena();a.alliances.add(frozenset((1,2)));a.players[2].fleets=[Fleet(5,system=1,used=True)]
  for f in a.players[0].fleets:f.system=1
  a.grant_defence(2,1,[0]);a.submit(0,'fleet',('ground',(0,1),3),random.Random(0),(10,10))
  ground=next(x for x in a.log if x.get('combat')=='ground')
  self.assertEqual(ground['totals'][1],62)
  self.assertIn((2,0),a.fleet_combat)

if __name__=='__main__':unittest.main()

class DiplomacyAndInteractionTests(unittest.TestCase):
 def test_pact_requires_reply_expires_and_does_not_create_alliance(self):
  a=Arena();a.players[0].fleets[0].system=1
  mid=a.propose_pact(0,1,2,random.Random(0))
  self.assertTrue(a.may_attack(0,1))
  a.answer_pact(1,mid,True)
  self.assertFalse(a.may_attack(0,1));self.assertFalse(a.allied(0,1))
  self.assertFalse(any(x[0]=='ground' and x[2] in (2,3) for x in a.actions(0,'fleet')))
  a.cycle=3;self.assertTrue(a.may_attack(0,1))
 def test_support_and_pact_are_replayable(self):
  from sim_replay import Replay,digest
  a=Arena();a.players[0].fleets[0].system=1
  r=Replay(a,3);r.apply(('pact_offer',0,1,3));r.apply(('pact_reply',1,0,True))
  self.assertEqual(digest(r.verify()),digest(a))
 def test_mobile_defend_uses_modified_maximum(self):
  a=Arena();s=a.players[2]
  s.projects=[Project('fortification_network',-1,integrity=5,maximum=5,completed=True)]
  a.check();s.fleets[0].strength=10
  a.submit(2,'faction',('defend',-1),random.Random(0))
  self.assertEqual(s.fleets[0].strength,14)
 def test_system_capture_does_not_steal_allied_construction(self):
  a=Arena();a.alliances.add(frozenset((0,1)))
  pr=Project('system_repair',('system',0),integrity=5,maximum=5,completed=True)
  a.players[1].projects=[pr];a.check()
  self.assertEqual(pr.integrity,5);self.assertIn(pr,a.players[1].projects)
 def test_cannons_destroyed_contributor_supplies_no_assault_bonus(self):
  a=Arena();s=a.players[0];s.fleets=[Fleet(1,system=1)]
  s.projects=[Project('carrier',('fleet',0),integrity=5,maximum=5,completed=True)]
  a.players[1].projects=[Project('orbital_cannons',3,integrity=3,maximum=3,completed=True)]
  a.submit(0,'fleet',('ground',(0,),3),random.Random(0))
  self.assertEqual(a.holdings[3].defence,4)
  self.assertEqual(a.ground_strength(0,(0,)),0)

class FinalInteractionTests(unittest.TestCase):
 def test_troop_transports_use_best_rate_not_sum(self):
  for upgraded,expected in ((False,17),(True,18)):
   a=Arena();s=a.players[0];s.fleets=[Fleet(25,25,1),Fleet(25,25,1)]
   s.projects=[Project('troop_transport',('fleet',i),integrity=6 if upgraded else 3,maximum=6 if upgraded else 3,completed=True,upgraded=upgraded) for i in range(2)]
   a.players[1].supply=1;a.players[1].manpower=1
   a.submit(0,'fleet',('ground',(0,1),2),random.Random(0),(20,1))
   self.assertEqual(s.manpower,expected)
 def test_mobile_capital_blocks_uncontested_bombardment(self):
  a=Arena();a.players[2].fleets=a.players[2].fleets[:1]
  for f in a.players[0].fleets:f.system=2
  self.assertFalse(any(order[0].startswith('bombard') for order in a.actions(0,'fleet')))
 def test_small_ground_force_has_no_uncontested_minimum_bonus(self):
  a=Arena();s=a.players[0];s.trait='none';s.fleets=[Fleet(4,system=1)]
  s.supply=s.manpower=90
  a.submit(0,'fleet',('ground',(0,),3),random.Random(0),(20,1))
  self.assertEqual(a.holdings[3].defence,4);self.assertEqual(s.manpower,90)
 def test_full_world_can_be_defended_for_status(self):
  a=Arena();a.submit(0,'faction',('defend',0),random.Random(0))
  self.assertEqual(a.holdings[0].defence,12);self.assertTrue(a.holdings[0].defended)
 def test_bot_forced_conscription_is_available_without_unlocking_resource(self):
  a=Arena();a.defender_policies[1]='balanced';a.players[1].change('manpower',-20)
  for f in a.players[0].fleets:f.system=1
  a.submit(0,'fleet',('ground',(0,1),3),random.Random(0),(10,10))
  self.assertTrue(any(x.get('action')=='forced_conscription' for x in a.log))
  self.assertEqual(a.players[1].manpower,0);self.assertIn('manpower',a.players[1].deficits)

class CampaignSituationTests(unittest.TestCase):
 def test_cycle17_style_krieg_defeat_and_resupply(self):
  a=Arena();s=a.players[0];s.supply=4;s.manpower=23
  s.fleets=[Fleet(4,system=1),Fleet(4,system=1),Fleet(4,system=0),Fleet(2,system=0)]
  a.holdings[3].defence=3;a.human_players.add(0);a.reported_outcomes[(0,3)]=False
  a.submit(0,'fleet',('ground',(0,1),3),random.Random(0))
  a.submit(0,'fleet',('expand',3),random.Random(0))
  a.submit(0,'faction',('reinforce',),random.Random(0))
  self.assertEqual((s.supply,s.manpower,a.holdings[3].defence),(4,22,2))
 def test_warp_damage_then_mobile_defend_and_repair(self):
  class Storm:
   def randint(self,a,b):return 1
  a=Arena();s=a.players[2];s.projects=[Project('forge',-1,integrity=5,maximum=5,completed=True)]
  a.opening(Storm());self.assertEqual((s.fleets[0].strength,s.projects[0].integrity),(11,4))
  self.assertFalse(s.projects[0].active)
  a.submit(2,'faction',('defend',-1),random.Random(0))
  a.submit(2,'construction',('repair',0,1),random.Random(0))
  self.assertEqual((s.supply,s.manpower,s.fleets[0].strength),(15,16,12))
  self.assertTrue(s.projects[0].active)

class BaselineDefensiveCostTests(unittest.TestCase):
 def test_preserves_existing_deficit_timing_for_balance_review(self):
  a=Arena();a.holdings[3].tier=3;a.holdings[3].maximum=8;a.holdings[3].defence=1
  a.players[1].supply=3
  for f in a.players[0].fleets:f.system=1
  a.submit(0,'fleet',('ground',(0,1),3),random.Random(0),(20,1))
  self.assertEqual(a.holdings[3].owner,0)
  self.assertEqual(a.players[1].supply,0)
  self.assertEqual(a.players[1].deficits['supply'],0)

class CrossTraitTests(unittest.TestCase):
 def test_allied_salvager_receives_its_own_battle_income(self):
  a=Arena();a.alliances.add(frozenset((0,2)));a.players[2].trait='salvagers'
  a.players[2].fleets=[Fleet(5,system=1)];a.players[0].fleets[0].system=1
  a.grant_support(2,0,[0]);a.submit(0,'fleet',('naval',(0,(2,0)),1,1),random.Random(0),(10,10))
  self.assertEqual(a.players[2].supply,21)
 def test_restarting_turn_cannot_reset_naval_limit(self):
  a=Arena();a.players[0].fleets=[Fleet(5,system=1) for _ in range(3)]
  a.begin_turn(0);a.submit(0,'fleet',('naval',(0,),1,1),random.Random(0),(10,10));a.begin_turn(0)
  self.assertFalse(any(x[0]=='naval' and x[2]==1 for x in a.actions(0,'fleet')))
 def test_guarded_strike_uses_system_fleet_battle_limit(self):
  a=Arena();a.players[0].fleets[0].system=1;a.players[0].fleets[1].system=1
  a.players[1].projects=[Project('defence_platform',('system',1),integrity=3,maximum=3,completed=True)]
  a.submit(0,'fleet',('structure_assault',(0,),1,0),random.Random(0),(10,10))
  self.assertFalse(any(x[0] in ('naval','structure_assault') for x in a.actions(0,'fleet')))

class RemainingTraitTests(unittest.TestCase):
 def test_dread_also_reduces_ai_defensive_supply_return(self):
  a=Arena();a.players[0].trait='dread';a.players[0].fleets[0].system=1
  a.submit(0,'fleet',('ground',(0,),2),random.Random(0),(1,20))
  self.assertEqual(a.players[1].supply,18)
 def test_fleet_endurance_regenerates_at_logistics_only(self):
  class Quiet:
   def randint(self,a,b):return 2
  a=Arena();s=a.players[0];s.trait='endurance';s.fleets[0].strength=3
  a.opening(Quiet());self.assertEqual(s.fleets[0].strength,3)
  a.cycle=2;a.opening(Quiet());self.assertEqual(s.fleets[0].strength,4)
 def test_fortification_trait_adds_two_to_defend(self):
  a=Arena();a.players[0].trait='fortification';a.holdings[1].defence=1
  a.submit(0,'faction',('defend',1),random.Random(0))
  self.assertEqual(a.holdings[1].defence,4)
 def test_locked_resource_ignores_only_its_own_income(self):
  a=Arena();s=a.players[0];s.change('supply',-20);before=s.manpower
  s.change('supply',50);s.change('manpower',4)
  self.assertEqual(s.supply,0);self.assertEqual(s.manpower,before+4)

class FleetSearchEquivalenceTests(unittest.TestCase):
 def test_search_covers_every_distinct_strength_and_construction_group(self):
  a=Arena();s=a.players[0];s.fleets=[Fleet(5,system=1) for _ in range(4)]
  s.projects=[Project('escort',('fleet',3),integrity=3,maximum=3,completed=True)]
  exhaustive=[x for x in a.actions(0,'fleet') if x[0]=='naval']
  reduced=a.actions(0,'fleet',search=True)
  self.assertEqual(len(exhaustive),15)
  self.assertEqual(sum(x[0]=='naval' for x in reduced),7)
  for order in exhaustive:self.assertIn(a.canonical_order(0,order),reduced)
 def test_human_can_select_any_identical_fleet_not_just_representative(self):
  a=Arena();s=a.players[0];s.fleets=[Fleet(5,system=1) for _ in range(20)]
  a.submit(0,'fleet',('naval',(19,),1,1),random.Random(0),(10,10))
  self.assertTrue(s.fleets[19].used)
  self.assertFalse(s.fleets[0].used)
 def test_used_fleet_cannot_be_laundered_through_equivalent_fleet(self):
  a=Arena();s=a.players[0];s.fleets=[Fleet(5,system=1),Fleet(5,system=1,used=True)]
  with self.assertRaises(ValueError):a.submit(0,'fleet',('naval',(1,),1,1),random.Random(0))
 def test_many_identical_fleets_scale_linearly_for_group_search(self):
  a=Arena();a.players[0].fleets=[Fleet(5,system=1) for _ in range(32)]
  self.assertEqual(len(a.representative_groups(0,list(range(32)))),32)
 def test_scout_anchor_remains_actual_participant(self):
  a=Arena();s=a.players[0];s.fleets=[Fleet(5,system=1),Fleet(5,system=0)]
  s.projects=[Project('scout',('fleet',i),integrity=5,maximum=5,completed=True) for i in range(2)]
  a.players[1].fleets=[]
  order=('scout_attack',1,1,('ground',(1,),3))
  self.assertIn(order,a.actions(0,'fleet',search=True))
  a.submit(0,'fleet',order,random.Random(0),(20,1))
  self.assertTrue(s.fleets[1].used);self.assertFalse(s.fleets[0].used)

class SearchCloneIsolationTests(unittest.TestCase):
 def test_every_legal_candidate_leaves_live_state_unchanged(self):
  from shared_sim import search_clone
  from sim_replay import snapshot
  a=Arena();a.players[0].fleets[0].system=1
  a.check();before=snapshot(a)
  for phase in ('fleet','faction','social','construction'):
   for order in a.actions(0,phase,search=True):
    clone=search_clone(a)
    clone.act(0,order,random.Random(0),(10,10),_validated=True)
    self.assertEqual(snapshot(a),before,order)
 def test_nested_mutable_fields_are_copied(self):
  from shared_sim import search_clone
  a=Arena();a.players[0].fleets[0].metadata={'history':[1]}
  clone=search_clone(a);clone.players[0].fleets[0].metadata['history'].append(2)
  self.assertEqual(a.players[0].fleets[0].metadata,{'history':[1]})
