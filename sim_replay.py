"""Versioned JSON snapshots and deterministic command replay; never pickle/code."""
import hashlib,json,random
from pathlib import Path
from shared_sim import Arena,SharedState,Holding
from balance_sim import Fleet,World,Project

TYPES={c.__name__:c for c in (Arena,SharedState,Holding,Fleet,World,Project)}

def inputs():
 root=Path(__file__).resolve().parent
 names=('shared_sim.py','balance_sim.py','construction_rules.py','battle_setup.py','sim_replay.py','Source_Rules.md')
 return {name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in names}

def encode(value):
 if value is None or type(value) in (str,int,float,bool):return value
 if type(value) is list:return [encode(v) for v in value]
 if type(value) is tuple:return {'$tuple':[encode(v) for v in value]}
 if type(value) is set:return {'$set':[encode(v) for v in sorted(value,key=repr)]}
 if type(value) is frozenset:return {'$frozenset':[encode(v) for v in sorted(value,key=repr)]}
 if type(value) is dict:return {'$dict':[[encode(k),encode(v)] for k,v in sorted(value.items(),key=lambda kv:repr(kv[0]))]}
 if type(value).__name__ in TYPES and TYPES[type(value).__name__] is type(value):
  return {'$type':type(value).__name__,'fields':encode(vars(value))}
 raise TypeError('Unsupported snapshot value: '+type(value).__name__)

def decode(value):
 if type(value) is list:return [decode(v) for v in value]
 if type(value) is not dict:return value
 if '$tuple' in value:return tuple(decode(v) for v in value['$tuple'])
 if '$set' in value:return set(decode(v) for v in value['$set'])
 if '$frozenset' in value:return frozenset(decode(v) for v in value['$frozenset'])
 if '$dict' in value:return {decode(k):decode(v) for k,v in value['$dict']}
 if value.get('$type') not in TYPES:raise ValueError('Unknown snapshot type')
 cls=TYPES[value['$type']];obj=cls.__new__(cls);obj.__dict__.update(decode(value['fields']))
 return obj

def snapshot(arena):return json.dumps({'schema':1,'arena':encode(arena)},sort_keys=True,separators=(',',':'))
def restore(text):
 document=json.loads(text)
 if document.get('schema')!=1:raise ValueError('Unsupported snapshot schema')
 arena=decode(document['arena'])
 if type(arena) is not Arena:raise ValueError('Snapshot does not contain an Arena')
 for player in arena.players:player.validate()
 return arena

def digest(arena):return hashlib.sha256(snapshot(arena).encode()).hexdigest()

class Replay:
 def __init__(self,arena,seed):
  self.arena=arena;self.initial=snapshot(arena);self.seed=seed;self.rng=random.Random(seed);self.commands=[]
 def apply(self,command):
  kind=command[0]
  if kind=='opening':self.arena.opening(self.rng)
  elif kind=='closing':self.arena.closing()
  elif kind=='begin':self.arena.begin_turn(command[1])
  elif kind=='submit':self.arena.submit(command[1],command[2],command[3],self.rng)
  else:raise ValueError('Unknown replay command')
  self.commands.append({'command':encode(command),'after':digest(self.arena)})
 def document(self):return dict(schema=1,inputs=inputs(),initial=self.initial,seed=self.seed,commands=self.commands)

 def verify(self):return verify(self.document())

def verify(document):
 if document.get('schema')!=1:raise ValueError('Unsupported replay schema')
 if document.get('inputs')!=inputs():raise ValueError('Replay requires its pinned engine and rule inputs')
 replay=Replay(restore(document['initial']),document['seed'])
 for index,entry in enumerate(document['commands']):
  replay.apply(decode(entry['command']))
  if replay.commands[-1]['after']!=entry['after']:raise ValueError('Replay divergence at command '+str(index))
 return replay.arena
