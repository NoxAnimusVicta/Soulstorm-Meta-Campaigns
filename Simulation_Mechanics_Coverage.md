# Simulation mechanics coverage

Updated 16 September 2026. Current status is controlled by `simulation_readiness.json` and **Simulation_Readiness_Report.md**. Earlier checklists are preserved in `Simulation_Mechanics_Coverage_Archive_20260916.md`; their pending items are historical, not current instructions.

## Implemented numerical Subsector baseline

| Area | Implementation and verification |
|---|---|
| Resources, Logistics and deficits | Separate locked tracks; capped income; mandatory upkeep; one-time degradation; three chosen recovery actions; voluntary zero-spending blocked. B21's existing automatic defensive commitment timing intentionally retained. |
| Cycle/phase/action order | Opening Logistics/event, ordered Major turns, per-fleet action budgets, one Faction/Social/Construction action, closing effects; re-entering a turn cannot reset budgets. |
| Major and Minor factions | Shared ownership; active Majors, static Minor defenders; per-world Minor resources and original fleet caps; recovery exclusions; Independent is not an automatic alliance. |
| Movement, creation, expansion, transfer, merge, scuttle | Actual modified fleet maxima; initiation-only transfer/merge actions; transferred constructions; shipyards; new fleets cannot act immediately. |
| Fleet combat and targeted structures | Dice/ties, escorts, platforms, initiation, shared allied participation, free defence, owner's losses, guarded/unguarded structure attacks, system combat limit. |
| Ground attacks and bombardment | Full strength-based commitment, construction modifiers, cannons before commitment, uncontested floors, shields, militia, forced conscription, isolation, normal/raid outcomes. |
| Capture, capitals, elimination | Surviving planetary constructions transfer; system control differs; strongest-fleet loss allocation; mobile destruction without capture; replacement capital priority; no fallback elimination. |
| Construction lifecycle | All 32 catalogue profiles; stages, full-host requirements, integrity, upgrades, partial Repair, zero destruction, completed fleet-capacity persistence. |
| Traits | All 12 source traits have implemented effects and regression coverage, including AI/player Dread returns, allied Salvagers and modified mobile defence. |
| Social and coalition decisions | Presence and reply limit, explicit temporary pacts/expiry, offensive and defensive consent, actual owner action use; bot choices never manufacture human consent. |
| Summoning | Valid system cession, costs, dynamic turn insertion, explicit Independent pact, normal capital establishment and policy inheritance. |
| Events | One shared event per Cycle, Logistics first; all six event effects, declared three-team raid profile, human Intel choice and reported raider result. |
| Human battle interface | Resource bands, difficulty, team sizes and map capacity; explicit reported outcomes and Major loss allocation; unsupported map extremes require a referee rather than fabricated outcomes. |
| Replay and scenarios | Typed JSON snapshots, pinned engine/rule files, command hashes, deterministic replay, arbitrary faction counts and explicit synthetic campaign fixtures. |
| Bot evaluation | Six policy profiles, sampled tactical evaluation, bounded multi-turn search with private future samples, explicit diplomacy/support/conscription, recovery and construction competence fixtures. |

## Explicit boundaries

This implements the documented numerical **Subsector** game. Source material explicitly leaves future Sector progression, lifespan numbers and weighted system-generation presets undesigned. Narrative succession is not replaced with invented numerical deaths. These are future design topics, not silently simulated mechanics.

Human Soulstorm wins and losses remain external inputs. AI campaign results cannot establish a human player's battle win rate. The setup calculator can be tested separately from those outcomes.

The raid profile, periodic damage-before-repair convention and B21 are exposed in documentation/results. An executable baseline is not proof that these rules are fair. Balance experiments must include sensitivity checks before recommending changes.

## Validation gate

`validate_release.py` requires 210 regression checks, the complete 432-game trait/strategy/seat matrix, current pinned results, complete opening logs and replay evidence, eight repeated 100-Cycle cases, two repeated allied cases, two larger-map cases, independent-controller comparisons in every seat, legacy-controller comparisons and 24 random legal-action stress/replay cases. The larger fixtures have 10 systems and 22 or 23 holdings depending on Mobile Capital substitution. A recorded behavioural review must have no unresolved blocking bot failure. The gate qualifies production operational horizon zero only; optional search remains experimental.
