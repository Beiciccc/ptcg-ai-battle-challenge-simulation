# 000 Baseline

Date: 2026-06-17

Package: `artifacts/submissions/baseline.zip`

Status: prepared, not submitted

Summary:
- Uses the sample 60-card deck.
- Uses a deterministic fallback selection policy.
- Includes deck validation and packaging checks.

Validation:
- `python tools/check_deck.py submission/deck.csv`
- `python tools/package_submission.py --name baseline`
- `pytest -q`
