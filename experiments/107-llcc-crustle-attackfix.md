# 107 LLCC Crustle AttackFix

Date: 2026-07-12 UTC

Package: `artifacts/submissions/s107-llcc-crustle-attackfix.tar.gz`

Kaggle submission: `54593777`

Validation episode: `85508912`

Public score: 904.2

Status: complete

Summary:
- Tested the LLCC Crustle AttackFix variant after a public roster update
  supplied current matchup evidence.
- The candidate keeps the Stable deck and narrows the Metal Defender and
  Raging Hammer overrides to opposing Crustle.
- Local validation passed for the 11-file archive layout, bare-namespace
  loading, entrypoint, 60-card deck, and three smoke battles.
- Later score refreshes recovered above 900 and made this the strongest result
  from the first three submissions.

Validation:
- `tar -tzf artifacts/submissions/s107-llcc-crustle-attackfix.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85508912` completed.
- Latest refreshed public score was 904.2.
