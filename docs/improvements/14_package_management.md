# Task: 14 - Beginner-friendly package & environment management

## Goal

Provide clear, beginner-friendly guidance and repository changes to make creating and managing a Python development environment straightforward—optionally recommending `poetry` (recommended) or the built-in `venv`.

## Priority

- Level: Medium
- Rationale: Proper package and environment management reduces onboarding friction and prevents many common dependency issues; it's high-value but straightforward to implement.

## Owner & Estimated effort

- Owner: Maintainer / contributor
- Estimated effort: 4–10 hours (split across quick wins and CI updates)

## Roadmap (example)

- Week 1–2 — Short-term goals
  - Action 1: Add a `pyproject.toml` (Poetry) or document `venv` setup in `README.md`.
  - Action 2: Add short setup snippets for macOS/Linux and Windows.
  - Action 3: Provide commands to create/activate environment and install deps.

- Week 3–4 — Mid-term goals
  - Action 1: Update CI workflows to install dependencies via Poetry or use `requirements.txt` exported from Poetry.
  - Action 2: Migrate `requirements.txt` (if kept) to be exported from Poetry to avoid drift.

- Week 5–8 — Longer-term goals
  - Action 1: Offer optional `dev` and `lock` workflows (e.g., `poetry.lock`) and include reproducible environment guidance in the contributing doc.
  - Action 2: Consider using `pipx` for installable CLI tools and adding `pyproject`-based packaging instructions.

### Quick wins (1–2 days)

- Add a short `Environment setup` section to `README.md` with both `poetry` and `venv` instructions.
- Add `docs/improvements/14_package_management.md` (this task file).
- Add a minimal `pyproject.toml` example or recommend `poetry init`.

### Medium projects (1–2 weeks)

- Add `pyproject.toml` and `poetry.lock` to the repo and export `requirements.txt` for CI (if CI is currently using `requirements.txt`).
- Update CI actions to use Poetry for install (or use exported `requirements.txt`).
- Add a short `CONTRIBUTING` section explaining local development with Poetry and `venv`.

### Longer projects (3–8+ weeks)

- Fully migrate dependency management to Poetry, remove hand-edited `requirements.txt` and keep exports for compatibility.
- Add automated checks that dependencies are up-to-date with the lockfile.

## Validation

- Verify a fresh clone can create a working environment and run tests using the documented method.
- CI passes when installing dependencies using the chosen approach (Poetry path or exported requirements path).
- `poetry.lock` is present and up-to-date (if Poetry is used), or the `requirements.txt` matches an exported lock.

## Acceptance criteria

- [ ] `README.md` contains a clear `Environment setup` section for beginners.
- [ ] Either `pyproject.toml` + `poetry.lock` are added, or the README documents the `venv` flow clearly.
- [ ] CI workflows are updated to install dependencies via the chosen approach.
- [ ] A short example of common commands is added (create env, install, run tests).

## Notes

- This task is intentionally friendly to beginners: it documents both an opinionated, reproducible approach (`poetry`) and the built-in, low-friction approach (`venv`). The maintainer can choose to adopt Poetry fully or keep it as an optional recommendation.
- Related: `docs/improvements/12_add_env_example_and_gitignore.md` and `CONTRIBUTING.md`.

---

Usage: Copy this file when creating a new task and replace the placeholders (`{number}`, `{short title}`, etc.). Keep each task focused and link related follow-up tasks under `Notes`.
