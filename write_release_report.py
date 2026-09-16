from pathlib import Path
from datetime import datetime
import json
from readiness import require_ready
from sim_replay import inputs

def main():
 status=require_ready();date=datetime.now().strftime('%d %B %Y').lstrip('0');s=status['trait_matrix']
 report=f'''# Simulation readiness

Updated {date}. **Ready for controlled baseline testing of the numerical Subsector game with the production operational bots (horizon zero).** This is not a claim that the game is balanced or that bots reproduce optimal human play.

## Completed qualification

- {status['tests']} regression checks pass, including focused tests covering all 12 traits and interactions with deficits, upgraded fleets, construction and shipyards.
- 432 trait/strategy/seat games executed 100 Cycles each; {s['verified_orders']:,} orders replayed through public validation with matching state hashes.
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
'''
 Path('Simulation_Readiness_Report.md').write_text(report,encoding='utf-8')
 old=Path('Balance_Simulation_Report.md').read_text(encoding='utf-8-sig')
 if not old.startswith('> Historical'):
  Path('Balance_Simulation_Report.md').write_text('> Historical pilot report. For current qualification and full-game evidence, read Simulation_Readiness_Report.md and Trait_Qualification_Report.md. These older numerical results are preserved for provenance.\n\n'+old,encoding='utf-8')
 notes=Path('Campaign_Notes_2026-09-15.md');text=notes.read_text(encoding='utf-8-sig')
 text+=f'''\n## Production bot and trait qualification — {date}

All 12 traits now rotate independently across six strategies and three turn positions in a 432-game, 100-Cycle-per-game qualification matrix. The production controller accounts for multi-turn operations, combat effects, resources, repairs and diplomacy; a free-expansion policy error for Void Supremacy was corrected. {status['tests']} regression checks pass. Current readiness and measured evidence are in Simulation_Readiness_Report.md and Trait_Qualification_Report.md; earlier stagnation reports remain historical.

This qualifies scoped baseline comparisons, not a rebalance. Small-map duration must not be used as a representative campaign average; the two ten-system checks reached control at 52/68. Use more seeds and representative maps for the 50-100 Cycle target. Siege Doctrine and Dread Reputation have player/AI distinctions, so AI-only rankings cannot establish their full value in player games. Less-used construction/action strategies require targeted testing before recommendations about them. No numerical change has been adopted; Dessica stays suspended.
'''
 notes.write_text(text,encoding='utf-8')
 handover=Path('Simulation_Development_Handover.md')
 Path('Simulation_Qualification_Working_Archive_20260916.md').write_text(handover.read_text(encoding='utf-8-sig'),encoding='utf-8')
 handover.write_text(f'''# Current handover — {date}

## Status

The numerical Subsector baseline and production operational controller (horizon zero) passed the release gate. Read Simulation_Readiness_Report.md and Trait_Qualification_Report.md first. {status['tests']} regression checks pass; the 432-game trait matrix is complete and {s['verified_orders']:,} orders replayed exactly. All worker batches are complete. Existing earlier handovers/reports are historical and are preserved in the bundle.

## User intent and constraints

Work toward proper balance testing before changing the campaign notes' rules. All 12 traits must be fairly represented, with traits fixed between setup and rule-driven changes, not randomly changed each Cycle. The intended average duration is 50-100 Cycles with natural swing and shorter outliers. The user has not chosen the exact ending criterion: report surviving Major coalition and complete holding/Mobile Capital control separately. Human battle outcomes must remain external. Retain Supply costs when testing additional fleet Manpower costs. Preserve B21's baseline defensive-cost behaviour until an explicit alternative is selected.

Dessica remains suspended at Cycle 21 after the Korps turn, revision 65dc4a60d17b. No campaign advancement or event rolls are authorised during source/simulation work. sources/ is read-only. No balance rule was adopted by qualification.

## Reproducible implementation

operational_bots.py contains persistent operation plans, public-state odds and actual-effect probes, threat/economy budgets, repairs/retreats and construction priorities. bot_dispatch.py selects operational, old tactical or independent diagnostic controllers. operational_search.py is optional experimental look-ahead, not qualified by this release. bot_control.py supplies diplomacy/support decisions. Existing engine modules implement all 12 traits and 32 construction profiles.

trait_qualification.py covers 12 traits x 6 strategies x 3 seats x 2 replicates. Every game executes 100 Cycles; traits are assigned between games. Opponents are matched within seed/seat blocks, so raw seat aggregates do not isolate turn-order causation. Core changes invalidate recorded hashes; never reuse stale evidence as current. audit_trait_matrix.py checks coverage; verify_bot_trace.py replays standard cohorts; validate_release.py gates readiness. Run from an extracted Balance_Simulation_Bundle.zip for all evidence directories.

Evidence: trait-qualification-20260916 (all 432 results, compressed complete traces and input pins); bot-current-20260916 (reselection, fresh-process, large, allied, independent/legacy comparisons, stress and 200 Cycle observation). Bot_Behaviour_Review.json records audited cases and limits. simulation_readiness.json pins the release. Earlier bot-development-* and bot-release-20260916 folders are superseded and must not be substituted for current evidence.

## Next work

Begin controlled baseline studies for the campaign notes. Use representative map sizes, more seeds and varied opponents around each proposed change. Do not infer close trait rankings from two matrix replicates. Examine rare-action and less-used construction strategies in targeted scenarios before balancing them. Keep AI-only combat conclusions separate from player setup/difficulty. Record proposed variants separately and seek agreement before adopting rule changes.

## Publication and maintenance

Repository: https://github.com/NoxAnimusVicta/Soulstorm-Meta-Campaigns
Branch: main
Source library: https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/source.html
Suspended campaign: https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/

package_simulation.py bundles current code, evidence and historical work. build.py generates source.html and the unchanged campaign. The included GitHub Actions workflow publishes dist/ on main pushes. Browser upload is available through the signed-in repository owner session; no claim of publication should be made without a successful deployment and live-content check. The final chat response records verification of this release. Do not change repository visibility.
''',encoding='utf-8')
 print('Wrote current readiness, dated notes and handover')
if __name__=='__main__':main()
