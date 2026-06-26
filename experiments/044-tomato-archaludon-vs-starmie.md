# 044 Tomato Archaludon vs Starmie

Date: 2026-06-26

Package: `artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`

Kaggle submission: `54081459`

Public score: 698.8

Status: complete

Summary:
- Tested the public Archaludon sample that reported a favorable matchup against
  a 1300+ Starmie benchmark.
- The candidate was submitted as a new archetype probe after two public-code
  candidates opened weakly. It recovered after refresh and became the best
  2026-06-26 result in this batch.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s045-tomato-archaludon-vs-starmie-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 698.8.
