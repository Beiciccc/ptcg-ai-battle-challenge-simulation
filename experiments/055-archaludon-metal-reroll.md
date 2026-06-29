# 055 Archaludon Metal Reroll

Date: 2026-06-29 UTC

Package: `artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`

Kaggle submission: `54182907`

Public score: 669.2

Status: complete

Summary:
- Re-submitted the 2026-06-29 Archaludon metal-tempo challenger after experiment
  052 refreshed to 813.1.
- The reroll tested whether the new Metal tempo lane could reproduce a high
  public score under the current live pool.
- The accepted submission recovered after refresh but did not reproduce the
  high score from experiment 052, so the final slot used a stronger guard
  package instead of another immediate reroll.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 669.2.
