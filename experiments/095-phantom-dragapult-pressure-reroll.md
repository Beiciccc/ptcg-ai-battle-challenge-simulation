# 095 Phantom Dragapult Pressure Reroll

Date: 2026-07-09 UTC

Package: `artifacts/submissions/s095-phantom-dragapult-pressure-reroll.tar.gz`

Kaggle submission: `54482061`

Validation episode: `84959616`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the known-complete Dragapult pressure package after the
  Archaludon metal reroll opened weak.
- Local validation passed, including package structure, deck validation, and
  one smoke battle from the extracted package directory.
- The new row opened weak, so the final slot should switch to a Tomato
  Archaludon guard reroll for diversity.

Validation:
- `tar -tzf artifacts/submissions/s095-phantom-dragapult-pressure-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84959616` completed.
- Public score was 600.0.
