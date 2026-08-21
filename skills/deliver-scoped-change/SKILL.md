---
name: deliver-scoped-change
description: Package an authorized repository change into a clean checkpoint, correctly based feature branch, and narrowly scoped pull request while preserving unrelated work and separating edit, commit, push, PR, review-readiness, and merge authority. Use when preparing or repairing branches, commits, cherry-picks, PR scope, draft status, changed-file sets, or delivery verification.
---

# Deliver Scoped Change

Keep one purpose per delivery unit. Treat every irreversible or externally visible step as a separate authorization boundary.

## Preflight

1. Read repository instructions and relevant plan or specification.
2. Inspect branch, HEAD, upstream, remotes, base/head relationship, worktree, staged and unstaged diffs, untracked files, and recent history.
3. Build an explicit authorized-file list. Classify every current change by purpose and ownership.
4. Stop if unrelated or ambiguous changes overlap the delivery. Never stage them.
5. Confirm the correct base and whether an existing matching branch or PR must be reused.

## Verify Scope

- Compare the complete change against the intended base, not only the worktree.
- Confirm generated files, lockfiles, plans, tests, and docs belong to the same purpose.
- Confirm protected paths and production state are unchanged unless explicitly authorized.
- Run targeted checks, the repository completion guardrail, and diff/whitespace checks.
- Record failures honestly; do not label environment failure as test failure or success.

Use [the delivery checklist](references/delivery-checklist.md) for exact evidence.

## Deliver Safely

1. Stage only explicit authorized paths; never stage the whole repository by convenience.
2. Create a local checkpoint only when commit authority exists.
3. If work is on the wrong branch, preserve it with a recoverable checkpoint, create the correct branch from the exact approved base, and transfer only the intended commit using a non-history-rewriting method.
4. Re-run scope and verification checks after transfer.
5. Push only with separate authorization and use a normal push. Never force-push or rewrite history without explicit destructive-action approval.
6. Reuse an existing matching PR. Otherwise create a draft PR unless the user explicitly requests ready status.
7. Include scope, exclusions, verification, production impact, and unresolved decisions in the PR body.
8. Verify local and remote SHAs, upstream ahead/behind, base/head, commit count, changed files, draft/open state, and clean worktree.

## Permission Ladder

Do not infer later steps from earlier ones:

`edit → stage/commit → push → create PR → mark ready → merge/deploy`

Moving through one arrow requires explicit authority or a request that unmistakably includes it. Never merge merely because verification passes.

## Special Cases

- A cherry-picked commit normally receives a new SHA; verify content equivalence rather than expecting identity.
- A PR may contain multiple commits. Use squash merge only when repository policy and the responsible human choose it.
- If a completed plan remains in an active location, close it according to repository policy before delivery.
- If the remote branch disappeared, do not recreate or overwrite it by assumption; determine whether the PR was merged, closed, or deleted.

## Report

Provide base and head SHAs, branch/upstream, commit count, exact changed files, verification results, protected-state comparison, external actions performed, PR URL/state when applicable, ahead/behind, and final worktree status.
