# Task: 5 - Repo Structure & Documentation (Medium)

## Goal

Separate research/educational artifacts from production code, and document safe development workflows.

## Priority

- Level: Medium
- Rationale: Clear separation improves maintainability and reduces accidental misuse of research code in production.

## Owner & Estimated effort

- Owner: Maintainer / docs contributor
- Estimated effort: 2–4 hours

## Roadmap (example)

- Week 1 — Short-term goals
  - Create a `notes/` or `recipes/` directory at the repo root and move notebooks, ad-hoc scripts, and experimental files there.
  - Ensure `README.md` contains a clear safety warning and links to `docs/improvements.md`.

- Week 2 — Mid-term goals
  - Update `CONTRIBUTING.md` with instructions for proposing changes, running tests, and PR expectations for live-trading code.
  - Keep `docs/improvements.md` as the canonical index for safety-related tasks.

### Quick wins (1–2 days)

- Move research notebooks into `notes/` or `recipes/` and add a README to explain their purpose.
- Add safety warning to root `README.md` linking to `docs/improvements/`.

### Medium projects (1–2 weeks)

- Clean up root directory to clearly separate library code, CLI/script entry points, and research artifacts.
- Add a docs index and link it from `README.md`.

## Validation

- `README.md` exists at repo root and contains the safety warning and links to documentation.
- Research artifacts are moved to a dedicated folder without breaking imports.

## Acceptance criteria

- [ ] Research notebooks and experiments are in a dedicated `notes/` or `recipes/` directory.
- [ ] Root `README.md` contains safety warning and links to `docs/improvements.md`.
- [ ] `CONTRIBUTING.md` updated with development workflow notes.

## Notes

- Moving files should be non-destructive; do not delete originals without team consent.

## Implementation hints

- Suggested files to change: `README.md`, `CONTRIBUTING.md`, add `notes/` folder.
- Update imports or CI paths if any moved scripts are used by tests or actions.
