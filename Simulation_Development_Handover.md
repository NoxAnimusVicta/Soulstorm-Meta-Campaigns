# Simulation development handover

Updated: 16 September 2026. Work in progress; experiments do not amend campaign rules.

## Mechanics completion phase — current priority

User instruction: finish ALL simulation mechanics and validate their interactions before balance testing or working through proposed changes. Simulation_Mechanics_Coverage.md is the current checklist. Earlier experimental results are diagnostics only. Latest checkpoint: 51 tests pass; seven additional planetary construction profiles plus structure Defend and regeneration are integrated. planner_experiment.py now requires --diagnostic; no new balance experiment was run.

## Read first — prior checkpoint

The 16 September continuation at the end of this document is the current status. Earlier sections are retained as historical checkpoint notes, not a current task list. Current code includes capital recovery, Major Planet Fall resource costs, direct mobile ground targeting and a bounded future-turn planner. The user ruled that Establish New Capital takes priority over Emergency Rationing. No other experimental balance changes were approved.

## Campaign and destination

Dessica is suspended at Cycle 21 after the Korps turn. Do not roll events or advance turns. Repository: https://github.com/NoxAnimusVicta/Soulstorm-Meta-Campaigns ; branch: main ; live app: https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/ . Synced files under sources/ are read-only.

## Completed before this continuation

Source library and a frontier pilot are published. balance_sim.py models one Major against static Minors; balance_tests.py has 19 regression tests. balance-results/ contains 432 pilot runs (8 seeds, 36 Cycles, 6 preference profiles, 3 traits, 3 cost variants). Balance_Simulation_Report.md correctly labels these preliminary. Zero bombardments and zero deficits mean the policies failed important behavioural coverage; the pilot is not evidence that the game is balanced. Existing outputs retain their original engine hash and must not be represented as runs of a revised engine.

## Current work

Checkpoint completed locally: shared_sim.py implements a separate shared Major campaign with ownership, active opposing factions, shared event timing, hostile fleet battles, planetary assaults, bombardments, Defend expiry and surviving construction transfer. shared_tests.py passes 9 tests; balance_tests.py now passes 21. Construction payments that damage a mobile host now stop and report unresolved sequencing rather than resurrecting a destroyed project. The timing ruling itself is not invented. No actual campaign costs changed.

shared-results-v2/ is the current integration batch: 12 runs, 2 seeds, 12-Cycle horizon, starts of 6/6 and 20/20, three turn-order rotations. Eight reached the horizon normally; four stopped on capital capture because relocation is unsupported. All stops remain recorded. Action totals: 252 ground assaults, 23 naval battles, 6 bombardments, 59 fleet expansions, 25 Defend actions, 9 rationing actions and 3 deficit entries. No fleet creation occurred. These are behavioural coverage observations, not balance results. Every trial has its full action/dice trace and the manifest pins both engine files and the source rules by hash.

The earlier shared-results/ batch predates the one-naval-battle-per-system-per-turn guard; it is superseded, not used for current conclusions. Current published bundle includes shared-results-v2 only. The original 432-run frontier bundle is retained intact as Historical_Frontier_Pilot.zip inside the new bundle, so its original scripts and hashes remain reproducible.

## Precise next steps

1. Read shared_sim.py and shared_tests.py. The current opponent policies are one-step heuristic evaluators (raider, industrial, fleet_control); they are deliberately NOT called complex or validated bots. Add multi-turn search with opponent replies, supply reserves for planned campaigns, repair/retreat and reinforcement plans. Add depth ablations and behavioural fixtures before another balance comparison. No fleet creation in this batch is an explicit failed coverage gate.
2. Add Major capital relocation and direct mobile-capital ground targeting; four current trials stop at capital loss. Add regression tests before removing those stops.
3. Pin defensive fleet action consumption/participation, AI ties, defender Supply payments and three-party raid adjudication. Current conventions: automatic defending fleets do not spend actions; ground ties favour defender; fleet ties deal no damage; no defender Supply debit; insufficient defender Manpower uses Isolated Defense instead of choosing Forced Conscription; raid-cycle ground assaults are unavailable. These are model assumptions, not approved campaign rulings.
4. Add fleet/system combat constructions, transfers, scuttling, consent/diplomacy, Minor factions sharing the same map, and full trait coverage. Only four economic construction profiles exist currently.
5. Rotate policy-to-trait and map assignments as well as turn order; current assignments are confounded and cannot rank traits. Build held-out scenarios and human-outcome sensitivity before suggesting numerical rebalances.

