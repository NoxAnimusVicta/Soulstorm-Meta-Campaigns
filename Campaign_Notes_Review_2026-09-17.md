> **Latest concrete proposals — 17 September 2026:** Read [Balance_Replacement_Proposal_2026-09-17.md](Balance_Replacement_Proposal_2026-09-17.md). It supplies replacement formulas, costs, player examples, a d20 generator and lore-supported storm installations. Candidate rules remain pending approval and integrated validation; Sector work is now tabled by the creator.

# Campaign Notes — corrected decisions and requirements
17 September 2026 • Supersedes the first proposed v0.2 package

The creator's playtest feedback and design intent govern this review. The previous proposal over-weighted numerical AI results, misinterpreted several notes and recommended inappropriate player-facing changes. Its caps, permanent difficulty trait, four-damage ceiling, small-system generator and damage-only storm protection are withdrawn.

This is the design decision record for the next synchronized rules/simulator revision. Approved design changes below are not yet implemented in Source_Rules.md or the simulator. Neither the 216-game sample nor previous qualification validates those new mechanics. Dessica remains suspended and unchanged. No new simulation batch was launched for this correction.

## 1. Construction slots and capital shipyards
The intended exemption is the built-in shipyard of an established Capital, including a Mobile Capital. It occupies no constructed slot. Ordinary Orbital Shipyards remain paid constructions; they are not free on every planet and occupy the planet's construction slot.

One planetary construction per holding remains the working proposal. The creator favours the capital exemption; fleet/system limits remain open, not approved. Distinguish limiting the number of attached constructions from limiting upgrade levels: these are different rules.

Recommendation for discussion: one constructed attachment per ordinary fleet is a coherent specialization rule, allowing its existing upgraded version in that slot. A whole-system limit of one construction is much broader and could prohibit combining a Defence Station with a Repair Station regardless of system size. Do not adopt that limit by implication. Decide system capacity separately after defining richer system sizes.

## 2. Upgrading — accepted design
Retain the completed base effect while its Integrity is at least the original full maximum. New upgrade stages absorb damage first in this sense. A Major at 8/10 still provides its base effect; at 5/10 it still does; at 4/10 it is inactive. The upgraded effect begins only after full completion at 10/10. Minor thresholds are 3 and 6. Existing full-host and paid rebuilding requirements remain.

## 3. Fleet personnel — accepted design
Expand Fleet costs 1 Supply and 1 Manpower, restoring up to its existing two strength. Supply material costs remain. Retain Create Fleet at 1 Supply/1 Manpower for now; higher costs may be considered if connected testing supports them. Apply existing trait waivers only to the resource they actually waive.

## 4. Resources and battlefield capability
Withdraw the proposed contribution cap at 20 or 30. It flattens materially different readiness bands and conflicts with their intended purpose. Critical, Rationed, Sustainable, Surplus and Abundant must continue to differ in battlefield capability.

No replacement coefficient or difficulty rule is approved. First compare actual player setups across all five bands, holding other conditions constant: Supply changes Soulstorm difficulty and Manpower changes available formations. Then examine the numerical resolver's representation of those differences. Do not equate a d20 modifier with a Soulstorm difficulty step or use AI survival results as human win rates.

## 5. Ordinary Minor fleets — accepted direction; Planet Fall retained
Halve ordinary starting Minor fleet strength using the previously proposed rounded-up calculation. This is a setup change. It does NOT remove Planet Fall damage, fleet destruction or elimination on loss of the final fallback.

AI ground resolution adds defending fleet strength to its combat total. Player battles use hostile in-system strength to add enemy formations: 5–9 gives +1, 10–14 gives +2, 15–19 gives +3 before other modifiers. Consequently a six-strength defence becoming three can remove one enemy formation; twelve becoming six reduces the fleet contribution from two extra formations to one. Final team size still includes Manpower and other existing rules. This player-facing effect is central to the creator's complaint.

## 6–7. Minor shared resources and prize factions
Withdraw the previous capped, damage-weighted formula. The outstanding design requirement is a simple holding/tier-based shared faction value whose numbers are chosen sensibly, without an arbitrary cap flattening its growth. No replacement formula is approved.

The exceptional-prize concept is accepted: rare stronger Minor powers with Capital-class holdings and unhalved fleet rules. Remove the proposed special resource cap. Preserve static Minor behaviour unless a separate rule explicitly changes it.

## 8. Fleet combat
Withdraw the complete proposed 2d10/four-damage package as an unapproved solution. A fixed four-damage maximum lets a full five-strength fleet survive one battle against overwhelming strength regardless of margin. That contradicts the required consequences of force disparity.

Retain the current baseline while redesigning. Any replacement must allow decisive destruction from overwhelming superiority and preserve the reason to build/commit greater strength. Dice-distribution changes and damage scaling must be judged separately; reducing variance does not require capping losses. No new numerical formula is approved.

## 9–10. Three viable attack choices
The objective is contextual strategy, not a mandatory naval battle → bombardment → final ground assault sequence. No new ground-assault penalty is approved. Player skill can make a contested ground assault attractive, allowing capture and Planet Fall damage without first risking fleets in a naval engagement.

The original notes floated orbital interaction, but the creator's latest clarification controls: investigate and, where needed, improve ground-first viability rather than infer authorization for a penalty.

