# Task: 3 - Broker API Hardening (High)

## Goal

Make broker API interactions explicit, validated, resilient, and testable.

## Priority

- Level: High
- Rationale: Resilient broker interactions are necessary to avoid unexpected behavior and losses.

## Owner & Estimated effort

- Owner: Backend developer / maintainer
- Estimated effort: 8–12 hours

## Roadmap (example)

- Week 1 — Short-term goals
  - Audit `broker_api.py` for `except:` usages and replace with specific handlers.
  - Add input validation for instruments, sizes, and prices.

- Week 2 — Mid-term goals
  - Add explicit online/offline modes and a retry helper with exponential backoff.
  - Add structured logging for requests/responses.

- Week 3–4 — Longer-term goals
  - Add unit tests that simulate network failures and verify retry/backoff behavior.

### Quick wins (1–2 days)

- Replace broad exception handlers in `broker_api.py`.
- Add a `logger = logging.getLogger('broker_api')` and ensure key events are logged.

### Medium projects (1–2 weeks)

- Implement a retry helper/decorator with exponential backoff and jitter.
- Add validation helpers for API inputs.

### Longer projects (3–8+ weeks)

- Add integration tests mocking broker responses and add an `offline` simulated broker implementation for CI.

## Validation

- Unit tests for `broker_api` run and pass; tests include simulated network failures to confirm retry behavior.

## Acceptance criteria

- [ ] Broad `except:` handlers are replaced and critical failures are logged.
- [ ] Retry/backoff helper exists and is applied to network calls.
- [ ] Input validation prevents obviously invalid orders from being sent.
- [ ] Structured logger outputs contextual fields for broker calls.

## Notes

- There are `oandapyV20` imports in `broker_api.py`; tests should mock or isolate those dependencies.

## Implementation hints

- Files to change: `broker_api.py`, tests under `tests/unit/` and `tests/integration/`.
- Consider `responses` or `requests-mock` for HTTP-based brokers, or use test doubles for SDKs like `oandapyV20`.
