# Faction control handover

Source v0.1 • 2026-09-15

A handover does not advance time, refresh actions, grant resources, change traits or resolve battles.

| Field | Confirmed value |
|---|---|
| Date / Cycle / exact phase | [value] |
| Outgoing player faction / new AI | [value] |
| Incoming player faction / advisor | [value] |
| Authoritative document / source version | [links/revision] |
| Resources / deficit tracks | [values] |
| Fleets / locations / used actions | [register] |
| Holdings / constructions / effects | [register] |
| Pending battles / approved conditional orders | [list] |
| Diplomacy / commitments / private knowledge | [recipient-specific scope] |
| Commander / ages / successor / trait | [values] |
| Next decision | [specific] |

Instantiate the Commander briefing for the outgoing player faction's AI and Advisor briefing for the new player faction. Preserve doctrine, palette, identity and decisions. Confirm who controls each faction; do not automatically transfer confidential knowledge. Log and publish the handover at the next authorised update, respecting unresolved player battle timing.
