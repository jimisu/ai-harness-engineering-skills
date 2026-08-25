---
name: verify-external-ai-review
description: Validate an external AI, automated, or human code review against the current repository before accepting or implementing its findings. Use when a user supplies review comments, an audit report, refactoring recommendations, a PR review, or another agent's analysis and wants evidence-based classification, scope, approvals, and verification without treating the review as authoritative.
---

# Verify External AI Review

Treat every supplied finding as a hypothesis. Establish current repository facts before judging it.

## Workflow

1. Read repository agent instructions and relevant architecture, policy, and execution-plan documents completely.
2. Inspect branch, HEAD, remotes, worktree status, base/head relationship, and relevant history.
3. Preserve unrelated work. Stop if existing changes overlap the review scope or their ownership is unclear.
4. Identify the review's claimed baseline. Report when it differs from the current code or PR head.
5. For each finding, inspect the exact implementation, callers, tests, configuration, and runtime path. Search the complete repository; do not rely on filenames quoted by the reviewer.
6. Run only safe, non-mutating diagnostics authorized by the request. Never convert a review request into implementation.
7. Classify every finding and assign priority or severity separately using [the rubric](references/classification-rubric.md). Represent true but non-defective facts explicitly as informational or as unsupported defect claims.
8. Propose the smallest safe correction or explain why no change is justified. For deterministic-test recommendations, evaluate every relevant injected dependency and explain any intentionally narrow replacement.
9. Identify protected behavior, required human decisions, plan requirements, and exact verification commands. Never equate no plan required with no approval required.
10. Report the complete review baseline, evidence inspected or executed, conclusions based only on inspection, authorization still required, plan status, and final worktree status.

## Evidence Standard

Require an exact current path, a concrete failure scenario, evidence that existing guards do not prevent it, a proportionate correction, and a test that can falsify the proposed fix. Downgrade claims based only on style preference, generic best practice, unmeasured performance, speculative scale, or stale code. When deterministic testing is proposed, inspect relevant fetch, sleep, randomness, and clock/time dependencies rather than assuming one injection point is sufficient.

## Safety Boundaries

- Default to read-only behavior.
- Do not edit, stage, commit, push, open or merge PRs, or run live/production operations unless separately authorized.
- Do not accept severity labels from the supplied review without verification.
- Do not recommend concurrency without ordering, rate-limit, and partial-failure analysis.
- Do not recommend generic retry for all failures.
- Do not recommend memoization or caching without measured cost or a demonstrated lifecycle requirement.
- Do not combine unrelated cleanup with a confirmed fix.
- Require repository planning and approval for changes to production state, identity, provenance, security, authorization, financial/economic meaning, or cross-system behavior.
- Treat approved or completed plans as design and scope history, not standing authority. Require current human authorization for each implementation, commit, push, merge, tag, release, production operation, or other externally visible action.

## Output Contract

For each finding provide:

1. Finding and reviewer claim.
2. Classification.
3. Priority or severity, reported independently from classification.
4. Current-code and test evidence.
5. Concrete failure scenario or reason the claim is unsupported.
6. Smallest safe scope.
7. Required tests.
8. Required human approvals and execution-plan status.

For the evaluation as a whole, report the skill used or explicitly `none`; exact branch, HEAD, and review baseline; files and commands actually inspected or executed; tests actually executed; conclusions based only on inspection; required human authorization; execution-plan status; and final worktree status.

End with confirmed-and-safe, valid-but-plan-gated, optional, incorrect-or-unsupported, and—when needed—clearly separate informational/non-actionable sections. State explicitly that evaluation does not authorize implementation.
