# 106 Tomato Archaludon Final Active

Date: 2026-07-11 UTC

Package: `artifacts/submissions/s106-tomato-archaludon-final-active.tar.gz`

Kaggle submission: `54571747`

Validation episode: `85396623`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Tomato Archaludon package as the second final active
  profile, preserving the LLCC and Tomato pair.
- Local validation passed for the archive layout, entrypoint, 60-card deck,
  and three smoke battles from the extracted root.
- The validation episode completed successfully and the first public score
  opened at 600.0.

Validation:
- `tar -tzf artifacts/submissions/s106-tomato-archaludon-final-active.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85396623` completed.
- First public score was 600.0.
