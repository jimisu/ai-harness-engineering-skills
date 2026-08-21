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
7. Classify every finding using [the rubric](references/classification-rubric.md).
8. Propose the smallest safe correction or explain why no change is justified.
9. Identify protected behavior, required human decisions, plan requirements, and exact verification commands.
10. Report inspected files, commands, baseline limitations, production impact, and final worktree status.

## Evidence Standard

Require an exact current path, a concrete failure scenario, evidence that existing guards do not prevent it, a proportionate correction, and a test that can falsify the proposed fix. Downgrade claims based only on style preference, generic best practice, unmeasured performance, speculative scale, or stale code.

## Safety Boundaries

- Default to read-only behavior.
- Do not edit, stage, commit, push, open or merge PRs, or run live/production operations unless separately authorized.
- Do not accept severity labels from the supplied review without verification.
- Do not recommend concurrency without ordering, rate-limit, and partial-failure analysis.
- Do not recommend generic retry for all failures.
- Do not recommend memoization or caching without measured cost or a demonstrated lifecycle requirement.
- Do not combine unrelated cleanup with a confirmed fix.
- Require repository planning and approval for changes to production state, identity, provenance, security, authorization, financial/economic meaning, or cross-system behavior.

## Output Contract

For each finding provide:

1. Finding and reviewer claim.
2. Classification.
3. Current-code and test evidence.
4. Concrete failure scenario or reason the claim is unsupported.
5. Smallest safe scope.
6. Required tests.
7. Required human approvals and execution-plan status.

End with confirmed-and-safe, valid-but-plan-gated, optional, and incorrect-or-unsupported sections. State explicitly that evaluation does not authorize implementation.
