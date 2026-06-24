# 023 Crustle Specific High Diversity Reroll

Date: 2026-06-21

Package: `artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Kaggle submission: `53907042`

Public score: 828.6

Status: complete

Summary:
- Re-submitted the historical Crustle-specific policy and wall deck package as
  a high-diversity repair slot after the first 2026-06-21 guard reroll scored
  weakly.
- The submission completed, and the refreshed public score recovered strongly
  from the initial result but stayed below the historical best run.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `tar -tzf artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 828.6.
