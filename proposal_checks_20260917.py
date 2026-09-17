"""Exact, isolated candidate calculations. Does not modify the campaign engine.

No sampled human results or claims of full-campaign validation. The historical
sample is read only to count existing action exposure, not to predict new play.
"""
import gzip
import hashlib
import itertools
import json
import math
import statistics
from collections import Counter
from pathlib import Path
from battle_setup import BattleSide, setup

ROOT = Path(__file__).resolve().parent


def distribution(sides, dice=1):
    return Counter(map(sum, itertools.product(range(1, sides + 1), repeat=dice)))


def outcomes(delta, sides=20, dice=1):
    faces = distribution(sides, dice)
    n = sum(faces.values()) ** 2
    margins = Counter()
    for a, ac in faces.items():
        for b, bc in faces.items():
            margins[a - b + delta] += ac * bc
    return {m: c / n for m, c in sorted(margins.items())}


def probability(delta, sides=20, dice=1):
    margins = outcomes(delta, sides, dice)
    return dict(win=sum(p for m, p in margins.items() if m > 0),
                tie=margins.get(0, 0),
                loss=sum(p for m, p in margins.items() if m < 0))


def resource_score(resource):
    return math.floor(resource / 5)


def ground_score(strength, supply, manpower, modifier=0):
    return strength + resource_score(supply) + resource_score(manpower) + modifier


def minor_resources(tiers):
    return 5 * sum(tiers)


def ordinary_minor_strength(maxima):
    return math.ceil(sum(maxima) / 2)


def bombard_cost(tier, damage):
    return 2 * tier + damage


def naval(attacker, defender):
    # Exactly one initiation point; no attached effects in these examples.
    delta = sum(attacker) - 1 - sum(defender)
    margins = outcomes(delta, 6, 2)
    return dict(attacker=attacker, defender=defender, delta=delta,
                **probability(delta, 6, 2),
                defender_all_destroyed=sum(p for m, p in margins.items()
                    if m > 0 and math.ceil(m / 3) >= max(defender)),
                minimum_attacker_victory_damage=min(
                    (math.ceil(m / 3) for m in margins if m > 0), default=0),
                maximum_damage=max(math.ceil(abs(m) / 3) for m in margins))


# (Minor planets, Standard planets, Major planets, Minor/Standard/Major stations)
SYSTEMS = [
    (2, 0, 0, ()), (3, 0, 0, ()), (1, 1, 0, ()),
    (2, 1, 0, ()), (3, 1, 0, ()), (2, 1, 0, (1,)),
    (1, 2, 0, ()), (2, 2, 0, ()), (1, 2, 0, (2,)),
    (2, 0, 1, ()), (1, 1, 1, ()), (2, 1, 1, ()),
    (1, 2, 1, ()), (1, 1, 1, (1,)), (2, 3, 0, ()),
    (2, 2, 0, (1,)), (2, 2, 1, ()), (2, 1, 2, ()),
    (2, 2, 1, (2,)), (2, 2, 2, (3,)),
]


