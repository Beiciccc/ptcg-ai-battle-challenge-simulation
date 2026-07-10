# 100 Tomato Archaludon Guard Reroll

Date: 2026-07-10 UTC

Package: `artifacts/submissions/s100-tomato-archaludon-guard-reroll.tar.gz`

Kaggle submission: `54514062`

Validation episode: `85134627`

Public score: 747.6

Status: complete

Summary:
- Re-submitted the Tomato Archaludon guard package after its prior run
  remained the strongest recent score.
- Local validation passed for the archive layout, entrypoint, 60-card deck,
  and three smoke battles from the extracted root.
- Later score refreshes recovered above the initial result and made this the
  strongest current result of the 2026-07-10 cycle.

Validation:
- `tar -tzf artifacts/submissions/s100-tomato-archaludon-guard-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85134627` completed.
- Latest refreshed public score was 747.6.
