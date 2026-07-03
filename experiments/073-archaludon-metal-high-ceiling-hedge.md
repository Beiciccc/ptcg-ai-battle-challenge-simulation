# 073 Archaludon Metal High Ceiling Hedge

Date: 2026-07-03 UTC

Package: `artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`

Kaggle submission: `54292179`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Archaludon metal high-ceiling package after the first July 3
  Tomato Archaludon reroll opened low.
- The hedge did not reproduce its historical high-ceiling behavior in this
  reroll.
- The next slot should test a non-Archaludon profile before returning to the
  Tomato package.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Public score was 600.0.
