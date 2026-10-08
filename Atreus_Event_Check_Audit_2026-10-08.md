# Atreus event-check audit — 8 October 2026

Reviewed Cycles 1–9 at the Cycle 9 opening checkpoint.

| Cycle | Check | Event-table roll | Result |
|---|---:|---:|---|
|1|3|—|No event|
|2|1|1|Warp Storm|
|3|3|—|No event|
|4|2|—|No event|
|5|4|—|No event|
|6|4|—|No event|
|7|2|—|No event|
|8|2|—|No event|
|9|2|—|No event|

The saved files Atreus_Cycle_01_Phase_0_Rolls.json through Atreus_Cycle_09_Phase_0_Rolls.json agree with the rule: one d6 check per Cycle; only 1 or 6 triggers one event-table d6. Cycle 2's table result 1 is Warp Storm. No extra event roll was required for the other checks.

Cycles 1–4 record Python secrets.randbelow(6)+1. Cycles 5–9 record JavaScript Math.random because local command execution is unavailable. The visible recent calls use 1 + Math.floor(Math.random()*6), with a conditional second draw only for check 1 or 6. No campaign results were rerolled during this audit.

Two separate diagnostic calls returned different sequences. A separate 60,000-draw diagnostic produced face counts 10065, 9817, 10145, 9794, 10138, 10041 (faces 1–6); chi-square 12.19 against 10,000 per face. All faces were reachable; no fixed-sequence or stuck-face defect was observed. This basic diagnostic is not a certification of unbiased or cryptographically secure randomness, and cannot retroactively verify the entropy of recorded rolls. JavaScript Math.random is not a cryptographic generator. Python secrets remains preferable when local execution recovers; a diagnostic retry of local execution still failed before Python launched.

Under independent fair d6 checks, seven consecutive no-event checks have probability (2/3)^7 = 5.85%. This makes the observed quiet run possible; it is not grounds to force an event or reroll.

Future procedure: preserve one global Phase 0 check, record the raw random value as well as the mapped result when using JavaScript, record any conditional table draw separately, save before resolving effects, and never redraw to obtain a more varied result. Diagnostic samples must remain separate from campaign rolls.

No rules, campaign resources, ownership, or past rolls changed.
