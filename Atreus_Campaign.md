# The Atreus Campaign

Created 7 October 2026 · Subsector playtest · **Cycle 14 - Phase 0 complete**

Authoritative ledger: [Atreus_Campaign.md](https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/Atreus_Campaign.md) · [Live campaign](https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/atreus.html) · [Status](https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/atreus-status.json)

Rules: **6 October 2026 playtest edition with the approved 7 October Minor Alignment correction and 8 October shipyard construction amendment**. The base edition was pinned to GitHub commit `113ec69a6163d36fb2164b9b624d14d8889986e5`. The complete rules, including those amendments, follow the campaign registers below. Later source changes do not automatically migrate this campaign. The observed balance spread remains 28 percentage points; human playtesting is now the purpose. Dessica remains a separate suspended campaign.

## Opening situation

For generations, Atreus sent armies outward and received their survivors through its shrines. Foundries cast engines beside cathedral bells; pilgrims crowded the same anchorages that loaded troop transports. Isolation has left the machinery of that old obligation intact in places, but no authority accepted everywhere.

From Tiryns, Warsmith Acastor Orontes offers the service of the Iron Paladins to worlds the wider Imperium can no longer reach. Canoness Althaia sees another danger in their arrival. To her, their ancestry and long passage through the Eye make their professions of loyalty impossible to trust. She intends to destroy the Chapter. In Calydon, Bell-Ringa has taken a foundry Capital and gathers mobs to the sound of stolen bells. The surviving rulers of Atreus must decide whose protection they can afford—and whose demands they can survive.

The Paladins’ loyalty is an established fact of the setting. Their supposed corruption is the Order’s conviction, not a revelation about the Chapter. No distant Imperial authority has issued a new decree in this campaign.

## Campaign conventions and opening status

- Standing rollover procedure (Jake, 7 October 2026): after the third Major turn, finish Cycle-end checks, increment the Cycle, reset Fleet Actions and resolve Phase 0 in order: construction effects, scheduled Logistics including income/upkeep, then events. Publish the resulting state before handing back to the Iron Paladins. Do not wait for a separate opening request.

- Three Major Factions, in fixed order: **Iron Paladins → WAAAGH! Bell-Ringa → Order of Saint Erigone**. Minor factions take no turns.
- Every Major starts with 20 Supply, 20 Manpower, one 5/5 fleet and its 12/12 Capital only. This equal 5/5 opening is the explicit Atreus setup convention; Create Fleet during play remains 1/5 unless a rule changes it.
- Each Major home system also contains one hostile ordinary Minor with a Standard and Minor planet. This is the approved home profile, not extra territory for the Major.
- Ten systems; Fleet Movement reaches any system with the normal action. **No directional, adjacency, distance or travel-lane mechanics.** The system directory is a roster, not a route network.
- Mycenae is the authored prize system: House Atreides owns a Major planet, Standard planet and Standard station. This fixed profile implements the approved prize placement; it is not represented as a rolled ordinary profile.
- The remaining six systems use the saved d20 rolls. Ownership, names and faction identities are authored independently of those rolls. No rerolls were made.
- Campaign victory convention: the last surviving Major wins after rival Majors lose their final fallback. An agreed concession can end play earlier. Minor holdings do not become owned territory and need not be conquered to meet this condition. No forced 100-Cycle ending.
- Cycle 1 Phase 0 is resolved once: no periodic construction effects or Endurance recovery; Logistics is not due; event check d6 = 3, so no event. Opening effects left starting resources, holdings and fleets unchanged. First Logistics is Cycle 3. All three Major turns are resolved below. Olenos has fallen to the Orks and Daeira to the Order. Cycle 1 is complete. Cycle 2 is complete; its Warp Storm has expired. Cycle 3 construction effects, Logistics and event check are resolved below; no event is active.
- Calendar date within Imperium Nihilus is intentionally unspecified. Track elapsed Cycles; there is no invented conversion to years. Exact officer ages and any finite lifespan windows remain unassigned, so no automatic ageing deaths are scheduled.
- Artwork establishes visual identity. Army Painter channel mapping remains unassigned until the actual faction interfaces are checked; this gives no mechanical benefit and does not delay campaign setup.


|Cycle|Phase|Event|Next faction|Pending battle|Next Logistics|
|---|---|---|---|---|---|
|14|Phase 0 complete; awaiting Iron Paladins orders|No event (check: 5)|Iron Paladins|None|15|

## Major faction registers

### 1. Iron Paladins

The Iron Paladins descend from loyal Iron Warriors who rejected Perturabo. Their penitence crusade in the Eye produced a distinct Chapter, its own offices and a religious obligation to the wounded Emperor. They serve the Imperium and would obey Guilliman; their independent operational oversight pending orders is not separatism. Orontes commands. Menandros advises, leads the Ironbound and is the designated successor; Jake retains the Warsmith’s decisions. The Chapter favours prepared assaults and durable protection, with each protected world adding obligations.

![Warsmith Acastor Orontes — supplied concept art](atreus_orontes.png)

|Field|Current value|
|---|---|
|Controller|Jake|
|Alignment|Imperium|
|Commander / deputy|Warsmith Acastor Orontes / First Paladin Menandros|
|Trait|The Iron Tithe — Efficient Logistics|
|Exact effect|Reinforce grants 8 Supply; Muster grants 8 Manpower.|
|Capital|Tiryns — Argos — 12/12|
|Resources|22 Supply / 23 Manpower; neither deficit active|
|Fleet|Crusade Fleet Anabasis - Aulis - 5/5; The Emperor’s Judgement - Aulis - 5/5; Vigilatius - Argos - 5/5; all actions unused in Cycle 14|
|Constructions|Built-in Capital Orbital Shipyard; The Grand Forge of Iron (upgraded Major Forge Complex), Tiryns, upgrade progress 5/5 and Integrity 10/10; upgrade complete and active, +14 Supply per Logistics Cycle; Gene-Seed Vaults (Major Military Academy) on Heraion, progress and Integrity 3/5, inactive|
|Next Logistics if unchanged|22 Supply / 8 Manpower gross including upgraded Forge and Schoenus; 3/3 fleet upkeep; net +19 / +5|
|Briefing|[briefing_first_paladin_menandros.md](briefing_first_paladin_menandros.md)|

### 2. WAAAGH! Bell-Ringa

Bell-Ringa won his command by crushing his predecessor with a cathedral bell. The captured foundries of Da Bellworks support a Goff host that values hard fighting, working engines and trophies earned by conquest. Boss Nob Klanga coordinates mobs and detached forces. Growth depends on bringing fighters, ships and ammunition to the same battle; pride can draw the Warboss into an expensive unfinished fight. Da Gate-Krasha commemorates the fleet’s breaches of the foundry anchorage, without assigning a special ship or bonus.

![Warboss Bell-Ringa — supplied concept art](atreus_bell_ringa.png)

|Field|Current value|
|---|---|
|Controller|AI faction instance|
|Alignment|Ork|
|Commander / deputy|Warboss Bell-Ringa / Boss Nob Klanga|
|Trait|More Boyz Fer Da Fight — Martial Culture|
|Exact effect|+4 Manpower each Logistics Cycle.|
|Capital|Da Bellworks — Calydon — 12/12|
|Resources|7 Supply / 28 Manpower; neither deficit active|
|Fleet|Da Gate-Krasha - Eleusis - 7/7; Da Fist - Eleusis - 5/5; Da Backhand - Calydon - 5/5; all actions unused in Cycle 14|
|Constructions|Built-in Capital Orbital Shipyard; Da Iron Gob, upgraded Major Forge Complex on Da Bellworks, upgrade progress 3/5 and Integrity 8/10; base +7 Supply income retained at Integrity 5 or above, +14 at full upgraded Integrity; Da Jaw-Breaka (Assault Cruiser) on Da Gate-Krasha, progress and Integrity 3/3, complete; +2 permanent Fleet Strength and capacity granted (7/7 total)|
|Next Logistics if unchanged|16 Supply / 13 Manpower gross including Forge, trait and Triptolemos; 3/3 fleet upkeep; net +13 / +10|
|Briefing|[briefing_warboss_bell_ringa.md](briefing_warboss_bell_ringa.md)|

### 3. Order of Saint Erigone

The Order’s convents and shrine network preserve hospitals, military stores and authority across isolated communities. Its fictional campaign saint, Erigone, is remembered for three refusals of sanctuary to a rebel household. Althaia’s immediate case against the Paladins is their time in the Eye, reinforced by their Legion ancestry. She seeks their destruction and refuses joint operations regardless of their loyal conduct. Palatine Ianthe shares that judgement but can dispute methods and timing. Material support does not remove the need to conserve trained Sisters.

![Canoness Althaia — supplied concept art](atreus_althaia.png)

|Field|Current value|
|---|---|
|Controller|AI faction instance|
|Alignment|Imperium|
|Commander / deputy|Canoness Althaia / Palatine Ianthe|
|Trait|Offerings of the Faithful — War Economy|
|Exact effect|+6 Supply each Logistics Cycle.|
|Capital|Erigone — Eleusis — 12/12|
|Resources|5 Supply / 34 Manpower; neither deficit active|
|Fleet|The Third Refusal - Eleusis - 5/5; The Returning Escort - Eleusis - 5/5; The Unbroken Procession - Eleusis - 5/5; The Oath at the Gate - Eleusis - 3/5; all actions unused in Cycle 14|
|Constructions|Built-in Capital Orbital Shipyard; The Vigil of the Three Refusals, Major Military Academy on Erigone, progress 5/5 and Integrity 5/5; complete and active, +7 Manpower per Logistics Cycle; Castalia Anchorage (Minor Orbital Shipyard), progress and Integrity 3/3, complete and operational; The Breach Litany (Bombardment Bay) on The Third Refusal in Eleusis, progress and Integrity 3/3, complete and active; +1 Ground Assault damage; The Watch of Daeira (Minor System Defence Platform), Eleusis, progress and Integrity 1/3, inactive|
|Next Logistics if unchanged|16 Supply / 17 Manpower gross including Academy, trait and Pytho; 4/4 fleet upkeep; net +12 / +13|
|Briefing|[briefing_canoness_althaia.md](briefing_canoness_althaia.md)|

## Personnel and succession

|Faction|Commander|Deputy|Age / lifespan record|Succession|
|---|---|---|---|---|
|Iron Paladins|Acastor Orontes|Menandros|Astartes; biological ages unassigned. Orontes is a Heresy veteran; Warp time is not biological age.|Menandros designated; no event scheduled|
|WAAAGH! Bell-Ringa|Bell-Ringa|Klanga|Orks; exact ages unknown, no natural expiry imposed.|Klanga is deputy, not guaranteed a peaceful succession|
|Order of Saint Erigone|Althaia|Ianthe|Humans; exact ages and rejuvenation access unassigned. Source human range is guidance, not a death roll.|Ianthe operational deputy; formal succession requires recorded resolution|

One Manpower represents approximately 40 Astartes, 400 Orks or 100 Sisters in the relevant Major military pool. These are abstractions, not exact ship complements or fixed Chapter establishments. Succession does not reset resources or traits. Jake may temporarily voice Klanga or Ianthe as in-character counsel; neither receives an extra action.

## Diplomacy and explicit hostility exceptions

**7 October ruling: only Major Factions have Alignments.** Minor Factions have no Alignment. They are independent hostile powers and cannot enter diplomatic agreements or alliances. Species, Emperor worship, human origin and Soulstorm army selection do not confer alliance. A Minor incorporated into a Major ceases to be a separate aligned Minor.

All three Majors are mutually hostile. Iron Paladins and Order of Saint Erigone retain Imperium Alignment but have the agreed explicit hostility exception. WAAAGH! Bell-Ringa has Ork Alignment.

All 13 Minors are independent hostile powers; none can negotiate an agreement with a Major or another Minor. Their ships count as hostile to other factions, including other Minors. Rustjaw is not allied to Bell-Ringa; the Thessalian commands are not allied to each other. No territorial absorption, truce or communiqué has occurred.

### Death is the only absolution

The Order of Saint Erigone and the Iron Paladins begin the campaign with this exchange defining their hostility.

**The Sisters:**

> The traitor legions are damned. The sin is in the geneseed. You carry Perturabo's legacy in your blood. Death is the only absolution.

**The Paladins:**

> We agree. We ARE damned. We owe a debt that can never be repaid. But a corpse digs no trenches. A corpse holds no wall. We will serve until our bodies fail, and THEN you can have our deaths - but not one moment sooner, because wasted potential is its own sin against the Great Work.

For Althaia, their answer confirms the sentence: continued service cannot cleanse what she believes is corruption carried in their blood. She seeks their destruction, not their departure from Atreus. Their years in the Eye of Terror deepen her conviction, even in the absence of outward taint.

For the Paladins, damnation expresses the debt they accept and the penance they owe. They remain loyal servants of the Emperor. Every trench dug, wall held and Imperial life defended is work still owed; surrendering their lives while they can perform that work would itself betray their duty. Their acknowledgement gives the Order no right to decide when that service ends.

The same language of guilt and absolution therefore sustains both sides of the conflict. The Order demands death now; the Paladins insist upon service for as long as they can give it.

## Fixed Third Party Raid

**The Nail-Takers**, an Iron Warriors raiding detachment led by **Warsmith Kordax**, are the fixed raiders for Atreus. Their name refers to the metal spikes driven through armour plates stripped from captured engines and displayed as trophies. They seek war matériel and captives while local defenders are committed elsewhere. They are separate from House Atreides and every other holding faction.

Use **Chaos Marines** to represent the Iron Warriors; switch to a dedicated Iron Warriors entry only if confirmed in the installed mod. The verified Unification roster does not list a standalone Iron Warriors race. The detachment has no campaign holdings, resource pool, fleet register, turns or territory-capture rights. The raid event is not active at setup. When it occurs, the raider fields one team in the first round, with each main side limited to three deployed teams while the raider remains; overflow waits in reserve. Once beaten, the raider is removed for that engagement. Subsequent main-side rounds use the agreed maximum four each and the survivor/reserve procedure. No extra trait or bespoke difficulty effect is granted.

## Systems and holdings

All holdings start at full defence; none is Defended. All fleets are unengaged with unused actions. A Capital’s built-in shipyard exists without a construction slot; other industrial or religious descriptions grant no completed construction.


### Argos

**Void Superiority:** Iron Paladins 5 vs hostile fleets 0 - Iron Paladins superior; no hostile fleet present.

The Iron Paladins control Tiryns, Prosymna and newly captured Heraion, securing all holdings in Argos. The Argive Muster Council has lost its final holding and is eliminated.

Setup: fixed home/prize profile recorded above.

**Argive Muster Council — Death Korps of Krieg:** Strategos Damas commands hereditary PDF officers whose authority rests on muster warrants issued before the isolation. Their families kept Heraion’s depots intact while promised reinforcements failed to arrive; they regard the Paladins’ requisitions as another attempt to spend Argive lives elsewhere. Loyal to the Emperor, they oppose both Imperial Majors’ claims to local command. Damas fights from prepared barrack lines, with artillery and reserve armour drawn from mothballed stores.

**Soulstorm selection:** Death Korps of Krieg. Local siege infantry, artillery crews and depot armour represented by Krieg; muted khaki with dark red unit markings. These are Argive troops, not a regiment imported from Dessica.

|Holding|Tier / type|Controller|Defence|Logistics / infrastructure|Description|Map theme|
|---|---|---|---|---|---|
|Tiryns|Capital Planet|Iron Paladins|12/12|4 Supply + 4 Manpower; built-in shipyard|A fortress-monastery crowns a basalt escarpment above ironworks and densely inhabited workers’ terraces. Siege roads climb through successive gate courts; outside them, ore conveyors cross ash fields scarred by old artillery pits. The Paladins have restored the battered gatehouses and reopened the ironworks below the monastery.|Fortress or industrial city; steep approaches, broad breach lanes and enclosed courtyards.|
|Heraion|Standard Planet|Iron Paladins|4/4|2 Supply + 2 Manpower|Immense muster squares and munition warehouses surround the former tithe citadel, now held by the Iron Paladins. Restored barrack lines, fortified rail sidings and reinforced checkpoints secure the depots and approaches. The garrison maintains a heightened watch over the rebuilt positions, while soldiers' families fill the streets behind the defensive lines.|Urban barracks or military depot; streets, warehouse cover and open parade grounds.|
|Prosymna|Minor Planet|Iron Paladins|2/2|1 Supply + 1 Manpower|Dry uplands are divided into recruiting estates and grain stores. The Iron Paladins occupy the former levy camp, using its grounded troop transports as quarters. Repaired positions now guard the dusty roads between walled villages, cisterns and granaries, with sentries maintaining a strengthened defensive watch.|Arid rural settlement; low hills, scattered walls and a fortified central camp.|

|Fleet|Owner|Strength / original maximum|
|---|---|---|
|Vigilatius|Iron Paladins|5/5|



Map themes describe terrain, not verified map-pack titles. Choose a thematically suitable installed map with the required team capacity; use the existing overflow/raid procedure. Terrain descriptions grant no extra defence, construction or faction bonus.

### Eleusis

**Void Superiority:** Order of Saint Erigone 18 vs WAAAGH! Bell-Ringa 12 - Order of Saint Erigone superior; hostile fleet present.

The Order holds Erigone and Daeira. Bell-Ringa captured Triptolemos in Cycle 12 and reinforced its damaged defences. The Eleusinian Synod has lost its final holding and is eliminated as an independent campaign faction.

Setup: fixed home/prize profile recorded above.

**Eleusinian Synod — Witch Hunters:** Prelate Lysandra governs through competing shrine chapters, granary trusts and hospital superiors. These institutions sheltered pilgrims during isolation and refuse to surrender their levies to Althaia’s convent. Their hostility to the Paladins and the Order is a jurisdictional dispute; they remain Emperor-worshipping humans, not a Chaos cult or a second Sisters army. Militia companies defend sacred precincts while household guards provide a more reliable reserve.

**Soulstorm selection:** Witch Hunters. Shrine guards and religious enforcement troops represented by the Witch Hunters roster; cream cloth, red insignia and worn military equipment. They belong to the independent Synod, not Althaia’s Order.

|Holding|Tier / type|Controller|Defence|Logistics / infrastructure|Description|Map theme|
|---|---|---|---|---|---|
|Erigone|Capital Planet|Order of Saint Erigone|12/12|4 Supply + 4 Manpower; built-in shipyard|A shrine Capital of pale stone basilicas, processional avenues and fortified convent precincts. Hospitals and pilgrims’ dormitories fill the lower city beneath the Order’s blackened bell towers. Broad ceremonial approaches become exposed killing grounds between substantial masonry walls.|Cathedral city or shrine fortress; plazas, cloisters and defended avenues.|
|Triptolemos|Standard Planet|WAAAGH! Bell-Ringa|3/4|2 Supply + 2 Manpower|Hospitaller estates and cathedral granaries feed a crowded pilgrim population. Bell-Ringa’s mobs have seized the gatehouses between the terraced farms and walled ecclesiastical town from the Order. Orks reinforce the canal crossings with barricades and looted materials; battered positions now bear Goff trophies, while the cathedral granaries and surrounding estates lie under their guns.|Temperate shrine settlement; farmland, waterways and stone bridges.|
|Daeira|Minor Planet|Order of Saint Erigone|1/2|1 Supply + 1 Manpower|Funerary settlements cling to a cold limestone plateau. The Order now posts Sisters at the reliquary chapels and burial gates, overlooking the narrow roads between tomb fields. Former Synod positions shelter the occupiers while damaged defences await repair. Burial attendants and pilgrims pass beneath the Order's scrutiny on their way to the ossuary galleries.|Graveyard or ruined shrine; narrow passages, stone cover and bleak open ground.|

|Fleet|Owner|Strength / original maximum|
|---|---|---|
|The Unbroken Procession|Order of Saint Erigone|5/5|
|The Returning Escort|Order of Saint Erigone|5/5|
|The Oath at the Gate|Order of Saint Erigone|3/5|
|The Third Refusal|Order of Saint Erigone|5/5|
|Da Gate-Krasha|WAAAGH! Bell-Ringa|7/7|
|Da Fist|WAAAGH! Bell-Ringa|5/5|




Map themes describe terrain, not verified map-pack titles. Choose a thematically suitable installed map with the required team capacity; use the existing overflow/raid procedure. Terrain descriptions grant no extra defence, construction or faction bonus.

### Calydon

**Void Superiority:** WAAAGH! Bell-Ringa 5 vs hostile fleets 0 - WAAAGH! Bell-Ringa superior; no hostile fleet present.

The Orks hold all of Calydon: Da Bellworks, Olenos and newly captured Pleuron. The Calydonian Labour Defence has lost its final holding and is eliminated.

Setup: fixed home/prize profile recorded above.

**Calydonian Labour Defence — Renegade Guard:** Marshal Oineus was a foundry defence officer before the Capital fell. His committees now bind surviving work gangs, PDF remnants and displaced families into a precarious common command. They refuse outside command, fearing requisitions that strip the remaining evacuation routes of protection. Their soldiers know the factories and maintain a few serviceable armoured vehicles amid much improvised equipment.

**Soulstorm selection:** Renegade Guard. Industrial rebels, worker levies and salvaged armour; soot-grey fatigues and ochre identification bands. Accept either Vraksian or Tekarn AI branch; this proxy does not establish a Chaos Alignment or dictate every unit’s narrative identity.

|Holding|Tier / type|Controller|Defence|Logistics / infrastructure|Description|Map theme|
|---|---|---|---|---|---|
|Da Bellworks|Capital Planet|WAAAGH! Bell-Ringa|12/12|4 Supply + 4 Manpower; built-in shipyard|Looted cathedral foundries cover a soot-black plain. Bell-Ringa’s mobs have hung bells from gantries and welded checkered armour onto furnace halls; slag heaps and wrecked transporters form rough outer walls. The original human avenues survive beneath scrap barricades and assembly yards.|Ork-held industrial city; scrap piles, furnace buildings and broad vehicle approaches.|
|Pleuron|Standard Planet|WAAAGH! Bell-Ringa|3/4|2 Supply + 2 Manpower|Ork mobs occupy the factory districts along the elevated freight railway. Scrap-plated barricades and reinforced firing positions now guard the crossings over the drainage cuts, while Meks work through the looted machine shops. Bell-Ringa's garrison has strengthened the captured approaches, though wrecked machinery and shattered human strongpoints still scar the outer districts.|Industrial ruins; rail embankments, workshops and barricaded intersections.|
|Olenos|Minor Planet|WAAAGH! Bell-Ringa|1/2|1 Supply + 1 Manpower|Mining townships shelter beneath slag ridges on a wind-scoured plain. Bell-Ringa's mobs occupy the captured pithead compounds, piling scrap around their camps and hauling machinery toward Ork workshops. Stolen bells summon work gangs and fighters alike. Conveyor towers and disused quarry terraces overlook the battered evacuation yards and rudimentary Ork positions.|Quarry or ash wasteland; stepped pits, mining buildings and evacuation pads.|

