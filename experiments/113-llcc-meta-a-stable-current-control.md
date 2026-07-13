# 113 LLCC Meta A Stable Current Control

Date: 2026-07-13 UTC

Package: `artifacts/submissions/s113-llcc-meta-a-stable-current-control.tar.gz`

Kaggle submission: `54626542`

Validation episode: `85658280`

Public score: 600.0

Status: complete

Summary:
- Re-submitted Stable LLCC as a same-deck control after the AttackFix probe
  opened weak.
- Local validation passed for the 11-file archive layout, entrypoint,
  60-card deck, and three smoke battles from the extracted root.
- The validation episode completed successfully and the first public score
  opened at 600.0.

Validation:
- `tar -tzf artifacts/submissions/s113-llcc-meta-a-stable-current-control.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85658280` completed.
- First public score was 600.0.
