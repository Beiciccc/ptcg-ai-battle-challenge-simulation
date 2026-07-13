# 114 Tomato Archaludon Current Probe

Date: 2026-07-13 UTC

Package: `artifacts/submissions/s114-tomato-archaludon-current-probe.tar.gz`

Kaggle submission: `54626692`

Validation episode: `85659212`

Public score: 827.9

Status: complete

Summary:
- Re-submitted the validated Tomato Archaludon package as the third
  current-day probe.
- Local validation passed for the nine-file archive layout, entrypoint,
  60-card deck, and three smoke battles from the extracted root.
- Later score refreshes rose above 800 and led the current-day comparison.

Validation:
- `tar -tzf artifacts/submissions/s114-tomato-archaludon-current-probe.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85659212` completed.
- Latest refreshed public score was 827.9.
