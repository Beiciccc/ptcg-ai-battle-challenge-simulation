# 047 Pilkwang 0628 Option C

Date: 2026-06-28 UTC

Local generated package (not committed): `artifacts/submissions/s047-pilkwang-0628-option-c.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/3c2ca4a8cb89-2a541d7bf3d9/main.py), [deck.csv](../agent_zoo/sources/3c2ca4a8cb89-2a541d7bf3d9/deck.csv)

Source SHA256: main.py `3c2ca4a8cb894671fb48815a71560e9a3564b575a43ad38bbee05c53642978f0`; deck.csv `2a541d7bf3d9e6b36037123f53f4dfef6348223f79fd27095dafc602a5357c19`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54152749`

Public score: 622.0

Status: complete

Summary:
- Tested the 2026-06-28 public meta snapshot's reference-derived Lucario option
  with the low-deck threshold set to 8.
- The candidate was chosen as a conservative exploration slot after the latest
  public field read favored measured Lucario tuning over a broad rewrite.
- The refreshed public score stayed below the stronger guard range, so the next
  slots should favor historical guard packages unless a refreshed public signal
  changes materially.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s047-pilkwang-0628-option-c.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 622.0.
