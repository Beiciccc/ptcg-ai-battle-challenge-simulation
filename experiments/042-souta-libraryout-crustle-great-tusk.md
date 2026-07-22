# 042 Souta LibraryOut Crustle Great Tusk

Date: 2026-06-26

Local generated package (not committed): `artifacts/submissions/s042-souta-libraryout-crustle-great-tusk-clean.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/244eb8c6b1a8-6415396d35c0/main.py), [deck.csv](../agent_zoo/sources/244eb8c6b1a8-6415396d35c0/deck.csv)

Source SHA256: main.py `244eb8c6b1a89d65769a3ecc315fcd39809dfc3243dd2067f3ca24b29cb8b498`; deck.csv `6415396d35c0f4b3d69ee6c231337968cc9f2d5d0767de801346d6f412c18e62`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54081208`

Public score: 617.0

Status: complete

Summary:
- Tested the public LibraryOut Crustle/Great Tusk candidate after the
  2026-06-26 code refresh.
- The public title reported a high max Elo, but the accepted submission stayed
  weak after refresh.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s042-souta-libraryout-crustle-great-tusk-clean.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 617.0.
