# 067 Tomato Archaludon Reroll

Date: 2026-07-02 UTC

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54251164`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Tomato Archaludon package after experiments 065 and 066
  refreshed into the high guard range.
- The first July 2 reroll opened much lower than the prior two refreshed runs.
- This keeps the package in the candidate set but argues against immediate
  repeated exposure without a decorrelated hedge.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Public score was 600.0.
