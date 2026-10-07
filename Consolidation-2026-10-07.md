# Consolidation checkpoint - 7 October 2026

The existing Documents checkout on main is the consolidation authority. Git reports one registered worktree. Menu alignment and Xerath alignment are already committed here. RuneTerraMap, alt and codex/country-selection-menu have no commits outside main; their refs are retained for recovery. No new checkout was created.

The current checkpoint includes scenario navigation, menu background bounds, repair receipts and two Shuriman infantry voice clips plus bindings. Error.Log is a local diagnostic and is excluded. Existing ignored graphics and personal source material are preserved. Git does not capture the runtime graphics described by the model/background receipts.

## Branch conflict requiring a design decision

dj's-branch contains five unique commits. A read-only git merge-tree trial reports seven conflicts: Shurima characters, traits, economic laws, focus tree, events, starting history, and a modified lore draft relocated on main. These concern authored Sivir ascension and country design. No automatic ours/theirs resolution or merge was performed; branch refs and content are intact. Integrating these changes requires comparing intended mechanics against the current Shurima routes rather than selecting one side wholesale.

## Runeterra expansion preparation

The known Runeterra and Quarior locations are Steam-managed Workshop downloads, not verified source checkouts. Do not use them as the authoritative merge destination. The source repository/path has been requested from the user. Azir currently depends on both layers; their state histories and replacement-path semantics must be reconciled before removing dependencies or producing a combined descriptor. Do not copy Azir's Workshop identity into a Runeterra release descriptor.

A runtime path/size inventory and exact-path overlap lists are saved outside the mod at ../Azir-consolidation-20261007/runtime-inventory.json. They describe the current files, not semantic conflict resolution or an asset backup. Cleanup should exclude documentation, personal source material, caches and diagnostics from the release package while preserving development originals. Registered loading screens and dynamically selected models must not be deleted based on a text search alone.

This checkpoint is not a published major expansion. Native campaign, visual, save/reload and multiplayer release gates remain open as recorded in Planner.md. No game restart or Workshop publication was performed.
