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
