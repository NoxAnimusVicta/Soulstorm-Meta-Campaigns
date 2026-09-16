"""Readiness gate for controlled baseline experiments; no claim of game balance."""
import json
from pathlib import Path
from sim_replay import inputs

def require_ready():
 path=Path(__file__).resolve().parent/'simulation_readiness.json'
 if not path.exists():raise RuntimeError('Run final validation and record readiness first')
 status=json.loads(path.read_text(encoding='utf-8'))
 if status.get('status')!='ready_for_baseline_testing' or status.get('inputs')!=inputs():
  raise RuntimeError('Readiness is missing or stale for these engine/rule inputs')
 return status
