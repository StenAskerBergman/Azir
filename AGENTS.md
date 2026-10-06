# Agent guidance

Read [Planner.md](Planner.md) before planning or editing this mod. It contains the author's Trello board, design and multiplayer constraints, execution rules, recorded repairs and remaining release blockers.

Use current code as implementation truth and preserve unrelated work in this local checkout. Follow direct user instructions over documentation. Use [CLAUDE.md](CLAUDE.md) for folder conventions and [the progress review](HOI4_Modding_Progress_Review.md) for historical design context.

Before staging or committing, follow [COMMIT_SCOPE.md](COMMIT_SCOPE.md) and the current `commit-scope.json`. Never infer commit scope from dirty status, folder membership, or an earlier commit request. Never use blanket `git add -A` or `git add .`. Run `python -B tools/check_commit_scope.py` against the final staged index before every commit; a failure blocks the commit. Preserve excluded and unrelated staged work without resetting or unstaging it unless authorized.
