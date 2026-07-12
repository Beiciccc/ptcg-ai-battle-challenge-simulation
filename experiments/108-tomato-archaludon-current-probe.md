# 108 Tomato Archaludon Current Probe

Date: 2026-07-12 UTC

Package: `artifacts/submissions/s108-tomato-archaludon-current-probe.tar.gz`

Kaggle submission: `54593959`

Validation episode: `85509938`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Tomato Archaludon package as a distinct current-day
  profile after the AttackFix exploration.
- Local validation passed for the archive layout, entrypoint, 60-card deck,
  and three smoke battles from the extracted root.
- The validation episode completed successfully, but the first public score
  opened below the recovering AttackFix result.

Validation:
- `tar -tzf artifacts/submissions/s108-tomato-archaludon-current-probe.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85509938` completed.
- First public score was 600.0.
