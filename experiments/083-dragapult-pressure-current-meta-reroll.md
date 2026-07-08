# 083 Dragapult Pressure Current Meta Reroll

Date: 2026-07-07 UTC

Package: `artifacts/submissions/s083-dragapult-pressure-current-meta-reroll.tar.gz`

Kaggle submission: `54410436`

Validation episode: `84492874`

Public score: 768.2

Status: complete

Summary:
- Re-submitted the Dragapult pressure profile after the Archaludon metal reroll
  opened weak.
- The profile was the best new candidate family from the 2026-07-06 cycle, and
  the latest refresh recovered modestly.
- The refreshed score stayed below the stronger Archaludon and Tomato guard
  references.

Validation:
- `tar -tzf artifacts/submissions/s083-dragapult-pressure-current-meta-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84492874` completed.
- Latest refreshed public score was 768.2.
