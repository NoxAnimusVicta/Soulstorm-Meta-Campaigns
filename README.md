# The Dessica Campaign

Mobile campaign reference for Safari and iPhone Home Screen, built from the authoritative Markdown document. No server, API keys, package downloads or JavaScript dependencies are needed.

## Campaign updates

1. Resolve the Cycle in the referee chat.
2. Update `Dessica_Campaign.md`, including every affected tracker and system entry.
3. Update `campaign-status.json`: the matching cycle number, phase, event, next faction, update label and notes. Do not invent event rolls or unresolved battle outcomes.
4. Run `python3 build.py`. It validates the matching cycle and generates the dashboard from the document.
5. Commit and push to `main`. The included GitHub Actions workflow builds and deploys `dist` to GitHub Pages.

This automates publication after a push. It does not observe ChatGPT conversations, play turns, or create event rolls independently. The referee pushes the updated record after resolving each Cycle.

## Initial publication

Push this project to the chosen GitHub repository. In Settings → Pages, choose GitHub Actions as the source. Run the Publish Dessica Campaign workflow if needed. The deployment job reports the live URL. GitHub Pages visibility depends on the account and repository configuration; confirm the intended audience before enabling publication.

## iPhone

Open the live URL in Safari, then Share → Add to Home Screen → Add. Keep Open as Web App enabled if shown. The icon opens in a standalone window. Visit online once to save offline assets. The app checks the published campaign on launch, on returning to the foreground, and once per minute while visible. Refresh checks immediately. Offline copies may be evicted by iOS; this is a reference cache, not the authoritative record.

## Structure

- `Dessica_Campaign.md`: full campaign rules, setting and state.
- `campaign-status.json`: explicit referee status, never inferred as a rolled event.
- `build.py`: dependency-free Markdown subset renderer and data extraction.
- `index.template.html`, `style.css`, `app.js`: mobile interface.
- `sw.template.js`: network-first offline cache.
- `dist/`: generated standalone site. Its HTML includes the initial data, styles and scripts and can be opened locally for a preview. Hosting enables offline caching and live updates.

All campaign content is escaped before rendering; raw HTML in campaign text is displayed literally. On iPhone, bottom navigation stays within thumb reach, faction details collapse, and rules tables become labelled cards. Search uses 17px input text and retains query and scroll position when switching tabs. Larger displays retain tables. The app preserves conflicting rules exactly as written for referee adjudication.

## Publication destination

- Repository: https://github.com/NoxAnimusVicta/Soulstorm-Meta-Campaigns
- Branch: main
- Publication: GitHub Actions, publishing dist/
- Live website: https://noxanimusvicta.github.io/Soulstorm-Meta-Campaigns/ (verified 10 September 2026)
- Repository and intended website visibility: public.


## Referee update policy

Publish both the campaign Markdown and generated website whenever campaign state or an agreed ruling changes, including mid-Cycle events. Rebuild, push to main, and verify Pages before reporting publication complete. Do not advance a Cycle merely to update the site. The website rules index uses level 2 and 3 headings. Level 4 headings stay inside their parent entry: individual phase actions are subheadings, not separate dropdowns. Within Turn Structure, each Phase 0–7 is the dropdown container for all of its mechanics. Fleet Battles and Void Superiority belong to Phase 2; Summon Allies belongs to Phase 3; all construction guidance belongs to Phase 5. Use level 4 subheadings within those phases, never separate dropdowns for their mechanics.

The ChatGPT project attachment is a separate copy. This local task cannot replace that attachment through a project-file tool; the user must replace it with the latest Dessica_Campaign.md download so other project chats receive the updated reference.
