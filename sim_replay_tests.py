import unittest,random,json
from shared_sim import Arena
from balance_sim import Project
from sim_replay import snapshot,restore,digest,Replay,verify

class ReplayTests(unittest.TestCase):
 def test_roundtrip_preserves_capacity_and_tuple_keys(self):
  a=Arena();a.players[0].projects=[Project('flagship',('fleet',0),4,5,False)]
  a.act(0,('build',0),random.Random(0))
  a.alliances.add(frozenset((0,1)));a.defence_choices[(0,1)]=((0,1),)
  b=restore(snapshot(a))
  self.assertEqual(digest(a),digest(b))
  self.assertEqual(b.players[0].projects[0].granted_capacity,5)
  b.players[0].hit_fleet(0,1)
  self.assertEqual(b.players[0].projects[0].integrity,5)

 def test_replay_checks_every_transition(self):
  replay=Replay(Arena(),2)
  replay.apply(('opening',));replay.apply(('begin',0))
  order=replay.arena.actions(0,'faction')[0]
  replay.apply(('submit',0,'faction',order));replay.apply(('closing',))
  self.assertEqual(digest(replay.verify()),digest(replay.arena))
  document=replay.document();document['commands'][0]['after']='tampered'
  with self.assertRaises(ValueError):verify(document)

 def test_unknown_types_rejected(self):
  with self.assertRaises(ValueError):restore(json.dumps({'schema':1,'arena':{'$type':'os.system','fields':{}}}))
