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

## Priority

High
Estimated effort: 8–16 hours
Owner: Maintainer / QA

## Validation

- `pytest` runs locally and in CI; unit tests cover core logic and integration
  smoke tests validate the dry-run loop.

## Notes

- Start with a focused, high-value test suite (critical math functions and the
  dry-run main loop) and expand coverage iteratively.