|Fleet|Owner|Strength / original maximum|
|---|---|---|
|Da Backhand|WAAAGH! Bell-Ringa|5/5|




Map themes describe terrain, not verified map-pack titles. Choose a thematically suitable installed map with the required team capacity; use the existing overflow/raid procedure. Terrain descriptions grant no extra defence, construction or faction bonus.

### Aulis

**Void Superiority:** Iron Paladins 10 vs Aulis Anchorage Command 3 - Iron Paladins superior; hostile fleet present.

Embarkation yards, troop-marshalling settlements and stranded naval administration.

Setup: d20 **5**; ownership authored separately.

**Aulis Anchorage Command — Imperial Guard:** Commodore Thestor has preserved a fragment of the Imperial Navy’s embarkation administration rather than declaring a personal kingdom. His officers still inspect troop transports for assignments whose destinations may no longer exist. Armsmen, shore regiments and support personnel hold the landing fields; Thestor refuses incoming claims of authority and orders his ships to challenge any force attempting to seize the anchorages.

**Soulstorm selection:** Imperial Guard. Naval shore troops and armsmen represented by Guard infantry and vehicles; navy blue and bone-white markings.

|Holding|Tier / type|Controller|Defence|Logistics / infrastructure|Description|Map theme|
|---|---|---|---|---|---|
|Schoenus|Minor Planet|Iron Paladins|2/2|1 Supply + 1 Manpower|A coastal supply world of fuel farms, barracks and disused embarkation beaches. Concrete causeways cross tidal flats to cargo piers; inland storage compounds still carry destination markings for vanished crusades. The Anchorage Command’s shore troops put up worthy resistance before the Iron Paladins overwhelmed their positions. Paladin sentries now hold the pump stations and transport terminals; repaired coastal defences guard the causeways and cargo piers.|Coastal military depot; low terrain, causeways and fuel-storage compounds.|
|Hyria|Major Planet|Aulis Anchorage Command|5/8|3 Supply + 3 Manpower|A heavily developed naval support world whose cities grew around surface landing fields. The Iron Paladins have broken through outer districts, driving Anchorage troops from alleyways and concealed positions among repair sheds and Administratum blocks. Damaged streets and breached defences mark their advance, but the Command retains the armoured traffic-control citadel and control of Hyria.|Spaceport or military-industrial city; hangars, long landing strips and a hardened central complex.|

|Fleet|Owner|Strength / original maximum|
|---|---|---|
|The Unanswered Muster|Aulis Anchorage Command|3/5|
|Crusade Fleet Anabasis|Iron Paladins|5/5|
|The Emperor’s Judgement|Iron Paladins|5/5|



Map themes describe terrain, not verified map-pack titles. Choose a thematically suitable installed map with the required team capacity; use the existing overflow/raid procedure. Terrain descriptions grant no extra defence, construction or faction bonus.

### Mycenae

**Void Superiority:** House Atreides 18 vs hostile fleets 0 - House Atreides superior; no hostile fleet present.

The prize dynasty holds a fortified seat, military estates and an orbital anchorage.

Setup: fixed home/prize profile recorded above.

**House Atreides — Vostroyan Firstborn:** Archon Pleisthenes Atreides is the hereditary Imperial governor of Perseia and master of a household compact binding Dendra’s estates to Lion Gate. The dynasty won loyalty by sheltering refugee crews and honouring old service pensions; it also enforces hereditary labour dues and executes breaches of the tithe oath. Its sea-cliff court maintains sanctioned confessors, Administratum assessors and an exacting household officer corps. Pleisthenes claims an old emergency commission gives him responsibility for Mycenae and refuses the competing authority of both Imperial Majors. His disciplined regiments and substantial flotilla make that claim expensive to challenge. Green livery, a copper hawk clutching an Imperial aquila, maritime ancestry and cultivated public duty provide the deliberate Dune homage; the people, history and conflict are native to this campaign. There is no spice monopoly, prescient heir or imported Dune political system.

**Soulstorm selection:** Vostroyan Firstborn. Hereditary household regiments with heirloom weapons and heavy infantry; deep green uniforms, charcoal armour and copper heraldry. Vostroyan models represent local troops rather than a visiting Vostroyan regiment.

|Holding|Tier / type|Controller|Defence|Logistics / infrastructure|Description|Map theme|
|---|---|---|---|---|---|
|Perseia|Major Planet|House Atreides|8/8|3 Supply + 3 Manpower|The dynasty’s seat is a storm-lashed ocean world with inhabited mountain islands. Black coastal bastions guard terraced cities and reservoir tunnels; the ruling household keeps its court above a harbour cut into volcanic rock. Sea approaches, cliff roads and sheltered dock basins determine where an invader can land.|Coastal fortress or wet mountain city; cliffs, bridges, stone bastions and harbour approaches.|
|Dendra|Standard Planet|House Atreides|4/4|2 Supply + 2 Manpower|A temperate estate world supplying the household regiments with food and recruits. Old orchards surround fortified manor towns, while oath-halls and vehicle barns stand along the military roads. The orderly estates conceal hard distinctions between protected tenants and hereditary labour obligations.|Wooded agricultural settlement; hedges, orchards, estate walls and open fields for armour.|
|Lion Gate|Standard Station|House Atreides|4/4|2 Supply + 2 Manpower|An orbital customs bastion built around a broad freight spine. Armoured inspection halls open into stacked cargo vaults; household armsmen guard the pressure doors leading to the fleet anchorage. Its carved heraldic beasts are devotional ornament, not xenos technology.|Station or ship-interior map; cargo halls, bulkhead chokepoints and docking galleries.|

|Fleet|Owner|Strength / original maximum|
|---|---|---|
|Pleisthenes’ Oath|House Atreides|5/5|
|The Copper Hawk|House Atreides|5/5|
|Perseia’s Breakwater|House Atreides|5/5|
|The Dendra Covenant|House Atreides|3/3|



Map themes describe terrain, not verified map-pack titles. Choose a thematically suitable installed map with the required team capacity; use the existing overflow/raid procedure. Terrain descriptions grant no extra defence, construction or faction bonus.

### Delphi

**Void Superiority:** No fleets present (0 vs 0); no faction has Void Superiority.

Astropathic facilities, signal stations and archives whose messages no longer agree.

Setup: d20 **17**; ownership authored separately.

**Delphic Custodians — Witch Hunters:** Logothete Manto leads hereditary archive wardens and the security staff serving Delphi’s astropathic establishments. Contradictory orders have become dangerous currency: commanders seek whichever sealed transcript favours their claim. Manto keeps the custodial oath above these disputes and defends vaults against the Lotus privateers, while refusing outside claims on her archives. Her soldiers are human guards, not Adeptus Custodes despite their title.

**Soulstorm selection:** Witch Hunters. Archive wardens and armoured enforcers represented by the Witch Hunters roster; ash-blue cloth, brass seals and ivory unit plates. Their title does not make them Adeptus Custodes.

**Lotus Company — Praetorian Guard:** Captain Eurylochos commands human deserters, smugglers, hired gun crews and Ork mercenaries from Castalia’s abandoned waterworks. His company presents expired letters of marque when useful and burns the records when they are not. It raids Delphi’s lighter traffic and avoids a decisive engagement with Manto’s stronger patrols. The company has no Alignment and remains hostile, with no established pact or Chaos allegiance.

**Soulstorm selection:** Praetorian Guard. Human privateers, hired Ork muscle and looted vehicles using the Praetorian roster; mismatched armour and faded violet patches. Its mercenary options fit the company’s mixed crews.

|Holding|Tier / type|Controller|Defence|Logistics / infrastructure|Description|Map theme|
|---|---|---|---|---|---|
|Castalia|Minor Planet|Order of Saint Erigone|2/2|1 Supply + 1 Manpower|The Order of Saint Erigone occupies the dry basin city around Castalia's abandoned water-processing plant. Sisters guard repaired landing approaches and the reservoir compounds seized from the Lotus Company, while patrols search the rock gullies beyond the settlement. Cargo yards have been secured and work has begun on an orbital anchorage above the captured world.|Arid spaceport or outlaw settlement; gullies, cargo cover and refinery ruins.|
|Corycia|Minor Planet|Order of Saint Erigone|1/2|1 Supply + 1 Manpower|The Order of Saint Erigone holds Corycia's cavern archive entrances and the lift terminals above its mist-filled ravines. Sisters establish battered bridgeheads among the monastic service towns, securing paths to the sealed repositories. Damaged cable stations and breached positions mark the assault; Pytho has also fallen to the Order, ending the Delphic Custodians’ territorial resistance.|Mountain stronghold; ravines, bridges, tunnels or narrow rocky approaches.|
|Pytho|Standard Planet|Order of Saint Erigone|1/4|2 Supply + 2 Manpower|A civilised world of signal towers, scribal districts and crowded transmission courts. The Order of Saint Erigone has taken the astropathic precinct and inner archives after overcoming the Custodians’ final resistance. Sisters hold the breached courtyards beneath damaged antenna towers; battered barricades and clerks’ tenements mark the route of the assault. The new garrison occupies defences still in need of restoration.|Dense Imperial city; plazas, administrative blocks and communications installations.|
|Omphalos Relay|Minor Station|Order of Saint Erigone|1/2|1 Supply + 1 Manpower|An orbital relay station whose rotating habitation rings surround a hardened signal core. Sisters of the Order of Saint Erigone hold the breached transit hubs and message vaults, establishing a garrison amid damaged bulkheads and machinery. The Custodians’ fleet has been destroyed and their final holding at Pytho has fallen; the Order now controls every holding in Delphi.|Station interior; compact junctions, machinery chambers and enclosed service corridors.|

|Fleet|Owner|Strength / original maximum|
|---|---|---|




Map themes describe terrain, not verified map-pack titles. Choose a thematically suitable installed map with the required team capacity; use the existing overflow/raid procedure. Terrain descriptions grant no extra defence, construction or faction bonus.

### Nemea

**Void Superiority:** Nemean Estate Compact 5 vs hostile fleets 0 - Nemean Estate Compact superior; no hostile fleet present.

Agricultural estates and hunting preserves once bound to the crusade provisioning system.

Setup: d20 **13**; ownership authored separately.

**Nemean Estate Compact — Praetorian Guard:** Warden Adrastos chairs a compact of landowners whose privileges depend on keeping crusade provisioning quotas. Isolation has let them retain more of the harvest, but loss of convoy protection has made those stores vulnerable. Estate riflemen, rural PDF and armoured agricultural security protect the processing towns. The Compact refuses outside authority and guards its harvest against requisition by any would-be protector.

**Soulstorm selection:** Praetorian Guard. Estate riflemen, regular household companies, mortar crews and hired auxiliaries; ochre cloth and dark green plates. The full Praetorian roster is permitted, including its mercenary options.

|Holding|Tier / type|Controller|Defence|Logistics / infrastructure|Description|Map theme|
|---|---|---|---|---|---|
|Cleonae|Minor Planet|Nemean Estate Compact|2/2|1 Supply + 1 Manpower|Grain-producing plains are broken by silo towns and irrigation cuts. Estate militia drill beside threshing sheds, and old redoubts overlook the bridges used by tithe convoys. Harvest stubble leaves little shelter outside the settlements.|Open farmland; irrigation channels, scattered villages and grain depots.|
|Phlius|Minor Planet|Nemean Estate Compact|2/2|1 Supply + 1 Manpower|Hill country supports vineyards, livestock estates and fortified market towns. Stone retaining walls divide narrow tracks climbing toward hilltop manor compounds. The Compact’s patrols know the gullies through which smugglers bypass its requisition stations.|Hilly rural map; stone walls, winding approaches and isolated compounds.|
|Apesas|Major Planet|Nemean Estate Compact|8/8|3 Supply + 3 Manpower|A populous agricultural processing world dominated by canneries, grain elevators and immense livestock yards. Its governing estates maintain walled pleasure preserves beside crowded industrial towns. Rail hubs and food warehouses are more strategically valuable than the ceremonial hunting lodges.|Agri-industrial city; rail yards, factories and wooded estate margins.|

|Fleet|Owner|Strength / original maximum|
|---|---|---|
|The Granary Key|Nemean Estate Compact|5/5|




Map themes describe terrain, not verified map-pack titles. Choose a thematically suitable installed map with the required team capacity; use the existing overflow/raid procedure. Terrain descriptions grant no extra defence, construction or faction bonus.

### Lerna

**Void Superiority:** Lerna Reclamation Directorate 3 vs Rustjaw Mob 2 - Lerna Reclamation Directorate superior; hostile fleet present.

Wet industrial worlds and chemical works separated by contaminated waterways.

Setup: d20 **12**; ownership authored separately.

**Lerna Reclamation Directorate — Adeptus Mechanicus Explorators:** Magister Polydoros administers the pumps, chemical plants and purification crews keeping Pontinos habitable. His civic administration depends on hereditary technical guilds, augmented engineers and machine-tending crews whose survival is tied to the reclamation works. Plant security and PDF survivors contest the system with Rustjaw’s Orks, trying to preserve works they cannot afford to demolish. He rejects outside command and treats approaching forces as a threat to the settled islands.

**Soulstorm selection:** Adeptus Mechanicus Explorators. Augmented plant guards, engineer cadres and reclamation machines represented by Mechanicus Explorators; slate armour with pale hazard markings. The Directorate remains a locally governed technical power.

**Rustjaw Mob — Orks:** Boss Skrag Rustjaw earned his name biting through a seized pump-station gate after his breaching charges failed. His mob hoards pipes, tankers and stolen engines, turning Amymone’s chemical yards into ramshackle vehicle shops. Rustjaw regards Bell-Ringa as another rival boss: he has neither surrendered his mob nor promised its ships. Their enemy in Lerna is the human Directorate.

**Soulstorm selection:** Orks. Boyz, Nobz and ramshackle vehicle mobs; rust-red plates, black checks and trophies made from industrial scrap.

|Holding|Tier / type|Controller|Defence|Logistics / infrastructure|Description|Map theme|
|---|---|---|---|---|---|
|Amymone|Standard Planet|Rustjaw Mob|4/4|2 Supply + 2 Manpower|The Rustjaw Mob has seized a chain of chemical plants amid reed-choked wetlands. Ork workshops occupy corroded tank farms; leaking pipes and welded scrap bridges connect islands of relatively firm ground. Polluted pools and collapsed process towers split the approaches into uneven lanes.|Toxic swamp or ruined refinery; water barriers, pipework and raised causeways.|
|Pontinos|Standard Planet|Lerna Reclamation Directorate|4/4|2 Supply + 2 Manpower|Habitable islands rise above a poisonous floodplain, each crowded with pump houses and worker settlements. Directorate troops guard levees linking reclamation plants to the principal town. Deliberate drainage keeps the roads usable, but the outer industrial zones are half submerged.|Flooded industrial terrain; levees, pumps, narrow crossings and low settlement blocks.|
|Alcyonian Dock|Minor Station|Lerna Reclamation Directorate|2/2|1 Supply + 1 Manpower|A compact orbital transfer station handling sealed chemical cargoes. Pressure-separated tank galleries surround a central customs hall and tug-control deck. Security troops favour the short approaches between freight lifts and docking collars.|Station cargo terminal; enclosed halls, machinery and short bulkhead chokepoints.|

|Fleet|Owner|Strength / original maximum|
|---|---|---|
|The Ninth Sluice|Lerna Reclamation Directorate|3/3|
|Da Pressure Drop|Rustjaw Mob|2/2|



Map themes describe terrain, not verified map-pack titles. Choose a thematically suitable installed map with the required team capacity; use the existing overflow/raid procedure. Terrain descriptions grant no extra defence, construction or faction bonus.

### Ithaca

**Void Superiority:** Ithacan Assembly 5 vs hostile fleets 0 - Ithacan Assembly superior; no hostile fleet present.

Resettlement worlds of displaced families, veterans and descendants of missing crews.

Setup: d20 **17**; ownership authored separately.

**Ithacan Assembly — Imperial Guard:** Speaker Eumaia speaks for settlement councils founded by stranded convoy families and demobilised soldiers. The Assembly’s officers have fought under too many absent patrons to confuse grand titles with reliable relief. Veteran-led militia protects the new towns and their reception station; the Assembly refuses to submit to the Paladins or the Order, despite the population’s continued Emperor worship. Its main fear is becoming another recruiting ground whose protectors never return.

**Soulstorm selection:** Imperial Guard. Veteran-led colonial PDF and resettlement militia; weathered blue-grey and white settlement badges.

|Holding|Tier / type|Controller|Defence|Logistics / infrastructure|Description|Map theme|
|---|---|---|---|---|---|
|Neriton|Minor Planet|Ithacan Assembly|2/2|1 Supply + 1 Manpower|Wooded highlands shelter settlements founded by retired soldiers and stranded crew families. Timber stockades have gradually acquired ferrocrete bunkers, while narrow roads climb through abandoned extraction sites. The veterans favour prepared village approaches over exposing their homes in open battle.|Forested hills; dispersed settlements, tracks and rough defensive works.|
|Eumaia’s Rest|Minor Planet|Ithacan Assembly|2/2|1 Supply + 1 Manpower|A quiet resettlement world of low houses, communal workshops and memorial gardens. The oldest transport hulls remain embedded in the original landing field and now serve as clinics and meeting halls. Assembly militia drill beyond irrigated fields rather than among the crowded homes.|Rural colony; low buildings, fields and a central landing-ground settlement.|
|Same|Standard Planet|Ithacan Assembly|4/4|2 Supply + 2 Manpower|The Assembly’s principal industrial and administrative world is a patchwork of rebuilt cities. Repair yards reuse machinery from scores of refugee vessels; elected delegates meet in a former naval victualling hall. Broad service roads connect workshops to dense residential quarters.|Rebuilt urban or industrial colony; workshops, wide roads and inhabited districts.|
|Return Anchorage|Minor Station|Ithacan Assembly|2/2|1 Supply + 1 Manpower|An orbital reception station expanded with salvaged habitation modules. Customs lines, quarantine wards and crowded arrival concourses flank the freight spine. Former naval personnel maintain a disciplined watch around the docking control rooms.|Orbital terminal or ship interior; concourses, cargo bays and narrow connecting passages.|

|Fleet|Owner|Strength / original maximum|
|---|---|---|
|A Place at the Hearth|Ithacan Assembly|5/5|



Map themes describe terrain, not verified map-pack titles. Choose a thematically suitable installed map with the required team capacity; use the existing overflow/raid procedure. Terrain descriptions grant no extra defence, construction or faction bonus.

### Thessaly

**Void Superiority:** Thessalian First Command 3 vs Thessalian Remount Command 2 - Thessalian First Command superior; hostile fleet present.

Military estates, vehicle depots and open-country settlements divided between surviving commands.

Setup: d20 **16**; ownership authored separately.

**Thessalian First Command — Steel Legion:** General Leontes possesses the senior surviving regimental commission and treats Pharsalos’s armoured depots as the centre of a future restored army. He resents Colonel Phereas keeping transport assets under a separate seal, yet neither command has opened hostilities against the other. Their separate fleets count as hostile for Void Superiority; neither command has recognised the other’s authority. First Command favours disciplined infantry supported by well-maintained armour.

**Soulstorm selection:** Steel Legion. Mechanised infantry and armoured depot reserves; deep red insignia on sand-grey armour. Both Steel Legion branches are valid representations; an AI tank preference is not guaranteed.

**Thessalian Remount Command — Vostroyan Firstborn:** Colonel Phereas commands the officers, mechanics and rural levies responsible for keeping Thessaly’s scattered forces mobile. He argues that Leontes’s seniority does not cancel his independent transport commission. The rival commissions now reject each other’s authority and treat each other’s armed forces as hostile; no battle has yet been resolved. Remount troops defend the depots and coastal loading grounds that support their small fleet.

**Soulstorm selection:** Vostroyan Firstborn. Remount-service troops, cavalry traditions and workshop escorts represented by Vostroyans; dun uniforms and dark blue vehicle panels.

|Holding|Tier / type|Controller|Defence|Logistics / infrastructure|Description|Map theme|
|---|---|---|---|---|---|
|Pherae|Minor Planet|Thessalian Remount Command|2/2|1 Supply + 1 Manpower|Open steppe surrounds cavalry breeding estates and vehicle remount compounds. The Remount Command occupies low fortresses beside watering stations, maintaining both draft animals and battered military haulers. Trenches interrupt the roads between otherwise widely separated settlements.|Grassland or steppe; open manoeuvre space, low forts and scattered compounds.|
|Pagasae|Minor Planet|Thessalian Remount Command|2/2|1 Supply + 1 Manpower|A wind-beaten embarkation world with transport pens and coastal freight towns. Abandoned troop-loading ramps rise over tidal marshes; Colonel Phereas keeps his workshops dispersed to avoid losing them in one raid. Raised roads connect the depots.|Coastal depot; marshes, ramps, causeways and dispersed industrial sheds.|
|Pelion|Minor Planet|Thessalian First Command|2/2|1 Supply + 1 Manpower|Mountain training estates overlook deep wooded valleys. First Command recruits march between ridge camps, artillery observation posts and enclosed supply yards. Heavy vehicles follow a handful of engineered switchback roads through the passes.|Mountain or forest military map; ridges, restricted passes and camp clearings.|
|Pharsalos|Standard Planet|Thessalian First Command|4/4|2 Supply + 2 Manpower|A broad continental plain carries the First Command’s principal armoured depots. Regimental towns cluster around repair factories and concrete dispersal yards; earthworks cover the major road junctions. Its officers favour keeping approach fields clear enough for long-range fire.|Open military-industrial plain; tank yards, road junctions and long firing lanes.|

