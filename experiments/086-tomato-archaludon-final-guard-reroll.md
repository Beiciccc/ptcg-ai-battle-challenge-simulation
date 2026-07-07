# 086 Tomato Archaludon Final Guard Reroll

Date: 2026-07-07 UTC

Package: `artifacts/submissions/s086-tomato-archaludon-final-guard-reroll.tar.gz`

Kaggle submission: `54410757`

Validation episode: `84494803`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Tomato Archaludon guard profile as the final slot after the
  second Archaludon metal reroll opened weak.
- The final reroll also opened weak.
- Experiment 082 remains the best result from the five-submission cycle.

Validation:
- `tar -tzf artifacts/submissions/s086-tomato-archaludon-final-guard-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py /tmp/ptcg_validate_pkg/s045/main.py`
- `python tools/check_deck.py /tmp/ptcg_validate_pkg/s045/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84494803` completed.
- Public score was 600.0.
