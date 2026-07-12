# 105 LLCC Meta A Stable Final Active

Date: 2026-07-11 UTC

Package: `artifacts/submissions/s105-llcc-meta-a-stable-final-active.tar.gz`

Kaggle submission: `54571645`

Validation episode: `85396146`

Public score: 874.6

Status: complete

Summary:
- Re-submitted the LLCC Meta A Stable package as the first final active
  profile after experiment 103 became the strongest current result.
- Local validation passed for the 11-file archive layout, entrypoint,
  60-card deck, and three smoke battles from the extracted root.
- Later score refreshes recovered into the high guard range and made this the
  strongest result of the 2026-07-11 cycle.

Validation:
- `tar -tzf artifacts/submissions/s105-llcc-meta-a-stable-final-active.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85396146` completed.
- Latest refreshed public score was 874.6.
