# Simulation readiness

Updated 17 September 2026. **Ready for controlled baseline testing of the numerical Subsector game with the production operational bots (horizon zero).** This is not a claim that the game is balanced or that bots reproduce optimal human play.

## Completed qualification

- 210 regression checks pass, including focused tests covering all 12 traits and interactions with deficits, upgraded fleets, construction and shipyards.
- 432 trait/strategy/seat games executed 100 Cycles each; 273,209 orders replayed through public validation with matching state hashes.
- Eight full campaigns reproduced their complete decisions and state; a separate fresh-process repeat also matched exactly.
- Two allied cases reproduced; two 10-system cases completed; independent-controller comparisons cover all three focal positions, alongside comparisons with the older tactical controller.
- 24 random legal-action stress cases replayed successfully; a separate 200-Cycle observation checked the former long-running case.
- Pinned source/rule hashes, complete traces, a behavioural review and an executable gate are included in the simulation bundle.

The two larger-map control milestones occurred at Cycles 52 and 68. These are two diagnostics, not an estimate of average campaign length. The target remains an average around 50-100 Cycles with shorter outliers. Read Trait_Qualification_Report.md for the full small-map matrix and censored results.

## What is now different

Bots retain operation targets and coordinate fleet assembly, funding, movement, repairs and attacks. They inspect actual damage effects and public combat odds, account for threats and upkeep, and reconsider stalled operations. Trait rotation no longer ties a particular trait to one strategy. Void Supremacy's free expansion is available to the controller at low or locked Supply.

## Boundaries for the next balance studies

Two matched matrix replicates establish coverage, not precise trait rankings. Extend seeds, opponent mixtures and representative map sizes for the specific note being tested. Compare alternative rules against the unchanged baseline using paired scenarios, and inspect decisions behind surprising results. Rare actions and less-used constructions need targeted strategy scenarios before making claims about their balance.

Optional sampled look-ahead remains experimental and is outside this qualification. Human Soulstorm outcomes remain external; traits with player-difficulty benefits require separate setup analysis. Undefined Sector, lifespan and weighted map-generation mechanics are not invented. The precise campaign ending criterion is still unconfirmed, so coalition survival and complete control remain separate measurements. B21's existing defensive-cost timing remains deliberately unchanged.

No balance rule was adopted and Dessica remains suspended at Cycle 21, revision 65dc4a60d17b.
