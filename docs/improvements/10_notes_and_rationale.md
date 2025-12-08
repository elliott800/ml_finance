# Task: 10 - Notes & Rationale (Low)

## Goal

Capture the rationale behind proposed changes, tradeoffs considered, and useful
links for future contributors.

## Rationale

- Safety-first default

  - Defaulting to `--dry-run` minimizes the risk of accidental live trades and
    matches a cautious operational posture for this project.

- Incremental improvements

  - Small, verifiable changes (linting, config validation, dry-run smoke tests)
    reduce cognitive load and make reviews easier.

- Layered configuration

  - Keep runtime overrides, local dev settings, and CI configuration clearly
    separated to reduce accidental exposure of secrets or enabling live modes.

## Tradeoffs considered

- `pydantic` vs `dynaconf`

  - `pydantic` provides typed settings and validation which reduces runtime
    surprises; `dynaconf` offers more features for complex deployments.

- Introducing strong typing (`mypy`) early vs later

  - Start with conservative `mypy` settings to reduce friction; gradually
    tighten checks as the codebase stabilizes.

- Test coverage thresholds

  - Aim for high-value coverage (critical math and the dry-run loop) rather
    than arbitrary percentage targets initially.

## Useful links

- `pydantic` BaseSettings: https://docs.pydantic.dev/latest/usage/settings/

## Notes for reviewers

- Prefer small PRs that change one concern at a time (safety, config, CI,
  tests).
