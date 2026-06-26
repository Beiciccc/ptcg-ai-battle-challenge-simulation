# 043 Pilkwang Lucario Alakazam

Date: 2026-06-26

Package: `artifacts/submissions/s043-pilkwang-lucario-alakazam-clean.tar.gz`

Kaggle submission: `54081359`

Public score: 600.0

Status: complete

Summary:
- Tested the public Pilkwang Lucario/Alakazam candidate after the 2026-06-26
  code refresh.
- The public notebook had strong community signal and a clean submission
  contract log, but the accepted submission opened weakly on the public
  leaderboard.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s043-pilkwang-lucario-alakazam-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
