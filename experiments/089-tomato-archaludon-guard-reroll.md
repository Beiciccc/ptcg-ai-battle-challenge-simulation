# 089 Tomato Archaludon Guard Reroll

Date: 2026-07-08 UTC

Package: `artifacts/submissions/s089-tomato-archaludon-guard-reroll.tar.gz`

Kaggle submission: `54457450`

Validation episode: `84816429`

Public score: 680.2

Status: complete

Summary:
- Re-submitted the Tomato Archaludon guard profile after the Archaludon metal
  reroll remained below the recent guard range.
- Latest refresh recovered modestly but stayed below the prior Tomato guard
  references.
- The next slot should diversify back to the Dragapult pressure profile, which
  was the strongest result in the 2026-07-06 public-meta probe set.

Validation:
- `tar -tzf artifacts/submissions/s089-tomato-archaludon-guard-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84816429` completed.
- Latest refreshed public score was 680.2.
