# Balance laboratory — first calibration results

15 September 2026 • Experimental model v0.1 • No rule changes adopted

**This is not a full-game balance verdict.** These runs cover Minor-faction frontier expansion, not a three-Major-Faction contest or human Soulstorm outcomes. Missing actions and heuristic planning can materially change rankings. See Balance_Simulation_Methods.md before interpreting these numbers.

Completed 432 trials: 3 cost settings ×6 policy profiles ×3 trait profiles ×8 seeds, up to 36 Cycles each. Starts are 20/20 on a matched synthetic three-system frontier. Each trial has seven initially hostile holdings. All stopped and no-capture trials remain in the dataset.

## Validation and reproducibility

19 regression tests passed, including recorded Dessica combat/accounting cases, resource locks, action availability and construction damage. Two recorded player battle setups also match. An initiation-selection edge case was found during audit, fixed and the campaign experiment rerun; interrupted pre-fix results are not included. Source-export terminology and the omitted AI formula were corrected.

Engine SHA-256: 7f15bd56e08dbeb2b2ce6e8379089181e9bf4d88781c951f3d1db94aaf1a9abd
Source SHA-256: a7c69047b59f3d2242e26a592fca9ac52b1b227313a2fbadd625b6f4cd4be9bf

## Behavioural validation warning

**Do not use this pilot to select a rebalance.** Across all 432 trials the planners used zero bombardment actions and entered zero deficits. Closing stocks approached the cap. This does not represent the strategic pressure observed in Dessica. The experiment differs in starting resources (20/20 rather than 10/10), opponents (static Minor factions only), combat resolution (AI rather than player Soulstorm) and available constructions. These differences must be tested, not explained away as proof of optimal play.

The cost perturbation is weakly exercised because many policies create/expand few fleets. Small measured differences do not establish that additional Manpower costs are ineffective. Policy labels such as naval_doctrine are evaluator preferences, not proof the bot is a competent naval opponent.

Exact-zero construction payments causing host degradation remain an unvalidated engine boundary; this pilot had no deficit entries, so that path was not exercised. Do not use that boundary in new experimental claims without fixing and regression-testing its action ordering.

## Cost settings

| Setting | Create Fleet | Expand Fleet |
|---|---|---|
| Baseline | 1 Supply +1 Manpower | 1 Supply |
| Expansion crew cost | 1 Supply +1 Manpower | 1 Supply +1 Manpower |
| Creation and expansion crew costs | 1 Supply +2 Manpower | 1 Supply +1 Manpower |

These are test parameters, not recommendations. Building materials remain represented by Supply in every setting.

## Aggregate results

| Setting | Mean captures | Mean closing Supply | Mean closing Manpower | Mean Supply spent | Mean Manpower spent | Deficit entries/trial | Stopped trials | No capture |
|---|---|---|---|---|---|---|---|---|
| baseline | 5.21 | 91.15 | 95.24 | 148.35 | 26.15 | 0.00 | 0 | 1 |
| expand_mp1 | 5.13 | 91.06 | 94.70 | 147.23 | 27.24 | 0.00 | 0 | 3 |
| create_mp2_expand_mp1 | 5.13 | 91.38 | 94.20 | 146.85 | 28.29 | 0.00 | 0 | 3 |

Spending is voluntary action expenditure, including committed Manpower before returns; event losses and maintenance are not included in spending columns. Closing resources from stopped trials are at stop time, not Cycle 36. Captures are progress measures, not campaign victory.

## Paired comparison uncertainty

Differences below compare identical seed/policy/trait conditions. Bootstrap resamples whole seed clusters so the eighteen shared-event policy/trait cases per seed are not counted as independent random worlds. Intervals describe sampling variation within this model only; they do not cover model bias. Eight seed clusters are a small pilot, not evidence of convergence.

| Candidate minus baseline | Mean capture difference | 95% seed-cluster bootstrap interval |
|---|---|---|
| expand_mp1 | -0.076 | -0.292 to 0.062 |
| create_mp2_expand_mp1 | -0.076 | -0.292 to 0.062 |

## Baseline by policy and trait

