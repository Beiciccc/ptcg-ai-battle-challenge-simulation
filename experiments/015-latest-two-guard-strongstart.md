# 015 Latest Two Guard Strong Start

Date: 2026-06-19

Package: `artifacts/submissions/s015-latest-two-guard-strongstart.tar.gz`

Kaggle submission: `53827828`

Public score: 548.0

Status: complete

Summary:
- Restored the retuned Strong Start policy and deck from experiment 011.
- Submitted it as the first latest-two guard after the exploratory 2026-06-19
  runs underperformed.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s015-latest-two-guard-strongstart`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 548.0.
