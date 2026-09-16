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

    def test_mobile_ground_target_damages_each_construction(self):
        a=Arena();a.players[0].supply=80;a.players[0].manpower=80
        for f in a.players[0].fleets:f.system=2
        a.players[2].projects=[Project('forge',-1,5,5,True),Project('depot',-1,3,3,True)]
        order=('ground_mobile',(0,1),2,0)
        self.assertIn(order,a.actions(0,'fleet'))
        a.act(0,order,random.Random(0),(20,1))
        self.assertEqual(a.players[2].fleets[0].strength,10)
        self.assertEqual([p.integrity for p in a.players[2].projects],[3,1])
        self.assertEqual(a.players[0].supply,76)

    def test_mobile_ground_destruction_is_not_capture(self):
        a=Arena();a.players[0].supply=80;a.players[0].manpower=80
        a.players[0].fleets[0].system=2;a.players[2].fleets[0].strength=1
        a.act(0,('ground_mobile',(0,),2,0),random.Random(0),(20,1))
        self.assertEqual(a.players[2].fleets[0].strength,0)
        self.assertEqual(a.players[0].captures,0)
        self.assertEqual(a.players[2].trait,'none')
        self.assertIsNone(a.capitals[2])

    def test_planet_fall_major_resource_penalty(self):
        a=Arena();a.holdings[3].defence=1;a.players[0].fleets[0].system=1
        a.act(0,('ground',(0,),3),random.Random(0),(20,1))
        self.assertEqual((a.players[1].supply,a.players[1].manpower),(18,18))

    def test_captured_capital_yard_does_not_transfer(self):
        a=Arena();a.holdings[2].defence=1;a.players[0].fleets[0].system=1
        a.act(0,('ground',(0,),2),random.Random(0),(20,1))
        self.assertIsNone(a.capitals[1]);self.assertNotIn(1,a.players[0].yards())
        self.assertNotIn(1,a.players[1].yards());self.assertFalse(a.stop)
        self.assertEqual(a.actions(1,'faction'),[('establish',3)])
        a.act(1,('establish',3),random.Random(0))
        self.assertEqual((a.holdings[3].defence,a.holdings[3].maximum),(8,8))
        self.assertNotIn(1,a.players[1].yards())
        a.holdings[3].defence=2
        a.act(1,('establish',3),random.Random(0))
        self.assertEqual((a.holdings[3].defence,a.holdings[3].maximum),(4,12))
        self.assertIn(1,a.players[1].yards())

    def test_mobile_loss_penalty_and_trait_once(self):
        a=Arena();s=a.players[2];s.hit_fleet(0,12);a.check()
        self.assertEqual((s.supply,s.manpower,s.trait),(16,15,'none'))
        self.assertFalse(a.stop);a.check()
        self.assertEqual((s.supply,s.manpower),(16,15))
        self.assertIn(('establish',4),a.actions(2,'faction'))

    def test_eliminated_player_cannot_generate_new_resources(self):
        a=Arena()
        for w in a.holdings:
            if w.owner==0:w.owner=1
        a.check();self.assertIn(0,a.eliminated)
        self.assertEqual(a.actions(0,'faction'),[('none',)])
        self.assertEqual(a.strength(0,0),0)

    def test_capital_recovery_precedes_rationing(self):
        a=Arena();a.capitals[0]=None;a.players[0].change('supply',-20)
        self.assertTrue(all(x[0]=='establish' for x in a.actions(0,'faction')))
        a.act(0,('establish',1),random.Random(0))
        self.assertEqual(a.players[0].deficits,{'supply':0})
        a.act(0,('establish',1),random.Random(0))
        self.assertEqual(a.actions(0,'faction'),[('ration','supply')])
        self.assertEqual(a.players[0].supply,0)

    def test_rollout_does_not_mutate_live_state(self):
        from strategic_planner import rollout
        a=Arena();before=repr(a.players[0]);rng=random.Random(42);state=rng.getstate()
        _,t=rollout(a,0,'faction',('create',0),['raider','industrial','fleet_control'],42,1)
        self.assertEqual(before,repr(a.players[0]));self.assertEqual(rng.getstate(),state)
        self.assertEqual(t.cycle,1)
        self.assertTrue(any(e.get('player')==1 for e in t.log))

    def test_investment_survives_candidate_pruning(self):
        from strategic_planner import candidates
        a=Arena();options=candidates(a,0,'faction','raider',0,2)
        self.assertTrue(any(x[0]=='create' for x in options))

if __name__=='__main__':unittest.main(verbosity=2)
