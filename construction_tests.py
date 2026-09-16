import random,unittest
from shared_sim import Arena
from balance_sim import Project

class ConstructionTests(unittest.TestCase):
 def test_bombardment_shield_reduction_precedes_one_defence_floor(self):
  a=Arena();a.holdings[3].defence=2
  for f in a.players[0].fleets:f.system=1
  for f in a.players[1].fleets:f.system=0
  a.players[1].projects=[Project('void_shield',3,5,5,True)]
  a.act(0,('bombard_shared',(0,1),3),random.Random(0))
  self.assertEqual(a.holdings[3].defence,1)
  self.assertEqual(a.players[1].projects[0].integrity,4)

 def test_faction_structure_defend_is_distinct_from_construction_repair(self):
  a=Arena();s=a.players[0];s.projects=[Project('bunker',0,1,3,True)]
  self.assertIn(('defend_structure',0),a.actions(0,'faction'))
  a.act(0,('defend_structure',0),random.Random(0))
  self.assertEqual((s.projects[0].integrity,s.supply,s.manpower),(2,19,19))
  self.assertFalse(a.holdings[0].defended)
  s.projects[0].completed=False
  self.assertNotIn(('defend_structure',0),a.actions(0,'faction'))

 def test_regeneration_only_unattacked_full_integrity_and_capped(self):
  a=Arena();a.holdings[1].defence=1
  a.players[0].projects=[Project('automated_defences',1,3,3,True),Project('regenerative_fortifications',1,5,5,True)]
  a.closing();self.assertEqual(a.holdings[1].defence,4)
  a.cycle+=1;a.holdings[1].defence=1;a.holdings[1].attacked=True
  a.closing();self.assertEqual(a.holdings[1].defence,1)
  a.cycle+=1;a.holdings[1].attacked=False;a.players[0].projects[0].integrity=2;a.players[0].projects[1].integrity=4
  a.closing();self.assertEqual(a.holdings[1].defence,1)

 def test_cycle_cannot_regenerate_twice(self):
  a=Arena();a.closing()
  with self.assertRaises(ValueError):a.closing()

 def test_upgrade_doubles_bunker_bonus(self):
  from construction_rules import magnitude
  a=Arena();a.players[0].projects=[Project('bunker',0,6,6,True,True)]
  self.assertEqual(magnitude(a.players[0],0,'bunker',5),10)

 def test_bunker_roll_and_damage_disables_it(self):
  a=Arena();a.players[0].fleets[0].system=1
  a.players[1].projects=[Project('bunker',3,3,3,True)]
  a.act(0,('ground',(0,),3),random.Random(0),(10,10))
  combat=[x for x in a.log if x.get('combat')=='ground'][-1]
  self.assertEqual(combat['totals'][1],63)
  self.assertEqual(a.players[1].projects[0].integrity,2)
  from construction_rules import magnitude
  self.assertEqual(magnitude(a.players[1],3,'bunker',5),0)

 def test_shield_prevents_damage_and_preserves_integrity(self):
  a=Arena();a.players[0].fleets[0].system=1;a.players[0].supply=80
  a.players[1].projects=[Project('void_shield',3,5,5,True),Project('bunker',3,3,3,True)]
  a.act(0,('ground',(0,),3),random.Random(0),(20,1))
  self.assertEqual(a.holdings[3].defence,4)
  self.assertEqual([p.integrity for p in a.players[1].projects],[5,3])
  self.assertEqual(a.players[0].supply,78)

 def test_militia_removes_commitment_and_isolation(self):
  a=Arena();a.players[1].change('manpower',-20)
  a.players[1].projects=[Project('militia',3,5,5,True)]
  for f in a.players[0].fleets:f.system=1
  a.act(0,('ground',(0,1),3),random.Random(0),(10,10))
  self.assertFalse(any(e.get('action')=='isolated_defense' for e in a.log))
  self.assertEqual(a.players[1].deficits,{'manpower':0})

 def test_shipyard_enables_creation_and_damage_disables(self):
  a=Arena();a.holdings[1].system=2
  s=a.players[0];s.projects=[Project('shipyard',1,3,3,True)]
  self.assertIn(('create',2),a.actions(0,'faction'))
  s.projects[0].integrity=2
  self.assertNotIn(('create',2),a.actions(0,'faction'))

 def test_grand_yard_prerequisite_and_creation(self):
  a=Arena();s=a.players[0]
  self.assertNotIn(('start','grand_shipyard',1),a.actions(0,'construction'))
  self.assertIn(('start','grand_shipyard',0),a.actions(0,'construction'))
  s.projects=[Project('grand_shipyard',0,5,5,True)]
  a.act(0,('create',0),random.Random(0));self.assertEqual(s.fleets[-1].strength,3)
  s.projects[0]=Project('grand_shipyard',0,10,10,True,True)
  a.act(0,('create',0),random.Random(0));self.assertEqual(s.fleets[-1].strength,5)
  self.assertTrue(s.fleets[-1].used)

 def test_nonupgradeable_and_repair(self):
  a=Arena();s=a.players[0];s.projects=[Project('militia',0,5,5,True)]
  self.assertNotIn(('upgrade',0),a.actions(0,'construction'))
  s.projects[0].integrity=3
  a.act(0,('repair',0),random.Random(0))
  self.assertTrue(s.projects[0].active);self.assertEqual(s.supply,18)

 def test_build_new_profile_and_upgrade(self):
  a=Arena();s=a.players[0]
  a.act(0,('start','bunker',0),random.Random(0))
  a.act(0,('build',0),random.Random(0));a.act(0,('build',0),random.Random(0))
  self.assertTrue(s.projects[0].active)
  s.supply=20;a.act(0,('upgrade',0),random.Random(0))
  self.assertEqual((s.projects[0].integrity,s.projects[0].maximum),(4,6))
  self.assertFalse(s.projects[0].active)

