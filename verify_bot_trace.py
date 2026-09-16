"""Replay recorded orders through public validation, without reselecting them."""
import json,random
from pathlib import Path
from sim_replay import restore,digest,decode
from bot_control import coordinate,social

def tuples(x):return tuple(tuples(y) for y in x) if isinstance(x,list) else x

def verify(row,doc):
 a=restore(doc['initial']);rng=random.Random(1000+row['case']+row['seed']*10000)
 commands=iter(doc['orders']);count=0;policies=row['policies']
 for cycle in range(1,row['cycles']+1):
  a.opening(random.Random(100000+row['case']*100+a.cycle+row['seed']*1000000))
  for p in a.turns():
   a.begin_turn(p);coordinate(a,p,policies)
   for phase in ('fleet','faction','social','construction'):
    if phase=='social':social(a,p,policies,rng);continue
    for _ in range(sum(len(s.fleets) for s in a.players)+1 if phase=='fleet' else 1):
     entry=next(commands);assert (entry['cycle'],entry['player'],entry['phase'])==(cycle,p,phase)
     memory=decode(entry['bot_memory'])
     for field,key in [('bot_plans','plans'),('diagnostic_targets','diagnostic')]:
      if memory[key] or hasattr(a,field):setattr(a,field,memory[key])
     order=tuples(entry['order']);a.submit(p,phase,order,rng);count+=1
     assert digest(a)==entry['after'],f'Command {count} diverged: Cycle{cycle}, {p}, {phase}'
     if order[0]=='none':break
  a.closing();a.check()
 assert next(commands,None) is None
 assert digest(a)==row['final'] and digest(restore(doc['final']))==row['final']
 return count

if __name__=='__main__':
 import sys
 folder=Path(sys.argv[1]);rows=json.loads((folder/'results.json').read_text());total=0
 for i,row in enumerate(rows):
  n=verify(row,json.loads((folder/f'trace-{i}.json').read_text()));total+=n;print(i,n,flush=True)
 print('Verified',total,'publicly validated orders')
