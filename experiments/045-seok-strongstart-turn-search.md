# 045 Seok Strongstart Turn Search

Date: 2026-06-26

Local generated package (not committed): `artifacts/submissions/s044-seok-strongstart-turn-search-clean.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/a3faf762fe9d-b4464eb525a2/main.py), [deck.csv](../agent_zoo/sources/a3faf762fe9d-b4464eb525a2/deck.csv)

Source SHA256: main.py `a3faf762fe9da0efc58e9916a746cc1b4a12539bb2d55f8ed0043da4799d6211`; deck.csv `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54081538`

Public score: 608.3

Status: complete

Summary:
- Tested the public Strong Start safe turn-search candidate after the
  2026-06-26 code refresh.
- The notebook output included local matchup checks with zero errors, but the
  accepted submission stayed weak after refresh.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s044-seok-strongstart-turn-search-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 608.3.
