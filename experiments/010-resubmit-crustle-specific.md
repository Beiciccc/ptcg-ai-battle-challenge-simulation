# 010 Resubmit Crustle Specific

Date: 2026-06-18

Package: `artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Kaggle submission: `53791955`

Public score: 761.4

Status: complete

Summary:
- Restored the previous Crustle-specific policy and Crustle wall deck.
- Submitted it as a latest-window wall candidate because the original run had
  reached 766.6 after public games.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s010-resubmit-crustle-specific`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 761.4.
