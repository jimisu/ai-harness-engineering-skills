# Classification rubric

## Confirmed and safe to fix now

Use only when current code demonstrates the issue, the correction is isolated, protected behavior is unchanged, and existing verification can cover it. A user must still authorize implementation.

## Valid but requires an execution plan

Use when the risk is real but the solution changes production behavior, crosses architectural boundaries, affects persistent state or identities, requires rollback/failure semantics, or leaves material human policy choices unresolved.

## Optional

Use for maintainability, cleanup, resilience, usability, or performance improvements with plausible value but no demonstrated current defect. Keep them separate from required fixes.

## Incorrect or unsupported

Use when the claim conflicts with current code/tests, depends on a stale baseline, mischaracterizes framework behavior, lacks a reproducible scenario, or proposes a solution without evidence of the underlying problem.

## Severity guidance

- **BLOCKER:** unsafe to merge or operate; credible irreversible, security, data-integrity, or authorization failure.
- **HIGH:** likely material failure in a normal or important path.
- **MEDIUM:** real defect with bounded impact or uncommon trigger.
- **LOW:** minor correctness, maintenance, or clarity issue.

Severity and disposition are independent. A high-risk concern can require design rather than an immediate patch.
