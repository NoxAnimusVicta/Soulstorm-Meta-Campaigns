# Simulation mechanics coverage

Updated 16 September 2026. **BALANCE TESTING LOCKED.** User decision: finish all simulation mechanics and interaction validation before evaluating changes from the campaign notes. Existing results are implementation diagnostics only.

Implemented means a rule is available in the shared engine and has focused regression coverage. Partial means some cases exist but important interactions or conventions are missing. Neither means fully validated campaign fidelity. This register is the current implementation checklist; older reports preserve historical limitations.

## Construction catalogue

| Source construction | Status | Evidence / outstanding work |
|---|---|---|
| Orbital Shipyard | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Supply Depot | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Training Grounds | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Automated Defences | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Bunker Network | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Orbital Cannons | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Grand Orbital Shipyard | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Forge Complex | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Military Academy | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Regenerative Fortifications | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Void Shield Generator | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Fortification Network | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Militia Barracks | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Landing Zones | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Planetary Shield Network | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Consolidation Works | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Troop Transport | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Repair Tender | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Escort Squadron | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Assault Boats | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Bombardment Bay | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Assault Cruiser | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Flagship | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Carrier | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Siege Platform | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Salvage Wing | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Scout Squadron | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Defence Platform | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| System Defence Station | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| System Repair Station | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Logistics Anchorage | Missing | Implement action availability, effects, damage, capture and upgrade interactions |
| Void Station | Missing | Implement action availability, effects, damage, capture and upgrade interactions |

## Other mechanics

| Area | Status | Required before balance testing |
|---|---|---|
| Military resource caps, expenditure, independent deficit tracks | Partial | Cost-trigger sequencing on mobile hosts; all action interactions |
| Logistics, upkeep, event timing | Partial | Remaining trait and system-construction effects; explicit timing order |
| Movement, expansion, creation, fleet actions | Partial | All traits/capacity effects; allied action consent; direct action API phase-budget enforcement |
| Fleet Transfer / Fleet Merge / Scuttle | Missing | Participant actions, donor limits, caps, attached structure fate and refunds |
| Ground assaults / bombardment | Partial | Fleet constructions, shields, retaliation ordering, every player setup modifier |
| Fleet Battles | Partial | Combat structures, chosen defending participation, ties and allied fleets |
| Structure Assault, system construction control and capture | Missing | Guarded/unguarded targeting; construction-only damage; transfer/destruction rules |
| Planet Fall, mobile destruction, elimination | Partial | Full allocation choices, mobile fall collateral interpretation and all capture effects |
| Capital replacement | Partial | Approved capital-before-rationing priority implemented; provisional tier/income convention needs ruling |
| Faction Reinforce / Muster / Defend | Partial | Basic actions and structure Defend implemented; remaining trait effects |
| Garrison Transfer / Landing Zones | Missing | Multiple donors, bounds, full-defence conditions and construction damage interpretation |
| Summon Allies | Missing | Dynamic faction count/turn order, grant validation, alignment and capital selection |
| Social actions, diplomacy, aligned and Independent factions | Missing | Presence, response limit, explicit pacts, consent and coordination |
| Mixed Major/Minor campaign | Missing | One shared ownership model with static Minor rules and active Majors |
| Minor per-world resources, fleets, recovery | Frontier only | Port to shared engine; regenerate once per faction; combat exclusion |
| Void Stations / pre-existing stations | Missing | Construction completion into holdings, tier changes, capture; never capital candidates |
| Events | Partial | Three-party raids unsupported; all newly added interactions require tests |
| Human battle setup/outcomes | Diagnostic only | Complete modifiers, participation/map slots, outcome injection; no invented human win rates |
| Scenario generation, starting assets, objectives | Partial | Standard starts and arbitrary faction counts; current shared fixture is synthetic |
| Personnel, Sector progression | Undefined source rules | Cannot implement unspecified ages/lifespans or Sector rules; explicitly scope before certification |

## Trait coverage

| Trait | Status |
|---|---|
| Mobile Capital | Partial: movement, income, ground/naval combat, host damage, loss and replacement implemented; remaining hybrid interactions pending |
| Efficient Logistics | Implemented +4 Reinforce/Muster |
| Siege Doctrine | Partial: defeat damage; complete player difficulty integration pending |
| War Economy | Missing |
| Martial Culture | Missing |
| Salvagers | Missing |
| Void Supremacy | Missing |
| Swift Mobilization | Missing |
| Fleet Endurance | Missing |
| Dread Reputation | Missing; AI/player resource-return distinction must stay explicit |
| Fortification Experts | Missing |
| Industrial Efficiency | Missing |

## Rulings to obtain during implementation

Do not invent rulings to make tests pass. Pending: defensive fleet participation/action consumption; AI tied totals and defender costs; three-party AI raid procedure; provisional-capital tier/income; mobile destruction collateral fleet damage; donor/recipient action expenditure and construction fate for fleet transfers/merges; construction payment/deficit sequencing; ambiguous periodic system effects and retaliatory cannon ordering.

Approved: Establish New Capital takes priority over Emergency Rationing, preserving locked resources and recovery progress. Surviving planetary structures transfer; obsolete Major-destroyed-on-capture table labels do not override that later explicit rule.

## Completion gate

1. Every documented mechanic is implemented or explicitly scoped by the user where source rules are undefined.
2. Every important cross-system interaction has deterministic expected-result tests, including damage/capture/income/action availability.
3. Replay campaign situations and verify state invariants and conservation, with full traces and pinned input versions.
4. Validate bots' access to, and competent use of, all legal strategies. Test independent policies and opponent responses.
5. Only after these pass begin controlled balance experiments and work through the notes. More random trials cannot substitute for these steps.

## This checkpoint

51 tests pass: 21 core, 18 shared, 12 construction tests. No new balance study was run. New construction coverage includes shipyards, grand shipyards, bunker bonuses, void shields, militia, automated defences and regenerative fortifications. Construction-phase Repair remains separate from Faction Action structure Defend. Regeneration runs once at Cycle closure in both real and simulated continuations. Capacity constructions and system/fleet structures remain missing.
