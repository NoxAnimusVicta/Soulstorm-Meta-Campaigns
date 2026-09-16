import unittest
from battle_setup import BattleSide,setup

class BattleSetupTests(unittest.TestCase):
 def test_committed_strength_and_resource_bands(self):
  result=setup(BattleSide(50,50,12,'Cerberus'),BattleSide(50,50,0,'Defender'))
  self.assertEqual(result['teams'][0]['formations'],3)
  self.assertEqual(result['teams'][1]['formations'],1)
  self.assertEqual(result['difficulty'],3)
  self.assertEqual(result['required_capacity'],6)

 def test_raid_preserves_both_teams_and_allows_larger_map(self):
  side=BattleSide(50,50,5,'A');other=BattleSide(50,50,5,'B')
  r=setup(side,other,raider='Iron Warriors',map_capacity=6)
  self.assertEqual([t['formations'] for t in r['teams']],[2,2,1])
  self.assertEqual((r['required_capacity'],r['closed_slots']),(5,1))
  self.assertFalse(r['teams'][2]['can_capture'])

 def test_status_modifiers_and_final_cap(self):
  side=BattleSide(50,50,5,'A');other=BattleSide(50,50,5,'B')
  self.assertEqual(setup(side,other,defended=True,siege=True)['difficulty'],3)
  self.assertEqual(setup(side,other,defended=True,ambush=True,bunker_levels=2)['difficulty'],5)
  self.assertEqual(setup(side,other,player_attacking=False,defended=True,bunker_levels=2)['difficulty'],1)

 def test_scaling_preserves_difference(self):
  r=setup(BattleSide(50,50,20,'A'),BattleSide(50,50,15,'B'))
  self.assertEqual([t['formations'] for t in r['teams']],[4,3])

 def test_impossible_scaling_does_not_silently_erase_difference(self):
  with self.assertRaises(ValueError):setup(BattleSide(50,100,30,'A'),BattleSide(50,1,0,'B'))

 def test_zero_resource_treated_as_critical_and_no_invented_outcome(self):
  r=setup(BattleSide(0,0,0,'A'),BattleSide(100,100,0,'B'))
  self.assertEqual(r['difficulty'],5)
  self.assertEqual(r['outcome'],'awaiting reported result')
