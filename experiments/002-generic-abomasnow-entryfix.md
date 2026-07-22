# 002 Generic Abomasnow Entrypoint Fix

Date: 2026-06-17

Local generated package (not committed): `artifacts/submissions/s002-generic-abomasnow-entryfix.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/8c02fa8a72f8-e92d5717fd04/main.py), [deck.csv](../agent_zoo/sources/8c02fa8a72f8-e92d5717fd04/deck.csv)

Source SHA256: main.py `8c02fa8a72f81174e26d5462adc28659bfd8de711ff14bf9ba2362ffdd46c93a`; deck.csv `e92d5717fd04865b0b528307df7a9d9aecc2c7b917bfbd5042fe58e3d1f26997`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53783691`

Public score: 556.4

Status: complete

Summary:
- Kept the sample Mega Abomasnow deck.
- Moved `agent()` to the final top-level function position.
- Added static entrypoint validation before packaging.

Validation:
- `python tools/check_submission_entrypoint.py submission/main.py`
- `python tools/check_deck.py submission/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `python tools/package_submission.py --name s002-generic-abomasnow-entryfix`

Result:
- Kaggle validation completed.
- Public score was low, so the next experiment should test a stronger public
  deck concept rather than only tuning the generic policy.
