# Validation case: ai-infrastructure-monitor

The five skills were distilled from and checked against real repository events. Validation was read-only where the skill is read-only and used existing recorded diffs, plans, tests, and PR evidence for delivery workflows. No live ingestion or production promotion was used to validate the skills.

## Scenario matrix

| Skill | Real scenario | Expected behavior | Observed evidence |
|---|---|---|---|
| `verify-external-ai-review` | An external AI recommended timeout, retry, memoization, module relocation, parallel ingestion, dead-code removal, and an error boundary. | Verify each claim; separate confirmed, plan-gated, optional, and unsupported findings; do not implement during review. | Timeout/retry were valid and plan-gated; duplicated score formula was isolated; dead components and error boundary were optional; memoization, module relocation, and concurrency lacked evidence. |
| `plan-gated-change` | Compare a one-line verification command with cross-cutting HTTP reliability work. | Allow isolated semantically neutral maintenance without a plan; require a plan for production acquisition behavior crossing multiple boundaries. | `verify:agent` was a package-script-only checkpoint; timeout/retry required a completed execution plan and explicit human decisions. |
| `deliver-scoped-change` | Timeout/retry work was accidentally implemented on the existing review PR branch. | Detect mixed purpose, preserve work, checkpoint it, transfer it to a branch based on current main, and create a separate draft PR without rewriting history. | Work moved through a recoverable checkpoint and cherry-pick; the new SHA was correctly treated as normal; PR #2 contained one commit and 13 authorized files. |
| `bootstrap-agent-harness` | The repository initially had commands and domain safeguards but lacked a unified agent guide, architecture map, plan policy, and completion entry point. | Assess first; create documentation and executable guardrails in small checkpoints; avoid overstated claims. | The project added `AGENTS.md`, architecture and plan guides, then `verify:agent`; docs explicitly distinguished dry-run, atomic replacement, fixtures, human approval, and production facts. |
| `design-resilient-http-ingestion` | Seven HTTP acquisition paths lacked timeout/retry consistency. | Inventory all paths; design full-body timeout, selective bounded retry, cancellation, deterministic tests, snapshot/canonical boundaries, and a plan. | Shared transport covered 15-second attempts, three attempts, allow-listed statuses, Retry-After cap, caller abort, deterministic details, legacy acquisition, and no failed-attempt snapshots. Recorded verification passed 170 ingestion tests and five downstream verifiers with canonical hashes unchanged. |

## Cross-skill assertions

- Repository-local instructions remain authoritative.
- Review never implies implementation authority.
- A written plan never approves itself.
- Edit, commit, push, PR, ready, merge, production write, and deployment remain separate grants.
- Tests report evidence; they do not grant operational authority.
- Project-specific issuers, paths, commands, values, and error codes stay outside the generic skills.

## Validation limits

This case demonstrates transfer of the workflows across multiple real tasks in one repository. It does not prove universal applicability, compatibility with every agent product, or correctness for every language and deployment model. New adopters must test the skills against their own repository policy and failure modes.
