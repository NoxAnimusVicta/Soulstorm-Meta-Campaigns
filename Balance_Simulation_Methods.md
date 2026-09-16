# Simulation methods

Updated 16 September 2026. Read Simulation_Readiness_Report.md for the current qualification result. This laboratory does not advance suspended Dessica or adopt balance changes.

## Rules and scope

The shared numerical Subsector engine represents Major and Minor factions, fleets, holdings, Mobile Capitals, resources, deficits, events, constructions, combat and diplomacy. It implements all 12 source traits and 32 construction profiles. Source_Rules.md and executable input hashes identify the exact baseline. Supply remains a military-material resource; construction and fleet Supply costs are retained. The existing automatic defensive-cost timing issue B21 remains in the baseline rather than being silently corrected.

Human Soulstorm battles require external outcomes. The simulator supplies setup and costs; AI-only campaign results do not estimate human battle win rates. In particular, Soulstorm difficulty benefits and player/AI resource-return distinctions mean that Siege Doctrine and Dread Reputation require separate player-setup analysis before changing those traits. Sector progression, lifespan values and weighted map-generation presets remain undefined future source work.

## Production bots

Six strategies express different preferences: raider, industrial, fleet control, conservative, opportunist and balanced. They share an operational controller but vary acceptable battle risk, reserves, force size, consolidation, investment and opportunistic attacks. Persistent operation targets connect movement, force assembly, stockpiling, repairs and attacks across turns. Budgets respond to upkeep, defender resources, hostile fleets, damaged ships and construction commitments. Actual isolated resolver probes account for shields and combat effects when judging legal attacks; these probes never inspect future campaign dice.

The controller can bombard, assault, fight fleets, raid constructions, use Scout attacks, withdraw to shipyards, expand, merge damaged fragments, replenish, create fleets, recover capitals/deficits, repair and construct. Diplomacy accounts for military threats and whether a pact would block the current operation. Allied consent and defensive conscription use explicit policy decisions. Rare legal actions remain engine-supported without a claim that the bots have mastered every use of them.

Operational horizon zero means no additional sampled search; it does not mean no plans beyond the current turn. Optional search completes hypothetical turns and samples opponent responses, but remains experimental and is not covered by qualification of the horizon-zero production controller. The old tactical controller and an independently written siege controller are retained for comparisons, rather than being counted as additional production strategies.

## Trait qualification

trait_qualification.py tests a full factorial: 12 focal traits x 6 strategies x 3 turn positions x 2 replicate seeds, yielding 432 games, each executing 100 Cycles. A faction retains its trait for a whole game. Opponent traits, policies and initial conditions vary between replicates but are fixed across focal comparisons within a replicate and seat. Each trait therefore receives the same strategy/seat coverage instead of being repeatedly paired with one strategy. Opponent identities also depend on seat, so raw seat aggregates are descriptive and do not isolate the causal effect of turn order. Trait and strategy comparisons are matched within seed/seat blocks.

Event draws are matched by seed and Cycle. Combat uses a separate seeded stream; actions can change how many combat draws are consumed, so identical battle dice are not promised for divergent wars. Replicates include starting ordinary-fleet strengths 1 and 4 and Minor world tiers 1 and 2. Mobile Capitals retain their rule-defined starting strength and replace the ordinary starting fleet. These are explicit synthetic fixtures, not generated copies of Dessica.

Two replicates are a qualification screen, not enough to rank closely matched traits with statistical confidence. They are not an exhaustive test of all possible three-trait combinations. Follow-up balance studies should broaden seeds, opponent mixtures, starting states and map sizes around any suspected effect.

## Evidence and interpretation

Every matrix game records initial/final states, all orders, bot memory, per-Cycle summaries, combat/event logs and exact inputs. Orders are replayed through public validation and state hashes checked. Compressed traces preserve the full evidence. Additional cohorts check full-campaign reselection and a fresh-process repeat, independently controlled opponents, allies, larger maps and random legal-action stress. Tests distinguish a long active war from a controller stuck in a repair or movement loop.

Report the first single surviving Major coalition and complete holding/Mobile Capital control separately. The user has not selected a universal end criterion. Unfinished games are censored at the observation limit, not recorded as victories or assigned a made-up duration. The design target is an average around 50–100 Cycles with shorter outliers; this is a balance goal, not a test condition or a requirement to keep every game contested for 100 Cycles.

Qualification permits controlled comparisons within the documented bot/rules scope. It does not prove optimal human play, game balance, or that a trait is weak because one heuristic uses it poorly. Review saved decisions, compare controllers and vary uncertain assumptions before recommending rule changes.

## Reproduction

Run the regression suite and validate_release.py for the release gate. Run trait_qualification.py to reproduce the trait matrix; output folders refuse differently pinned inputs. audit_trait_matrix.py summarizes completed cells and missing coverage. verify_bot_trace.py replays ordinary qualification folders without reselecting orders.

After the gate passes, balance_experiment.py is the controlled variant driver. Preserve baseline output, use paired seeds, rotate traits/strategies/seats, and record opponent controllers. Begin with production horizon zero; compare optional deeper search only as an explicitly experimental sensitivity test. Use substantially more seeds than the qualification screen for close balance decisions.
