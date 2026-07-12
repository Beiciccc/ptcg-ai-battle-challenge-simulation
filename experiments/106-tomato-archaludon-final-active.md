# 106 Tomato Archaludon Final Active

Date: 2026-07-11 UTC

Package: `artifacts/submissions/s106-tomato-archaludon-final-active.tar.gz`

Kaggle submission: `54571747`

Validation episode: `85396623`

Public score: 806.7

Status: complete

Summary:
- Re-submitted the Tomato Archaludon package as the second final active
  profile, preserving the LLCC and Tomato pair.
- Local validation passed for the archive layout, entrypoint, 60-card deck,
  and three smoke battles from the extracted root.
- Later score refreshes recovered into the high guard range.

Validation:
- `tar -tzf artifacts/submissions/s106-tomato-archaludon-final-active.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85396623` completed.
- Latest refreshed public score was 806.7.
