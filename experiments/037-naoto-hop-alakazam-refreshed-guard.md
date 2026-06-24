# 037 Naoto Hop Alakazam Refreshed Guard

Date: 2026-06-24

Package: `artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`

Kaggle submission: `54010123`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Naoto Hop/Alakazam target-priority Lucario variant after the
  prior refresh reached 1027.6 and became the strongest observed local result.
- The accepted submission returned a weak initial public score, reinforcing that
  same-package rerolls can vary sharply before later refreshes.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
