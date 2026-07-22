# 027 Roman V10 Strong Start Baseline

Date: 2026-06-22

Local generated package (not committed): `artifacts/submissions/s027-roman-v10-strong-start-baseline.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/db3772cc387b-fd2fc062ffc2/main.py), [deck.csv](../agent_zoo/sources/db3772cc387b-fd2fc062ffc2/deck.csv)

Source SHA256: main.py `db3772cc387b2a6106bb18344708093576beebd5de5f7ba994e8bb79855eeced`; deck.csv `fd2fc062ffc23c5a4f77f30c05d2fc1d08a7bade73e1dc67e1dd547192fd46b3`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53945192`

Public score: 652.0

Status: complete

Summary:
- Tested the public Roman V10 Strong Start baseline after the 2026-06-22 code
  refresh identified it as a high-signal updated baseline.
- The package validated successfully, but the refreshed public score stayed
  below the strongest guard candidates.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `python tools/package_submission.py --source $TEMP_DIR --name s027-roman-v10-strong-start-baseline`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 652.0.
