# AI Harness Engineering Skills

[繁體中文](README.zh-TW.md)

Current version: `0.1.2`

Five reusable agent skills distilled from building, reviewing, planning, implementing, verifying, and delivering a production-sensitive AI data-monitoring project.

These skills teach workflow. They do not copy project-specific companies, schemas, commands, scoring rules, or production paths into other repositories.

## Skills

| Skill | Use it when |
|---|---|
| `verify-external-ai-review` | Another AI, tool, or reviewer supplies findings that must be checked against current code and tests. |
| `plan-gated-change` | A change may require an execution plan, human decisions, rollback boundaries, or protected-area approval. |
| `deliver-scoped-change` | Changes must be isolated into the correct commit, branch, and pull request without mixing unrelated work. |
| `bootstrap-agent-harness` | A repository needs agent instructions, an architecture map, plan policy, protected areas, and one safe completion command. |
| `design-resilient-http-ingestion` | An HTTP data pipeline needs timeout, retry, cancellation, deterministic tests, and no-partial-promotion guarantees. |

## Installation

### Recommended: project-local installation

Clone or download this repository, inspect the selected skill, then copy only its complete directory into the target repository:

```bash
mkdir -p .agents/skills
cp -R /path/to/ai-harness-engineering-skills/skills/verify-external-ai-review \
  .agents/skills/verify-external-ai-review
```

Repeat for each selected skill. Commit project-local skills with the target project so every agent and reviewer sees the same instructions.

Before accepting the copy:

```bash
python3 /path/to/ai-harness-engineering-skills/scripts/validate_skills.py
git status --short
git diff --check
```

Review `SKILL.md`, every referenced file, and `agents/openai.yaml`. Do not install a skill based only on its name or README.

### Agent skill registry or installer

If your agent supports GitHub skill installation, point it at this repository and name the exact skill. Installer syntax varies by product and version. Some installers may ignore a skill filter and copy the whole repository. Always install on a clean feature branch, inspect the complete changed-file set, remove unrequested directories explicitly, validate, and commit only the intended skill.

### Manual use without registry support

Any coding agent that can read Markdown can use these skills. Instruct it to read the selected `SKILL.md` completely and follow repository-local policy first:

```text
Read .agents/skills/verify-external-ai-review/SKILL.md completely.
Then evaluate this review against the current repository in read-only mode.
Repository instructions override generic skill guidance.
```

`agents/openai.yaml` provides OpenAI-specific UI metadata. Other agents may ignore it safely.

## Recommended adoption order

1. Start with `bootstrap-agent-harness` in read-only assessment mode.
2. Add repository-local `AGENTS.md`, architecture navigation, plan policy, and a non-production-mutating completion command in separately reviewed checkpoints.
3. Use `verify-external-ai-review` for outside review reports.
4. Use `plan-gated-change` before cross-boundary or protected work.
5. Use `deliver-scoped-change` for commit/branch/PR delivery.
6. Add `design-resilient-http-ingestion` only to projects with external HTTP acquisition.

## Usage examples

### Validate an AI review

```text
Use $verify-external-ai-review. Treat every supplied finding as a hypothesis.
Read repository instructions first, verify against current code and tests,
classify each finding, and do not implement anything.
```

### Decide whether work needs a plan

```text
Use $plan-gated-change to determine whether this change is isolated maintenance
or plan-gated work. List protected areas, unresolved human decisions, forbidden
scope, authorization still required, and exact verification.
```

### Deliver one clean PR

```text
Use $deliver-scoped-change. Inspect all staged, unstaged, untracked, and committed
differences against the intended base. Stop on unrelated work. Do not infer push,
PR, ready-for-review, or merge authority from permission to edit or commit.
```

### Bootstrap a repository harness

```text
Use $bootstrap-agent-harness in read-only mode. Inventory source-of-truth,
architecture, commands, protected areas, and existing safeguards. Propose the
smallest staged harness; do not create files until authorized.
```

### Design reliable ingestion

```text
Use $design-resilient-http-ingestion to inventory every HTTP acquisition path,
trace persistence timing, and propose a full-body timeout, bounded selective
retry, Retry-After, caller-abort, deterministic-test, and no-partial-promotion contract.
```

## Composition

These skills can be combined, but each retains its boundary:

```text
bootstrap-agent-harness
  -> verify-external-ai-review
  -> plan-gated-change
  -> domain implementation skill
  -> deliver-scoped-change
```

They complement interviewing, domain-modeling, ADR, and handoff skills. They do not replace repository policy or executable tests.

## Limitations

- Skills are instructions, not a security sandbox or permission system.
- They cannot prove correctness without current code, tests, runtime evidence, and human review.
- Repository-local instructions and applicable law/policy override generic guidance.
- A plan document cannot authorize itself; a responsible human must approve it.
- Passing tests does not authorize production writes, deployment, merge, or business-semantic changes.
- `deliver-scoped-change` does not make destructive Git operations safe by default.
- `bootstrap-agent-harness` must not overstate safeguards that code does not enforce.
- `design-resilient-http-ingestion` supplies a design method, not universal timeout or retry values.
- Different agent products resolve skills and invocation metadata differently.

## Supply-chain safety

Pin a commit or reviewed release when importing. Inspect all files, compare hashes if your installer provides them, and do not assume a lockfile hash is a source version unless its format explicitly records a commit or release. Install on a branch, verify the exact file list, and avoid running unknown scripts before review.

## Validation

Run:

```bash
python3 scripts/validate_skills.py
```

The script validates required files, frontmatter names/descriptions, directory-name consistency, OpenAI metadata, and local Markdown references. It does not evaluate behavioral quality.

See [the ai-infrastructure-monitor validation case](docs/validation/ai-infrastructure-monitor.md) for the real project scenarios used to derive and test the workflows.

## Publishing and versioning

Use semantic tags for public releases. Record the source commit in release notes or your consumer lockfile. Review skill changes like code: show the diff, validate every skill, and avoid silently changing invocation policy or authorization boundaries.

To improve the collection, read [CONTRIBUTING.md](CONTRIBUTING.md), follow the
[iteration workflow](docs/ITERATION-WORKFLOW.md), and record behavioral evidence
with the [validation case template](docs/validation/CASE-TEMPLATE.md). Release
history is recorded in [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [MIT License](LICENSE).
