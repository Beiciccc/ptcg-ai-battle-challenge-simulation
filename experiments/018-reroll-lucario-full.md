# 018 Reroll Lucario Full

Date: 2026-06-20

Package: `artifacts/submissions/s018-reroll-lucario-full.tar.gz`

Kaggle submission: `53864259`

Public score: 742.5

Status: complete

Summary:
- Restored the full Lucario policy and original Mega Lucario deck from
  experiment 009.
- Submitted it as a guard reroll because the original run remained the best
  observed result at 893.0.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s018-reroll-lucario-full`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 742.5.
