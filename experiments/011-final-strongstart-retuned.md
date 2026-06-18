# 011 Final Strong Start Retuned

Date: 2026-06-18

Package: `artifacts/submissions/s011-final-strongstart-retuned.tar.gz`

Kaggle submission: `53792068`

Public score: 600.0

Status: complete

Summary:
- Restored the retuned Strong Start policy and deck from experiment 008.
- Selected this version because experiment 008 had refreshed to 799.5, the
  best score from the second-day batch at submission time.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s011-final-strongstart-retuned`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
