---
name: bootstrap-agent-harness
description: "Assess and establish a minimal repository-local harness for safe AI-assisted engineering: agent instructions, source-of-truth hierarchy, architecture map, protected areas, execution-plan policy, completion checks, and reusable verification entry points. Use when onboarding Codex or other agents to a repository, auditing missing guardrails, or making agent work repeatable across projects."
---

# Bootstrap Agent Harness

Build the smallest harness that makes repository facts discoverable and risky actions explicit. Do not replace executable safeguards with prose.

## Phase 1: Read-Only Assessment

1. Inspect repository instructions, branch, HEAD, remotes, worktree, languages, build system, tests, CI, deployment, persistent data, and ownership boundaries.
2. Trace the real dependency and data flow from external inputs through storage, domain logic, and presentation or outputs.
3. Identify authoritative code, schemas, data, specifications, and operational state. Report contradictions.
4. Inventory existing commands and classify them as deterministic/local, networked, production-mutating, destructive, or credential-dependent.
5. Identify protected areas: production data, migrations, identity, provenance, security, business semantics, deployment, and irreversible operations.
6. Compare findings to [the harness layers](references/harness-layers.md).
7. Propose changes in small checkpoints. Do not write until authorized.

## Phase 2: Repository Guidance

When authorized, create or refine repository-local guidance that states:

- Purpose and system boundary.
- Source-of-truth hierarchy.
- Repository map and verified dependency direction.
- Required workflow and completion evidence.
- Protected areas and human approval gates.
- Dirty-worktree preservation.
- Skill triggers and read-before-use rules.
- Known gaps without overstating guarantees.

Keep project-specific facts in repository docs, not in this skill.

## Phase 3: Executable Guardrail

Prefer one non-production-mutating completion entry point that composes existing lint, typecheck/build, tests, and domain verifiers. It may write ignored build artifacts or disposable temporary files; describe that accurately rather than claiming literal filesystem read-only behavior.

Do not:

- Include live acquisition, deployment, promotion, migration, or destructive commands.
- Require a clean worktree unless repository policy truly requires it.
- duplicate expensive checks unnecessarily.
- invent new tests or policy in the first wrapper change unless separately scoped.

Run each composed command and the wrapper itself. Preserve existing individual commands.

## Phase 4: Plan Policy

Define when execution plans are required, lifecycle locations, statuses, required fields, approval authority, production-promotion separation, and closeout. Use `$plan-gated-change` when available for plan decisions.

## Validation

- Resolve all documentation links.
- Search for stale or overstated claims.
- Run the repository completion guardrail and diff checks.
- Confirm production/protected paths are unchanged.
- Report exact files, commands, limitations, and final status.

Deliver harness work as reviewable checkpoints. Use `$deliver-scoped-change` when available for branch and PR delivery.
