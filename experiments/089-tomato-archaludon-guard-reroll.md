# 089 Tomato Archaludon Guard Reroll

Date: 2026-07-08 UTC

Local generated package (not committed): `artifacts/submissions/s089-tomato-archaludon-guard-reroll.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/03216723e42e-42165967b565/main.py), [deck.csv](../agent_zoo/sources/03216723e42e-42165967b565/deck.csv)

Source SHA256: main.py `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`; deck.csv `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54457450`

Validation episode: `84816429`

Public score: 661.7

Status: complete

Summary:
- Re-submitted the Tomato Archaludon guard profile after the Archaludon metal
  reroll remained below the recent guard range.
- Latest refresh recovered into the middle of the current cycle but stayed
  below the strongest guard references.
- The next slot should diversify back to the Dragapult pressure profile, which
  was the strongest result in the 2026-07-06 public-meta probe set.

Validation:
- `tar -tzf artifacts/submissions/s089-tomato-archaludon-guard-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84816429` completed.
- Latest refreshed public score was 661.7.
