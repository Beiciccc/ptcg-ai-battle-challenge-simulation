# 045 Seok Strongstart Turn Search

Date: 2026-06-26

Package: `artifacts/submissions/s044-seok-strongstart-turn-search-clean.tar.gz`

Kaggle submission: `54081538`

Public score: 600.0

Status: complete

Summary:
- Tested the public Strong Start safe turn-search candidate after the
  2026-06-26 code refresh.
- The notebook output included local matchup checks with zero errors, but the
  accepted submission opened weakly on the public leaderboard.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s044-seok-strongstart-turn-search-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
