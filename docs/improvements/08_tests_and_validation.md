# Task: 8 - Tests & Validation (High)

## Goal

Provide automated tests and validation harnesses to ensure correctness of core
logic and to prevent regressions.

## Tasks

- Testing strategy

  - Use `pytest` as the test runner. Organize tests under `tests/` with clear
    directories such as `tests/unit/` and `tests/integration/`.

- Unit tests

  - Add unit tests for pure functions and local logic (indicators, sizing, and
    margin calculations). Use fixtures to share common setup.

- Integration / smoke tests (dry-run)

  - Add an integration smoke test that runs the main loop in `--dry-run` mode
    against mocked broker endpoints to confirm end-to-end behavior.

- Property and fuzz tests

  - For critical numeric functions, add property-based tests using
    `hypothesis` to detect edge cases.

- Validation harnesses

  - Add `tests/fixtures` that provide sample CSV price feeds (use
    `csvs/assets/*` already in the repo) and expected outputs for replay
    testing.

- CI integration

  - Ensure tests run in CI and that failing tests block merges.

## Roadmap (phased)

- Quick wins (1–2 days): Add `tests/` skeleton, a single unit test for a pure function, and the dry-run smoke test that executes one iteration.
- Medium (1–2 weeks): Add fixtures for CSV replay tests, integrate `hypothesis` for property tests for critical math, and ensure tests run in CI.
- Longer (2–4 weeks): Expand integration tests against a simulated broker and add coverage reporting.

## Priority

High

Estimated effort: 8–16 hours
Owner: Maintainer / QA

## Acceptance criteria

- [ ] `tests/` directory exists with `unit/` and `integration/` subdirs.
- [ ] At least one unit test for a core pure function exists and passes.
- [ ] `tests/integration/test_dryrun.py` exists and passes locally with `--dry-run`.
- [ ] CI runs tests and fails the build on test failures.

## Validation

- `pytest` runs locally and in CI; unit tests cover core logic and integration
  smoke tests validate the dry-run loop.

## Implementation hints

- Use `csvs/assets/*` sample CSVs for replay tests. Add fixtures under `tests/fixtures/` that load these CSVs and provide deterministic data to the dry-run loop.
- Prefer subprocess-based smoke tests for initial quick wins (see `docs/improvements/11_add_ci_and_smoke_test.md`), then refactor `scalper.py` to expose an importable `main()` for faster, in-process tests.
- Example test file for smoke test (subprocess approach):

  ```python
  # tests/integration/test_dryrun.py
  import subprocess, sys

  def test_scalper_dryrun_smoke():
      cmd = [sys.executable, "scalper.py", "--dry-run", "--iterations", "1"]
      result = subprocess.run(cmd, capture_output=True, text=True)
      assert result.returncode == 0, result.stderr
  ```

- Consider using `pytest` markers to separate quick smoke tests from longer integration tests that rely on heavier fixtures.

## Notes

- Start with a focused, high-value test suite (critical math functions and the
  dry-run main loop) and expand coverage iteratively.