|Fleet|Owner|Strength / original maximum|
|---|---|---|
|The Senior Warrant|Thessalian First Command|3/3|
|The Unbroken Trace|Thessalian Remount Command|2/2|



Map themes describe terrain, not verified map-pack titles. Choose a thematically suitable installed map with the required team capacity; use the existing overflow/raid procedure. Terrain descriptions grant no extra defence, construction or faction bonus.

## Minor faction register

Minor resources below are **derived defence values**, not spendable Major stockpiles. Ordinary fleet allocation is ceil(total maximum holding defence / 2); the prize uses the full sum. Partial final fleets keep their original setup maximum. No automatic rebuild follows a lost holding. No Minor has a faction trait.

|Minor|Leader|Holdings|Fleet allocation|Derived Supply / Manpower|
|---|---|---|---|---|
|Argive Muster Council|Strategos Damas|None; eliminated in Cycle 5|None; The Unspent Levy destroyed at Heraion|0 / 0; eliminated|
|Eleusinian Synod|Prelate Lysandra|None; eliminated in Cycle 4|None; fleet destroyed in Cycle 2 Warp Storm|0 / 0; eliminated|
|Calydonian Labour Defence|Marshal Oineus|None; eliminated in Cycle 6|None; fleet destroyed in Cycle 2 Warp Storm|0 / 0; eliminated|
|Aulis Anchorage Command|Commodore Thestor|Hyria|3/5 surviving|15 / 15|
|House Atreides (prize)|Archon Pleisthenes Atreides|Perseia, Dendra, Lion Gate|5/5, 5/5, 5/5, 3/3 surviving|70 / 70|
|Delphic Custodians|Logothete Manto|None; eliminated in Cycle 12|None; The Sealed Testimony destroyed in Cycle 9|0 / 0; eliminated|
|Lotus Company|Captain Eurylochos|None; eliminated in Cycle 7|None; fleet destroyed in Cycle 2 Warp Storm|0 / 0; eliminated|
|Nemean Estate Compact|Warden Adrastos|Cleonae, Phlius, Apesas|5/5 surviving|25 / 25|
|Lerna Reclamation Directorate|Magister Polydoros|Pontinos, Alcyonian Dock|3/3 surviving|15 / 15|
|Rustjaw Mob|Boss Skrag Rustjaw|Amymone|2/2 surviving|10 / 10|
|Ithacan Assembly|Speaker Eumaia|Neriton, Eumaia’s Rest, Same, Return Anchorage|5/5 surviving|25 / 25|
|Thessalian First Command|General Leontes|Pelion, Pharsalos|3/3 surviving|15 / 15|
|Thessalian Remount Command|Colonel Phereas|Pherae, Pagasae|2/2 surviving|10 / 10|



### Argive Muster Council

Strategos Damas commands hereditary PDF officers whose authority rests on muster warrants issued before the isolation. Their families kept Heraion’s depots intact while promised reinforcements failed to arrive; they regard the Paladins’ requisitions as another attempt to spend Argive lives elsewhere. Loyal to the Emperor, they oppose both Imperial Majors’ claims to local command. Damas fights from prepared barrack lines, with artillery and reserve armour drawn from mothballed stores.

**Soulstorm selection:** Death Korps of Krieg. Local siege infantry, artillery crews and depot armour represented by Krieg; muted khaki with dark red unit markings. These are Argive troops, not a regiment imported from Dessica.

### Eleusinian Synod

Prelate Lysandra governs through competing shrine chapters, granary trusts and hospital superiors. These institutions sheltered pilgrims during isolation and refuse to surrender their levies to Althaia’s convent. Their hostility to the Paladins and the Order is a jurisdictional dispute; they remain Emperor-worshipping humans, not a Chaos cult or a second Sisters army. Militia companies defend sacred precincts while household guards provide a more reliable reserve.

**Soulstorm selection:** Witch Hunters. Shrine guards and religious enforcement troops represented by the Witch Hunters roster; cream cloth, red insignia and worn military equipment. They belong to the independent Synod, not Althaia’s Order.

### Calydonian Labour Defence

Marshal Oineus was a foundry defence officer before the Capital fell. His committees now bind surviving work gangs, PDF remnants and displaced families into a precarious common command. They refuse outside command, fearing requisitions that strip the remaining evacuation routes of protection. Their soldiers know the factories and maintain a few serviceable armoured vehicles amid much improvised equipment.

**Soulstorm selection:** Renegade Guard. Industrial rebels, worker levies and salvaged armour; soot-grey fatigues and ochre identification bands. Accept either Vraksian or Tekarn AI branch; this proxy does not establish a Chaos Alignment or dictate every unit’s narrative identity.

### Aulis Anchorage Command

Commodore Thestor has preserved a fragment of the Imperial Navy’s embarkation administration rather than declaring a personal kingdom. His officers still inspect troop transports for assignments whose destinations may no longer exist. Armsmen, shore regiments and support personnel hold the landing fields; Thestor refuses incoming claims of authority and orders his ships to challenge any force attempting to seize the anchorages.

**Soulstorm selection:** Imperial Guard. Naval shore troops and armsmen represented by Guard infantry and vehicles; navy blue and bone-white markings.

### House Atreides

Archon Pleisthenes Atreides is the hereditary Imperial governor of Perseia and master of a household compact binding Dendra’s estates to Lion Gate. The dynasty won loyalty by sheltering refugee crews and honouring old service pensions; it also enforces hereditary labour dues and executes breaches of the tithe oath. Its sea-cliff court maintains sanctioned confessors, Administratum assessors and an exacting household officer corps. Pleisthenes claims an old emergency commission gives him responsibility for Mycenae and refuses the competing authority of both Imperial Majors. His disciplined regiments and substantial flotilla make that claim expensive to challenge. Green livery, a copper hawk clutching an Imperial aquila, maritime ancestry and cultivated public duty provide the deliberate Dune homage; the people, history and conflict are native to this campaign. There is no spice monopoly, prescient heir or imported Dune political system.

**Soulstorm selection:** Vostroyan Firstborn. Hereditary household regiments with heirloom weapons and heavy infantry; deep green uniforms, charcoal armour and copper heraldry. Vostroyan models represent local troops rather than a visiting Vostroyan regiment.

### Delphic Custodians

Logothete Manto leads hereditary archive wardens and the security staff serving Delphi’s astropathic establishments. Contradictory orders have become dangerous currency: commanders seek whichever sealed transcript favours their claim. Manto keeps the custodial oath above these disputes and defends vaults against the Lotus privateers, while refusing outside claims on her archives. Her soldiers are human guards, not Adeptus Custodes despite their title.

**Soulstorm selection:** Witch Hunters. Archive wardens and armoured enforcers represented by the Witch Hunters roster; ash-blue cloth, brass seals and ivory unit plates. Their title does not make them Adeptus Custodes.

### Lotus Company

Captain Eurylochos commands human deserters, smugglers, hired gun crews and Ork mercenaries from Castalia’s abandoned waterworks. His company presents expired letters of marque when useful and burns the records when they are not. It raids Delphi’s lighter traffic and avoids a decisive engagement with Manto’s stronger patrols. The company has no Alignment and remains hostile, with no established pact or Chaos allegiance.

**Soulstorm selection:** Praetorian Guard. Human privateers, hired Ork muscle and looted vehicles using the Praetorian roster; mismatched armour and faded violet patches. Its mercenary options fit the company’s mixed crews.

### Nemean Estate Compact

Warden Adrastos chairs a compact of landowners whose privileges depend on keeping crusade provisioning quotas. Isolation has let them retain more of the harvest, but loss of convoy protection has made those stores vulnerable. Estate riflemen, rural PDF and armoured agricultural security protect the processing towns. The Compact refuses outside authority and guards its harvest against requisition by any would-be protector.

**Soulstorm selection:** Praetorian Guard. Estate riflemen, regular household companies, mortar crews and hired auxiliaries; ochre cloth and dark green plates. The full Praetorian roster is permitted, including its mercenary options.

### Lerna Reclamation Directorate

Magister Polydoros administers the pumps, chemical plants and purification crews keeping Pontinos habitable. His civic administration depends on hereditary technical guilds, augmented engineers and machine-tending crews whose survival is tied to the reclamation works. Plant security and PDF survivors contest the system with Rustjaw’s Orks, trying to preserve works they cannot afford to demolish. He rejects outside command and treats approaching forces as a threat to the settled islands.

**Soulstorm selection:** Adeptus Mechanicus Explorators. Augmented plant guards, engineer cadres and reclamation machines represented by Mechanicus Explorators; slate armour with pale hazard markings. The Directorate remains a locally governed technical power.

### Rustjaw Mob

Boss Skrag Rustjaw earned his name biting through a seized pump-station gate after his breaching charges failed. His mob hoards pipes, tankers and stolen engines, turning Amymone’s chemical yards into ramshackle vehicle shops. Rustjaw regards Bell-Ringa as another rival boss: he has neither surrendered his mob nor promised its ships. Their enemy in Lerna is the human Directorate.

**Soulstorm selection:** Orks. Boyz, Nobz and ramshackle vehicle mobs; rust-red plates, black checks and trophies made from industrial scrap.

### Ithacan Assembly

Speaker Eumaia speaks for settlement councils founded by stranded convoy families and demobilised soldiers. The Assembly’s officers have fought under too many absent patrons to confuse grand titles with reliable relief. Veteran-led militia protects the new towns and their reception station; the Assembly refuses to submit to the Paladins or the Order, despite the population’s continued Emperor worship. Its main fear is becoming another recruiting ground whose protectors never return.

**Soulstorm selection:** Imperial Guard. Veteran-led colonial PDF and resettlement militia; weathered blue-grey and white settlement badges.

### Thessalian First Command

General Leontes possesses the senior surviving regimental commission and treats Pharsalos’s armoured depots as the centre of a future restored army. He resents Colonel Phereas keeping transport assets under a separate seal, yet neither command has opened hostilities against the other. Their separate fleets count as hostile for Void Superiority; neither command has recognised the other’s authority. First Command favours disciplined infantry supported by well-maintained armour.

**Soulstorm selection:** Steel Legion. Mechanised infantry and armoured depot reserves; deep red insignia on sand-grey armour. Both Steel Legion branches are valid representations; an AI tank preference is not guaranteed.

### Thessalian Remount Command

Colonel Phereas commands the officers, mechanics and rural levies responsible for keeping Thessaly’s scattered forces mobile. He argues that Leontes’s seniority does not cancel his independent transport commission. The rival commissions now reject each other’s authority and treat each other’s armed forces as hostile; no battle has yet been resolved. Remount troops defend the depots and coastal loading grounds that support their small fleet.

**Soulstorm selection:** Vostroyan Firstborn. Remount-service troops, cavalry traditions and workshop escorts represented by Vostroyans; dun uniforms and dark blue vehicle panels.

## Minor force representation

Each Minor has an explicit Soulstorm selection in its system dossier and faction register. The thirteen Minors now use nine roster selections, including Krieg, Witch Hunters, Renegade Guard, Vostroyans, Praetorians, Mechanicus Explorators and Steel Legion alongside Guard and Orks. These are full gameplay rosters representing local forces, not just uniform changes. All Minors remain independent hostile powers without Alignment or diplomatic agreements.

Use the full selected roster; narrative preferences do not force an AI branch or prohibit its units. These selections add no meta-campaign traits or construction bonuses. Consult the [Unification roster reference](Unification_Roster_Reference_2026-10-07.md) for available armies, source links and optional-content distinctions. Record the actual installed menu selection and enabled options with each player battle.

## Construction register

No purchased, unfinished or upgraded projects at setup. Tiryns, Da Bellworks and Erigone have their inherent established-Capital shipyards. Perseia has no built-in shipyard: it is a Major world, not a Capital. The three Capital yards have no construction Integrity track or slot cost and are destroyed on Capital fall under the source rules.

|Faction|Project|Type / location|Progress / Integrity|Effect / status|
|---|---|---|---|---|
|Iron Paladins|The Grand Forge of Iron|Upgraded Major Forge Complex / Tiryns, Argos|Upgrade progress 5/5; Integrity 10/10|Upgrade complete and active at full Integrity. +14 Supply per Logistics Cycle; no immediate payout. Tiryns construction slot occupied.|
|WAAAGH! Bell-Ringa|Da Iron Gob|Upgraded Major Forge Complex / Da Bellworks, Calydon|Upgrade progress 3/5; Integrity 8/10|Base complete and active: +7 Supply per Logistics Cycle while Integrity remains at least 5. Upgrade unfinished; +14 Supply per Logistics Cycle at full upgraded Integrity. Da Bellworks construction slot occupied.|
|Order of Saint Erigone|The Vigil of the Three Refusals|Major Military Academy / Erigone, Eleusis|Progress 5/5; Integrity 5/5|Complete and active at full Integrity. +7 Manpower per Logistics Cycle. Erigone construction slot occupied.|
|WAAAGH! Bell-Ringa|Da Jaw-Breaka|Minor Fleet Construction / Da Gate-Krasha, Eleusis|Progress 3/3; Integrity 3/3|Complete. Grants +2 permanent current and maximum Fleet Strength; Da Gate-Krasha is 7/7 (base 5 plus 2 from Da Jaw-Breaka). Granted capacity remains until the fleet is destroyed.|
|Order of Saint Erigone|Castalia Anchorage|Minor Orbital Shipyard / Castalia, Delphi|Progress 3/3; Integrity 3/3|Complete and operational. Orbital Shipyard available in Delphi. Castalia ordinary construction slot occupied.|
|Order of Saint Erigone|The Breach Litany|Minor Bombardment Bay / The Third Refusal, Eleusis|Progress 3/3; Integrity 3/3|Complete and active. Grants +1 Ground Assault damage for subsequent eligible assaults.|
|Iron Paladins|Gene-Seed Vaults|Major Military Academy / Heraion, Argos|Progress 3/5; Integrity 3/5|Unfinished and inactive. +7 Manpower per Logistics Cycle when complete at full Integrity. Heraion ordinary construction slot occupied.|
|Order of Saint Erigone|The Watch of Daeira|Minor System Defence Platform / Eleusis|Progress 1/3; Integrity 1/3|Unfinished and inactive. Completion grants +5 to the defender’s Fleet Battle roll in Eleusis.|

## Setup provenance and decision ledger

**9 October 2026 correction:** Minor Factions cannot have Capital-tier holdings. Perseia is corrected to Major 8/8 and Lion Gate to Standard Station 4/4; Dendra stays Standard 4/4. Perseia has no inherent Capital shipyard. House Atreides retains its existing fleets and prize-resource multiplier; its total holding tiers remain 7, so derived resources remain 70 Supply / 70 Manpower. This holding-tier correction does not retroactively rerun battles or fleet recovery.

The 6 October thematic roster, Major identities, Capitals, deputies and hostility concept were approved by Jake. The 7 October documentation task supplies the remaining authored setup: equal 5/5 starts, turn order, local holding names and ownership, the fixed Mycenae profile and Nail-Takers raider. These are declared setup choices, not historical campaign outcomes or random ownership results.


|System|d20 result|Reroll|
|---|---|---|
|Aulis|5|None|
|Delphi|17|None|
|Nemea|13|None|
|Lerna|12|None|
|Ithaca|17|None|
|Thessaly|16|None|

The saved machine-readable roll record is [Atreus_Setup_Rolls_2026-10-07.json](Atreus_Setup_Rolls_2026-10-07.json). The Cycle 1 event check is recorded separately in the Cycle ledger. The system directory’s order does not encode movement restrictions. Planet/station type follows the roll; lore does not add holdings.


## Cycle ledger

| Cycle / phase | Orders | Costs | Outcome | Pending |
|---|---|---|---|---|
| 1 / Phase 0 | Construction effects → Logistics check → event check | None | No eligible periodic effects; Logistics not due; d6 = 3, no event. All starting values unchanged. [Saved roll](Atreus_Cycle_01_Phase_0_Rolls.json). | Iron Paladins orders |
| 1 / Iron Paladins / Fleet | Crusade Fleet Anabasis holds position; no assault | None | Remains 5/5 in Argos; Fleet Action unused. | None |
| 1 / Iron Paladins / Faction | Reinforce through The Iron Tithe | None | +8 Supply: 20 to 28. Manpower remains 20. | None |
| 1 / Iron Paladins / Social | No action | None | No Communique. | None |
| 1 / Iron Paladins / Construction | Begin The Forge of Iron, Major Forge Complex on Tiryns | 5 Supply: 28 to 23 | Progress 1/5; Integrity 1/5. Tiryns 12/12 satisfies full-defence requirement; ordinary slot occupied. Unfinished and inactive. | WAAAGH! Bell-Ringa orders |
| 1 / WAAAGH! Bell-Ringa / Fleet | Da Gate-Krasha Ground Assault on Olenos, 5 Strength | 1 Supply: 20 to 19; commit 1 Manpower: 20 to 19 | AI victory 23 to 17: attacker d20 12 + 5 + 3 + 3; defender d20 10 + 3 + 2 + 2, using post-commitment resources. Damage 2 captures Olenos at 1/2. Return floor(60% of 1) = 0 Manpower. Da Gate-Krasha stays 5/5, action spent. Planet Fall damages The Last Shift by 2: 3/3 to 1/3; Pleuron remains its fallback. Minor derived resources become 10/10. [Saved battle roll](Atreus_Cycle_01_Olenos_Battle.json). | None |
| 1 / WAAAGH! Bell-Ringa / Faction | Reinforce | None | +3 Supply: 19 to 22. | None |
| 1 / WAAAGH! Bell-Ringa / Social | No action | None | No Communique. | None |
| 1 / WAAAGH! Bell-Ringa / Construction | Begin unnamed Major Forge Complex on Da Bellworks | 5 Supply: 22 to 17 | Progress 1/5; Integrity 1/5; inactive. Host at 12/12, ordinary slot available and now occupied. Final resources 17 Supply / 19 Manpower. | Order of Saint Erigone orders |
| 1 / Order of Saint Erigone / Fleet | The Third Refusal Ground Assault on Daeira, 5 Strength | 1 Supply: 20 to 19; commit 1 Manpower: 20 to 19 | AI victory 19 to 11: attacker d20 8 + 5 + 3 + 3; defender d20 4 + 3 + 2 + 2, using post-commitment resources. Damage 2 captures Daeira at 1/2. Return floor(60% of 1) = 0 Manpower. The Third Refusal stays 5/5, action spent. Planet Fall reduces The Locked Reliquary 3/3 to 1/3; Triptolemos remains its fallback. Minor derived resources become 10/10. [Saved battle roll](Atreus_Cycle_01_Daeira_Battle.json). | None |
| 1 / Order of Saint Erigone / Faction | Muster | None | +3 Manpower: 19 to 22. | None |
| 1 / Order of Saint Erigone / Social | No action | None | No Communique. | None |
| 1 / Order of Saint Erigone / Construction | Begin The Vigil of the Three Refusals, Major Military Academy on Erigone | 5 Supply: 19 to 14 | Progress 1/5; Integrity 1/5; inactive. Host at 12/12; ordinary slot now occupied. Final resources 14 Supply / 22 Manpower. | None |
| 1 / Cycle end | Minor recovery check | None | All surviving unattacked Minor holdings are already at maximum defence. Calydonian Labour Defence and Eleusinian Synod engaged this Cycle and receive no fleet recovery; other surviving Minor fleets are full. No changes. Cycle 1 closed. | Cycle 2 Phase 0; then Iron Paladins |
| 2 / Phase 0 | Construction effects, Logistics check, event check; Fleet Actions reset | Warp Storm: 1 Strength per fleet | Three unfinished projects remain inactive at 1/5; no automatic progress. Logistics not due until Cycle 3. Event check 1; event-table roll 1: Warp Storm. All Major fleets 5/5 to 4/5. The Locked Reliquary, The Last Shift, The Convenient Pardon and The Winter Measure destroyed at 0. All other fleets lose 1; no attached fleet projects or Major fleet destruction penalties. No resource changes. Ordinary movement blocked for Cycle 2. [Saved rolls and fleet audit](Atreus_Cycle_02_Phase_0_Rolls.json). | Iron Paladins orders |
| 2 / Iron Paladins / Fleet | Expand Crusade Fleet Anabasis at Tiryns built-in shipyard | 1 Supply: 23 to 22; 1 Manpower: 20 to 19 | Restored 4/5 to 5/5, capped at maximum. Fleet Action spent; no assault. Warp Storm blocks movement, not yard expansion. | None |
| 2 / Iron Paladins / Faction | Reinforce through The Iron Tithe | None | +8 Supply: 22 to 30. | None |
| 2 / Iron Paladins / Social | No action | None | No Communique. | None |
| 2 / Iron Paladins / Construction | Continue The Forge of Iron on Tiryns | 5 Supply: 30 to 25 | Progress and Integrity 1/5 to 2/5; unfinished and inactive. Tiryns remains 12/12. Final resources 25 Supply / 19 Manpower. Submitted heading said Cycle 1; resolved as Cycle 2 because orders match the current state. | WAAAGH! Bell-Ringa orders |
| 2 / WAAAGH! Bell-Ringa / Fleet | Expand Da Gate-Krasha at Da Bellworks built-in shipyard | 1 Supply: 17 to 16; 1 Manpower: 19 to 18 | Restored 4/5 to 5/5, capped at maximum. Fleet Action spent; no assault. | None |
| 2 / WAAAGH! Bell-Ringa / Faction | Reinforce | None | +3 Supply: 16 to 19. | None |
| 2 / WAAAGH! Bell-Ringa / Social | No action | None | No Communique. | None |
| 2 / WAAAGH! Bell-Ringa / Construction | Continue Major Forge Complex on Da Bellworks | 5 Supply: 19 to 14 | Progress and Integrity 1/5 to 2/5; unfinished and inactive. Da Bellworks remains 12/12. Final resources 14 Supply / 18 Manpower. | Order of Saint Erigone orders |
| 2 / Order of Saint Erigone / Fleet | Expand The Third Refusal at Erigone built-in shipyard | 1 Supply: 14 to 13; 1 Manpower: 22 to 21 | Restored 4/5 to 5/5; Fleet Action spent. No assault. | None |
| 2 / Order of Saint Erigone / Faction | Reinforce | None | +3 Supply: 13 to 16. | None |
| 2 / Order of Saint Erigone / Social | No action | None | No Communique. | None |
| 2 / Order of Saint Erigone / Construction | Continue The Vigil of the Three Refusals on Erigone | 5 Supply: 16 to 11 | Progress and Integrity 1/5 to 2/5; inactive. Host remains 12/12. Ends turn at 11 Supply / 21 Manpower. | Cycle closure |
| 2 / Cycle end | Unattacked Minor holding and unengaged Minor fleet recovery | None | Holdings already full. Each eligible Minor restores 1 total Strength; House Atreides restores Pleisthenes' Oath, first listed damaged fleet, only. Destroyed fleets remain destroyed. Full per-fleet recovery audit in Cycle 3 opening record. Warp Storm expires. | Cycle 3 Phase 0 |
| 3 / Phase 0 / Constructions | Resolve eligible construction effects and Endurance | None | Three Major projects at 2/5 remain unfinished and inactive; no eligible effects or automatic progress. Fleet Actions reset. | Logistics |
| 3 / Phase 0 / Logistics | Income followed by upkeep | Each Major pays 1 Supply and 1 Manpower fleet upkeep | Iron Paladins: 25/19 +4/4 -1/1 = 28/22. Bell-Ringa: 14/18 +5/9 -1/1 = 18/26. Order: 11/21 +11/5 -1/1 = 21/25. No construction income. Next Logistics Cycle 6. | Event check |
| 3 / Phase 0 / Events | Event check d6 | None | Check 3: no event; no event-table roll. [Opening roll, Logistics and recovery audit](Atreus_Cycle_03_Phase_0_Rolls.json). | Iron Paladins orders |