| Policy | Trait | Mean captures | Fleet battles/trial | Assaults/trial | Bombardments/trial | Create/expand actions |
|---|---|---|---|---|---|---|
| adaptive | siege | 6.00 | 0.50 | 23.12 | 0.00 | 0.50/0.00 |
| adaptive | efficient | 4.50 | 0.00 | 14.62 | 0.00 | 1.12/1.12 |
| adaptive | mobile | 5.50 | 0.00 | 13.75 | 0.00 | 1.88/1.12 |
| ground_doctrine | siege | 5.62 | 0.62 | 21.62 | 0.00 | 0.38/0.00 |
| ground_doctrine | efficient | 4.75 | 0.12 | 15.75 | 0.00 | 1.12/1.00 |
| ground_doctrine | mobile | 5.88 | 0.00 | 15.62 | 0.00 | 2.25/0.62 |
| naval_doctrine | siege | 6.88 | 0.12 | 26.88 | 0.00 | 0.38/0.50 |
| naval_doctrine | efficient | 4.38 | 0.00 | 14.62 | 0.00 | 3.00/3.88 |
| naval_doctrine | mobile | 4.75 | 1.88 | 10.62 | 0.00 | 3.25/3.00 |
| industrial | siege | 2.75 | 1.62 | 9.75 | 0.00 | 0.88/0.12 |
| industrial | efficient | 4.62 | 0.00 | 14.50 | 0.00 | 1.00/1.00 |
| industrial | mobile | 5.12 | 0.00 | 11.38 | 0.00 | 1.50/0.62 |
| personnel_preservation | siege | 6.38 | 0.38 | 25.00 | 0.00 | 0.50/0.12 |
| personnel_preservation | efficient | 4.50 | 0.00 | 14.50 | 0.00 | 1.12/1.12 |
| personnel_preservation | mobile | 5.12 | 0.00 | 12.75 | 0.00 | 2.00/1.12 |
| opportunist | siege | 6.88 | 0.00 | 26.88 | 0.00 | 0.38/0.38 |
| opportunist | efficient | 4.50 | 0.00 | 16.00 | 0.00 | 3.38/4.75 |
| opportunist | mobile | 5.62 | 0.00 | 14.75 | 0.00 | 3.75/3.50 |

## Exact fleet battle probabilities

All 400 d20 pairs enumerated for each of 48 matchups. Strength is before initiation. The no-damage tie convention applies; expected own battle loss excludes the guaranteed initiation point.

| Attacker vs defender | Attacker wins | Tie | Expected own battle strength lost | Expected enemy strength lost |
|---|---|---|---|---|
| 5 vs 5 | 42.8% | 4.8% | 1.000 | 0.775 |
| 10 vs 10 | 42.8% | 4.8% | 2.038 | 1.550 |
| 15 vs 10 | 66.0% | 4.0% | 1.425 | 2.990 |
| 17 vs 8 | 80.5% | 3.0% | 0.877 | 4.000 |

## Findings we can safely use

- In the specified AI ground formula, one additional available Supply and one additional available Manpower each add exactly one to the roll. Their direct roll coefficient is equal; that does not make their strategic spending opportunities equal.
- Equal pre-initiation Fleet Strength favours the defender statistically. Fleet count also changes aggregate damage because losses apply to every participating losing fleet. Comparing only total strength misses this exposure.
- The planner can choose direct assaults before clearing fleets, and it can split or combine attacks. Its preferences still depend on the evaluator and restricted action catalogue, so observed choices are not proof of optimal strategy.
- Supply/Manpower cost variants can be rerun reproducibly without changing the campaign. The frontier experiment cannot establish their effects in a war against an adaptive Major opponent.
- Missing combat buildings and Major counterattacks are especially important for judging economy-first strategies. We must add those before accepting that result as game balance.

## Next validation gate

Extend to shared Major-versus-Major campaigns with the complete action/construction catalogue, capital transitions and explicit raid resolution, then test independent policy families, planning-depth ablations and held-out scenarios. Player battles need a separately calibrated outcome model or recorded outcomes. No trait buff, bombardment change, fleet crew price or construction limit is approved by this pilot.

## Files

Download Balance_Simulation_Bundle.zip for scripts, rules snapshot, tests, full trial CSV/JSON, first-seed action traces and exact combat tables. Source changes are separate from suspended Dessica.
