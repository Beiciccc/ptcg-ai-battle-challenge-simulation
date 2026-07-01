# 065 Tomato Archaludon High Guard

Date: 2026-07-01 UTC

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54219440`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Tomato Archaludon profile after experiment 062 refreshed
  into the high guard range.
- This rerun opened weakly, but the same package still owns the two strongest
  latest results in this lane.
- The final slot should continue prioritizing the strongest current
  high-variance profile.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
