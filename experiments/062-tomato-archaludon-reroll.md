# 062 Tomato Archaludon Reroll

Date: 2026-07-01 UTC

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54219204`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Tomato Archaludon anti-Starmie package after experiment 061
  refreshed to 920.8 and became the strongest result in the previous batch.
- The rerun opened weakly, reinforcing that this matchup profile is high
  variance under the updated match mix.
- The next slot should move to a different high-ceiling profile before deciding
  whether to reroll this package again.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
