# Azir development planner

Updated 7 October 2026. Use this planner to choose bounded repairs, preserve the author's country designs, and record the evidence needed before a Workshop release. The current codebase determines what is implemented; historical progress claims do not establish that a mechanic works.

## Trello and design intent

The author's board is [Runeterra Shurima on Trello](https://trello.com/b/kCzJIYNA/runeterra-shurima). Read relevant cards before planning country or focus-tree work. Access may require the author's signed-in account; do not assume another agent can access it. Board access does not authorize editing cards or messaging contributors.

The board was read during this session. Its lists included ICED, FIX LATER, TODO, DOING, COMPLETE, COMMENTS and BACKLOG. Recheck a card's current list and content when using it. ICED content is paused; a card's existence or historical move to COMPLETE is not evidence of current implementation or runtime acceptance.

Relevant context includes the [paused-focus guidance](https://trello.com/c/QlIt7L6r/81-these-focuses-either-are-for-some-reason-paused-until-further-notice), [Quarior state integration](https://trello.com/c/w0WGT19z/74-include-the-state-i-done-from-quariors-patch-it-is-always-a-dependencies-for-get-the-countries), and [gold and diamond implementation concern](https://trello.com/c/57sclUCg/110-so-some-focus-talk-about-gold-and-diamants-but-this-ressources-doesnt-exists). These provide intent to investigate, not permission to invent new resource systems or choose conflicting state owners.

## Author constraints

- Preserve the core essence of every country, focus tree, political route, narrative and intended outcome. The author invested substantial work in these designs. A compatibility repair is not a redesign.
- Keep repairs modest. Reuse existing systems and repair the smallest complete production path. Do not create duplicate authorities, test-only production paths, speculative abstractions, unrelated refactors or cleanup.
- Multiplayer is a release requirement. Avoid adding expensive recurring scans or machine-dependent behavior. Measure simulation performance and test synchronization rather than promising no lag or desync from static checks.
- Ship appropriate runtime art, not unused collections, source projects or entire downloaded artworks retained as development resources. Preserve originals outside the release package. Cropping or converting an image does not establish permission or suitability to distribute it.
- Preserve the loading-screen replacement intent. Check DLC, integrated-DLC, archive and interface paths as well as the main graphics folder. Existing registered choices are not automatically unused art.
- Fix actual duplicate full IDs and conflicting implementations. Sharing an event namespace alone is valid. Keep distinct authored behaviors separate rather than deleting or merging them merely because their IDs collided.
- Use the existing local checkout; do not create or select a worktree unless explicitly requested. Preserve all unrelated dirty and staged work, including ignored art. Do not spawn agents without an explicit request or applicable instruction requiring delegation.
- Make low-risk, reversible decisions and continue. Stop for a genuine architectural conflict, information needed for a safe implementation, dirty-state overlap that risks overwriting work, or a compile/crash/tooling failure that prevents execution.

## Planning and execution

Follow the author's sequence: **Authority -> Planning/Contracts -> Verification/Freeze -> Emission**.

1. Read current production definitions and callers, relevant Trello intent, and the author's instructions. Use [the progress review](HOI4_Modding_Progress_Review.md) for historical design context, then verify its claims in code.
2. Define the precise broken behavior and the smallest repair. Keep existing costs, timers, prerequisites, scopes, rewards, localization and artwork unless they are the defect being repaired. Do not add another architecture audit unless a concrete conflict prevents implementation.
3. Use the narrowest existing static or runtime proof appropriate to the behavior. If it fails, identify the failing production behavior, repair it, rerun the proof and continue. Verify the intended result and preserve unrelated work before delivery.
4. Report what works, files changed, verification results, concrete remaining blockers and a commit hash if committed. Distinguish source checks, native startup, visual inspection, gameplay progression and multiplayer acceptance.

For focus work, trace the focus definition, prerequisites and availability, rewards, called events and decisions, localization, sprite binding and actual texture. HOI4 Mod Utilities and CWTools are installed; their paths were corrected for the installed game. A VS Code tree preview helps assess layout but does not prove gameplay. The current tools cannot operate native VS Code or HOI4 UI.

## Recorded implementation status

This is the session checkpoint, not a claim that the entire mod is complete. Recheck it against later edits.

| Slice | Implemented and checked | Still requires verification |
| --- | --- | --- |
| Void Open University | `VOI_law_university` checks the defined and recruited `VOI_Zilean`. Other focus bytes were preserved. | Normal progression and reward in-game. |
| Exact ID collisions | Five Void events moved to `shurima_void`; two Targon BOP-panel decisions use `TAR_bop_influence_*`; four Shurima decisions use `SHU_void_*`. Existing internal callers and renamed localization were checked. Eleven targeted collision groups became zero in the modeled dependency stack; effects, costs and timers were preserved. | Native execution, save implications and multiplayer behavior. These are not proof of full event-chain completion. |
| Loading screens | Files cover 27 installed registered wallpaper names and 61 additional custom choices, each with thumbnails. Seven missing integrated-DLC copies were added; all ten integrated wallpaper paths exist. Hash checks passed for the new copies; 176 main-folder DDS headers passed. | Runtime selection, crop and appearance. Three older integrated full images differ from their main-folder counterparts and were preserved. |
| Native launch | HOI4 was launched with Runeterra, Quarior and local Azir, using debug logging. Fresh logs confirmed Azir content was read and reported missing textures. | Main-menu completion, a new 990 campaign, all gameplay paths and multiplayer. Inspect the current process before launching again; the game window belongs to the user. |

`python -B tools/validate_hoi4_mod.py` passed after the ID repairs. It checks selected focus structure and English localization; it is not the native parser and does not establish branch completion.

## Remaining bounded work

Choose one concrete behavior per repair batch. Reproduce or trace it before changing it; these items do not authorize new lore or balance decisions.

- Resolve the incomplete Void encounter chain. Missing outcomes remain, and two hidden encounter branches still point at unity events. Do not invent replacement outcomes to make references pass.
- Repair Targon character casing, Xerath's nonexistent conquest-focus target, Shurima's nonexistent speech mission and Void's missing idea references after identifying their intended targets.
- Trace assassination country/global flags and restore consistent initiating and receiving scopes. Settle the intended unity loss/recovery conditions and guild cadence before changing their behavior.
- Resolve conflicting state histories and missing GES/GSD/GWS/JGL OOBs against the intended 990 scenario. Ownership and cores are design decisions; do not pick an arbitrary duplicate file.
- Correct the extra interface brace, isolate game-loaded drafts from release, and repair required GFX confirmed by active consumers or native logs.
- Decide which disconnected shared focuses belong in the release. Paused drafts must not be imported automatically to inflate completion.

## Local layers and release evidence

Recorded installation paths:

- Game: `E:/SteamLibrary/steamapps/common/Hearts of Iron IV` (checked version 1.19.3).
- Runeterra: `E:/SteamLibrary/steamapps/workshop/content/394360/3032467701`.
- Quarior patch: `E:/SteamLibrary/steamapps/workshop/content/394360/3297129305`.
- Development Azir: this checkout, registered by `../Azir.mod`.
- Downloaded Workshop Azir: `E:/SteamLibrary/steamapps/workshop/content/394360/3274473271`; this is a separate copy and not proof of the server's latest contents. Do not enable both Azir copies for development testing.

The 7 October 2026 progress checkpoint is being committed and pushed on `main`, starting from `3f05d5fc24e971cfdcbd65598d65ddd2ad3ddbbd`, including the accumulated local script, localization, draft relocation and tooling work. The static validator passed again before committing; gameplay and multiplayer gates remain open. `gfx/` and `.vscode/` are ignored by Git; a commit does not capture the complete mod package. Generated Python caches are excluded. This Git checkpoint is not a Workshop publication. The launcher descriptors have stale supported-version metadata; only claim compatibility after testing the exact package and dependency versions.

Before publishing, verify a new 990 campaign, intended focus and decision routes, event outcomes, starting states/armies, required visuals, save/reload and a two-player run using the same package, dependencies and game version. Record errors, simulation stalls and out-of-sync incidents. Keep development material out of the upload and establish the origin and suitability of retained art. Publication requires a separate user instruction.

When updating this planner, record the affected production path, preserved design, evidence level and unresolved next step. Never promote a static pass or successful launch into full gameplay or multiplayer acceptance.
