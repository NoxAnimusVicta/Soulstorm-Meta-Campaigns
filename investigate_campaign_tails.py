import concurrent.futures,gzip,json
from pathlib import Path
from bot_qualification import play
from verify_bot_trace import verify
from sim_replay import inputs
ROOT=Path('integrated-balance-20260917')
OUT=Path('integrated-notes-investigation-20260917')
def run(r):
 row,trace=play(case=r['case'],seed=r['seed'],cycles=200,large=True,setup=r['setup'])
 old=json.load(gzip.open(ROOT/f"case-{r['sample_id']:03}.trace.json.gz",'rt',encoding='utf-8'))
 assert trace['history'][:100]==old['history']
 assert json.loads(json.dumps(trace['orders'][:len(old['orders'])]))==old['orders']
 row['sample_id']=r['sample_id'];row['verified_orders']=verify(row,trace)
 with gzip.open(OUT/f"tail-{r['sample_id']:03}.trace.json.gz",'wt',encoding='utf-8') as f:json.dump(trace,f)
 (OUT/f"tail-{r['sample_id']:03}.json").write_text(json.dumps(row,indent=2),encoding='utf-8')
 return dict(id=r['sample_id'],milestones=row['milestones'],verified_orders=row['verified_orders'])
if __name__=='__main__':
 OUT.mkdir(exist_ok=True);rows=json.loads((ROOT/'results.json').read_text())
 pending=[r for r in rows if 'all_holdings_and_mobile_capitals' not in r['milestones']]
 with concurrent.futures.ProcessPoolExecutor(max_workers=3) as pool:
  result=list(pool.map(run,pending))
 (OUT/'tails.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps(result,indent=2),flush=True)
