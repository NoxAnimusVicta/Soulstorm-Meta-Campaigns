# Revised balance testing — 17 September 2026

**Complete: approved rules implemented in an isolated candidate; 432 campaigns recorded and replay-validated. This is a balance assessment, not certification that the package is balanced.**

The original simulator and historical evidence remain preserved. Dessica remains suspended at Cycle 21. Use the revised simulator download for this rules package; the old root engine is retained as a historical control.

## What was implemented

Holding construction capacity with free built-in Capital yards and the agreed shipyard/Consolidation exceptions; base effects retained during upgrades; transferred fleet constructions preserved on merges; Expand Fleet costs 1 Supply/1 Manpower; shared Minor support and reduced ordinary Minor starting strength; doubled prize-Minor support; divided resource contributions; assault breakthrough and Siege bonus; damage-priced bombardment; 2d6 naval combat with uncapped margin-based losses; revised Troop Transports, Fortification and Dread; random Planet Fall allocation; Storm Transit installations; and the d20 generator with 2–4 holdings and mean 3. No new fleet/system construction limits.

Fortification pays normal Defend costs, restores +2 extra defence and repairs one completed defensive construction Integrity only after the host reaches full defence. Repair ties use stable existing-project order. Dread discounts defensive Build/Upgrade to 3 Supply per stage and no longer penalises defensive resource returns. The named alignment-specific Storm Transit structures all use identical mechanics.

## Validation and correction

227 regression checks and six additional interaction checks passed. Every campaign was replayed through public order validation: **386,978 orders** in this sample.
A generated-map case exposed an empty-action crash when a Capital-less faction retained only stations. The corrected engine allows an idle Faction Action until it acquires an eligible planetary site; it does not permit a station Capital or bypass Establish New Capital priority. All 127 previously completed games reproduced exactly under the correction before reuse. First-version inputs and the requalification record are preserved. No failed case is counted as a completed game.

## Study design

Two arms of 216 games each: 12 focal traits × 6 strategies × 3 seats. The matched arm retains the historical geography and event-seed blocks. The generated arm uses 18 seeded maps, each shared across the 12 focal-trait variants. There are 18 blocks per arm, not 432 independent random replicates.

The endpoint is the first single surviving Major coalition, matching the previous competitive milestone. Games are followed to Cycle 200; unresolved games stay in the counts. This endpoint can precede conquest of remaining Minor holdings. Bots use revised combat estimates and compare attack routes; historical differences therefore reflect the rules package with adapted bots, not a rules-only causal experiment. No human Soulstorm victory or defeat is fabricated.

## Campaign duration

| Measure | Historical geography, revised rules | Generated maps, revised rules |
|---|---:|---:|
| Games | 216 | 216 |
| Completed by 200 | 216 | 216 |
| Still unresolved at 200 | 0 | 0 |
| Finished below Cycle 50 | 54 | 35 |
| Finished in Cycles 50–100 | 152 | 164 |
| Finished after Cycle 100 | 10 | 17 |
| Median among completed games | 59.0 | 67.0 |
| Mean among completed games | 62.25 | 70.046 |
| Full control also reached at stopping point | 192 | 154 |
| Average initial holdings | 22.75 | 30.639 |

On the matched geography, the paired difference in duration restricted to the first 100 Cycles is **-1.07 Cycles** relative to the historical sample. The block-bootstrap 95% interval is [-4.8, 2.91]. This uses the same 100-Cycle observation window so historical unfinished cases are not discarded.

## Attack choices and resources

| Measure | Matched geography | Generated maps |
|---|---:|---:|
| ground orders | 17786 | 21264 |
| ground_mobile orders | 31 | 29 |
| naval orders | 2498 | 2741 |
| bombard_shared orders | 944 | 1169 |
| structure_assault orders | 1280 | 1909 |
| ration orders | 1579 | 1550 |
| Games using bombardment | 183 | 190 |
| Fortification bonus repairs triggered | 0 | 1 |
| Mean Supply, surviving original factions | 21.98 | 24.74 |
| Mean Manpower, surviving original factions | 28.83 | 32.0 |
| Supply locked, % of surviving faction-Cycles | 3.49 | 2.92 |
| Manpower locked, % of surviving faction-Cycles | 2.4 | 2.1 |

A prespecified 36-game replay audit found **149 bombardments**. **46** had at least one affordable Ground Assault against the same holding at that moment; **10** had an affordable alternative with at least 65% AI victory probability. These counts test whether bombardment is merely a last legal option. They do not establish optimality or substitute for human battle performance.

## Trait results

The entries below count the focal original faction surviving in the winning coalition. Each cell has only 18 cases. Unresolved games are not counted as wins; coalition descendants do not make an eliminated original faction a survivor. Treat differences as investigation signals, not a definitive trait ranking.

