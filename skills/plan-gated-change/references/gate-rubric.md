# Gate rubric

## Plan usually required

- Multi-step or operationally high-risk work.
- Production behavior, deployment, or persistent-state changes.
- Schema, identity, provenance, revision, migration, or compatibility changes.
- Security, privacy, access-control, or credential-flow changes.
- Business, financial, ranking, threshold, confidence, or scoring semantics.
- Work crossing multiple architecture or ownership boundaries.
- Changes with partial-failure, rollback, backfill, or irreversible consequences.
- Material unresolved policy choices.

## Plan may be unnecessary

A change may proceed without a plan only when it is isolated, reversible, outside protected areas, semantically neutral, covered by existing verification, and explicitly authorized. Examples include a package-script alias, a typo, or replacing a duplicated calculation with its already-authoritative function without changing behavior.

## Stop conditions

Stop when the worktree contains overlapping unknown changes, the baseline is stale, current code conflicts with recorded data, approval is ambiguous, acceptance criteria cannot be tested, or implementation exposes a new material decision.
