# 026 Final Latest-Two Lucario Full Guard

Date: 2026-06-21

Local generated package (not committed): `artifacts/submissions/s009-resubmit-lucario-full.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/9154a80b62c1-b4464eb525a2/main.py), [deck.csv](../agent_zoo/sources/9154a80b62c1-b4464eb525a2/deck.csv)

Source SHA256: main.py `9154a80b62c1eb67fcda5273bc637e97d337f8efff85734ffd7719a07a796d6f`; deck.csv `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53907370`

Public score: 632.7

Status: complete

Summary:
- Re-submitted the historical full Lucario guard package as the final
  latest-two slot for the 2026-06-21 batch.
- The submission completed, and the refreshed public score stayed below the
  strongest 2026-06-21 run.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `tar -tzf artifacts/submissions/s009-resubmit-lucario-full.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 632.7.
