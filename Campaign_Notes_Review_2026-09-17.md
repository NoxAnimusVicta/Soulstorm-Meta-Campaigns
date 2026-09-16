# Campaign Notes — evidence review and proposed revision
17 September 2026 • Proposal v0.2-A • **Not adopted rules**

This reviews every issue in Campaign_Notes_2026-09-15.md, including the original narrative notes. Dessica remains suspended at Cycle 21. The current Source_Rules.md is unchanged. Numerical candidates below form a connected package for comparison; none has yet passed a full-campaign variant test.

## What the shared sample establishes

216 campaigns ran for 100 Cycles on one ten-system fixture, covering 12 focal traits, six policies and three seats. All 199,376 decisions replayed correctly. This is 18 matched seed/opponent blocks, not 216 independent random replicates. Five campaigns remained contested at Cycle 100. Among the 211 that reached full control, mean duration was 61.9 Cycles, median 60 and range 42–99. All five formerly unfinished cases reached full control: 102, 108, 111, 115 and 169 Cycles. Each 200-Cycle extension reproduced its original first 100 Cycles and orders exactly, then passed public replay. Including these endings, all 216 campaigns reached full control: mean 63.26, median 61, range 42–169. This is a complete duration distribution for this fixture, not all campaign maps. That is consistent with the desired timescale in this fixture, not proof that all proposed map sizes will average 50–100.

Before the first single-Major-coalition milestone, surviving faction-Cycles had mean Supply 32.3 versus Manpower 38.7; medians were 24 and 28. Supply was at 5 or below in 3.04% of observations, Manpower in 1.14%. Reinforce occurred 21,982 times versus 5,389 Musters. These end-of-Cycle measurements miss short within-turn shortages.

The central interaction is that both stockpiles add directly to AI combat totals. Resources are not merely currencies: saving them buys combat superiority. Among 6,227 ground battles against Major defenders, 4,246 had a pre-dice advantage large enough to guarantee the attacker beat that defender's d20 total. A third-party raider can still change the overall outcome. Selection bias matters: bots deliberately choose favourable attacks. This is evidence of a strong stockpile/combat link, not a prediction that humans win 68% of battles automatically.

Construction starts were concentrated: 1,372 at the builder's original capital or Mobile Capital versus 205 at other holdings. That is 87.0% of holding-hosted starts. Economic projects were 485 of 613 recorded first constructions (79.1%). However, the controller explicitly prioritises an Academy or Forge in several situations. The result confirms behaviour under this policy, not that economic construction is globally optimal.

## B01 — Construction concentration

**Recommend testing one constructed planetary slot per holding**, including a Mobile Capital. The built-in capital shipyard is infrastructure and does not consume it. A Grand Shipyard occupies the slot; upgrading a constructed Shipyard replaces that construction in its existing slot. Other upgrades replace their parent in the same slot. An unfinished project reserves its slot; destruction frees it. Completed Consolidation Works changes the holding and frees the slot.

Do not impose a blanket one-construction-per-system limit: that would make new holdings much less useful. For system structures, propose one instance of each profile per owning faction per system, with allied copies of the same effect using the strongest effect rather than stacking. Fleet modules remain a separate question; count Mobile Capital planetary attachments consistently so a second host label cannot bypass the slot.

This directly addresses safe capital stacking while giving conquest and upgrades a reason to exist. It also constrains a mobile empire's safe income stack, so do not additionally nerf the Mobile Capital trait before testing. Existing campaign buildings should be grandfathered if this is ever migrated to Dessica; no demolition implied.

**Interaction:** Combine with crew costs, Minor resistance and repair/consolidation incentives. Slot limits alone could just make factions hoard still more resources.

## B02–B03 — Orbital contest and fleet-first versus ground-first

Healthy Minor ground resources are a bigger early barrier than orbital strength. Example: two full fleets attacking a Standard world with 20/20 resources have 10 + 18 + 18 = 46 before dice. A healthy Standard world with a six-strength defending force has 6 + 58 + 59 = 123. Halving that fleet gives 120: both are unwinnable on two opposing d20 rolls. This is a controlled arithmetic example, not a recorded campaign turn.

