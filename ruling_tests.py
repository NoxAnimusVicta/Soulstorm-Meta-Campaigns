import copy,random,unittest
from shared_sim import Arena
from balance_sim import Fleet

class RulingsTests(unittest.TestCase):
 def test_voluntary_spending_cannot_empty_either_resource(self):
  a=Arena();s=a.players[0];s.supply=5
  before=copy.deepcopy(a.__dict__)
  self.assertNotIn(('start','depot',0),a.actions(0,'construction'))
  with self.assertRaises(ValueError):a.submit(0,'construction',('start','depot',0),random.Random(0))
  self.assertEqual(a.__dict__,before)
  s.manpower=1
  self.assertFalse(s.afford(1,1))
  s.change('supply',-5)
  self.assertEqual(s.deficits,{'supply':0})

 def test_upgraded_fleet_transfer_uses_modified_maximum(self):
  a=Arena();s=a.players[0];s.fleets[1]=Fleet(8,10,0)
  a.submit(0,'fleet',('transfer',0,1,2),random.Random(0))
  self.assertEqual([f.strength for f in s.fleets],[3,10])
  self.assertFalse(s.fleets[1].used)

 def test_summoned_ally_has_no_free_capital_or_shipyard(self):
  a=Arena();s=a.players[0]
  for wi in (4,5):a.holdings[wi].owner=0
  for f in a.players[2].fleets:f.system=1
  s.fleets[0].system=2
  turns=a.turns();self.assertEqual(next(turns),0)
  a.submit(0,'faction',('summon',2,4,'martial'),random.Random(0))
  q=3;self.assertEqual(next(turns),q)
  ally=a.players[q]
  self.assertEqual((ally.supply,ally.manpower,ally.fleets),(10,10,[]))
  self.assertIsNone(a.capitals[q]);self.assertEqual(ally.yards(),set())
  self.assertEqual(a.holdings[4].defence,4)
  a.act(q,('establish',4),random.Random(0));self.assertEqual(ally.yards(),set())
  a.act(q,('establish',4),random.Random(0));self.assertEqual(ally.yards(),{2})
  self.assertTrue(a.allied(0,q));self.assertFalse(a.allied(1,q))

 def raid(self):
  a=Arena();a.event=5
  for f in a.players[0].fleets:f.system=1
  return a

 def test_raider_victory_cannot_capture_or_create_holdings(self):
  a=self.raid();a.players[1].supply=5;a.players[1].manpower=5
  before=len(a.holdings)
  a.submit(0,'fleet',('ground',(0,),2),random.Random(0),(1,1,20))
  self.assertEqual(a.holdings[2].owner,1)
  self.assertEqual(a.holdings[2].defence,6)
  self.assertEqual(len(a.holdings),before)
  record=[e for e in a.log if e.get('combat')=='third_party_raid'][-1]
  self.assertEqual(record['winner'],'raider');self.assertTrue(record['provisional'])

 def test_raid_does_not_block_legal_attacks(self):
  a=self.raid()
  self.assertIn(('ground',(0,),3),a.actions(0,'fleet'))

 def test_human_raider_result_does_not_roll_substitute_dice(self):
  a=self.raid();a.human_players.add(0);a.reported_outcomes[(0,2)]='raider'
  rng=random.Random(42);before=rng.getstate()
  a.submit(0,'fleet',('ground',(0,),2),rng)
  self.assertEqual(rng.getstate(),before)
  self.assertEqual((a.holdings[2].owner,a.holdings[2].defence),(1,6))
