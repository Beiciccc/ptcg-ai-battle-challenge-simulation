# 098 Pilkwang 0909 Phantom Focus Standard Rebuild

Date: 2026-07-10 UTC

Local generated package (not committed): `artifacts/submissions/s098-pilkwang-0909-phantom-focus-standard-rebuild.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/60bc08be65be-29cabb30a406/main.py), [deck.csv](../agent_zoo/sources/60bc08be65be-29cabb30a406/deck.csv)

Source SHA256: main.py `60bc08be65be2df7bccff5dc3f8bc06e9a604800749d6af3d822c907e8d9d3ea`; deck.csv `29cabb30a40645e83c5260b83511cabdef62264f3a596cf18b265cb19493f159`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54513702`

Validation episode: `85132675`

Public score: 646.5

Status: complete

Summary:
- Rebuilt the Phantom Focus Transfer candidate with the standard 11-file
  package layout after the prior archive failed before validation.
- Local validation passed for the archive layout, entrypoint, 60-card deck,
  bare-namespace loading, and three smoke battles from the extracted root.
- The new validation episode completed successfully and later score refreshes
  recovered above the initial result.

Validation:
- `python tools/package_submission.py --format tar.gz`
- `tar -tzf artifacts/submissions/s098-pilkwang-0909-phantom-focus-standard-rebuild.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85132675` completed.
- Latest refreshed public score was 646.5.
