# Connected balance replacement proposal

17 September 2026. **Proposal for review, not an adopted rules release.**

This supplies the missing formulas, costs, system table and lore implementations. The accepted changes from the corrected decision record are included as dependencies. Dessica stays suspended at Cycle 21. Source_Rules.md and the qualified baseline engine are unchanged. Sector-scale work is tabled at the creator's explicit instruction on 17 September; no new Sector interpretation is proposed here. The mod project also remains tabled.

The numbers below have exact local arithmetic checks, including player setup examples and naval outcomes. They have NOT passed a full-campaign candidate comparison. Previous campaign results describe the old rules, not this package. The distinction matters because easier early conquest and a denser map pull campaign duration in opposite directions.

## 1. Construction capacity and upgrade continuity

Recommended capacity rules:

- Each planet, station or Mobile Capital has **one permanent planetary/orbital construction slot**. Its established Capital shipyard is built-in and uses no slot. An ordinary shipyard built elsewhere uses the slot and costs normally.
- Each ordinary fleet has **one attached construction**, which may receive its existing upgrade. The Mobile Capital uses its holding slot rather than gaining a second free ordinary-fleet slot.
- Each faction may build **one system construction of each type per system**, not just one construction across the whole system. This permits a Defence Station and a Repair Station together but prevents stacking multiple copies of either. Effects of identical allied installations do not stack on the same fleet/holding in the same Cycle; apply the strongest eligible effect once.
- A completed Void Station becomes a holding, so it does not block construction of another Void Station. Only one unfinished Void Station project per faction per system at a time. Each completed station has its own holding slot.
- Consolidation Works improve the holding itself and do not permanently occupy its construction slot. They still consume the normal paid Construction Actions and require the host to be at full defence.
- Orbital Shipyard → Grand Orbital Shipyard → Grand Orbital Shipyard Complex is one infrastructure line, not multiple occupied slots. A Grand Shipyard developed from a Capital's free built-in yard occupies the ordinary slot. Its build and upgrade costs remain payable.
- A Fleet Merge remains legal only if the transferred attachments fit the surviving fleet's capacity. Two attached constructions cannot be combined into one slot through merging; keep those fleets separate. Do not silently destroy either construction. Empty receiving fleets may accept the absorbed fleet's attachment normally.

This is a proposed new-campaign restriction. It does not delete Dessica's existing constructions.

**Accepted upgrade continuity:** an upgrading Major retains its base effect at 5–9/10 Integrity; an upgrading Minor at 3–5/6. At 10/10 or 6/6 the upgraded effect starts. Below the original threshold neither ordinary effect operates. Damage is deducted from the current Integrity, so new stages provide a buffer. The full-host requirement remains. Preserve the existing special rule for completed Flagships/Assault Cruisers: their completed strength remains until the fleet is destroyed.

## 2. Resource use and combat formula

**Accepted fleet personnel cost:** Expand Fleet costs **1 Supply and 1 Manpower** for up to +2 strength, limited by actual fleet capacity. Create Fleet remains 1 Supply/1 Manpower. Void Supremacy waives only Supply. Voluntary payment must leave each spent resource above zero.

**Proposed AI ground score:**

`d20 + participating Fleet Strength + floor(post-cost Supply / 5) + floor(post-commitment Manpower / 5) + situational modifiers`

There is no contribution cap. Every additional five points of either resource adds another roll point. A full twenty-point readiness band adds four. The existing Major storage maximum of 100 is a separate rule and remains unchanged. Zero-resource deficit rules remain separate, including forced defence and isolated defence; this formula grants no permission to spend the last resource point.

Why divide by five: currently a 20-point stockpile lead in ONE resource exceeds the largest possible difference between two d20 rolls. The proposal makes that lead significant without automatically deciding an otherwise equal engagement. It also reduces the numerical gap between raw fleet strength and reserves. It does not remove readiness or convert military resources into civilian wealth.

| Post-cost resources; otherwise equal | Numerical advantage | Exact AI attacker win probability |
|---|---:|---:|
| 30 Supply /30 Manpower versus 30/30 | 0 | 47.5% |
| 50/30 versus 30/30 | +4 | 66.0% |
| 50/50 versus 30/30 | +8 | 80.5% |
| 10/30 versus 90/30 | -16 | 1.5% |