## Commands for this checkpoint

    python -X utf8 balance_tests.py
    python -X utf8 shared_tests.py
    python -X utf8 shared_sim.py --seeds 2 --cycles 12 --out shared-results-v2-replay
    python -X utf8 package_simulation.py
    python -X utf8 build.py
    node --check app.js

Do not rerun balance_report.py casually: it regenerates the original pilot report and bundle, overwriting later additions. Use package_simulation.py for this checkpoint. Historical data must not be relabelled as results from newer code.

## Outstanding fidelity requirements

Reactive Major opponents; multi-turn strategic policies with distinct behaviour; all construction and transfer mechanics; defender expenditure and ground tie ambiguities; three-team raid outcomes; human battle outcome sensitivity; diplomacy and allied action consent; capital loss and relocation. Unsupported interactions must be explicit and counted, never silently replaced by favourable outcomes. Replay Dessica situations and inspect action coverage before interpreting balance results.

## Resume and publication

Work from this file's directory. Run python -X utf8 balance_tests.py. Existing pilot: python -X utf8 balance_sim.py --seeds 8 --cycles 36 --out NEW_OUTPUT_DIRECTORY (do not overwrite historic results). Build website with python -X utf8 build.py and validate node --check app.js. Update this handover after each checkpoint. GitHub connector reads worked; writes previously returned 403. Signed-in GitHub browser uploads successfully published root sources and generated dist files. Verify Actions and the live source page before calling an update published. Checkpoint source commit 3524c4026dcb79a8fef37a0d4e87043a4e9a6b0e deployed successfully in Actions run 34941755685; the live source page and development handover were verified on 15 September 2026. Later documentation-only commits may follow this receipt. Verify the latest run when resuming.

## Active continuation — 16 September 2026

The earlier sections describe the 15 September checkpoint. Current local work supersedes several gaps: shared_sim.py now applies Major Planet Fall resource penalties, tracks established capital shipyards separately from captured holdings, supports free doubling actions to establish a replacement capital, processes Mobile Capital loss penalties/trait loss once, and prevents eliminated factions taking turns or receiving Logistics/events. The user subsequently ruled that Establish New Capital takes priority over Emergency Rationing; that priority is now implemented and tested.

strategic_planner.py adds bounded lookahead: it evaluates the rest of this Cycle and future Cycles, including opponent replies and privately sampled events. Investment candidates survive the immediate-value shortlist, so creation can be considered for future usefulness. This remains a bounded heuristic rollout, not expert play or complete game fidelity. planner_experiment.py compares depth 0 with depth 1 using paired event seeds and turn-order rotations, preserving every trace and saving partial results after each run. Completed first batch: python -X utf8 planner_experiment.py --cycles 6 --seeds 1 --out planner-results-20260916 . Six trials finished with no unsupported stops; this batch predates the ruling and mobile ground targeting and includes its exact source snapshots.

Validation: 21 core tests and 18 shared tests pass. Historical shared engine preserved as shared_sim_checkpoint_20260915.py; its corresponding core as balance_sim_checkpoint_20260915.py. The old shared-results-v2 runs omitted Major Planet Fall resource penalties and therefore must not be used for economic conclusions. They remain historical integration evidence only. No campaign rules or Dessica state changed. This continuation has not yet been published.

Early observation (not a completed comparison): the first lookahead trial commissioned four fleets, whereas its paired one-step trial commissioned none. This shows that future-turn evaluation can change investment behaviour. It does not establish that more fleets or the new planner are better. Wait for the full batch and report opposing outcomes, costs and limitations before drawing conclusions.


## Final local checkpoint — 16 September 2026

