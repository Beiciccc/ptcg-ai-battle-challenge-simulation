# 024 Alakazam Psychic Control

Date: 2026-06-21

Package: `artifacts/submissions/s024-alakazam-psychic-control.tar.gz`

Kaggle submission: `53907175`

Public score: 713.2

Status: complete

Summary:
- Tested a public Alakazam psychic-control candidate after the latest public
  code and discussion scan suggested that control-style decks were becoming
  more relevant than older Lucario-only baselines.
- The candidate validated successfully and recovered after the initial score,
  but did not improve over the strongest guard candidate in this batch.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `python tools/package_submission.py --source $TEMP_DIR --name s024-alakazam-psychic-control`
- `tar -tzf artifacts/submissions/s024-alakazam-psychic-control.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 713.2.
