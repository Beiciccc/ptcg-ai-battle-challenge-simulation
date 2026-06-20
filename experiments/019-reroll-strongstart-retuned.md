# 019 Reroll Strong Start Retuned

Date: 2026-06-20

Package: `artifacts/submissions/s019-reroll-strongstart-retuned.tar.gz`

Kaggle submission: `53864336`

Public score: 550.1

Status: complete

Summary:
- Restored the retuned Strong Start policy and deck from experiment 011.
- Submitted it as the second guard reroll because the original run had reached
  885.8.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s019-reroll-strongstart-retuned`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 550.1.
