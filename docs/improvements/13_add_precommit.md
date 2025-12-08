# Task: 13 - Add `pre-commit` and basic linters (Black, Ruff, isort)

## Goal

Introduce `pre-commit` hooks to run formatting and basic linting automatically on commits to keep code style consistent
and catch simple issues early.

## Priority

- Level: Medium
- Rationale: Linting and formatting reduce review friction and help contributors follow project conventions, but they
  are not blockers for safety-critical fixes.

## Owner & Estimated effort

- Owner: maintainer / contributor
- Estimated effort: 30–60 minutes

## Roadmap (example)

- Week 1 — Short-term goals

  - Add `.pre-commit-config.yaml` with `black`, `ruff`, and `isort`.
  - Document installation and usage in contributor docs.

- Week 2 — Mid-term goals
  - Run `pre-commit run --all-files` and commit formatting fixes in a single PR.
  - Add `pre-commit` run step to CI workflow.

### Quick wins (1–2 days)

- Add `.pre-commit-config.yaml` and `pre-commit install` instructions.
- Run hooks locally and fix any auto-formatting outputs.

## Validation

- `pre-commit install` succeeds locally and running `pre-commit run --all-files` returns success or shows fixable
  issues.
- A PR includes the `.pre-commit-config.yaml` and instructions in the repo docs.

## Acceptance criteria

- [ ] `.pre-commit-config.yaml` added to repo root.
- [ ] Developer instructions added to `docs/improvements/06_code_quality_ci.md` or similar.
- [ ] CI runs `pre-commit` or `pre-commit` hooks are enforced locally.

## Notes

- Pin `rev` values for reproducible hook versions.
- When enabling `pre-commit` across the repo, run `pre-commit run --all-files` and commit formatting changes in a single
  PR to reduce noise.

## Implementation hints

- Example `.pre-commit-config.yaml` (copy/paste):

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.1.0
    hooks:
      - id: black
        args: [--line-length=88]

  - repo: https://github.com/charliermarsh/ruff
    rev: 0.1.0
    hooks:
      - id: ruff
        args: ["check", "."]

  - repo: https://github.com/pre-commit/mirrors-isort
    rev: v5.12.0
    hooks:
      - id: isort
        args: [--profile=black]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-merge-conflict
```

- Local install steps:

```bash
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## Implementation checklist

- [ ] Add `.pre-commit-config.yaml` to repo root.
- [ ] Document how to install and run pre-commit in `CONTRIBUTING.md` or `docs/improvements/06_code_quality_ci.md`.
- [ ] Run `pre-commit run --all-files` and commit resulting formatting changes in a single PR.

---

This task helps standardize formatting and linting to improve code quality and reviewer experience.
