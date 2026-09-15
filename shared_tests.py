import random, unittest
from shared_sim import Arena, Holding, run
from balance_sim import Project

class SharedTests(unittest.TestCase):
    def test_shared_naval_damages_actual_opponent(self):
        a=Arena();a.players[0].fleets[0].system=1
        a.act(0,('naval',(0,),1,1),random.Random(0),(20,1))
        self.assertEqual([f.strength for f in a.players[1].fleets],[2,2])
        self.assertEqual(a.players[0].fleets[0].strength,4)
        self.assertTrue(a.players[0].fleets[0].used)

    def test_defender_action_remains_available(self):
        # Explicit experimental convention; defensive action timing needs a ruling.
        a=Arena();a.players[0].fleets[0].system=1
        a.act(0,('naval',(0,),1,1),random.Random(0),(20,1))
        self.assertTrue(all(not f.used for f in a.players[1].fleets))

    def test_one_naval_battle_per_system_per_turn(self):
        a=Arena()
        for f in a.players[0].fleets:f.system=1
        a.act(0,('naval',(0,),1,1),random.Random(0),(10,10))
        self.assertFalse(any(x[0]=='naval' and x[2]==1 for x in a.actions(0,'fleet')))

    def test_capture_single_owner_transfers_surviving_building(self):
        a=Arena();a.holdings[3].defence=1
        a.players[1].projects=[Project('forge',3,5,5,True)]
        a.players[0].fleets[0].system=1
        a.act(0,('ground',(0,),3),random.Random(0),(20,1))
        self.assertEqual(a.holdings[3].owner,0)
        self.assertEqual(a.players[0].projects[0].integrity,4)
        self.assertEqual(a.players[1].projects,[])
        self.assertEqual(a.players[0].worlds[3].owned,True)
        self.assertEqual(a.players[1].worlds[3].owned,False)

    def test_shared_event_once_and_same_for_all(self):
        a=Arena();a.opening(random.Random(2))
        self.assertEqual(len([e for e in a.log if e.get('action')=='event']),1)
        self.assertEqual({p.event for p in a.players},{a.event})

    def test_defended_expires_only_owner_turn(self):
        a=Arena();a.holdings[3].defended=True
        a.begin_turn(0);self.assertTrue(a.holdings[3].defended)
        a.begin_turn(1);self.assertFalse(a.holdings[3].defended)

    def test_hostile_third_player_blocks_bombardment(self):
        a=Arena();a.players[0].fleets[0].system=1
        self.assertFalse(any(x[0]=='bombard_shared' and x[2]==3 for x in a.actions(0,'fleet')))

    def test_creation_no_action_and_supply_retained(self):
        a=Arena(create_mp=2);a.act(0,('create',0),random.Random(0))
        self.assertEqual((a.players[0].supply,a.players[0].manpower),(19,18))
        self.assertTrue(a.players[0].fleets[-1].used)

    def test_seed_replay(self):
        x=run(3,2);y=run(3,2);self.assertEqual(x,y)

if __name__=='__main__':unittest.main(verbosity=2)
