# Task: 2 - Dependency Cleanup

## Goal

Make dependency management reproducible and remove typos and obsolete packages.

## 90‑day roadmap (example)

- Week 1: Audit `requirements.txt` and fix typos/incorrect names.
- Week 2: Pin stable versions and create `requirements-legacy.txt` for
  research-only deps.
- Week 3–4: Add `pyproject.toml` and optionally a lockfile workflow.

### Quick wins (1–2 day tasks)

- Fix obvious package name typos in `requirements.txt`.
- Add a short README note describing `requirements-legacy.txt` usage.

### Medium projects (1–2 weeks)

- Pin versions for all production dependencies and verify installs in a clean
  virtualenv.
- Document the dependency update policy (minor vs major, testing before bump).

### Longer projects (3–8 weeks)

- Introduce a reproducible lockfile (`poetry.lock` or `requirements.txt` generated
  by `pip-tools`) and CI checks to ensure dependency installations succeed.

## Priority

High  Estimated effort: 1–3 hours  Owner: Maintainer / dev

## Validation

- Fresh virtualenv install of pinned `requirements.txt` completes successfully.
- `requirements-legacy.txt` contains explanatory comments for optional or legacy
  packages.

## Notes

- Avoid bumping everything at once; prefer small, tested upgrades.
