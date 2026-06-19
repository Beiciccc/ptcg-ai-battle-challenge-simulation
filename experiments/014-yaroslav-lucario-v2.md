# 014 Yaroslav Lucario V2

Date: 2026-06-19

Package: `artifacts/submissions/s014-yaroslav-lucario-v2.tar.gz`

Kaggle submission: `53827710`

Public score: 681.2

Status: complete

Summary:
- Tested a public Lucario V2 crustle-aware policy using the original Mega
  Lucario deck list.
- Selected it as the last exploratory run before restoring high-scoring guard
  submissions, because public round-robin notes suggested it was competitive
  against the visible sample of public agents.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s014-yaroslav-lucario-v2`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 681.2.