These enumerate all 400 d20 pairs. Ties favour the ground defender. They are **not human Soulstorm win rates**. Twenty resource points still matter; Critical does not equal Abundant. Within a band, the numerical game has five-point increments, whereas player setup retains the named twenty-point bands.

**Player battles:** keep the existing Supply→difficulty and Manpower→formation tables. No global easier-difficulty adjustment or permanent trait difficulty shift is introduced. Player outcomes remain reported outcomes. We must inspect the resulting matchup and the opportunity cost of spending before accepting the whole package; a d20 probability does not calibrate Unification difficulty.

**Matching numerical modifier proposal:** with the smaller resource contribution, use Defended +4 instead of +15; Ambush +4 instead of +10; Intel Breakthrough +4 instead of +10; Bunker +4/+8; Isolated Defence -8 instead of -15. Preserve their existing player setup effects. These are candidate numerical weights, not assertions that one difficulty step equals exactly four roll points in Soulstorm. Siege ignores the Defended contribution in both resolution modes. Other bonuses keep their specified scope; naval installations are not ground modifiers.

The temporary AI raider becomes a fixed **d20 +13** encounter score: the old provisional 5+20+20 arithmetic transformed through this resource formula is 5+4+4. It owns no Supply/Manpower pool, receives no income and is never given a resource cap. Player raids retain the separate hostile formation and fixed campaign identity.

**Use of existing evidence:** the 216 old-rule campaigns contain 14,800 Expand Fleet actions by the original three Majors before their respective coalition milestones, a median of 20 per faction history. Charging the new crew cost would therefore matter substantially. This is exposure on old orders, not a claim those orders remain affordable or that the new economy will evolve identically. It is a reason to avoid raising Create Fleet at the same time without evidence.

## 3. Shared Minor resources and fleets

Each controlled holding contributes the following to BOTH the Minor faction's shared Supply and shared Manpower:

| Holding | Supply contribution | Manpower contribution |
|---|---:|---:|
| Minor | 5 | 5 |
| Standard | 10 | 10 |
| Major | 15 | 15 |
| Capital, exceptional prize faction | 20 | 20 |

**Formula:** add the contributions of every holding the Minor still controls. No starting constant, damage fraction, logarithm or artificial resource cap.

Examples: Standard+Minor =15/15; Major+Standard+Minor =30/30; Capital+Major+Standard+Minor =50/50. Losing the Minor in the second example changes the whole faction to 25/25. Losing the Major next leaves 10/10. Losing the final fallback eliminates the faction and its remaining fleets.

These remain derived military-support values, not a spendable treasury: Minors do not acquire strategic turns, income accumulation or deficit tracks. Pay the existing temporary defensive commitments for the individual combat calculation. Do not persist Major resource penalties against this pool.

**Important change:** damaging a holding's defence does not reduce its contribution. Capturing it does. Bombardment weakens fortifications; conquest removes the wider faction's supporting infrastructure. This directly removes the present double reward in which bombardment both reduces defence and makes that planet's resource-based battle dramatically easier.

**Accepted starting fleets:** ordinary Minor strength = `ceil(total starting maximum holding defence /2)`. Fill ordinary five-strength formations, then the remainder. Regeneration cannot recreate destroyed fleets or grow beyond initial capacities. Never recalculate away damage or create new strength when a planet falls. Apply Planet Fall and final-fallback elimination normally. Prize Minors retain the unhalved calculation, use the same uncapped resource-contribution table, and have a Capital-class holding.

**Player setup checks**, before traits, events or constructions; attacker starts at 20/20:

| Assault | Old setup | Proposed setup |
|---|---|---|
| One full fleet attacks the Standard world of a Standard+Minor owner | Insane, 1 versus 2 | Hard, 1 versus 1 |
| Two full fleets attack the Major world of a Major+Standard+Minor owner | Insane, 1 versus 4 | Harder, 1 versus 1 |

These use paid Supply and committed Manpower in the actual existing player setup calculator. The improvement comes from the proposed ordinary Minor fleet/resource changes, not a free player difficulty trait. Against richer regional powers and Major factions, resources and formations still scale normally. Scenario Minor resources above 100 would need an explicit extension of the last display band (81+) without truncating the derived value; the proposed generator below does not create that case.

## 4. Three attack routes with different uses

