# 115 LLCC Meta A Stable Final Active

Date: 2026-07-13 UTC

Package: `artifacts/submissions/s115-llcc-meta-a-stable-final-active.tar.gz`

Kaggle submission: `54626834`

Validation episode: `85659682`

Public score: 879.2

Status: complete

Summary:
- Re-submitted Stable LLCC after the same-day control continued to outperform
  AttackFix.
- Local validation passed for the 11-file archive layout, bare-namespace
  loading, entrypoint, 60-card deck, and three smoke battles.
- Mature score refreshes recovered into the high guard range and preserved
  the Stable LLCC side of the final pair.

Validation:
- `tar -tzf artifacts/submissions/s115-llcc-meta-a-stable-final-active.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85659682` completed.
- Mature public score was 879.2.
