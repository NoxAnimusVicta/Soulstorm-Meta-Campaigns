"""Descriptive trait-matrix audit; no inferred human win rates or balance approval."""
import json,gzip,statistics,argparse
from pathlib import Path
from collections import Counter,defaultdict
from trait_qualification import cases
from sim_replay import inputs

def audit(folder):
 folder=Path(folder);specs={r['id']:r for r in cases((0,1))};expected=set(specs);rows=[]
 for file in sorted(folder.glob('s*-t*-p*-seat*.json')):
  row=json.loads(file.read_text());assert row['inputs']==inputs(),str(file)+' stale';rows.append(row)
 actual={r['cell']['id'] for r in rows};assert actual<=expected
 traits=defaultdict(list);policies=defaultdict(list);seats=defaultdict(list);actions=Counter();stalled=[]
 for r in rows:
  c=r['cell'];assert c==specs[c['id']]
  assert r['traits']==c['setup']['traits'] and r['policies']==c['setup']['policies']
  p=c['seat'];final=r['players'][p]
  sample=dict(survived=not final['eliminated'],holdings=final['holdings'],captures=final['captures'],sole_survivor=not final['eliminated'] and sum(not x['eliminated'] for x in r['players'])==1)
  for target,key in ((traits,c['trait']),(policies,c['policy']),(seats,str(p))):target[key].append(sample)
  for a in r['actions']:
   if a['player']==p:actions[a['action']]+=a['count']
  if 'one_major_coalition' not in r['milestones']:stalled.append(c['id'])
 def group(data):
  return {key:dict(games=len(vals),survivals=sum(v['survived'] for v in vals),sole_survivors=sum(v['sole_survivor'] for v in vals),mean_captures=statistics.mean(v['captures'] for v in vals),mean_holdings=statistics.mean(v['holdings'] for v in vals)) for key,vals in data.items()}
 milestones={}
 for key in ('one_major_coalition','all_holdings_and_mobile_capitals'):
  times=[r['milestones'][key] for r in rows if key in r['milestones']]
  milestones[key]=dict(observed=len(times),censored_at_100=len(rows)-len(times),observed_mean=statistics.mean(times) if times else None,observed_median=statistics.median(times) if times else None,minimum=min(times,default=None),maximum=max(times,default=None))
 return dict(expected=len(expected),completed=len(rows),complete=actual==expected,verified_orders=sum(r['verified_orders'] for r in rows),by_trait=group(traits),by_policy=group(policies),by_seat=group(seats),focal_actions=dict(actions),milestones=milestones,unresolved=stalled,inputs=inputs(),not_a_balance_conclusion=True)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('folder',nargs='?',default='trait-qualification-20260916');args=ap.parse_args();result=audit(args.folder)
 Path(args.folder,'summary.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ('inputs','focal_actions')},indent=2))
