# 037 Naoto Hop Alakazam Refreshed Guard

Date: 2026-06-24

Package: `artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`

Kaggle submission: `54010123`

Public score: 745.2

Status: complete

Summary:
- Re-submitted the Naoto Hop/Alakazam target-priority Lucario variant after the
  prior refresh reached 1027.6 and became the strongest observed local result.
- The accepted submission recovered after refresh but stayed below the prior
  high refresh, reinforcing that same-package rerolls can vary sharply.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 745.2.
