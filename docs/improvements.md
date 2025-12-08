# Improvements and Safety Recommendations

This document summarizes prioritized, concrete recommendations for the
repository. It focuses on immediate safety for live trading, dependency and
packaging fixes, hardening of the broker API and trading loop, repository
organization, and suggested next steps.

## Glossary

- `--dry-run`: a command-line flag that runs the trading logic without placing
  real orders.

### Safety Note

- The project defaults to `--dry-run`. Live trading must be explicitly enabled
  with `ALLOW_LIVE=true` and `--live`.

## Checklist (Top Priority)

- [ ] Implement the `--dry-run` + `ALLOW_LIVE` guard in `scalper.py` (High
  priority)

## Task: 1 - Immediate Safety (Critical)

- Add an explicit "dry-run" mode and require an explicit environment variable to
  enable live trading.

## Task: 2 - Dependency Cleanup

- Pin package versions in `requirements.txt` to reproducible versions.

## Task: 3 - broker_api.py Hardening

- Replace broad `except` blocks with targeted exceptions and add structured
  logging for errors.

## Task: 4 - scalper.py Safety Improvements

- Add CLI args: `--dry-run`, `--config`, `--log-level`, and `--max-trades`.

## Task: 5 - Repo Structure & Documentation

- Move example/educational snippets into a `notes/` or `recipes/` folder and
  mark them as non-production examples.

## Task: 6 - Code Quality & CI

- Add basic CI that runs linters (e.g., `flake8` or `ruff`) and tests on
  push/PR.

## Task: 7 - Config & Secrets

- Move configuration out of code into environment variables or a config file
  (YAML/JSON) that is excluded from VCS.

## Task: 8 - Tests & Validation

- Add unit tests for critical logic: order sizing, currency conversion, signal
  filtering, and backtest-like dry-run trade execution.

## Task: 9 - Suggested Prioritized Action Plan

1. Add `--dry-run` and require `ALLOW_LIVE` + `--live` to place orders
   (Critical).

## Task: 10 - Notes and Rationale

- Safety-first: the trading loop and broker API contain patterns (silent
  fallbacks, broad exceptions, infinite loops) that are acceptable for research
  but dangerous in production.

---

## Detailed Plans Index

The authoritative, per-topic detailed plans live in `docs/improvements/` and
should be used for implementation and assignment. Use this index as the single
glanceable entry; each linked file contains the expanded tasks, validation
steps, and owner suggestions.

- [Immediate safety](docs/improvements/01_immediate_safety.md) —
  `docs/improvements/01_immediate_safety.md:1`

- [Add CI & smoke test](docs/improvements/11_add_ci_and_smoke_test.md) —
  `docs/improvements/11_add_ci_and_smoke_test.md:1`

- [Add .env.example & ignore `.env`](docs/improvements/12_add_env_example_and_gitignore.md) —
  `docs/improvements/12_add_env_example_and_gitignore.md:1`

- [Add pre-commit hooks](docs/improvements/13_add_precommit.md) —
  `docs/improvements/13_add_precommit.md:1`

The top-level checklist is below for quick tracking; consult the per-topic files
for implementation details.

## Checklist

- [ ] Implement the `--dry-run` + `ALLOW_LIVE` guard in `scalper.py` (High
  priority)

Tell me which of the above you want next, and I will proceed.
