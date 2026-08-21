---
name: design-resilient-http-ingestion
description: Design or review reliable HTTP acquisition for evidence, ETL, crawler, API-sync, and ingestion pipelines, including full-body timeouts, bounded selective retries, Retry-After, caller cancellation, deterministic errors and tests, idempotency, snapshot boundaries, and prevention of partial promotion. Use before implementing or auditing network reliability in data pipelines.
---

# Design Resilient HTTP Ingestion

Treat transport reliability as observable production behavior. Design before changing every acquisition path.

## Inventory Current Behavior

1. Read repository rules, architecture, data contracts, and plan policy.
2. Inventory every production HTTP entry point, including shared clients, direct calls, legacy collectors, discovery, evidence download, redirects, and body consumption.
3. Record source class, method, authentication, rate limits, current errors, timeout/retry behavior, and caller cancellation.
4. Trace the exact order of fetch, body read, snapshot persistence, parsing, validation, canonical promotion, verification, and report persistence.
5. Determine what partial raw, manifest, canonical, or report state can remain after each failure.
6. Require an execution plan when behavior crosses acquisition, persistence, orchestration, or production boundaries. Use `$plan-gated-change` when available.

## Define the Contract

Specify explicitly:

- Per-attempt timeout covering headers, redirects, and complete body consumption.
- Total attempts, retryable methods, statuses, network/body failures, and timeouts.
- Non-retryable caller abort, authentication/access denial, validation, parser, provenance, identity, and business-semantic failures.
- Exponential backoff, cap, jitter, and exact `Retry-After` delta/date behavior.
- Caller `AbortSignal` composition, reason preservation, and immediate cancellation during fetch, body read, or backoff.
- Fresh timeout state and timer/listener cleanup for every attempt.
- Deterministic public error codes/details and nondeterministic fields to exclude.
- Whether failed responses or attempts may become forensic snapshots.
- Idempotency and identity invariants across retries.

If the helper consumes the body, define a return structure containing response metadata and the consumed bytes. Never require callers to read a consumed body again.

Use [the review checklist](references/http-reliability-checklist.md).

## Make Tests Deterministic

Inject `fetch`, `sleep`, clock, and randomness. Tests must not use real networks or real delays. Prove call counts, requested delays, retry classification, `Retry-After`, already-aborted signals, cancellation during every phase, timeout during headers and body, cleanup, exhaustion, error mapping, idempotency, and byte-for-byte protected-state isolation.

## Safety Boundaries

- Do not retry all errors or all 5xx responses by default.
- Do not retry access-control failures to work around intentional denial.
- Do not persist failed attempts as trusted evidence by default.
- Do not let attempts, timing, jitter, stacks, or acquisition time enter economic/canonical identity.
- Do not run live ingestion for implementation verification unless separately authorized.
- Do not claim atomic file replacement is verification-before-promotion.
- Preserve issuer/domain validation outside the transport helper.

## Output

Provide the inventory, behavioral contract, alternatives, smallest safe scope, affected boundaries, acceptance criteria, negative tests, unresolved human decisions, plan requirement, verification commands, and protected-state comparison.
