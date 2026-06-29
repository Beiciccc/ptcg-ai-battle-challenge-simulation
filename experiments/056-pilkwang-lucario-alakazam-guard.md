# 056 Pilkwang Lucario Alakazam Guard

Date: 2026-06-29 UTC

Package: `artifacts/submissions/s043-pilkwang-lucario-alakazam-clean.tar.gz`

Kaggle submission: `54182970`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Pilkwang Lucario/Alakazam guard package as the final slot in
  the five-submission batch.
- The package was chosen as a distinct guard axis from the newly strong
  Archaludon metal-tempo candidate and the Crustle guard package.
- The accepted submission opened weakly. The best current result in this batch
  is experiment 052 at 813.1, followed by experiment 054 at 811.3.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s043-pilkwang-lucario-alakazam-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
