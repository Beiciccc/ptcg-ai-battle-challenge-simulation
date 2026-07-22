# 058 Naoto Hop Alakazam Guard

Date: 2026-06-30 UTC

Local generated package (not committed): `artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/635999b1a0f7-e07b796d823c/main.py), [deck.csv](../agent_zoo/sources/635999b1a0f7-e07b796d823c/deck.csv)

Source SHA256: main.py `635999b1a0f7970e70c17bb591c21b7576ddc83889ef5f50b76b8687ced5b09d`; deck.csv `e07b796d823cbbfec98ccd6a1038527321264f0357afa7f60a021cf92066e510`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54214377`

Public score: 662.2

Status: complete

Summary:
- Re-submitted the historical Naoto Hop/Alakazam target-priority guard package
  after the Archaludon metal-tempo reroll opened weakly under the updated match
  mix.
- The package had prior high-refresh results above 1000 and 800, but this rerun
  settled in the mid guard range after refresh.
- The next slot should use a different resilient guard profile rather than
  immediately rerolling this lane.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 662.2.
