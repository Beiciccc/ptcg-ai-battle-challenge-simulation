# 054 Crustle Specific Guard

Date: 2026-06-29 UTC

Package: `artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Kaggle submission: `54182835`

Public score: 733.1

Status: complete

Summary:
- Re-submitted the historical Crustle-specific guard package after the
  Alakazam/Dunsparce complement opened weakly.
- The package was selected for stability: prior refreshed runs include 885.6,
  828.6, 787.1, 783.2, 782.1, and 755.2.
- The accepted submission recovered into the guard range after refresh; the
  strongest current result in this batch is experiment 052 at 813.1.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 733.1.
