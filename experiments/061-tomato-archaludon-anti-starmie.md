# 061 Tomato Archaludon Anti Starmie

Date: 2026-06-30 UTC

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54214588`

Public score: 920.8

Status: complete

Summary:
- Re-submitted the Tomato Archaludon anti-Starmie package as the final
  decorrelated matchup profile in this five-submission batch.
- The package had prior official validation in the current project history, and
  this rerun refreshed into the strongest result in the batch.
- The next batch should prioritize this matchup profile before moving to lower
  confidence historical guards.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 920.8.
