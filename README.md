# Soulstorm Campaign Command — Atreus

The main app now runs the Atreus Subsector playtest. Cycle 1 is unopened. The grey command interface retains the original mobile navigation, faction registers, searchable systems and rules, record and Cycle narratives.

- [Active Atreus app](https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/)
- [Atreus briefings and complete reference](https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/atreus.html)
- [Suspended Dessica archive](https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/archives/dessica-cycle21-20261007/index.html)
- [Download Dessica archive](https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/Dessica_Archive_Cycle21_2026-10-07.zip)

## Updating Atreus

Resolve play in the referee chat, then update `Atreus_Campaign.md` and `atreus-status.json`. The app derives resources and traits from Major faction tables, holdings and fleets from system tables, projects from the Construction register, records from Cycle ledger and Cycle Records, and rules from the pinned appendix. Keep duplicate summary rows consistent. `Atreus_Setup_Registers.json` is the opening snapshot, not the live ledger.

Run `python build.py`, then publish the changed source files to main. GitHub Actions builds and deploys dist. Verify the published state before reporting completion. The site does not play turns, roll events or run background simulations. Phase 0 is construction effects, Logistics if due, then events. Do not advance past an unresolved player battle; publish its resolution only after the player reports the outcome.

## Dessica preservation

Dessica remains suspended at Cycle 21, revision `65dc4a60d17b`. The archive ZIP contains the exact original generated page, data and source files plus a browsable snapshot. Its manifest records SHA-256 hashes. The browsable copy disables service worker registration and initial polling and links back to Atreus; the original page is retained in `source/original-published-index.html`. The root Dessica ledger and status are unchanged.

On a clean checkout build.py extracts the checked-in archive ZIP into archives, then copies it to dist. Do not regenerate the archive from the active app. The original root README is preserved separately as README_Dessica_Archived_2026-10-07.md.

The Home Screen app uses the same URL and retains its identity, with an updated title and grey theme. Existing installations may keep their old OS-level icon/name until re-added. Offline caches are a convenience, never the authoritative campaign record.
