# 081 Tomato Archaludon Guard Reroll

Date: 2026-07-06 UTC

Local generated package (not committed): `artifacts/submissions/s081-tomato-archaludon-guard-reroll.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/03216723e42e-42165967b565/main.py), [deck.csv](../agent_zoo/sources/03216723e42e-42165967b565/deck.csv)

Source SHA256: main.py `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`; deck.csv `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54379819`

Public score: 868.2

Status: complete

Summary:
- Re-submitted the Tomato Archaludon guard package as the final slot after the
  Archaludon metal reroll.
- This package had multiple recent high guard results, and the latest refresh
  recovered into a high guard range.
- The refreshed result stayed below the Archaludon metal and Dragapult pressure
  profiles from the same cycle.

Validation:
- `tar -tzf artifacts/submissions/s081-tomato-archaludon-guard-reroll.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 868.2.
