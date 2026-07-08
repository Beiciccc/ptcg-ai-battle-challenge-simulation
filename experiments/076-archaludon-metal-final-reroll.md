# 076 Archaludon Metal Final Reroll

Date: 2026-07-03 UTC

Package: `artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`

Kaggle submission: `54292591`

Public score: 908.7

Status: complete

Summary:
- Re-submitted the Archaludon metal package as the final reroll after
  experiment 073 led the batch.
- Later refresh recovered strongly and surpassed experiment 074.
- This became the best result in the July 3 five-submission cycle.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 908.7.
