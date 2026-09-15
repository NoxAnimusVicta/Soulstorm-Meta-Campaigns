"""Exact combat enumeration and sensitivity diagnostics; no fabricated Soulstorm odds."""
from pathlib import Path
import csv,json,math,random
from balance_sim import fleet_losses,win_probability,run_trial

def player_setup(supply,manpower,enemy_supply,enemy_manpower,friendly_fs,enemy_fs,defended=False,ambush=False,siege=False,raid=False):
    band=lambda x: min(4,max(0,(max(1,x)-1)//20))
    difficulty=max(1,min(5,5-band(supply)+(band(enemy_supply)-2)+(int(defended and not siege))+int(ambush)))
    friendly=max(1,min(4,1+friendly_fs//5+band(manpower)-2))
    enemy=max(1,min(4,1+enemy_fs//5+band(enemy_manpower)-2))
    teams=[friendly,enemy]+([1] if raid else [])
    return {'difficulty':difficulty,'teams':teams,'map_minimum':max(2*max(teams),sum(teams))}

def naval(attacker,defender):
    # Input is pre-initiation strength. Balanced conventional 5-strength formations.
    af=[5]*(attacker//5)+([attacker%5] if attacker%5 else [])
    df=[5]*(defender//5)+([defender%5] if defender%5 else [])
    af[0]-=1
    rows=[]
    for x in range(1,21):
        for y in range(1,21):
            margin=x+attacker-1-y-defender
            loss=fleet_losses(abs(margin)) if margin else 0
            rows.append((margin>0,margin==0,sum(min(loss,f) for f in af) if margin<0 else 0,sum(min(loss,f) for f in df) if margin>0 else 0,margin>=16,margin<=-16))
    return dict(zip(('win_probability','tie_probability','expected_own_battle_fs_loss','expected_enemy_fs_loss','enemy_total_destruction_band','own_total_destruction_band'),[sum(r[i] for r in rows)/400 for i in range(6)]))

def main():
    out=Path('balance-results');out.mkdir(exist_ok=True)
    matrix=[{'attacker_pre_init':a,'defender':d,**naval(a,d)} for a in (5,10,12,15,17,20) for d in (4,5,8,10,12,14,15,20)]
    (out/'naval_exact.json').write_text(json.dumps(matrix,indent=2))
    # Analytical comparison after attack costs: AI resource additions enter identically.
    ground=[]
    for fs in (5,10,17):
        for defence,maxdef,tier in ((2,2,1),(4,4,2),(1,4,2),(8,8,3)):
            for supply,mp in ((10,10),(20,20),(40,20),(20,40),(60,60)):
                dc=max(1,fs//5)//2;resource={1:40,2:60,3:80}[tier]*defence/maxdef
                a=fs+supply+mp;b=10+resource*2-dc
                ground.append({'fs':fs,'defence':defence,'maxdef':maxdef,'supply_post_cost':supply,'mp_post_commit':mp,'win':win_probability(a,b),'plus5_supply':win_probability(a+5,b),'plus5_manpower':win_probability(a+5,b),'defender_supply_debit_alternative':win_probability(a,b-tier)})
    (out/'ground_exact.json').write_text(json.dumps(ground,indent=2))
    setups={
        'Dessica Cycle20 Corvid':player_setup(2,22,30,28,10,10,raid=True),
        'Dessica Cycle21 Corvid':player_setup(6,28,15,13,10,10,raid=True),
    }
    assert setups['Dessica Cycle20 Corvid']=={'difficulty':4,'teams':[2,2,1],'map_minimum':5}
    assert setups['Dessica Cycle21 Corvid']=={'difficulty':3,'teams':[2,1,1],'map_minimum':4}
    (out/'player_setup_checks.json').write_text(json.dumps(setups,indent=2))
    print('Exact enumeration complete: 48 naval matchups ×400 outcomes, 60 ground states, two recorded player setups.')

if __name__=='__main__':main()