if __name__=='__main__':unittest.main(verbosity=2)

class ExtendedConstructionTests(unittest.TestCase):
 def test_catalogue_does_not_offer_unimplemented_effects(self):
  from construction_rules import UNIMPLEMENTED
  a=Arena()
  self.assertFalse(any(x[0]=='start' and x[1] in UNIMPLEMENTED for x in a.actions(0,'construction')))

 def test_attached_damage_does_not_hit_other_fleet(self):
  a=Arena();s=a.players[0]
  s.projects=[Project('escort',('fleet',0),3,3,True),Project('escort',('fleet',1),3,3,True)]
  s.hit_fleet(0,1)
  self.assertEqual([p.integrity for p in s.projects],[2,3])
  s.hit_fleet(0,99)
  self.assertEqual([p.integrity for p in s.projects],[0,3])

 def test_ground_strength_modifiers_do_not_increase_bombardment(self):
  a=Arena();s=a.players[0]
  s.projects=[Project('carrier',('fleet',0),5,5,True)]
  s.fleets[0].system=1
  for f in a.players[1].fleets:f.system=0
  self.assertEqual(a.ground_strength(0,(0,)),10)
  a.act(0,('bombard_shared',(0,),3),random.Random(0))
  self.assertEqual(a.holdings[3].defence,3)

 def test_consolidation_is_permanent_and_repeatable_until_major(self):
  a=Arena();s=a.players[2]
  s.projects=[Project('consolidation',5,4,5,False)]
  a.act(2,('build',0),random.Random(0))
  self.assertEqual((a.holdings[5].tier,a.holdings[5].defence,a.holdings[5].maximum),(2,4,4))
  self.assertEqual(s.projects,[])
  self.assertIn(('start','consolidation',5),a.actions(2,'construction'))
  s.projects=[Project('consolidation',5,4,5,False)]
  a.act(2,('build',0),random.Random(0))
  self.assertEqual((a.holdings[5].tier,a.holdings[5].maximum),(3,8))
  self.assertNotIn(('start','consolidation',5),a.actions(2,'construction'))

 def test_station_completion_detaches_from_builder_and_cannot_be_capital(self):
  a=Arena();s=a.players[0]
  s.projects=[Project('void_station',('fleet',0),4,5,False)]
  a.act(0,('build',0),random.Random(0))
  w=a.holdings[-1]
  self.assertEqual((w.owner,w.system,w.defence,w.maximum,w.station),(0,0,2,2,True))
  s.hit_fleet(0,99)
  self.assertEqual(w.defence,2)
  a.capitals[0]=None
  self.assertNotIn(('establish',len(a.holdings)-1),a.actions(0,'faction'))

 def test_targeted_bombardment_destroys_only_target(self):
  a=Arena();s=a.players[0];d=a.players[1]
  for f in d.fleets:f.system=0
  s.fleets[0].system=1
  d.projects=[Project('depot',3,1,3,False),Project('training',3,1,3,False)]
  a.act(0,('structure_assault',(0,),1,0),random.Random(0))
  self.assertEqual([p.integrity for p in d.projects],[0,1])
  self.assertEqual(a.holdings[3].defence,4)
  self.assertEqual((s.supply,s.manpower,s.fleets[0].strength),(18,20,5))

 def test_guarded_targeted_strike_spares_defending_fleets(self):
  a=Arena();s=a.players[0];d=a.players[1]
  for f in s.fleets:f.system=1
  d.projects=[Project('depot',3,3,3,True)]
  a.act(0,('structure_assault',(0,1),1,0),random.Random(0),(20,1))
  self.assertEqual(d.projects[0].integrity,0)
  self.assertEqual([f.strength for f in d.fleets],[5,5])
  self.assertEqual([f.strength for f in s.fleets],[4,5])

 def test_lost_targeted_strike_spares_structure(self):
  a=Arena();s=a.players[0];d=a.players[1]
  s.fleets[0].system=1;d.projects=[Project('depot',3,3,3,True)]
  a.act(0,('structure_assault',(0,),1,0),random.Random(0),(1,20))
  self.assertEqual(d.projects[0].integrity,3)
  self.assertEqual(s.fleets[0].strength,0)

