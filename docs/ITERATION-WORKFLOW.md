# Skill Iteration Workflow

## Purpose

GitHub is the canonical public source. Real projects are the proving ground.
Installed or copied skills are consumers, not independent sources of truth.

The loop is:

```text
observe in a real project
  -> capture a sanitized validation case
  -> propose the smallest skill change
  -> validate locally and in CI
  -> review in a Draft PR
  -> merge and release
  -> update consumers deliberately
  -> observe again
```

## 1. Observe

Record a concrete failure, ambiguity, unsafe action, unnecessary delay, or missing
capability. Preserve the user prompt, relevant repository facts, agent result, and
verification evidence when they can be shared safely. Do not copy credentials,
private code, production data, or confidential logs.

## 2. Classify

Decide whether the correction belongs in:

- repository-level guidance for users;
- `SKILL.md` for essential procedure and triggering;
- a referenced file for detailed conditional guidance;
- a deterministic script when repeated logic needs executable validation.

Keep project facts in the project. Generalize only the reusable decision process.

## 3. Propose narrowly

Define the behavior being changed, non-goals, affected skills, authorization
boundaries, and expected evidence. Prefer one purpose per pull request. Changes to
invocation policy, destructive actions, production authority, or permission
assumptions require explicit maintainer review.

## 4. Validate

For every change:

```bash
python3 scripts/validate_skills.py
git diff --check
```

For behavioral changes, add or update a sanitized validation case using
[`docs/validation/CASE-TEMPLATE.md`](validation/CASE-TEMPLATE.md). Exercise both a
successful case and an important refusal, stop, or negative case. Structural
validation checks package shape and links; it does not prove judgment quality.

## 5. Review and release

Open a Draft PR. Review the complete diff, changed-file list, validation evidence,
compatibility, authority changes, and documentation. Only a responsible human may
mark it ready, merge it, or publish a release.

Use Semantic Versioning as described in [`CONTRIBUTING.md`](../CONTRIBUTING.md).
After the release PR is merged, tag that exact reviewed commit as `vX.Y.Z` and
publish release notes derived from [`CHANGELOG.md`](../CHANGELOG.md).

## 6. Update consumers

Projects should pin a reviewed tag or commit. Update project-local copies on a
feature branch, inspect the entire changed-file set, run the target repository's
own safeguards, and deliver the update through its normal review process. Never
assume a package hash identifies a Git source version unless the lock format says so.

Personal installations may be updated from the released skill, but they should not
silently replace repository-local pinned copies. Different projects may remain on
different versions until each has validated the upgrade.

## Known limitations

- Agent behavior varies by model, product, tool access, and repository context.
- A passing example does not prove that a skill generalizes.
- A skill cannot grant authority that the user or repository has not granted.
- CI cannot validate production safety, economic judgment, or every future prompt.
- Public validation cases must be sanitized and may omit important private context.
