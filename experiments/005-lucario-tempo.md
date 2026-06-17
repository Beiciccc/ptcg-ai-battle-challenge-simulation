# 005 Lucario Tempo

Date: 2026-06-17

Package: `artifacts/submissions/s005-lucario-tempo.tar.gz`

Kaggle submission: `53784007`

Public score: 423.4

Status: complete

Summary:
- Switched to a Mega Lucario deck.
- Used a concise tempo policy with higher priority for evolution, abilities,
  key setup items, and energy attachment before attacking.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s005-lucario-tempo`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 423.4, below the Crustle variants.
