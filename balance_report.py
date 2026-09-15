"""Summarise completed runs, retaining censoring and paired seed clusters."""
from pathlib import Path
import json,random,statistics,zipfile

def mean(rows,key):return statistics.mean(r[key] for r in rows)

def main():
    folder=Path('balance-results');rows=json.loads((folder/'trials.json').read_text())
    manifest=json.loads((folder/'manifest.json').read_text())
    variants=list(manifest['variants']);seeds=range(manifest['seeds'])
    lines=['# Balance laboratory — first calibration results','',
      '15 September 2026 • Experimental model v0.1 • No rule changes adopted','',
      '**This is not a full-game balance verdict.** These runs cover Minor-faction frontier expansion, not a three-Major-Faction contest or human Soulstorm outcomes. Missing actions and heuristic planning can materially change rankings. See Balance_Simulation_Methods.md before interpreting these numbers.','',
      f"Completed {len(rows)} trials: {len(variants)} cost settings ×6 policy profiles ×3 trait profiles ×{manifest['seeds']} seeds, up to {manifest['cycles']} Cycles each. Starts are 20/20 on a matched synthetic three-system frontier. Each trial has seven initially hostile holdings. All stopped and no-capture trials remain in the dataset.",'',
      '## Validation and reproducibility','',
      '19 regression tests passed, including recorded Dessica combat/accounting cases, resource locks, action availability and construction damage. Two recorded player battle setups also match. An initiation-selection edge case was found during audit, fixed and the campaign experiment rerun; interrupted pre-fix results are not included. Source-export terminology and the omitted AI formula were corrected.','',
      f"Engine SHA-256: {manifest['engine_sha256']}",f"Source SHA-256: {manifest['source_sha256']}",'',
      '## Behavioural validation warning','',
      '**Do not use this pilot to select a rebalance.** Across all 432 trials the planners used zero bombardment actions and entered zero deficits. Closing stocks approached the cap. This does not represent the strategic pressure observed in Dessica. The experiment differs in starting resources (20/20 rather than 10/10), opponents (static Minor factions only), combat resolution (AI rather than player Soulstorm) and available constructions. These differences must be tested, not explained away as proof of optimal play.', '',
      'The cost perturbation is weakly exercised because many policies create/expand few fleets. Small measured differences do not establish that additional Manpower costs are ineffective. Policy labels such as naval_doctrine are evaluator preferences, not proof the bot is a competent naval opponent.', '',
      'Exact-zero construction payments causing host degradation remain an unvalidated engine boundary; this pilot had no deficit entries, so that path was not exercised. Do not use that boundary in new experimental claims without fixing and regression-testing its action ordering.', '',
      '## Cost settings','',
      '| Setting | Create Fleet | Expand Fleet |','|---|---|---|',
      '| Baseline | 1 Supply +1 Manpower | 1 Supply |',
      '| Expansion crew cost | 1 Supply +1 Manpower | 1 Supply +1 Manpower |',
      '| Creation and expansion crew costs | 1 Supply +2 Manpower | 1 Supply +1 Manpower |','',
      'These are test parameters, not recommendations. Building materials remain represented by Supply in every setting.','',
      '## Aggregate results','',
      '| Setting | Mean captures | Mean closing Supply | Mean closing Manpower | Mean Supply spent | Mean Manpower spent | Deficit entries/trial | Stopped trials | No capture |',
      '|---|---|---|---|---|---|---|---|---|']
    for variant in variants:
        subset=[r for r in rows if r['variant']==variant]
        vals=[mean(subset,k) for k in ('captures','supply','manpower','supply_spent','manpower_spent','deficits')]
        lines.append('| '+variant+' | '+' | '.join(f'{v:.2f}' for v in vals)+f" | {sum(bool(r['stopped']) for r in subset)} | {sum(r['first_capture'] is None for r in subset)} |")
    lines+=['','Spending is voluntary action expenditure, including committed Manpower before returns; event losses and maintenance are not included in spending columns. Closing resources from stopped trials are at stop time, not Cycle 36. Captures are progress measures, not campaign victory.','',
      '## Paired comparison uncertainty','',
      'Differences below compare identical seed/policy/trait conditions. Bootstrap resamples whole seed clusters so the eighteen shared-event policy/trait cases per seed are not counted as independent random worlds. Intervals describe sampling variation within this model only; they do not cover model bias. Eight seed clusters are a small pilot, not evidence of convergence.','',
      '| Candidate minus baseline | Mean capture difference | 95% seed-cluster bootstrap interval |','|---|---|---|']
    baseline={(r['seed'],r['policy'],r['trait']):r for r in rows if r['variant']=='baseline'}
    for variant in variants[1:]:
        clusters=[]
        for seed in seeds:
            subset=[r for r in rows if r['variant']==variant and r['seed']==seed]
            clusters.append(statistics.mean(r['captures']-baseline[(seed,r['policy'],r['trait'])]['captures'] for r in subset))
        rng=random.Random(808);boots=sorted(statistics.mean(rng.choices(clusters,k=len(clusters))) for _ in range(4000))
        lines.append(f'| {variant} | {statistics.mean(clusters):.3f} | {boots[100]:.3f} to {boots[3899]:.3f} |')
    lines+=['','## Baseline by policy and trait','',
      '| Policy | Trait | Mean captures | Fleet battles/trial | Assaults/trial | Bombardments/trial | Create/expand actions |','|---|---|---|---|---|---|---|']
    for policy in manifest['policies']:
        for trait in ('siege','efficient','mobile'):
            sub=[r for r in rows if r['variant']=='baseline' and r['policy']==policy and r['trait']==trait]
            count=lambda name:statistics.mean(r['actions'].get(name,0) for r in sub)
            lines.append(f'| {policy} | {trait} | {mean(sub,"captures"):.2f} | {count("battle"):.2f} | {count("assault"):.2f} | {count("bombard"):.2f} | {count("create"):.2f}/{count("expand"):.2f} |')
    naval=json.loads((folder/'naval_exact.json').read_text())
    lines+=['','## Exact fleet battle probabilities','',
      'All 400 d20 pairs enumerated for each of 48 matchups. Strength is before initiation. The no-damage tie convention applies; expected own battle loss excludes the guaranteed initiation point.','',
      '| Attacker vs defender | Attacker wins | Tie | Expected own battle strength lost | Expected enemy strength lost |','|---|---|---|---|---|']
    for r in naval:
        if (r['attacker_pre_init'],r['defender']) in ((5,5),(10,10),(15,10),(17,8)):
            lines.append(f"| {r['attacker_pre_init']} vs {r['defender']} | {r['win_probability']:.1%} | {r['tie_probability']:.1%} | {r['expected_own_battle_fs_loss']:.3f} | {r['expected_enemy_fs_loss']:.3f} |")
    lines+=['','## Findings we can safely use','',
      '- In the specified AI ground formula, one additional available Supply and one additional available Manpower each add exactly one to the roll. Their direct roll coefficient is equal; that does not make their strategic spending opportunities equal.',
      '- Equal pre-initiation Fleet Strength favours the defender statistically. Fleet count also changes aggregate damage because losses apply to every participating losing fleet. Comparing only total strength misses this exposure.',
      '- The planner can choose direct assaults before clearing fleets, and it can split or combine attacks. Its preferences still depend on the evaluator and restricted action catalogue, so observed choices are not proof of optimal strategy.',
      '- Supply/Manpower cost variants can be rerun reproducibly without changing the campaign. The frontier experiment cannot establish their effects in a war against an adaptive Major opponent.',
      '- Missing combat buildings and Major counterattacks are especially important for judging economy-first strategies. We must add those before accepting that result as game balance.','',
      '## Next validation gate','',
      'Extend to shared Major-versus-Major campaigns with the complete action/construction catalogue, capital transitions and explicit raid resolution, then test independent policy families, planning-depth ablations and held-out scenarios. Player battles need a separately calibrated outcome model or recorded outcomes. No trait buff, bombardment change, fleet crew price or construction limit is approved by this pilot.','',
      '## Files','',
      'Download Balance_Simulation_Bundle.zip for scripts, rules snapshot, tests, full trial CSV/JSON, first-seed action traces and exact combat tables. Source changes are separate from suspended Dessica.']
    Path('Balance_Simulation_Report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    with zipfile.ZipFile('Balance_Simulation_Bundle.zip','w',zipfile.ZIP_DEFLATED) as z:
        for name in ('balance_sim.py','balance_tests.py','balance_diagnostics.py','balance_report.py','Balance_Simulation_Methods.md','Balance_Simulation_Report.md','Source_Rules.md'):
            z.write(name,name)
        for p in sorted(folder.glob('*')):
            if p.is_file():z.write(p,str(p).replace('\\','/'))
    print('Report and reproducibility bundle created.')

if __name__=='__main__':main()
