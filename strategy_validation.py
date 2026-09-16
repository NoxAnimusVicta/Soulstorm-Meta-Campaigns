"""Whole-game strategic diagnostics with pinned scenarios and deterministic replay."""
import argparse,json,random,time
from pathlib import Path
from sim_scenarios import campaign_fixture
from sim_replay import Replay,snapshot,digest,inputs
from shared_sim import choose,policy_for
from bot_control import coordinate,social

TRAITS=('siege','efficient','mobile','war_economy','martial','salvagers','void','swift','endurance','dread','fortification','industrial')
POLICIES=('raider','industrial','fleet_control','conservative','opportunist','balanced')

def play(case,cycles=9,depth=0,progress=False):
 started=time.monotonic()
 traits=tuple(TRAITS[(case*3+i)%len(TRAITS)] for i in range(3))
 policies=tuple(POLICIES[(case+i)%len(POLICIES)] for i in range(3))
 a=campaign_fixture(traits,initial_strength=(1,4,5)[case%3],minor_tier=(1,2,3)[case%3]);a.rotation=case%3
 a.defender_policies=dict(enumerate(policies));rng=random.Random(1000+case);decision=0
 initial=snapshot(a);trace=[]
 for _ in range(cycles):
  a.opening(random.Random(100000+case*100+a.cycle))
  for p in a.turns():
   a.begin_turn(p);coordinate(a,p,policies)
   for phase in ('fleet','faction','social','construction'):
    if phase=='social':social(a,p,policies,rng);continue
    budget=sum(len(st.fleets) for st in a.players)+1 if phase=='fleet' else 1
    for _ in range(budget):
     if depth:
      from strategic_planner import plan
      order=plan(a,p,phase,policies,decision,horizon=depth,beam=2,samples=2)
     else:order=choose(a,p,phase,policy_for(a,p,policies),decision)
     decision+=1;a.submit(p,phase,order,rng)
     trace.append(dict(cycle=a.cycle,player=p,phase=phase,order=order,after=digest(a)))
     if order[0]=='none':break
   if a.stop:raise RuntimeError(a.stop)
  a.closing()
  if progress and a.cycle%5==0:print('Actual campaign Cycle',a.cycle,'elapsed',round(time.monotonic()-started),flush=True)
 counts={}
 for row in a.log:
  kind=row.get('action',row.get('combat','unknown'));counts[kind]=counts.get(kind,0)+1
 return dict(case=case,cycles=cycles,depth=depth,traits=traits,policies=policies,actions=counts,decisions=decision,final=digest(a),stop=a.stop,players=[dict(supply=s.supply,manpower=s.manpower,deficits=s.deficits,holdings=sum(w.owner==p for w in a.holdings),strength=sum(f.strength for f in s.fleets)) for p,s in enumerate(a.players)],inputs=inputs()),dict(initial=initial,final=snapshot(a),commands=trace,log=a.log)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--cases',type=int,default=12);ap.add_argument('--cycles',type=int,default=9);ap.add_argument('--depth',type=int,default=0);ap.add_argument('--out',default='strategy-diagnostics');args=ap.parse_args()
 out=Path(args.out);out.mkdir(exist_ok=True);rows=[];start=time.monotonic()
 for case in range(args.cases):
  row,trace=play(case,args.cycles,args.depth)
  # Repeat the complete decision process; compare decisions, state and battle log.
  check,checktrace=play(case,args.cycles,args.depth)
  assert row==check and trace==checktrace,'Whole-game reproducibility failed'
  row['reproduced']=True;rows.append(row)
  (out/f'trace-{case}.json').write_text(json.dumps(trace,indent=2),encoding='utf-8')
  (out/'results.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
  print(case,row['decisions'],round(time.monotonic()-start),flush=True)