|3 / Iron Paladins / Fleet|Anabasis 5/5 assaults Prosymna 2/2.|Previously paid 1 Supply and committed 1 Manpower: 28/22 to 27/21. No duplicate charge. Victory return floor(60% of 1) = 0.|Jake reported overwhelming victory, 8 October 2026. Human result; no AI roll. 2 damage (1 base + 1 breakthrough) captures Prosymna at 1/2. Planet Fall reduces The Unspent Levy 3/3 to 1/3. Council retains Heraion; derived resources now 10/10. Anabasis remains 5/5.|None|
|3 / Iron Paladins / Faction|Reinforce through The Iron Tithe.|+8 Supply: 27 to 35.|Resolved after battle.|None|
|3 / Iron Paladins / Social|No action.|None.|No change.|None|
|3 / Iron Paladins / Construction|Continue The Forge of Iron on Tiryns.|5 Supply: 35 to 30.|Progress and Integrity 2/5 to 3/5; inactive. Tiryns remains 12/12. Final resources 30 Supply / 21 Manpower.|WAAAGH! Bell-Ringa orders|

|3 / WAAAGH! Bell-Ringa / Fleet|Da Gate-Krasha assaults Pleuron with 5 Strength.|2 Supply: 18 to 16; commit 1 Manpower: 26 to 25. Victory recovery rounds down to 0.|AI victory 33 to 20: attacker d20 20 + 5 Strength + 3 Supply + 5 Manpower; defender d20 18 + 0 Strength + 1 Supply + 1 Manpower. Defender setup 8 Supply / 9 Manpower. Pleuron 4/4 to 2/4, still Calydonian Labour Defence-controlled; no capture or Planet Fall. Da Gate-Krasha remains 5/5, action spent. [Saved roll](Atreus_Cycle_03_Pleuron_Battle.json).|None|
|3 / WAAAGH! Bell-Ringa / Faction|Reinforce.|+3 Supply: 16 to 19.|Resolved after assault.|None|
|3 / WAAAGH! Bell-Ringa / Social|No action.|None.|No change.|None|
|3 / WAAAGH! Bell-Ringa / Construction|Continue Major Forge Complex on Da Bellworks.|5 Supply: 19 to 14.|Progress and Integrity 2/5 to 3/5; unfinished and inactive. Host remains 12/12. Final resources 14 Supply / 25 Manpower.|Order of Saint Erigone orders|

|3 / Order of Saint Erigone / Fleet|Third Refusal 5/5 assaults Triptolemos.|2 Supply: 21 to 19; commit 1 Manpower: 25 to 24. Victory recovery rounds down to 0.|AI victory 16 to 11: attacker d20 4 + 5 Strength + 3 Supply + 4 Manpower; defender d20 9 + 0 Strength + 1 Supply + 1 Manpower. Defender setup resources 8/9. Triptolemos 4/4 to 2/4, still Synod-controlled; no Planet Fall. Fleet remains 5/5, action spent. [Saved roll](Atreus_Cycle_03_Triptolemos_Battle.json).|None|
|3 / Order of Saint Erigone / Faction|Reinforce.|+3 Supply: 19 to 22.|Resolved.|None|
|3 / Order of Saint Erigone / Social|No action.|None.|No change.|None|
|3 / Order of Saint Erigone / Construction|Continue Vigil of the Three Refusals on Erigone.|5 Supply: 22 to 17.|Progress and Integrity 2/5 to 3/5, inactive; host 12/12. Final resources 17 Supply / 24 Manpower.|Cycle closure|
|3 / Cycle end|Minor recovery.|None.|Attacked Pleuron and Triptolemos do not recover. All other Minor holdings full. Argive, Calydonian and Eleusinian factions engaged; no fleet recovery. Unengaged House Atreides restores The Copper Hawk 4/5 to 5/5, its first listed surviving damaged fleet. Other eligible fleets full; no resurrection. Cycle 3 complete.|Cycle 4 Phase 0|
|4 / Phase 0 / Constructions|Resolve periodic construction effects; reset Fleet Actions.|None.|All three projects at 3/5 inactive; no effects, automatic progress or Endurance. All three Major fleets 5/5, actions unused.|Logistics check|
|4 / Phase 0 / Logistics|Scheduled Logistics check.|None.|Not due; next Logistics Cycle 6.|Event check|
|4 / Phase 0 / Events|Roll d6 once.|None.|Check 2: no event, no event-table roll. [Opening roll and recovery audit](Atreus_Cycle_04_Phase_0_Rolls.json).|Iron Paladins orders|

|4 / Iron Paladins / Fleet|Anabasis 5/5 assaults Heraion.|2 Supply: 30 to 28; commit 1 Manpower: 21 to 20. Victory recovery floor(60% of 1) = 0.|Jake reported overwhelming victory on 8 October 2026. Human Soulstorm result, no AI roll. 2 damage (1 base + 1 breakthrough): Heraion 4/4 to 2/4, still Council-controlled. No Planet Fall or extra overwhelming-victory bonus. Anabasis remains 5/5, action spent; The Unspent Levy remains 1/3.|None|
|4 / Iron Paladins / Faction|Defend Prosymna.|1 Supply: 28 to 27; 1 Manpower: 20 to 19.|Defence 1/2 to 2/2; Defended until start of Iron Paladins Cycle 5 turn. Replaces Reinforce.|None|
|4 / Iron Paladins / Social|No action.|None.|No change.|None|
|4 / Iron Paladins / Construction|Continue The Forge of Iron on Tiryns.|5 Supply: 27 to 22.|Progress and Integrity 3/5 to 4/5; unfinished and inactive. Tiryns remains 12/12. Final resources 22 Supply / 19 Manpower.|WAAAGH! Bell-Ringa orders|

|4 / WAAAGH! Bell-Ringa / Fleet|Da Gate-Krasha 5/5 assaults Pleuron 2/4.|2 Supply: 14 to 12; commit 1 Manpower: 25 to 24; no recovery on defeat.|AI totals 13 to 13: attacker d20 2 + 5 Strength + 2 Supply + 4 Manpower; defender d20 11 + 0 Strength + 1 Supply + 1 Manpower. Ties favour defender: Calydonian Labour Defence wins. No defence damage or capture; Pleuron remains 2/4. No Planet Fall. Da Gate-Krasha remains 5/5, action spent. [Saved battle roll](Atreus_Cycle_04_Pleuron_Battle.json).|None|
|4 / WAAAGH! Bell-Ringa / Faction|Reinforce.|+3 Supply: 12 to 15.|Resolved after assault.|None|
|4 / WAAAGH! Bell-Ringa / Social|No action.|None.|No change.|None|
|4 / WAAAGH! Bell-Ringa / Construction|Continue Major Forge Complex on Da Bellworks.|5 Supply: 15 to 10.|Progress and Integrity 3/5 to 4/5; unfinished and inactive. Host remains 12/12. Final resources 10 Supply / 24 Manpower.|Order of Saint Erigone orders|

|4 / Order of Saint Erigone / Fleet|Third Refusal 5/5 assaults Triptolemos 2/4.|2 Supply: 17 to 15; commit 1 Manpower: 24 to 23; victory recovery rounds down to 0.|AI victory 32 to 19: attacker d20 20 + 5 Strength + 3 Supply + 4 Manpower; defender d20 17 + 0 Strength + 1 Supply + 1 Manpower. 2 damage captures Triptolemos at 1/4. Synod loses its final holding and is eliminated. No surviving enemy fleet to suffer Planet Fall damage. Third Refusal remains 5/5. [Saved roll](Atreus_Cycle_04_Triptolemos_Battle.json).|None|
|4 / Order of Saint Erigone / Faction|Reinforce.|+3 Supply: 15 to 18.|Resolved.|None|
|4 / Order of Saint Erigone / Social|No action.|None.|No change.|None|
|4 / Order of Saint Erigone / Construction|Continue Vigil of the Three Refusals on Erigone.|5 Supply: 18 to 13.|Progress and Integrity 3/5 to 4/5; inactive. Host 12/12. Final resources 13 Supply / 23 Manpower.|Cycle closure|
|4 / Cycle end|Minor recovery.|None.|Attacked Heraion and Pleuron do not recover. Other surviving Minor holdings full. Argive and Calydonian fleets ineligible after engagement; Synod eliminated. House Atreides restores Perseia's Breakwater 4/5 to 5/5, first listed surviving damaged fleet. Other eligible fleets full. Cycle 4 closed; completed narrative recorded.|Cycle 5 Phase 0|
|5 / Phase 0 / Constructions|Resolve periodic effects and reset Fleet Actions.|None.|Three projects at 4/5 remain inactive; no automatic progress or Endurance effects. All Major fleets 5/5 with unused actions.|Logistics check|
|5 / Phase 0 / Logistics|Scheduled Logistics check.|None.|Not due until Cycle 6.|Event check|
|5 / Phase 0 / Events|Roll d6 once.|None.|Check 4: no event. [Opening check and recovery audit](Atreus_Cycle_05_Phase_0_Rolls.json). Prosymna's Defended status expires at the start of the Iron Paladins Cycle 5 turn; defence remains 2/2.|Iron Paladins orders|

|5 / Iron Paladins / Fleet|Anabasis 5/5 assaults Heraion 2/4.|2 Supply: 22 to 20; commit 1 Manpower: 19 to 18. Victory recovery rounds down to 0.|Jake reported overwhelming victory on 8 October 2026; human battle at Hard difficulty, no AI roll. 2 damage captures Heraion at 1/4. Planet Fall destroys The Unspent Levy (1/3); no surviving fleet to receive remaining damage. Argive Muster Council loses its final holding and is eliminated. Anabasis remains 5/5, action spent. No additional bonus for descriptive victory margin.|None|
|5 / Iron Paladins / Faction|Reinforce through The Iron Tithe.|+8 Supply: 20 to 28.|Resolved after battle.|None|
|5 / Iron Paladins / Social|No action.|None.|No change.|None|
|5 / Iron Paladins / Construction|Complete The Forge of Iron on Tiryns.|5 Supply: 28 to 23.|Progress and Integrity 4/5 to 5/5; complete and active. Host remains 12/12. +7 Supply per Logistics Cycle while operational; no immediate payout. Final resources 23 Supply / 18 Manpower.|WAAAGH! Bell-Ringa orders|

|5 / WAAAGH! Bell-Ringa / Fleet|Da Gate-Krasha 5/5 assaults Pleuron 2/4.|2 Supply: 10 to 8; commit 1 Manpower: 24 to 23. No recovery on defeat.|AI defeat 14 to 15: attacker d20 4 + 5 Strength + 1 Supply + 4 Manpower; defender d20 13 + 0 Strength + 1 Supply + 1 Manpower. Pleuron remains Calydonian Labour Defence-controlled at 2/4; no damage, capture or Planet Fall. Da Gate-Krasha stays 5/5, action spent. [Saved roll](Atreus_Cycle_05_Pleuron_Battle.json).|None|
|5 / WAAAGH! Bell-Ringa / Faction|Reinforce.|+3 Supply: 8 to 11.|Resolved after battle.|None|
|5 / WAAAGH! Bell-Ringa / Social|No action.|None.|No change.|None|
|5 / WAAAGH! Bell-Ringa / Construction|Complete Major Forge Complex on Da Bellworks.|5 Supply: 11 to 6.|Progress and Integrity 4/5 to 5/5, complete and active. Host remains 12/12. +7 Supply per Logistics Cycle while operational; no immediate payout. Final resources 6 Supply / 23 Manpower.|Order of Saint Erigone orders|

|5 / Order of Saint Erigone / Fleet|Third Refusal holds in Eleusis.|None.|5/5; Fleet Action unused.|None|
|5 / Order of Saint Erigone / Faction|Defend Triptolemos.|2 Supply: 13 to 11; 2 Manpower: 23 to 21.|Defence 1/4 to 3/4; Defended until start of the Order's Cycle 6 turn.|None|
|5 / Order of Saint Erigone / Social|No action.|None.|No change.|None|
|5 / Order of Saint Erigone / Construction|Complete Vigil of the Three Refusals on Erigone.|5 Supply: 11 to 6.|Progress and Integrity 4/5 to 5/5; complete and active, host 12/12. +7 Manpower per Logistics Cycle; no immediate payout. Ends at 6 Supply / 21 Manpower.|Cycle closure|
|5 / Cycle end|Minor recovery; close Cycle and record unified narrative.|None.|Pleuron was attacked and does not recover. Calydonian faction engaged; no fleet recovery. Argive and Eleusinian factions eliminated. Other surviving Minor holdings full; House Atreides restores The Dendra Covenant 2/3 to 3/3, its sole damaged fleet. No resurrection.|Cycle 6 Phase 0|
|6 / Phase 0 / Constructions|Resolve periodic effects and reset Fleet Actions.|None.|Two Forges and one Academy complete at 5/5; their income is applied once in Logistics below. No separate repair, damage or Endurance effects. All Major fleets 5/5, actions unused.|Logistics|
|6 / Phase 0 / Logistics|Holding income, active constructions, passive traits, then fleet upkeep.|1 Supply / 1 Manpower upkeep per Major.|Iron Paladins: 23/18 +14/7 gross -1/1 = 36/24. Bell-Ringa: 6/23 +12/9 gross -1/1 = 17/31. Order: 6/21 +13/14 gross -1/1 = 18/34. Supply/Manpower; Forge +7 Supply each, Academy +7 Manpower, Martial Culture +4 Manpower, War Economy +6 Supply included. Next Logistics Cycle 9.|Events|
|6 / Phase 0 / Events|Roll d6 once.|None.|Check 4: no event. [Opening audit](Atreus_Cycle_06_Phase_0_Rolls.json). Triptolemos remains Defended until the Order's own Cycle 6 turn begins.|Iron Paladins orders|

|6 / Iron Paladins / Fleet|Anabasis holds in Argos.|None.|Remains 5/5; Fleet Action unused.|None|
|6 / Iron Paladins / Faction|Defend Heraion.|2 Supply: 36 to 34; 2 Manpower: 24 to 22.|Defence 1/4 to 3/4; Defended until start of Iron Paladins Cycle 7 turn.|None|
|6 / Iron Paladins / Social|No action.|None.|No change.|None|
|6 / Iron Paladins / Construction|Begin upgrade to The Grand Forge of Iron on Tiryns.|5 Supply: 34 to 29.|Upgrade stage 1/5; Integrity 5/5 to 6/10. Host remains 12/12. Base +7 Supply per Logistics Cycle retained at Integrity 5 or above; +14 only at full upgraded Integrity. No immediate payout. Final resources 29 Supply / 22 Manpower.|WAAAGH! Bell-Ringa orders|

|6 / WAAAGH! Bell-Ringa / Fleet|Da Gate-Krasha 5/5 assaults Pleuron 2/4.|2 Supply: 17 to 15; commit 1 Manpower: 31 to 30. Victory recovery floor(60% of 1) = 0.|AI victory 29 to 6: attacker d20 15 + 5 Strength + 3 Supply + 6 Manpower; defender d20 4 + 0 Strength + 1 Supply + 1 Manpower. 2 damage captures Pleuron at 1/4. Calydonian Labour Defence loses its final holding and is eliminated; no surviving fleet for Planet Fall. Da Gate-Krasha remains 5/5, action spent. [Saved roll](Atreus_Cycle_06_Pleuron_Battle.json).|None|
|6 / WAAAGH! Bell-Ringa / Faction|Create Da Fist at Da Bellworks' built-in Orbital Shipyard.|1 Supply: 15 to 14; 1 Manpower: 30 to 29.|New fleet 1/5 in Calydon; cannot take a Fleet Action this Cycle.|None|
|6 / WAAAGH! Bell-Ringa / Social|No action.|None.|No change.|None|
|6 / WAAAGH! Bell-Ringa / Construction|Begin Da Jaw-Breaka, Assault Cruiser attached to Da Gate-Krasha.|3 Supply: 14 to 11.|Progress and Integrity 1/3; unfinished and inactive. Host 5/5. Completion grants +2 current and maximum Fleet Strength. Final resources 11 Supply / 29 Manpower.|Order of Saint Erigone orders|

|6 / Order of Saint Erigone / Fleet|Move The Third Refusal from Eleusis to Delphi.|None.|5/5; Fleet Action spent. No assault. Order has Void Superiority 5 to 4 over The Sealed Testimony; hostile fleet remains. Triptolemos Defended expired at start of this turn; defence stays 3/4.|None|
|6 / Order of Saint Erigone / Faction|Create The Returning Escort at Erigone's built-in Orbital Shipyard.|1 Supply: 18 to 17; 1 Manpower: 34 to 33.|1/5 in Eleusis; cannot act in Cycle 6.|None|
|6 / Order of Saint Erigone / Social|No action.|None.|No change.|None|
|6 / Order of Saint Erigone / Construction|No action; defer The Breach Litany.|None.|No new project or Integrity. Academy stays active 5/5. Final resources 17 Supply / 33 Manpower.|Cycle closure|
|6 / Cycle end|Minor recovery and completed Cycle record.|None.|Calydonian Labour Defence eliminated; no resurrection. All surviving Minor holdings and fleets already full, so no recovery changes. Cycle 6 closed.|Cycle 7 Phase 0|
|7 / Phase 0 / Constructions|Resolve periodic effects; reset Fleet Actions.|None.|No automatic damage, repair or Endurance effects apply. Grand Forge 6/10 retains base income; Da Jaw-Breaka 1/3 remains inactive. Newly created fleets can act this Cycle. Heraion Defended expires at start of Iron Paladins Cycle 7 turn; defence remains 3/4.|Logistics check|
|7 / Phase 0 / Logistics|Scheduled Logistics check.|None.|Not due; next Logistics Cycle 9. Resources unchanged: Iron Paladins 29/22, Bell-Ringa 11/29, Order 17/33 (Supply/Manpower).|Events|
|7 / Phase 0 / Events|Roll d6 once.|None.|Check 2: no event; no event-table roll. [Opening audit](Atreus_Cycle_07_Phase_0_Rolls.json).|Iron Paladins orders|

|7 / Iron Paladins / Fleet|Anabasis holds in Argos.|None.|Remains 5/5; Fleet Action unused.|None|
|7 / Iron Paladins / Faction|Create The Emperor’s Judgement at Tiryns’s built-in Orbital Shipyard.|1 Supply: 29 to 28; 1 Manpower: 22 to 21.|New fleet 1/5 in Argos; cannot take a Fleet Action this Cycle. No Defend action: Heraion remains 3/4 without Defended.|None|
|7 / Iron Paladins / Social|No action.|None.|No change.|None|
|7 / Iron Paladins / Construction|Continue upgrade of The Grand Forge of Iron on Tiryns.|5 Supply: 28 to 23.|Upgrade progress 1/5 to 2/5; Integrity 6/10 to 7/10. Tiryns remains 12/12. Base +7 Supply per Logistics Cycle retained; no immediate payout. Final resources 23 Supply / 21 Manpower.|WAAAGH! Bell-Ringa orders|

|7 / WAAAGH! Bell-Ringa / Fleet|Da Gate-Krasha holds; Expand Da Fist at Da Bellworks' built-in Orbital Shipyard.|1 Supply: 11 to 10; 1 Manpower: 29 to 28.|Da Gate-Krasha remains 5/5, action unused. Da Fist 1/5 to 3/5, action spent. Both remain in Calydon; no assault.|None|
|7 / WAAAGH! Bell-Ringa / Faction|Reinforce.|+3 Supply: 10 to 13.|Resolved.|None|
|7 / WAAAGH! Bell-Ringa / Social|No action.|None.|No change.|None|
|7 / WAAAGH! Bell-Ringa / Construction|Continue Da Jaw-Breaka, Assault Cruiser on Da Gate-Krasha.|3 Supply: 13 to 10.|Progress and Integrity 1/3 to 2/3; unfinished and inactive. Host remains full at 5/5 in Calydon with Da Bellworks' operational shipyard. Final resources 10 Supply / 28 Manpower.|Order of Saint Erigone orders|

