# 007 Strong Start Lucario

Date: 2026-06-18

Package: `artifacts/submissions/s007-strongstart-lucario.tar.gz`

Kaggle submission: `53791680`

Public score: 600.0

Status: complete

Summary:
- Adopted the public Strong Start Crustle-aware Lucario policy.
- Kept the original Mega Lucario deck list.
- Search remained disabled for safety.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s007-strongstart-lucario`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
