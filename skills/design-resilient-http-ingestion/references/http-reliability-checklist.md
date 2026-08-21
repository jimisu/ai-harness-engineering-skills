# HTTP reliability checklist

## Timeout and cancellation

- Headers and complete body are bounded.
- Each attempt has a fresh timeout controller.
- Caller and timeout signals are composed without mutation.
- Already-aborted callers make zero requests.
- Abort during fetch, body, or backoff stops immediately.
- Timers and listeners are cleaned up.

## Retry policy

- Total attempts and method eligibility are explicit.
- Retryable statuses and errors are allow-listed.
- Authentication, authorization, validation, parser, provenance, and semantic failures are not retried.
- Backoff, cap, jitter, and Retry-After delta/date behavior are deterministic under test.
- Excessive server-directed delay fails closed rather than retrying early.

## Persistence and identity

- Failed attempts do not become trusted snapshots.
- A later-document failure cannot partially promote canonical facts.
- Successful retry creates one evidence identity and no duplicate observation.
- Re-run remains idempotent.
- Timing and attempt metadata do not alter domain identity.

## Evidence

- Tests use injected time, sleep, random, and fetch.
- Tests assert calls and delays without real waiting.
- Existing domain, provenance, and downstream tests pass.
- Protected production paths are byte-for-byte unchanged.
