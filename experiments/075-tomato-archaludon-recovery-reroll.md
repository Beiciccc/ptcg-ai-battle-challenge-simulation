# 075 Tomato Archaludon Recovery Reroll

Date: 2026-07-03 UTC

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54292462`

Public score: 874.1

Status: complete

Summary:
- Re-submitted the Tomato Archaludon package after the hedge slots did not
  reach the prior high guard range.
- Later refresh recovered into the high guard range.
- The result kept the Tomato Archaludon package viable, though below the final
  Archaludon metal reroll.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 874.1.
