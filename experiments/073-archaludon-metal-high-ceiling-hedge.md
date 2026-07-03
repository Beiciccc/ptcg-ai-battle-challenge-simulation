# 073 Archaludon Metal High Ceiling Hedge

Date: 2026-07-03 UTC

Package: `artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`

Kaggle submission: `54292179`

Public score: 721.6

Status: complete

Summary:
- Re-submitted the Archaludon metal high-ceiling package after the first July 3
  Tomato Archaludon reroll opened low.
- The hedge refreshed into the best July 3 score so far, but it stayed below
  the prior high guard range.
- The next slot should test a non-Archaludon profile before returning to the
  Tomato package.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 721.6.
