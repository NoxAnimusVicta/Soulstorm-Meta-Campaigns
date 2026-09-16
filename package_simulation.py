from pathlib import Path
import shutil, zipfile
root=Path(__file__).resolve().parent
archive=root/'Historical_Frontier_Pilot.zip'
if not archive.exists():
    raise SystemExit('Historical archive missing: preserve the original published pilot bundle before packaging.')
with zipfile.ZipFile(root/'Balance_Simulation_Bundle.zip','w',zipfile.ZIP_DEFLATED) as z:
    names=['Historical_Frontier_Pilot.zip','Historical_Shared_Checkpoint_20260915.zip','balance_sim.py','balance_tests.py','shared_sim.py','shared_tests.py','strategic_planner.py','planner_experiment.py','package_simulation.py','Simulation_Development_Handover.md','Balance_Simulation_Methods.md','Balance_Simulation_Report.md','Source_Rules.md']
    for name in names:z.write(root/name,name)
    for name in ('construction_rules.py','construction_tests.py','battle_setup.py','battle_setup_tests.py','Simulation_Mechanics_Coverage.md'):z.write(root/name,name)
    for p in sorted((root/'shared-results-v2').glob('*.json')):z.write(p,'shared-results-v2/'+p.name)
    for folder in ('planner-results-20260916','planner-results-20260916-ruling'):
        for p in sorted((root/folder).rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts:z.write(p,p.relative_to(root).as_posix())
print('Bundle includes current code, full shared traces, handover and intact historical pilot.')
