# Balance laboratory — methods and coverage

Date: 15 September 2026 • Version: 0.1 • Status: calibration instrument, not a balance certification.

## Purpose

Supply is military-grade material, equipment and operating stock. Manpower is military personnel/capacity. All tested fleet-cost candidates retain the existing Supply charge. No candidate is adopted into the campaign. Dessica remains suspended.

## Three linked tests

1. **Rules and ledger tests:** standard-library unit tests against hand calculations and selected Dessica outcomes. These check the accounting engine, not whether a game mechanic is fun or balanced.
2. **Exact combat enumeration:** all 400 pairs of d20 results for each naval matchup; analytic AI ground win probabilities; recorded player difficulty/team calculations. These results do not depend on Monte Carlo sample size.
3. **Frontier campaign experiments:** repeated multi-Cycle expeditions with one Major Faction fighting static Minor factions, with resources, movement, repairs, fleet actions, host damage, economic construction and end-Cycle recovery. Six planners compare legal actions and replan after each realised action. This is the first stage of a larger model; it is not a full three-Major-Faction campaign.

## Rules implemented in frontier engine

- Supply/Manpower caps, affordability, military fleet creation and expansion, Fleet Actions, shared attack cost, full Manpower commitment and post-cost AI rolls.
- Mobile Capital strength, shipyard, movement and maintenance exemption; its host damage affects every attached project.
- Standard capital shipyards; no movement during Warp Storm; no same-Cycle action for a newly created fleet.
- Multiple separate or combined fleet attacks, one Fleet Battle per system per turn, conventional fleet caps, initiation cost, loss bands and Planet Fall.
- Ground assault allowed with hostile fleets present; unopposed bombardment double cost, zero Manpower and defence floor.
- Siege Doctrine's damage on defeat; Efficient Logistics' +4 Reinforce/Muster; Mobile Capital profile. Other traits are not tested.
- Static Minor per-world resources, original fleet maxima, engaged-faction recovery exclusions, no destroyed-fleet resurrection, capture and final-holding fleet elimination.
- Separate resource deficits, three selected recovery actions, ignored gains/losses while locked and one-time degradation. Both resources remain otherwise independent.
- Logistics every third Cycle before events, four economic buildings, incomplete/active states, Integrity, repairs and upgrades, full-host eligibility and construction damage.
- Six event table entries sampled at the documented frequency. Raid cycles defer ground assaults because a three-way AI resolution formula is missing; this is a declared experimental restriction, not a new rule.

## Coverage gaps — prohibit overall balance claims

- No strategic Major-versus-Major opponent, diplomacy, alliances, Summon Allies, information asymmetry or negotiated control. There is no win-rate league among the six planners: they face identical static frontiers independently.
- No Soulstorm combat simulation or estimated human win probability. The player setup calculator outputs difficulty, formations and map capacity only. Mechanical AI simulations cannot validate the player's Siege Doctrine experience.
- No combat constructions, fleet transfer/merge/scuttle, Garrison Transfer, new shipyard construction, station construction, Consolidation Works or Capital relocation. A Mobile Capital loss stops the trial and is reported, not silently discarded or treated as a complete campaign.
- Only one Minor faction per system in the synthetic map. Matching the frontier controls map variation but does not reproduce the entire Dessica opening map or its original 10/10 start.
- No automatic final verdict that the system or any candidate is balanced. More seeds cannot repair missing mechanics or poor strategic coverage.

## Planning and assumptions

Each policy enumerates legal moves, repairs, fleet group subsets, assaults/bombardment, fleet creation, resource actions and four economic construction profiles. A common evaluator uses diminishing resource utility, scarcity/deficit costs, future Logistics income, force strength, target progress, estimated AI combat probability and capture value. Six weight profiles emphasise adaptation, ground doctrine, naval doctrine, industry, personnel preservation and opportunism. These are **six variants of one search algorithm**, not six independently designed expert agents.

