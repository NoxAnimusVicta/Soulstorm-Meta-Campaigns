> **Latest concrete proposals — 17 September 2026:** Read [Balance_Replacement_Proposal_2026-09-17.md](Balance_Replacement_Proposal_2026-09-17.md). It supplies replacement formulas, costs, player examples, a d20 generator and lore-supported storm installations. Candidate rules remain pending approval and integrated validation; Sector work is now tabled by the creator.

## Latest decisions — 17 September 2026, follow-up review

Accepted for the connected candidate: holding construction rules and upgrade continuity; Expand Fleet personnel cost; resource-based ground formula; shared Minor pools; naval formula; ground breakthrough and bombardment pricing for testing; Siege successful-assault bonus; Warp transit implementations. Fleet and system construction limits are NOT approved. Remove the merger restriction: absorbed constructions transfer.

System generation is now 2–4 total holdings (planets and stations combined), with a mean of 3: d20 1–5 gives 2, 6–15 gives 3, 16–20 gives 4. The updated proposal contains all twenty mixed profiles. A ten-system/three-Major map averages 30 holdings.

Pending candidates: double the whole derived resource pool of designated prize Minors (including a proposed persistent designation after Capital loss); Fortification retains normal Defend prices and +2 restoration, with one completed defensive construction Integrity repaired if the host reaches full defence; Dread replaces its old effect with defensive Build/Upgrade at 3 Supply per stage. The rejected flat 1/1 Defend and half-defence capture proposals must not be implemented. These trait replacements have arithmetic comparisons, not validated balance claims.

Mandatory evaluation: bombardment must have useful situations beyond being the only legal option at extreme Manpower shortage. Compare all three attack routes together. Exact generator and route-affordability checks pass, but no new full-campaign candidate run has occurred. Source_Rules.md and the qualified engine remain the historical baseline; Dessica stays suspended.

See [updated replacement package](Balance_Replacement_Proposal_2026-09-17.md).


> Creator corrections take precedence: read Campaign_Notes_Review_2026-09-17.md. Earlier proposed packages were withdrawn; the baseline is historical evidence, not approval of those packages.

# Integrated campaign balance review — 17 September 2026

## Mandate

Review the campaign notes as a connected system. Do not adopt isolated fixes and then compensate for their side effects later. The user rejected a serial "first fleet costs, then everything else" approach.

The shared baseline is complete: 216 ten-system campaigns, each observed for 100 Cycles. Twelve focal traits, six policies and three seats are crossed. All begin with the source's 20/20 resources, ordinary fleets at 5 strength and the existing Mobile Capital exception. Opponents and event seeds match within strategy/seat blocks across focal traits and future packages. This is 18 random seed blocks, not 216 independent replicates. The fixed synthetic map is a controlled starting point, not an approved generation table or a complete representation of campaign geography.

Preserve the qualified engine and bots. No proposed numerical rules are adopted. Dessica remains suspended.

## One connected issue map

| Notes | Connected questions | Evidence from the same campaigns and follow-up scenarios |
|---|---|---|
| B01, B04, B05, B11 | Capital construction concentration, spending/saving, military Manpower demand, viable non-economic builds | Resource histories before endings, costs and recovery actions, investment location/type, interruption losses, capture/force growth. Judge construction limits together with additional resource sinks and income. |
| B02, B03, B08, B09, B10, B13 | Minor resistance, naval-first versus ground-first, shared Minor economy, combat variance, bombardment | Opening captures, target tiers, naval/ground/bombardment choices, damage and losses, campaign milestones. Test resistance and attack-cost packages together; player difficulty and enjoyment require separate assessment. |
| B12, B17 | Trait strength, construction access, alignment resilience | Trait-by-policy outcomes under every candidate package; targeted hostile events and construction cases. AI-only outcomes cannot measure the full player benefit of Siege Doctrine or Dread Reputation. |
| B07, B16 | Map density, travel, event pressure, 50–100 Cycle duration | Matched map/event scenarios; duration distribution with unfinished campaigns explicitly censored. Expand beyond one topology before claiming representative campaign duration. |
| B14, B21, B22 | Planet Fall allocation, automatic defensive resource settlement, station timing | Keep current baseline, then explicit targeted comparisons. Test their resource/repair feedback within the same packages. |
| B06, B15, B18 | Alignment terminology, fixed raider identity, personnel continuity | Preserve adopted directions. Unwritten Sector rules/lifespans require design, not fabricated simulation results. |
| B19 | Credible strategic testing | Exact replay, varied policies/opponents/traits, inspect apparently dominant or failed strategies, disclose bot limitations. |
| B20 | Mod assets/subproject | Separate development work; cannot be assessed by the campaign economy simulator. |

## Comparison procedure

1. Collect and inspect the shared current-rules sample before selecting numerical candidate packages.
2. Identify joint failure patterns: for example idle Manpower plus capital investment plus weak expansion, rather than treating three metrics as three unrelated problems.
3. Specify coherent candidate packages against the whole issue map. Preserve Supply costs for military materials and aim for stronger useful trait choices rather than blanket nerfs.
4. Run each package against exactly matched initial scenarios and seed blocks. Use selected component combinations to detect interactions; those diagnostic comparisons are not proposals to adopt changes individually.
5. Compare distributions and trade-offs, not one overall win-rate score. Track resource pressure, genuine choices, deficits, expansion, investment risk, trait/policy sensitivity and both campaign-ending milestones.
6. Stress promising packages on more independent seeds, varied maps and deliberately relevant construction/combat scenarios. Do not extrapolate sparse decisions into balance conclusions.
7. Present one integrated proposed revision with unresolved design questions and adverse effects clearly identified. Adoption remains a user decision.

For duration and resources, stop analytical observation at the relevant ending milestone even though the simulator continues to Cycle 100. Post-conquest stockpiles are not evidence of wartime resource surplus. Report both single surviving Major coalition and full holding/Mobile Capital control until the campaign victory condition is settled. Inspect and, where useful, extend unfinished campaigns rather than treating Cycle 100 as a victory.

## Evidence and resumption

- Runner: integrated_balance_sample.py
- Pinned inputs, manifest and individual results: integrated-balance-20260917/
- Each complete case has a compressed full trace and exact public-order replay count.
- The runner resumes complete cases and refuses changed engine fingerprints.
- A running manifest is not a completed study. Check actual case count and completion status before reporting results.


## Review completed — 17 September 2026

Campaign_Notes_Review_2026-09-17.md now covers every issue with evidence, proposed changes and remaining design/test limits. All five formerly unfinished cases reached full control: 102, 108, 111, 115 and 169 Cycles. Each 200-Cycle extension reproduced its original first 100 Cycles and orders exactly, then passed public replay. Including these endings, all 216 campaigns reached full control: mean 63.26, median 61, range 42–169. This is a complete duration distribution for this fixture, not all campaign maps. No proposed package has yet been simulated or adopted.