def main():
    checks = 0
    for r in range(100):
        assert resource_score(r + 1) >= resource_score(r)
        checks += 1
    for r in range(81):
        assert resource_score(r + 20) == resource_score(r) + 4
        checks += 1
    assert naval([5] * 20, [5])['defender_all_destroyed'] == 1
    assert naval([5], [5])['defender_all_destroyed'] == 0
    assert len(SYSTEMS) == 20 and min(sum(x[:3]) + len(x[3]) for x in SYSTEMS) == 2
    checks += 3
    examples = []
    # Post-commitment values, no optional modifiers or third-party raid.
    for name, a, d in [
        ('Equal supplied forces', (5, 30, 30), (5, 30, 30)),
        ('One full Supply band ahead', (5, 50, 30), (5, 30, 30)),
        ('One full band ahead in both resources', (5, 50, 50), (5, 30, 30)),
        ('Critical vs Abundant in Supply', (5, 10, 30), (5, 90, 30)),
        ('Single Minor world; 20/20 attacker before cost', (5, 19, 19), (1, 4, 4)),
        ('Standard plus Minor; 20/20 attacker before Standard assault', (5, 18, 19), (3, 13, 14)),
        ('Major plus Standard plus Minor; 20/20 attacker, two full fleets', (10, 17, 18), (7, 27, 29)),
    ]:
        av, dv = ground_score(*a), ground_score(*d)
        examples.append(dict(name=name, attacker=a, defender=d, scores=[av, dv],
                             delta=av-dv, **probability(av-dv)))
    # Fixed dice-independent damage comparison; no regeneration, traits, shields.
    routes = []
    for strength in (5, 10, 15):
        commitment = strength // 5
        assault = commitment + 1
        bombard = max(1, strength // 5)
        for tier, defence in ((1, 2), (2, 4), (3, 8), (4, 12)):
            wins = math.ceil(defence / assault)
            volleys = math.ceil((defence - 1) / bombard)
            routes.append(dict(strength=strength, tier=tier, defence=defence,
                direct_winning_assaults=wins, direct_supply=wins*tier,
                direct_mp_net=wins*(commitment-math.floor(.6*commitment)),
                bombard_then_win_actions=volleys+1,
                bombard_then_win_supply=volleys*bombard_cost(tier,bombard)+tier,
                bombard_then_win_mp_net=commitment-math.floor(.6*commitment)))
    # Exposure count only: changed rules would change orders and outcomes.
    exposures=[]
    sample=ROOT/'integrated-balance-20260917'
    if sample.exists():
        rows=json.loads((sample/'results.json').read_text())
        for row in rows:
            end=row['milestones'].get('one_major_coalition',100)
            with gzip.open(sample/f"case-{row['sample_id']:03}.trace.json.gz",'rt',encoding='utf-8') as f:
                trace=json.load(f)
            counts=Counter(o['player'] for o in trace['orders'] if o['cycle']<=end and o['order'][0]=='expand' and o['player']<3)
            exposures.extend(counts.get(p,0) for p in range(3))
    output=dict(status='PROPOSAL ONLY: exact microchecks, not campaign validation',
        assertions=checks, ground=examples,
        resource_scores=[dict(resource=r,score=resource_score(r)) for r in (0,1,5,10,20,21,30,40,50,60,70,80,90,100,120)],
        naval=[naval(a,d) for a,d in [([5],[5]),([5,5],[5]),([5,5,5,5],[5]),([5]*20,[5])]],
        minor=[dict(tiers=t,each_resource=minor_resources(t)) for t in ([1],[2],[3],[2,1],[3,2,1],[4,3,2,1])],
        routes=routes,
        systems=[dict(d20=i+1,minor=x[0],standard=x[1],major=x[2],stations=x[3],holdings=sum(x[:3])+len(x[3])) for i,x in enumerate(SYSTEMS)],
        mean_holdings=statistics.mean(sum(x[:3])+len(x[3]) for x in SYSTEMS),
        expansion_exposure=dict(faction_histories=len(exposures),total=sum(exposures),
            median=statistics.median(exposures) if exposures else None,
            mean=statistics.mean(exposures) if exposures else None,
            interpretation='Additional nominal Manpower expenditure on old orders only; not a feasible new-rules replay or outcome prediction.'),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    output['player_examples'] = []
    for label, player, old_enemy, new_enemy in [
        ('20/20 start, five strength attacks Standard of Standard+Minor owner',
         BattleSide(18,19,5,'Player'), BattleSide(58,59,6,'Minor'), BattleSide(13,13,3,'Minor')),
        ('20/20 start, ten strength attacks Major of Major+Standard+Minor owner',
         BattleSide(17,18,10,'Player'), BattleSide(77,78,14,'Minor'), BattleSide(27,27,7,'Minor')),
    ]:
        output['player_examples'].append(dict(name=label,
            baseline=setup(player,old_enemy),candidate=setup(player,new_enemy)))
    (ROOT/'Proposal_Checks_20260917.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in output.items() if k not in ('systems','routes')},indent=2))


if __name__=='__main__': main()
