# Faction traits and bot qualification

Updated 17 September 2026. All 12 traits are applied mechanically and independently rotated across the production bot strategies. Traits are assigned between campaigns, never rerolled mid-game; rule-driven loss of a trait still applies.

## Coverage

The completed matrix contains **432 games**, each executing **100 Cycles**: 12 traits x 6 strategies x 3 turn positions x 2 matched replicates. Each trait appears as the focal faction in 36 games. Every strategy/seat combination appears for every trait. Opponent profiles and starting conditions vary between replicates but remain fixed across paired focal comparisons.

This is a qualification screen, not an exhaustive set of three-trait combinations or a statistically precise ranking. The synthetic matrix has three systems; separate ten-system scenarios test larger campaigns. Close balance claims need more seeds, more opponent mixtures and maps appropriate to the intended campaign.

| Trait | Games | Implemented interaction |
|---|---:|---|
| Siege Doctrine | 36 | Losing ground-assault attrition; human setup ignores Defended difficulty |
| Efficient Logistics | 36 | Reinforce and Muster grant four instead of three |
| Mobile Capital | 36 | Moving capital/shipyard; defence contributes strength; host damage and integrity |
| War Economy | 36 | Three extra Supply each Logistics Cycle |
| Martial Culture | 36 | Five extra Manpower each Logistics Cycle |
| Salvagers | 36 | Battle and capture Supply rewards |
| Void Supremacy | 36 | Expansion has no Supply cost, including while Supply is locked |
| Swift Mobilization | 36 | New fleets begin at three strength |
| Fleet Endurance | 36 | One strength restored at Logistics, capped at each fleet maximum |
| Dread Reputation | 36 | Reduced successful-defender resource returns under the applicable AI/player rules |
| Fortification Experts | 36 | Two additional defence restored by Defend |
| Industrial Efficiency | 36 | Four-Supply construction stages instead of five |

## What changed in the bots

Persistent operation plans connect fleet movement, assembly, repair, resources and attacks. The bots check actual combat effects, so a nominal win against an invulnerable shield is not mistaken for useful damage. Funding responds to enemy resources and upkeep. Plans distinguish new progress from a defender repairing the same damage repeatedly. Home defence evaluates resources as well as fleet strength. Free Void Supremacy expansion is no longer suppressed by a paid-expansion Supply reserve.

The six strategies still share controller code; they are not six independent expert players. A separate siege controller and the older tactical controller are included as opponents to help expose shared weaknesses. Optional sampled search remains experimental and is outside horizon-zero qualification.

## Measured results

The matrix replayed and verified **273,209 orders** through the public rules interface. Initial/final snapshots, per-Cycle states, bot memory, event/combat logs and compressed complete order traces are retained.

| Milestone | Reached by Cycle 100 | Still unresolved | Mean among observed milestones | Observed range |
|---|---:|---:|---:|---|
| One surviving Major coalition | 431 | 1 | 35.6 | 18-83 |
| All holdings and Mobile Capitals controlled | 431 | 1 | 35.8 | 22-83 |

These are milestone times on small synthetic maps, not the duration of a representative campaign. Unresolved games are censored; the observed mean omits them and is not an estimated overall mean. No universal victory condition has been invented. The user target remains an average around 50-100 Cycles with shorter outliers.

## Reading trait outcomes

| Trait | Sole surviving focal faction | Focal faction survives | Mean captures |
|---|---:|---:|---:|
| Siege Doctrine | 8/36 | 8/36 | 4.89 |
| Efficient Logistics | 13/36 | 13/36 | 5.14 |
| Mobile Capital | 17/36 | 18/36 | 6.31 |
| War Economy | 18/36 | 18/36 | 6.28 |
| Martial Culture | 26/36 | 26/36 | 7.28 |
| Salvagers | 17/36 | 17/36 | 5.83 |
| Void Supremacy | 11/36 | 11/36 | 5.06 |
| Swift Mobilization | 9/36 | 9/36 | 4.44 |
| Fleet Endurance | 10/36 | 10/36 | 5.11 |
| Dread Reputation | 11/36 | 11/36 | 4.75 |
| Fortification Experts | 11/36 | 11/36 | 4.67 |
| Industrial Efficiency | 11/36 | 11/36 | 4.61 |

These counts describe these bots and fixtures. They are not human win probabilities, significance tests, or approved nerfs/buffs. Siege Doctrine has a Soulstorm difficulty benefit, and Dread Reputation has player/AI return distinctions; their AI-only results cannot establish their full value in player battles. Opponent mixtures, position, map size, resource rules and strategy quality can all affect them. Use the saved decisions to investigate suspected causes before changing a trait.

## Reproduction and state preservation

The simulation bundle contains the source, input pins, all matrix results and compressed traces. trait_qualification.py reproduces the matrix; audit_trait_matrix.py checks coverage; validate_release.py checks the release gate. The handover records current status and remaining work. Dessica remains suspended at Cycle 21; no campaign turn, event or balance-rule change was made.
