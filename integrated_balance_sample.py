"""Connected campaign-notes baseline. Leaves qualified engine and campaign untouched."""
import concurrent.futures,gzip,hashlib,json,shutil,time
from pathlib import Path
from bot_qualification import play
from strategy_validation import TRAITS,POLICIES
from sim_replay import inputs
from verify_bot_trace import verify
from readiness import require_ready

OUT=Path('integrated-balance-20260917')
def specification(n):
 t,p,seat=n//18,(n//3)%6,n%3
 # Opponents fixed within policy/seat block for matched focal-trait comparisons.
 traits=[TRAITS[(p*2+seat+3)%12],TRAITS[(p*2+seat+8)%12]]
 policies=[POLICIES[(p+2)%6],POLICIES[(p+4)%6]]
 traits.insert(seat,TRAITS[t]);policies.insert(seat,POLICIES[p])
 return dict(traits=traits,policies=policies,initial_strength=5,minor_tier=2,rotation=0)
def run(n):
 dest=OUT/f'case-{n:03}.json'
 if dest.exists():return json.loads(dest.read_text(encoding='utf-8'))
 setup=specification(n);seat=n%3;p=(n//3)%6
 # Seed depends on block, not focal trait, and will be reused for rule packages.
 row,trace=play(case=p*3+seat,seed=1700+p*3+seat,cycles=100,large=True,setup=setup)
 row.update(sample_id=n,focal_seat=seat,classification='integrated notes baseline')
 row['verified_orders']=verify(row,trace)
 with gzip.open(OUT/f'case-{n:03}.trace.json.gz','wt',encoding='utf-8') as f:json.dump(trace,f,separators=(',',':'))
 dest.write_text(json.dumps(row,indent=2),encoding='utf-8')
 return row
def main():
 require_ready();OUT.mkdir(exist_ok=True)
 fingerprint=inputs()
 manifest=dict(status='running',games=216,cycles=100,systems=10,traits=list(TRAITS),policies=list(POLICIES),inputs=fingerprint,
  design='12 focal traits x 6 strategies x 3 seats; opponents/event seeds matched within strategy-seat blocks across traits and future packages',
  limits=['18 seed blocks, not 216 independent random replicates','One ten-system topology; map-generation table not approved','AI ground combat is not a human Soulstorm win-rate model','No candidate rules adopted'])
 path=OUT/'manifest.json'
 if path.exists():assert json.loads(path.read_text(encoding='utf-8'))['inputs']==fingerprint
 path.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
 pin=OUT/'inputs';pin.mkdir(exist_ok=True)
 for name in list(fingerprint)+['integrated_balance_sample.py','bot_qualification.py','verify_bot_trace.py']:
  shutil.copy2(name,pin/name)
 start=time.monotonic();rows=[]
 with concurrent.futures.ProcessPoolExecutor(max_workers=3) as pool:
  for row in pool.map(run,range(216)):
   rows.append(row)
   print(f"Completed {len(rows)}/216; case {row['sample_id']}; {round(time.monotonic()-start)}s",flush=True)
 assert inputs()==fingerprint
 (OUT/'results.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
 manifest.update(status='complete',verified_orders=sum(r['verified_orders'] for r in rows),elapsed_seconds=round(time.monotonic()-start))
 path.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
if __name__=='__main__':main()
