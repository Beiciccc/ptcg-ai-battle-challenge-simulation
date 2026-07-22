# 079 Pilkwang 0704 Dragapult Pressure

Date: 2026-07-06 UTC

Local generated package (not committed): `artifacts/submissions/s079-pilkwang-0704-dragapult-pressure.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/ef8936859fd2-29cabb30a406/main.py), [deck.csv](../agent_zoo/sources/ef8936859fd2-29cabb30a406/deck.csv)

Source SHA256: main.py `ef8936859fd215e6c704071042e5438d55e2e972b8f1806fb6eddbd03027e0b9`; deck.csv `29cabb30a40645e83c5260b83511cabdef62264f3a596cf18b265cb19493f159`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54379571`

Public score: 885.4

Status: complete

Summary:
- Tested the 2026-07-04 public meta snapshot's Phantom Dragapult pressure
  profile.
- This was the final probe from the same public snapshot after both the
  Library-Out complement and Archaludon anchor stayed weak.
- The public score recovered into the best result in this five-submission
  cycle.

Validation:
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/package_submission.py --name s079-pilkwang-0704-dragapult-pressure`
- `python tools/smoke_battle.py --agent main.py --deck deck.csv --games 1 --max-steps 400`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 885.4.