class SystemInteractionTests(unittest.TestCase):
 def test_system_control_captures_minor_destroys_major_ignores_station(self):
  a=Arena();d=a.players[1]
  for f in d.fleets:f.system=2
  d.projects=[Project('defence_platform',('system',0),2,3,False),Project('system_repair',('system',0),5,5,True)]
  from shared_sim import Holding
  a.holdings.append(Holding(1,2,2,0,1,station=True))
  a.check()
  self.assertEqual(a.players[0].projects[0].profile,'defence_platform')
  self.assertEqual(a.players[0].projects[0].integrity,2)
  self.assertEqual(d.projects[0].integrity,0)
  self.assertEqual(a.holdings[-1].owner,1)

 def test_partial_system_control_does_not_capture(self):
  a=Arena();a.holdings[1].owner=1
  a.players[1].projects=[Project('defence_platform',('system',0),3,3,True)]
  a.check()
  self.assertEqual(len(a.players[1].projects),1)
  self.assertEqual(a.players[0].projects,[])

 def test_shield_network_void_superiority_prevents_ground_damage(self):
  a=Arena();s=a.players[0];d=a.players[1]
  s.fleets[0].system=1;s.supply=90
  d.projects=[Project('planetary_shield',3,5,5,True)]
  a.act(0,('ground',(0,),3),random.Random(0),(20,1))
  self.assertEqual(a.holdings[3].defence,4)
  self.assertEqual(d.projects[0].integrity,5)

 def test_shield_without_void_grants_defended_bonus_once(self):
  a=Arena();s=a.players[0];d=a.players[1]
  for f in s.fleets:f.system=1
  d.projects=[Project('planetary_shield',3,5,5,True)]
  a.holdings[3].defended=True
  a.act(0,('ground',(0,1),3),random.Random(0),(10,10))
  result=[x for x in a.log if x.get('combat')=='ground'][-1]
  self.assertEqual(result['totals'][1],72)

class ActionBudgetTests(unittest.TestCase):
 def test_one_faction_action_even_if_turn_restarted(self):
  a=Arena();r=random.Random(0)
  a.submit(0,'faction',('reinforce',),r)
  a.begin_turn(0)
  with self.assertRaises(ValueError):a.submit(0,'faction',('reinforce',),r)
  self.assertEqual(a.players[0].supply,23)

 def test_cannot_return_to_fleet_phase(self):
  a=Arena();r=random.Random(0)
  a.submit(0,'faction',('reinforce',),r)
  with self.assertRaises(ValueError):a.submit(0,'fleet',('move',0,1),r)

 def test_fleet_cannot_act_twice(self):
  a=Arena();r=random.Random(0)
  a.submit(0,'fleet',('move',0,1),r)
  with self.assertRaises(ValueError):a.submit(0,'fleet',('move',0,0),r)

 def test_new_cycle_restores_phase_budget(self):
  a=Arena();r=random.Random(0)
  a.submit(0,'faction',('reinforce',),r)
  a.opening(r)
  a.submit(0,'faction',('reinforce',),r)
  self.assertIn((0,'faction'),a.phase_spent)

