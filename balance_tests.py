"""Hand-calculated and Dessica-ledger regression cases, standard-library only."""
import random
import unittest
from balance_sim import State,Fleet,World,Project,apply,legal,fixture,fleet_losses,win_probability

class RulesTests(unittest.TestCase):
    def test_dessica_cycle19_fleet_battle(self):
        s=State(supply=10,manpower=21,fleets=[Fleet(5),Fleet(12,12,mobile=True)],enemies={0:[5,3]},enemy_max={0:[5,3]})
        apply(s,('battle',(0,1),0),random.Random(0),forced=(19,4))
        self.assertEqual([f.strength for f in s.fleets],[4,12]);self.assertEqual(s.enemies[0],[0,0])
        self.assertEqual(s.trace[-1]['margin'],23)

    def test_initiator_can_pay_without_untracked_destruction(self):
        s=fixture('mobile');s.fleets.append(Fleet(1))
        apply(s,('battle',(0,1),0),random.Random(0),forced=(20,1))
        self.assertEqual([f.strength for f in s.fleets],[11,1])

    def test_cycle20_cerberus(self):
        s=State(supply=13,manpower=21,trait='mobile',fleets=[Fleet(12,12,mobile=True),Fleet(4)],worlds=[World(1,2,2,0)],enemies={0:[0,0]})
        apply(s,('bombard',(0,),0),random.Random(0));apply(s,('expand',1),random.Random(0));apply(s,('reinforce',),random.Random(0));apply(s,('start','depot',-1),random.Random(0))
        self.assertEqual((s.supply,s.manpower,s.worlds[0].defence),(8,21,1));self.assertEqual(s.fleets[1].strength,5)
        self.assertEqual(s.projects[0].integrity,1);self.assertFalse(s.projects[0].active)

    def test_cycle13_halstrave_ai(self):
        # Ledger: 23 Supply /22 MP before queued Reinforce and Academy cost means
        # battle was paid at 24 Supply /22 MP; attacker 5+24+22+d10=61.
        s=State(supply=26,manpower=23,trait='efficient',fleets=[Fleet(5)],worlds=[World(2,1,4,0)],enemies={0:[]})
        apply(s,('assault',(0,),0),random.Random(0),forced=(10,14))
        self.assertEqual(s.trace[-2]['totals'],[61,44]);self.assertTrue(s.worlds[0].owned)

    def test_planet_fall_two_points(self):
        s=State(supply=8,manpower=30,fleets=[Fleet(5),Fleet(5)],worlds=[World(2,1,4,0),World(3,8,8,0)],enemies={0:[4,3,3]})
        apply(s,('assault',(0,1),0),random.Random(0),forced=(20,1))
        apply(s,('reinforce',),random.Random(0))
        self.assertEqual(s.enemies[0],[2,3,3]);self.assertEqual((s.supply,s.manpower),(9,29))
        self.assertEqual(s.worlds[0].defence,1)

    def test_ground_does_not_require_void(self):
        s=fixture();self.assertTrue(any(a[0]=='assault' for a in legal(s,'fleet')))
        self.assertFalse(any(a[0]=='bombard' for a in legal(s,'fleet')))

    def test_actions_not_double_used(self):
        s=fixture();apply(s,('move',0,1),random.Random(0))
        self.assertEqual(legal(s,'fleet'),[('none',)])

    def test_create_after_fleet_phase_is_used(self):
        s=fixture();apply(s,('create',0),random.Random(0));self.assertTrue(s.fleets[-1].used)

    def test_warp_damage_each_attached_project(self):
        s=fixture('mobile');s.projects=[Project('forge',-1,4,5),Project('depot',-1,1,3)]
        s.hit_fleet(0,1);self.assertEqual([p.integrity for p in s.projects],[3,0]);self.assertEqual(s.fleets[0].strength,11)

    def test_initiation_not_construction_damage(self):
        s=fixture('mobile');s.projects=[Project('forge',-1,4,5)]
        apply(s,('battle',(0,),0),random.Random(0),forced=(20,1));self.assertEqual(s.projects[0].integrity,4)

    def test_repair_not_build_and_full_host(self):
        s=fixture('mobile');s.projects=[Project('forge',-1,4,5,False)]
        self.assertNotIn(('repair',0),legal(s,'construction'))
        s.projects[0].completed=True;self.assertIn(('repair',0),legal(s,'construction'))
        s.fleets[0].strength=11;self.assertNotIn(('repair',0),legal(s,'construction'))

    def test_last_supply_cannot_resurrect_mobile_construction(self):
        s=fixture('mobile');s.supply=5;s.projects=[Project('forge',-1,1,5)]
        apply(s,('build',0),random.Random(0))
        self.assertEqual(s.projects[0].integrity,0)
        self.assertEqual(s.fleets[0].strength,11)
        self.assertTrue(s.stop.startswith('Unresolved timing:'))

    def test_last_supply_cannot_start_on_damaged_mobile_host(self):
        s=fixture('mobile');s.supply=5
        apply(s,('start','forge',-1),random.Random(0))
        self.assertEqual(s.projects,[])
        self.assertTrue(s.stop)

    def test_upgrade_inactive(self):
        s=fixture();s.projects=[Project('forge',0,5,5,True)]
        apply(s,('upgrade',0),random.Random(0));p=s.projects[0]
        self.assertEqual((p.integrity,p.maximum,p.active),(6,10,False))

    def test_deficits_separate_locked_three_actions(self):
        s=fixture();s.supply=1;s.manpower=2;s.change('supply',-1)
        self.assertEqual(s.fleets[0].strength,4)
        apply(s,('ration','supply'),random.Random(0));s.change('supply',-5);s.change('supply',20)
        self.assertEqual(s.supply,0);self.assertEqual(s.deficits['supply'],1)
        s.change('manpower',-5);self.assertEqual(s.fleets[0].strength,3)
        apply(s,('ration','supply'),random.Random(0));apply(s,('ration','supply'),random.Random(0))
        self.assertEqual(s.supply,10);self.assertEqual(s.deficits,{'manpower':0})

    def test_income_incomplete_and_mobile_upkeep(self):
        s=fixture('mobile');s.projects=[Project('forge',-1,5,5,True),Project('depot',-1,1,3)]
        s.fleets.append(Fleet(5));self.assertEqual(s.income(),(9,4,1))

    def test_recovery_not_presence(self):
        s=fixture();s.enemies[0]=[3];s.enemy_max[0]=[4];s.closing();self.assertEqual(s.enemies[0],[4])
        s.enemies[0]=[3];s.engaged.add(0);s.closing();self.assertEqual(s.enemies[0],[3])

    def test_no_recovery_for_destroyed_fleet(self):
        s=fixture();s.enemies[0]=[0];s.closing();self.assertEqual(s.enemies[0],[0])

    def test_exact_probability_and_margin_boundaries(self):
        self.assertEqual(win_probability(0,0),190/400)
        self.assertEqual(win_probability(20,0),1)
        self.assertEqual([fleet_losses(x) for x in (1,5,6,10,11,15,16)],[1,1,2,2,3,3,99])

    def test_candidate_keeps_supply_cost(self):
        s=fixture(expand_mp=1);s.fleets[0].strength=3;apply(s,('expand',0),random.Random(0))
        self.assertEqual((s.supply,s.manpower,s.fleets[0].strength),(19,19,5))

    def test_raid_not_silently_resolved(self):
        s=fixture();s.event=5;self.assertFalse(any(a[0]=='assault' for a in legal(s,'fleet')))

if __name__=='__main__':unittest.main(verbosity=2)
