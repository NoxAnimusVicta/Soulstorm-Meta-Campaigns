"""Random legal-action stress checks; NOT strategic play or balance evidence."""
import argparse,hashlib,json,random
from pathlib import Path
from shared_sim import Arena
from sim_replay import Replay

def run(seed,cycles):
 arena=Arena();arena.add_minor([(2,4,4,3,False),(1,2,2,3,False)])
 replay=Replay(arena,7000+seed);selection=random.Random(6000+seed)
 for _ in range(cycles):
  replay.apply(('opening',))
  if arena.stop:break
  for p in arena.turns():
   if p in arena.eliminated:continue
   replay.apply(('begin',p))
   for phase in ('fleet','faction','social','construction'):
    attempts=len(arena.players[p].fleets)+1 if phase=='fleet' else 1
    for _ in range(attempts):
     order=selection.choice(arena.actions(p,phase))
     replay.apply(('submit',p,phase,order))
     if order[0]=='none' or arena.stop:break
    if arena.stop:break
   if arena.stop:break
  if arena.stop:break
  replay.apply(('closing',))
 replay.verify()
 return replay.document(),arena.stop

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--out',default='mechanics-diagnostics-20260916');parser.add_argument('--seeds',type=int,default=8);parser.add_argument('--cycles',type=int,default=8);args=parser.parse_args()
 out=Path(args.out);out.mkdir(exist_ok=True);results=[]
 for seed in range(args.seeds):
  document,stop=run(seed,args.cycles)
  (out/f'replay-{seed}.json').write_text(json.dumps(document,indent=2),encoding='utf-8')
  results.append(dict(seed=seed,commands=len(document['commands']),stop=stop,replay_verified=True))
 from sim_replay import inputs as core_inputs
 inputs=list(core_inputs())+['readiness.py','mechanics_smoke.py']
 (out/'inputs').mkdir(exist_ok=True)
 hashes={}
 for name in inputs:
  data=Path(name).read_bytes();(out/'inputs'/name).write_bytes(data);hashes[name]=hashlib.sha256(data).hexdigest()
 (out/'manifest.json').write_text(json.dumps(dict(classification='Random legality stress and deterministic replay; NOT balance evidence',cycles=args.cycles,results=results,inputs=hashes),indent=2),encoding='utf-8')
 print(json.dumps(results))
