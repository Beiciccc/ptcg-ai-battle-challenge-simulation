# 083 Dragapult Pressure Current Meta Reroll

Date: 2026-07-07 UTC

Package: `artifacts/submissions/s083-dragapult-pressure-current-meta-reroll.tar.gz`

Kaggle submission: `54410436`

Validation episode: `84492874`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Dragapult pressure profile after the Archaludon metal reroll
  opened weak.
- The profile was the best new candidate family from the 2026-07-06 cycle, but
  this reroll also opened weak.
- The next slot shifts to the Tomato Archaludon guard profile for a historically
  steadier result curve.

Validation:
- `tar -tzf artifacts/submissions/s083-dragapult-pressure-current-meta-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py /tmp/ptcg_validate_pkg/s079/main.py`
- `python tools/check_deck.py /tmp/ptcg_validate_pkg/s079/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84492874` completed.
- Public score was 600.0.