**Ground Assault candidate:** keep the existing tier Supply cost (1/2/3/4) and compulsory Manpower commitment `floor(participating strength /5)`. On a successful assault add **+1 breakthrough damage** to that base, plus existing construction/event bonuses, then apply defensive damage reductions. A below-five-strength force still cannot launch an ordinary Ground Assault under the current no-minimum ground rule. The breakthrough adds no formation slot and does not increase attacker Manpower commitment, just as damage-only constructions do not. Defender commitment uses total incoming damage under the relevant existing AI/player procedure. No new orbital attrition or Fleet Battle initiation cost is added.

| Participating strength | Manpower commitment | Successful damage before other modifiers |
|---|---:|---:|
| 5–9 | 1 | 2 |
| 10–14 | 2 | 3 |
| 15–19 | 3 | 4 |

Ordinary defeat deals no damage; preserve Siege's separate defeat effect. Apply Planet Fall using the final assault's damage under the existing allocation rule. The extra point does not bypass Void Shields or an invulnerable Planetary Shield Network.

**Uncontested Bombardment candidate:** retain no Manpower commitment, no dice and the one-defence floor. Replace the price with:

`Supply cost = twice the target's tier cost + the strike's calculated bombardment damage`

Calculate damage from participating strength and applicable bombardment bonuses, before the target's one-defence floor reduces actual damage. Paying for an oversized strike wastes ammunition; do not refund it. This prevents a large fleet applying more destruction for the same fixed ammunition payment.

| Target | One-damage strike | Three-damage strike |
|---|---:|---:|
| Minor | 3 Supply | 5 Supply |
| Standard | 5 Supply | 7 Supply |
| Major | 7 Supply | 9 Supply |
| Capital | 9 Supply | 11 Supply |

**Worked choice:** a five-strength fleet facing an unguarded Standard at 4/4 can capture it with two successful Ground Assaults: 4 Supply in total and 2 net Manpower, before transports/traits. Bombarding three times and then winning the final assault costs 17 Supply, four Fleet Actions and 1 net Manpower. The first route is cheaper and faster if it wins; the second guarantees the first three defence points and preserves scarce troops. With only 2 available Manpower, the commander cannot voluntarily fund two one-Manpower assaults, but can fund that bombardment route and one final assault. Failure risk, regeneration between interruptions, Defended status, constructions, events and the player's skill still matter.

A ten-strength force can capture a Minor holding immediately on a successful assault even with hostile fleets overhead. That can trigger Planet Fall and remove a final-fallback fleet, providing a concrete reason to attack the ground first. Conversely, defeating a dangerous mobile enemy fleet can protect several systems and remove its future Fleet Actions; capturing one of its many holdings may leave that threat intact. Naval action is then valuable independently of preparing bombardment.

The bot comparison must evaluate complete affordable routes and their consequences, not just immediate damage per action. Failed assaults and counterattacks must remain in the evaluation. The arithmetic examples are not proof that all three routes will be selected well by the existing controller.

## 5. Less swingy naval combat without a damage ceiling

**Candidate:** each side rolls `2d6 + actual participating Fleet Strength + applicable naval bonuses`. Keep the single one-strength initiation payment, one Fleet Action, free defensive participation and ordinary participation rules. A tie does no damage. The loser takes `ceil(winning margin /3)` damage on each participating fleet. Damage has no maximum; reaching zero destroys the formation. Attached construction damage follows normal host damage rules. This replaces the old 16+ automatic-destruction band with one continuing formula.

For guarded targeted Structure Assaults, apply the same winning-margin damage to the target only on an attacker win; the defending fleets are not damaged. On attacker loss apply normal naval losses. High enough damage destroys the structure at zero. This replaces that attack's old separate 16+ destruction clause too.

Exact outcomes with no construction bonuses:

| Starting forces | Attacker wins | Full five-strength defender destroyed in one battle |
|---|---:|---:|
| 5 versus 5 | 33.56% | 0% |
| 10 versus 5 | 84.10% | 0.39% |
| 20 versus 5 | 100% | 66.44% |
| 100 versus 5 | 100% | 100% |

The initiating equal fleet begins the roll at 4 versus 5, explaining the defensive advantage. A damaged initiating fleet can still be destroyed. The twenty-full-fleets example always destroys the lone five-strength opponent, even on the worst dice. Thus neither a lucky small force defeating overwhelming strength nor a guaranteed one-strength survivor is built into the rule.

