# 074 Lucario Search Hedge

Date: 2026-07-03 UTC

Local generated package (not committed): `artifacts/submissions/s013-lucario-search-915.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/8026b86be33f-b4464eb525a2/main.py), [deck.csv](../agent_zoo/sources/8026b86be33f-b4464eb525a2/deck.csv)

Source SHA256: main.py `8026b86be33fdec0fcb60051c6adecf91a3ecd9cbbff539fb0a0c617d1601ad3`; deck.csv `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54292357`

Public score: 812.8

Status: complete

Summary:
- Re-submitted the Lucario search package as a non-Archaludon hedge after the
  Archaludon metal reroll.
- The hedge refreshed into the best July 3 score so far.
- The result outperformed the Tomato and Archaludon metal rerolls in this
  cycle.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s013-lucario-search-915.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 812.8.
