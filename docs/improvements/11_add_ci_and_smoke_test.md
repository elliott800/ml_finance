# Task: 11 - Add CI job and minimal dry‑run smoke test

## Goal

Add a minimal GitHub Actions CI job and a single dry‑run smoke test so PRs validate that `scalper.py` starts and completes a single iteration without placing live orders.

## Priority

- Level: High
- Rationale: Automated CI with a dry‑run smoke test prevents regressions and gives maintainers confidence before merging changes that touch trading or startup code.

## Owner & Estimated effort

- Owner: maintainer / contributor
- Estimated effort: 1–3 hours

## Roadmap (example)

- Week 1 — Short-term goals
  - Add `tests/integration/test_dryrun.py` smoke test that runs `scalper.py --dry-run --iterations 1`.
  - Add minimal `.github/workflows/ci.yml` to run tests and basic linters.

- Week 2 — Mid-term goals
  - Improve tests to import `scalper` main function (faster, more reliable).
  - Add caching of dependencies in CI and extend linters run.

- Week 3–4 — Longer-term goals
  - Add more integration tests (config validation, startup guards).
  - Harden CI (dependency scanning, matrix tests for Python versions).

### Quick wins (1–2 days)

- Add the smoke test using `subprocess` (fast to implement).  
- Add `ci.yml` with a single job that installs dependencies and runs `pytest`.

### Medium projects (1–2 weeks)

- Refactor `scalper.py` to expose an importable `main()` so tests can call it directly.  
- Add more unit tests around critical functions (order sizing, position checks).

### Longer projects (3–8+ weeks)

- Add full integration tests against a simulated broker or recorded responses.  
- Add security scans and dependency auditing into CI.

## Validation

- CI run on PRs completes and the smoke test passes.  
- `pytest` locally passes for the new smoke test (`pytest tests/integration/test_dryrun.py`).

## Acceptance criteria

- [ ] `tests/integration/test_dryrun.py` exists and is runnable locally.  
- [ ] `.github/workflows/ci.yml` exists and triggers on `push`/`pull_request`.  
- [ ] CI job runs tests and exits with status 0 on the main branch (or PR against main).

## Notes

- The smoke test must use `--dry-run` and never enable live trading.  
- If startup requires credentials, the test should either set harmless env vars or use a mode that avoids external calls.
- Link to related tasks: `docs/improvements/08_tests_and_validation.md` and `docs/improvements/01_immediate_safety.md`.

## Implementation hints

- Files to add: `tests/integration/test_dryrun.py`, `.github/workflows/ci.yml`.  
- Commands (local):
  - `python -m venv .venv && source .venv/bin/activate`
  - `pip install -U pip && pip install pytest`
  - `pytest -q tests/integration/test_dryrun.py`

- Minimal smoke test snippet (subprocess approach):

```python
# tests/integration/test_dryrun.py
import subprocess, sys

def test_scalper_dryrun_smoke():
    cmd = [sys.executable, "scalper.py", "--dry-run", "--iterations", "1"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
```

- Minimal CI example: create `.github/workflows/ci.yml` that sets up Python 3.10, installs deps, and runs `pytest`.

---

Usage: Copy this task into the `docs/improvements/` folder and assign an owner. Start with the quick wins to get CI validation fast.