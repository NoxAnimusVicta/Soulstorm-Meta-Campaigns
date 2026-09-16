"""Matched factorial trait/strategy/seat qualification; traits never change mid-game."""
import argparse,json,shutil,time
from pathlib import Path
from bot_qualification import play
from strategy_validation import TRAITS,POLICIES
from sim_replay import inputs
from verify_bot_trace import verify

def cases(seeds=(0,1)):
 for seed in seeds:
  for ti,trait in enumerate(TRAITS):
   for pi,policy in enumerate(POLICIES):
    for seat in range(3):
     # Opponents and world conditions depend on replicate only, not focal trait.
     # Rotating their labels across replicates avoids a fixed trait matchup.
     ts=[TRAITS[(seed*5+i*4+1)%len(TRAITS)] for i in range(3)]
     ps=[POLICIES[(seed+i*2+1)%len(POLICIES)] for i in range(3)]
     ts[seat]=trait;ps[seat]=policy
     yield dict(id=f's{seed}-t{ti}-p{pi}-seat{seat}',seed=seed,trait=trait,policy=policy,seat=seat,
      setup=dict(traits=ts,policies=ps,initial_strength=(1,4,5)[seed%3],minor_tier=(1,2,3)[seed%3],rotation=0))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--seeds',nargs='+',type=int,default=[0,1]);ap.add_argument('--shard',type=int,default=0);ap.add_argument('--shards',type=int,default=1);ap.add_argument('--out',default='trait-qualification-20260916');args=ap.parse_args()
 out=Path(args.out);out.mkdir(parents=True,exist_ok=True);pin=out/'inputs';pin.mkdir(exist_ok=True)
 for name in list(inputs())+['bot_qualification.py','trait_qualification.py','verify_bot_trace.py']:
  target=pin/name
  if target.exists():assert target.read_bytes()==Path(name).read_bytes(),'Changed inputs: use a fresh output directory'
  else:shutil.copy2(name,target)
 rows=[];start=time.monotonic()
 for cell in cases(args.seeds):
  if cell['seat']%args.shards!=args.shard:continue
  path=out/(cell['id']+'.json')
  if path.exists():continue
  row,trace=play(case=0,seed=cell['seed'],cycles=100,setup=cell['setup'])
  row['cell']=cell;row['verified_orders']=verify(row,trace)
  # Keep complete evidence compressed; every submitted order remains replayable.
  import gzip
  with gzip.open(out/(cell['id']+'.trace.json.gz'),'wt',encoding='utf-8') as f:json.dump(trace,f)
  path.write_text(json.dumps(row,indent=2),encoding='utf-8');rows.append(row)
  print(cell['id'],[p['holdings'] for p in row['players']],round(time.monotonic()-start),flush=True)
if __name__=='__main__':main()
