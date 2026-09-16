"""Summarise one shared baseline without treating post-conquest play as war."""
import gzip,json,statistics
from pathlib import Path
from collections import Counter,defaultdict
ROOT=Path('integrated-balance-20260917')
def mean(x):return round(statistics.mean(x),2) if x else None
def analyse():
 manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
 rows=[json.loads(p.read_text(encoding='utf-8')) for p in sorted(ROOT.glob('case-*.json'))]
 stats=[];actions=Counter();constructions=Counter();trait_groups=defaultdict(list)
 for r in rows:
  n=r['sample_id']
  with gzip.open(ROOT/f'case-{n:03}.trace.json.gz','rt',encoding='utf-8') as f:d=json.load(f)
  end=r['milestones'].get('all_holdings_and_mobile_capitals',100)
  competitive_end=r['milestones'].get('one_major_coalition',100)
  vals=[h['players'][p] for h in d['history'] if h['cycle']<=competitive_end for p in range(3) if not h['players'][p]['eliminated']]
  counts=Counter(e['order'][0] for e in d['orders'] if e['cycle']<=competitive_end)
  actions.update(counts)
  for e in d['orders']:
   if e['cycle']<=competitive_end and e['order'][0] in ('build','build_new','construct'):
    constructions[str(e['order'][1:])]+=1
  focal=r['focal_seat']
  focal_hist=[h['players'][focal] for h in d['history'] if h['cycle']<=competitive_end and not h['players'][focal]['eliminated']]
  s=dict(sample_id=n,trait=r['traits'][focal],policy=r['policies'][focal],seat=focal,
    control=r['milestones'].get('all_holdings_and_mobile_capitals'),
    coalition=r['milestones'].get('one_major_coalition'),
    alive_faction_cycles=len(vals),
    supply_mean=mean([v['supply'] for v in vals]),manpower_mean=mean([v['manpower'] for v in vals]),
    supply_low_cycles=sum(v['supply']<=5 for v in vals),manpower_low_cycles=sum(v['manpower']<=5 for v in vals),
    supply_locked_cycles=sum('supply' in v['deficits'] for v in vals),
    manpower_locked_cycles=sum('manpower' in v['deficits'] for v in vals),
    focal_supply_mean=mean([v['supply'] for v in focal_hist]),
    focal_manpower_mean=mean([v['manpower'] for v in focal_hist]),actions=dict(counts))
  stats.append(s);trait_groups[s['trait']].append(s)
 durations={}
 for key in ('coalition','control'):
  done=[r[key] for r in stats if r[key] is not None]
  durations[key]=dict(completed=len(done),censored=len(stats)-len(done),observed_mean=mean(done),
   observed_median=statistics.median(done) if done else None,observed_min=min(done) if done else None,
   observed_max=max(done) if done else None,restricted_mean_through_100=mean([r[key] or 100 for r in stats]))
 total=sum(r['alive_faction_cycles'] for r in stats)
 summary=dict(status=manifest['status'],completed_cases=len(rows),planned_cases=216,durations=durations,
  alive_faction_cycles=total,
  low_supply_percent=round(100*sum(r['supply_low_cycles'] for r in stats)/total,2) if total else None,
  low_manpower_percent=round(100*sum(r['manpower_low_cycles'] for r in stats)/total,2) if total else None,
  locked_supply_percent=round(100*sum(r['supply_locked_cycles'] for r in stats)/total,2) if total else None,
  locked_manpower_percent=round(100*sum(r['manpower_locked_cycles'] for r in stats)/total,2) if total else None,
  competitive_actions=dict(actions),cases=stats)
 (ROOT/'analysis.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
 text=['# Integrated campaign baseline — 17 September 2026','',
  f"Status: **{manifest['status']}**. {len(rows)}/216 campaigns available. No candidate rules have been adopted.",
  '', 'This is a shared current-rules sample for the full campaign-notes review. Each game has ten systems and 100 observed Cycles. Twelve focal traits, six strategies and three seats are crossed. There are 18 matched seed blocks; these are not 216 independent replicates. All results use AI resolution and one synthetic geography.',
  '', '## Duration','', '| Milestone | Reached | Unfinished at 100 | Mean among completed | Median among completed | Observed range |','|---|---:|---:|---:|---:|---|']
 for key,v in durations.items():text.append(f"| {key} | {v['completed']} | {v['censored']} | {v['observed_mean']} | {v['observed_median']} | {v['observed_min']}–{v['observed_max']} |")
 text+=['','Completed-only averages omit unfinished wars and cannot establish an uncensored average campaign length. The design target is 50–100 Cycles on average, with shorter outliers, not a requirement that every game last that long.',
 '', '## Shared resource and choice observations','',
 'Measurements below stop at the first single-Major-coalition milestone (or Cycle 100) and exclude eliminated factions. They use end-of-Cycle stocks, so cannot detect every within-turn shortage. The same populations and cutoff apply to both resources.',
 '',f"- Supply at 5 or below: {summary['low_supply_percent']}% of surviving faction-Cycles.",
 f"- Manpower at 5 or below: {summary['low_manpower_percent']}%.",
 f"- Supply locked by deficit: {summary['locked_supply_percent']}%.",
 f"- Manpower locked by deficit: {summary['locked_manpower_percent']}%.",
 '', '| Action | Recorded competitive-period orders |','|---|---:|']
 text += [f'| {a} | {n} |' for a,n in actions.most_common() if a!='none']
 text += ['','Action frequency measures bot behaviour, not the intrinsic value of a rule. Targeted opportunities and alternative policies are needed before declaring a rarely selected construction or attack ineffective.',
 '', '## Connected review','',
 'Read Integrated_Balance_Review.md for the full issue map. Consider resource demand, construction concentration, resistance and combat choices together. These baseline observations are not evidence that a proposed package improves the system; no package comparison has yet been conducted. Player-specific trait value, thematic map selection, Sector design and personnel lifespans are not resolved by this numerical sample.']
 Path('Integrated_Balance_Baseline_Report.md').write_text('\n'.join(text).replace('\\n','\n'),encoding='utf-8')
 print(json.dumps({k:v for k,v in summary.items() if k not in ('cases','competitive_actions')},indent=2))
if __name__=='__main__':analyse()