This candidate makes naval superiority substantially more reliable and could encourage concentrated fleets. The connected test must check that risk against multiple simultaneous ground attacks and the cost of leaving systems undefended. It is not yet a naval balance verdict.

## 6. Strengthen situational traits through campaign effects

These replace the rejected trait suggestions. They are proposals, not the creator's already approved values.

- **Siege Doctrine:** retain ignoring Defended and its existing one-damage-on-defeat effect; add +1 damage on a successful Ground Assault, on top of the general breakthrough. Five strength therefore deals three on a win before mitigation, versus two for another trait. No new permanent Soulstorm difficulty change is added. Preserve existing defeat/capture semantics rather than silently changing them here.
- **Fortification Experts:** a planetary/station/Mobile Capital Defend action costs **1 Supply and 1 Manpower**, restores the normal tier amount **plus 2**, and grants normal Defended status. A Capital repairs up to six defence for 1/1 instead of four for 4/4: six resources saved when that action is needed. This does not discount construction Repair, repair above maximum, waive the voluntary-deficit rule or grant a second action.
- **Dread Reputation:** retain the existing enemy successful-defence return penalty, and add **captured holdings begin at half maximum defence, rounded up, instead of one**. Minor 2→1; Standard 4→2; Major 8→4; Capital-class 12→6. This represents a more intact surrender/occupation, rewarding conquest and reducing consolidation time. Apply battle damage and construction destruction before changing ownership; do not restore destroyed structures or give free construction Integrity. Do not grant a second Capital designation/shipyard or capture a Mobile Capital. No difficulty or army-count modifier.

Dread's benefit is deliberately after the fight; it cannot make the player's next enemy easier merely for possessing the trait. A Standard capture saves one defence point, a Major three and a Capital-class five. That is materially more than changing a fractional return which usually rounds identically. Fortification is responsive repair efficiency; Siege is faster offensive progress; Dread is stronger consolidation after conquest. Keep the useful economic/mobile traits intact while comparing these candidates together.

**Accepted Troop Transport:** normal successful-assault recovery plus one committed Manpower (two upgraded), capped at what was committed, best participating transport only. No creation of additional personnel through the return.

## 7. A twenty-result system generator

Roll d20 for each non-home system. All listed planets/stations are mechanically usable holdings; additional uninhabitable astronomical bodies are scenery and grant no income. Each exact result has a 5% chance. Two-holding systems occur on 1 and 3, not only on a maximum roll; most systems contain three to five holdings. Mean holdings per roll is exactly four.

| d20 | Planets | Additional stations | Total holdings |
|---:|---|---|---:|
| 1 | 2 Minor | — | 2 |
| 2 | 3 Minor | — | 3 |
| 3 | 1 Standard, 1 Minor | — | 2 |
| 4 | 1 Standard, 2 Minor | — | 3 |
| 5 | 1 Standard, 3 Minor | — | 4 |
| 6 | 1 Standard, 2 Minor | 1 Minor station | 4 |
| 7 | 2 Standard, 1 Minor | — | 3 |
| 8 | 2 Standard, 2 Minor | — | 4 |
| 9 | 2 Standard, 1 Minor | 1 Standard station | 4 |
| 10 | 1 Major, 2 Minor | — | 3 |
| 11 | 1 Major, 1 Standard, 1 Minor | — | 3 |
| 12 | 1 Major, 1 Standard, 2 Minor | — | 4 |
| 13 | 1 Major, 2 Standard, 1 Minor | — | 4 |
| 14 | 1 Major, 1 Standard, 1 Minor | 1 Minor station | 4 |
| 15 | 3 Standard, 2 Minor | — | 5 |
| 16 | 2 Standard, 2 Minor | 1 Minor station | 5 |
| 17 | 1 Major, 2 Standard, 2 Minor | — | 5 |
| 18 | 2 Major, 1 Standard, 2 Minor | — | 5 |
| 19 | 1 Major, 2 Standard, 2 Minor | 1 Standard station | 6 |
| 20 | 2 Major, 2 Standard, 2 Minor | 1 Major station | 7 |

For equal opening opportunities, each Major home system contains its Capital plus a Standard and a Minor held by a hostile ordinary Minor faction; only the Capital starts owned by the Major. Names, world themes and station appearance can differ. This is a candidate standard opening, not a retcon to Dessica.