|7 / Order of Saint Erigone / Fleet|Third Refusal assaults Castalia; Returning Escort expands at Erigone.|Assault 1 Supply / 1 Manpower: 17/33 to 16/32; victory recovery rounds down to 0. Expand 1/1: 16/32 to 15/31.|AI victory 16 to 2: attacker d20 2 +5 Strength +3 Supply +6 Manpower; defender d20 2 +0 Strength +0 Supply +0 Manpower, post-commitment 4/4. Custodians do not defend the separate hostile Lotus Company. 2 damage captures Castalia at 1/2; Lotus eliminated with no surviving fleet for Planet Fall. Third Refusal stays 5/5; Escort 1/5 to 3/5. Both actions spent. [Saved roll](Atreus_Cycle_07_Castalia_Battle.json).|Conditional Faction action|
|7 / Order of Saint Erigone / Faction|Defend captured Castalia.|1 Supply / 1 Manpower: 15/31 to 14/30.|Defence 1/2 to 2/2; Defended until start of Order Cycle 8 turn. No Reinforce.|None|
|7 / Order of Saint Erigone / Social|No action.|None.|No change.|None|
|7 / Order of Saint Erigone / Construction|Begin Castalia Anchorage, Minor Orbital Shipyard.|3 Supply: 14 to 11.|Progress and Integrity 1/3; unfinished and inactive, ordinary slot occupied. Castalia full 2/2. Planetary construction does not require an existing yard. Final resources 11 Supply / 30 Manpower.|Cycle closure|
|7 / Cycle end|Minor recovery and completed narrative.|None.|Lotus eliminated; no resurrection. All surviving Minor holdings and fleets already full; no recovery changes.|Cycle 8 Phase 0|
|8 / Phase 0 / Constructions|Periodic effects; reset Fleet Actions.|None.|No automatic damage, repair or Endurance effects. Grand Forge 7/10 retains base income; Da Jaw-Breaka 2/3 and Castalia Anchorage 1/3 inactive. All fleets may act, including Emperor’s Judgement. Castalia remains Defended until Order's own turn.|Logistics check|
|8 / Phase 0 / Logistics|Scheduled Logistics check.|None.|Not due until Cycle 9. Resources unchanged: Iron Paladins 23/21, Bell-Ringa 10/28, Order 11/30 (Supply/Manpower).|Events|
|8 / Phase 0 / Events|Roll d6 once.|None.|Check 2: no event. [Opening audit](Atreus_Cycle_08_Phase_0_Rolls.json).|Iron Paladins orders|

|8 / Iron Paladins / Fleet|Anabasis holds; Expand The Emperor’s Judgement at Tiryns's built-in Orbital Shipyard.|1 Supply: 23 to 22; 1 Manpower: 21 to 20.|Anabasis remains 5/5, action unused. The Emperor’s Judgement 1/5 to 3/5, action spent. Both in Argos.|None|
|8 / Iron Paladins / Faction|Defend Heraion.|2 Supply: 22 to 20; 2 Manpower: 20 to 18.|Defence 3/4 to 4/4, capped at maximum; Defended until start of Iron Paladins Cycle 9 turn.|None|
|8 / Iron Paladins / Social|No action.|None.|No change.|None|
|8 / Iron Paladins / Construction|Continue The Grand Forge of Iron upgrade.|5 Supply: 20 to 15.|Upgrade progress 2/5 to 3/5; Integrity 7/10 to 8/10. Tiryns remains 12/12. Base +7 Supply per Logistics Cycle active; no immediate payout. Final resources 15 Supply / 18 Manpower.|WAAAGH! Bell-Ringa orders|

|8 / WAAAGH! Bell-Ringa / Fleet|Da Gate-Krasha holds for construction; Expand Da Fist at Da Bellworks' shipyard.|1 Supply: 10 to 9; 1 Manpower: 28 to 27.|Da Fist 3/5 to 5/5, action spent. Da Gate-Krasha holds 5/5 before construction, action unused. Both in Calydon; no assault.|None|
|8 / WAAAGH! Bell-Ringa / Faction|Defend Pleuron.|2 Supply: 9 to 7; 2 Manpower: 27 to 25.|Defence 1/4 to 3/4; Defended until start of Bell-Ringa Cycle 9 turn.|None|
|8 / WAAAGH! Bell-Ringa / Social|No action.|None.|No change.|None|
|8 / WAAAGH! Bell-Ringa / Construction|Complete Da Jaw-Breaka at Da Bellworks' operational shipyard.|3 Supply: 7 to 4.|Progress and Integrity 2/3 to 3/3. Host full 5/5 before completion. Grants +2 current and maximum Fleet Strength once: Da Gate-Krasha 5/5 to 7/7 (base 5 plus permanent 2). Final resources 4 Supply / 25 Manpower.|Order of Saint Erigone orders|

|8 / Order of Saint Erigone / Fleet|First assault Omphalos Relay with Third Refusal; then Expand Returning Escort at Erigone.|Assault 1 Supply / 1 Manpower: 11/30 to 10/29; victory recovery rounds down to 0. Expand 1/1: 10/29 to 9/28.|AI victory 27 to 16: attacker d20 15 +5 Strength +2 Supply +5 Manpower; defender d20 6 +4 Strength +3 Supply +3 Manpower (post-commitment 19/19). 2 damage captures Relay at 1/2; Planet Fall reduces Sealed Testimony 4/4 to 2/4. Custodians retain Corycia and Pytho, derived resources 15/15. Third Refusal stays 5/5; Escort 3/5 to 5/5; both actions spent. Castalia Defended expired at turn start. [Saved roll](Atreus_Cycle_08_Omphalos_Battle.json).|None|
|8 / Order of Saint Erigone / Faction|Reinforce.|+3 Supply: 9 to 12.|Resolved after fleet actions.|None|
|8 / Order of Saint Erigone / Social|No action.|None.|No change.|None|
|8 / Order of Saint Erigone / Construction|Continue Castalia Anchorage.|3 Supply: 12 to 9.|Progress and Integrity 1/3 to 2/3, inactive. Host full at 2/2. Final resources 9 Supply / 28 Manpower.|Cycle closure|
|8 / Cycle end|Minor recovery; completed narrative.|None.|Custodians engaged and receive no fleet recovery. Their remaining holdings and all other surviving Minor holdings and fleets are full; no changes. No resurrection.|Cycle 9 Phase 0|
|9 / Phase 0 / Constructions|Periodic effects and Fleet Action reset.|None.|No automatic damage, repair or Endurance. Grand Forge 8/10 retains +7 Supply base income. Ork Forge and Order Academy active 5/5; Anchorage 2/3 inactive. Da Jaw-Breaka's permanent +2 already applied, not added again. Heraion Defended expires at Iron Paladins turn start; Pleuron retains Defended until Bell-Ringa's turn.|Logistics|
|9 / Phase 0 / Logistics|Income then fleet upkeep.|2 Supply / 2 Manpower upkeep per Major.|Iron Paladins 15/18 +14/7 gross -2/2 = 27/23. Bell-Ringa 4/25 +14/11 gross -2/2 = 16/34. Order 9/28 +15/16 gross -2/2 = 22/42. Supply/Manpower; all active construction and passive trait income included. Next Logistics Cycle 12.|Events|
|9 / Phase 0 / Events|Roll d6 once.|None.|Check 2: no event. [Opening audit](Atreus_Cycle_09_Phase_0_Rolls.json).|Iron Paladins orders|

|9 / Iron Paladins / Fleet|Anabasis holds; Expand The Emperor’s Judgement at Tiryns's built-in Orbital Shipyard.|1 Supply: 27 to 26; 1 Manpower: 23 to 22.|Anabasis remains 5/5, action unused. The Emperor’s Judgement 3/5 to 5/5, action spent. Both in Argos.|None|
|9 / Iron Paladins / Faction|Create Vigilatius at Tiryns's built-in Orbital Shipyard.|1 Supply: 26 to 25; 1 Manpower: 22 to 21.|New fleet 1/5 in Argos; cannot take a Fleet Action this Cycle.|None|
|9 / Iron Paladins / Social|No action.|None.|No change.|None|
|9 / Iron Paladins / Construction|Continue The Grand Forge of Iron upgrade.|5 Supply: 25 to 20.|Upgrade progress 3/5 to 4/5; Integrity 8/10 to 9/10. Tiryns remains 12/12. Base +7 Supply per Logistics Cycle remains active; no immediate payout. Final resources 20 Supply / 21 Manpower.|WAAAGH! Bell-Ringa orders|

|9 / WAAAGH! Bell-Ringa / Fleet|Move Da Gate-Krasha 7/7 and Da Fist 5/5 from Calydon to Lerna.|None.|Both Fleet Actions spent; no assault. Combined 12 Strength grants Void Superiority over 5 hostile Strength. Da Jaw-Breaka moves with its host. Pleuron Defended expired at turn start; defence remains 3/4.|None|
|9 / WAAAGH! Bell-Ringa / Faction|Create Da Backhand at Da Bellworks' built-in Orbital Shipyard.|1 Supply: 16 to 15; 1 Manpower: 34 to 33.|1/5 in Calydon; cannot take a Fleet Action this Cycle.|None|
|9 / WAAAGH! Bell-Ringa / Social|No action.|None.|No change.|None|
|9 / WAAAGH! Bell-Ringa / Construction|Begin Da Iron Gob upgrade on Da Bellworks.|5 Supply: 15 to 10.|Upgrade progress 1/5; Integrity 5/5 to 6/10. Host remains 12/12. Base +7 Supply per Logistics Cycle retained at Integrity at least 5; +14 only at full upgraded Integrity. No immediate payout. Final resources 10 Supply / 33 Manpower.|Order of Saint Erigone orders|

|9 / Order of Saint Erigone / Fleet|Third Refusal assaults Corycia; Returning Escort moves Eleusis to Calydon.|1 Supply: 22 to 21; 1 Manpower: 42 to 41. Victory return rounds down to 0. Movement free.|AI victory 31 to 24: attacker d20 14 +5 Strength +4 Supply +8 Manpower; defender d20 18 +2 Strength +2 Supply +2 Manpower (14/14 post-commitment). 2 damage captures Corycia at 1/2; Planet Fall destroys Sealed Testimony 2/4. Custodians retain Pytho, derived 10/10. Both Major fleets remain 5/5, actions spent. Escort gains Void Superiority 5 to 1 in Calydon; no assault there. [Saved roll](Atreus_Cycle_09_Corycia_Battle.json).|None|
|9 / Order of Saint Erigone / Faction|Create The Unbroken Procession at Erigone.|1 Supply: 21 to 20; 1 Manpower: 41 to 40.|1/5 in Eleusis, cannot act this Cycle.|None|
|9 / Order of Saint Erigone / Social|No action.|None.|No change.|None|
|9 / Order of Saint Erigone / Construction|Complete Castalia Anchorage.|3 Supply: 20 to 17.|Progress and Integrity 2/3 to 3/3; operational Orbital Shipyard in Delphi. Host 2/2. Final resources 17 Supply / 40 Manpower.|Cycle closure|
|9 / Cycle end|Minor recovery; completed narrative.|None.|Custodians engaged; destroyed fleet cannot recover. All remaining Minor holdings and surviving fleets full; no changes or resurrection.|Cycle 10 Phase 0|
|10 / Phase 0 / Constructions|Periodic effects; reset Fleet Actions.|None.|No periodic damage, repair or Endurance. Forges retain base income during upgrades; Castalia Anchorage operational. No automatic progress or repeat Cruiser bonus. Newly created fleets may act.|Logistics check|
|10 / Phase 0 / Logistics|Scheduled Logistics check.|None.|Not due; next Cycle 12.|Events|
|10 / Phase 0 / Events|Check 6; event-table result 3: Supply Crisis.|Each Major loses 5 Supply and 5 Manpower.|Iron Paladins 20/21 to 15/16; Bell-Ringa 10/33 to 5/28; Order 17/40 to 12/35. No deficit triggered. Minor values remain holding-derived, not persistent resource pools. [Raw rolls and opening audit](Atreus_Cycle_10_Phase_0_Rolls.json).|Iron Paladins orders|

|10 / Iron Paladins / Fleet|Anabasis and The Emperor’s Judgement hold; Expand Vigilatius at Tiryns's shipyard.|1 Supply: 15 to 14; 1 Manpower: 16 to 15.|First two fleets remain 5/5 with unused actions. Vigilatius 1/5 to 3/5, action spent. All in Argos.|None|
|10 / Iron Paladins / Faction|Reinforce through The Iron Tithe.|+8 Supply: 14 to 22.|Resolved; no additional Logistics payout.|None|
|10 / Iron Paladins / Social|No action.|None.|No change.|None|
|10 / Iron Paladins / Construction|Complete The Grand Forge of Iron upgrade.|5 Supply: 22 to 17.|Upgrade progress 4/5 to 5/5; Integrity 9/10 to 10/10. Host remains 12/12. Upgraded +14 Supply per Logistics Cycle now active, replacing base +7; no immediate payout. Final resources 17 Supply / 15 Manpower.|WAAAGH! Bell-Ringa orders|

|10 / WAAAGH! Bell-Ringa / Fleet|Move Da Gate-Krasha 7/7 and Da Fist 5/5 from Lerna to Calydon; then Expand Da Backhand at Da Bellworks' shipyard.|Movement free. Expand 1 Supply: 5 to 4; 1 Manpower: 28 to 27.|Da Backhand 1/5 to 3/5. All three Fleet Actions spent; no attack. Orks regain Void Superiority 15 to 5 in Calydon; Returning Escort remains 5/5. Da Jaw-Breaka travels with its host.|None|
|10 / WAAAGH! Bell-Ringa / Faction|Reinforce.|+3 Supply: 4 to 7.|Resolved.|None|
|10 / WAAAGH! Bell-Ringa / Social|No action.|None.|No change.|None|
|10 / WAAAGH! Bell-Ringa / Construction|Pause Da Iron Gob upgrade; no action.|None.|Upgrade stays 1/5, Integrity 6/10; base +7 Supply per Logistics Cycle active. Final resources 7 Supply / 27 Manpower.|Order of Saint Erigone orders|

|10 / Order of Saint Erigone / Fleet|First Third Refusal assaults Pytho; then Returning Escort moves Calydon to Delphi; Expand Unbroken Procession at Erigone.|Assault 2 Supply / 1 Manpower: 12/35 to 10/34; victory recovery rounds down to 0. Movement free. Expand 1/1: 10/34 to 9/33.|AI victory 31 to 10: attacker d20 18 +5 Strength +2 Supply +6 Manpower; defender d20 8 +0 Strength +1 Supply +1 Manpower (8/9 after commitment). 2 damage reduces Pytho 4/4 to 2/4, still Custodian-controlled; no Planet Fall. Returning Escort does not participate in assault. Procession 1/5 to 3/5. All actions spent. [Saved roll](Atreus_Cycle_10_Pytho_Battle.json).|None|
|10 / Order of Saint Erigone / Faction|Reinforce.|+3 Supply: 9 to 12.|Resolved.|None|
|10 / Order of Saint Erigone / Social|No action.|None.|No change.|None|
|10 / Order of Saint Erigone / Construction|Begin The Breach Litany, Bombardment Bay on Third Refusal, Delphi.|3 Supply: 12 to 9.|Progress and Integrity 1/3, inactive. Host full 5/5; Castalia Anchorage operational in same system. Final resources 9 Supply / 33 Manpower.|Cycle closure|
|10 / Cycle end|Minor recovery and completed narrative.|None.|Pytho attacked: no defence recovery. Custodians engaged and have no surviving fleet. Other surviving Minor assets full; no changes or resurrection.|Cycle 11 Phase 0|
|11 / Phase 0 / Constructions|Periodic effects and Fleet Action reset.|None.|No periodic damage, repair or Endurance. Grand Forge upgraded income active; Da Iron Gob retains base income; Breach Litany inactive 1/3. No automatic progress or repeated permanent Strength grant.|Logistics check|
|11 / Phase 0 / Logistics|Scheduled Logistics check.|None.|Not due until Cycle 12. Resources Iron Paladins 17/15, Bell-Ringa 7/27, Order 9/33 (Supply/Manpower).|Events|
|11 / Phase 0 / Events|Roll d6 once.|None.|Check 4: no event. Prior Supply Crisis already settled; no repeat loss. [Opening audit](Atreus_Cycle_11_Phase_0_Rolls.json).|Iron Paladins orders|

|11 / Iron Paladins / Fleet|Move The Emperor’s Judgement to Aulis; Anabasis holds; Expand Vigilatius at Tiryns.|Movement free; Expand 1 Supply: 17 to 16; 1 Manpower: 15 to 14.|Judgement 5/5 in Aulis, action spent, no assault; 5 to 5 contested with Unanswered Muster. Anabasis 5/5 Argos, action unused; Vigilatius 3/5 to 5/5 Argos, action spent.|None|
|11 / Iron Paladins / Faction|Muster through The Iron Tithe.|+8 Manpower: 14 to 22.|Resolved.|None|
|11 / Iron Paladins / Social|No action.|None.|No change.|None|
|11 / Iron Paladins / Construction|Begin Gene-Seed Vaults, Major Military Academy on Heraion.|5 Supply: 16 to 11.|Progress and Integrity 1/5, inactive; full host 4/4, ordinary slot occupied. +7 Manpower per Logistics Cycle upon completion at full Integrity. Final resources 11 Supply / 22 Manpower.|WAAAGH! Bell-Ringa orders|

|11 / WAAAGH! Bell-Ringa / Fleet|Move Da Gate-Krasha 7/7 and Da Fist 5/5 to Eleusis; Expand Da Backhand at Da Bellworks.|Movement free. Expand 1 Supply: 7 to 6; 1 Manpower: 27 to 26.|Da Jaw-Breaka travels with Gate-Krasha. Da Backhand 3/5 to 5/5 in Calydon. All actions spent; no assault. Orks have Void Superiority 12 to 3 in Eleusis over Unbroken Procession.|None|
|11 / WAAAGH! Bell-Ringa / Faction|Reinforce.|+3 Supply: 6 to 9.|Resolved.|None|
|11 / WAAAGH! Bell-Ringa / Social|No action.|None.|No change.|None|
|11 / WAAAGH! Bell-Ringa / Construction|Continue Da Iron Gob upgrade on Da Bellworks.|5 Supply: 9 to 4.|Upgrade progress 1/5 to 2/5; Integrity 6/10 to 7/10. Host 12/12; base +7 Supply income remains active. Final resources 4 Supply / 26 Manpower.|Order of Saint Erigone orders|

|11 / Order of Saint Erigone / Fleet|Third Refusal assaults Pytho first; Escort moves to Eleusis; Expand Procession at Erigone.|Assault 2 Supply / 1 Manpower: 9/33 to 7/32; no recovery on defeat. Expand 1/1: 7/32 to 6/31.|AI defeat 13 to 14: attacker d20 1 +5 Strength +1 Supply +6 Manpower; defender d20 12 +0 Strength +1 Supply +1 Manpower (8/9 post-commitment). Pytho remains Custodian-controlled at 2/4; no damage or Planet Fall. Third Refusal 5/5; Escort 5/5 Eleusis; Procession 3/5 to 5/5. All actions spent; Orks retain Void Superiority 12 to 10 in Eleusis. [Saved roll](Atreus_Cycle_11_Pytho_Battle.json).|None|
|11 / Order of Saint Erigone / Faction|Reinforce.|+3 Supply: 6 to 9.|Resolved.|None|
|11 / Order of Saint Erigone / Social|No action.|None.|No change.|None|
|11 / Order of Saint Erigone / Construction|Continue The Breach Litany at Castalia Anchorage.|3 Supply: 9 to 6.|Progress and Integrity 1/3 to 2/3; inactive. Host full 5/5 in Delphi with operational shipyard. Final resources 6 Supply / 31 Manpower.|Cycle closure|
|11 / Cycle end|Minor recovery; completed narrative.|None.|Pytho attacked and does not recover. Custodians engaged with no fleet; all other surviving Minor assets full. No changes or resurrection.|Cycle 12 Phase 0|
|12 / Phase 0 / Constructions|Periodic effects and Fleet Action reset.|None.|No damage, repair or Endurance effects. Grand Forge +14 Supply, Da Iron Gob base +7 Supply, Academy +7 Manpower eligible for Logistics. Gene-Seed Vaults 1/5 and Breach Litany 2/3 remain inactive. No automatic progress.|Logistics|
|12 / Phase 0 / Logistics|Income then fleet upkeep.|3 Supply / 3 Manpower upkeep per Major.|Iron Paladins 11/22 +21/7 gross -3/3 = 29/26. Bell-Ringa 4/26 +14/11 gross -3/3 = 15/34. Order 6/31 +16/17 gross -3/3 = 19/45. Supply/Manpower; construction and passive trait income included. Next Logistics Cycle 15.|Events|
|12 / Phase 0 / Events|Roll d6 once.|None.|Check 5: no event; no event-table roll. [Opening audit](Atreus_Cycle_12_Phase_0_Rolls.json).|Iron Paladins orders|

|12 / Iron Paladins / Fleet|Move Anabasis from Argos to Aulis before Emperor’s Judgement assaults Schoenus; Vigilatius holds in Argos.|Movement free. Assault 1 Supply: 29 to 28; commit 1 Manpower: 26 to 25. Victory return floor(60% of 1) = 0.|Jake reported Iron Paladin victory: “The Aulis Anchorage Command put up a worthy resistance but they were eventually drowned in a wave of Iron.” Human Soulstorm result; no AI roll. Judgement alone commits 5 Strength; Anabasis cannot attack after moving. 2 damage captures Schoenus at 1/2. Planet Fall reduces Unanswered Muster 5/5 to 3/5; Command retains Hyria, derived resources 15/15. Paladin fleets remain 5/5; Anabasis and Judgement actions spent, Vigilatius unused. Void Superiority 10 to 3 in Aulis. [Battle record](Atreus_Cycle_12_Schoenus_Battle.json).|Conditional Faction action|
|12 / Iron Paladins / Faction|Defend captured Schoenus.|1 Supply: 28 to 27; 1 Manpower: 25 to 24.|Defence 1/2 to 2/2; Defended until start of Iron Paladins Cycle 13 turn. Reinforce alternative not taken.|None|
|12 / Iron Paladins / Social|No action.|None.|No change.|None|
|12 / Iron Paladins / Construction|Continue Gene-Seed Vaults on Heraion.|5 Supply: 27 to 22.|Progress and Integrity 1/5 to 2/5; unfinished and inactive. Host full at 4/4. Final resources 22 Supply / 24 Manpower. Cycle 12 remains open; no Cycle-end recovery or Phase 0 repeated.|WAAAGH! Bell-Ringa orders|

