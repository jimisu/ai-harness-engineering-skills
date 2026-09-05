# Contributing

Thank you for improving these skills. Treat a skill change like a code change:
state the problem, keep the patch narrow, test it on realistic work, and make
authorization boundaries visible.

## Before changing a skill

1. Open an issue or describe the observed failure in the pull request.
2. Include a real or sanitized prompt, the relevant output or trace, and why the
   current behavior is unsafe, unclear, inefficient, or incomplete.
3. Check whether the problem belongs in repository documentation, a skill's
   `SKILL.md`, or a bundled reference. Do not add project-specific facts to a
   reusable skill.

## Development workflow

1. Branch from current `main`.
2. Prefer one behavioral purpose per pull request.
3. Edit only the affected skill and directly related repository documentation.
4. Add or update a file under `docs/validation/` when behavior changes.
5. Run `python3 scripts/validate_skills.py` and `git diff --check`.
6. Open a Draft pull request using the repository template.
7. Obtain human review before marking the pull request ready or merging it.

Do not put `README.md`, changelogs, or installation guides inside an individual
skill directory. Keep user documentation at repository level; keep only agent
instructions and necessary resources inside each skill.

Playground scenarios live under `examples/playground/` and are fixtures, not
skills. Do not add project-specific production facts to them. Plugin and
marketplace manifests live under `.claude-plugin/` and must stay valid JSON
without claiming extra authority.

## Versioning

This repository uses Semantic Versioning:

- PATCH: wording or workflow corrections that preserve triggering and authority.
- MINOR: new skills or backward-compatible capabilities.
- MAJOR: incompatible invocation, authorization, file-layout, or behavioral changes.

Update `CHANGELOG.md` with user-visible changes. The maintainer updates `VERSION`,
merges the reviewed release changes, creates the matching `vX.Y.Z` tag, and
publishes release notes. A pull request does not authorize its own release.

## Safety and scope

- Never include secrets, private production data, or proprietary traces.
- Sanitize validation artifacts before committing them.
- Never weaken human approval, production-write, deployment, merge, or destructive
  operation boundaries without explicit discussion and maintainer approval.
- Passing structural validation does not prove behavioral correctness.
- Consumers must inspect and pin a reviewed release or commit.

See [the iteration workflow](docs/ITERATION-WORKFLOW.md) for the full lifecycle.
