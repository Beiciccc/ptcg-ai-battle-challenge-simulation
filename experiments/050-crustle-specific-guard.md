# 050 Crustle Specific Guard

Date: 2026-06-28 UTC

Package: `artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Kaggle submission: `54152877`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the historical Crustle-specific guard package after the new
  2026-06-28 candidates opened weakly.
- The package has been one of the more stable historical guard routes, with
  prior public runs reaching 885.6, 828.6, 787.1, 783.2, and 782.1 after refresh.
- The accepted submission opened weakly, so the final slot should use the best
  currently refreshed package rather than another new exploratory profile.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
