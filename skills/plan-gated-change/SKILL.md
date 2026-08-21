---
name: plan-gated-change
description: Decide whether a proposed repository change may proceed as isolated maintenance or must be governed by an explicit execution plan and human approval. Use for architecture changes, production behavior, persistent data, identity/provenance, security or authorization, migrations, cross-boundary work, scoring or business semantics, rollback-sensitive changes, and requests to draft, approve, execute, or close a plan.
---

# Plan-Gated Change

Separate evidence, planning, authorization, implementation, promotion, and merge authority.

## Gate the Change

1. Read repository instructions and its plan policy. Repository rules override this generic workflow.
2. Inspect current code, tests, architecture boundaries, protected areas, branch, HEAD, and worktree.
3. Define the requested outcome, exact paths/systems, forbidden adjacent scope, and unresolved decisions.
4. Apply [the gate rubric](references/gate-rubric.md).
5. If isolated maintenance qualifies, state why no plan is needed, the smallest scope, required authorization, and verification.
6. If plan-gated, stop implementation until a responsible human approves a complete plan.

## Plan Contract

When authorized to draft a plan, include:

- Title, status, responsible human, scope, and forbidden scope.
- Source specifications and baseline checkpoint.
- Ordered, rollback-safe work packages.
- Acceptance criteria and negative cases.
- Verification and production-state evidence.
- Human decisions, progress, decision log, and closeout.

Create a draft only in the repository's designated location. A document that says `APPROVED` is not self-authorizing. Record approval only after the responsible human explicitly grants it.

## Authority Boundaries

Treat these as separate grants:

1. Draft a plan.
2. Approve the plan.
3. Implement the approved scope.
4. Write or promote production state.
5. Commit.
6. Push or open a PR.
7. Merge or deploy.

Never infer a later grant from an earlier one. Stop when a new policy choice, protected area, production mutation, destructive action, or scope expansion appears.

## Execution

When implementation is explicitly authorized:

- Re-establish the baseline and preserve unrelated work.
- Implement one work package at a time.
- Use disposable state and fixtures for development where possible.
- Update the plan factually; do not rewrite decisions to hide changes.
- Run targeted tests during work and the repository's full completion guardrail at the end.
- Compare protected production paths before and after.
- Mark completed only when acceptance criteria pass; otherwise record blocked or partial status.
- Move closed plans to the repository's completed-plan location when policy requires it.

## Output

Report the gate decision, evidence, smallest scope, forbidden scope, plan location/status, unresolved human decisions, authorization still required, verification commands, rollback boundary, and final worktree state.
