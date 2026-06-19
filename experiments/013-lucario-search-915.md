# 013 Lucario Search 915

Date: 2026-06-19

Package: `artifacts/submissions/s013-lucario-search-915.tar.gz`

Kaggle submission: `53827594`

Public score: 600.0

Status: complete

Summary:
- Tested the public Lucario search baseline with bounded forward search enabled.
- Used the original Mega Lucario deck list from that notebook.
- Selected it because the public Code title reported a 915+ result and it
  offered a different high-scoring implementation from the retuned V7 policy.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s013-lucario-search-915`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
