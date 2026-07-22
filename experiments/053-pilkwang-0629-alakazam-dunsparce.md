# 053 Pilkwang 0629 Alakazam Dunsparce

Date: 2026-06-29 UTC

Local generated package (not committed): `artifacts/submissions/s053-pilkwang-0629-alakazam-dunsparce.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/46aae79654ec-0f8fb632ade2/main.py), [deck.csv](../agent_zoo/sources/46aae79654ec-0f8fb632ade2/deck.csv)

Source SHA256: main.py `46aae79654eca7d91e9a3c840d92e38d3ac6271b052379df43dc630163f68225`; deck.csv `0f8fb632ade2833645af8c6ffe2b282fe24e7446ee8b23f3e468b8410d8ea36c`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54182783`

Public score: 445.6

Status: complete

Summary:
- Tested the 2026-06-29 public meta snapshot's Alakazam/Dunsparce complement as
  a decorrelated second profile after the Archaludon metal-tempo challenger.
- The profile was chosen because the public snapshot framed it as a portfolio
  hedge against duplicated failure modes.
- The accepted submission stayed weak after refresh, so the next slot should
  return to current guard packages or a separately validated archetype.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s053-pilkwang-0629-alakazam-dunsparce.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 445.6.
