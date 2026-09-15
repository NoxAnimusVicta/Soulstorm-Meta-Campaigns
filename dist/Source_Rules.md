# Soulstorm Meta Campaigns — Source Rules

Version 0.1 • 2026-09-15 • Provisional development baseline, not a balanced release.

Extracted from resolved Dessica rules through Cycle 21. Named rosters, holdings and history are not starting state. Numerical rules remain for review, not as evidence of balance. Campaign_Notes_2026-09-15.md distinguishes proposals from decisions. Do not silently adopt alternatives.

## Source-level directions

- New Subsector roster-building campaigns start each Major Faction at **20 Supply /20 Manpower**. Sector-directed campaigns may specify another recorded start. This does not reset Dessica.
- Establish one fixed Third Party Raid faction at Subsector setup; it cannot capture territory.
- Major/Minor are campaign roles; Independent is an Alignment and grants no automatic alliance among its members.
- Pin campaigns to a source version. Dated, approved changes replace rules prospectively; do not silently migrate an existing campaign.
- One or more Subsector campaigns generate a future Sector roster. Sector timing, subordinate factions and transfer of territory need further design; this is not a complete Sector ruleset.

## Personnel and succession

Track commanders and supporting staff: species, known age/range, elapsed local time, life-extension treatment and successors. Major Factions choose narrative deaths and successors; the referee manages Minor personnel. Establish plausible lifespan assumptions before play; unknown age is not permission to invent a death. Use agreed local and Sector clocks, including Chronostrife. Succession retains the selected faction trait; explicit mechanical trait-loss rules still apply. Species lifespan numbers remain to be agreed.

## Known conflicts requiring review

- Planet Fall's old example conflicts with strongest-fleet point-by-point wording. Use the explicit point-by-point rule; referee chooses Minor ties. Major choice ownership/randomisation alternatives remain open.
- Dread Reputation references 80% returns while other return rules differ. Resolve scope before selecting it.
- Faction scaling mentions proportional reduction and equal subtraction; newer raid map rules preserve all participants. Resolve unsupported map capacities before battle.
- One-battle-per-turn wording conflicts with separate Fleet Actions permitting attacks. Preserve per-asset limits; clarify edge cases before resolution.

## SECTION 1: CAMPAIGN SETUP

### Fleet Strength Clarification

**Fleet Strength represents combat effectiveness — NOT vessel count.** A single point of Fleet Strength encompasses crew readiness, ammunition stores, morale, hull integrity, fuel reserves, and operational capacity. A fleet cannot be reduced to a single vessel; when Fleet Strength drops to 1/5, the fleet is combat-ineffective but still exists as a formation. At 0, the fleet is destroyed as a coherent fighting force.

This distinction matters for:
- **Damage calculations:** Fleet Strength lost represents degraded combat capability, not ships exploding
- **Regeneration:** Recovering Fleet Strength represents repairs, resupply, crew rotation, and morale recovery
- **Constructions:** Fleet-attached constructions represent specialized capacity, not individual ships

### Faction Alignments

Factions sharing a non-Independent Alignment use the inherited alliance rules; different Alignments are hostile unless an applicable diplomatic agreement says otherwise. Independent is an Alignment, not a faction size: two Independent-aligned factions are not automatically allied. They need an explicit pact or recorded subordinate relationship. Major/Minor describes campaign role separately from Alignment.

| Faction | Alignment | Per Manpower | Ratio to Marine | vs Guard | Force Description |
|---------|-----------|--------------|-----------------|----------|-------------------|
| Space Marines | Imperium | 40 | 1:1 | 1:15 | Battle-brothers only. Chapter Serfs, Servitors, and non-combat personnel not tracked. Vehicle crews included. |
| Chaos Space Marines | Chaos | 40 | 1:1 | 1:15 | Traitor Astartes only. Cultists, mutants, and daemonic auxiliaries supplement forces but not explicitly tracked. |
| Grey Knights | Imperium | 40 | 1:1 | 1:15 | Battle-brothers only. Inquisitorial retinues and support staff not tracked. |
| Sisters of Battle | Imperium | 100 | 1:2.5 | 1:6 | Battle Sisters and vehicle crews. Ecclesiarchy support, Arco-flagellants, Penitent Engines as auxiliary not tracked. |
| Imperial Guard | Imperium | 600 | 1:15 | Baseline | Frontline infantry, officers, heavy weapons teams, tank crews. Logistics and rear echelon not tracked. |
| Traitor Guard | Chaos | 600 | 1:15 | Baseline | As Imperial Guard. Mutants and Chaos-touched may supplement but not tracked. |
| Craftworld Eldar | Aeldari | 100 | 1:2.5 | 1:6 | Mix of Aspect Warriors and Guardian militia. Seers, vehicle crews included. Wraithbone constructs as heavy support not explicitly tracked. |
| Harlequins | Aeldari | 15 | 2.67:1 | 1:40 | Players only. Troupes, Shadowseers, Death Jesters, Solitaires. No auxiliaries - they operate alone. |
| Drukhari | Drukhari | 160 | 1:4 | 1:3.75 | Kabalite Warriors, Wyches, vehicle crews. Haemonculus creations and slaves may supplement raids but not tracked. |
| Necrons | Necron | 160 | 1:4 | 1:3.75 | Warriors, Immortals, command elements. Canoptek constructs (Scarabs, Wraiths, Spyders) as auxiliary not explicitly tracked. |
| Tau | T'au | 320 | 1:8 | 1:1.9 | Fire Caste Warriors, Pathfinders, Battlesuit pilots, vehicle crews. Kroot and Vespid auxiliaries handled as separate formations. |
| Orks | Ork | 400 | 1:10 | 1:1.5 | Boyz, Nobz, specialist mobs, vehicle crews. Gretchin serve as support. Squigs not tracked. |
| Tyranids | Tyranid | 800 | 1:20 | 1:1.3 | Weighted average: primarily Gaunts with Warriors and Genestealers as synapse/elite. Larger bioforms (Carnifexes, etc.) as heavy support. |
| Chaos Daemons | Chaos | 100 | 1:2.5 | 1:6 | Full daemonic incursion: lesser daemons as line troops (Bloodletters, Daemonettes, Plaguebearers, Horrors). Greater Daemons and Daemon Princes as command elements. |
| Adeptus Mechanicus | Imperium | 240 | 1:6 | 1:2.5 | Skitarii Rangers/Vanguard, Tech-Priests, Servitors. Battle Automata and heavier war machines as support not explicitly tracked. |
| Independent (Rogue Traders, Pirates, minor xenos, unaligned forces) | Independent | Varies | Varies | Varies | Independents are all-encompassing. Manpower ratios depend on the specific force composition — use the ratio of whichever faction type best represents the force being fought. |

---

### Faction Traits

When selecting a trait for your faction, rename it to something evocative that alludes to the effect without being a direct description. The name should sound like a doctrine, characteristic, or battle cry befitting your faction.

