# 077 Pilkwang 0704 LibraryOut Complement

Date: 2026-07-06 UTC

Local generated package (not committed): `artifacts/submissions/s077-pilkwang-0704-libraryout-complement.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/244eb8c6b1a8-6415396d35c0/main.py), [deck.csv](../agent_zoo/sources/244eb8c6b1a8-6415396d35c0/deck.csv)

Source SHA256: main.py `244eb8c6b1a89d65769a3ecc315fcd39809dfc3243dd2067f3ca24b29cb8b498`; deck.csv `6415396d35c0f4b3d69ee6c231337968cc9f2d5d0767de801346d6f412c18e62`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54379313`

Public score: 376.8

Status: complete

Summary:
- Tested the 2026-07-04 public meta snapshot's Great Tusk / Crustle
  Library-Out complement profile.
- The public snapshot framed this profile as a portfolio complement for a
  wider field with Marnie/Munkidori, Starmie, and smaller stress archetypes.
- The public score stayed weak after refresh, so the next slot should prefer a
  stronger anchor profile rather than expanding this complement line
  immediately.

Validation:
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/package_submission.py --name s077-pilkwang-0704-libraryout-complement`
- `python tools/smoke_battle.py --games 1 --max-steps 400`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 376.8.
