# 009 Resubmit Lucario Full

Date: 2026-06-18

Package: `artifacts/submissions/s009-resubmit-lucario-full.tar.gz`

Kaggle submission: `53791858`

Public score: 600.0

Status: complete

Summary:
- Restored the previous full Lucario policy and original Mega Lucario deck.
- Submitted it as a safety baseline because the prior matching strategy had
  reached 870.3 after public games.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s009-resubmit-lucario-full`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
