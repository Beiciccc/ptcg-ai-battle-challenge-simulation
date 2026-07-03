# 075 Tomato Archaludon Recovery Reroll

Date: 2026-07-03 UTC

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54292462`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Tomato Archaludon package after the hedge slots did not
  reach the prior high guard range.
- This reroll opened weakly and did not recover the package's recent high
  scores.
- The Archaludon metal hedge remains the best July 3 result so far.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Public score was 600.0.
