# 113 LLCC Meta A Stable Current Control

Date: 2026-07-13 UTC

Package: `artifacts/submissions/s113-llcc-meta-a-stable-current-control.tar.gz`

Kaggle submission: `54626542`

Validation episode: `85658280`

Public score: 696.8

Status: complete

Summary:
- Re-submitted Stable LLCC as a same-deck control after the AttackFix probe
  opened weak.
- Local validation passed for the 11-file archive layout, entrypoint,
  60-card deck, and three smoke battles from the extracted root.
- The refreshed public score recovered above its opening value and led the
  current AttackFix probe.

Validation:
- `tar -tzf artifacts/submissions/s113-llcc-meta-a-stable-current-control.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85658280` completed.
- Latest refreshed public score was 696.8.
