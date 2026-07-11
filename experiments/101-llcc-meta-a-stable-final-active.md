# 101 LLCC Meta A Stable Final Active

Date: 2026-07-10 UTC

Package: `artifacts/submissions/s101-llcc-meta-a-stable-final-active.tar.gz`

Kaggle submission: `54514154`

Validation episode: `85135116`

Public score: 741.2

Status: complete

Summary:
- Re-submitted the LLCC Meta A Stable package as the final active anchor after
  it remained the strongest result among the first four submissions.
- Local validation passed for the 11-file archive layout, entrypoint,
  60-card deck, and three smoke battles from the extracted root.
- Later score refreshes recovered above the initial result but stayed below
  the Tomato anchor.

Validation:
- `tar -tzf artifacts/submissions/s101-llcc-meta-a-stable-final-active.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85135116` completed.
- Latest refreshed public score was 741.2.
