# 017 Maktha 1084 Baseline

Date: 2026-06-20

Package: `artifacts/submissions/s017-maktha-1084-baseline.tar.gz`

Kaggle submission: `53864132`

Public score: 695.6

Status: complete

Summary:
- Tested the public 1084.5 baseline candidate from the latest Code list.
- Used its Mega Lucario policy and deck extraction from the public notebook.
- Selected it as the first 2026-06-20 exploratory run before restoring
  high-scoring latest-two guard submissions.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s017-maktha-1084-baseline`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 695.6.
