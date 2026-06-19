# 012 Roman V7 Guarded

Date: 2026-06-19

Package: `artifacts/submissions/s012-roman-v7-guarded.tar.gz`

Kaggle submission: `53827461`

Public score: 748.4

Status: complete

Summary:
- Kept the retuned Mega Lucario deck from experiment 011.
- Updated the policy with the public V7 guard changes: low-deck draw
  suppression, setup bench scoring, discard scoring, and damage-counter target
  handling.
- Submitted this as the first 2026-06-19 candidate because the public Code
  list showed a V7 title with a 960+ leaderboard claim.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s012-roman-v7-guarded`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 748.4.
