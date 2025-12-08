# Task: 1 - Immediate Safety (Critical)

## Goal

Prevent accidental live trading and ensure the trading loop can be stopped and
audited safely.

## 90‑day roadmap (example)

- Week 1–2: Implement dry-run default and live guard, add interactive
  confirmation.
- Week 3: Add signal handlers and graceful shutdown behavior.
- Week 4: Audit and replace silent exception swallowing in critical paths.

### Quick wins (1–2 day tasks)

- Make `--dry-run` the default and require `ALLOW_LIVE=true` plus `--live` to
  place real orders.
- Add an interactive `Type YES to continue:` confirmation for live mode.
- Add `--yes` override for CI when `ALLOW_LIVE=true` is set.

### Medium projects (1–2 weeks)

- Replace broad `except:` blocks in order-placement paths with
  `except Exception as e:` and `logging.exception(...)`.
- Add unit tests for dry-run behavior covering the main loop.

### Longer projects (3–8 weeks)

- Introduce a controlled scheduler to replace unconditional `while True:` loops
  and support deterministic iteration counts for testing.

## Priority

Critical  Estimated effort: 4–8 hours  Owner: Maintainer / dev

## Validation

- `python scalper.py --dry-run` runs without placing orders.
- `ALLOW_LIVE=true python scalper.py --live` prompts for `YES`.
- `rg "except:\s*pass" || true` returns no matches in live code paths.

## Notes

- Keep `--dry-run` as the default until live behavior is fully audited and
  tested.
