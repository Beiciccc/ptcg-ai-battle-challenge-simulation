# 064 Lucario Search Hedge

Date: 2026-07-01 UTC

Package: `artifacts/submissions/s013-lucario-search-915.tar.gz`

Kaggle submission: `54219383`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Lucario search package as a non-Archaludon hedge after the
  Archaludon metal reroll settled below the current Tomato profile.
- Historical runs of this package were stable in the mid-to-high guard range,
  but this rerun opened weakly.
- With the Tomato profile now producing two recent high scores, the next slot
  should prioritize that stronger current lane.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s013-lucario-search-915.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
