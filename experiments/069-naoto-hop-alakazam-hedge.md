# 069 Naoto Hop Alakazam Hedge

Date: 2026-07-02 UTC

Package: `artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`

Kaggle submission: `54251334`

Public score: 688.0

Status: complete

Summary:
- Re-submitted the Naoto Hop/Alakazam target-priority guard as a decorrelated
  hedge after two Archaludon-family rerolls opened low.
- The hedge did not recover its historical high-scoring behavior in this
  reroll, though it refreshed above its opening score.
- The refreshed Tomato Archaludon result remains the best July 2 score so far.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s028-naoto-hop-alakazam-target.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 688.0.