The planner samples four private combat outcomes for candidate actions, penalises downside, retains four candidates and looks ahead one additional action or phase. It re-evaluates after real results. It cannot see the trial RNG or future events. Subset enumeration is capped at eight assets plus the full group. Future income is valued heuristically for up to five Logistics payments. These horizon/utility choices can favour certain investments; policy and horizon ablations are required before interpreting preferences as dominance.

Baseline AI ground calculation follows the current referee formula: d20 + participating strength + post-cost Supply + post-commit Manpower; Minor defender commits floor(damage/2). Baseline does not additionally debit Minor defender Supply; a sensitivity switch exists because the generic player table differs. AI ground ties favour defender; fleet ties cause no damage after initiation. Those are simulation conventions pending explicit tie rulings. Defended status is not strategically exercised because static Minor factions cannot take Defend actions. Assaults on raid cycles are unavailable to all bots, so measured capture times include that shared delay; no raid strength or winner is fabricated.

All fixtures use distinct non-allied sides. The primary matched fixture consists of three systems: Standard target in system 0; Major + Standard + Minor in system 1; Standard + Minor + Minor in system 2. Starting Minor strength is summed defence split into 5-strength formations. Planet Capitals use 12 defence and a 5-strength fleet; Mobile Capitals use 12 strength and no conventional fleet. The mobile capital receives no free starting planet.

## Reproducibility

Run from repository root with Python 3, standard library only:

    python balance_tests.py
    python balance_diagnostics.py
    python balance_sim.py --seeds 8 --cycles 36 --out balance-results

Files: balance_sim.py, balance_tests.py, balance_diagnostics.py. Results include all trial outcomes, first-seed action traces per condition, exact combat tables and a manifest with engine/source hashes. Event RNG is isolated from combat RNG so paired variants receive identical event sequences until a trial stops. Different decisions mean different combat situations; shared seeds are not identical battle histories. Planning RNG is separate from both. Stopped trials remain in outputs and must be reported.

Use captures/resources/deficits and action distributions together; a high final stock is not a win. Confidence intervals across paired seeds describe Monte Carlo variability within this model, not uncertainty about omitted game rules. A trial with no capture has an undefined first-capture time, not zero days. Report censored/no-capture runs separately.

## Required next stages

1. Resolve AI/player defender accounting, ties and three-way raid resolution with the user. Pin conventions and add tests.
2. Add all construction and fleet tools before judging economy-first, bombardment-first or optimal Manpower costs.
3. Add a shared multi-Major map, reactive opponents, counterattack/defence, elimination/relocation and explicit victory objectives. Rotate traits, map positions and turn order; add strong non-greedy baselines and planner-depth/weight ablations.
4. Build a player combat dataset from actual reported outcomes with difficulty, teams, faction matchup, map, raid involvement and player/mod versions. Do not fit precise win rates from Dessica's small, changing sample.
5. Run scenario sweeps, holdout seeds/maps, uncertainty analysis and adversarial exploit search. Compare against historical choices without forcing the bot to imitate an obviously constrained or roleplayed move.

These steps are necessary to reach the user's requested full-game fidelity. The initial experiment is useful for checking implementation and identifying questions, not for approving a rebalance.

## Pilot rejection gate

The initial 432 runs produced no bombardment actions or deficit entries and high closing stocks. This is a coverage/behaviour warning, not proof of a balanced economy. Exact-zero construction payments with host degradation are an unvalidated boundary and must be repaired/tested before extending to those situations. None of the reported pilot runs entered any deficit.

## Continuation checkpoint

shared_sim.py and shared_tests.py add the shared-Major integration layer. See the development handover for the current coverage matrix in prose, exact run commands, model conventions and remaining implementation order. Current runs are stored in shared-results-v2; the original frontier pilot remains archived intact. The construction exact-zero boundary now has regression coverage and explicitly stops for unresolved ordering. This does not retroactively validate the pilot's missing behaviours.
