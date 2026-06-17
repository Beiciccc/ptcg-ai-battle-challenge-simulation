# 004 Crustle Specific

Date: 2026-06-17

Package: `artifacts/submissions/s004-crustle-specific.tar.gz`

Kaggle submission: `53783875`

Public score: 600.0

Status: complete

Summary:
- Kept the Crustle wall deck.
- Replaced the generic policy with a short Crustle-specific sequencing policy.
- Prioritized setup actions before attack and conditionally used healing cards.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s004-crustle-specific`

Result:
- Kaggle validation completed.
- Initial public score stayed at 600.0, so the next experiment should test a
  different proven deck family.
