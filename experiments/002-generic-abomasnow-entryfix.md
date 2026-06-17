# 002 Generic Abomasnow Entrypoint Fix

Date: 2026-06-17

Package: `artifacts/submissions/s002-generic-abomasnow-entryfix.tar.gz`

Kaggle submission: `53783691`

Public score: 556.4

Status: complete

Summary:
- Kept the sample Mega Abomasnow deck.
- Moved `agent()` to the final top-level function position.
- Added static entrypoint validation before packaging.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s002-generic-abomasnow-entryfix`

Result:
- Kaggle validation completed.
- Public score was low, so the next experiment should test a stronger public
  deck concept rather than only tuning the generic policy.
