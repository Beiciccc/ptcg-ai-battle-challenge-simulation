# 083 Dragapult Pressure Current Meta Reroll

Date: 2026-07-07 UTC

Local generated package (not committed): `artifacts/submissions/s083-dragapult-pressure-current-meta-reroll.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/ef8936859fd2-29cabb30a406/main.py), [deck.csv](../agent_zoo/sources/ef8936859fd2-29cabb30a406/deck.csv)

Source SHA256: main.py `ef8936859fd215e6c704071042e5438d55e2e972b8f1806fb6eddbd03027e0b9`; deck.csv `29cabb30a40645e83c5260b83511cabdef62264f3a596cf18b265cb19493f159`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54410436`

Validation episode: `84492874`

Public score: 768.2

Status: complete

Summary:
- Re-submitted the Dragapult pressure profile after the Archaludon metal reroll
  opened weak.
- The profile was the best new candidate family from the 2026-07-06 cycle, and
  the latest refresh recovered modestly.
- The refreshed score stayed below the stronger Archaludon and Tomato guard
  references.

Validation:
- `tar -tzf artifacts/submissions/s083-dragapult-pressure-current-meta-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84492874` completed.
- Latest refreshed public score was 768.2.
