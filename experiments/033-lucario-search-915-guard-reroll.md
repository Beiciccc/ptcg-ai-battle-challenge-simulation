# 033 Lucario Search 915 Guard Reroll

Date: 2026-06-23

Local generated package (not committed): `artifacts/submissions/s013-lucario-search-915.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/8026b86be33f-b4464eb525a2/main.py), [deck.csv](../agent_zoo/sources/8026b86be33f-b4464eb525a2/deck.csv)

Source SHA256: main.py `8026b86be33fdec0fcb60051c6adecf91a3ecd9cbbff539fb0a0c617d1601ad3`; deck.csv `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53961230`

Public score: 737.1

Status: complete

Summary:
- Re-submitted the Lucario search 915 package as a high-ceiling guard reroll
  after the first 2026-06-23 Naoto reroll started weakly.
- The submission completed, and the refreshed public score recovered but stayed
  below the Naoto reroll.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s013-lucario-search-915.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 737.1.
