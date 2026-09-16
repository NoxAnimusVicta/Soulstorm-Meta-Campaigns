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
| Orbital Cannons | Partial | Effect implemented; full interaction and strategy coverage still required |
| Grand Orbital Shipyard | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Forge Complex | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Military Academy | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Regenerative Fortifications | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Void Shield Generator | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Fortification Network | Partial | Effect implemented; full interaction and strategy coverage still required |
| Militia Barracks | Implemented in shared engine | Core/shared/construction regression suites; effects require completion and full Integrity |
| Landing Zones | Partial | Effect implemented; full interaction and strategy coverage still required |
| Planetary Shield Network | Partial | Core effect and focused regression tests implemented; cross-mechanic audit remains |
| Consolidation Works | Partial | Core effect and focused regression tests implemented; cross-mechanic audit remains |
| Troop Transport | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| Repair Tender | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| Escort Squadron | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| Assault Boats | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| Bombardment Bay | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| Assault Cruiser | Partial | Effect implemented; full interaction and strategy coverage still required |
| Flagship | Partial | Effect implemented; full interaction and strategy coverage still required |
| Carrier | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| Siege Platform | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| Salvage Wing | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| Scout Squadron | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| Defence Platform | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| System Defence Station | Partial | Effect implemented; full interaction and strategy coverage still required |
| System Repair Station | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| Logistics Anchorage | Partial | Effects added; focused tests and cross-mechanic audit still being completed |
| Void Station | Partial | Core effect and focused regression tests implemented; cross-mechanic audit remains |

## Other mechanics

| Area | Status | Required before balance testing |
|---|---|---|
| Military resource caps, expenditure, independent deficit tracks | Partial | Cost-trigger sequencing on mobile hosts; all action interactions |
| Logistics, upkeep, event timing | Partial | Remaining trait and system-construction effects; explicit timing order |
| Movement, expansion, creation, fleet actions | Partial | All traits/capacity effects; allied action consent; direct action API phase-budget enforcement |
| Fleet Transfer / Fleet Merge / Scuttle | Missing | Participant actions, donor limits, caps, attached structure fate and refunds |
| Ground assaults / bombardment | Partial | Fleet constructions, shields, retaliation ordering, every player setup modifier |
| Fleet Battles | Partial | Combat structures, chosen defending participation, ties and allied fleets |
| Structure Assault, system construction control and capture | Partial | Guarded/unguarded attacks and control capture tested; allied guards and trait interactions remain |
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
| War Economy | Partial: effect implemented; interaction audit pending |
| Martial Culture | Partial: effect implemented; interaction audit pending |
| Salvagers | Partial: effect implemented; interaction audit pending |
| Void Supremacy | Partial: effect implemented; interaction audit pending |
| Swift Mobilization | Partial: effect implemented; interaction audit pending |
| Fleet Endurance | Partial: effect implemented; interaction audit pending |
| Dread Reputation | Partial: explicit human defence return test; AI-specific return remains 60% |
| Fortification Experts | Partial: effect implemented; interaction audit pending |
| Industrial Efficiency | Partial: effect implemented; interaction audit pending |

## Rulings to obtain during implementation

Do not invent rulings to make tests pass. Resolved on 16 September: defensive participation never spends an action; fleet ties inflict no damage and ground ties favour defence; AI defender Supply/Manpower commitments recorded in Source_Rules. Pending: three-party AI raid procedure; provisional-capital tier/income; mobile destruction collateral fleet damage; donor/recipient action expenditure and construction fate for fleet transfers/merges; construction payment/deficit sequencing; ambiguous periodic system effects and retaliatory cannon ordering.

Approved: Establish New Capital takes priority over Emergency Rationing, preserving locked resources and recovery progress. Surviving planetary structures transfer; obsolete Major-destroyed-on-capture table labels do not override that later explicit rule.

## Completion gate

1. Every documented mechanic is implemented or explicitly scoped by the user where source rules are undefined.
2. Every important cross-system interaction has deterministic expected-result tests, including damage/capture/income/action availability.
3. Replay campaign situations and verify state invariants and conservation, with full traces and pinned input versions.
4. Validate bots' access to, and competent use of, all legal strategies. Test independent policies and opponent responses.
5. Only after these pass begin controlled balance experiments and work through the notes. More random trials cannot substitute for these steps.

## This checkpoint

Earlier checkpoint: 51 tests passed (21 core, 18 shared, 12 construction). No new balance study was run. New construction coverage includes shipyards, grand shipyards, bunker bonuses, void shields, militia, automated defences and regenerative fortifications. Construction-phase Repair remains separate from Faction Action structure Defend. Regeneration runs once at Cycle closure in both real and simulated continuations. Capacity constructions and system/fleet structures remain missing.

### Local continuation (not yet published)

119 regression tests pass. All 32 profiles are catalogued; unfinished effects are explicitly excluded from bot purchases. See the current handover for implementation progress and remaining gates. No balance certification.

The validated submit API now enforces phase budgets in production runs. Minor resource/starting fleet/recovery scaffolding and Scout movement-attacks are tested. Player setup calculations cover resource bands, modifiers, symmetric scaling, and third-team map capacity; outcome integration remains pending. Fleet Scuttle, ordinary Transfer and Merge are implemented; enhanced/Mobile Transfer interpretation remains pending.

All 32 construction effects now have implementation paths. This does not certify all interactions. Explicit allied assault consent, Garrison Transfer, Minor local resources, transaction rollback, and permanent fleet-capacity constructions have tests. Summoning, raids, human outcome integration, strategy competence and full replay validation still prevent balance testing. See the latest handover first.

Latest local verification: 119 tests across six suites. Eight pinned random-action stress replays verified 1351 transitions; these are legality diagnostics, not balance or competent-strategy evidence. Human preview/reporting, explicit Major fleet-damage choices, Social bandwidth and four-Major scenario handling are now implemented with focused tests. Pending rulings and completion work are listed at the top of the handover.
