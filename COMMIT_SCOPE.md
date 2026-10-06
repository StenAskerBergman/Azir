# Commit scope

`commit-scope.json` is the explicit scope for the next commit. Direct user instructions take precedence; record their scope here before staging. A request to commit progress does not automatically include every dirty file.

Each batch has a purpose, the exact starting `HEAD` in `base_commit`, and three lists of exact repository-relative paths:

- `include`: commit these paths for this batch, including intended deletions.
- `hold`: keep these changes local for now; do not commit them in this batch.
- `never`: local-only paths that must not be committed. Changing this designation requires a direct user instruction.

An unlisted path is **UNCLASSIFIED** and must stay out. Empty `include` means no commit is authorized by the manifest. Do not use directory names or wildcards. A file cannot appear in multiple lists. When unrelated changes share an included file, stage only the authorized hunks; inclusion of a path is not permission to commit unrelated edits.

Before each commit:

1. Read the user's current request and inspect both working-tree and staged changes. Update the scope for the bounded batch; do not reuse an old batch's inclusion list.
2. Stage explicit included paths or hunks. Preserve unrelated work, including changes already staged by someone else. If the existing index contains excluded work, stop before committing and resolve ownership rather than silently unstaging it.
3. Run `python -B tools/check_commit_scope.py`. It requires the manifest's base to match `HEAD`, rejects unclassified/excluded staged paths, and requires every included path to be staged. Then review `git diff --cached` and run the appropriate validation.
4. Commit and push only when requested. Report the commit and anything intentionally left local.

After a commit, the base no longer matches `HEAD`, so the manifest cannot authorize another commit unchanged. Start a fresh batch for the next request.

The checker enforces path scope, not hunk intent or gameplay correctness. It is a required workflow check, not an installed Git hook. `.gitignore` continues to protect local artwork, editor settings, personal notes, archives and generated caches; never force-add ignored files without explicit user authorization. Git storage and Workshop publication are separate decisions: reference drafts can be committed without belonging in a release package.
