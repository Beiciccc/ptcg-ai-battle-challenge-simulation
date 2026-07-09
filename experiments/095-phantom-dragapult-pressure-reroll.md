# 095 Phantom Dragapult Pressure Reroll

Date: 2026-07-09 UTC

Package: `artifacts/submissions/s095-phantom-dragapult-pressure-reroll.tar.gz`

Kaggle submission: `54482061`

Validation episode: `84959616`

Public score: 711.8

Status: complete

Summary:
- Re-submitted the known-complete Dragapult pressure package after the
  Archaludon metal reroll opened weak.
- Local validation passed, including package structure, deck validation, and
  one smoke battle from the extracted package directory.
- Latest refresh recovered into the second-best result of the current cycle.

Validation:
- `tar -tzf artifacts/submissions/s095-phantom-dragapult-pressure-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84959616` completed.
- Latest refreshed public score was 711.8.
