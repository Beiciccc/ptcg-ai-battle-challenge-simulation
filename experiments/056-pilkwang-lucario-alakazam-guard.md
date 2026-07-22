# 056 Pilkwang Lucario Alakazam Guard

Date: 2026-06-29 UTC

Local generated package (not committed): `artifacts/submissions/s043-pilkwang-lucario-alakazam-clean.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/46aae79654ec-7b413177e507/main.py), [deck.csv](../agent_zoo/sources/46aae79654ec-7b413177e507/deck.csv)

Source SHA256: main.py `46aae79654eca7d91e9a3c840d92e38d3ac6271b052379df43dc630163f68225`; deck.csv `7b413177e5077777f2178143839c0155b03b92bbc8b3a6607621a7d43f351141`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54182970`

Public score: 697.8

Status: complete

Summary:
- Re-submitted the Pilkwang Lucario/Alakazam guard package as the final slot in
  the five-submission batch.
- The package was chosen as a distinct guard axis from the newly strong
  Archaludon metal-tempo candidate and the Crustle guard package.
- The accepted submission recovered after refresh but stayed below the leading
  Archaludon metal-tempo run.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s043-pilkwang-lucario-alakazam-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 697.8.
