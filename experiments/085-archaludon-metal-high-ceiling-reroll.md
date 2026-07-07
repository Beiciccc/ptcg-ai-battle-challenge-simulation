# 085 Archaludon Metal High Ceiling Reroll

Date: 2026-07-07 UTC

Package: `artifacts/submissions/s085-archaludon-metal-high-ceiling-reroll.tar.gz`

Kaggle submission: `54410676`

Validation episode: `84494158`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Archaludon metal high-ceiling package after experiment 082
  recovered into the guard range.
- This second same-day reroll opened weak.
- The final slot shifts back to the Tomato Archaludon guard profile because it
  has the steadier recent score curve.

Validation:
- `tar -tzf artifacts/submissions/s085-archaludon-metal-high-ceiling-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py /tmp/ptcg_validate_pkg/s052/main.py`
- `python tools/check_deck.py /tmp/ptcg_validate_pkg/s052/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84494158` completed.
- Public score was 600.0.
