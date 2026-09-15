from pathlib import Path
import shutil, zipfile
root=Path(__file__).resolve().parent
archive=root/'Historical_Frontier_Pilot.zip'
if not archive.exists():
    raise SystemExit('Historical archive missing: preserve the original published pilot bundle before packaging.')
with zipfile.ZipFile(root/'Balance_Simulation_Bundle.zip','w',zipfile.ZIP_DEFLATED) as z:
    names=['Historical_Frontier_Pilot.zip','balance_sim.py','balance_tests.py','shared_sim.py','shared_tests.py','package_simulation.py','Simulation_Development_Handover.md','Balance_Simulation_Methods.md','Balance_Simulation_Report.md','Source_Rules.md']
    for name in names:z.write(root/name,name)
    for p in sorted((root/'shared-results-v2').glob('*.json')):z.write(p,'shared-results-v2/'+p.name)
print('Bundle includes current code, full shared traces, handover and intact historical pilot.')
