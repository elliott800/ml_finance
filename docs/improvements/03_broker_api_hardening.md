# Task: 3 - Broker API Hardening (High)

## Goal

Make broker API interactions explicit, validated, resilient, and testable.

## Tasks

- Replace broad exception handlers

  - Audit `broker_api.py` for `except:` usages and replace with specific
    handlers such as `except <SpecificException> as e:` or `except Exception as
    e:` where appropriate.

- Add explicit online/offline modes

  - Add a `mode` parameter or configuration to choose `online` or `offline`
    behavior (used by `scalper.py` and tests).

- Input validation

  - Validate instruments (non-empty strings, known formats), sizes (positive
    numbers, not NaN), and prices (sane ranges).

- Centralize retries & backoff

  - Implement a retry helper or decorator that performs exponential backoff
    with jitter and apply it to network calls.

- Structured logging

  - Add `logger = logging.getLogger('broker_api')` and ensure requests,
    responses, and errors are logged with contextual fields.

- Add unit tests

  - Add tests that simulate network failures and verify retry/backoff behavior.

## Priority

High
Estimated effort: 8–12 hours
Owner: Backend developer / maintainer

## Validation

- Unit tests for `broker_api` run and pass; tests include simulated network
  failures to confirm retry behavior.

## Notes

- There are several `oandapyV20` imports in `broker_api.py` that currently
  cause diagnostics warnings in the repo; keep that in mind when adding tests.
