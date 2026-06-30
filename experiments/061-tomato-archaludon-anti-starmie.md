# 061 Tomato Archaludon Anti Starmie

Date: 2026-06-30 UTC

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54214588`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Tomato Archaludon anti-Starmie package as the final
  decorrelated matchup profile in this five-submission batch.
- The package had prior official validation in the current project history, but
  this rerun opened in the weak range under the updated match mix.
- The best result in this batch came from the retuned Strong Start guard after
  refresh.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
