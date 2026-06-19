# 016 Latest Two Guard Lucario Full

Date: 2026-06-19

Package: `artifacts/submissions/s016-latest-two-guard-lucario-full.tar.gz`

Kaggle submission: `53827932`

Public score: 600.0

Status: complete

Summary:
- Restored the full Lucario policy and original Mega Lucario deck from
  experiment 009.
- Submitted it as the final latest-two guard because experiment 009 remained
  the best observed result at 893.0.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s016-latest-two-guard-lucario-full`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
