# 028 Naoto Hop Alakazam Target

Date: 2026-06-22

Package: `artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`

Kaggle submission: `53945346`

Public score: 783.9

Status: complete

Summary:
- Tested the public Naoto Hop/Alakazam target-priority Lucario variant after
  the 2026-06-22 code refresh suggested target priorities against Hop and
  Alakazam were worth checking.
- The package validated successfully, and the refreshed public score became
  the best 2026-06-22 result in this batch.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `python tools/package_submission.py --source $TEMP_DIR --name s028-naoto-hop-alakazam-target`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 783.9.