class MinorFactionTests(unittest.TestCase):
 def test_minor_resources_are_local_and_scale_with_damage(self):
  a=Arena();q=a.add_minor([(2,2,4,3,False),(3,8,8,3,False)])
  self.assertEqual(a.minor_resources(6),(30,30))
  self.assertEqual(a.minor_resources(7),(80,80))
  a.players[q].change('supply',-100)
  self.assertEqual(a.minor_resources(6),(30,30))
  self.assertEqual(a.players[q].deficits,{})

 def test_minor_starting_fleets_and_no_turns(self):
  a=Arena();q=a.add_minor([(3,8,8,3,False),(1,2,2,3,False),(1,2,2,3,True)])
  self.assertEqual([(f.strength,f.maximum) for f in a.players[q].fleets],[(5,5),(5,5),(2,2)])
  self.assertEqual(a.actions(q,'faction'),[('none',)])
  self.assertNotIn(q,a.turn_order)

 def test_minor_regeneration_is_one_per_faction_and_no_resurrection(self):
  a=Arena();q=a.add_minor([(3,8,8,3,False)])
  s=a.players[q];s.fleets[0].strength=3;s.fleets[1].strength=0
  a.closing()
  self.assertEqual([f.strength for f in s.fleets],[4,0])
  a.cycle+=1;a.engaged_factions.add(q);a.closing()
  self.assertEqual([f.strength for f in s.fleets],[4,0])

class TraitInteractionTests(unittest.TestCase):
 def test_economic_traits_modify_only_their_income(self):
  a=Arena();s=a.players[0];baseline=s.income()
  s.trait='war_economy';self.assertEqual(s.income(),(baseline[0]+3,baseline[1],baseline[2]))
  s.trait='martial';self.assertEqual(s.income(),(baseline[0],baseline[1]+5,baseline[2]))

 def test_free_expansion_is_available_with_supply_locked(self):
  a=Arena();s=a.players[0];s.trait='void';s.change('supply',-20)
  self.assertIn(('expand',0),a.actions(0,'fleet'))
  a.act(0,('expand',0),random.Random(0))
  self.assertEqual((s.fleets[0].strength,s.supply,s.deficits),(5,0,{'supply':0}))

 def test_swift_creation_and_industrial_build_cost(self):
  a=Arena();s=a.players[0];s.trait='swift'
  a.act(0,('create',0),random.Random(0));self.assertEqual(s.fleets[-1].strength,3)
  s.trait='industrial';before=s.supply
  a.act(0,('start','depot',0),random.Random(0));self.assertEqual(s.supply,before-4)

 def test_repair_tender_combat_exclusion(self):
  a=Arena();s=a.players[0];s.fleets[0].strength=3
  s.projects=[Project('repair_tender',('fleet',0),3,3,True)]
  a.fleet_combat.add((0,0));a.closing();self.assertEqual(s.fleets[0].strength,3)
  a.cycle+=1;a.fleet_combat.clear();a.closing();self.assertEqual(s.fleets[0].strength,4)

 def test_escort_changes_naval_margin(self):
  a=Arena();s=a.players[0];s.fleets[0].system=1
  s.projects=[Project('escort',('fleet',0),3,3,True)]
  a.act(0,('naval',(0,),1,1),random.Random(0),(10,10))
  result=[e for e in a.log if e.get('combat')=='naval'][-1]
  self.assertEqual(result['margin'],-3)
  self.assertEqual(s.fleets[0].strength,3)
  self.assertEqual(s.projects[0].integrity,2)

