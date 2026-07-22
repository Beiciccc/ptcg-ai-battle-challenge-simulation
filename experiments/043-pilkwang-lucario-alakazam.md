# 043 Pilkwang Lucario Alakazam

Date: 2026-06-26

Local generated package (not committed): `artifacts/submissions/s043-pilkwang-lucario-alakazam-clean.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/46aae79654ec-7b413177e507/main.py), [deck.csv](../agent_zoo/sources/46aae79654ec-7b413177e507/deck.csv)

Source SHA256: main.py `46aae79654eca7d91e9a3c840d92e38d3ac6271b052379df43dc630163f68225`; deck.csv `7b413177e5077777f2178143839c0155b03b92bbc8b3a6607621a7d43f351141`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54081359`

Public score: 621.3

Status: complete

Summary:
- Tested the public Pilkwang Lucario/Alakazam candidate after the 2026-06-26
  code refresh.
- The public notebook had strong community signal and a clean submission
  contract log, but the accepted submission stayed weak after refresh.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s043-pilkwang-lucario-alakazam-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 621.3.
