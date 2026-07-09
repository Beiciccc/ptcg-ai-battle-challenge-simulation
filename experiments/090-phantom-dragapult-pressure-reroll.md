# 090 Phantom Dragapult Pressure Reroll

Date: 2026-07-08 UTC

Package: `artifacts/submissions/s090-phantom-dragapult-pressure-reroll.tar.gz`

Kaggle submission: `54457570`

Validation episode: `84816931`

Public score: 677.6

Status: complete

Summary:
- Re-submitted the Dragapult pressure profile after the 2026-07-06 public-meta
  probe was the strongest result in that candidate family.
- Local validation passed, including package structure, deck validation, and
  one smoke battle from the extracted package directory.
- Latest refresh settled below stronger historical guard results.

Validation:
- `tar -tzf artifacts/submissions/s090-phantom-dragapult-pressure-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84816931` completed.
- Latest refreshed public score was 677.6.