| Placeholder | Effect |
|-------------|--------|
| [Mobile Capital] | May use a Mobile Capital instead of a Planet-based Capital. See Mobile Capital Rules. **No starting fleet.** |
| [War Economy] | +3 Supply per Logistics Cycle |
| [Martial Culture] | +5 Manpower per Logistics Cycle |
| [Efficient Logistics] | Reinforce and Muster grant +4 instead of +3 |
| [Salvagers] | +1 Supply per battle (planetary assault or Fleet Battle, as attacker or defender). +2 Supply when you capture a planet. |
| [Void Supremacy] | Expand Fleet costs no Supply |
| [Swift Mobilization] | Create Fleet starts at 3/5 instead of 1/5 |
| [Fleet Endurance] | Your fleets regenerate +1 strength per Logistics Cycle if below maximum. |
| [Siege Doctrine] | Ignore Defended status difficulty modifier when attacking. Your attacks deal 1 damage even on defeat. |
| [Dread Reputation] | Enemies return only 60% resources on successful defence against you (instead of 80%) |
| [Fortification Experts] | Defend restores +2 additional defence |
| [Industrial Efficiency] | Construction costs 4 Supply instead of 5 |

### Capital Infrastructure

All established Capitals include a built-in Orbital Shipyard. This Shipyard is destroyed if the Capital falls and does not transfer to the new controller.

When establishing a new Capital via the Establish New Capital forced action, the built-in Orbital Shipyard is gained only after the Capital reaches maximum defense of 12 and is fully established.

### Mobile Capital Rules

A faction with the [Mobile Capital] trait uses a mobile fortress — a Craftworld, World-Engine, Hive Ship, Ark Mechanicus, or equivalent — as their Capital instead of a planet.

**Core Properties:**
- 12/12 defence (Capital-class)
- Generates +4 Supply / +4 Manpower per Logistics Cycle, as any Capital
- Built-in Orbital Shipyard, as any Capital
- Constructions may be built on it following normal Planetary/Orbital construction rules
- **No starting fleet** — the faction must build its first fleet from the Capital's Shipyard

**Movement:** The Mobile Capital may move to any system within the Subsector. This consumes a Fleet Action for the turn. The Mobile Capital is not a fleet and does not pay fleet maintenance during Logistics Cycles.

**Fleet Battle:** The Mobile Capital may participate in Fleet Battles, using its **current defence value** as its Fleet Strength for the roll. Initiating a Fleet Battle costs -1 defence (mirroring the -1 Fleet Strength initiation cost). Fleet Battle damage is applied to the Mobile Capital's defence value. The Mobile Capital contributes its current defence value toward Void Superiority calculations.

**Ground Assault:** The Mobile Capital may launch Ground Assaults, using its current defence value as Fleet Strength for damage calculation. It may be attacked by enemies via Ground Assault, as a planet.

**Uncontested Bombardment:** A Mobile Capital cannot be reduced below 1 defence by Uncontested Bombardment, as any planet.

**Destruction:** If the Mobile Capital's defence reaches 0, it is **destroyed** — it does not transfer to the attacker. The owning faction suffers Capital-tier Planet Fall penalties (-4 Supply, -4 Manpower) and must designate a new Capital on an owned planet, entering the Establish New Capital forced action. **The [Mobile Capital] trait is permanently lost** — the faction operates without a Faction Trait for the remainder of the campaign.

**Elimination:** A faction whose Mobile Capital is destroyed while holding no planets is eliminated from the campaign.


---

## SECTION 2: TURN STRUCTURE

**Resource Requirements:** A faction cannot voluntarily take any action that would reduce their Supply or Manpower below 0. If an action requires more resources than the faction possesses, that action cannot be taken. Reaching exactly 0 through an affordable voluntary action also triggers a deficit. Involuntary losses can trigger a deficit at 0 or below; record the affected resource as 0 and apply the recovery rules.

Each turn represents one battle. Follow these phases in order:

### Phase 0: Logistics (Every 3rd Cycle Only)

On Logistics Cycles (Cycles 3, 6, 9, 12, etc.), before any faction acts:

**Income (Variable by World Type):**
| World Type | Supply | Manpower |
|------------|--------|----------|
| Minor | +1 | +1 |
| Standard | +2 | +2 |
| Major | +3 | +3 |
| Capital | +4 | +4 |

- All factions gain resources based on planets controlled (sum of world types)
- All factions pay -1 Supply and -1 Manpower per Fleet owned (maintenance)
- If Supply maintenance cannot be paid, Supply Deficit occurs (see Resource Deficits)
- If Manpower maintenance cannot be paid, Manpower Deficit occurs (see Resource Deficits)

### Phase 1: Event Roll (Optional — Once Per Cycle)

Rolled ONCE per Cycle, before any faction takes its turn. On Logistics Cycles, this follows immediately after Phase 0.

Roll 1d6. On a 1 or 6, roll on the Event Table (Section 4). Otherwise, no event this Cycle.

**Duration:** A triggered event applies for the whole of the Cycle in which it is rolled. It affects every faction's turn in that Cycle, in turn order, and expires at the start of the following Cycle — immediately before Major Faction 1 begins its turn. Events do not carry over. There is one Event Roll per Cycle, not one per faction.

### Phase 2: Fleet Actions

Each fleet may take **ONE Fleet Action per Cycle**, including actions taken during an allied faction's turn. Different fleets can take different actions. A fleet that takes a Fleet Action cannot take another Fleet Action this turn.

#### Fleet Movement

Move this fleet to any system within the Subsector.

#### Fleet Transfer

Transfer strength points between this fleet and another fleet in the same system. No fleet can drop below 1/5 or exceed 5/5. Requires Void Superiority.

#### Fleet Merge

Merge this fleet with another fleet in the same system. Combined strength caps at 5/5 (excess is lost). The absorbed fleet ceases to exist.

#### Scuttle Fleet

Decommission this fleet and recover half its Fleet Strength as Supply (rounded down). Requires Void Superiority.

#### Attack

Assault an enemy or neutral planet. Costs Supply based on world type (Minor -1, Standard -2, Major -3, Capital -4). Commit Manpower equal to base damage dealt. Damage dealt = 1 per 5 participating friendly Fleet Strength (minimum 1 if uncontested). **Uncontested Bombardment:** When no hostile fleets are present in-system, the attack automatically succeeds — no battle is fought. The attacker pays double Supply costs (Minor -2, Standard -4, Major -6, Capital -8) and commits no Manpower. Damage is applied directly. A planet cannot be reduced below 1 defence by Uncontested Bombardment — the final point of defence must be broken by a Ground Assault. **Ground Assault:** A full planetary assault engaging the planet's garrison directly. This can be launched whether or not hostile fleets are present in-system — you do not need to clear enemy fleets first. If hostile fleets ARE present, they contribute to the defender's strength in the battle. Difficulty and AI rolls are calculated after costs are paid and Manpower is committed.

**Attack Participation:** All friendly fleets in-system that wish to contribute their strength to an Attack must use their Fleet Action for that battle. Fleets that do not participate keep their Fleet Action for other purposes but do not add their strength to the damage calculation. Multiple fleets combining for a single Attack pool their Fleet Strength for calculating damage dealt.

**Multi-Front Warfare:** A faction with multiple fleets can launch multiple Attacks in the same turn — each fleet can attack independently. This represents the strategic advantage of maintaining multiple operational formations.