| Focal trait | Matched wins / 18 | Generated wins / 18 |
|---|---:|---:|
| siege | 7 | 4 |
| efficient | 6 | 10 |
| mobile | 12 | 9 |
| war_economy | 5 | 7 |
| martial | 9 | 9 |
| salvagers | 8 | 6 |
| void | 3 | 6 |
| swift | 6 | 7 |
| endurance | 5 | 7 |
| dread | 1 | 3 |
| fortification | 1 | 3 |
| industrial | 1 | 1 |

## Player-facing formation audit

The separate 100-setup stress matrix found 32 setups where the inherited formation-scaling rule cannot preserve the difference while keeping each side between one and four formations. This is a deliberately chosen stress matrix, not the frequency of that problem in normal play.
Example: a player starting at 20 Supply/20 Manpower attacks with 5 strength. Ordinary Standard+Minor opposition gives Hard, 1 versus 1; a lone prize Capital gives Harder, 1 versus 2. A prize Capital+Standard+Minor gives a 1-versus-5 formation calculation that the existing scaling rule cannot represent. High-resource oversized player armies can break the rule in the other direction too. No formations were silently removed to make those setups pass. This needs a player-facing rules decision before calling the candidate ready for unrestricted Soulstorm play.

## Evidence and reproduction

Download the revised simulator plus both evidence archives. Extract them into the same folder. `python revised_study.py` resumes or regenerates the 432-case study, refusing mixed fingerprints. `python analyse_revised.py`, `python audit_revised_routes.py` and `python audit_player_setups.py` reproduce the summaries and audits. Analysis of the historical paired difference also requires the earlier integrated-balance-20260917 results in the parent directory or the bundled historical-baseline folder.

Read `revised-study/manifest.json` for exact inputs and completion status, `requalification.json` for the crash-fix replay audit, and the per-game compressed traces for orders, events and outcomes. Human outcomes remain external inputs. Sector work and the mod project remain tabled.

## Assessment and next priorities

The duration target is broadly met in this sample: 316/432 games (73.1%) finish in Cycles 50–100, 89 (20.6%) finish earlier and 27 (6.3%) later. Generated maps put 75.9% inside the target versus 70.4% on historical maps. The historical paired interval crosses zero, so this does not establish a duration improvement over baseline. All games finish by 200, but only 346/432 have full territorial control at the coalition endpoint. This remains a competitive-duration assessment, not a guarantee about clearing every Minor holding.

Bombardment remains used: 2,113 orders across 373/432 games. In the route audit, 103/149 bombardments had no affordable Ground Assault alternative; 46 did, including 10 with at least 65% modelled victory odds. It therefore has a viable niche, often when ground commitment is unavailable, with some use even when assault is attractive. Usage alone does not prove the pricing optimal. The 39,110 ground/mobile assault orders versus 5,239 naval orders contradict a universal fleet-first sequence, but aggregate counts cannot establish that every tactical situation gets the best choice. Preserve all three routes for further playtesting rather than declare bombardment obsolete.

Resource shortages remain consequential: 3,129 Emergency Ration actions. Supply was locked for 3.49%/2.92% of surviving faction-Cycles and Manpower for 2.40%/2.10% (matched/generated). Positive average stocks do not mean a struggling faction has adequate resources; the averages omit eliminated factions after elimination. No additional shortage penalty is justified solely by these aggregates.

All 12 traits were included. Across both arms, focal survivors were mobile 21/36; martial 18; efficient 16; salvagers 14; swift 13; war_economy and endurance 12 each; siege 11; void 9; dread and fortification 4 each; industrial 2. These are shared-block heuristic-bot observations, not independent trait win-rate estimates. Mobile and martial deserve scrutiny for strength; industrial, Dread and Fortification deserve scrutiny for weak payoff or poor bot use. Siege does not show dominance. The Fortification bonus repaired a construction only once across the entire sample: its new secondary effect is demonstrably rare under these bots, so it cannot presently be credited as a substantial counterweight. Audit trait-specific opportunities and bot decisions before choosing new numbers. Do not infer that the lower observed traits are equally weak for a human defender.

The next rules decision should address player formation scaling, alongside the weak defensive/construction trait payoff. Keep the implemented package available as a tested candidate; do not label it fully balanced or replace the preserved baseline silently. AI combat outcomes cannot predict human Soulstorm/Unification win rates. Sector gameplay and the mod project remain tabled.

## Execution recovery record

Matched case 208 initially hit a MemoryError while serializing a snapshot alongside other workers. It completed unchanged when retried alone: same seed, rules and fingerprint, 2,727 replay-validated orders. The original error and recovery record are included in the evidence. The final manifest elapsed_seconds describes cached-result consolidation, not the total study runtime; the main batch took about 4,643 seconds plus the isolated retry and subsequent audits.