For ordinary non-home ownership roll another d20: 1–6 separate one-holding Minor powers; 7–15 group holdings into two-holding Minor powers; 16–20 group into three-holding Minor powers. Randomise holding order before grouping; a remainder forms a smaller group. These are generation patterns, not a universal ownership cap. Unrelated Independent factions do not become allies automatically.

Place one declared prize Minor in a campaign of up to ten systems, two in a larger setup. Randomly choose non-home systems and upgrade the highest-tier planet in each to a Capital-class holding; stations are not Capitals. Its owner uses unhalved fleet calculation. Keep the remaining generated holdings and ownership unless the scenario explicitly allocates them to that prize faction. This makes the prize visible and contestable rather than hiding its existence behind a rare roll.

A ten-system, three-Major map now averages 37 holdings (nine home-system holdings plus seven rolls averaging four). Compare it with Dessica's 27 and the old sample's specific fixture; do not report the old 61-Cycle median as a prediction for this map. The target remains typical completion in 50–100 Cycles with shorter and longer outliers.

## 8. Warp Storm bypass, with an implementation for each alignment

**Mechanical proposal: Major System Construction — Storm Transit Installation.** Five Build actions, 5 Supply per action, 5 maximum Integrity; no upgrade initially. It uses the same-type system limit above and the existing system-construction build/capture/destruction requirements.

At the event roll, an active installation protects its owner's fleets and Mobile Capital in that system from the Warp Storm's one-point damage, including consequential attached-construction damage. During the storm, those assets may use their normal Fleet Movement action to depart that system for a legal destination despite the movement prohibition. A facility must still be active at departure; it grants no extra action. Protection does not extend to assets elsewhere. Explicitly authorised allied access can share the service; it creates no automatic Independent alliance. Completion during a storm permits subsequent departure but does not refund damage already suffered.

The structure represents local shelter, prepared transit capacity and a usable bypass, not a faction-wide claim of immunity to every Warp phenomenon. The named installations below are **homebrew campaign implementations based on lore precedents**. No source establishes their exact 5-action cost or this game's guaranteed protection. That mechanical abstraction is explicit.

| Alignment | Proposed implementation | Lore boundary |
|---|---|---|
| Imperium | **Noctilith Transit Array:** a Mechanicus-supported installation suppresses the local disruption and maintains a narrow departure corridor. | Based on Cawl's work modulating Warp energies with blackstone. The corridor application is our campaign extrapolation, not an ordinary Geller field upgrade or a claim every Imperial fleet already has it. |
| Chaos | **Bound Passage Gate:** a ritual complex and bound guides force a prepared channel through the local storm. | Sorcerer-guided travel provides the precedent. Chaos affiliation alone grants no immunity. Khorne-aligned forces can use a daemon-engine/forged portal maintained by allied Dark Mechanicum rather than requiring their own sorcerer commander. |
| Aeldari | **Webway Anchorage:** a fleet-capable webway entrance with shelter and charted exits serving this Subsector. | Spacecraft require a sufficiently large arterial route; an infantry webway portal is not enough. This does not declare the entire damaged webway universally safe. |
| Drukhari | **Webway Breach Anchorage:** a maintained fleet-scale passage and secured staging pocket. | The same transit medium, with Drukhari engineering and control; not a personal portal magically transporting a fleet. |
| Necron | **Dolmen Transit Complex:** a maintained fleet-access gate and local noctilith shielding. | Dolmen Gates provide fleet transit access; blackstone supplies a plausible local protection mechanism. |
| Ork | **Mega-Tellyporta Array:** a Mek-built staging array flings the flotilla through a prepared passage. | Official fleet-scale mega-tellyshokka precedent exists. Reliable operation against this campaign event is the house-rule abstraction, not a claim all tellyportas are safe. |
| T'au | **Earth Caste Nexus Anchorage:** containment, survey drones and fleet staging around a recovered dimensional conduit. | Use an existing local anomaly/relic route, as T'au exploitation of the Startide Nexus demonstrates. Do not claim the T'au can mass-produce new Startide Nexuses. Discovering/reactivating this local asset is part of the paid project, not an extra random prerequisite unavailable to them. |
| Tyranid | **Narvhal Brood Anchorage:** dedicated gravitic guide organisms with a concentrated synaptic shelter maintain a compressed-space departure route. | Narvhals already supply non-Warp interstellar travel. The enhanced shelter and reliable local-storm operation are the constructed benefit; do not describe Tyranids as lacking Narvhals until they build this. |
| Independent | **Recovered Transit Anchorage:** select a mechanism appropriate to that faction's species and technology at setup; human pirates can use recovered noctilith/relic machinery. | Independent is not a species. It grants one mechanically identical installation, not access to cumulative benefits from every alignment. |

