"""Full-game bot diagnostics with frozen inputs and whole-process reproducibility.
No user campaign state is loaded or changed. Duration milestones are separate
from the still-unconfirmed campaign victory condition.
"""
import argparse,json,random,hashlib,shutil,time
from pathlib import Path
from collections import Counter
from sim_replay import snapshot,digest,inputs
from sim_scenarios import campaign_fixture
from strategy_validation import TRAITS,POLICIES
from shared_sim import SharedState,Holding
from bot_dispatch import select_order
from bot_control import coordinate,social

def play(case=0,seed=0,cycles=100,modes=('operational',)*3,large=False,horizon=0,allied=False,setup=None):
 starting_inputs=inputs()
 traits=tuple(TRAITS[(case*3+i)%12] for i in range(3));policies=tuple(POLICIES[(case+i)%6] for i in range(3))
 setup=setup or {}
 traits=tuple(setup.get('traits',traits));policies=tuple(setup.get('policies',policies))
 a=campaign_fixture(traits,initial_strength=setup.get('initial_strength',(1,4,5)[case%3]),minor_tier=setup.get('minor_tier',(1,2,3)[case%3]));a.rotation=setup.get('rotation',case%3)
 if large:
  for k in range(3,10):a.add_minor([(2,4,4,k,False),(1,2,2,k,False)])
  a.check()
 a.defender_policies=dict(enumerate(policies));a.bot_controller_modes=dict(enumerate(modes))
 if allied:a.alliances.add(frozenset((0,1)))
 initial=snapshot(a);combat=random.Random(1000+case+seed*10000);decision=0;orders=[];history=[];milestones={}
 for cycle in range(1,cycles+1):
  a.opening(random.Random(100000+case*100+a.cycle+seed*1000000))
  for p in a.turns():
   a.begin_turn(p);coordinate(a,p,policies)
   for phase in ('fleet','faction','social','construction'):
    if phase=='social':social(a,p,policies,combat);continue
    for _ in range(sum(len(s.fleets) for s in a.players)+1 if phase=='fleet' else 1):
     order=select_order(a,p,phase,policies,decision,horizon)
     memory=dict(plans=getattr(a,'bot_plans',{}),diagnostic=getattr(a,'diagnostic_targets',{}))
     # JSON serialisation now, before later plan updates, makes this immutable.
     from sim_replay import encode
     memory=json.loads(json.dumps(encode(memory)))
     a.submit(p,phase,order,combat);decision+=1
     orders.append(dict(cycle=cycle,player=p,phase=phase,order=order,bot_memory=memory,after=digest(a)))
     if order[0]=='none':break
   if a.stop:raise RuntimeError(a.stop)
  a.closing();a.check()
  alive=[p for p in a.turn_order if p not in a.eliminated]
  if alive and all(a.allied(alive[0],q) for q in alive):milestones.setdefault('one_major_coalition',cycle)
  owners={w.owner for w in a.holdings}
  owners.update(p for p,s in enumerate(a.players) if any(f.mobile and f.strength>0 for f in s.fleets))
  if owners and any(all(a.allied(p,q) for q in owners) for p in alive):milestones.setdefault('all_holdings_and_mobile_capitals',cycle)
  history.append(dict(cycle=cycle,players=[dict(supply=s.supply,manpower=s.manpower,holdings=sum(w.owner==p for w in a.holdings),strength=sum(f.strength for f in s.fleets),captures=s.captures,eliminated=p in a.eliminated,deficits=dict(s.deficits),projects=sum(pr.active for pr in s.projects)) for p,s in enumerate(a.players)]))
  if horizon and cycle%10==0:print('Look-ahead actual Cycle',cycle,flush=True)
 counts=Counter((e['player'],e['order'][0]) for e in orders)
 assert inputs()==starting_inputs,'Inputs changed during the run; discard this evidence'
 row=dict(case=case,seed=seed,cycles=cycles,large=large,allied=allied,modes=modes,horizon=horizon,traits=traits,policies=policies,setup=setup,milestones=milestones,players=history[-1]['players'][:3],decisions=decision,actions=[dict(player=p,action=k,count=v) for (p,k),v in sorted(counts.items())],inputs=starting_inputs,final=digest(a))
 trace=dict(initial=initial,final=snapshot(a),orders=orders,history=history,log=a.log)
 return row,trace

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cases',type=int,nargs='+',default=[0,1,2,3]);ap.add_argument('--seeds',type=int,nargs='+',default=[0]);ap.add_argument('--cycles',type=int,default=100);ap.add_argument('--modes',nargs=3,default=['operational']*3);ap.add_argument('--large',action='store_true');ap.add_argument('--allied',action='store_true');ap.add_argument('--horizon',type=int,default=0);ap.add_argument('--repeat',action='store_true');ap.add_argument('--out',default='bot-qualification-20260916');args=ap.parse_args()
 out=Path(args.out);out.mkdir(exist_ok=True);pin=out/'inputs';pin.mkdir(exist_ok=True)
 for name in list(inputs())+['bot_qualification.py']:
  if (pin/name).exists() and (pin/name).read_bytes()!=Path(name).read_bytes():raise RuntimeError('Do not overwrite differently pinned qualification inputs')
  shutil.copy2(name,pin/name)
 rows=[];start=time.monotonic()
 for case in args.cases:
  for seed in args.seeds:
   row,trace=play(case,seed,args.cycles,tuple(args.modes),args.large,args.horizon,args.allied)
   if args.repeat:
    again,againtrace=play(case,seed,args.cycles,tuple(args.modes),args.large,args.horizon,args.allied)
    assert row==again and trace==againtrace,'Controller or engine replay divergence'
    row['reproduced']=True
   index=len(rows);rows.append(row)
   (out/f'trace-{index}.json').write_text(json.dumps(trace,indent=2),encoding='utf-8')
   (out/'results.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
   print('Finished',case,seed,args.modes,'holdings',[p['holdings'] for p in row['players']],round(time.monotonic()-start),flush=True)

if __name__=='__main__':main()
