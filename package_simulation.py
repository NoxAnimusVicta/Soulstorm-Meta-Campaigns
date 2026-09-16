"""Package runnable source, qualification evidence and preserved historical work."""
from pathlib import Path
import zipfile
root=Path(__file__).resolve().parent
required=['Historical_Frontier_Pilot.zip','Historical_Shared_Checkpoint_20260915.zip','simulation_readiness.json','Simulation_Readiness_Report.md','Bot_Behaviour_Review.json']
for name in required:
 if not (root/name).exists():raise SystemExit('Required release artifact missing: '+name)
paths={root/name for name in required}
from sim_replay import inputs
paths.update(root/name for name in inputs())
paths.update(root/name for name in ('balance_tests.py','shared_tests.py','construction_tests.py','battle_setup_tests.py','sim_replay_tests.py','sim_scenario_tests.py','ruling_tests.py','coalition_tests.py','strategy_tests.py','search_assessment_tests.py','siege_diagnostic_tests.py','operational_bot_tests.py','bot_trait_tests.py','mechanics_smoke.py','readiness.py','validate_release.py','bot_qualification.py','trait_qualification.py','verify_bot_trace.py','audit_trait_matrix.py','write_trait_report.py','write_release_report.py','inspect_unfinished_traits.py','package_simulation.py'))
paths.update(p for p in root.glob('*.md') if p.name!='Dessica_Campaign.md')
historical=[p for name in ['strategy-assessment-20260916','stagnation-investigation-20260916'] for p in (root/name).rglob('*') if p.is_file() and '__pycache__' not in p.parts]
if historical:
 with zipfile.ZipFile(root/'Historical_Bot_Diagnostics.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for path in sorted(historical):z.write(path,path.relative_to(root).as_posix())
for name in ['trait-qualification-20260916','bot-current-20260916']:
 paths.update(p for p in (root/name).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
with zipfile.ZipFile(root/'Balance_Simulation_Bundle.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for path in sorted(paths):z.write(path,path.relative_to(root).as_posix())
print('Packaged',len(paths),'files;',round((root/'Balance_Simulation_Bundle.zip').stat().st_size/1048576,2),'MiB; campaign ledger excluded.')
