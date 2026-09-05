# Changelog

All notable changes to this project are documented here. Releases follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Stated the collection as governed agent workflows, with core change-control
  skills separated from the optional HTTP ingestion skill.
- Documented Agent Skills installer and Claude Code marketplace/plugin install
  paths, plus `.claude-plugin/` manifests for discovery.
- Added disposable playground scenarios for review verification, mixed dirty
  work, and read-only harness assessment.
- Added an adoption roadmap that keeps future skills on the verify → plan →
  deliver chain.

### Changed

- README installation now pins the documented `v0.1.2` tag in the copy example
  and tells consumers to inspect installer file lists before committing.

## [0.1.2] - 2026-08-25

### Changed

- Tightened `verify-external-ai-review` approval, classification-versus-priority,
  deterministic-test, informational-fact, plan-authority, and output-contract rules.
- Recorded the controlled A/B evaluation without overstating its single-experiment
  evidence.

## [0.1.1] - 2026-08-21

### Changed

- Corrected the `ai-infrastructure-monitor` validation case to distinguish
  retryable transport failures from persisted but unpromoted raw artifacts
  and to separate directly tested behavior from code-traced behavior.

## [0.1.0] - 2026-08-21

### Added

- Five reusable AI harness engineering skills.
- English and Traditional Chinese installation and usage documentation.
- Repository-wide structural validation and a real-project validation case.
- Contribution, iteration, validation-case, pull-request, and CI workflows.

[Unreleased]: https://github.com/jimisu/ai-harness-engineering-skills/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/jimisu/ai-harness-engineering-skills/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/jimisu/ai-harness-engineering-skills/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/jimisu/ai-harness-engineering-skills/releases/tag/v0.1.0
