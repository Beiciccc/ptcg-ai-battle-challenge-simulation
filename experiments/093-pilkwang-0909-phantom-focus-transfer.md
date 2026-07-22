# 093 Pilkwang 0909 Phantom Focus Transfer

Date: 2026-07-09 UTC

Local generated package (not committed): `artifacts/submissions/s093-pilkwang-0909-phantom-focus-transfer.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/60bc08be65be-29cabb30a406/main.py), [deck.csv](../agent_zoo/sources/60bc08be65be-29cabb30a406/deck.csv)

Source SHA256: main.py `60bc08be65be2df7bccff5dc3f8bc06e9a604800749d6af3d822c907e8d9d3ea`; deck.csv `29cabb30a40645e83c5260b83511cabdef62264f3a596cf18b265cb19493f159`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54481871`

Validation episode: n/a

Public score: n/a

Status: error

Summary:
- Tested the 2026-07-09 public meta snapshot's Phantom Focus Transfer profile.
- Local validation passed, including archive root structure, entrypoint check,
  deck validation, and one smoke battle from the extracted package directory.
- Kaggle returned an ERROR row with no validation episode, so the next slot
  should avoid this exact package path and use a known-complete profile.

Validation:
- `tar -tzf artifacts/submissions/s093-pilkwang-0909-phantom-focus-transfer.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle submission `54481871` returned status ERROR.
- No validation episode was available from the Kaggle episodes endpoint.