#### Structure Assault

Target one enemy construction, including a system-based construction. Each participating fleet spends its one Fleet Action; moving, striking and leaving require separate actions unless an existing ability explicitly permits a combination.

**Defending fleets present:** Resolve as a Fleet Battle. The attacker pays the single initiation cost of **1 Fleet Strength** (or 1 defence from an initiating Mobile Capital). Use participating attacker strength after that cost and defending fleet strength. On an attacker win, damage **only the targeted construction**: margin 1–5 =1 Integrity, 6–10 =2, 11–15 =3, 16+ =target destroyed outright. Defending fleets take no damage from a successful targeted strike. On attacker defeat, participating attacker fleets suffer normal Fleet Battle losses; the targeted construction takes none. Normal Fleet Battle tie rules apply. This is not a Ground Assault.

**No defending fleet:** Pay **2 Supply**, commit **0 Manpower**, and automatically deal **floor(participating Fleet Strength /5), minimum 1**, to the targeted construction’s Integrity. No initiation strength cost or dice roll. There is **no minimum-Integrity floor**: the attack can destroy the construction. This targeted bombardment damages only the construction, not the host or neighbouring structures. Relevant construction bonuses apply only where their stated effect covers this attack.

Both unfinished and completed constructions use the same Integrity damage rules. A targeted strike cannot capture a construction. Completed Void Stations are holdings and use Void Station Assault instead; constructions aboard them may be targeted normally.

#### Expand Fleet

+2 Fleet Strength to this Fleet (max 5). Costs -1 Supply. This fleet must be at a location with an Orbital Shipyard or established Capital to take this action.


#### Fleet Battles

Initiating faction (aggressor) pays -1 Fleet Strength to initiate. Both Factions roll a d20 plus their in-system Fleet Strength (calculated after the -1 initiation cost is paid). Highest roll wins. 1-5 higher = Loser -1 Fleet Strength per Fleet in Battle. 6-10 higher = Loser -2 Fleet Strength per Fleet in Battle. 11-15 higher = Loser -3 Fleet Strength per Fleet in Battle. 16-20+ higher = Loser Fleet(s) destroyed. Multiple fleets in a system combine their strength for the roll. **All calculations use values after initiation costs are paid.**

**Fleet Battle Participation:** All friendly fleets in-system that wish to contribute their strength to a Fleet Battle must use their Fleet Action for that battle. Fleets that do not participate keep their Fleet Action for other purposes but do not add their strength to the roll. Only one Fleet Battle may occur per system per turn, regardless of how many fleets participate.

#### Void Superiority

**Void Superiority:** Your total fleet strength in-system exceeds total enemy fleet strength.

### Phase 3: Faction Action

A faction may take ONE Faction Action per turn. This represents the faction's central command capacity.

#### Defend

