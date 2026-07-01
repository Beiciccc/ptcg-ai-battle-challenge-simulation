# 063 Archaludon Metal High Ceiling

Date: 2026-07-01 UTC

Package: `artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`

Kaggle submission: `54219319`

Public score: 600.0

Status: complete

Summary:
- Re-submitted the Archaludon metal high-ceiling package after the Tomato
  Archaludon reroll settled below its prior high.
- Historical runs of this package include the strongest observed score in the
  project history, but this rerun opened weakly.
- The next slot should switch to a non-Archaludon hedge with prior stable
  official scores.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
