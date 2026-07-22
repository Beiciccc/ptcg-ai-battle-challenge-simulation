# 048 Naoto Hop Alakazam Guard

Date: 2026-06-28 UTC

Local generated package (not committed): `artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/635999b1a0f7-e07b796d823c/main.py), [deck.csv](../agent_zoo/sources/635999b1a0f7-e07b796d823c/deck.csv)

Source SHA256: main.py `635999b1a0f7970e70c17bb591c21b7576ddc83889ef5f50b76b8687ced5b09d`; deck.csv `e07b796d823cbbfec98ccd6a1038527321264f0357afa7f60a021cf92066e510`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54152792`

Public score: 591.6

Status: complete

Summary:
- Re-submitted the historical Naoto Hop/Alakazam guard package after the new
  2026-06-28 Option C candidate underperformed.
- The package remains the strongest historical local result, with prior public
  runs reaching 1027.6, 854.6, 835.2, and 822.1 after refresh.
- The accepted submission stayed weak after refresh, so the next slot should
  include a different archetype or guard package rather than another immediate
  repeat.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 591.6.
