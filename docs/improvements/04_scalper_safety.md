# Task: 4 - Scalper Safety Improvements (High)

## Goal

Harden the trading loop and add operational controls to reduce the risk of runaway trades.

## Priority

- Level: High
- Rationale: Preventing runaway trades is essential to protect capital.

## Owner & Estimated effort

- Owner: Trading engineer / maintainer
- Estimated effort: 8–16 hours

## Roadmap (example)

- Week 1 — Short-term goals

  - Add CLI arguments: `--dry-run`, `--live`, `--config PATH`, `--log-level LEVEL`, `--max-trades N`, and
    `--iterations N`.
  - Enforce live guard requiring `ALLOW_LIVE=true` and `--live`.

- Week 2 — Mid-term goals

  - Add logging with rotation and JSON formatting.
  - Implement a rate-limiter for order submissions.

- Week 3–4 — Longer-term goals
  - Add pre-trade checks (balance, positions, concentration limits).
  - Add monitoring hooks for metrics and alerts.

### Quick wins (1–2 days)

- Add `--max-trades` and `--iterations` flags and ensure they limit actions in `--dry-run` mode.
- Add live guard enforcement with clear error messaging.

### Medium projects (1–2 weeks)

- Implement a token-bucket or leaky-bucket limiter for submissions.
- Enforce client-side stop-loss placement where supported.

### Longer projects (3–8+ weeks)

- Add observability hooks (Prometheus, webhooks) and integrate with monitoring.

## Validation

- `--max-trades` and `--iterations` limit actions in `--dry-run` mode and the throttler prevents rapid submissions
  during tests.

## Acceptance criteria

- [ ] CLI flags added and documented.
- [ ] Live guard enforced and tested.
- [ ] Throttler implemented and tested in dry-run mode.
- [ ] Pre-trade checks prevent obviously risky orders.

## Notes

- Ensure `scalper.py` checks broker API mode before any order submission.

## Implementation hints

- Files to change: `scalper.py`, `broker_api.py`, add tests under `tests/` and CI workflow updates.
- Concrete steps:
  - Add a CLI parser (e.g., `argparse`) in `scalper.py` with flags: `--dry-run`, `--live`, `--config`, `--log-level`,
    `--max-trades`, `--iterations`.
  - Enforce live guard early: check `ALLOW_LIVE` env var and `--live` flag, prompt for confirmation and support `--yes`
    for automated CI.
  - Implement a throttler (token-bucket or leaky-bucket) as a small helper module and integrate it around order
    submissions.
  - Add pre-trade checks: fetch account balance from `broker_api`, verify available margin, and check
    concentration/position limits before placing orders.
  - Add JSON structured logging and log rotation (use `logging.handlers.RotatingFileHandler` or
    `TimedRotatingFileHandler`).
  - Add unit and integration tests for the throttler, CLI flags, and pre-trade checks (use the offline broker for
    deterministic tests).
- Libraries/techniques to consider: `ratelimit`, simple token-bucket implementation, `argparse`/`click`, `logging` with
  structured formatters.
