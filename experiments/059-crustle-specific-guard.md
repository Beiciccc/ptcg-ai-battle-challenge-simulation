# 059 Crustle Specific Guard

Date: 2026-06-30 UTC

Package: `artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Kaggle submission: `54214471`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Crustle-specific guard package as a decorrelated historical
  stability probe after the Naoto Hop/Alakazam guard recovered.
- Historical reruns of this package were relatively stable, but the updated
  match mix produced a weak initial result in this slot.
- The next slot should move to another high-ceiling guard profile rather than
  immediately rerolling this package.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
