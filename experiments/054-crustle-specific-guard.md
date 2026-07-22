# 054 Crustle Specific Guard

Date: 2026-06-29 UTC

Local generated package (not committed): `artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/main.py), [deck.csv](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/deck.csv)

Source SHA256: main.py `6de341ae762f15a7d926f5359e783e189bf25d5a0cff5ec69f78a954d0bdb6d3`; deck.csv `9c2647bd80d51bfd9cf89c74026e6a53607903b94cae9c235fad0c2128aad3aa`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54182835`

Public score: 689.8

Status: complete

Summary:
- Re-submitted the historical Crustle-specific guard package after the
  Alakazam/Dunsparce complement opened weakly.
- The package was selected for stability: prior refreshed runs include 885.6,
  828.6, 787.1, 783.2, 782.1, and 755.2.
- The accepted submission recovered after refresh but stayed below the strongest
  current guard results.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 689.8.