**Do not add automatic orbital attrition yet.** It punishes the already disadvantaged ground-first route and may force naval-first even more often. First make ground-first viable through the shared resource/combat revisions below. Fleet-first already trades a Fleet Action and initiation strength for removing defensive support and enabling bombardment; ground-first risks the garrison while threatening ownership and Planet Fall damage.

If a residual free-pass problem remains after that revision, test a capped contested-landing loss separately within the package: at most one total strength from the largest attacking ordinary fleet, never per participating fleet, with timing explicitly before commitment. Do not include this extra penalty in the initial preferred package.

Keep one action per fleet, free defensive participation, and consent/action accounting for allied fleets. Do not let a new naval engagement and a ground assault use the same attacking Fleet Action.

## B04–B05 — Economy and military Manpower

**Preferred candidate:** Expand Fleet costs 1 Supply and 1 Manpower for its existing up-to-two-strength restoration. Create Fleet keeps its existing 1 Supply/1 Manpower cost. Do not also double creation cost in the first candidate. Materials costs remain; Void Supremacy waives the Supply component only. Fleet Endurance still repairs without this action cost. Full-host construction requirements and voluntary spending above zero remain.

This makes trained crew/replacement capacity relevant without treating Manpower as civilian builders. Damaged and expanding fleets both use the action: we should describe the expenditure as rebuilding operational personnel capacity, not assume every lost point is a destroyed ship.

**Pair it with a limit on stockpile combat power:** for AI ground resolution, test Fleet Strength + min(Supply,20) + min(Manpower,20), with existing commitments paid first. Leave stored amounts, income, spending and player Soulstorm difficulty tables intact for this comparison. Test caps of 20 and 30 as sensitivity settings. This is a substantial AI-resolution change, not a neutral clarification; its mismatch with player tables needs paired player-setup review before adoption.

A cap removes the unlimited combat reward for hoarding, while materials and crew still fund sustained operations. It also reduces the enormous Minor resource wall, so the Minor-economy candidate must be assessed alongside it, not added blindly.

Keep 20/20 starts and the three-action deficit system for now. The observed duration does not justify globally cutting income or raising every price. Measure spending drawdowns and recovery, not only the size of the closing stockpile. Preserve a baseline cost variant and test the full package with and without the new crew cost to identify interactions; these comparisons are not separate adopted patches.

## B06 — Alignment, subordinates and Sector play

The terminology correction is already incorporated: Major/Minor is role; Independent is Alignment. Retain it and replace remaining ambiguous uses in the eventual edited release.

**Proposed Sector framework:** finish Subsector campaigns under a pinned version; transfer a roster record containing faction identity, alignment, commander/successor, trait and earned narrative assets. Do not directly pour a mature Subsector's entire numeric stockpile into a new 20/20 roster-building campaign. A subordinate remains an explicit relationship, not an automatic alliance between unrelated Independents.

Sector income, overlapping campaigns and reinforcements need their own scale and action budget. They cannot be validated with the present Subsector sample. Keep these as design work rather than inventing a functioning Sector economy.

## B07 — System generation and campaign duration

Use weighted, constrained generation rather than independently rolling every holding. **Draft d6 non-home system presets:**

| Roll | Holdings |
|---|---|
| 1 | One Minor |
| 2 | Two Minors |
| 3–4 | One Standard and one Minor |
| 5 | One Major and one Minor |
| 6 | One Standard and two Minors |

Give each Major a capital home system under the starting rules. For an initial ten-system test, fill the seven non-home systems from the table; at most one can instead be a declared stronghold prize. Stations substitute for equivalent tiers rather than adding free income. Split local ownership explicitly when there are multiple Minor factions.

Generate several candidate layouts and accept those with reasonably comparable expansion opportunities for each Major. Current travel allows any-system movement, so “distance from the prize” has no mechanical meaning until a travel graph exists. Do not pretend geographic symmetry was tested by the current fixture.