Current authoritative development files: shared_sim.py, strategic_planner.py, planner_experiment.py, shared_tests.py, balance_sim.py and balance_tests.py. Direct mobile ground targeting and destruction tests are now included. Source_Rules.md contains the user's capital-before-rationing ruling. No other balance changes or Dessica ledger changes were made.

Both batches finished: planner-results-20260916 has six 6-Cycle trials; planner-results-20260916-ruling has six 3-Cycle trials with the current ruling and mobile targets. Both use seed 0 and three turn-order rotations at planner depths 0 and 1. No unsupported stops occurred. First batch: creation 0 versus 15; second batch: 0 versus 10. These are tiny integration/behaviour comparisons, not win-rate studies. Their manifests and inputs/ directories preserve the code actually used; do not combine them as identical model versions.

Next work, in order:
1. Add combat constructions, system construction targets and explicit capacity/effect invalidation tests. Four economic profiles remain the only construction choices. Add fleet transfers/merges/scuttles with documented participant-action accounting.
2. Add mixed Minor/Major maps and fully rotate trait, policy, home-system layout and turn order. Current synthetic map grants extra starting assets and is not a standard campaign opening. Add explicit scenario objectives and independent policy families.
3. Improve planning efficiency and deeper-horizon tests: the first 6-Cycle batch took about 249 seconds; the 3-Cycle batch about 94 seconds. Keep investment candidates, but test shortlist sensitivity and opponent-model errors. Current depth comparison also changes the relative-opponent scoring term, so it is not a pure horizon ablation.
4. Settle remaining defensive participation, AI tie/defender Supply, three-way raid and mobile Planet Fall allocation conventions before claiming full fidelity. Review provisional-capital income tier (currently unchanged until maximum reaches 12). The captured capital's yard does not transfer.
5. Calibrate human battle outcomes separately; do not infer them from AI dice or use the small Dessica sample to claim precise win probabilities.

Resume commands: python -X utf8 balance_tests.py ; python -X utf8 shared_tests.py ; python -X utf8 planner_experiment.py --cycles 6 --seeds 2 --out NEW_DIRECTORY . Use separate commands in the shell. package_simulation.py bundles the current scripts, both fixed 16 September result directories, the handover and historical archives; add a new output directory to its folder list when packaging future runs. build.py generates the source-library page and downloads.

Publication status at packaging: ready for upload; verify the GitHub commit, Actions run and live page. GitHub connector tools are absent after the account switch, but the signed-in in-app browser still exposes repository uploads. No login or permission change was needed. Earlier publication receipts refer to 15 September, not this continuation.


## Mechanics implementation checkpoint — 16 September 2026

Added construction_rules.py and construction_tests.py. Shared engine integrates shipyard creation eligibility, grand-yard creation strength and prerequisites, bunker defender bonuses, damage-reducing void shields, militia zero commitment, and automated/regenerative defence recovery. All effects require full Integrity and completed status; upgrades, capture, repairs and host damage use existing project state. Structure Defend is a Faction Action with its own Supply/Manpower price, not a replacement for construction-phase Repair.

Cycle closing now runs in both shared_sim.run and strategic_planner.rollout; double-closing is rejected. Current test command: python -m unittest balance_tests shared_tests construction_tests -q (51 passing). A regression caught a mobile-target variable ordering error during development; it was fixed before this checkpoint. No unresolved failed test remains.

Next: finish the five remaining planetary profiles (Orbital Cannons, Fortification Network, Landing Zones, Planetary Shield Network, Consolidation Works), then fleet-attached and system constructions with typed host references and capacity tracking. See the coverage register for the rest. Do not silently assume action/retaliation/transfer timings. The old source table's Major planetary destruction label is superseded by the explicit surviving-structure capture ruling.

Packaging must include construction_rules.py, construction_tests.py and Simulation_Mechanics_Coverage.md. Experiment input snapshots now include construction_rules.py. Do not compare current runs with old results as identical engines. Github publication uses the existing signed-in browser if connector tools remain absent. Publication status at packaging: files prepared; confirm latest commit and Pages before calling this checkpoint published.
