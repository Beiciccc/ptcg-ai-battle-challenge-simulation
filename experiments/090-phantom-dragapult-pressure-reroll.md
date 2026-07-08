# 090 Phantom Dragapult Pressure Reroll

Date: 2026-07-08 UTC

Package: `artifacts/submissions/s090-phantom-dragapult-pressure-reroll.tar.gz`

Kaggle submission: `54457570`

Validation episode: `84816931`

Public score: 719.8

Status: complete

Summary:
- Re-submitted the Dragapult pressure profile after the 2026-07-06 public-meta
  probe was the strongest result in that candidate family.
- Local validation passed, including package structure, deck validation, and
  one smoke battle from the extracted package directory.
- Latest refresh recovered into the best result of the current cycle, but
  stayed below stronger historical guard results.

Validation:
- `tar -tzf artifacts/submissions/s090-phantom-dragapult-pressure-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84816931` completed.
- Latest refreshed public score was 719.8.
