# Task: 1 - Immediate Safety (Critical)

## Goal

Prevent accidental live trading and ensure the trading loop can be stopped and audited safely.

## Priority

- Level: High (Critical)
- Rationale: Preventing accidental live trades is safety-critical and must be addressed first.

## Owner & Estimated effort

- Owner: Maintainer / dev
- Estimated effort: 4–8 hours

## Roadmap (example)

- Week 1–2 — Short-term goals

  - Make `--dry-run` the default and require `ALLOW_LIVE=true` plus `--live` to place real orders.
  - Add an interactive `Type YES to continue:` confirmation for live mode.
  - Add `--yes` override for CI when `ALLOW_LIVE=true` is set.

- Week 3 — Mid-term goals

  - Add signal handlers and graceful shutdown behavior.
  - Replace silent exception swallowing in critical paths with explicit logging.

- Week 4+ — Longer-term goals
  - Audit and replace silent exception swallowing in critical paths throughout the codebase.

### Quick wins (1–2 days)

- Make `--dry-run` the default and require `ALLOW_LIVE=true` plus `--live` to place real orders.
- Add an interactive `Type YES to continue:` confirmation for live mode.
- Add `--yes` override for CI when `ALLOW_LIVE=true` is set.

### Medium projects (1–2 weeks)

- Replace broad `except:` blocks in order-placement paths with `except Exception as e:` and `logging.exception(...)`.
- Add unit tests for dry-run behavior covering the main loop.

### Longer projects (3–8+ weeks)

- Introduce a controlled scheduler to replace unconditional `while True:` loops and support deterministic iteration
  counts for testing.

## Validation

- `python scalper.py --dry-run` runs without placing orders.
- `ALLOW_LIVE=true python scalper.py --live` prompts for `YES` when executing live actions.
- No critical live code paths use silent `except: pass` (search and audit results).

## Acceptance criteria

- [ ] `--dry-run` is the default behavior in `scalper.py`.
- [ ] Live mode requires both `ALLOW_LIVE=true` and `--live` flag (plus interactive confirmation).
- [ ] Signal handlers and graceful shutdown are implemented for the main loop.
- [ ] Broad `except:` blocks in order submission paths are replaced and logged.

## Notes

- Keep `--dry-run` as the default until live behavior is fully audited and tested.
- Link related tasks: `docs/improvements/11_add_ci_and_smoke_test.md`, `docs/improvements/08_tests_and_validation.md`.

## Implementation hints

- Suggested files to change: `scalper.py`, `broker_api.py`.
- Add tests under `tests/integration/` for dry-run smoke tests and unit tests for error handling.
- Consider adding an environment check early in `scalper.py` that fails fast when `ALLOW_LIVE` is not present for live
  operations.
