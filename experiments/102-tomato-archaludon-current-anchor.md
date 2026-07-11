# 102 Tomato Archaludon Current Anchor

Date: 2026-07-11 UTC

Package: `artifacts/submissions/s102-tomato-archaludon-current-anchor.tar.gz`

Kaggle submission: `54571211`

Validation episode: `85394214`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the strongest recent Tomato Archaludon package after the
  public-code refresh produced no newer evidence-backed candidate.
- Local validation passed for the archive layout, entrypoint, 60-card deck,
  and three smoke battles from the extracted root.
- The validation episode completed successfully, but the first public score
  opened below the prior Tomato result.

Validation:
- `tar -tzf artifacts/submissions/s102-tomato-archaludon-current-anchor.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85394214` completed.
- First public score was 600.0.
