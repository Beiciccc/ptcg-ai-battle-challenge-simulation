# 071 Tomato Archaludon Final Reroll

Date: 2026-07-02 UTC

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54251621`

Public score: 964.1

Status: complete

Summary:
- Re-submitted the Tomato Archaludon package as the final reroll in the July 2
  five-submission cycle.
- The result refreshed above experiments 067 and 070.
- It became the best result from this batch.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 964.1.