class ScoutTests(unittest.TestCase):
 def test_scout_moves_and_attacks_once_without_other_fleets(self):
  a=Arena();s=a.players[0]
  s.projects=[Project('scout',('fleet',0),5,5,True)]
  order=('scout_attack',0,1,('ground',(0,),3))
  self.assertIn(order,a.actions(0,'fleet'))
  a.submit(0,'fleet',order,random.Random(0),(1,20))
  self.assertEqual(s.fleets[0].system,1)
  self.assertTrue(s.fleets[0].used)
  self.assertFalse(s.fleets[1].used)
  self.assertNotIn(order,a.actions(0,'fleet'))

 def test_warp_storm_and_damaged_scout_prevent_combined_action(self):
  a=Arena();s=a.players[0];s.projects=[Project('scout',('fleet',0),5,5,True)]
  a.event=1
  self.assertFalse(any(x[0]=='scout_attack' for x in a.actions(0,'fleet')))
  a.event=0;s.projects[0].integrity=4
  self.assertFalse(any(x[0]=='scout_attack' for x in a.actions(0,'fleet')))

class ScuttleTests(unittest.TestCase):
 def test_scuttle_refund_destruction_and_attached_constructions(self):
  a=Arena();s=a.players[0];s.projects=[Project('escort',('fleet',0),3,3,True)]
  a.submit(0,'fleet',('scuttle',0),random.Random(0))
  self.assertEqual((s.supply,s.manpower,s.fleets[0].strength),(22,19,0))
  self.assertEqual(s.projects[0].integrity,0)

 def test_scuttle_requires_void_superiority(self):
  a=Arena();a.players[0].fleets[0].system=1
  self.assertNotIn(('scuttle',0),a.actions(0,'fleet'))

class DefensiveParticipationTests(unittest.TestCase):
 def test_used_defender_still_contributes_full_strength(self):
  a=Arena();s=a.players[0];d=a.players[1];s.fleets[0].system=1
  for f in d.fleets:f.used=True
  a.act(0,('naval',(0,),1,1),random.Random(0),(10,10))
  result=[x for x in a.log if x.get('combat')=='naval'][-1]
  self.assertEqual(result['margin'],-6)
  self.assertTrue(all(f.used for f in d.fleets))

 def test_unused_defender_keeps_action_but_is_in_combat(self):
  a=Arena();a.players[0].fleets[0].system=1
  a.act(0,('naval',(0,),1,1),random.Random(0),(10,10))
  self.assertTrue(all(not f.used for f in a.players[1].fleets))
  self.assertIn((1,0),a.fleet_combat)
  self.assertIn(('move',0,0),a.actions(1,'fleet'))

class TieResolutionTests(unittest.TestCase):
 def test_fleet_tie_retains_initiation_cost_only(self):
  a=Arena();a.players[0].fleets[0].system=1
  a.act(0,('naval',(0,),1,1),random.Random(0),(16,10))
  self.assertEqual(a.players[0].fleets[0].strength,4)
  self.assertEqual([f.strength for f in a.players[1].fleets],[5,5])
  self.assertEqual([x for x in a.log if x.get('combat')=='naval'][-1]['margin'],0)

 def test_ground_tie_is_defender_win_with_siege_damage(self):
  a=Arena();s=a.players[0]
  for f in s.fleets:f.system=1
  a.act(0,('ground',(0,1),3),random.Random(0),(11,10))
  combat=[x for x in a.log if x.get('combat')=='ground'][-1]
  self.assertEqual(combat['totals'][0],combat['totals'][1])
  self.assertFalse(combat['won'])
  self.assertEqual(a.holdings[3].defence,3)

class DefenderCostTests(unittest.TestCase):
 def test_defence_win_returns_supply_and_ai_manpower_at_different_rates(self):
  a=Arena();s=a.players[0];d=a.players[1]
  for f in s.fleets:f.system=1
  a.act(0,('ground',(0,1),3),random.Random(0),(1,20))
  self.assertEqual((d.supply,d.manpower),(19,19))

 def test_planet_fall_replaces_supply_loss(self):
  a=Arena();s=a.players[0];d=a.players[1];s.supply=90
  for f in s.fleets:f.system=1
  a.holdings[3].tier=3;a.holdings[3].maximum=8;a.holdings[3].defence=1
  a.act(0,('ground',(0,1),3),random.Random(0),(20,1))
  self.assertEqual(d.supply,18)
  self.assertEqual(a.holdings[3].owner,0)

