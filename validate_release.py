"""Require current trait matrix, replay and controller evidence before baseline use."""
import json,unittest,gzip,hashlib
from datetime import datetime
from pathlib import Path
from sim_replay import inputs,restore,digest
from audit_trait_matrix import audit
from verify_bot_trace import verify
MODULES=('balance_tests','shared_tests','construction_tests','battle_setup_tests','sim_replay_tests','sim_scenario_tests','ruling_tests','coalition_tests','strategy_tests','search_assessment_tests','siege_diagnostic_tests','operational_bot_tests','bot_trait_tests')

def main():
 result=unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromNames(MODULES))
 assert result.wasSuccessful(),'Regression failure'
 hashes=inputs();folder=Path('trait-qualification-20260916');summary=audit(folder)
 assert summary['complete'],'Trait/strategy/seat matrix incomplete'
 evidence={};orders=0
 for p in sorted(folder.glob('s*-t*-p*-seat*.json')):
  row=json.loads(p.read_text());trace=folder/(row['cell']['id']+'.trace.json.gz')
  doc=json.load(gzip.open(trace,'rt',encoding='utf-8'))
  assert row['cycles']==100 and row['verified_orders']==len(doc['orders'])
  initial=restore(doc['initial']);assert [p.trait for p in initial.players[:3]]==row['traits']
  assert row['inputs']==hashes and digest(restore(doc['final']))==row['final']
  assert [e['cycle'] for e in doc['log'] if e.get('action')=='event']==list(range(1,101))
  evidence[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest();evidence[str(trace)]=hashlib.sha256(trace.read_bytes()).hexdigest()
  orders+=row['verified_orders']
 groups={}
 for name,count,repeated in [('repeat',8,True),('large',2,False),('allied',2,True),('challenger-seat0',4,False),('challenger-seat1',4,False),('challenger-seat2',4,False),('independent-baseline',4,False),('legacy-opponents',3,False)]:
  base=Path('bot-current-20260916')/name;rows=json.loads((base/'results.json').read_text());assert len(rows)==count,name
  verified=0
  for i,row in enumerate(rows):
   assert row['inputs']==hashes and row['cycles']==100 and (not repeated or row.get('reproduced'))
   verified+=verify(row,json.loads((base/f'trace-{i}.json').read_text()))
  groups[name]=dict(games=count,repeated=repeated,verified_orders=verified);print(name,'verified',verified,flush=True)
 stress=json.loads(Path('bot-current-20260916/stress/manifest.json').read_text())
 assert len(stress['results'])==24 and stress['cycles']==24
 assert all(r['replay_verified'] and not r['stop'] for r in stress['results'])
 assert all(stress['inputs'][name]==value for name,value in hashes.items())
 fresh=json.loads(Path('bot-current-20260916/fresh-process/fresh-process-match.json').read_text())
 assert fresh['matched'] and fresh['inputs']==hashes
 tail=Path('bot-current-20260916/long-tail');tailrow=json.loads((tail/'results.json').read_text())[0]
 assert tailrow['inputs']==hashes and tailrow['cycles']==200
 tailverified=verify(tailrow,json.loads((tail/'trace-0.json').read_text()))
 groups['long-tail']=dict(games=1,cycles=200,verified_orders=tailverified)
 review=json.loads(Path('Bot_Behaviour_Review.json').read_text())
 assert review['inputs']==hashes and review['reviewed'] and review['blocking_bot_failures']==[], 'Behaviour review missing or unresolved'
 status=dict(status='ready_for_baseline_testing',scope='Numerical Subsector; operational controller, horizon zero; sensitivity comparisons, not human or optimal-play certification',date=datetime.now().date().isoformat(),tests=result.testsRun,inputs=hashes,trait_matrix=summary,cohorts=groups,stress_cases=24,review=review,evidence=evidence,not_a_balance_conclusion=True,limitations=['Two matrix replicates are a coverage screen, not precise trait rankings','Three-system matrix and separate ten-system checks are synthetic fixtures','Human battle results remain external','Optional sampled search is experimental, not qualified here','Rare actions may require dedicated strategy scenarios','Ending criterion unresolved; coalition/control milestones reported separately'])
 Path('simulation_readiness.json').write_text(json.dumps(status,indent=2),encoding='utf-8')
 print('Ready for scoped baseline testing;',result.testsRun,'tests;',orders,'matrix orders')
if __name__=='__main__':main()
