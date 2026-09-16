"""Paired planner-depth integration experiment; not a balance ranking."""
import argparse,hashlib,json,time,shutil
from pathlib import Path
from shared_sim import run
p=argparse.ArgumentParser();p.add_argument('--cycles',type=int,default=6);p.add_argument('--seeds',type=int,default=2);p.add_argument('--out',default='planner-results');p.add_argument('--diagnostic',action='store_true');args=p.parse_args()
if not args.diagnostic:p.error('Balance studies are locked until mechanics coverage is complete. Use --diagnostic only for implementation checks.')
out=Path(args.out);out.mkdir(exist_ok=True);rows=[];began=time.monotonic()
files=['shared_sim.py','balance_sim.py','construction_rules.py','strategic_planner.py','planner_experiment.py','Source_Rules.md']
(out/'inputs').mkdir(exist_ok=True)
for f in files:shutil.copyfile(f,out/'inputs'/f)
hashes={f:hashlib.sha256((out/'inputs'/f).read_bytes()).hexdigest() for f in files}
for depth in (0,1):
    for seed in range(args.seeds):
        for rotation in range(3):
            row,trace=run(seed,args.cycles,20,rotation,planner_depth=depth,policy_rotation=seed%3)
            rows.append(row)
            (out/f'trace-d{depth}-s{seed}-r{rotation}.json').write_text(json.dumps(trace,indent=2))
            (out/'trials.json').write_text(json.dumps(rows,indent=2))
            print('depth',depth,'seed',seed,'rotation',rotation,'cycles',row['cycles'],'stop',row['stop'],'elapsed',round(time.monotonic()-began),flush=True)
manifest=dict(cycles=args.cycles,seeds=args.seeds,hashes=hashes,
    assumptions=['Major-only synthetic map','Future events privately sampled, never read from realised RNG','Depth 1 adds remainder of current Cycle and one full future Cycle with greedy opponent replies','Common sampled futures across candidates; bounded shortlist preserves investment options','Defender action retention and ground/fleet ties remain provisional','Raids defer assaults; four economic profiles only','Capital recovery precedes rationing per 16 September ruling','Policy rotation linked to seed in this small integration batch; no trait ranking','Direct mobile assaults use explicit destruction penalties; additional ordinary-fleet Planet Fall damage on mobile destruction not applied','No human battle model'])
(out/'manifest.json').write_text(json.dumps(manifest,indent=2))
