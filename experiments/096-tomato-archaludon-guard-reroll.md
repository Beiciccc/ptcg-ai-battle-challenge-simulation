# 096 Tomato Archaludon Guard Reroll

Date: 2026-07-09 UTC

Package: `artifacts/submissions/s096-tomato-archaludon-guard-reroll.tar.gz`

Kaggle submission: `54482175`

Validation episode: `84960102`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Tomato Archaludon guard package as the final diversity slot
  after the Dragapult pressure reroll opened weak.
- Local validation passed, including package structure, deck validation, and
  one smoke battle from the extracted package directory.
- The new row opened weak, leaving experiment 092 as the best current result
  in this cycle.

Validation:
- `tar -tzf artifacts/submissions/s096-tomato-archaludon-guard-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84960102` completed.
- Public score was 600.0.