class FleetStrengthConstructionTests(unittest.TestCase):
 def test_flagship_strength_survives_damage_and_is_not_granted_twice(self):
  a=Arena();s=a.players[0];s.projects=[Project('flagship',('fleet',0),4,5,False)]
  a.act(0,('build',0),random.Random(0))
  self.assertEqual((s.fleets[0].strength,s.fleets[0].maximum),(10,10))
  s.hit_fleet(0,2)
  self.assertEqual((s.fleets[0].strength,s.fleets[0].maximum,s.projects[0].integrity),(8,10,5))
  s.hit_fleet(0,99);self.assertEqual(s.projects[0].integrity,0)

 def test_assault_cruiser_and_upgrade_add_incremental_capacity(self):
  a=Arena(start=90);s=a.players[0];s.projects=[Project('assault_cruiser',('fleet',0),2,3,False)]
  a.act(0,('build',0),random.Random(0))
  self.assertEqual((s.fleets[0].strength,s.fleets[0].maximum),(7,7))
  a.act(0,('upgrade',0),random.Random(0))
  a.act(0,('build',0),random.Random(0));a.act(0,('build',0),random.Random(0))
  self.assertEqual((s.fleets[0].strength,s.fleets[0].maximum),(9,9))

 def test_transfer_only_uses_donor_action_and_conserves_strength(self):
  a=Arena();s=a.players[0];s.fleets[1].strength=2
  a.submit(0,'fleet',('transfer',0,1,3),random.Random(0))
  self.assertEqual([f.strength for f in s.fleets],[2,5])
  self.assertEqual([f.used for f in s.fleets],[True,False])
  self.assertEqual((s.supply,s.manpower),(20,20))

class FortificationCapacityTests(unittest.TestCase):
 def test_maximum_bonus_does_not_grant_free_current_defence(self):
  a=Arena();s=a.players[0]
  s.projects=[Project('fortification_network',1,5,5,True)]
  a.check();self.assertEqual((a.holdings[1].defence,a.holdings[1].maximum),(4,6))
  a.check();self.assertEqual(a.holdings[1].maximum,6)

 def test_damage_disables_capacity_without_second_damage_to_structures(self):
  a=Arena();s=a.players[0]
  s.projects=[Project('fortification_network',1,5,5,True),Project('depot',1,3,3,True)]
  a.check();a.holdings[1].defence=6
  s.hit_host(1,1);a.holdings[1].defence-=1;a.check()
  self.assertEqual((a.holdings[1].defence,a.holdings[1].maximum),(4,4))
  self.assertEqual([p.integrity for p in s.projects],[4,2])

class NewlyRuledMechanicsTests(unittest.TestCase):
 def test_cannons_reduce_strength_before_manpower_commitment(self):
  a=Arena();s=a.players[0];d=a.players[1]
  for f in s.fleets:f.system=1
  d.projects=[Project('orbital_cannons',3,3,3,True)]
  a.act(0,('ground',(0,1),3),random.Random(0),(1,20))
  self.assertEqual(sum(f.strength for f in s.fleets),9)
  self.assertEqual(s.manpower,19)

 def test_system_defence_hits_every_enemy_fleet_only(self):
  a=Arena();s=a.players[0];d=a.players[1]
  for f in d.fleets:f.system=0
  s.projects=[Project('system_defence',('system',0),5,5,True)]
  a.closing()
  self.assertEqual([f.strength for f in d.fleets],[4,4])
  self.assertEqual([f.strength for f in s.fleets],[5,5])

 def test_merge_transfers_constructions_and_only_initiator_spends_action(self):
  a=Arena();s=a.players[0];s.fleets[0].strength=2;s.fleets[1].strength=2
  s.projects=[Project('escort',('fleet',1),3,3,True)]
  a.submit(0,'fleet',('merge',0,1),random.Random(0))
  self.assertEqual([f.strength for f in s.fleets],[4,0])
  self.assertEqual(s.projects[0].host,('fleet',0))
  self.assertTrue(s.fleets[0].used);self.assertFalse(s.fleets[1].used)
  self.assertEqual(s.manpower,20)

