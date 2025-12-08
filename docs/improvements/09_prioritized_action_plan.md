# Task: 9 - Prioritized Action Plan (Medium)

## Goal

Provide a clear sequence of prioritized, time-boxed actions to improve safety, reliability, and maintainability.

## 90‑day roadmap (example)

- Week 1–2 (Safety & gating)

  - Implement `--dry-run` default and `--live` guard (`ALLOW_LIVE`) in
    `scalper.py`.

- Week 3–4 (CI and tests)

  - Add `pre-commit` hooks for formatting and linting.

- Month 2 (Config & secrets)

  - Centralize config with `pydantic.BaseSettings` and add `.env.example`.

- Month 3 (Robustness & observability)

  - Add integration tests and recorded replay fixtures.

### Quick wins (1–2 day tasks)

- Add `--iterations` and `--interval` CLI flags for the main loop.
- Add `--dry-run` default enforcement and document how to enable live mode.

### Medium projects (1–2 weeks)

- Add `pytest` tests for core modules and a dry-run smoke test.
- Add `.pre-commit-config.yaml` and a minimal `ci.yml` workflow.

### Longer projects (3–8 weeks)

- Move broker interactions behind an interface and add a simulated broker
  implementation for testing and replay.
- Add observability (structured logging, metrics) and deployable monitoring.

## Priority

Medium

Estimated effort: 2–6 weeks (incremental)
Owner: Team lead / Maintainer

## Acceptance criteria

- [ ] `scalper.py` defaults to `--dry-run` and requires an explicit `ALLOW_LIVE` to run live.
- [ ] A short-term CI job exists that runs the smoke test and linters on PRs.
- [ ] A documented 90-day plan is present in `docs/improvements/09_prioritized_action_plan.md` with owner and time estimates.

## Validation

- The short-term safety tasks are complete and verified manually.
- PRs implement one change at a time and are validated in CI.

## Notes

- Break larger items into smaller PRs and verify each change in CI.
