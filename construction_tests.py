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
  self.assertEqual(combat['totals'][1],65)
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
