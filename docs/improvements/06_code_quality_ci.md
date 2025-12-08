# Task: 6 - Code Quality & CI (High)

## Goal

Establish automated checks that ensure consistent code quality, formatting,
static analysis, and safe CI gating before merging or deploying.

## Tasks

- Formatting & style

  - Adopt `black` for code formatting and `isort` for import sorting. Add or
    update `pyproject.toml` to pin formatter settings.

- Static typing

  - Introduce `mypy` with a conservative configuration (start with
    `--ignore-missing-imports`) and tighten over time.

- Tests in CI

  - Create a GitHub Actions workflow `ci.yml` to run tests and linters on PRs
    and pushes to `main`.

- Security & dependency scanning

  - Use `pip-audit` or `safety` in CI to scan for known vulnerabilities.

- CI safety gates for live operations

  - Add CI checks to ensure `ALLOW_LIVE` is not set in repository secrets without
    justification and to block merges that could enable live trading by default.

- Developer ergonomics

  - Add `pre-commit` config that runs formatting and linters locally.

## Priority

High
Estimated effort: 8–16 hours (phased)
Owner: Maintainer / DevOps

## Validation

- `pre-commit` hooks run locally and fix or flag issues on commit.

## Notes

- Start with conservative rules to avoid overwhelming contributors; tighten
  rules in phases.
