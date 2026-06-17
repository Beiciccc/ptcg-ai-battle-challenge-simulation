# 003 Crustle Wall

Date: 2026-06-17

Package: `artifacts/submissions/s003-crustle-wall.tar.gz`

Kaggle submission: `53783789`

Public score: 741.4

Status: complete

Summary:
- Switched from the sample Mega Abomasnow deck to a Crustle wall deck.
- Added light card-specific handling for Hero's Cape, Jumbo Ice Cream, Cook,
  and Buddy-Buddy Poffin.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s003-crustle-wall`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 741.4, making this a clear improvement over
  the sample-deck baseline.
