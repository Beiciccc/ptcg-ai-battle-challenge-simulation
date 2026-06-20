# 020 Reroll Crustle Specific

Date: 2026-06-20

Package: `artifacts/submissions/s020-reroll-crustle-specific.tar.gz`

Kaggle submission: `53864421`

Public score: 723.4

Status: complete

Summary:
- Restored the Crustle-specific policy and Crustle wall deck from experiment
  010.
- Submitted it as the first final latest-two guard slot.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s020-reroll-crustle-specific`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 723.4.
