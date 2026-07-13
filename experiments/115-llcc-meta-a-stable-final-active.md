# 115 LLCC Meta A Stable Final Active

Date: 2026-07-13 UTC

Package: `artifacts/submissions/s115-llcc-meta-a-stable-final-active.tar.gz`

Kaggle submission: `54626834`

Validation episode: `85659682`

Public score: 682.4

Status: complete

Summary:
- Re-submitted Stable LLCC after the same-day control continued to outperform
  AttackFix.
- Local validation passed for the 11-file archive layout, bare-namespace
  loading, entrypoint, 60-card deck, and three smoke battles.
- Later score refreshes recovered above the opening value and preserved the
  Stable LLCC side of the final pair.

Validation:
- `tar -tzf artifacts/submissions/s115-llcc-meta-a-stable-final-active.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85659682` completed.
- Latest refreshed public score was 682.4.
