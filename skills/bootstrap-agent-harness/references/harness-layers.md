# Harness layers

## 1. Orientation

Repository purpose, map, architecture, terminology, and source-of-truth hierarchy.

## 2. Behavioral policy

Agent workflow, dirty-worktree rules, protected areas, authorization boundaries, forbidden operations, and domain invariants.

## 3. Executable verification

One safe entry point composing existing static checks, build/type checks, tests, and domain verifiers. CI may call the same entry point but is not required for an initial harness.

## 4. Plan governance

Rules for plan-required work, responsible-human approval, work packages, evidence, rollback, progress, and closeout.

## 5. Delivery controls

Narrow commits, branch isolation, draft PRs, changed-file verification, production-state comparison, and separate merge/deploy authority.

## Common gaps

- Documentation claims stronger guarantees than code provides.
- A dry-run workflow exists but other commands can still write production paths.
- Atomic replacement is mistaken for verification-before-promotion.
- Fixtures are confused with production evidence.
- Human approval is represented only by editable status text.
- Multiple verification commands exist without one safe completion entry point.
