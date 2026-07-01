# 062 Tomato Archaludon Reroll

Date: 2026-07-01 UTC

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54219204`

Public score: 862.9

Status: complete

Summary:
- Re-submitted the Tomato Archaludon anti-Starmie package after experiment 061
  refreshed to 920.8 and became the strongest result in the previous batch.
- The rerun recovered into the high guard range, reinforcing that this matchup
  profile remains the strongest current lane despite variance.
- Later slots can justify another reroll if alternative hedges stay weak.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 862.9.
