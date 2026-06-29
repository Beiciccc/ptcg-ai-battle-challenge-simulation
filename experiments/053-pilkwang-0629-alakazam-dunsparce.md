# 053 Pilkwang 0629 Alakazam Dunsparce

Date: 2026-06-29 UTC

Package: `artifacts/submissions/s053-pilkwang-0629-alakazam-dunsparce.tar.gz`

Kaggle submission: `54182783`

Public score: 513.7

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
- Latest refreshed public score was 513.7.