|12 / WAAAGH! Bell-Ringa / Fleet|Gate-Krasha 7/7 and Da Fist 5/5 jointly assault Triptolemos; Da Backhand holds Calydon.|2 Supply: 15 to 13; commit 2 Manpower: 34 to 32; victory return floor(60% of 2) = 1, to 33.|AI victory 39 to 29: attacker d20 19 +12 Strength +2 Supply +6 Manpower; defender d20 8 +10 Strength +3 Supply +8 Manpower, post-commitment 17/44. 3 damage captures Triptolemos 3/4 at 1/4. Order loses 2 Supply and 3 Manpower total: 19/45 to 17/42 (2/2 Planet Fall plus 1 defensive Manpower; no double Supply charge). Planet Fall hits Procession, Escort, Escort: Procession 5/5 to 4/5, Escort 5/5 to 3/5. Ties randomly resolved and saved. Ork fleets unchanged, both attacking actions spent; Backhand unused. Void Superiority 12 to 7. [Saved battle](Atreus_Cycle_12_Triptolemos_Battle.json).|Conditional Faction action|
|12 / WAAAGH! Bell-Ringa / Faction|Defend captured Triptolemos.|2 Supply: 13 to 11; 2 Manpower: 33 to 31.|Defence 1/4 to 3/4; Defended until start of Bell-Ringa Cycle 13 turn. Reinforce alternative not taken.|None|
|12 / WAAAGH! Bell-Ringa / Social|No action.|None.|No change.|None|
|12 / WAAAGH! Bell-Ringa / Construction|Continue Da Iron Gob upgrade at Da Bellworks.|5 Supply: 11 to 6.|Upgrade progress 2/5 to 3/5; Integrity 7/10 to 8/10; base +7 Supply income retained. Final resources 6 Supply / 31 Manpower. Cycle remains open.|Order of Saint Erigone orders|

|12 / Order of Saint Erigone / Fleet|Third Refusal assaults Pytho first; expand Returning Escort and Unbroken Procession at Erigone.|Assault 2 Supply / 1 Manpower: 17/42 to 15/41; victory return 0. Expansions 2 Supply / 2 Manpower: 15/41 to 13/39.|AI victory 24 to 22: attacker d20 8 +5 Strength +3 Supply +8 Manpower; defender d20 20 +0 Strength +1 Supply +1 Manpower, post-commitment 8/9. 2 damage captures Pytho at 1/4; Custodians eliminated with no fleet for Planet Fall. Breach Litany unfinished during assault, no bonus. Escort 3/5 to 5/5; Procession 4/5 to 5/5, capped. All three actions spent. [Saved roll](Atreus_Cycle_12_Pytho_Battle.json).|None|
|12 / Order of Saint Erigone / Faction|Create The Oath at the Gate at Erigone.|1 Supply / 1 Manpower: 13/39 to 12/38.|New fleet 1/5 in Eleusis, unable to act this Cycle. Orks retain Void Superiority 12 to 11.|None|
|12 / Order of Saint Erigone / Social|No action.|None.|No change.|None|
|12 / Order of Saint Erigone / Construction|Complete The Breach Litany at Castalia Anchorage, Delphi.|3 Supply: 12 to 9.|Progress and Integrity 2/3 to 3/3; host Third Refusal full 5/5. +1 Ground Assault damage active for subsequent eligible assaults. Final resources 9 Supply / 38 Manpower.|Cycle closure|
|12 / Cycle end|Minor recovery; completed narrative.|None.|Aulis Anchorage Command engaged, no fleet recovery; Hyria already full. Custodians eliminated. All other surviving Minor holdings and fleets full; no change or resurrection.|Cycle 13 Phase 0|
|13 / Phase 0 / Constructions|Periodic effects and Fleet Action reset.|None.|No automatic damage, repair or Endurance effects. Breach Litany active; other project progress unchanged. All Fleet Actions reset, including Oath at the Gate. Schoenus Defended expires as Iron Paladins turn begins; Triptolemos remains Defended until Bell-Ringa turn.|Logistics check|
|13 / Phase 0 / Logistics|Scheduled Logistics check.|None.|Not due until Cycle 15. Resources: Iron Paladins 22/24, Bell-Ringa 6/31, Order 9/38 (Supply/Manpower). No income or upkeep applied.|Events|
|13 / Phase 0 / Events|Roll d6 once.|None.|Check 3: no event; no event-table roll. [Opening audit](Atreus_Cycle_13_Phase_0_Rolls.json).|Iron Paladins orders|

|13 / Iron Paladins / Fleet|Anabasis and The Emperor’s Judgement jointly assault Hyria with 10 Strength; Vigilatius holds Argos.|3 Supply: 22 to 19; commit 2 Manpower: 24 to 22; victory return floor(60% of 2) = 1, to 23.|Jake reported Iron Paladin victory on 10 October 2026: “The men of the Aulis Anchorage Command tried to use every alley way and hiding spot they could to avoid being wiped out, but nothing can escape the tide of Iron.” Human result; no AI roll. 3 damage reduces Hyria 8/8 to 5/8; still Command-controlled. No capture or Planet Fall. Both attacking fleets remain 5/5, actions spent; Vigilatius 5/5, unused. Unanswered Muster remains 3/5. [Battle record](Atreus_Cycle_13_Hyria_Battle.json).|None|
|13 / Iron Paladins / Faction|Reinforce through The Iron Tithe after battle.|+8 Supply: 19 to 27.|Resolved after battle; no effect on battle starting resources.|None|
|13 / Iron Paladins / Social|No action.|None.|No change.|None|
|13 / Iron Paladins / Construction|Continue Gene-Seed Vaults on Heraion.|5 Supply: 27 to 22.|Progress and Integrity 2/5 to 3/5, unfinished and inactive; host full 4/4. Final resources 22 Supply / 23 Manpower. Cycle 13 remains open.|WAAAGH! Bell-Ringa orders|

|13 / WAAAGH! Bell-Ringa / Fleet|Gate-Krasha 7/7 and Da Fist 5/5 jointly assault Daeira with 12 Strength; Backhand holds Calydon.|1 Supply: 6 to 5; commit 2 Manpower: 31 to 29; no recovery on defeat. Order commits 1 Supply / 1 Manpower: 9/38 to 8/37; winning returns floor(80% of 1) Supply and floor(60% of 1) Manpower both 0.|AI defeat 22 to 23: attacker d20 4 +12 Strength +1 Supply +5 Manpower; defender d20 4 +11 Strength +1 Supply +7 Manpower. Daeira stays Order-controlled at 1/2; no damage, capture or Planet Fall. All fleets unchanged; both Ork attacking actions spent, Backhand unused. Triptolemos Defended expired at turn start. [Saved roll](Atreus_Cycle_13_Daeira_Battle.json).|None|
|13 / WAAAGH! Bell-Ringa / Faction|Reinforce after assault.|+3 Supply: 5 to 8.|Final resources 8 Supply / 29 Manpower; Order 8 Supply / 37 Manpower after defence.|None|
|13 / WAAAGH! Bell-Ringa / Social|No action.|None.|No change.|None|
|13 / WAAAGH! Bell-Ringa / Construction|Pause Da Iron Gob upgrade.|None.|Upgrade progress 3/5; Integrity 8/10. Base +7 Supply per Logistics Cycle remains active. Cycle 13 remains open.|Order of Saint Erigone orders|

|13 / Order of Saint Erigone / Fleet|First move Third Refusal with Breach Litany from Delphi to Eleusis; then Escort and Procession jointly assault Triptolemos; then Expand Oath at the Gate at Erigone.|Movement free. Assault 2 Supply / 2 Manpower: 8/37 to 6/35; no return on defeat. Orks commit 2 Supply / 1 Manpower: 8/29 to 6/28; victory returns 1 Supply and 0 Manpower, ending 7/28. Oath expansion 1/1: Order 6/35 to 5/34.|AI defeat 19 to 30: attacker d20 1 +10 Strength +1 Supply +7 Manpower; defender d20 12 +12 Strength +1 Supply +5 Manpower. Triptolemos stays Ork-controlled at 3/4; no damage or Planet Fall. Third Refusal cannot join after moving; Breach Litany adds no damage to other fleets. Oath 1/5 to 3/5. All four Order actions spent; fleet strength otherwise unchanged. Final Void Superiority Order 18 to Orks 12. [Saved roll](Atreus_Cycle_13_Triptolemos_Battle.json).|None|
|13 / Order of Saint Erigone / Faction|Reinforce.|+3 Supply: 5 to 8.|Resolved after Fleet actions.|None|
|13 / Order of Saint Erigone / Social|No action.|None.|No change.|None|
|13 / Order of Saint Erigone / Construction|Begin The Watch of Daeira, Minor System Defence Platform in Eleusis.|3 Supply: 8 to 5.|Progress and Integrity 1/3, unfinished and inactive. Order presence and Void Superiority 18 to 12 satisfy System construction access. Future +5 defender Fleet Battle roll; no current bonus. Final resources 5 Supply / 34 Manpower.|Cycle closure|
|13 / Cycle end|Minor recovery; completed narrative.|None.|Hyria attacked, no defence recovery; Aulis Anchorage Command engaged, no fleet recovery. Other surviving Minor holdings and fleets full; no change or resurrection. Major holdings gain no ordinary free repair.|Cycle 14 Phase 0|
|14 / Phase 0 / Constructions|Periodic effects and Fleet Action reset.|None.|No automatic damage, repair or Endurance effects. Watch of Daeira 1/3 inactive; all other progress and Integrity retained. All Fleet Actions reset; no Defended status remains active.|Logistics check|
|14 / Phase 0 / Logistics|Scheduled Logistics check.|None.|Not due until Cycle 15. Resources: Iron Paladins 22/23, Bell-Ringa 7/28, Order 5/34 (Supply/Manpower). No income or upkeep applied.|Events|
|14 / Phase 0 / Events|Roll d6 once.|None.|Check 5: no event; no event-table roll. [Opening audit](Atreus_Cycle_14_Phase_0_Rolls.json).|Iron Paladins orders|

## Cycle Records

### Cycle 1 - Foundries and burial gates

On Tiryns, the Iron Paladins turned their attention to the means of sustaining the war ahead. Anabasis remained in Argos while military stores were replenished and work began on The Forge of Iron beneath the fortress-monastery's industrial skyline. Its workshops were still a promise of future production; the Chapter's existing stores carried the undertaking.

In Calydon, Bell-Ringa's first assault broke the Calydonian Labour Defence's hold on Olenos. The mining settlements and burial-grey slag ridges passed into Ork hands, while The Last Shift emerged from the loss badly diminished. Pleuron remained beyond the Warboss's control. At Da Bellworks, replenishment and the beginnings of another forge accompanied the conquest, giving the expanding war host work to return to between battles.

The Order advanced upon Daeira's funerary settlements and overcame the Synod's defenders. The Locked Reliquary survived the fall of the world with its fighting strength severely reduced, and the Synod retained Triptolemos. Back on Erigone, new musters gathered as work began on The Vigil of the Three Refusals. The Order had gained ground, but the academy's promised flow of trained replacements still lay ahead.

No communiques passed between the Major powers. Each had committed to a new construction; two had taken their first hostile holdings. The next Cycle had yet to open.

### Cycle 2 - Repairs beneath closed skies

The storm battered the fleets of Atreus and closed their passages between systems. Ships already crippled by the fall of Olenos and Daeira were lost, along with two smaller Minor formations. Surviving local squadrons attended to what damage their remaining crews could repair.

At Tiryns, the Iron Paladins restored Anabasis, replenished their military stores and continued work on The Forge of Iron. Bell-Ringa's Meks brought Da Gate-Krasha back to fighting condition while the foundries of Da Bellworks supplied the next stage of his forge. At Erigone, The Third Refusal returned to readiness and work continued on The Vigil of the Three Refusals.

No new assault was launched. Olenos and Daeira remained damaged conquests, and the three new construction projects remained unfinished. When the storm passed, the Major fleets were ready again. The next scheduled deliveries reached their holdings, with provisions set aside to sustain the ships before another round of orders.

### Cycle 3 - Levy camps and broken lines

The Iron Paladins carried Prosymna in an overwhelming victory. The Council's levy positions fell, and its recruiting estates and grain stores passed into the Warsmith's keeping. Damas retained Heraion, but the loss left his remaining fleet badly weakened. Anabasis held its strength above the newly claimed world.

In Calydon, Bell-Ringa's mobs broke into Pleuron's industrial districts, driving the labour defence back through workshops and barricaded crossings. Marshal Oineus held enough ground to continue the resistance. The Orks had breached his defences, but Pleuron remained beyond their control.

The Order advanced through Triptolemos's shrine settlements and broke part of the Synod's defensive line. Prelate Lysandra's forces withdrew from the lost positions without surrendering the world. The Third Refusal remained intact above Eleusis as the Sisters prepared to consolidate their gains.

Replenishment continued across the three Major powers. On Tiryns and Da Bellworks, work advanced on the unfinished forges; on Erigone, the Vigil of the Three Refusals drew closer to completion. None was yet ready to sustain the armies in the field.

No communiques passed between the Major powers. Prosymna joined the Paladins' holdings, while Pleuron and Triptolemos remained contested objectives. Elsewhere, House Atreides restored The Copper Hawk as its fleets recovered from the earlier storm.

### Cycle 4 - Gatehouses and stubborn lines

The Iron Paladins broke through Heraion's defensive belts in an overwhelming victory. The Council retained its tithe citadel and enough ground to continue the fight, but its hold on the world was weakened. Anabasis remained intact, while the Warsmith's forces restored Prosymna's damaged positions and strengthened the watch over its roads and stores.

In Calydon, Bell-Ringa's renewed assault met resistance that his mobs could not overcome. The labour defence held Pleuron's battered lines, denying the Orks their conquest. Da Gate-Krasha remained above the system as the war host replenished its stores and work continued at Da Bellworks.

The Order carried Triptolemos. Its gatehouses and cathedral granaries passed into the Sisters' hands, ending the Eleusinian Synod's independent hold on the system. The Third Refusal survived intact, and the Order began securing the damaged world alongside its earlier conquest of Daeira.

Work advanced on the Forge of Iron, the Orks' forge and the Vigil of the Three Refusals. All remained unfinished. Away from the fighting, House Atreides restored Perseia's Breakwater. No communiques passed between the Major powers; the Cycle closed with the Order holding all of Eleusis, the Paladins pressing Heraion and Bell-Ringa still facing defiance on Pleuron.

### Cycle 5 - The foundries awaken

The Iron Paladins carried Heraion in an overwhelming victory. The Council's last positions fell, and the destruction of The Unspent Levy ended its remaining military presence in Argos. The Chapter now held the system's worlds, with battered Heraion joining Tiryns and Prosymna under the Warsmith's protection. On Tiryns, the Forge of Iron was completed and made ready to supply the campaigns ahead.

Bell-Ringa returned to Pleuron, but the labour defence again held against his mobs. The world remained defiant despite its damaged lines. At Da Bellworks, the Meks completed their forge, giving the war host a new source of materiel as its existing stores dwindled.

The Order kept The Third Refusal in Eleusis and turned to securing Triptolemos. Sisters restored much of the damaged defensive line and strengthened its crossings. On Erigone, the Vigil of the Three Refusals was completed, ready to train replacements for the Order's continuing war.

House Atreides finished restoring The Dendra Covenant away from the fighting. No communiques passed between the Major powers. The Cycle closed with Argos and Eleusis secured by their conquerors, while Pleuron's defenders continued to deny Bell-Ringa control of Calydon.

### Cycle 6 — Beyond the home fires

The Iron Paladins consolidated their conquest of Argos. On Heraion, battered barrack lines and rail approaches were repaired and garrisoned, securing the depots won from the Muster Council. Anabasis remained in system while the Warsmith committed the workshops of Tiryns to a larger undertaking. The Forge of Iron continued its work as new halls and machinery began to take shape around it.

Bell-Ringa finally broke the resistance on Pleuron. Ork mobs poured into the factory districts, overran the railway barricades and seized the militia's remaining machine shops. The Calydonian Labour Defence ceased to hold any ground, leaving the system in the Warboss's hands. At Da Bellworks, Da Fist joined the gathering fleet, while work began on Da Jaw-Breaka aboard Da Gate-Krasha.

The Order looked beyond Eleusis. The Third Refusal departed for Delphi, where the arrival of Althaia's fleet challenged the Delphic Custodians' control of the void. Their warship remained in place, and no battle was fought. Back at Erigone, The Returning Escort entered service to maintain the Order's presence at home. The Breach Litany remained deferred, with no shipyard available to support its construction in Delphi.

No communiques passed between the Major powers. The Cycle closed with the Paladins strengthening their holdings, Bell-Ringa master of Calydon, and the Order's advance fleet facing a new enemy beyond its home system.

### Cycle 7 — A foothold in Delphi

Anabasis held the watch over Argos as The Emperor’s Judgement entered service at Tiryns. Around the working furnaces of the Grand Forge, the Paladins continued the expansion of their industrial halls. Heraion's garrison held its repaired positions while the Chapter committed its resources to the fleet and forge.

In Calydon, Bell-Ringa gathered strength after the conquest of Pleuron. Da Fist received additional ships at Da Bellworks, while the Meks continued work on Da Jaw-Breaka with Da Gate-Krasha remaining at the shipyard. No new assault drew the Orks away from their captured system.

The Order struck at Castalia. The Third Refusal carried Althaia's forces against the Lotus Company's basin city, where the privateers' positions fell and their last territorial foothold was taken. Sisters secured the reservoir compounds and restored the landing approaches. Work began on Castalia Anchorage above the newly occupied world, though the yard was not yet ready to serve the fleet. The Delphic Custodians retained their own holdings and warship, leaving the Order with a foothold in a system still contested by a separate enemy.

At Erigone, The Returning Escort was strengthened to maintain the Order's presence at home. No communiques passed between the Major powers as the Cycle closed.

### Cycle 8 — The relay falls

The Iron Paladins strengthened The Emperor’s Judgement at Tiryns while Anabasis held its station in Argos. On Heraion, the remaining damaged positions were restored and the garrison placed on a heightened watch. Work continued around the Grand Forge's operating halls, expanding the industrial complex without interrupting its existing output.

Bell-Ringa consolidated his own conquests. Pleuron's approaches bristled with reinforced scrap barricades, and Da Fist returned to full fighting strength. At Da Bellworks, the Meks completed Da Jaw-Breaka, adding its weight to Da Gate-Krasha as the growing fleet waited in Calydon.

In Delphi, the Order carried the assault into Omphalos Relay. Sisters seized the station's transit hubs and hardened message vaults, taking the relay from the Delphic Custodians. The loss left The Sealed Testimony diminished, but Manto retained Corycia and Pytho and a surviving fleet with which to resist. The Third Refusal remained intact above the Order's new footholds.

The Returning Escort was brought to full strength at Erigone. Construction continued at Castalia Anchorage, where the unfinished yard awaited further work before it could service the Order's ships. No communiques passed between the Major powers as the Cycle ended.

### Cycle 9 — New fronts

The Iron Paladins brought The Emperor’s Judgement to full strength and commissioned Vigilatius at Tiryns. Anabasis remained in Argos while work continued on the Grand Forge, its existing halls maintaining production beneath the growing expansion.

Bell-Ringa sent Da Gate-Krasha and Da Fist into Lerna. Their combined strength overshadowed the Directorate's ships and the Rustjaw Mob, but no assault followed their arrival. Da Backhand entered service at Da Bellworks, where the Meks began expanding Da Iron Gob around its working furnaces.

In Delphi, the Order seized Corycia's archive entrances and bridgeheads. The loss destroyed The Sealed Testimony, leaving the Delphic Custodians holding Pytho without a surviving fleet. Castalia Anchorage was completed, giving Althaia an operational shipyard in the system.

The Returning Escort departed Eleusis for Calydon, where it confronted the newly commissioned Da Backhand without opening battle. The Unbroken Procession took up the Order's presence at Erigone. With the Ork main fleet in Lerna and the Order's ships above Da Bellworks, the Cycle ended with the Major powers facing each other directly in the void.

### Cycle 10 — A narrow withdrawal

The supply crisis strained the armies of Atreus. The Iron Paladins replenished their military stores and strengthened Vigilatius while Anabasis and The Emperor’s Judgement held in Argos. At Tiryns, the Grand Forge's expansion was completed, bringing its new halls into production.

Bell-Ringa recalled Da Gate-Krasha and Da Fist from Lerna. Their return, together with the strengthening of Da Backhand, restored Ork superiority above Calydon. The Returning Escort withdrew to Delphi without battle. Work on Da Iron Gob's expansion paused as the Warboss replenished his stores, its existing furnaces continuing to serve the host.

The Third Refusal struck Pytho before the returning fleet arrived. The Order broke the outer defensive districts, but the Custodians retained their inner archives and astropathic precinct. At Castalia Anchorage, work began on The Breach Litany aboard The Third Refusal, while The Unbroken Procession was expanded at Erigone.

The Cycle closed with the Order's advance fleets gathered in Delphi and the Ork fleets back over their own holdings. No communiques passed between the Major powers.

### Cycle 11 — The wardens hold

The Emperor’s Judgement entered Aulis and met the strength of The Unanswered Muster without opening battle. In Argos, Vigilatius was brought to full readiness while Anabasis held its station. The Iron Paladins replenished their ranks and began the Gene-Seed Vaults on Heraion.

Bell-Ringa sent Da Gate-Krasha and Da Fist into Eleusis. Da Backhand was strengthened at Da Bellworks, where work resumed on Da Iron Gob's expansion. The Ork ships arrived above the Order's home holdings while Althaia's advance fleet remained committed elsewhere.

At Pytho, the Delphic Custodians held their remaining lines. The Third Refusal's assault failed to break the inner defences, and the Order gained no further ground. Work continued on The Breach Litany in Delphi.

The Returning Escort moved back to Eleusis, joining the newly reinforced Unbroken Procession. Together they faced the larger Ork presence, but neither side fought a fleet engagement. The Cycle ended with opposing fleets gathered above the Order's home system and the Custodians still resisting on Pytho.

### Cycle 12 — A wave of iron

