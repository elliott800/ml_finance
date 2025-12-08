# ML Finance (Beginner Guide)

This repository collects useful Python finance/algorithmic trading utilities,
reference code, and documentation. It is a research-first project — do not run
any code in live trading mode without following the safety instructions in the
`docs/` folder.

## Purpose

- Collect well-known finance and ML routines in one place.

## Quick Start (for beginners)

1. Clone the repo:

   ```bash
   git clone <repo-url>
   cd ml_finance
   ```

2. Create a Python virtual environment and activate it:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies (the repo may not have pinned versions yet; check
   `requirements.txt`):

   ```bash
   pip install -r requirements.txt
   ```

4. Read the docs first:

    - `docs/improvements.md` — high-level summary + top checklist (start here)

5. Run scripts in dry-run / offline mode only. The project recommends adding and
   using a `--dry-run` flag. Do not enable live trading without team approval
   and safety checks.

## Recommended Reading (select a few to start)

- See `docs/reading_recommendations.md` for a curated table of suggested books
  and categories.

(These books are advanced; pick one and focus on the practical chapters.)

## Contributing & Safety

- Always open a PR for code changes. Small, focused PRs are easier to review.

## Notes

- This repo currently emphasizes documentation and planning; several code files
  may be research snippets that require cleanup before production use.

If you want, I can also convert `readme.txt` into a `README.md` in-place (done)
and improve the per-topic docs for beginners (wording, examples, step-by-step
commands).
