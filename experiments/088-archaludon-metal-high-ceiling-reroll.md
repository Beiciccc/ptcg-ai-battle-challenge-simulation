# 088 Archaludon Metal High Ceiling Reroll

Date: 2026-07-08 UTC

Package: `artifacts/submissions/s088-archaludon-metal-high-ceiling-reroll.tar.gz`

Kaggle submission: `54457364`

Validation episode: `84815933`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Archaludon metal high-ceiling package after experiment 085
  became the latest best result from the prior cycle.
- This reroll opened weak.
- The next slot shifts to the Tomato Archaludon guard profile for score-curve
  diversity.

Validation:
- `tar -tzf artifacts/submissions/s088-archaludon-metal-high-ceiling-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84815933` completed.
- Public score was 600.0.
