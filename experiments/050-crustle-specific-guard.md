# 050 Crustle Specific Guard

Date: 2026-06-28 UTC

Local generated package (not committed): `artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/main.py), [deck.csv](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/deck.csv)

Source SHA256: main.py `6de341ae762f15a7d926f5359e783e189bf25d5a0cff5ec69f78a954d0bdb6d3`; deck.csv `9c2647bd80d51bfd9cf89c74026e6a53607903b94cae9c235fad0c2128aad3aa`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54152877`

Public score: 755.2

Status: complete

Summary:
- Re-submitted the historical Crustle-specific guard package after the new
  2026-06-28 candidates opened weakly.
- The package has been one of the more stable historical guard routes, with
  prior public runs reaching 885.6, 828.6, 787.1, 783.2, and 782.1 after refresh.
- The accepted submission recovered after refresh and became the best result in
  this five-submission batch.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 755.2.
