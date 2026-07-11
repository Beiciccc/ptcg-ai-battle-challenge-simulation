# 104 Tomato Archaludon Second Probe

Date: 2026-07-11 UTC

Package: `artifacts/submissions/s104-tomato-archaludon-second-probe.tar.gz`

Kaggle submission: `54571515`

Validation episode: `85395669`

Public score: 772.2

Status: complete

Summary:
- Re-submitted the Tomato Archaludon package for a second independent
  current-day observation after the first reroll began recovering.
- Local validation passed for the archive layout, entrypoint, 60-card deck,
  and three smoke battles from the extracted root.
- Later score refreshes recovered into the guard range but remained below the
  strongest LLCC run.

Validation:
- `tar -tzf artifacts/submissions/s104-tomato-archaludon-second-probe.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85395669` completed.
- Latest refreshed public score was 772.2.
