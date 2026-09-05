# Roadmap

This is a packaging and adoption plan, not an authorization document. It does
not change skill behavior by existing.

## Positioning

This repository is a small set of **agent change-control skills**.

It is for production-sensitive repositories where an agent must:

- treat another model's review as a hypothesis;
- separate planning, approval, implementation, promotion, and merge;
- refuse to mix unrelated work into a delivery unit;
- inventory a harness without overstating unenforced safeguards.

It is not:

- a harness-pattern encyclopedia;
- a one-click AGENTS.md generator;
- a multi-agent runtime, plugin marketplace product, or permission system.

Core skills:

- `verify-external-ai-review`
- `plan-gated-change`
- `deliver-scoped-change`
- `bootstrap-agent-harness`

Optional domain skill:

- `design-resilient-http-ingestion`

## Near term

1. Keep install paths inspectable: project-local copy, Agent Skills installers,
   and Claude Code plugin/marketplace manifests.
2. Keep a playground that demonstrates refusal and classification, not only
   happy-path scaffolding.
3. Add behavioral fixtures under `examples/playground/` and record results with
   the validation-case template. Structural validation remains mandatory; it
   still does not prove judgment quality.
4. Pin a reviewed tag in at least one consuming repository and publish a
   sanitized delivery case.

## Later, only on the same governance chain

Candidate skills must close a gap in verify → plan → implement → deliver.
Examples that may be considered:

- close-out of an approved plan without treating old approval as standing authority;
- protected-area classification that reports Always / Ask / Never without writing
  policy the repository does not enforce;
- review-baseline comparison when the supplied review targets a different SHA.

Do not add memory persistence, hook lifecycle, or multi-agent orchestration here.
Point consumers at dedicated harness-pattern or runtime projects instead.

## Release policy

Packaging and documentation land on `main` through the normal Draft PR process.
Version bumps, tags, and GitHub releases remain a separate maintainer action.
A merged documentation change does not publish `v0.2.0`.
