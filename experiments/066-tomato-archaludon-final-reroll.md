# 066 Tomato Archaludon Final Reroll

Date: 2026-07-01 UTC

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54219508`

Public score: 932.2

Status: complete

Summary:
- Re-submitted the Tomato Archaludon package as the final high-variance reroll
  in this five-submission batch.
- The accepted submission refreshed into the high guard range, while experiment
  065 became the strongest result in the batch.
- The profile remains volatile, but it produced the strongest current results
  across the last two batches.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 932.2.
