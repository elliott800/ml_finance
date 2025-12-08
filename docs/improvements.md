# Improvements and Safety Recommendations

This document is the single, glanceable index of prioritized, concrete recommendations for the repository. It focuses on immediate safety for live trading, dependency and packaging fixes, broker API and trading-loop hardening, repository organization, and suggested next steps. Detailed per-topic implementation plans live under `docs/improvements/` (linked below).

## Glossary

- `--dry-run`: CLI flag that runs trading logic without placing real orders.
- `ALLOW_LIVE`: environment variable required to enable live trading when `--live` is passed.

## Safety note

- The project defaults to dry-run. Live trading must be explicitly enabled by both setting `ALLOW_LIVE=true` and passing `--live`.
- Always run `python scalper.py --dry-run` and verify logs before any live run.

## Top-priority checklist (do these first)

- [ ] Add a strict dry-run guard in `scalper.py`: require both `ALLOW_LIVE=true` and `--live` to place orders (Critical).
- [ ] Add CLI flags to `scalper.py`: `--dry-run`, `--config`, `--log-level`, `--max-trades`.
- [ ] Harden `broker_api.py`: remove broad `except:` blocks, raise or handle targeted exceptions, add structured logging and retry/backoff where appropriate.

## Prioritized tasks (summary)

1. Immediate Safety (Critical)
   - Implement explicit dry-run + live gating (see top checklist).
   - Add a smoke test that runs a full dry-run loop verifying no orders are placed.
2. Dependency & packaging
   - Pin versions in `requirements.txt` and add `constraints.txt` if needed for reproducible installs.
3. Broker API hardening
   - Replace broad catches with targeted exceptions, add timeouts, input validation, and structured logs.
4. Scalper safety improvements
   - Add CLI, config file support, limits (`--max-trades`), and graceful shutdown handling.
5. Repo structure & docs
   - Move educational/example snippets to `notes/` or `recipes/` and mark them non-production.
6. Code quality & CI
   - Add CI that runs linters (`ruff`/`flake8`) and tests on push/PR; add pre-commit hooks.
7. Config & secrets
   - Move secrets out of code. Provide `.env.example` and update `.gitignore` to exclude runtime secret files.
8. Tests & validation
   - Add unit tests for order sizing, currency conversion, signal filtering, and dry-run trade execution.

## Detailed plans index (authoritative)

- Immediate safety — `docs/improvements/01_immediate_safety.md:1`
- Dependency cleanup — `docs/improvements/02_dependency_cleanup.md:1`
- Broker API hardening — `docs/improvements/03_broker_api_hardening.md:1`
- Scalper safety improvements — `docs/improvements/04_scalper_safety.md:1`
- Repo structure & docs — `docs/improvements/05_repo_structure_docs.md:1`
- Code quality & CI — `docs/improvements/06_code_quality_ci.md:1`
- Config & secrets — `docs/improvements/07_config_and_secrets.md:1`
- Tests & validation — `docs/improvements/08_tests_and_validation.md:1`
- Prioritized action plan — `docs/improvements/09_prioritized_action_plan.md:1`
- Notes & rationale — `docs/improvements/10_notes_and_rationale.md:1`
- Add CI & smoke test — `docs/improvements/11_add_ci_and_smoke_test.md:1`
- Add .env example & ignore `.env` — `docs/improvements/12_add_env_example_and_gitignore.md:1`
- Add pre-commit hooks — `docs/improvements/13_add_precommit.md:1`
- Package management — `docs/improvements/14_package_management.md:1`

## Next steps (recommended immediate actions)

- Implement the dry-run guard and smoke dry-run test first (owner: repo maintainer).
- Harden `broker_api.py` exception handling and add structured logging (owner: backend/broker lead).
- Pin `requirements.txt` and validate reproducible installs in a fresh venv (owner: devops/maintainer).
- Add a minimal CI job that runs a lint and the smoke dry-run (owner: maintainer / CI owner).