**Lore references and scope:**

- [Warhammer Community — Cawl's blackstone/liminal-abraiser research](https://www.warhammer-community.com/en-gb/articles/QIdVW6Hv/the-adeptus-mechanicus-have-their-ocular-arrays-fixed-on-the-pariah-nexus-in-the-upcoming-crusade-book/) describes intended precise manipulation of Warp energies. It supports the research direction, not proven mass-produced storm immunity.
- [Lexicanum — Warp jump](https://wh40k.lexicanum.com/wiki/Warp_jump) cites sorcerers making paths and fleet-sized webway arteries. It is a secondary reference to the listed fiction/codices.
- [Lexicanum — Dolmen Gate](https://wh40k.lexicanum.com/wiki/Dolmen_Gate) describes Necron access to the webway.
- [Warhammer Community — Ghazghkull's grand plan](https://www.warhammer-community.com/en-gb/articles/0gmcnp9x/lore-of-armageddon-part-3-ghazghkulls-grand-plan/) explicitly describes fleet-scale Ork teleportation, rather than merely squad teleporters.
- [Warhammer Community — Beyond the Startide Nexus](https://www.warhammer-community.com/en-gb/articles/6t4uXwVK/psychic-awakening-beyond-the-startide-nexus/) supplies the T'au wormhole-transit precedent; [Lexicanum's history](https://wh40k.lexicanum.com/mediawiki/index.php?mobileaction=toggle_view_mobile&title=Startide_Nexus) records its exceptional origin.
- [Lexicanum — Narvhal](https://wh40k.lexicanum.com/wiki/Narvhal), citing Codex: Tyranids 5th edition p.19, describes compressed-space travel and its gravitational limitations. [Second Battle of Shadowbrink](https://wh40k.lexicanum.com/wiki/Second_Battle_of_Shadowbrink) supplies a precedent for concentrated Tyranid psychic presence suppressing rifts. Neither makes all Tyranids invulnerable to Warp events.

This is a complete proposed roster of implementations, including the harder Imperium/T'au/Independent cases. The campaign extrapolations are identified so approval is of an honest house-rule design, not fabricated canon.

## 9. Retained rulings and package evaluation

Keep automatic random selection among eligible Planet Fall choices, including strongest-fleet ties. Preserve strongest-first allocation and the final-fallback elimination rule. Record the draw; do not request another chat's choice. Keep global Cycle timing for automatic station effects and the specified Logistics cadence for income. Preserve separate deficit tracks, their locked-resource immunity and the prohibition on voluntary depletion to zero.

Keep fixed campaign raider identity, player-reported ground outcomes, action tracking and pending-battle publication policy. Sector rules are tabled by the creator. Personnel reference work remains a separate documented task; it is not used to invent campaign timing. Mod work remains tabled.

The next candidate implementation should include the connected set: capacity/upgrade continuity, crew cost, Minor pools/fleets, resource formula and its modifiers, assault/bombardment choices, naval damage, trait changes and the generator. Preserve the old engine as the baseline. Required targeted cases include:

- Same battle across all resource bands; exact human difficulty/formation output separate from AI probabilities.
- Alternative affordable routes against the SAME defended position; short-term damage, casualties, capture timing, enemy fleet threat and Planet Fall all counted.
- Deficits from involuntary defence only; unavailable voluntary orders blocked without spending actions.
- Equal and overwhelming naval forces, upgraded fleets, Mobile Capitals, targeted structures and construction damage.
- Damaged upgrades retaining base effects, slot-safe mergers, built-in shipyard progression and automated system effects.
- All traits rotated across strategies/seats on multiple generated maps; record map size and rare prize ownership.

Only after those cases pass should matched full campaigns assess duration, resource swings, first-build choices, trait performance and whether each attack route has situations where it is useful. No human difficulty claim can be certified from an AI-only run. Approval of this proposal is not a claim it is already balanced.

**Reproduction:** proposal_checks_20260917.py and Proposal_Checks_20260917.json contain exact calculations, player setup examples and the historical expansion exposure count. The standalone proposal bundle contains these alongside this report. The old 216-campaign evidence remains historical and unchanged.
