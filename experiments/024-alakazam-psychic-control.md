# 024 Alakazam Psychic Control

Date: 2026-06-21

Local generated package (not committed): `artifacts/submissions/s024-alakazam-psychic-control.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/df4d597f5939-7b413177e507/main.py), [deck.csv](../agent_zoo/sources/df4d597f5939-7b413177e507/deck.csv)

Source SHA256: main.py `df4d597f593950b0d0c372f3e0bb26c182c4116648977f15adbb329a6ba922f4`; deck.csv `7b413177e5077777f2178143839c0155b03b92bbc8b3a6607621a7d43f351141`

Reproducibility: exact source snapshot; Kaggle runtime required

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
