from pathlib import Path
import json,zipfile,hashlib
from sim_replay import inputs
root=Path('.')
files=set(inputs())|{'package_integrated_review.py','readiness.py','simulation_readiness.json','bot_qualification.py','verify_bot_trace.py','integrated_balance_sample.py','analyse_integrated_balance.py','audit_campaign_notes.py','balance_microtests_20260917.py','investigate_campaign_tails.py','Campaign_Notes_Review_2026-09-17.md','Campaign_Notes_2026-09-15.md','Integrated_Balance_Baseline_Report.md','Integrated_Balance_Review.md','Integrated_Notes_Evidence.json','Balance_Microtests_20260917.json','Simulation_Development_Handover.md'}
for folder in ('integrated-balance-20260917','integrated-notes-investigation-20260917'):
 files.update(str(p) for p in Path(folder).rglob('*') if p.is_file())
manifest={name:hashlib.sha256(Path(name).read_bytes()).hexdigest() for name in sorted(files)}
Path('Integrated_Review_Evidence_Manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
files.add('Integrated_Review_Evidence_Manifest.json')
with zipfile.ZipFile('Integrated_Balance_Evidence_20260917.zip','w',zipfile.ZIP_DEFLATED) as z:
 for name in sorted(files):z.write(name)
with zipfile.ZipFile('Integrated_Balance_Evidence_20260917.zip') as z:
 assert z.testzip() is None
 assert sum(n.endswith('.trace.json.gz') for n in z.namelist())==221
print('Evidence zip MiB',round(Path('Integrated_Balance_Evidence_20260917.zip').stat().st_size/1048576,2))
