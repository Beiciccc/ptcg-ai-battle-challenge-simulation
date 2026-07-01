# 066 Tomato Archaludon Final Reroll

Date: 2026-07-01 UTC

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54219508`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Tomato Archaludon package as the final high-variance reroll
  in this five-submission batch.
- The accepted submission opened weakly, while experiment 062 remained the
  strongest result in the batch after refresh.
- The profile remains volatile: it produced both the best current batch result
  and two weak reruns.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
