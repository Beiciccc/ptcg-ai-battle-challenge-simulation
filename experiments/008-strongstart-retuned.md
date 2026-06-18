# 008 Strong Start Retuned

Date: 2026-06-18

Package: `artifacts/submissions/s008-strongstart-retuned.tar.gz`

Kaggle submission: `53791767`

Public score: 600.0

Status: complete

Summary:
- Kept the Strong Start Crustle-aware Lucario policy.
- Switched from the original Lucario list to the retuned anti-Crustle deck.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s008-strongstart-retuned`

Result:
- Kaggle validation completed.
- Initial public score was 600.0. The retuned deck should be treated cautiously.