Compare sparse, baseline and dense layouts. Report both ending milestones and unfinished cases; the five long wars require investigation, not automatic rejection. This table is a proposed test generator, not approved setup rules.

## B08–B09 — Minor resistance and shared resources

**Preferred ordinary Minor fleet candidate:** starting strength = ceiling(half the sum of its holdings' maximum defence), distributed in fleets of up to 5. This is setup strength, not recalculated regeneration or fleet creation after losing a world. Keep the existing total +1 recovery when not engaged; destroyed fleets remain destroyed.

**Preferred shared Minor resource candidate:** derive each resource from all its surviving holdings:
R = min(40, floor(5 + 5 × sum(tier × current defence / maximum defence))).
Use R for both Supply and Manpower before temporary defensive commitments. No persistent income, purchasing, deficit track or Major resource-loss penalties. If the faction has no fallback it is eliminated, not kept alive by the base 5.

A healthy Standard plus Minor gives 20/20. Damaging or capturing either weakens the whole faction. A lone Minor gives 10/10. This matches the desired shared support concept without making each planet an isolated 40/40 fortress. The exact 5 and 40 are candidate parameters, not measured optima.

A prize faction should be explicitly marked: one Capital-tier holding, normal unhalved starting fleet calculation, and candidate shared resource cap 60 rather than 40. It remains a static Minor, with no automatic Major trait, capital-establishment turn or spendable economy. Its tier and cap must be supported in the engine before running those cases; the present baseline does not support Minor Capital holdings.

**Interaction:** Easier Minors accelerate income acquisition and may shorten games; construction dispersal and crew demand must be tested alongside that acceleration. Test half-fleet alone as a diagnostic to show whether the ground wall remains, not as the proposed finished fix.

## B10 — Naval randomness and AI ground resolution

4,934 recorded naval battles included 1,350 margins of at least 16 (27.4%). That is the current automatic-destruction tier. It combines force disparity and dice, so it is not a pure measure of “bad luck.”

Exact enumeration of an unmodified 5-versus-5 engagement after the initiator pays one strength gives:
- d20 each: 42.75% attacker win, 4.75% tie, 52.50% defender win; 5.25% chance either side reaches a destruction-tier margin.
- 2d10 each: 40.05% attacker win, 6.60% tie, 53.35% defender win; 0.40% extreme-margin chance.

**Preferred naval candidate:** roll 2d10 each; retain initiation and ordinary margin bands, but replace the 16+ automatic wipe with 4 damage per participating losing fleet. Destruction still occurs at zero. Stronger forces become more reliable, so this needs an overconcentration check; it is not a free improvement.

Keep ground dice at d20 in the initial preferred package while testing the capped resource contribution. Reducing ground variance simultaneously would make entrenched statistical advantages even harder to overcome. Player ground battles still use reported Soulstorm outcomes.

## B11 — Construction alternatives, upgrades and incentives

A Supply Depot costs 15 Supply and repays that in eight Logistics payments; a Forge costs 25 and repays in five. Both require their build time first. The Major is deliberately more efficient long-term, but safe capitals and large stockpiles erase much of the Minor's early-access advantage.

**Preferred package:** slot limits; an upgrade retains the completed base effect until it takes damage below base Integrity, then gains its upgraded effect only when complete at full upgraded Integrity. This avoids switching off the entire existing economy during five more actions. Record base completion separately from upgraded completion. Any damage-source destruction at zero and the full-host rule remain.

**Troop Transport fix candidate:** instead of percentage steps that often round to no benefit, on a successful assault return one additional committed Manpower with a base transport, two with upgraded, capped at the commitment; use only the best participating transport. Current 60/70/80% rounding returns identical amounts at commitments one and two, making its advertised benefit disappear in common small battles. Test the fixed return alongside crew demand; otherwise it could erase too much attrition.

Keep tactical construction prices initially. Sixteen of the 32 profiles were started in this sample; absence of the other sixteen is not proof they are bad. The controller's construction priority favours specific projects and safe hosts. We need targeted opportunities for shield-breaking, scouting, regeneration, consolidation, fleet capacity, salvage and forward yards before price changes to those profiles.

Consolidation already trades Supply/actions for defence and income; retain the cost pending the slot test. Do not make it secretly grant another construction slot unless we deliberately choose tier-scaled slots.

## B12 — All twelve traits

Treat observed trait outcomes as warning signals, not rankings. Martial Culture survived to the observation cutoff in 15/18 focal runs, Mobile Capital 7/18, Efficient Logistics 6/18 and Siege Doctrine 5/18. Survival is not necessarily sole victory; opponent composition and bot policy matter, and 18 matched cases cannot settle fine differences.

| Trait | Proposed treatment |
|---|---|
| Mobile Capital | Retain identity, strength and upkeep exception; apply the same planetary slot constraint. Measure repairs, attached damage and capital-loss exposure. |
| War Economy | Retain +3 Supply/Logistics; retest after capped combat contributions. |
| Martial Culture | Retain +5 Manpower/Logistics initially. Its strong AI result may reflect unlimited Manpower-to-combat conversion; do not nerf income first. |
| Efficient Logistics | Retain +4 Reinforce/Muster; compare action savings under crew demand. |
| Salvagers | Retain rewards; count useful gains versus gains lost to caps/deficit locks. |
| Void Supremacy | Retain free Supply expansion; proposed crew cost still applies. Check that it remains distinctive. |
| Swift Mobilization | Retain creation at 3; preserve strongest-benefit rather than additive yard stacking. |
| Fleet Endurance | Retain +1/Logistics; proposed crew cost makes this more valuable. |
| Siege Doctrine | Retain defeat damage. Candidate clarification/buff: ignore the AI +15 from the Defend action as well as the player difficulty modifier. Do not ignore separate shields/bunkers automatically. |
| Dread Reputation | Replace the largely rounding-limited successful-defence refund effect with a candidate -5 to the opposing AI ground total, and +1 difficulty when the player defends against it. Player attacks using Dread reduce their difficulty by 1. Test this mapping; it is a redesign, not a typo fix. |
| Fortification Experts | Retain +2 restoration; candidate addition: Defend costs 1 less Supply, minimum 1. Full Manpower price remains. Test durability loops. |
| Industrial Efficiency | Retain Build cost 4; slot/upgrading changes may improve value without a direct buff. |

Do not award all traits compensating buffs before observing the connected package. The three proposed weak-trait changes should be compared with a package retaining current traits. Player-specific Siege/Dread conclusions require actual setup examples, not AI-only win statistics.

## B13 — Bombardment

The bots recorded 11,675 ordinary ground orders versus 4,116 bombardments. They do not universally choose bombardment, but those counts do not compare equivalent opportunities.

**Keep doubled Supply and the one-defence floor in the first package.** Once early ground attacks are viable, bombardment retains its intended trade: certain damage and no Manpower against high material cost, delay and no capture. A fleet must still have uncontested conditions.

If matched target tests still show domination, use a candidate +1 Supply per bombardment, not double the already doubled price. Do not simultaneously weaken Minors, add landing losses and heavily tax bombardment: that would make it impossible to identify which route remains attractive.

## B14 — Planet Fall allocation

Keep point-by-point allocation to the currently strongest eligible fleet, recalculating after every point. The attacking Major chooses ties against another Major; the referee chooses against a Minor. Log the choice. This preserves the inherited player agency rule.

For automated Major tie choices, use a declared deterministic policy with a stable fleet-ID fallback. Do not randomise hidden decisions to save a message; randomness changes survival of attached constructions. A random tie-break may be an explicit campaign option, not the default.

## B15 — Third-party raider identity

Already adopted: select and record the raider once at setup; keep Iron Warriors for Dessica. Correct the old event-table wording that still says a random faction is chosen each occurrence. Raiders never capture holdings, never replace a defender, and withdraw after battle.

The AI +45 raid profile is provisional. With capped normal combat totals its relative strength increases. Test profiles 35/45/55 alongside the package; no evidence currently justifies making the raider stronger.

## B16 — Events and travel

Each named event currently has probability 1/18 per Cycle: about 5.56 occurrences per 100 Cycles in expectation. A five-Cycle span has a 24.86% chance of at least one Warp Storm. This is not a prediction of losing the entire build; repair timing and Integrity determine that.

Keep the existing event frequency and one shared roll. Preserve construction damage, track-specific resource locks and one-time degradation. Crisis and Fervor do not cancel neatly: caps and deficit locks make their effects asymmetric.

**Do not add routine multi-Cycle travel to the initial package.** The baseline already reaches the desired duration range in this layout. An optional later transit variant should have one declared arrival delay, no stacking indefinite delays, and explicit defence/retreat rules. Do not count a moving fleet twice or let it support either endpoint while in transit. Test travel separately on the same package and maps, not as an uncosted narrative detail.

## B17 — Alignment constructions and Warp resilience

Give all alignments equivalent mechanical access with different lore. Chaos bindings, Necron inertial/blackstone systems and Imperial Geller/navigation measures can share one profile; naming does not grant hidden advantages.

**Prototype:** Minor fleet-attached “Storm Protection”, 3 Build stages, 3 Integrity. While completed and full, prevent the first one point of Warp Storm strength/defence damage to its host, including the resulting inherited host-damage hit to attachments. It does not prevent the movement ban, combat damage or deficit degradation. It occupies the usual attachment slot if one exists; no faction-wide immunity. Protecting itself is intentional and must be tested against Mobile Capital construction safety. No upgraded version until its base value is measured.

This is optional in the first full package comparison: storm-proof mobile economic hubs may undo the risk that constrains Mobile Capital. Measure that interaction explicitly.

## B18 — Personnel, time and succession

Preserve succession retaining the faction trait and explicit treatment/lifespan records. The missing rule is the clock, not a forced random death chart.

**Proposed setup choice:** record years per Cycle and any time-jump separately. Use 0.5 years/Cycle as a test-campaign narrative default only if desired; it is not a lore fact. A 50–100 Cycle campaign then spans 25–50 years. If a human begins at 40 with an agreed untreated retirement/death window of 70–90, succession becomes a plausible campaign event. Those ages are example design assumptions, not canonical species limits.

For long-lived or uncertain cases, use an agreed review date/range, not a fabricated universal maximum. Do not force a Necron or Astartes death merely because a counter expired. Log local age and Sector elapsed time separately; never add concurrent Subsector durations together automatically. This affects narrative continuity rather than numerical resource balance unless later rules explicitly connect them.

## B19 — Simulation quality and remaining investigations

The baseline is useful, but it is not an oracle. Exact replay establishes implementation reproducibility; it does not establish optimal strategy. Construction priorities visibly influence selections. Rare actions and absent designs need scenarios that give them a reason to exist.

All five formerly unfinished cases reached full control: 102, 108, 111, 115 and 169 Cycles. Each 200-Cycle extension reproduced its original first 100 Cycles and orders exactly, then passed public replay. Including these endings, all 216 campaigns reached full control: mean 63.26, median 61, range 42–169. This is a complete duration distribution for this fixture, not all campaign maps. The original last-20-Cycle logs contain active attacks, expansion and movement in every case; long duration alone is not evidence of an idle loop.

For package comparisons, retain matched initial states and event streams, vary opponent mixes, add independent seed blocks and sparse/dense maps. Keep all twelve traits. Campaign durations, deficits, stockpile drawdowns, meaningful construction use, losses and attack-route choices should be reported together. A nominal 50–100 mean is not sufficient if most turns are forced recovery or harmless shuffling.

Use at least the original 216 cells for a full package comparison. Before spending that compute, run targeted rule tests and a small pilot that catches invalid orders and policy assumptions. Those tests must not replace the full sample.

## B20 — Mod subproject

Recommended first prototype: one infantry unit built from an existing compatible skeleton, mesh parts and animation set, with a proper recolourable material and Army Painter preview. Validate idle, move, fire, melee, death, selection, attachments and team colours before attempting a whole faction.

The tool author's Dawn of War import/export FAQ confirms that action copying requires matching skeletons and documents texture paths, .whe editing and the Army Painter camera. Therefore “it came from another DoW expansion” is not enough to guarantee a working kitbash. A model from another 40k game is an even larger compatibility project. See [the tool author's FAQ](https://www.moddb.com/games/dawn-of-war-soulstorm/tutorials/faq6).

Pin the actual game/mod version and preserve asset provenance/author permissions; the [Unification team's project page](https://www.moddb.com/mods/unification-mod-dawn-of-war-soulstorm/) is the starting point for its own releases, not a blanket asset-reuse grant. No installed game assets were inspected or changed in this review, so compatibility is not yet verified.

## B21 — Automatic defensive commitment timing

Recommended correctness fix: keep a temporary post-commitment combat view, then settle the actual final resource loss once after the outcome. A capture's Planet Fall penalty replaces ordinary defeated-defender Supply expenditure; it must not trigger an irreversible deficit from a payment later refunded/replaced.

This applies to automatic defence, not the voluntary Defend action. Voluntary actions still cannot spend a resource to zero. Mandatory final losses can trigger deficits. Tests must cover successful defence, failed defence without capture, capture, raider outcomes and simultaneous tracks. Baseline evidence deliberately preserves the current immediate-entry behaviour, as requested.

## B22 — System station timing

Keep damage-before-repair as the preferred explicit sequence. Determine active station effects at the phase start, apply damage, destroy zero-strength fleets and their attachments, then repair eligible survivors. A fleet destroyed at zero cannot be resurrected by a Repair Station. Effects cover every eligible fleet in-system, as ruled.

Test start-of-phase snapshots against sequential station evaluation to remove owner/array-order advantages. Multiple effects and mobile-capital destruction need explicit ordering. Do not rebalance station cost until the same ordering is used in both the rules and simulator.

## Source documents, briefings and GM workflow

The blank campaign, commander/advisor briefings, takeover handover, GM guide and source library already exist. Preserve source-version pinning and briefing provenance. After approval, publish a new source version and an upgrade note; do not silently rewrite the suspended campaign to fit it.

Keep narrative free of resource numbers, followed by mechanical action tables. Advisors recommend, commanders declare, and the referee resolves. Keep the rule against publishing an unresolved player battle as completed. Retain faction palette and personnel records.

A prospective wording cleanup should reconcile: default fleet maximum 5 versus construction upgrades; each fleet's action versus “one battle per turn”; Mobile Capital's prevention of uncontested bombardment versus its old bombardment paragraph; fixed raider identity versus “random”; and obsolete construction-capture labels versus surviving-Integrity rules. These are identified for the approved revision, not silently changed here.

## Connected package and decision order

**Preferred v0.2-A for testing:** one planetary slot; base benefits retained during upgrades; crew-cost expansion; capped AI stockpile contributions; half-strength ordinary Minor fleets with faction-derived resources; 2d10 naval rolls and finite extreme damage; fixed extra transport recovery; final-net defensive settlement; explicit station ordering. Keep existing income, bombardment price, events, travel and current traits for the first package run.

**Companion v0.2-B:** the same package plus the three proposed Siege/Dread/Fortification changes. Storm Protection is a separate optional package extension, not an assumed free benefit.

The cap, Minor support formula and naval rule are the largest uncertainties. Diagnostic component combinations must measure whether each improves or worsens the full package. Compare cap20 versus cap30 and unchanged cap, existing versus half Minor fleets, and current versus proposed naval resolution in a small screening design before committing the full sample. Report this as interaction testing, never as proof that one isolated tweak solved the campaign.

These proposals are ready for discussion. They are not a claim that the system has been balanced or that new variants have already been run.
