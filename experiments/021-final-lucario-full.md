# 021 Final Lucario Full

Date: 2026-06-20

Package: `artifacts/submissions/s021-final-lucario-full.tar.gz`

Kaggle submission: `53864476`

Public score: 807.4

Status: complete

Summary:
- Restored the full Lucario policy and original Mega Lucario deck from
  experiment 009.
- Submitted it as the final latest-two guard slot for the 2026-06-20 batch.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s021-final-lucario-full`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 807.4.
