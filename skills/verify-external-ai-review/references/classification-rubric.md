# Classification rubric

Classification describes evidentiary disposition: confirmed, plan-gated, optional, or unsupported. Priority or severity describes urgency and impact. Report them independently; a confirmed documentation or maintenance defect may be safe to fix while remaining low priority.

## Confirmed and safe to fix now

Use only when current code demonstrates the issue, the correction is isolated, protected behavior is unchanged, and existing verification can cover it. A user must still explicitly authorize implementation. “No execution plan required” describes process overhead only; it never means “no approval required.”

## Valid but requires an execution plan

Use when the risk is real but the solution changes production behavior, crosses architectural boundaries, affects persistent state or identities, requires rollback/failure semantics, or leaves material human policy choices unresolved.

## Optional

Use for maintainability, cleanup, resilience, usability, or performance improvements with plausible value but no demonstrated current defect. Keep them separate from required fixes.

## Incorrect or unsupported

Use when the claim conflicts with current code/tests, depends on a stale baseline, mischaracterizes framework behavior, lacks a reproducible scenario, or proposes a solution without evidence of the underlying problem.

If a statement is factually true but does not demonstrate the claimed defect, classify the defect claim here or place the fact in a clearly separate informational/non-actionable section. Do not omit it from the declared disposition.

## Informational or non-actionable facts

Use a separate section for verified context that is not itself a defect, improvement request, or implementation reason. State why it is non-actionable and do not count it as a confirmed finding.

## Priority and severity guidance

- **BLOCKER:** unsafe to merge or operate; credible irreversible, security, data-integrity, or authorization failure.
- **HIGH:** likely material failure in a normal or important path.
- **MEDIUM:** real defect with bounded impact or uncommon trigger.
- **LOW:** minor correctness, maintenance, or clarity issue.

Priority/severity and classification are independent. A high-risk concern can require design rather than an immediate patch; a confirmed low-impact defect can be low priority.

## Deterministic-test recommendations

Evaluate every dependency that can make the behavior nondeterministic, including sleep, randomness, clock/time, and fetch behavior. If replacing only one dependency is sufficient, identify the others and explain why they are already deterministic, irrelevant to the tested path, or safely controlled.

## Authorization and plans

Classification never grants implementation authority. An approved or completed execution plan may preserve design and scope history, but it does not self-authorize later edits. Record the current human authorization separately for implementation, commit, push, merge, tag, release, production operations, and other externally visible actions as applicable.