class GarrisonTests(unittest.TestCase):
 def test_transfer_conserves_defence_and_does_not_damage_construction(self):
  a=Arena();s=a.players[0];a.holdings[1].defence=1
  s.projects=[Project('depot',0,3,3,True)]
  a.submit(0,'faction',('garrison',((0,1,3),)),random.Random(0))
  self.assertEqual([a.holdings[i].defence for i in (0,1)],[9,4])
  self.assertEqual(s.projects[0].integrity,3)

 def test_landing_zone_allows_nonfull_donor(self):
  a=Arena();a.holdings[0].defence=10;a.holdings[1].defence=1
  order=('garrison',((0,1,3),))
  self.assertNotIn(order,a.actions(0,'faction'))
  a.players[0].projects=[Project('landing_zones',1,5,5,True)]
  self.assertIn(order,a.actions(0,'faction'))
  a.submit(0,'faction',order,random.Random(0))
  self.assertEqual(a.holdings[0].defence,7)

 def test_cannot_empty_donor_or_overfill_recipient(self):
  a=Arena();a.holdings[1].defence=1
  with self.assertRaises(ValueError):a.validate_garrison(0,((0,1,12),))
  with self.assertRaises(ValueError):a.validate_garrison(0,((0,1,4),))

class AlliedParticipationTests(unittest.TestCase):
 def test_presence_without_consent_grants_no_assault_strength(self):
  a=Arena();a.alliances.add(frozenset((0,1)))
  for p in (0,1):
   for f in a.players[p].fleets:f.system=2
  self.assertFalse(any(x[0]=='ground' and any(isinstance(i,tuple) for i in x[1]) for x in a.actions(0,'fleet')))

 def test_approved_allied_fleet_spends_its_single_cycle_action(self):
  a=Arena();a.alliances.add(frozenset((0,1)))
  for p in (0,1):
   for f in a.players[p].fleets:f.system=2
  a.grant_support(1,0,[0]);order=('ground',(0,(1,0)),4)
  self.assertIn(order,a.actions(0,'fleet'))
  a.submit(0,'fleet',order,random.Random(0),(1,20))
  self.assertTrue(a.players[1].fleets[0].used)
  self.assertFalse(a.players[1].fleets[1].used)
  a.begin_turn(1)
  self.assertNotIn(('move',0,0),a.actions(1,'fleet'))
  self.assertEqual(a.players[0].manpower,18)

 def test_already_moved_fleet_cannot_consent(self):
  a=Arena();a.alliances.add(frozenset((0,1)))
  a.submit(1,'fleet',('move',0,2),random.Random(0))
  with self.assertRaises(ValueError):a.grant_support(1,0,[0])

class ConscriptionTests(unittest.TestCase):
 def test_conscripts_avoid_isolation_without_unlocking_manpower(self):
  a=Arena();s=a.players[0];d=a.players[1]
  for f in s.fleets:f.system=1
  d.change('manpower',-20)
  a.defence_choices[(1,3)]=((2,1),)
  a.act(0,('ground',(0,1),3),random.Random(0),(1,20))
  self.assertEqual(a.holdings[2].defence,11)
  self.assertEqual((d.manpower,d.deficits),(0,{'manpower':0}))
  self.assertTrue(any(e.get('action')=='forced_conscription' for e in a.log))
  self.assertFalse(any(e.get('action')=='isolated_defense' for e in a.log))

class TransactionTests(unittest.TestCase):
 def test_invalid_defence_choice_rolls_back_costs_actions_and_randomness(self):
  import copy
  a=Arena();r=random.Random(99)
  for f in a.players[0].fleets:f.system=1
  a.players[1].change('manpower',-20)
  a.defence_choices[(1,3)]=((2,12),)
  before=copy.deepcopy(a.__dict__);rng_before=r.getstate()
  with self.assertRaises(ValueError):a.submit(0,'fleet',('ground',(0,1),3),r)
  self.assertEqual(a.__dict__,before)
  self.assertEqual(r.getstate(),rng_before)

class AlignmentTests(unittest.TestCase):
 def test_independent_is_not_automatic_alliance(self):
  a=Arena();self.assertFalse(a.allied(0,1))
  a.players[0].alignment=a.players[1].alignment='Imperium'
  self.assertTrue(a.allied(0,1))
  for f in a.players[0].fleets:f.system=1
  self.assertFalse(any(x[0]=='ground' and x[2] in (2,3) for x in a.actions(0,'fleet')))
