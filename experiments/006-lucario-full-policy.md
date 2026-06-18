# 006 Lucario Full Policy

Date: 2026-06-17

Package: `artifacts/submissions/s006-lucario-full-policy.tar.gz`

Kaggle submission: `53784094`

Public score: 870.3

Status: complete

Summary:
- Kept the Mega Lucario deck.
- Replaced the concise tempo policy with a fuller deck-specific public-rule
  implementation.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s006-lucario-full-policy`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 870.3, the best result in the first batch.
