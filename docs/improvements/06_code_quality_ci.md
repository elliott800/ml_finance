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

## Roadmap (phased)

- Quick wins (1–2 days): Add `.pre-commit-config.yaml`, run `pre-commit run --all-files`, add a minimal `ci.yml` that runs linters and tests.
- Medium (1–2 weeks): Add `mypy` with gradual strictness, enable dependency scanning in CI, cache dependencies in CI.
- Longer (2–4 weeks): Harden CI safety gates around `ALLOW_LIVE` secrets and add matrix testing across Python versions.

## Priority

High

Estimated effort: 8–16 hours (phased)
Owner: Maintainer / DevOps

## Acceptance criteria

- [ ] `.pre-commit-config.yaml` exists in the repo root and is referenced in docs.
- [ ] A CI workflow `ci.yml` runs linters and `pytest` on PRs and pushes to `main`.
- [ ] `mypy` is present with a baseline config and documented plan to tighten rules.
- [ ] Dependency scanning (e.g., `pip-audit`) runs in CI.
- [ ] CI contains checks that prevent accidental enabling of live trading (see validation).

## Validation

- `pre-commit` hooks run locally and fix or flag issues on commit.
- CI runs successfully on a representative PR and blocks merges when checks fail.

## Implementation hints

- Files to add or update:
  - `.pre-commit-config.yaml` (black, isort, ruff or flake8)
  - `pyproject.toml` (formatter settings)
  - `.github/workflows/ci.yml` (runs linters, tests, and dependency scans)
  - `mypy.ini` or `pyproject.toml` mypy section
- Start by enabling auto-fix hooks (black/isort) and a non-blocking `ruff` check; move to blocking once the repo is formatted.
- For CI gating around `ALLOW_LIVE`, add a job step that checks repository secrets or environment variables and fails if `ALLOW_LIVE` is set without approved justification.

## Notes

- Start with conservative rules to avoid overwhelming contributors; tighten
  rules in phases.
