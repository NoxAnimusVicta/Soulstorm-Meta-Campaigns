"""Controlled baseline/sensitivity trials. Proposed variants never edit campaign rules."""
import argparse,hashlib,itertools,json,random,shutil,time
from pathlib import Path
from sim_scenarios import campaign_fixture
from sim_replay import inputs,snapshot,digest
from shared_sim import POLICY_WEIGHTS,choose,policy_for
from bot_control import coordinate,social
from strategy_validation import TRAITS
from readiness import require_ready

def simulate(*,trait,policy,seat,seed,cycles=100,horizon=0,initial_strength=5,minor_tier=2,expand_mp=0,create_mp=1,raid_total=45,controllers=('operational','operational','operational'),opponent_traits=('efficient','siege'),opponent_policies=('raider','industrial')):
 traits=list(opponent_traits);traits.insert(seat,trait)
 policies=list(opponent_policies);policies.insert(seat,policy)
 a=campaign_fixture(tuple(traits),initial_strength,minor_tier)
 a.bot_controller_modes=dict(enumerate(controllers))
 for s in a.players:s.expand_mp=expand_mp;s.create_mp=create_mp
 a.defender_policies=dict(enumerate(policies));a.raid_profile.update(strength=5,supply=(raid_total-5)//2,manpower=raid_total-5-(raid_total-5)//2)
 initial=snapshot(a);combat=random.Random(seed+700000);decision=0;orders=[]
 for _ in range(cycles):
  # Event draws remain paired by seed/Cycle even if a variant changes battle counts.
  a.opening(random.Random(seed*100000+a.cycle+9000000))
  for p in a.turns():
   a.begin_turn(p);coordinate(a,p,policies)
   for phase in ('fleet','faction','social','construction'):
    if phase=='social':social(a,p,policies,combat);continue
    for _ in range(sum(len(s.fleets) for s in a.players)+1 if phase=='fleet' else 1):
     from bot_dispatch import select_order
     action=select_order(a,p,phase,policies,decision,horizon)
     decision+=1;a.submit(p,phase,action,combat)
     orders.append(dict(cycle=a.cycle,player=p,phase=phase,order=action,after=digest(a)))
     if action[0]=='none':break
   if a.stop:raise RuntimeError(a.stop)
  a.closing()
 counts={}
 for e in a.log:
  if e.get('player')==seat and 'action' in e:counts[e['action']]=counts.get(e['action'],0)+1
 s=a.players[seat]
 row=dict(trait=trait,policy=policy,seat=seat,seed=seed,cycles=cycles,horizon=horizon,controllers=controllers,opponent_traits=opponent_traits,opponent_policies=opponent_policies,initial_strength=initial_strength,minor_tier=minor_tier,expand_mp=expand_mp,create_mp=create_mp,raid_total=raid_total,eliminated=seat in a.eliminated,supply=s.supply,manpower=s.manpower,deficit_entries=sum(v for k,v in s.counts.items() if k.startswith('deficit_')),recovery_progress=s.deficits,holdings=sum(w.owner==seat for w in a.holdings),holding_tiers=sum(w.tier for w in a.holdings if w.owner==seat),coalition_holdings=sum(a.allied(seat,w.owner) for w in a.holdings),fleet_strength=sum(f.strength for f in s.fleets),active_constructions=sum(p.active for p in s.projects),actions=counts,final=digest(a),stop=a.stop)
 return row,dict(initial=initial,final=snapshot(a),orders=orders,log=a.log)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--diagnostic',action='store_true');ap.add_argument('--traits',nargs='+',default=list(TRAITS));ap.add_argument('--policies',nargs='+',default=list(POLICY_WEIGHTS));ap.add_argument('--seats',nargs='+',type=int,default=[0,1,2]);ap.add_argument('--seeds',type=int,default=4);ap.add_argument('--cycles',type=int,default=100);ap.add_argument('--horizon',type=int,default=0);ap.add_argument('--initial-strength',type=int,default=5);ap.add_argument('--minor-tier',type=int,default=2);ap.add_argument('--expand-mp',type=int,default=0);ap.add_argument('--create-mp',type=int,default=1);ap.add_argument('--raid-total',type=int,default=45);ap.add_argument('--out',default='balance-results');ap.add_argument('--controllers',nargs=3,choices=['operational','tactical','diagnostic'],default=['operational']*3);ap.add_argument('--opponent-traits',nargs=2,choices=TRAITS,default=['efficient','siege']);ap.add_argument('--opponent-policies',nargs=2,choices=list(POLICY_WEIGHTS),default=['raider','industrial']);args=ap.parse_args()
 if not args.diagnostic:require_ready()
 if any(t not in TRAITS for t in args.traits) or any(p not in POLICY_WEIGHTS for p in args.policies) or any(s not in (0,1,2) for s in args.seats):ap.error('Unknown trait, policy or seat')
 if not 1<=args.initial_strength<=5 or args.minor_tier not in (1,2,3) or min(args.horizon,args.expand_mp,args.create_mp)<0 or args.raid_total<5:ap.error('Invalid scenario/variant setting')
 out=Path(args.out);out.mkdir(exist_ok=True);pinned=out/'inputs';pinned.mkdir(exist_ok=True)
 names=set(inputs())|{'balance_experiment.py','readiness.py','simulation_readiness.json'}
 for name in names:
  if Path(name).exists():shutil.copy2(name,pinned/name)
 fingerprint={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in pinned.iterdir() if p.is_file()}
 manifest=dict(classification='implementation diagnostic' if args.diagnostic else 'controlled baseline/sensitivity experiment; not a balance conclusion',settings=vars(args),inputs=fingerprint,opponents=list(zip(args.opponent_traits,args.opponent_policies)),controllers=args.controllers,limitations=['Human Soulstorm outcomes must be supplied; no human win-rate model','Raid profile is provisional','B21 immediate defensive deficit behaviour is intentionally retained','Initial fleet strength and Minor tier are explicit scenario parameters, not an approved random-generation preset','Do not infer trait rankings from a single policy, seat, seed or search depth'])
 (out/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8');rows=[]
 for n,(trait,policy,seat,seed) in enumerate(itertools.product(args.traits,args.policies,args.seats,range(args.seeds))):
  row,trace=simulate(trait=trait,policy=policy,seat=seat,seed=seed,cycles=args.cycles,horizon=args.horizon,initial_strength=args.initial_strength,minor_tier=args.minor_tier,expand_mp=args.expand_mp,create_mp=args.create_mp,raid_total=args.raid_total,controllers=tuple(args.controllers),opponent_traits=tuple(args.opponent_traits),opponent_policies=tuple(args.opponent_policies))
  rows.append(row);(out/f'trace-{n}.json').write_text(json.dumps(trace,indent=2),encoding='utf-8');(out/'results.json').write_text(json.dumps(rows,indent=2),encoding='utf-8');print(n,trait,policy,seat,seed,flush=True)
if __name__=='__main__':main()
