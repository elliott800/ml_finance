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

## Priority

High
Estimated effort: 4–8 hours
Owner: Maintainer / Dev

## Validation

- No secrets present in the repository (ignoring historical commits) and
  `.gitignore` includes credential files and `.env`.

## Notes

- Prefer `pydantic.BaseSettings` for typed configuration with validation.
