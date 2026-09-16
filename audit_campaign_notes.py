import gzip,json,statistics
from collections import Counter,defaultdict
from pathlib import Path
from sim_replay import restore
root=Path('integrated-balance-20260917')
rows=json.loads((root/'results.json').read_text())
profiles=Counter();first=Counter();host_types=Counter();starts_by_trait=defaultdict(Counter);combat=defaultdict(Counter);events=Counter();traits=defaultdict(list);stocks=defaultdict(list);unfinished=[]
for r in rows:
 d=json.load(gzip.open(root/f"case-{r['sample_id']:03}.trace.json.gz",'rt',encoding='utf-8'))
 end=r['milestones'].get('one_major_coalition',100);init=restore(d['initial']);final=restore(d['final'])
 seen=set()
 for o in d['orders']:
  if o['cycle']>end:continue
  if o['order'][0]=='start':
   profile,host=o['order'][1:];profiles[profile]+=1;starts_by_trait[r['traits'][o['player']]][profile]+=1
   if o['player'] not in seen:first[profile]+=1;seen.add(o['player'])
   category='fleet' if isinstance(host,list) and host[0]=='fleet' else 'system' if isinstance(host,list) else 'original_capital' if host in (init.capitals[o['player']],-1) else 'other_holding'
   host_types[category]+=1
 for h in d['history']:
  if h['cycle']>end:continue
  for p in range(3):
   s=h['players'][p]
   if not s['eliminated']:
    for resource in ('supply','manpower'):stocks[resource].append(s[resource])
 for e in d['log']:
  if e.get('cycle',0)>end:continue
  if e.get('action')=='event':events[str(e.get('table'))]+=1
  if e.get('combat')=='ground' and e.get('rolls'):
   at,de=e['totals'];ar,dr=e['rolls'][:2];gap=(at-ar)-(de-dr)
   target='minor' if init.players[e['defender']].role=='minor' else 'major'
   combat[target]['battles']+=1;combat[target]['attacker_wins']+=bool(e['won'])
   combat[target]['deterministic']+=(gap<=-19 or gap>=20)
   combat[target]['guaranteed_loss']+=gap<=-19
   combat[target]['guaranteed_win']+=gap>=20
  if e.get('combat')=='naval':
   combat['naval']['battles']+=1;combat['naval']['wipeout_margin']+=abs(e['margin'])>=16
 focal=r['focal_seat'];atend=d['history'][end-1]['players'][focal]
 traits[r['traits'][focal]].append(dict(id=r['sample_id'],survives=not atend['eliminated'],holdings=atend['holdings'],control=r['milestones'].get('all_holdings_and_mobile_capitals'),supply=atend['supply'],manpower=atend['manpower']))
 if 'all_holdings_and_mobile_capitals' not in r['milestones']:
  c=Counter(o['order'][0] for o in d['orders'] if o['cycle']>80 and o['order'][0]!='none')
  unfinished.append(dict(id=r['sample_id'],actions_last20=dict(c),players=r['players']))
out=dict(construction_starts=dict(profiles),first_construction=dict(first),construction_hosts=dict(host_types),combat={k:dict(v) for k,v in combat.items()},events=dict(events),stocks={k:dict(mean=statistics.mean(v),median=statistics.median(v),over40=sum(x>40 for x in v)/len(v),over60=sum(x>60 for x in v)/len(v),n=len(v)) for k,v in stocks.items()},traits={k:dict(n=len(v),survival=sum(x['survives'] for x in v),mean_holdings=statistics.mean(x['holdings'] for x in v)) for k,v in traits.items()},unfinished=unfinished)
Path('Integrated_Notes_Evidence.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('unfinished','events')},indent=2))
