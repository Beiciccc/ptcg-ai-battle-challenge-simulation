# 058 Naoto Hop Alakazam Guard

Date: 2026-06-30 UTC

Package: `artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`

Kaggle submission: `54214377`

Public score: 759.5

Status: complete

Summary:
- Re-submitted the historical Naoto Hop/Alakazam target-priority guard package
  after the Archaludon metal-tempo reroll opened weakly under the updated match
  mix.
- The package had prior high-refresh results above 1000 and 800, and this rerun
  recovered into the current guard range after refresh.
- The next slot should use a different resilient guard profile rather than
  immediately rerolling this lane.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 759.5.