Aggregate attack counts do not answer this question. Compare equivalent target situations: surviving orbital defenders, resource/Manpower pressure, likely player outcome, time until capture and enemy recovery. Naval battle should be valuable when destroying orbital capability is the objective; bombardment when avoiding personnel risk justifies its costs and delay; ground assault when securing territory and Planet Fall benefits justify combat risk.

Bombardment costs and downsides remain an active design problem. The previous recommendation to largely leave it alone was not a resolution of the playtest complaint.

## 11. Troop Transports — accepted design
Replace percentage increments with one additional committed Manpower recovered after a successful assault for a base transport, two for upgraded, capped at the actual commitment. Only the best participating transport applies. Retain the normal base recovery underneath this additional return. Implement and test alongside the fleet personnel change.

## 12. Traits and actual Soulstorm difficulty
Withdraw Dread Reputation's proposed permanent difficulty shift and corresponding blanket AI modifier. A Soulstorm difficulty step cannot be valued as a modest interchangeable dice bonus.

Siege and Fortification changes received agreement in direction only, with explicit concern that they remain too weak. Do not mark their proposed values approved. Strengthen their relevant identities against the useful traits rather than simply nerf the useful ones. Player battle consequences and opportunity frequency must be assessed; no human win rates were measured by this sample.

The preliminary documentation check found a Unification author explicitly describing increased AI resources on Insane and distinct optional AI tactics settings. This supports treating difficulty and match rules as material, separate settings; it does not establish exact values in the creator's installed version. Do not claim current version-specific calibration from that historical comment:
https://www.moddb.com/mods/unification-mod-dawn-of-war-soulstorm/downloads/unification

## 13. System generation
Withdraw the small-system d6 table. Design at least a d20 table with varied, richer multi-holding systems; use Dessica's actual systems as references. Do not assume a ten-system layout with around two holdings per system represents the desired campaign. Holdings-per-system, station mix, Minor ownership and prize locations require meaningful variety. Exact size distribution remains open.

## 14. Lore-supported storm bypass
The required technology includes bypassing the Warp Storm movement restriction. Damage-only shielding does not satisfy the request. Ordinary Imperial Geller protection/navigation is not an adequate explanation of immunity.

Resolve a credible implementation for every relevant alignment before introducing the construction. Chaos and Necron concepts do not justify invented equivalences for everyone else. The cross-alignment lore question remains unresolved; no universal protection profile is ready for implementation.

## 15. Allocation, deficits and automatic effects
Randomise Planet Fall allocation to avoid asking another faction chat to select each damaged fleet. Working scope: use a recorded random draw wherever the existing damage-priority rules otherwise require a choice, including strongest-fleet ties and eligible destruction choices. This preserves existing strongest-first/eligibility restrictions while eliminating the decision-message overhead. Do not silently change all priority rules into unrestricted random targeting.

Voluntary Attack, Defend, Build and other spending actions cannot reduce a spent resource to zero. Involuntary defensive costs, enemy effects and upkeep can trigger deficits. An already locked resource ignores further losses and income. Recovery is possible; calling a deficit irreversible was wrong. The earlier settlement discussion concerned involuntary defender bookkeeping, not a right to attack using unaffordable resources. No altered settlement rule is adopted.

Automated construction effects occur at the specified global Cycle transition, not on their owner's turn or as a Fleet/Faction Action. The current engine already places system fire and repair in closing(), outside faction turns. Its internal fire-before-repair order is baseline behaviour, not a newly accepted ruling. Income effects retain their specified Logistics schedule; do not turn Logistics income into every-Cycle income.

## 16. Raiders, Sector layer, personnel and mod work
Raiders are temporary encounter participants, not a persistent resource-owning campaign faction. The simulator's 5-strength/20-Supply/20-Manpower profile was a provisional arithmetic device totaling 45, not actual raider reserves. Do not impose caps or an economy on them. Their identity remains fixed.

Sector play begins after multiple Subsector campaigns determine its roster. Winners control Subsectors and act at Sector level. An attack on another Subsector is resolved through a whole Subsector campaign, effectively a nested Sector action. The earlier stockpile-import restriction was invented and is withdrawn. Resource conversion and scheduling may need later design, but neither has been decided here.

Add a species/force lifespan reference table alongside the personnel-per-Manpower reference, covering typical lifespan, relevant life extension and succession treatment. Do not substitute an invented years-per-Cycle default for that requested table. Values need supported lore or explicitly agreed campaign assumptions; succession retains the trait.

The mod project is parked until balancing is complete. No further mod work is part of the current balance review.

## Testing requirements and evidence status
The 216 campaigns and five long-war extensions remain a reproducible historical baseline. They do not establish that the playtest concerns are resolved. The observed 63.26-Cycle average belongs to one sparse synthetic layout, with specified bots and AI-only battle resolution.

Next work must jointly examine the accepted mechanics and the creator's corrected requirements. Do not reuse the withdrawn caps, naval ceiling, permanent difficulty trait or d6 generator. Do not launch another expensive broad run until the candidate rules and player-facing setup cases are coherent. No simulated win percentage overrides the creator's report that a mechanic is unfun or creates the wrong decisions.

Original proposal retained only as Campaign_Notes_Review_2026-09-17_SUPERSEDED.md. The current document takes precedence.