Anabasis joined The Emperor’s Judgement in Aulis before the assault on Schoenus. The Anchorage Command’s shore troops put up worthy resistance among the causeways and fuel depots, but were eventually overwhelmed by the Iron Paladins. The victors repaired the coastal positions and secured the cargo piers. The Unanswered Muster survived the fall of the world in diminished strength, while the Command retained its headquarters on Hyria. On Heraion, work continued on the Gene-Seed Vaults.

In Eleusis, Bell-Ringa committed Da Gate-Krasha and Da Fist against Triptolemos. The Orks broke through the Order’s positions and seized the cathedral granaries and surrounding estates. Scrap barricades rose along the canal crossings as the mobs consolidated their prize. The Returning Escort and The Unbroken Procession suffered in the fall, then returned to Erigone’s shipyard to restore their strength. Da Backhand held Calydon while the expansion of Da Iron Gob continued.

The Order answered its loss at home with the capture of Pytho. The Custodians defended their inner archives fiercely, but The Third Refusal’s assault finally broke their resistance. With their last world taken and their fleet already destroyed, the Delphic Custodians ceased to exist as an independent territorial power. Sisters occupied the damaged transmission courts and astropathic precinct, bringing all Delphi’s holdings under Althaia’s control.

The Oath at the Gate entered service at Erigone. In Delphi, Castalia Anchorage completed The Breach Litany aboard The Third Refusal after the fighting. The Cycle closed with the Order established across Delphi but facing the larger Ork force over its home system. No communiques passed between the Major powers.

### Cycle 13 — The homeward fleet

Anabasis and The Emperor’s Judgement struck Hyria together. The Anchorage Command’s troops used alleyways and concealed positions to resist the advance, but the Iron Paladins drove them from the outer districts. The naval support world remained in the Command’s hands, its damaged defences still covering the traffic-control citadel and embarkation fields. The Paladins replenished their stores while work continued on the Gene-Seed Vaults at Heraion.

Bell-Ringa sent his main force against Daeira. The Order’s Sisters held the battered approaches among the tomb fields and burial gates, narrowly repelling the Orks. Da Gate-Krasha and Da Fist remained in Eleusis, while Da Backhand held Calydon. The Warboss replenished his stores and left Da Iron Gob’s expansion paused around its working furnaces.

The Third Refusal returned from Delphi with The Breach Litany aboard, joining the Order’s ships in Eleusis. The Returning Escort and The Unbroken Procession then carried the counterattack against Triptolemos. The Orks held the canal crossings and cathedral granaries, repelling the Sisters and retaining their foothold in the Order’s home system.

At Erigone, The Oath at the Gate was strengthened. With its fleets now concentrated in Eleusis, the Order gained superiority in the void despite the failed landing. Work began on The Watch of Daeira, a defensive platform intended to support the system’s fleet defences. It remained unfinished as the Cycle closed. No communiques passed between the Major powers.

## Pinned rules appendix

The following is the complete adopted 6 October edition. The explicit Atreus setup conventions above supply scenario-specific names, ownership, opening fleet strength, diplomacy and victory conditions. This is a frozen copy; later source-library edits require an agreed migration.


# Soulstorm campaign rules — current playtest edition

6 October 2026. This is the consolidated source for the selected decision/recovery package of 6 October, including its inherited rules and approved campaign conventions. It supersedes conflicting numerical rules in the 15 September baseline, 27 September draft and intermediate proposals. Do not combine their trait values with this edition.

This is a playtest release, not a claim of final balance. The latest 200-game comparison reduced the observed highest-to-lowest trait win-rate spread from 32 to 28 percentage points; it remains above the requested 25-point target. AI campaign results do not predict human Soulstorm win rates. Sector design, the global Soulstorm difficulty problem and the mod project remain deferred. Historical source, frozen studies and suspended Dessica Cycle 21 are unchanged.

For a new campaign, copy the templates, pin this edition and record local exceptions before play. The source is reusable; the campaign ledger alone records current resources, outcomes and characters. The reconciliation record is Source_Reconciliation_2026-10-06.txt.

## Setup, resources and personnel

New roster-building Subsector Major factions begin with 20 Supply and 20 Manpower, capped at 100 each. Both represent military resources, not the civilian economy. Use one agreed rules version and record exceptions before play. Only Major Factions have Alignments. Minor Factions have none; force species does not confer alliance. Independent remains a Major Alignment, never an automatic alliance. Fleets measure combat effectiveness, not a literal ship count.

Establish the Subsector's fixed raiding faction at setup; raiders cannot hold territory. Dessica's raiders remain Iron Warriors. Generate ordinary systems from the d20 table below: 2–4 combined planets/stations, averaging 3. Minor Factions cannot hold Capital-tier planets or stations, including prize factions.

### Faction Alignments

**7 October 2026 creator correction:** Alignments apply only to Major Factions. Majors sharing a non-Independent Alignment are allied by default unless an explicit hostility exception is recorded, such as the Atreus Sisters and Iron Paladins. Different Major Alignments are hostile without an applicable agreement; two Independent Majors are not automatically allied.

Minor Factions have no Alignment and cannot enter diplomatic agreements or alliances. They are hostile to other factions; species, force representation and narrative worship do not make them allied. A Minor absorbed into a Major is no longer a separate aligned Minor. The Alignment column below applies only when the force is a Major; the manpower and representation guidance applies to both roles.

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

### Personnel lifespan reference — 20 September 2026

Place this reference alongside the Manpower conversion table. These describe personnel, not the age of a faction or its entire Manpower pool. Numeric campaign defaults below are provisional house assumptions, not universal canonical death ages. Track biological age separately from time spent in stasis or distorted Warp time. No Cycle-to-years conversion is introduced here.

| Personnel profile | Lifespan guidance for campaign records |
|---|---|
| Unaugmented humans: Guard, Sisters, mortal Traitor Guard, human Independents | Proposed natural-age reference: 60–100 Terran years where living conditions and medical care permit. This is a house range, not average Imperial life expectancy or a mandatory retirement age. |
| Humans with sustained rejuvenation | Centuries are possible; proposed record range 200–400 years, adjusted for the specific treatment and character. Not automatically available to all human personnel. |
| Space Marines and Grey Knights | Centuries; exceptional individuals exceed a millennium. No established universal natural death age: record individual history rather than imposing a fabricated species expiry. |
| Chaos Space Marines | Astartes baseline, modified by recorded Warp exposure and supernatural effects. Calendar age is not automatically biological age. |
| Craftworld Aeldari and Harlequins | Millennial lifespans; approximately 1,000–2,000+ years as broad reference, not a hard maximum. Individual and psychic exceptions apply. |
| Drukhari | Record Aeldari ancestry plus rejuvenation/reconstruction arrangements; no automatic old-age deadline while sustained by those arrangements. |
| T'au | Approximately 40 Terran years ordinarily. Record stasis, exceptional medicine or other established life extension separately. |
| Orks | No dependable natural maximum specified here; do not invent an automatic old-age death. |
| Necrons | No ordinary biological ageing; destruction, degradation and personality loss are distinct narrative events. |
| Tyranids | Bioform-specific lifespan and recycling; persistent command identity is not necessarily the same biological body. No species-wide age band. |
| Chaos Daemons | No ordinary biological lifespan; banishment and destruction follow their narrative circumstances. |
| Adeptus Mechanicus | Human baseline modified individually by augmentation and rejuvenation; heavily augmented personnel may endure for centuries or longer. |
| Independent or mixed-species personnel | Use the actual individual's species and recorded life extension; Independent is not a species. |

