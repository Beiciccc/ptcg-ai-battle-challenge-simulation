# 039 Maktha 1084 Latest Probe

Date: 2026-06-24

Local generated package (not committed): `artifacts/submissions/s033-maktha-1084-latest.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/459cf970d9ff-2a541d7bf3d9/main.py), [deck.csv](../agent_zoo/sources/459cf970d9ff-2a541d7bf3d9/deck.csv)

Source SHA256: main.py `459cf970d9ffc28fcb13473cff216750f17d53a35fa990fcab1805e00e78a848`; deck.csv `2a541d7bf3d9e6b36037123f53f4dfef6348223f79fd27095dafc602a5357c19`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54010393`

Public score: 609.0

Status: complete

Summary:
- Tested the refreshed public 1084.5 baseline candidate as a distinct
  exploration slot after the Naoto and Diary Day 3 submissions started weakly.
- The package differs from the earlier 1084.5 baseline package and passed the
  same entrypoint and deck checks.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s033-maktha-1084-latest.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 609.0.
