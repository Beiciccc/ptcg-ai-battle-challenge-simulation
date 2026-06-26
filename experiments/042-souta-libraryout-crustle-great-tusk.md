# 042 Souta LibraryOut Crustle Great Tusk

Date: 2026-06-26

Package: `artifacts/submissions/s042-souta-libraryout-crustle-great-tusk-clean.tar.gz`

Kaggle submission: `54081208`

Public score: 617.0

Status: complete

Summary:
- Tested the public LibraryOut Crustle/Great Tusk candidate after the
  2026-06-26 code refresh.
- The public title reported a high max Elo, but the accepted submission stayed
  weak after refresh.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s042-souta-libraryout-crustle-great-tusk-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 617.0.
