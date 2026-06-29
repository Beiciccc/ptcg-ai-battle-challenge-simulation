# 052 Pilkwang 0629 Archaludon Metal

Date: 2026-06-29 UTC

Package: `artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`

Kaggle submission: `54182720`

Public score: 600.0

Status: complete

Summary:
- Tested the 2026-06-29 public meta snapshot's Archaludon metal-tempo challenger.
- The candidate was selected because the 2026-06-28 episode data refresh and
  public meta analysis both pointed to Metal tempo as a rising pressure lane.
- The accepted submission opened weakly, so the next slot should either use the
  paired 2026-06-29 Alakazam/Dunsparce complement for diversity or return to the
  current guard packages if the score does not recover.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Initial public score was 600.0.
