# 074 Lucario Search Hedge

Date: 2026-07-03 UTC

Package: `artifacts/submissions/s013-lucario-search-915.tar.gz`

Kaggle submission: `54292357`

Public score: 669.4

Status: complete

Summary:
- Re-submitted the Lucario search package as a non-Archaludon hedge after the
  Archaludon metal reroll.
- The hedge refreshed into a modest guard range but did not improve over the
  July 3 Archaludon metal result.
- The remaining slots should return to the Tomato Archaludon package, which
  still owns the strongest recent refreshed scores.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s013-lucario-search-915.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 669.4.
