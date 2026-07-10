# 099 Phantom Dragapult Pressure Reroll

Date: 2026-07-10 UTC

Package: `artifacts/submissions/s099-phantom-dragapult-pressure-reroll.tar.gz`

Kaggle submission: `54513822`

Validation episode: `85133161`

Public score: 499.4

Status: complete

Summary:
- Re-submitted the known-complete Phantom Dragapult pressure package as a
  complementary profile to the rebuilt Focus candidate.
- Local validation passed for the 11-file archive layout, entrypoint,
  60-card deck, and three smoke battles from the extracted root.
- Later score refreshes remained below the current LLCC anchor.

Validation:
- `tar -tzf artifacts/submissions/s099-phantom-dragapult-pressure-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85133161` completed.
- Latest refreshed public score was 499.4.