Reference sources for numerical anchors: [human rejuvenation](https://wh40k.lexicanum.com/mediawiki/index.php?title=Rejuvenat), [T'au physiology](https://wh40k.lexicanum.com/mediawiki/index.php?title=T%27au), and [Aeldari](https://wh40k.lexicanum.com/wiki/Aeldari). These are lore reference summaries; proposed human ranges are campaign conventions. Major factions select narrative succession; the referee manages Minor personnel. Succession retains the faction trait. Agree any finite character death window when establishing that character, rather than retroactively assigning one.

## Faction traits

Narrative names do not change the following mechanics. Each faction uses one profile. Income and refunds respect the resource cap and deficit locks.

| Trait | Current effect |
|---|---|
| Mobile Capital | Starts with a 12/12 Mobile Capital instead of an ordinary starting fleet. Grants 4 Supply and 4 Manpower each Logistics Cycle, a built-in shipyard and support for planetary constructions. No Mobile Capital upkeep. Its intrinsic hull contributes floor((6 × current hull + 5) / 10) combat Strength: 7 at 12 hull. Added permanent Fleet-construction Strength contributes in full and takes damage before intrinsic hull. Losing the Mobile Capital permanently removes the trait. |
| War Economy | +6 Supply each Logistics Cycle. |
| Martial Culture | +4 Manpower each Logistics Cycle. |
| Efficient Logistics | Reinforce grants 8 Supply; Muster grants 8 Manpower, instead of the normal 3. These are total action yields. |
| Salvagers | +3 Supply on a qualifying victory; +1 on defeat or draw; +1 additional Supply on capture. Ground battles, Fleet Battles and guarded Structure Assaults qualify, once per participating faction per engagement. Uncontested bombardment and unguarded Structure Assaults do not. If raiders win, both main factions receive the defeat reward. |
| Void Supremacy | Ordinary Expand Fleet restores up to 4 Strength for 1 Supply and 1 Manpower, without a shipyard. Ordinary fleet upkeep is 0 Supply and ceil(number of living ordinary fleets / 2) Manpower. Creation still needs a yard; this does not improve Mobile Capital self-repair. |
| Swift Mobilization | Create Fleet produces 6/6 for 1 Supply and 1 Manpower. Its base capacity remains 6; existing starting fleets are not enlarged retroactively. The new fleet cannot act that Cycle. Ordinary fleet upkeep is ceil(number of living ordinary fleets / 2) of each resource. Expand remains the normal +2. |
| Fleet Endurance | Each Cycle, before events, restore up to 2 Strength to every surviving fleet, capped at its actual maximum. Ordinary fleet upkeep is ceil(number of living ordinary fleets / 2) of each resource. No resurrection or Integrity repair. |
| Siege Doctrine | Ground Assault base Supply cost is ceil(holding tier / 2); enemy surcharges are not halved. Ignore Defended. Victory adds 1 damage above the ordinary +1 breakthrough; defeat deals 1 before mitigation. On victory, recover 2 additional committed Manpower, capped at commitment, and refund 1 paid base Supply. No refund funds the attack in advance; no surcharge refund or non-victory refund. |
| Dread Reputation | Each attack against this faction costs the initiator an additional 2 + max(1, ceil(declared participating combat Strength / 5)) of BOTH Supply and Manpower. Calculate before initiation losses or cannons, including ground-only Strength for a Ground Assault. Charge once for the combined group, including allied assets. Applies to ground, naval, bombardment and targeted construction attacks. This Manpower is expenditure, not recoverable commitment. No Soulstorm difficulty modifier. |
| Fortification Experts | The holding/Mobile Capital Defend action costs no resources, restores up to 4 defence, grants Defended and grants 2 Supply. It still uses the Faction Action, including when defending a full holding. No Manpower grant, Integrity repair or construction discount. |
| Industrial Efficiency | Each Build or Upgrade action costs 3 less Supply, minimum 1. A new project begins at 2 Integrity; subsequent Build and Upgrade actions add the normal 1. Repair is unchanged. |

## Cycle sequence and resources

**Phase 0 happens once globally (there is no separate second event phase):** snapshot and resolve periodic construction damage; apply surviving eligible repair/regeneration effects; resolve Logistics on Cycles 3, 6, 9…; then make the single event check. Endurance recovery precedes events. No faction gets a second copy on its own turn. Destruction precedes repair, and destroyed assets cannot regenerate.

Logistics grants Supply and Manpower equal to owned holding tiers: Minor 1, Standard 2, Major 3, Capital 4, plus active constructions and traits. Ordinary living fleets normally cost 1 of each resource per Logistics Cycle; apply the trait upkeep exceptions above. Credit income up to the 100 cap first, then deduct upkeep; income above the cap is not banked against upkeep. Mobile Capitals do not pay ordinary fleet upkeep. Existing deficit locks suppress their affected resource's income and penalties.

Each Major then completes Phase 2 Fleet actions, one Phase 3 Faction action, one Phase 4 Social action and one Phase 5 Construction action in that order. Resolve each attack before dependent later actions. A player battle pauses the turn for the reported result; do not update GitHub with unresolved projected outcomes. At Cycle end resolve eligible Minor recovery and record the narrative, then advance the Cycle and begin the next Phase 0. Defended expires at the start of the owning faction's next turn. Attacked/engaged flags govern the relevant recovery interval and are cleared only after that recovery has been assessed. Narration uses in-world language; mechanical records remain separate.

**Voluntary expenditure must leave each resource spent above 0.** Involuntary losses may trigger deficits. Automatic defensive commitment is calculated for the battle but the final actual loss is settled once, after the attack on the attacker's turn. Planet Fall replaces ordinary defeat Supply loss rather than adding it twice. It is not the voluntary Defend action.

## Fleet and Faction actions

- Every fleet has one offensive/movement Fleet Action per Cycle, including consented participation on an ally's turn. Defending is automatic and consumes no action, even after an earlier action.
- Move to any system in the Subsector: map directions describe location, not adjacency or extra travel distance. Storms prevent ordinary movement. Only an explicit ability such as Scout combines movement and attack.
- Expand at an available yard: 1 Supply and 1 Manpower for+2 strength, capped at actual maximum, subject to trait exceptions.
- Create Fleet uses the Faction Action at an available yard: 1 Supply and 1 Manpower, normally 1/5. Yard/trait starting strengths use the best applicable value, not an additive stack. The new fleet takes no Fleet Action that Cycle.
- Reinforce gives 3 Supply; Muster gives 3 Manpower; Efficient Logistics gives 8. Rationing replaces the relevant action while its resource is locked.
- Defend a holding or Mobile Capital costs its tier in each resource, restores that much defence, and grants Defended until the next turn. Fortification uses its listed exception. Full-defence hosts can receive Defended without extra restoration.
- Fleet Transfer/Merge require co-location and Void Superiority; only the initiator spends an action. A Transfer donor retains at least 1; transfer amounts respect actual capacity. A Merge absorbs the other fleet completely without a fleet-destruction penalty. Its constructions transfer, including permanent capacity. Keep the absorbing fleet's base capacity and add the absorbed fleet's permanent construction capacity, not its ordinary base capacity. Excess combined current Strength above that surviving capacity is lost. Mobile Capitals cannot be transferred or merged.
- Garrison Transfer may distribute defence within a system. Donors normally start full and always retain 1; recipients cannot exceed maximum. An active Landing Zones recipient permits damaged donors. This uses the Faction Action.
- Scuttle a fleet with Void Superiority, using its Fleet Action, to recover floor(current Strength / 2) Supply. Apply destruction penalties before the refund; it cannot fund an otherwise illegal voluntary action. A Mobile Capital also incurs its Capital penalties and permanently loses its trait. Scuttling cannot cause a resource deficit.


### Holdings, Void Superiority and action timing

| Holding tier | Normal defence | Logistics income (each resource) | Ground Assault base Supply | Normal Defend cost (each resource) and restoration |
|---|---:|---:|---:|---:|
| Minor | 2 | 1 | 1 | 1 |
| Standard | 4 | 2 | 2 | 2 |
| Major | 8 | 3 | 3 | 3 |
| Capital | 12 | 4 | 4 | 4 |

Planets and stations use the same tier rules. Void Superiority means the total friendly combat Strength in a system strictly exceeds total hostile combat Strength; a tie is contested. Include allied fleets and Mobile Capitals. This is different from uncontested bombardment, which requires no hostile fleet at all. A full holding may still take Defend to gain Defended. Ordinary Defend restores the tier amount, capped at maximum; Fortification replaces that amount with 4. Active Militia Barracks removes the holding Defend action's Manpower cost, not its normal Supply cost.

A Mobile Capital may spend its Fleet Action and 1 Supply / 1 Manpower to Expand itself by up to 2 defence. This does not grant Defended or repair attached Integrity. Its Faction-action Defend normally costs 4 of each resource and restores up to 4. Its actual defence, not its reduced combat contribution, determines whether its construction host is full.

Establish New Capital is compulsory when applicable. An established Capital's built-in Orbital Shipyard costs no construction action, Supply or slot. Normal fleets have base capacity 5 unless a rule explicitly changes it. Repair and expansion use actual capacity, including permanent additions.

### Summon Allies

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

**Summoned capital — ruling, 16 September 2026:** The new faction chooses an existing planet or station in the ceded system as its provisional capital and performs Establish New Capital normally. Summoning grants no free defence increase or built-in shipyard; the shipyard becomes available only when establishment is complete. The faction still starts with 10 Supply, 10 Manpower and no fleet, and takes its first turn immediately after its summoner.

**Independent summoners:** Record an explicit subordinate pact when an Independent-aligned faction summons an ally. Shared Independent Alignment alone never allies unrelated factions. Sector-level grant and roster consequences remain undefined.

**Multiple Factions:** You may have multiple factions of the same type in play (e.g., two Space Marine Chapters, three Drukhari Archons). Each operates independently but remains aligned with their summoner.

### Phase 4: Social Action

A faction may take ONE Social Action per turn. This represents diplomatic bandwidth.

| Action | Effect |
|--------|--------|
| **Communiqué** | Send one message to another Major Faction. They may respond immediately but only once. Requires both Factions to have a presence in the same system (fleet or planet — any combination). Extended conversations require multiple cycles. |

#### Diplomacy between Major Factions

**Diplomacy between Major Factions:** Temporary cease-fires or non-aggression pacts with other Major Factions outside your alignment are possible through the Communiqué action, but these are inherently unstable. Conflicting alignments will inevitably come to blows — such arrangements should be treated as temporary strategic convenience, not true alliance.

## Combat and capture

**Ground Assault:** available even with hostile fleets present. Only committed fleets contribute. Apply Orbital Cannons to the largest attacker before strength and Manpower commitment. A legal assault needs at least 5 ground Strength after projected cannon damage. Commit floor(participating ground Strength / 5) Manpower. Pay world-tier Supply, or Siege's reduced cost, plus any Dread surcharge. Check affordability for the whole expenditure, not each component in isolation. Ground Strength includes Carrier/Assault Boats; flat Bay/Platform damage does not increase attacker commitment. There is no naval initiation loss for a Ground Assault.

A Mobile Capital can be targeted by Ground Assault like a Capital, but is destroyed at zero rather than captured. It cannot be uncontested-bombarded while alive. Orbital Cannons also fire against bombardment; Dread is assessed before cannons, while ordinary attack Strength and costs use the surviving group. Attached projects lose Integrity only for actual host damage, capped at the host's remaining defence, not overkill.

If cannons destroy the entire attacking group on approach, cancel the assault before ordinary Supply and Manpower commitment; spent actions and the earlier Dread charge remain spent. No ground battle or capture occurs. This failed approach is not an exception allowing a surviving group below 5 ground Strength to launch a ground battle.

Successful damage = floor(ground strength/5)+1, plus applicable trait/construction damage, after mitigation. Ordinary defeat causes no ground damage; Siege causes 1. Capture at 0 resets the holding to 1 defence. The attacker normally recovers floor(60% committed Manpower) on victory. Best participating Troop Transport adds 2 returned Manpower, 4 upgraded, capped at commitment; transports do not stack. This is the accepted replacement for historical 70%/80% transport wording.

For the attacking side use committed ground Strength; for the defending side use eligible in-system defending fleets' combat Strength, not the holding's defence and not ground-only Carrier/Assault Boats bonuses. AI ground totals use d20 + the applicable side's strength + floor(Supply/5) + floor(Manpower/5), using post-commitment resources. Defended gives defender+4 unless Siege; Ambush+4 to defender; Intel+4 to attacker; Bunker+4/+8; Isolated Defence−8. Ties favour the defender. AI defenders commit floor(incoming damage/2) Manpower and normal tier Supply limited to available stock; winning defenders recover 60% committed Manpower and 80% committed Supply, rounded down. In a human-resolved engagement, defensive commitment is full incoming potential damage and winning defensive Manpower recovery is 80%. Incoming potential damage includes breakthrough and flat damage bonuses before mitigation, not just points actually removed from the host. Militia removes defensive commitment/isolation. Forced Conscription draws the required defence from other fully defended owned donor holdings, leaving at least 1 each; these need not be in the attacked system. It substitutes for the commitment, not for resources in a deficit pool. Without affordable commitment or adequate conscription, the defence is Isolated. A losing attacker against an Isolated defence retains the inherited exception: floor(60% commitment) plus 1/2 for the best base/upgraded Transport, capped at commitment; no Siege victory bonus and no such recovery if raiders win.

**Uncontested Bombardment:** no hostile fleet presence, 0 ordinary Manpower (Dread still charges both resources), damage max(1, floor(participating combat Strength/5)); Supply cost 2×tier+that damage, plus Dread. Mitigation applies and defence cannot fall below 1. No capture or battle roll. A surviving Mobile Capital is itself defending fleet presence and prevents uncontested bombardment.

**Fleet Battle:** one initiation Strength point from one participating asset with more than 1 Strength. This expenditure does not damage attached constructions. Escort adds 3/6 to its side; defending system Defence Platforms add 5/10. Each side rolls 2d6 plus applicable strength/modifiers; a positive margin inflicts ceil(margin/3) damage on every participating losing fleet, without a damage cap. Ties inflict no combat damage; costs/actions remain spent. Destruction and attached construction damage apply normally. There is one Fleet Battle per initiating faction/system/turn; a guarded Structure Assault uses that allowance.

**Structure Assault:** target one construction. If guarded, use Fleet Battle resolution, but an attacking win damages the construction only; attacker defeat damages participating attackers normally. An unguarded target costs 2 Supply plus Dread, no ordinary Manpower commitment, and suffers max(1, floor(combat Strength/5)) Integrity damage. There is no general Integrity floor. Completed permanent Assault Cruiser/Flagship capacity is the explicit exception: its granted portion remains until the fleet dies; unfinished upgrade progress can still be damaged. Movement/attack/withdrawal require separate actions unless an ability combines them.

**Planet Fall:** captured non-Capital holdings impose 2 Supply/2 Manpower; Capitals 4/4. Replace ordinary defensive Supply loss, and add the applicable defensive Manpower loss. Fleet damage equals the final assault's resolved damage, including overkill beyond the holding's remaining defence. Apply it to the defeated owner's eligible fleets in that system. Allocate it point by point to the currently strongest eligible fleet, logging seeded/random tie choices automatically. Do not stop for a separate player allocation message. Destroy fleets with no remaining planet, station or Mobile Capital fallback. Minor factions do not lose Major resource pools. Destruction of a Major faction's fleet, including a Mobile Capital, also costs 1 Manpower; apply existing deficit locks normally.

## Capital replacement and deficits

Every owned planet or station can become the replacement Capital when the functioning Capital is lost. Establish New Capital is free, takes priority over rationing and doubles current/maximum defence toward 12. Completion requires actual 12/12; only then grant Capital tier/income and the built-in yard. Being attacked may delay completion. No holding or surviving Mobile Capital means elimination, not an endless Capital-recovery loop. A destroyed Mobile Capital permanently loses its trait and incurs 4 Supply / 4 Manpower loss plus the fleet-destruction 1 Manpower. It does not apply ordinary Planet Fall collateral damage to other fleets. Owned planets or stations still allow replacement Capital establishment. Lock the chosen provisional holding until it is lost; establishment doubles current and maximum defence, each capped at 12, without granting Capital income or the yard early.

Each resource has its own deficit track. Involuntary depletion to 0 locks that resource at 0, ignoring its income and further resource penalties while the other resource behaves normally. Entry removes 1 Strength from each surviving fleet once for that resource: Supply can destroy fleets; Manpower degradation leaves surviving fleets at least 1. Resolve simultaneous Supply first. Direct combat/construction damage remains effective.

Emergency Rationing takes a chosen Faction Action: three actions on a track restore exactly 10 total. Overlapping tracks require separate actions and the faction chooses which to advance; elapsed Cycles do not advance them. Other affordable actions remain available subject to Capital replacement priority, and ordinary Reinforce/Muster cannot bypass the corresponding deficit. Ignore income lost during the lock rather than banking it.

## Minor factions and systems

Ordinary Minor starting Fleet Strength = ceil(sum of maximum defence of owned holdings in the system/2), distributed into fleets up to 5. Prize factions use the unhalved sum. Maximum defence determines the initial fleet allocation; losing a holding does not rebuild the allocation. Apply normal Planet Fall fleet losses.

Each Minor's Supply and Manpower are separately 5 × sum(owned holding tiers), doubled for prize factions. These are shared derived values, not per-planet pools or persistent Major stockpiles. Defence damage alone does not reduce them. Minors take no turns, cannot build replacements, and lose no Major-style resource penalties. At Cycle end, each unattacked Minor holding recovers 1 defence, capped at maximum. An unengaged Minor faction restores 1 total Strength to an eligible surviving damaged fleet. Major holdings have no free ordinary recovery; they need Defend or an applicable construction.

## Construction costs, Integrity and capacity

One Construction action begins/advances one project or repairs a completed construction. **Construction baseline — approved 8 October 2026:** Every Minor construction requires 3 Build actions at 3 Supply per action (9 Supply total). Every Major construction requires 5 Build actions at 5 Supply per action (25 Supply total). Where an upgrade exists, it requires another 3 actions at 3 Supply for a Minor or 5 actions at 5 Supply for a Major. These are the undamaged baseline requirements; there are no construction-specific cost or action-count exceptions. Explicit faction-trait modifiers are defined in the trait description. Grand Orbital Shipyard is Minor. Full host defence/strength is required to Build, Upgrade or Repair; system-based constructions require an owned holding or living fleet providing presence in their system and have no host defence prerequisite. Fleet Build/Upgrade actions require an operational friendly Orbital Shipyard; System Build/Upgrade actions require Void Superiority instead, as specified below.

**Construction access — amended 9 October 2026:** Every Build or Upgrade action on a System-category construction requires Void Superiority in that system when the action resolves; no Orbital Shipyard is required. Friendly combat Strength must strictly exceed total hostile combat Strength; a tie is insufficient. If superiority is lost, construction cannot advance until it is regained. Every Fleet-category Build or Upgrade action requires the host fleet to be in a system with an operational friendly Orbital Shipyard, including an established Capital's built-in yard. Fleet creation and ordinary fleet expansion also require an eligible shipyard, subject to explicit trait or ability exceptions. A fleet may move with unfinished projects aboard: work is suspended without an eligible yard and may resume at any eligible yard. Progress and Integrity are retained subject to normal damage; suspended projects remain vulnerable to enemy attacks and host-damage Integrity loss, and are destroyed at 0 Integrity. Existing full-host, completed base-effect and Repair rules remain unchanged.

Repair restores up to 3 Integrity at 1 Supply each, no Manpower. It cannot finish unfinished construction/upgrades. A separate Faction-action Defend may repair a completed damaged construction at a full host: Minor costs 1 Supply / 1 Manpower and restores 1 Integrity; Major costs 3 of each and restores 3. Fortification Experts does not alter this construction action. Repair never completes unfinished Build/Upgrade work.

Every point of actual host damage removes 1 Integrity from every attached project. Initiation/resource expenditure is not damage. At 0, construction is destroyed regardless of source. Minor 3/Major 5, upgraded 6/10 maximum Integrity. Ordinary planetary/system constructions operate at full applicable Integrity; an upgrade retains its completed base effect while Integrity remains at least the base maximum. Newly unfinished projects give no effect.

**Persistent planetary exceptions:** once completed, Automated Defences, Regenerative Fortifications, Landing Zones, Militia Barracks, Void Shield Generator and Fortification Network retain their base effect at positive Integrity. Full upgraded Integrity is required for improved effects, except already granted Fortification Network capacity persists until destruction. Its completion adds 2 current and maximum defence, or 4 total after upgrade; repair never grants that capacity again. At destruction remove the granted maximum and cap current defence accordingly.

Completed **Fleet-category** constructions retain base effects at any positive Integrity; upgraded effects require full upgraded Integrity. Their base remains during upgrading. This category exception does not turn a planetary Forge aboard a Mobile Capital into a Fleet construction, or protect an unfinished Void Station as one. Completed Assault Cruiser/Flagship capacity remains until the fleet is destroyed. Repair never grants unrelated lost Fleet Strength.

One ordinary construction slot per holding, with its established Capital's built-in yard free and outside the slot. Consolidation is a holding development, not a permanent occupied building slot. Apply the existing shipyard/Grand Yard prerequisite chain. No new fleet/system construction cap; normal unique-profile rules and transferred fleet constructions remain. Multiple projects may exist but only one Construction action is available.

Capture applies host/construction damage first. Surviving planetary constructions transfer with remaining Integrity/progress. System constructions transfer only when one faction controls all planets and has Void Superiority: Minor transfers, Major destroyed. Completed Void Stations are holdings and use ordinary capture; an unfinished station remains attached to its construction fleet.

### Construction catalogue

The catalogue shows the baseline Supply cost per Build/Upgrade action. Minor projects and upgrades take 3 actions; Major projects and upgrades take 5. An upgrade adds another base-sized block to maximum Integrity. “No upgrade” means no separate upgraded profile. Damage may require additional work; a destroyed project must be rebuilt.


**Planetary/Orbital Constructions** — Built on a specific planet, station or eligible Mobile Capital. Affects that planet or system.

*Minor (3 actions base, 3 actions upgrade, capturable)*

| Construction | Supply per Build/Upgrade action | Base Effect | Upgraded Effect |
|---|---:|---|---|
| [Orbital Shipyard] | 3 | Allows fleet creation and ordinary expansion here; Create normally starts 1/5 | No upgrade; prerequisite for Grand Orbital Shipyard |
| [Grand Orbital Shipyard] | 3 | Minor, 3 stages: Create at 3/5; requires a shipyard, including a built-in Capital yard | Create at 5/5; best starting-Strength effect applies, not an additive stack |
| [Supply Depot] | 3 | +3 Supply per Logistics Cycle | +6 Supply per Logistics Cycle |
| [Training Grounds] | 3 | +3 Manpower per Logistics Cycle | +6 Manpower per Logistics Cycle |
| [Automated Defences] | 3 | +1 defence regen/cycle if not attacked | +2 defence regen/cycle if not attacked |
| [Bunker Network] | 3 | +4 defender roll (AI) / -1 Difficulty (Player) | +8 defender roll (AI) / -2 Difficulty (Player) |
| [Landing Zones] | 3 | Minor: Garrison Transfers to this holding may use damaged donors; donors retain 1. | No upgrade |
| [Orbital Cannons] | 3 | -1 Fleet Strength to largest hostile fleet when attacked | -2 Fleet Strength to largest hostile fleet when attacked |

*Major (5 actions base, 5 actions upgrade; surviving planetary constructions transfer on capture)*

| Construction | Supply per Build/Upgrade action | Base Effect | Upgraded Effect |
|---|---:|---|---|
| [Forge Complex] | 5 | +7 Supply per Logistics Cycle | +14 Supply per Logistics Cycle |
| [Military Academy] | 5 | +7 Manpower per Logistics Cycle | +14 Manpower per Logistics Cycle |
| [Regenerative Fortifications] | 5 | +3 defence regen/cycle if not attacked | +6 defence regen/cycle if not attacked |
| [Void Shield Generator] | 5 | -1 incoming attack damage (can reduce to 0) | -2 incoming attack damage (can reduce to 0) |
| [Fortification Network] | 5 | +2 to planet's maximum defence | +4 to planet's maximum defence |
| [Militia Barracks] | 5 | No defensive Manpower commitment or isolation; holding Defend costs no Manpower | No upgrade |
| [Planetary Shield Network] | 5 | Invulnerable with Void Superiority / Defended status without | No upgrade |
| [Consolidation Works] | 5 | Upgrade planet type by one tier: Minor (2/2) → Standard (4/4) → Major (8/8). Current and maximum defence double. **Repeatable** until Major. Cannot upgrade to Capital — only one Capital per faction. | N/A (repeatable construction, not upgradeable) |

#### Void Constructions (Fleet-Attached)

**Void Constructions (Fleet-Attached)** — Mobile, destroyed if fleet is destroyed.

*Minor (3 actions base, 3 actions upgrade)*

| Construction | Supply per Build/Upgrade action | Base Effect | Upgraded Effect |
|---|---:|---|---|
| [Troop Transport] | 3 | Victory return +2 committed Manpower | Victory return +4 committed Manpower; best transport only, cap at commitment |
| [Repair Tender] | 3 | +1 to its surviving host fleet each Cycle, even after combat | +2 to its surviving host fleet each Cycle |
| [Escort Squadron] | 3 | +3 to Fleet Battle roll | +6 to Fleet Battle roll |
| [Assault Boats] | 3 | +2 fleet strength for ground assaults | +4 fleet strength for ground assaults |
| [Bombardment Bay] | 3 | +1 ground assault damage | +2 ground assault damage |
| [Assault Cruiser] | 3 | +2/2 fleet strength (tracked separately) | +4/4 fleet strength (tracked separately) |

*Major (5 actions base, 5 actions upgrade)*

| Construction | Supply per Build/Upgrade action | Base Effect | Upgraded Effect |
|---|---:|---|---|
| [Flagship] | 5 | +5 permanent strength/capacity | +10 total permanent strength/capacity; add to existing capacity |
| [Carrier] | 5 | +10 strength for ground assaults | +20 strength for ground assaults |
| [Siege Platform] | 5 | +3 ground assault damage | +6 ground assault damage |
| [Salvage Wing] | 5 | +3 Supply per equipped victorious fleet in a Fleet Battle or attacking Ground Assault | +6; not a bombardment or Structure Assault reward |
| [Scout Squadron] | 5 | This fleet may Move and Ground Assault or Uncontested Bombardment with the same Fleet Action. Resolve movement first; eligible allies already at the destination may join, spending their own actions. | No upgrade |

#### Void Constructions (System-Based)

**Void Constructions (System-Based)** — Stationary. Use the distinct system-control capture rule above.

*Minor (3 actions base, 3 actions upgrade)*

| Construction | Supply per Build/Upgrade action | Base Effect | Upgraded Effect |
|---|---:|---|---|
| [Defence Platform] | 3 | +5 to defender roll in Fleet Battles | +10 to defender roll in Fleet Battles |

*Major (5 actions base, 5 actions upgrade)*

| Construction | Supply per Build/Upgrade action | Base Effect | Upgraded Effect |
|---|---:|---|---|
| [System Defence Station] | 5 | -1 strength to every hostile fleet in system each Cycle | -2 to every hostile fleet |
| [System Repair Station] | 5 | +1 strength to every eligible allied fleet in system each Cycle | +2 to every eligible allied fleet |
| [Logistics Anchorage] | 5 | +1 defence regen to unattacked planets/cycle | +2 defence regen to unattacked planets/cycle |
| [Void Station] | 5 | 2/2 station, functions as Minor planet | Upgrade via Consolidation Works: Minor (2/2) → Standard (4/4) → Major (8/8). Eligible for Establish New Capital when the faction has no functioning Capital. |
| [Storm Transit] | 5 | Major, 5 stages, no upgrade: protect eligible allied fleets in this system from storm damage and permit their departure during a Warp Storm. | No upgrade |


## Player battle setup and overflow

### Difficulty (Based on YOUR Supply)

Supply represents the materiel, ammunition, fuel and provisions available to sustain the battle. **Your post-commitment Supply sets the base Soulstorm difficulty.**

| Supply | Base Difficulty |
|---|---|
| 0–20 Critical | Insane 5/5 |
| 21–40 Rationed | Harder 4/5 |
| 41–60 Sustainable | Hard 3/5 |
| 61–80 Surplus | Standard 2/5 |
| 81–100 Abundant | Easy 1/5 |

### Difficulty (Based on ENEMY Supply)

| Enemy Supply | Modifier |
|---|---|
| 0–20 Critical | −2 Difficulty |
| 21–40 Rationed | −1 Difficulty |
| 41–60 Sustainable | No modifier |
| 61–80 Surplus | +1 Difficulty |
| 81–100 Abundant | +2 Difficulty |

### Allied Factions (Based on YOUR Manpower)

Manpower represents trained personnel, replacements and the capacity to field multiple formations. **Use your post-commitment Manpower to modify your total team count.** One formation is one Soulstorm team; your total includes the player.

| Your Manpower | Effect |
|---|---|
| 0–20 Critical | −2 formations |
| 21–40 Rationed | −1 formation |
| 41–60 Sustainable | No modifier |
| 61–80 Surplus | +1 formation |
| 81–100 Abundant | +2 formations |

### Enemy Factions (Based on ENEMY Manpower)

Calculate the enemy's team count independently using its post-commitment Manpower.

| Enemy Manpower | Effect |
|---|---|
| 0–20 Critical | −2 formations |
| 21–40 Rationed | −1 formation |
| 41–60 Sustainable | No modifier |
| 61–80 Surplus | +1 formation |
| 81–100 Abundant | +2 formations |

### Quick Reference: Modifier Stacking

| Source | Effect |
|---|---|
| Your Supply | Sets base difficulty from 1/5 to 5/5 |
| Enemy Supply | Modifies difficulty by −2 to +2 |
| Your participating Strength | +1 formation per full 5 Strength |
| Your Manpower | Modifies your formation pool by −2 to +2 |
| Enemy defending fleet Strength | +1 enemy formation per full 5 Strength |
| Enemy Manpower | Modifies the enemy formation pool by −2 to +2 |

**Total formations per side = max(1, 1 + floor(participating Strength / 5) + Manpower modifier).**

Apply battle-specific difficulty modifiers, then cap difficulty at 1/5–5/5. Each side has a minimum of one formation after all formation modifiers.

Example: 5 Strength and 21–40 Manpower give 1 + 1 − 1 = 1 team. At 41–60 Manpower, that same Strength gives 2 teams: you and one ally. Calculate the opposing force separately.

### Faction Count Limits and Reserves

Keep the full calculated formation pools. Deploy up to four teams per side in each battle; retain overflow in reserve.

| Situation | Deployment |
|---|---|
| No active raider | Up to 4 vs 4 |
| Active Third Party Raid | Up to 3 vs 3, plus one hostile raider |
| Raider defeated | Raider leaves the engagement; subsequent rounds return to up to 4 vs 4 |

After each reported round, remove defeated formations and destroyed winning formations. Surviving winners may fight again and refill from reserves. There is no free replacement principal team. Once defeated, the raider never returns. Resolve campaign costs, Fleet Actions and the final outcome once for the whole engagement.

### Map Size

Use a map with at least twice the largest deployed main side's team count and enough slots for every participant, up to eight. Choose a larger available map when needed for availability or the battlefield's theme; close unused slots.

| Deployed teams | Minimum map capacity | Unused slots at that capacity |
|---|---|---|
| 1 vs 1 | 2 | 0 |
| 2 vs 1 or 2 vs 2 | 4 | 1 or 0 |
| 3 vs 1, 3 vs 2 or 3 vs 3 | 6 | 2, 1 or 0 |
| 4 vs 1, 4 vs 2, 4 vs 3 or 4 vs 4 | 8 | 3, 2, 1 or 0 |
| 3 vs 3 plus one raider | 7; an 8-player map is also suitable | 0; or 1 on an 8-player map |

Do not remove formations, change their allegiance or add unearned teams to fit a map. Keep excess formations in reserve for later rounds.

### Participating Fleet Strength (Friendly Fleets)

Only assets committed to the assault contribute attacking ground Strength and formation bonuses. Fleets merely present in-system still count for Void Superiority but do not join the assault automatically.

| Participating Strength | Formation bonus |
|---|---|
| 0–4 | No bonus |
| 5–9 | +1 |
| 10–14 | +2 |
| 15–19 | +3 |
| 20–24 | +4 |
| 25–29 | +5 |
| Each further full 5 Strength | Another +1 |

Pool participating Strength before dividing by five. Use attacking ground Strength for the attacker and eligible in-system defending fleet combat Strength for the defender. Holding defence is not defending Fleet Strength. Ground-only Carrier or Assault Boats bonuses do not contribute to the defender's fleet combat Strength.

Distinct allied factions require participating fleets and consent. Otherwise, additional teams use the controlling faction.

### Battle Modifiers and Reporting

| Condition | Human battle effect |
|---|---|
| Defended | One difficulty step in the defender's favour, unless Siege Doctrine ignores it |
| Bunker | One or two difficulty steps in the defender's favour, according to its level |
| Ambush | One difficulty step in the defender's favour |
| Intel Breakthrough | Attacker chooses one easier step or +1 successful damage |
| Isolated human defender | +2 difficulty for that defender |

Global Soulstorm difficulty also affects allied AI; this engine limitation remains unresolved. Report the winning side and its surviving formations after each round so reserves and subsequent rounds can be resolved. AI campaign rolls do not predict human Soulstorm results.

## Events and alignment transit

At the event step of Phase 0, roll d6; on 1 or 6 roll once on the event table. Other opening checks mean no event. Effects last the current Cycle. Keep the established single raider identity.

| d6 | Event | Effect |
|----|-------|--------|
| 1 | **Warp Storm** | All living fleets, including Mobile Capitals, lose 1 Strength and ordinary movement is blocked this Cycle. Active Storm Transit protects eligible allied fleets in its system and permits departure. Storm damage also damages attached Integrity. |
| 2 | **Ambush!** | Attackers this Cycle get +1 difficulty. Defenders get -1 difficulty. AI vs AI: Defender +4 to roll. |
| 3 | **Supply Crisis** | All Factions: -5 Supply and -5 Manpower. |
| 4 | **War Fervor** | All Factions: +5 Supply and +5 Manpower. |
| 5 | **Third Party Raid** | If a ground battle occurs, add the fixed campaign raiding faction. Raiders are an additional hostile team and cannot capture territory or establish holdings, regardless of world tier or battle result. Survivors withdraw after the raid. If raiders win on a Major/Capital, retain the existing defence-halving effect (rounded down), but no territorial transfer to raiders. On Minor/Standard worlds, remove the former capture effect; normal applicable battle effects and traits still resolve. Do not invent additional loot or resource penalties. |
| 6 | **Intel Breakthrough** | You choose: -1 difficulty this battle OR +1 damage dealt on a successful attack. AI vs AI: Attacker +4 to roll. |

---

The provisional AI raider total is d20 + 13 (the fixed reference of 5 Strength, 20 Supply and 20 Manpower); these are resolution constants, not a spendable faction economy. The highest unique total wins; a tie favours the defender. Raiders cannot capture. On their Major/Capital victory, provisional damage is the larger of applicable Siege defeat damage and current defence minus floor(current defence / 2). Cap this at current defence minus 1, then apply shields and other mitigation. Thus an unshielded holding at 7 defence falls to 3, not to 4; shields can reduce that loss. Minor/Standard holdings receive only applicable defeat damage, also unable to fall below 1 when raiders win. Player raiders follow the reported formation-series result.

Human difficulty modifiers: apply enemy Supply band index minus 2; Defended shifts one step in favour of the defender unless Siege ignores it; Bunker shifts 1/2 steps; Ambush shifts one in favour of the defender; Intel gives the attacker a choice of one easier step or +1 successful damage. An Isolated human defender suffers +2 difficulty. Clamp the final result to 1–5. Changing global difficulty also affects allied AI; that unresolved Soulstorm limitation has not been removed by these campaign rules.

Transit names are faction-themed implementations of equal mechanics; speculative engineering is campaign lore, not a claim of canon.

| Alignment | Implementation | Rationale |
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

## d20 system profiles

| d20 | Minor planets | Standard planets | Major planets | Station tiers |
|---|---:|---:|---:|---|
|1|2|0|0|None|
|2|1|0|0|1|
|3|1|1|0|None|
|4|0|1|0|1|
|5|1|0|1|None|
|6|3|0|0|None|
|7|2|0|0|1|
|8|2|1|0|None|
|9|1|1|0|1|
|10|0|1|0|1, 1|
|11|1|2|0|None|
|12|0|2|0|1|
|13|2|0|1|None|
|14|1|0|1|1|
|15|1|1|1|None|
|16|3|1|0|None|
|17|2|1|0|1|
|18|2|2|0|None|
|19|1|1|1|1|
|20|1|1|1|2|

Prize designation is a separate setup choice, not an extra ordinary-system holding.
