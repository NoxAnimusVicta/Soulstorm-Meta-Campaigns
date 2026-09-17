# Latest work — concrete replacement proposals, 17 September 2026

## Latest decisions — 17 September 2026, follow-up review

Accepted for the connected candidate: holding construction rules and upgrade continuity; Expand Fleet personnel cost; resource-based ground formula; shared Minor pools; naval formula; ground breakthrough and bombardment pricing for testing; Siege successful-assault bonus; Warp transit implementations. Fleet and system construction limits are NOT approved. Remove the merger restriction: absorbed constructions transfer.

System generation is now 2–4 total holdings (planets and stations combined), with a mean of 3: d20 1–5 gives 2, 6–15 gives 3, 16–20 gives 4. The updated proposal contains all twenty mixed profiles. A ten-system/three-Major map averages 30 holdings.

Pending candidates: double the whole derived resource pool of designated prize Minors (including a proposed persistent designation after Capital loss); Fortification retains normal Defend prices and +2 restoration, with one completed defensive construction Integrity repaired if the host reaches full defence; Dread replaces its old effect with defensive Build/Upgrade at 3 Supply per stage. The rejected flat 1/1 Defend and half-defence capture proposals must not be implemented. These trait replacements have arithmetic comparisons, not validated balance claims.

Mandatory evaluation: bombardment must have useful situations beyond being the only legal option at extreme Manpower shortage. Compare all three attack routes together. Exact generator and route-affordability checks pass, but no new full-campaign candidate run has occurred. Source_Rules.md and the qualified engine remain the historical baseline; Dessica stays suspended.

See [updated replacement package](Balance_Replacement_Proposal_2026-09-17.md).


Read Balance_Replacement_Proposal_2026-09-17.md before continuing. It answers the previously missing proposals: uncapped resource/5 score, shared 5/10/15/20 Minor contributions, +1 successful-assault breakthrough, bombardment 2*tier+damage, 2d6 naval rolls with ceil(margin/3) losses, stronger situational traits, a 20-entry map table, and all-alignment local storm bypass implementations with lore boundaries. None of these new numerical proposals has been approved merely by publication.

Creator confirmed the earlier accepted directions; they remain implementation work for a synchronized candidate, not changes already present in Source_Rules.md or the qualified engine. Do not mark that engine rebalanced. Source_Rules.md and all pinned engine files remain unchanged. Dessica remains suspended at Cycle 21, revision 65dc4a60d17b.

184 exact assertions passed. Proposal_Checks_20260917.json records complete dice enumerations, player setup examples, map arithmetic and exposure to the new expansion cost on the old sample. The sample contained 14,800 expansion actions before coalition milestones (648 original-faction histories, median 20); do not claim the old orders remain affordable under changed costs. The whole connected package has not run through full campaigns. Earlier qualification and the 216-campaign sample are historical baseline evidence.

Sector documentation was sought in the public campaign repository recursive tree, local archives and related Warhammer repository file list. No separate Sector rules were located. The creator replied: "Not sure, it should have been in there. Not really relevant until Subsector Scale is sorted properly. Table it". Sector work is TABLED, not permission to reconstruct or invent it. Mod work remains tabled.

A standalone proposal/checks ZIP is published separately from the unchanged historical simulation evidence. Next: review the concrete candidate; implement the agreed package in an isolated variant, reconcile its bot valuations and player setup coverage, then run targeted checks and matched full-game comparisons across richer generated maps. Research sources and campaign-only extrapolations are listed in the report. Do not run rejected cap/difficulty/damage-ceiling proposals.

---

# PRIORITY: creator corrections, 17 September 2026

Read Campaign_Notes_Review_2026-09-17.md FIRST. The prior proposed packages were rejected in material respects. It now contains a point-by-point corrected decision record. Accepted: base operation during upgrades, Expand Fleet personnel cost, ordinary Minor starting-fleet reduction while retaining Planet Fall, stronger prize Minor concept, fixed extra Troop Transport recovery, and random allocation to eliminate faction-message overhead. Planetary capital shipyard exemption favoured; fleet/system slot limits, resource formula, naval redesign and exact trait improvements remain open. Sector/Subsector relationship, global Cycle effects, lore-based travel bypass and lifespan table requirements are corrected. Mod work parked.

This turn corrected documentation only. Source_Rules.md and simulator still implement the old qualified baseline; approved design changes are not yet implemented or validated. No new sims were run. Do not describe the existing readiness result as qualification for new mechanics. Do not implement withdrawn proposal values. Original review is explicitly archived as SUPERSEDED.

---

# Latest work — campaign notes review, 17 September 2026

Every B01–B22 issue and the original source/briefing requests are reviewed in Campaign_Notes_Review_2026-09-17.md. Read that report before selecting changes. It proposes connected packages; none has been adopted or run as a full campaign variant. Original rules/controller hashes are unchanged.

All five formerly unfinished cases reached full control: 102, 108, 111, 115 and 169 Cycles. Each 200-Cycle extension reproduced its original first 100 Cycles and orders exactly, then passed public replay. Including these endings, all 216 campaigns reached full control: mean 63.26, median 61, range 42–169. This is a complete duration distribution for this fixture, not all campaign maps.

Evidence: Integrated_Notes_Evidence.json; Balance_Microtests_20260917.json; integrated-notes-investigation-20260917; Integrated_Balance_Evidence_20260917.zip (includes baseline traces, exact inputs, review scripts, reports and this handover). The first extension attempt failed a Python tuple-versus-JSON-list comparison; normalising the comparison fixed the audit wrapper, without changing engine results. All five corrected extensions passed.

