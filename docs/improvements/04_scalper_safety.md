# Task: 4 - Scalper Safety Improvements (High)

## Goal

Harden the trading loop and add operational controls to reduce the risk of
runaway trades.

## Tasks

- CLI arguments

  - Add `--dry-run`, `--live`, `--config PATH`, `--log-level LEVEL`,
    `--max-trades N`, and `--iterations N`.

- Enforce live guard

  - Require `ALLOW_LIVE=true` in the environment **and** the `--live` flag to
    execute real orders; otherwise exit with a clear error.

- Logging & rotation

  - Use `logging` with JSON formatting (e.g., `python-json-logger`) and a
    `RotatingFileHandler`.

- Rate-limiting and throttling

  - Implement a token-bucket or leaky-bucket limiter for order submissions.

- Pre-trade checks

  - Before submitting an order, check available balance, current positions, and
    position concentration / risk limits.

- Fail-safe order enforcement

  - Enforce client-side stop-loss placement where supported; require a
    `stop_loss` parameter when submitting orders.

- Monitoring hooks

  - Add hooks for metrics and alerts (e.g., Prometheus / Pushgateway or
    webhook notifications).

## Priority

High
Estimated effort: 8–16 hours
Owner: Trading engineer / maintainer

## Validation

- `--max-trades` and `--iterations` limit actions in `--dry-run` mode and the
  throttler prevents rapid submissions during tests.

## Notes

- `scalper.py` contains multiple calls into the broker API — ensure broker API
  mode is checked prior to any order submission.
