# Playground scenarios

These fixtures let a human or coding agent exercise the skills without a private
production repository. They are prompts and expected boundaries, not an
authorization to implement, push, or merge anything in a real project.

Use them on a throwaway branch of a disposable clone. Do not point them at
production data, credentials, or a dirty worktree you cannot reconstruct.

## How to run

1. Install only the skill under test into the target repository, or instruct the
   agent to read that skill's `SKILL.md` completely.
2. Paste the scenario prompt.
3. Compare the result with the expected boundaries in the scenario file.
4. If behavior is wrong, capture a sanitized case with
   [`docs/validation/CASE-TEMPLATE.md`](../../docs/validation/CASE-TEMPLATE.md).

Structural validation of this repository does not grade playground output.

## Scenarios

| File | Skill | What it should demonstrate |
|---|---|---|
| [toxic-external-review.md](scenarios/toxic-external-review.md) | `verify-external-ai-review` | Stale baseline, style-as-defect, and generic retry are classified; nothing is implemented. |
| [dirty-worktree-protected-path.md](scenarios/dirty-worktree-protected-path.md) | `plan-gated-change`, `deliver-scoped-change` | Overlapping dirty work and a protected path stop delivery; later Git actions stay unauthorized. |
| [empty-harness-assessment.md](scenarios/empty-harness-assessment.md) | `bootstrap-agent-harness` | Read-only inventory and a staged proposal; no files written until a human authorizes a checkpoint. |

`design-resilient-http-ingestion` is optional. Use it only in repositories that
actually acquire data over HTTP. Do not treat these scenarios as timeout or
retry standards.