Next: discuss the connected proposals, then implement separate candidate variants and targeted scenario checks before matched full-package campaigns. Pay special attention to construction policy bias, the raw-stockpile combat bonus, Minor Capital support and player/AI differences. Publication verification is recorded in the task response. Dessica remains suspended.

---

# Current handover — 17 September 2026

## Status

The numerical Subsector baseline and production operational controller (horizon zero) passed the release gate. Read Simulation_Readiness_Report.md and Trait_Qualification_Report.md first. 210 regression checks pass; the 432-game trait matrix is complete and 273,209 orders replayed exactly. All worker batches are complete. Existing earlier handovers/reports are historical and are preserved in the bundle.

## User intent and constraints

Work toward proper balance testing before changing the campaign notes' rules. All 12 traits must be fairly represented, with traits fixed between setup and rule-driven changes, not randomly changed each Cycle. The intended average duration is 50-100 Cycles with natural swing and shorter outliers. The user has not chosen the exact ending criterion: report surviving Major coalition and complete holding/Mobile Capital control separately. Human battle outcomes must remain external. Retain Supply costs when testing additional fleet Manpower costs. Preserve B21's baseline defensive-cost behaviour until an explicit alternative is selected.

Dessica remains suspended at Cycle 21 after the Korps turn, revision 65dc4a60d17b. No campaign advancement or event rolls are authorised during source/simulation work. sources/ is read-only. No balance rule was adopted by qualification.

## Reproducible implementation

operational_bots.py contains persistent operation plans, public-state odds and actual-effect probes, threat/economy budgets, repairs/retreats and construction priorities. bot_dispatch.py selects operational, old tactical or independent diagnostic controllers. operational_search.py is optional experimental look-ahead, not qualified by this release. bot_control.py supplies diplomacy/support decisions. Existing engine modules implement all 12 traits and 32 construction profiles.

trait_qualification.py covers 12 traits x 6 strategies x 3 seats x 2 replicates. Every game executes 100 Cycles; traits are assigned between games. Opponents are matched within seed/seat blocks, so raw seat aggregates do not isolate turn-order causation. Core changes invalidate recorded hashes; never reuse stale evidence as current. audit_trait_matrix.py checks coverage; verify_bot_trace.py replays standard cohorts; validate_release.py gates readiness. Run from an extracted Balance_Simulation_Bundle.zip for all evidence directories.

Evidence: trait-qualification-20260916 (all 432 results, compressed complete traces and input pins); bot-current-20260916 (reselection, fresh-process, large, allied, independent/legacy comparisons, stress and 200 Cycle observation). Bot_Behaviour_Review.json records audited cases and limits. simulation_readiness.json pins the release. Earlier bot-development-* and bot-release-20260916 folders are superseded and must not be substituted for current evidence.

## Next work

Begin controlled baseline studies for the campaign notes. Use representative map sizes, more seeds and varied opponents around each proposed change. Do not infer close trait rankings from two matrix replicates. Examine rare-action and less-used construction strategies in targeted scenarios before balancing them. Keep AI-only combat conclusions separate from player setup/difficulty. Record proposed variants separately and seek agreement before adopting rule changes.

## Publication and maintenance

Repository: https://github.com/NoxAnimusVicta/Soulstorm-Meta-Campaigns
Branch: main
Source library: https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/source.html
Suspended campaign: https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/

package_simulation.py bundles current code, evidence and historical work. build.py generates source.html and the unchanged campaign. The included GitHub Actions workflow publishes dist/ on main pushes. Browser upload is available through the signed-in repository owner session; no claim of publication should be made without a successful deployment and live-content check. The final chat response records verification of this release. Do not change repository visibility.

## Active integrated balance work — 17 September 2026

User rejected sequential isolated fixes. See Integrated_Balance_Review.md for the connected issue map and joint comparison procedure. A 216-game ten-system current-rules sample is now executing via integrated_balance_sample.py (three worker processes, no agent delegation). Results and compressed replay-verified traces are in integrated-balance-20260917. This crosses 12 focal traits, six strategies and three seats; there are 18 matched random blocks, not 216 independent replicates. No candidate package has been run or adopted yet. Do not present this running sample as completed. Resume from the manifest/case files; preserve qualified engine hashes. Analyse wartime resources before milestones, not post-conquest accumulation. The new study files have not yet been published.

## Integrated sample completed — 17 September 2026

All 216 ten-system campaigns completed their 100-Cycle observation. manifest.json is complete, results.json has all unique cases 0–215, and 199,376 decisions have matching public replay verification. All compressed traces are present. analyse_integrated_balance.py generated Integrated_Balance_Baseline_Report.md and integrated-balance-20260917/analysis.json.

211 campaigns reached each ending milestone; five remained unfinished at Cycle 100. Among completed campaigns, mean full control was 61.90 Cycles (median 60, range 42–99); mean single surviving Major coalition was 61.47. Completed-only means exclude unfinished campaigns and are not uncensored duration estimates. One map layout and 18 matched seed blocks remain limitations.

Next: inspect shared resource/combat/construction patterns and the five unfinished campaigns against the complete issue map in Integrated_Balance_Review.md, then compare coherent packages. Do not adopt isolated fixes or infer balance from aggregate duration alone. No candidate packages have yet been tested or adopted. Dessica remains suspended. These new study files/results are local and have not yet been published to GitHub.
