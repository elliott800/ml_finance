# Task: 12 - Add `.env.example` and update `.gitignore` for secrets

## Goal

Create a `.env.example` documenting required environment variables and add `.env` to `.gitignore` so contributors can safely populate secrets locally without risking commits.

## Priority

- Level: High
- Rationale: Preventing accidental credential commits is critical for safety and prevents credential leaks and accidental live trading.

## Owner & Estimated effort

- Owner: maintainer / contributor
- Estimated effort: 15–45 minutes

## Roadmap (example)

- Week 1 — Short-term goals
  - Create `.env.example` with required keys.  
  - Add `.env` to `.gitignore` and ensure `.env` is not tracked.

- Week 2 — Mid-term goals
  - Add documentation snippet to `docs/improvements/07_config_and_secrets.md`.  
  - Add guidance for rotating secrets if leaked.

### Quick wins (1–2 days)

- Create `.env.example` and append `.env` to `.gitignore`.  
- Add a short paragraph to `07_config_and_secrets.md` explaining how to use `.env.example`.

## Validation

- `.env.example` exists in the repo root and lists required variables.  
- `.gitignore` contains `.env` and `git check-ignore -v .env` shows it is ignored.

## Acceptance criteria

- [ ] `.env.example` present at repo root.  
- [ ] `.env` entry added to `.gitignore`.  
- [ ] Documentation updated to instruct contributors how to copy `.env.example` to `.env`.

## Notes

- Do not store real credentials in `requirements` or docs. Use CI provider secret stores for runner secrets.  
- If `.env` was previously committed, rotate any leaked credentials and consider removing the file from history.

## Implementation hints

- Example `.env.example` content (copy/paste):

```text
# Safety: set ALLOW_LIVE only when you understand the risks
ALLOW_LIVE=false
# Broker / API credentials (fill these in locally, not in repo)
API_KEY=
API_SECRET=
# Optional: other config
LOG_LEVEL=INFO
```

- Commands to add `.env` to `.gitignore` and ensure it is not tracked:

```bash
# Add .env to .gitignore
echo ".env" >> .gitignore
# Ensure .env is not in the index
git rm --cached .env || true
```

- Suggested doc text to add to `docs/improvements/07_config_and_secrets.md`:

> Copy `.env.example` to `.env` and fill in local values: `cp .env.example .env`. Never commit `.env` to Git. If a secret is
> accidentally committed, rotate it immediately.

## Implementation checklist

- [ ] Create `.env.example` at repo root.
- [ ] Append `.env` to `.gitignore` if missing.
- [ ] Update `docs/improvements/07_config_and_secrets.md` with usage instructions for `.env`.

---

Start with the quick wins to make local setup explicit and safe for contributors.