Fortify a Planet or repair a Construction you control. **Planet:** Costs Supply and Manpower based on world type (Minor -1/-1, Standard -2/-2, Major -3/-3, Capital -4/-4). Restore defence based on planet type: Minor +1, Standard +2, Major +3, Capital +4 (up to planet's maximum). The defended planet gains Defended status until your next turn: attackers face +1 difficulty, you face -1 difficulty when defending. AI vs AI: Defender roll +15. **Construction:** The existing Faction Action repair option remains: Minor costs 1 Supply and 1 Manpower to restore 1 Integrity; Major costs 3 Supply and 3 Manpower to restore up to 3 Integrity, capped at maximum. Upgraded structures use their underlying Minor/Major class. Only completed structures may be repaired; the host must be at full defence/Fleet Strength. This repairs Integrity, does not advance an unfinished build or upgrade, and does not grant a structure Defended status. Planet, station and Mobile Capital Defend actions remain unchanged.

#### Reinforce

+3 Supply (max 100). Unavailable while a deficit requires the compulsory Emergency Rationing Faction Action.

#### Muster

+3 Manpower (max 100). Unavailable while a deficit requires the compulsory Emergency Rationing Faction Action.

#### Create Fleet

Create a new fleet at Fleet Strength 1/5. New fleets are created at the faction's Capital location or at any Shipyard. Costs -1 Supply and -1 Manpower.

#### Garrison Transfer

Transfer defense points between planets in the same system. Donor planets must be at full defense. Recipients cannot exceed maximum defense. When you take this action, you may perform multiple transfers from different donors.

#### Summon Allies

Call a new allied Major Faction into the subsector by granting them an entire system. **Costs -10 Supply and -10 Manpower.** The newly summoned faction starts with 10 Supply and 10 Manpower (inherited mid-campaign Summon Allies exception to the 20/20 opening start) but no fleet — they rely on their summoner for protection. **Requirements:** (1) You must control planets in more than one system. (2) You must control ALL planets in the system being granted. (3) You must have Void Superiority in that system. (4) The new faction must share your alignment and make sense within established 40K lore. **Effect:** Immediately cede all planets in that system to the new faction. The new faction is aligned with you — they will not attack your holdings and will coordinate against mutual enemies. Design the new faction (name, background, trait) when summoned. The new faction activates immediately after your turn in the turn order.


**Important:** You cannot grant away your only fully controlled system. You must fully control at least two systems to use Summon Allies — one to keep and one to grant.

**Summon Allies — Alignment Restrictions:**

The summoned faction must belong to the same broad alignment as the summoning faction. This represents calling in reinforcements, granting territory to allies, or allowing subordinate powers to establish their own domains. The new faction must have a plausible lore reason for arriving in the subsector.

| Alignment | Eligible Faction Types | Examples |
|-----------|----------------------|----------|
| Imperium | Astra Militarum, Adeptus Mechanicus, Other Space Marine Chapters, Adepta Sororitas, Rogue Traders, Imperial Navy, Inquisitorial Forces | A cut-off Guard regiment, an Explorator fleet, a Magos establishing a Forge World, a brother Chapter answering a distress call |
| Chaos | Other Chaos Warbands, Daemon Cults, Dark Mechanicum, Traitor Guard, Other Traitor Legions | A warband sworn to a different god, a cult that rises in the new territory, a splinter fleet of the same Legion |
| Drukhari | Other Kabals, Wych Cults, Haemonculus Covens | A rival Archon granted hunting grounds, a Coven providing support in exchange for specimens, a Wych Cult seeking new arenas |
| Craftworld Aeldari | Other Craftworlds, Corsairs, Harlequins, Ynnari | A Corsair fleet, rangers from another Craftworld, a Harlequin masque |
| Orks | Other Warbosses, Freebooterz | Another Waaagh! drawn by the fighting, Freebooterz smelling loot |
| Necrons | Other Dynasties, Destroyer Cults | An awakening Tomb World, a vassal Dynasty, a Destroyer Lord claiming territory |
| Tyranids | Other Hive Fleets, Genestealer Cults | A splinter fleet, a cult uprising on the granted world |
| T'au | Other Septs, Auxiliaries | An expansion fleet, Kroot kindreds, Vespid contingents |

**Independent summoners:** Record an explicit subordinate pact when an Independent-aligned faction summons an ally. Shared Independent Alignment alone never allies unrelated factions. Sector-level grant and roster consequences remain undefined.

**Multiple Factions:** You may have multiple factions of the same type in play (e.g., two Space Marine Chapters, three Drukhari Archons). Each operates independently but remains aligned with their summoner.

### Phase 4: Social Action

A faction may take ONE Social Action per turn. This represents diplomatic bandwidth.

| Action | Effect |
|--------|--------|
| **Communiqué** | Send one message to another Faction. They may respond immediately but only once. Requires both Factions to have a presence in the same system (fleet or planet — any combination). Extended conversations require multiple cycles. |

#### Diplomacy with Non-Aligned Factions

**Diplomacy with Non-Aligned Factions:** Temporary cease-fires or non-aggression pacts with factions outside your alignment are possible through the Communiqué action, but these are inherently unstable. Conflicting alignments will inevitably come to blows — such arrangements should be treated as temporary strategic convenience, not true alliance.

### Phase 5: Construction Action

A faction may take ONE Construction Action per turn. This represents the faction's engineering and industrial capacity.

| Action | Effect |
|--------|--------|
| **Build** | Spend 5 Supply to begin or advance one construction or upgrade by 1 stage, adding 1 Integrity. Minor base builds require 3 stages; Major base builds require 5. Host must be at full defence or Fleet Strength for every Build action. Lost unfinished stages are regained through paid Build actions. See Construction Integrity below. |
| **Repair** | Spend the Construction Action to restore up to 3 Integrity to one completed structure, paying 1 Supply per point actually restored, no Manpower cost. Cap at its maximum. Host must be at full defence/Fleet Strength. Does not advance an unfinished construction or upgrade; those require Build. |

**Construction Integrity — inherited baseline:**
- Integrity is separate from planetary defence and Fleet Strength. Maximums: **Minor 3, Major 5, upgraded Minor 6, upgraded Major 10**. A new project starts at 1 Integrity after its first paid Build action. Track current/maximum Integrity and whether construction or upgrade has been completed.
- Each point of damage suffered by a planet, station, fleet or Mobile Capital also removes **1 Integrity from every construction attached to that host**, independently. It is not divided between projects or absorbed instead of host damage. Apply actual host damage after applicable reductions, once per damage instance. A targeted Structure Assault damages only its named target instead.
- Applies to unfinished and completed structures, including hostile Fleet Battles, Ground Assaults and environmental damage. A Warp Storm that damages a fleet or Mobile Capital by 1 also removes 1 Integrity from every attached construction. Ordinary Supply costs, Manpower costs and voluntarily paid initiation strength costs are not damage.
- At **0 Integrity, any construction is destroyed**, Minor or Major, finished or unfinished, regardless of damage source. Rebuilding starts a new paid project. There are no disabled zero-Integrity foundations.
- A construction provides **no effects unless completed and at full Integrity**. Damaged completed structures regain their effects when fully repaired. Repair cannot cheaply complete an unfinished project. Fleet Strength bonuses and other capacity effects are also unavailable while the granting structure is inactive; restoring the structure restores its granted capacity, not unrelated battle losses. Do not repeatedly propagate damage merely because a construction effect switches off.
- Upgrading requires the same number of additional paid Build stages as its base construction. On beginning an upgrade, its maximum becomes 6 for Minor or 10 for Major; retained Integrity is preserved and each Build adds 1. It is inactive until the upgrade is completed at full Integrity. Damage during upgrading removes stages and requires additional Build actions to replace them.
- Full host defence/Fleet Strength is required to begin, continue or Repair. A Mobile Capital may use its Faction Action to Defend itself, then Build or Repair in the same turn if fully restored. System-based structures without a host have no host-repair prerequisite. In-progress Void Stations remain attached to their construction fleet until completion.
- Destruction of a fleet or Mobile Capital destroys its attached constructions. Completed Void Stations become holdings with their own defence and retain their existing capture rules; their own construction Integrity is superseded by holding defence. Constructions aboard them retain Integrity normally.
- **Planetary/station capture:** apply assault damage to the host and all attached constructions first. **Any surviving construction transfers to the captor, Minor or Major**, at its remaining Integrity and build/upgrade state. Zero-Integrity structures are destroyed. The holding resets to 1 defence; structures do not reset or repair. Existing full-host requirements apply to subsequent Build or Repair actions.
- **System-based capture remains distinct:** control all planets and have Void Superiority; surviving Minor constructions transfer, Major constructions are destroyed. Completed Void Stations are captured as holdings, not through this system-control rule.
- Examples: a 4/5 project taking 3 damage becomes **1/5**; taking 2 becomes **2/5**. A 1/5 project hit by a Warp Storm is destroyed. If a host carries two projects, both lose the full damage amount.
- Applies prospectively from this inherited ruling. Current projects map directly to Integrity: **Vitae Womb Complex 1/5, Assimilation Viscera 1/5, Trial’s End Fabrication Array 5/5 completed and active**. No past battle or construction outcome is recalculated.

**Construction Limits:** A faction may have multiple constructions in progress simultaneously, but can only advance ONE per turn. Constructions on different planets progress independently.

#### Construction Examples

When building constructions, rename them to describe what the structure actually is within your faction's aesthetic and technology.

#### Construction Upgrade System

**Core Rules:**
- One of each unique construction per planet/fleet/system (no stacking duplicates)
- **Exception:** Constructions marked as **Repeatable** can be built multiple times on the same planet
- Existing constructions can be upgraded by spending additional actions
- Upgrades cost the same number of actions as the base construction
- Most upgrades are straight 2x the base effect
- Some constructions have no upgrade (already complete at base)

#### Planetary/Orbital Constructions

**Planetary/Orbital Constructions** — Built on a specific planet. Affects that planet or system.

*Minor (3 actions base, 3 actions upgrade, capturable)*

| Placeholder | Base Effect | Upgraded Effect |
|-------------|-------------|-----------------|
| [Orbital Shipyard] | Allows fleet creation at this location. Fleets created at 1/5. | No upgrade (prerequisite for Grand Orbital Shipyard) |
| [Supply Depot] | +2 Supply per Logistics Cycle | +4 Supply per Logistics Cycle |
| [Training Grounds] | +2 Manpower per Logistics Cycle | +4 Manpower per Logistics Cycle |
| [Automated Defences] | +1 defence regen/cycle if not attacked | +2 defence regen/cycle if not attacked |
| [Bunker Network] | +5 defender roll (AI) / -1 Difficulty (Player) | +10 defender roll (AI) / -2 Difficulty (Player) |
| [Orbital Cannons] | -1 Fleet Strength to largest hostile fleet when attacked | -2 Fleet Strength to largest hostile fleet when attacked |

*Major (5 actions base, 5 actions upgrade, destroyed on capture)*

| Placeholder | Base Effect | Upgraded Effect |
|-------------|-------------|-----------------|
| [Grand Orbital Shipyard] | Fleets created at 3/5. **Requires Orbital Shipyard.** | Grand Orbital Shipyard Complex — Fleets created at 5/5 |
| [Forge Complex] | +5 Supply per Logistics Cycle | +10 Supply per Logistics Cycle |
| [Military Academy] | +5 Manpower per Logistics Cycle | +10 Manpower per Logistics Cycle |
| [Regenerative Fortifications] | +2 defence regen/cycle if not attacked | +4 defence regen/cycle if not attacked |
| [Void Shield Generator] | -1 incoming attack damage (can reduce to 0) | -2 incoming attack damage (can reduce to 0) |
| [Fortification Network] | +2 to planet's maximum defence | +4 to planet's maximum defence |
| [Militia Barracks] | Defender commits 0 Manpower when defending this planet | No upgrade |
| [Landing Zones] | Garrison Transfers to this planet ignore full defence requirement | No upgrade |
| [Planetary Shield Network] | Invulnerable with Void Superiority / Defended status without | No upgrade |
| [Consolidation Works] | Upgrade planet type by one tier: Minor (2/2) → Standard (4/4) → Major (8/8). Current and maximum defence double. **Repeatable** until Major. Cannot upgrade to Capital — only one Capital per faction. | N/A (repeatable construction, not upgradeable) |

#### Void Constructions (Fleet-Attached)

**Void Constructions (Fleet-Attached)** — Mobile, destroyed if fleet is destroyed.

*Minor (3 actions base, 3 actions upgrade)*

| Placeholder | Base Effect | Upgraded Effect |
|-------------|-------------|-----------------|
| [Troop Transport] | 70% Manpower return (+10%) | 80% Manpower return (+20%) |
| [Repair Tender] | +1 fleet regen/cycle if no combat | +2 fleet regen/cycle if no combat |
| [Escort Squadron] | +3 to Fleet Battle roll | +6 to Fleet Battle roll |
| [Assault Boats] | +2 fleet strength for ground assaults | +4 fleet strength for ground assaults |
| [Bombardment Bay] | +1 ground assault damage | +2 ground assault damage |
| [Assault Cruiser] | +2/2 fleet strength (tracked separately) | +4/4 fleet strength (tracked separately) |

*Major (5 actions base, 5 actions upgrade)*

| Placeholder | Base Effect | Upgraded Effect |
|-------------|-------------|-----------------|
| [Flagship] | +5/5 fleet strength, max becomes 10/10 | +10/10 fleet strength, max becomes 15/15 |
| [Carrier] | +5 fleet strength for ground assaults | +10 fleet strength for ground assaults |
| [Siege Platform] | +2 ground assault damage | +4 ground assault damage |
| [Salvage Wing] | +3 Supply on Fleet Battle win | +6 Supply on Fleet Battle win |
| [Scout Squadron] | This fleet may Move and Attack with the same Fleet Action. The attack occurs after movement is resolved. | No upgrade |

#### Void Constructions (System-Based)

**Void Constructions (System-Based)** — Stationary. Follow same capture/destroy rules as Planetary constructions.

*Minor (3 actions base, 3 actions upgrade)*

| Placeholder | Base Effect | Upgraded Effect |
|-------------|-------------|-----------------|
| [Defence Platform] | +5 to defender roll in Fleet Battles | +10 to defender roll in Fleet Battles |

*Major (5 actions base, 5 actions upgrade)*

| Placeholder | Base Effect | Upgraded Effect |
|-------------|-------------|-----------------|
| [System Defence Station] | -1 enemy fleet strength/cycle | -2 enemy fleet strength/cycle |
| [System Repair Station] | +1 allied fleet strength/cycle (to max) | +2 allied fleet strength/cycle (to max) |
| [Logistics Anchorage] | +1 defence regen to unattacked planets/cycle | +2 defence regen to unattacked planets/cycle |
| [Void Station] | 2/2 station, functions as Minor planet | Upgrade via Consolidation Works: Minor (2/2) → Standard (4/4) → Major (8/8). Cannot become Capital. |

#### System Construction Capture Rules

**System Construction Capture Rules:**

To capture system-based constructions (Defence Platforms, System Defence Stations, etc.), you must:
1. Control ALL planets in the system
2. Have Void Superiority in the system

Once both conditions are met:
- **Minor constructions** transfer to the new controller
- **Major constructions** are destroyed (too specialized for enemy use)
- **Exception: Void Stations** — the only Major construction that transfers on capture (functions as a planet once complete). Constructions built ON the Void Station follow planetary capture rules: any surviving Minor or Major construction transfers after assault damage; zero-Integrity constructions are destroyed.

#### Void Station Assault

**Void Station Assault:** Void Stations are captured by reducing their defence to 0 through Attack actions (assault them like a planet), not through the system construction capture rules. When a Void Station falls, it transfers to the attacker and resets to 1 defence like any other planet.

#### Pre-Existing Stations

**Pre-Existing Stations:** Some holdings in the subsector are void installations rather than planetary bodies. These are marked in the Type column as "(Station)" and are treated as Void Stations of the listed tier in every respect — defence value, Attack and Defend cost scaling, Logistics income, Minor Faction resource values, and the Minor Faction fleet calculation. They are assaulted, captured, and reset to 1 defence exactly as planets are, and constructions may be built on them under normal rules. A Station cannot serve as a Capital.

### Phase 6: Resolve Battle

If any faction chose Attack, fight the battle in Soulstorm. See Section 3 for battle setup. Or conduct AI to AI battle. Fleet Battles are handled by dice rolls outlined in Phase 2.

**Turn Order:** Factions act in order: Major Faction A → Major Faction B → Major Faction C. Each faction completes all their actions (Fleet, Faction, Social, Construction) before the next faction's turn begins.

**AI vs AI Rules:** On a defended planet, the defender's total roll gains +15.

If all factions skip combat actions: No battle this cycle. All sides gain their chosen benefits.

#### Planet Fall Penalties

**Planet Fall Penalties:** When a planet falls (defence reaches 0), the planet changes hands and resets to 1 defence. The losing faction suffers:
- **Supply:** -2 (or -4 if Capital) — replaces normal defeat Supply loss
- **Manpower:** -2 (or -4 if Capital) — additional penalty on top of committed Manpower
- **Fleet Damage:** Equal to damage dealt in the final assault, distributed as follows:
  - Apply damage one point at a time to the strongest fleet present
  - Ties: Attacker chooses which fleet takes the point. Against Minor Minor factions, the referee chooses the allocation; retain player choice against Major Factions (inherited ruling).
  - No fleet drops below 1/5 until ALL fleets are at 1/5
  - Once all fleets are at 1/5, each additional point of damage destroys one fleet (attacker chooses which). Destroying a fleet consumes 1 damage.

*Example: Defender has three fleets (2/5, 5/5, 5/5) and the final assault dealt 8 damage. Damage applies to strongest first: 5/5 → 4/5 → 3/5 → 2/5 → 1/5, then second 5/5 → 4/5 → 3/5 → 2/5, then 2/5 → 1/5. Final state: 1/5, 2/5, 1/5.*

#### Fleet Destruction

**Fleet Destroyed:** When a fleet is destroyed (reduced to 0 or below), the owning faction loses -1 Manpower in addition to losing the fleet. This applies whether destroyed through Fleet Battle, Planet Fall penalties, or any other means.

### Phase 7: End of Cycle

- Record battle result
- Update Planet progress. Successful attack lowers defence based on attacker's fleet strength (1 per 5 strength, minimum 1 if uncontested).
- Check if any Planets changed hands
- Advance Cycle Counter

---

## SECTION 3: BATTLE SETUP

### Difficulty (Based on YOUR Supply)

Supply represents logistics capacity: materiel, munitions, fuel, food, replacement parts, and everything needed to sustain military operations. **Supply determines difficulty only — how well-equipped your forces are.**

| Supply | Base Difficulty |
|--------|-----------------|
| 1-20 Critical | Insane 5/5 |
| 21-40 Rationed | Harder 4/5 |
| 41-60 Sustainable | Hard 3/5 |
| 61-80 Surplus | Standard 2/5 |
| 81-100 Abundant | Easy 1/5 |

### Difficulty (Based on ENEMY Supply)

| Enemy Supply | Modifier |
|--------------|----------|
| 1-20 Critical | -2 Difficulty |
| 21-40 Rationed | -1 Difficulty |
| 41-60 Sustainable | — |
| 61-80 Surplus | +1 Difficulty |
| 81-100 Abundant | +2 Difficulty |

### Allied Factions (Based on YOUR Manpower)

Manpower represents trained combat personnel, casualty replacement capacity, and strategic depth — your ability to field multiple formations. **Manpower determines faction count only — how many formations you can deploy.**

| Manpower | Effect |
|----------|--------|
| 1-20 Critical | -2 Allied Factions (minimum 1) |
| 21-40 Rationed | -1 Allied Faction (minimum 1) |
| 41-60 Sustainable | No modifier |
| 61-80 Surplus | +1 Allied Faction |
| 81-100 Abundant | +2 Allied Factions |

### Enemy Factions (Based on ENEMY Manpower)

| Enemy Manpower | Effect |
|----------------|--------|
| 1-20 Critical | -2 Enemy Factions (minimum 1) |
| 21-40 Rationed | -1 Enemy Faction (minimum 1) |
| 41-60 Sustainable | No modifier |
| 61-80 Surplus | +1 Enemy Faction |
| 81-100 Abundant | +2 Enemy Factions |

### Quick Reference: Modifier Stacking

| Source | Effect |
|--------|--------|
| Your Supply | Sets base Difficulty (1/5 to 5/5) |
| Enemy Supply | -2 to +2 Difficulty |
| Your Manpower | -2 to +2 Allied Factions (minimum 1) |
| Enemy Manpower | -2 to +2 Enemy Factions (minimum 1) |

Difficulty caps at 1/5 minimum and 5/5 maximum. Faction count minimum is 1 (cannot remove only player or only opponent).

### Faction Count Limits

The maximum factions per side is 4 (map maximum 8 total). If bonuses would create more factions than the map allows, scale both sides down proportionally while maintaining the difference.

| Calculated | Scaled |
|------------|--------|
| 5v4 | 4v3 |
| 5v5 | 4v4 |
| 6v4 | 4v2 |
| 6v5 | 4v3 |
| 6v6 | 4v4 |
| 7v5 | 4v2 |
| 7v6 | 4v3 |

Continue pattern: reduce both sides equally until largest side is 4, maintaining the original difference.

### Map Size

**Multi-team and map-availability clarification (inherited clarification):** Start with twice the largest team’s final formation count. If total participants exceed that capacity, use at least enough slots for every participant. The player may choose the exact required capacity, including an odd-sized map, or a larger map if the exact size is unavailable or another map better fits the battle’s narrative location. Close unused slots. Never remove formations or change their allegiance to fit a map. A third-party raider is an additional hostile team, not a replacement for an attacker or defender. Example: 2 Faction A vs 2 Minor defenders vs 1 raider uses a 5-player map, or a 6-player map with one slot closed at the player’s preference. This exception takes precedence over the two-team examples below.

**Use a map with twice as many player slots as the larger team has factions, after applying all faction-count modifiers and limits.** Count every faction on that team, including the player. This determines the map's player capacity, not the number of factions that must participate: leave unused slots closed rather than adding extra factions.

| Final teams | Required map size | Unused slots |
|---|---|---|
| 1v1 | 2-player map | 0 |
| 2v1 or 2v2 | 4-player map | 1 or 0 |
| 3v1, 3v2 or 3v3 | 6-player map | 2, 1 or 0 |
| 4v1, 4v2, 4v3 or 4v4 | 8-player map | 3, 2, 1 or 0 |

For example, **two attacking factions versus one defending faction use a 4-player map with one slot closed**, not a 3-player map. This keeps the map capacity consistent for the larger force instead of shrinking it to match an outnumbered opponent.

### Participating Fleet Strength (Friendly Fleets)

For a Ground Assault, calculate total Fleet Strength only from your fleets and approved allied fleets **actually participating in that battle**. Fleets merely present in-system grant no ground-battle faction slots, damage or combat-roll strength. They still count for void superiority.

| Fleet Strength | Modifier |
|----------------|----------|
| 1-4 | No bonus |
| 5-9 | +1 Allied Faction |
| 10-14 | +2 Allied Factions |
| 15-19 | +3 Allied Factions |
| 20-24 | +4 Allied Factions |
| 25+ | +5 Allied Factions |

**Clarification — Mobile Capitals and Fleet Constructions (inherited clarification):** Ground-assault allied formation bonuses depend on the **combined actual Fleet Strength committed**, not the number of fleet assets. Gain **+1 allied formation for each full 5 participating Fleet Strength**, before applying Manpower modifiers and the existing team-size limits. A participating Mobile Capital contributes its **current defence as Fleet Strength**: a 12/12 Mobile Capital alone contributes 12 strength, giving **+2 allied formations**, with 2 strength left over that grants no additional formation. It remains one asset and spends one Fleet Action; it does not become two separate fleets. Strength from all participating assets is pooled before dividing by 5.

Fleet Constructions follow their stated effects. Any construction effect explicitly increasing participating Fleet Strength contributes to this calculation. A bonus to bombardment or assault **damage alone is not Fleet Strength** and does not grant allied formations or increase base Manpower commitment. Only constructions attached to participating assets contribute applicable assault effects. A 12-strength Mobile Capital therefore has **2 base damage and commits 2 Manpower**, before construction damage bonuses; its final Soulstorm team still depends on Manpower modifiers. This clarifies the existing strength-based rule and does not change previously resolved battles.

#### Fleet Action Availability and Ground Assault Commitment

**One action per fleet per Cycle:** A fleet may act on its owner's turn or, with its owner's approval, join an ally's assault on that ally's turn. Either use consumes the same single Fleet Action. A fleet that already moved, expanded, fought or otherwise acted this Cycle cannot participate in a later allied assault. Acting for an ally also prevents acting again on its owner's turn. For example, moving into an ally's system on your turn prevents that fleet joining the ally's assault later in the same Cycle. Mobile Capitals follow the same Fleet Action limit. Reset availability at the next Cycle; track the action used for each fleet.

**Choose participants before paying costs.** Ground Assault base damage is **floor(total participating Fleet Strength / 5), minimum 1**. The attacker must commit Manpower equal to that full base damage, even when the target has fewer defence points remaining. You cannot undercommit Manpower while retaining the strength, damage or additional faction slots of more fleets. Construction damage bonuses do not increase this base commitment.

Three participating 5/5 fleets mean **15 strength, 3 base damage and 3 Manpower committed**, even against 1 remaining defence. One participating 5/5 fleet means **5 strength, 1 base damage and 1 Manpower**, with only its own strength contributing to allied slot bonuses. Other fleets retain unused actions and contribute only to void superiority until assigned an action.

These clarified participation rules apply prospectively from the inherited ruling. Previously resolved battles stand. Minor Faction defensive fleet support continues under the Minor Faction rules; this allied action-sharing rule does not create Minor Faction turns or orders.

#### Allied Battle Faction Eligibility

Extra allied slots in a Soulstorm battle may represent another campaign faction **only if that allied faction has a fleet in the system**. For an attack, its fleet must participate with its owner’s explicit approval and spend its one Fleet Action for that Cycle. Approval must be relayed to the referee; do not invent allied consent. An allied alignment alone does not permit calling in an absent faction.

When all contributing fleets belong to the same campaign faction, fill any additional allied battle slots with **duplicate formations of that faction**. These slots represent its own forces fighting together; they do not introduce a new campaign faction, grant extra resources or fleets, or constitute the Summon Allies Faction Action. Eligibility determines who may fill the calculated slots, not additional slot bonuses.

**Station A example:** Fleet A, Fleet B and Fleet C all belong to the Major Faction A. Therefore, the two attacking slots are **the player's Major Faction A and one AI-controlled duplicate Major Faction A formation**. No other Imperial faction is called in.

### Fleet Strength in System (Hostile Fleets)

Calculate total Fleet Strength of all hostile fleets (different Alignment) in-system.

| Fleet Strength | Modifier |
|----------------|----------|
| 1-4 | No bonus |
| 5-9 | +1 Enemy Faction |
| 10-14 | +2 Enemy Factions |
| 15-19 | +3 Enemy Factions |
| 20-24 | +4 Enemy Factions |
| 25+ | +5 Enemy Factions |

**Example:** You have a 5/5 Fleet and a 2/5 Fleet (total 7) in-system. A hostile faction has two 3/5 Fleets (total 6). You gain +1 Allied Faction, and the enemy gains +1 Enemy Faction. The battle becomes a 2v2 engagement.

### Planet Conquest

| Planet Type | Planet Defences | Examples |
|-------------|-----------------|----------|
| Minor | 2 | Agri-worlds, Mining colonies, Outposts |
| Standard | 4 | Forge worlds, Civilised worlds |
| Major | 8 | Hive worlds, Fortress worlds |
| Capital | 12 | Sector capitals, Aeldari Craftworlds, Necron Tomb Worlds |

### Attack Cost Scaling

| Planet Type | Supply Cost |
|-------------|-------------|
| Minor | -1 Supply |
| Standard | -2 Supply |
| Major | -3 Supply |
| Capital | -4 Supply |

### Defend Cost Scaling

| Planet Type | Supply Cost | Manpower Cost |
|-------------|-------------|---------------|
| Minor | -1 Supply | -1 Manpower |
| Standard | -2 Supply | -2 Manpower |
| Major | -3 Supply | -3 Manpower |
| Capital | -4 Supply | -4 Manpower |

### Battle Outcome Effects

**Attacker Commitment:**
- Supply: Paid upfront, scaled by world type (see Attack Cost Scaling). Lost regardless of outcome.
- Manpower: Commit equal to base damage dealt (1 per 5 Fleet Strength, minimum 1). Lost on defeat, 60% returned on victory.

**Defender Commitment:**
- Supply: Commit equal to attacker's Supply cost (scaled by world type: Minor 1, Standard 2, Major 3, Capital 4). Lost on defeat, 80% returned on victory.
- Manpower: Commit equal to attacker's damage dealt (including construction bonuses). Lost on defeat, 80% returned on victory.

**Note on Damage Bonuses:** Constructions like Bombardment Bay (+1) and Siege Platform (+2) increase total damage but do NOT increase attacker Manpower commitment. The attacker's commitment is based purely on fleet strength — the bodies being thrown at the problem. Damage bonuses represent superior firepower, not more troops on the ground. The defender, however, must respond to the full incoming damage.

| Outcome | Effect |
|---------|--------|
| **Victory on Attack** | Planet Defence reduced by damage dealt. Attacker returns 60% Manpower. Defender loses 100% committed Supply and Manpower. |
| **Defeat on Attack** | Attacker loses 100% committed Manpower (Supply already spent). Defender returns 80% committed Supply and Manpower. |
| **Victory on Defence** | Defender returns 80% committed Supply and Manpower. Attacker loses 100% committed Manpower (Supply already spent). |
| **Defeat on Defence** | Planet Defence reduced by damage dealt. Defender loses 100% committed Supply and Manpower. Attacker returns 60% Manpower. |
| **Planet Falls** | See Planet Fall Penalties in Section 2. |

**Note:** In uncontested systems (no hostile fleets present), attacks resolve via Uncontested Bombardment — see Attack action in Phase 2.

### Losing a Capital

When a faction loses their Capital, they must designate a new Capital on an owned planet. The faction is then locked into the **Establish New Capital** forced action until the new Capital reaches maximum defense of 12. This forced action has no Supply or Manpower cost.

**Establish New Capital:** Each use doubles both current and maximum defense of the Provisional Capital until maximum reaches 12.

| Starting World | Cycle 1 | Cycle 2 | Cycle 3 |
|----------------|---------|---------|---------|
| Minor (2/2) | 4/4 | 8/8 | 12/12 |
| Standard (4/4) | 8/8 | 12/12 | — |
| Major (8/8) | 12/12 | — | — |

Once maximum defense reaches 12, the Capital is fully established and immediately gains a built-in Orbital Shipyard. The faction is then unlocked and may take other actions, even if current defense is below 12. If attacked during rebuild, damage is applied after the defense doubling.

**Loss of the final fallback point:** If a faction has no remaining controlled planets, stations or surviving Mobile Capital, it is eliminated and all its remaining fleets are destroyed: they have nowhere to return, resupply or regroup. Apply normal Planet Fall fleet damage first, then destroy any survivors if no fallback point remains. A surviving controlled planet, station or Mobile Capital prevents this automatic destruction; normal battle and Planet Fall losses still apply. Apply normal fleet-destruction consequences where applicable; Minor factions do not suffer Major Faction resource penalties.

### Minor Faction Factions

**Terminology — Minor Factions vs Minor Faction-Aligned Major Factions:**

"Minor Faction" serves two distinct roles in this campaign. **Minor Factions** are static NPC powers — they do not take turns, do not act strategically, and defend when attacked. They are obstacles and opportunities on the map. **Minor Faction-Aligned Major Factions** are full player or AI factions that happen to carry the Minor Faction alignment. They take turns, make strategic decisions, and operate with full agency. The alignment simply means they are not bound to Imperium, Chaos, Necron, or any other bloc — they fight for themselves. No Major Faction in the the example campaign Campaign currently carries this alignment.

These two uses of "Minor Faction" should never be confused. The rules below apply only to Minor Factions.

---

### Minor Factions

Minor Factions are minor powers that control one or more planets within a system. They do not take turns or actions — they are static obstacles that defend when attacked.

**Fleet Calculation:**
- Total Fleet Strength = sum of total planetary defence across all controlled worlds
- Fill 5/5 fleets first, remainder becomes additional fleet
- Example: Major (8/8) + Minor (2/2) + Minor (2/2) = 12 → two 5/5 fleets and one 2/5 fleet

**Fleet Rules:**
- Fleets do not move (system defense only)
- Fleets provide orbital support during ground assaults (counts as combat)
- +1 Fleet Strength regeneration per cycle if not engaged in Fleet Battle or Ground Assault (allocate to any fleet, up to original starting max)
- If a fleet is destroyed, it is gone forever — Minor Factions cannot create new fleets

**Resources (Per Planet):**

When a Minor Faction planet is attacked, only that planet's individual resources are used for the defense roll — not the combined resources of all planets controlled by the faction.

| World Type | Base Supply | Base Manpower |
|------------|-------------|---------------|
| Minor | 40 | 40 |
| Standard | 60 | 60 |
| Major | 80 | 80 |

Current Supply/Manpower = Base × (Current Defense / Max Defense)

**Agreed ruling — Minor Faction resources (inherited clarification):** These are defence-derived per-planet values, not Major Faction resource pools. Do not deduct Major Faction resource losses from them, including Supply Crisis or the -1 Manpower fleet-destruction penalty. This applies to both single-world and multi-world Minor Factions. Defence changes still alter resources through the formula above; fleet damage and destruction still apply normally. Independent-aligned Major Factions continue to use Major Faction resource rules.

Example: A Standard world at 2/4 defense has 60 × (2/4) = 30 Supply and 30 Manpower

Fleet Strength in system still counts for all Minor Faction fleets present, but ground resources are planet-specific.

**Defense:**
- Regenerates +1 per cycle if not attacked (up to max)

**Scope:**
- Minor Factions are typically single-system, often single-planet
- Multiple Minor factions can exist in the same system
- Each Minor Faction faction has its own fleet, resources, and defense values

### Resource Deficits

**Resource deficit rule — applies prospectively.** Supply and Manpower have separate deficit and recovery tracks. Whenever either resource reaches **0 or below**, including through an affordable voluntary action, immediately trigger its deficit and record it as **0**. Voluntary actions that cost more than available resources remain prohibited. Past turns are not recalculated.

**Resource lock:** While a track is active, its resource stays at 0 and cannot be spent. Ignore all income, gains and losses to that resource, including Logistics, events, returns and other effects; nothing is banked or deferred. The other resource continues to gain and lose normally unless it has its own active track. Further losses cannot restart, extend or retrigger an already active track. This immunity concerns resource changes only, not direct fleet, holding or construction damage.

**Emergency Rationing — compulsory Faction Action:** While either track is active, the faction must spend its Faction Action on Emergency Rationing for one active resource. This replaces Reinforce for a Supply deficit and Muster for a Manpower deficit; neither ordinary action can bypass the recovery requirement. Each Emergency Rationing action advances the selected track by one, costs no resources, and gives no immediate income. After **three actions assigned to that track**, end its lock and restore that resource to **exactly 10 total**, not +10 per action. Recovery counts actions, not elapsed Cycles.

If a deficit begins after the Faction Action has already been used, the compulsory action starts next turn. If it begins before that phase, the next available Faction Action must be Emergency Rationing. Other phases remain available subject to their normal rules and affordable costs using unlocked resources. Completion releases the resource immediately for subsequent phases; income ignored earlier is not awarded retroactively.

**Overlapping tracks:** Track Supply and Manpower separately, each at 0/3, 1/3 or 2/3 recovery actions. With both active, the faction chooses which one to advance each turn; one Faction Action cannot advance both. The unselected track retains its progress. Both tracks require six actions in total. Once a resource has recovered, normal gains and losses resume and a later fall to 0 can start a new deficit for it.

**One-time fleet degradation on entry:**
- Supply deficit: all fleets lose 1 Fleet Strength; fleets at 1/5 are destroyed.
- Manpower deficit: all fleets lose 1 Fleet Strength, minimum 1/5; this degradation alone cannot destroy a fleet.
- Apply each loss once when that resource’s new deficit begins, never once per recovery action or further ignored penalty. Existing mobile-capital and attached-construction damage rules still apply where relevant.
- If both trigger together, resolve Supply first, then Manpower. A fleet-destruction Manpower loss can trigger the separate Manpower track if it is not already locked. Starting both tracks does not merge their recovery.

**Defending during a Manpower deficit:** Retain the existing battle options: Forced Conscription or Isolated Defense. Forced Conscription strips defence from fully defended planets elsewhere, one defence per required Manpower, providing that battle’s commitment only; it does not replenish or unlock the resource pool or advance recovery. Isolated Defense uses the local garrison: AI defender −15 to roll; player defender +2 difficulty. If the attacker wins, apply normal damage and no defender Manpower commitment; if the attacker loses, it returns 60% of its commitment. Any return to a resource currently locked by a deficit is ignored. Normal caps and rounding apply.

**Example:** Supply recovery is at 1/3 and Manpower is 2. A Supply Crisis ignores its Supply loss, leaving that track at 1/3, but its −5 Manpower triggers a new Manpower deficit at 0/3. Apply Manpower degradation once. The faction chooses which track its next compulsory Emergency Rationing action advances. Each resource stays at 0 until its own third action restores it to 10.

---

## SECTION 4: RANDOM EVENTS

At the start of each Cycle, before any faction takes its turn, roll 1d6. On a 1 or 6, roll 1d6 again on the table below. One roll per Cycle, not one per faction. The resulting event applies for the whole of that Cycle and expires immediately before Major Faction 1 begins the next.

| d6 | Event | Effect |
|----|-------|--------|
| 1 | **Warp Storm** | All Factions: All Fleets -1 Fleet Strength. Fleets cannot move for the remainder of this Cycle. |
| 2 | **Ambush!** | Attackers this Cycle get +1 difficulty. Defenders get -1 difficulty. AI vs AI: Defender +10 to roll. |
| 3 | **Supply Crisis** | All Factions: -5 Supply and -5 Manpower. |
| 4 | **War Fervor** | All Factions: +5 Supply and +5 Manpower. |
| 5 | **Third Party Raid** | If a ground battle occurs, add a random hostile faction (player determines faction type based on context). Raiders are an additional hostile team and cannot capture territory or establish holdings, regardless of world tier or battle result. Survivors withdraw after the raid. If raiders win on a Major/Capital, retain the existing defence-halving effect (rounded down), but no territorial transfer to raiders. On Minor/Standard worlds, remove the former capture effect; normal applicable battle effects and traits still resolve. Do not invent additional loot or resource penalties. |
| 6 | **Intel Breakthrough** | You choose: -1 difficulty this battle OR +1 damage dealt on a successful attack. AI vs AI: Attacker +10 to roll. |

---


