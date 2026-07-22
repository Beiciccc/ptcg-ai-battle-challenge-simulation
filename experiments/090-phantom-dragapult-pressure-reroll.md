# 090 Phantom Dragapult Pressure Reroll

Date: 2026-07-08 UTC

Local generated package (not committed): `artifacts/submissions/s090-phantom-dragapult-pressure-reroll.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/ef8936859fd2-29cabb30a406/main.py), [deck.csv](../agent_zoo/sources/ef8936859fd2-29cabb30a406/deck.csv)

Source SHA256: main.py `ef8936859fd215e6c704071042e5438d55e2e972b8f1806fb6eddbd03027e0b9`; deck.csv `29cabb30a40645e83c5260b83511cabdef62264f3a596cf18b265cb19493f159`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54457570`

Validation episode: `84816931`

Public score: 677.6

Status: complete

Summary:
- Re-submitted the Dragapult pressure profile after the 2026-07-06 public-meta
  probe was the strongest result in that candidate family.
- Local validation passed, including package structure, deck validation, and
  one smoke battle from the extracted package directory.
- Latest refresh settled below stronger historical guard results.

Validation:
- `tar -tzf artifacts/submissions/s090-phantom-dragapult-pressure-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84816931` completed.
- Latest refreshed public score was 677.6.
