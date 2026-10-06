# Azir (Runeterra - Azir)

Before planning or editing, read [Planner.md](Planner.md) for the author's Trello board, design constraints, execution rules and current repair checkpoint. Current code determines implementation status; the progress review provides historical design context.

HOI4 submod that ports the League of Legends / Runeterra universe into Hearts of Iron IV. Depends on a base "Runeterra" mod (see `descriptor.mod`) — this mod adds/patches content on top of it, with a focus on Shurima, Targon, Void/Icathia, Xerath, and Nazumah.

Folder layout below is dictated by the HOI4 (Clausewitz engine) mod convention — files must live in the exact folder the engine expects or they won't load. A few folders are this project's own working areas and aren't read by the game at all; those are called out explicitly.

## Git-ignored (local only, not in the repo)
`.gitignore` excludes `gfx/`, `_info/`, `folder-alias.json`, `.vscode/`, and `NOTES and USEFUL CODE LINES.txt`. Don't expect changes there to show up in `git status`/diffs, and don't assume they're backed up anywhere but this machine.

## Engine-read folders (actual mod content)

- **`common/`** — the bulk of game-rules scripting: `national_focus/` (focus trees), `decisions/`, `ideas/`, `ideologies/`, `countries/` + `country_tags/` + `country_leader/`, `characters/`, `units/` + `unit_leader/`, `military_industrial_organization/`, `scripted_effects/` + `scripted_triggers/` (reusable script snippets), `on_actions/`, `opinion_modifiers/`, `dynamic_modifiers/`, `bookmarks/` (start dates), `bop/` (balance of power), `frontend/`. Write here when adding/editing game mechanics, focuses, decisions, ideas, characters, or unit rosters.
- **`events/`** — event chain `.txt` files, one file per faction/arc (e.g. `Shurima_events.txt`, `Targon_events.txt`, `Xerath_events.txt`). Look here to trace or extend a country's event chain.
- **`history/`** — starting-state data: `countries/` (per-tag starting political/military setup, filename `TAG - Name.txt`), `states/` (per-state ownership/buildings, filename `ID-Name.txt`, with subfolders per region), `units/` (starting OOB per tag).
- **`common/national_focus/`, `events/`, `history/`** together define "what exists in the world and what can happen" — the actual mod logic. This is where most day-to-day scripting work happens.
- **`interface/`** — `.gui` (window/widget layout) and `.gfx` (sprite-to-file bindings) definitions. This is the *plumbing* connecting UI to art — when adding new focus icons, idea icons, or character portraits, you register the mapping here (e.g. `focus-SHU_customicons.gfx`), pointing at files that actually live under `gfx/`.
- **`gfx/`** — the actual art assets: `interface/` (UI dds textures), `characters/` (portraits), `entities/` + `models/` (3D unit models), `event_pictures/`, `flags/`, `leaders/`, `loadingscreens/`, `minimap/`. Git-ignored — treat as local binary assets, not something to diff or expect in version control.
- **`localisation/english/`** — all in-game text as `..._l_english.yml`, generally one file per content area (e.g. `focus_SHU_shurima_l_english.yml`, `events_SHU_shurima_l_english.yml`, `ideas_SHU_shurima_l_english.yml`). Every new focus/event/idea/decision key needs a matching loc entry here or it'll show up as the raw key in-game. `_other_/` holds shared defs like text color codes (`__color.txt`), not per-country text.
- **`sound/`** — voice line `.wav` files (by unit/nation code, e.g. `hun/`, `tar/`) and `.asset` files binding them to in-game triggers. `sound/files/` has a shortcut/pointer to an external music folder rather than the audio itself.
- **`dlc/`, `integrated_dlc/`** — overrides/extensions for base-game DLC content (e.g. `dlc018_together_for_victory`) that this mod needs to patch GFX or data for. Only touch these if a specific DLC feature needs adjusting for compatibility.
- **`descriptor.mod`, `thumbnail.png`** — mod metadata read by the launcher/Steam Workshop. Edit `descriptor.mod` only for version bumps, dependency changes, or supported-version updates.

## Non-engine folders (your own reference material)

- **`documentation/`** — official HOI4 scripting reference (effects/triggers/modifiers/console commands etc.), copied from the game install, in `.md`+`.html` pairs. Read-only reference — look here first for correct effect/trigger syntax before guessing.
- **`_info/`** — personal scratch space, git-ignored: `Lore Notes/` (faction lore, focus-list drafts in plain `.txt`), `Code Library/` (reusable snippets and vanilla-file copies for reference, e.g. `MAN_decisions.txt`), `Icon Collection/` (source art/renders to eventually convert into `gfx/` assets), `TODO` (running task list), `_documentation/` (misc modding notes, some marked `old/`). Treat as working notes, not shippable mod content — nothing here is read by the game.
- **`other/`** — misc standalone notes that don't fit elsewhere (currently just `List of Terrible Things.txt`).
- **`HOI4_Modding_Progress_Review.md`** — the standing project status doc: what's built per faction/focus-tree, what's in progress. Update this when finishing a substantial chunk of work (a focus tree branch, an event chain) rather than trusting memory of what's done.
- **`NOTES and USEFUL CODE LINES.txt`** — grab-bag of copy-pasteable script snippets and reminders (e.g. the "every_country" trigger pattern, the GFX file layout needed per 3D soldier model). Git-ignored. Check here before re-deriving a snippet from scratch.
- **`README.md`** — currently a placeholder, not authoritative.

## Practical workflow implication

Adding a new piece of country content (e.g. a focus) typically touches four places: `common/national_focus/<tag>_focus.txt` (the focus itself), `localisation/english/focus_<TAG>_..._l_english.yml` (its text), `interface/focus-<TAG>_customicons.gfx` (icon binding), and `gfx/interface/goals/` (the actual icon file) — check all four before considering the work done.
