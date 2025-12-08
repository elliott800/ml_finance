# Task: 7 - Configuration & Secrets (High)

## Goal

Centralize configuration, keep secrets out of source control, and provide safe
defaults for local development and CI.

## Tasks

- Configuration structure

  - Introduce `app/settings.py` or `src/config.py` that defines configuration
    objects and sensible defaults (prefer `pydantic.BaseSettings`).

- Secrets management

  - Do NOT store credentials in the repo. Add examples in `docs/` for how to
    provide credentials locally (e.g., `.env` and environment variables) and
    document secure workflows.

- Config validation & schema

  - Validate critical values at startup (non-empty API keys, numeric timeouts
    within acceptable ranges) and ensure `ALLOW_LIVE` is managed explicitly.

- File permissions and safe defaults

  - If local credential files are used, ensure the code checks file permissions
    and warns if they are overly permissive (e.g., 0644).

- Rotation and expiration workflow

  - Document key rotation and secrets expiration best practices in `docs/`.

## Roadmap (phased)

- Quick wins (1–2 days): Add `.env.example`, add `.env` to `.gitignore`, and document copying `.env.example` to `.env`.
- Medium (1–2 weeks): Implement `pydantic` settings object and add validation at startup, add checks for file permissions.
- Longer (2–4 weeks): Integrate secrets with a secrets manager in CI and document rotation policies.

## Priority

High

Estimated effort: 4–8 hours
Owner: Maintainer / Dev

## Acceptance criteria

- [ ] `.env.example` exists and documents required variables.
- [ ] `.env` is listed in `.gitignore` and not tracked in the index.
- [ ] There is a typed settings object (e.g., `pydantic.BaseSettings`) with validation for critical values.
- [ ] `scalper.py` or startup path validates critical config and fails fast with clear errors.

## Validation

- No secrets present in the repository (ignoring historical commits) and
  `.gitignore` includes credential files and `.env`.
- Running the app with missing critical settings returns a clear, non-zero exit code and helpful error message.

## Implementation hints

- Files to add/update:
  - `app/settings.py` or `src/config.py` (implement `pydantic.BaseSettings`)
  - `.env.example` at repo root
  - `.gitignore` (append `.env` if missing)
- Concrete steps:
  - Implement a `Settings` class using `pydantic.BaseSettings` that reads from `.env` and environment variables and validates required fields.
  - Add `.env.example` with keys like `ALLOW_LIVE`, `API_KEY`, `API_SECRET`, and `LOG_LEVEL` and append `.env` to `.gitignore`.
  - Add startup validation in `scalper.py` to fail fast with clear error messages when critical settings are missing.
  - Check file permissions for any local credential files and warn when too permissive (e.g., world readable).
  - Document secret rotation and CI secret storage recommendations in `docs/improvements/07_config_and_secrets.md`.
- Example `pydantic` settings snippet:

  ```python
  from pydantic import BaseSettings, Field

  class Settings(BaseSettings):
      api_key: str = Field(..., env="API_KEY")
      api_secret: str = Field(..., env="API_SECRET")
      allow_live: bool = Field(False, env="ALLOW_LIVE")

      class Config:
          env_file = ".env"
  ```

- When validating file permissions, check `os.stat(path).st_mode` and warn if world-readable.

## Notes

- Prefer `pydantic.BaseSettings` for typed configuration with validation.
