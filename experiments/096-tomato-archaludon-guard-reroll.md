# 096 Tomato Archaludon Guard Reroll

Date: 2026-07-09 UTC

Package: `artifacts/submissions/s096-tomato-archaludon-guard-reroll.tar.gz`

Kaggle submission: `54482175`

Validation episode: `84960102`

Public score: 855.1

Status: complete

Summary:
- Re-submitted the Tomato Archaludon guard package as the final diversity slot
  after the Dragapult pressure reroll opened weak.
- Local validation passed, including package structure, deck validation, and
  one smoke battle from the extracted package directory.
- Later score refreshes recovered into the guard range and made this the
  strongest result of the 2026-07-09 cycle.

Validation:
- `tar -tzf artifacts/submissions/s096-tomato-archaludon-guard-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84960102` completed.
- Latest refreshed public score was 855.1.
