# 068 Archaludon Metal High Ceiling

Date: 2026-07-02 UTC

Package: `artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`

Kaggle submission: `54251262`

Public score: 657.4

Status: complete

Summary:
- Re-submitted the Archaludon metal package after the July 2 Tomato Archaludon
  reroll opened weakly.
- The package retained historical upside from experiment 055 but did not
  recover that ceiling in this reroll.
- The result stayed below the refreshed Tomato Archaludon run.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 657.4.
