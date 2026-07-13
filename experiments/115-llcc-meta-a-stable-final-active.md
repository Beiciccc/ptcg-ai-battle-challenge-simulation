# 115 LLCC Meta A Stable Final Active

Date: 2026-07-13 UTC

Package: `artifacts/submissions/s115-llcc-meta-a-stable-final-active.tar.gz`

Kaggle submission: `54626834`

Validation episode: `85659682`

Public score: 600.0

Status: complete

Summary:
- Re-submitted Stable LLCC after the same-day control continued to outperform
  AttackFix.
- Local validation passed for the 11-file archive layout, bare-namespace
  loading, entrypoint, 60-card deck, and three smoke battles.
- The validation episode completed successfully and the first public score
  opened at 600.0.

Validation:
- `tar -tzf artifacts/submissions/s115-llcc-meta-a-stable-final-active.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85659682` completed.
- First public score was 600.0.
