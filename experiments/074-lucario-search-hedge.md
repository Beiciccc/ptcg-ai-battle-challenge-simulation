# 074 Lucario Search Hedge

Date: 2026-07-03 UTC

Package: `artifacts/submissions/s013-lucario-search-915.tar.gz`

Kaggle submission: `54292357`

Public score: 812.8

Status: complete

Summary:
- Re-submitted the Lucario search package as a non-Archaludon hedge after the
  Archaludon metal reroll.
- The hedge refreshed into the best July 3 score so far.
- The result outperformed the Tomato and Archaludon metal rerolls in this
  cycle.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s013-lucario-search-915.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 812.8.
