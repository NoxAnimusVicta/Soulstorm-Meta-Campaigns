# Simulation development handover

Updated: 15 September 2026. Work in progress; experiments do not amend campaign rules.

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
