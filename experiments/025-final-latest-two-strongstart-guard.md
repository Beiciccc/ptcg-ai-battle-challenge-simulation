# 025 Final Latest-Two Strongstart Guard

Date: 2026-06-21

Local generated package (not committed): `artifacts/submissions/s011-final-strongstart-retuned.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/ccffdb6e8565-fd2fc062ffc2/main.py), [deck.csv](../agent_zoo/sources/ccffdb6e8565-fd2fc062ffc2/deck.csv)

Source SHA256: main.py `ccffdb6e85658dedf21dd3f9829b97bc29a1a2a30e986f79054d86796bfdab12`; deck.csv `fd2fc062ffc23c5a4f77f30c05d2fc1d08a7bade73e1dc67e1dd547192fd46b3`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53907297`

Public score: 778.0

Status: complete

Summary:
- Re-submitted the retuned Strong Start guard package as the first final
  latest-two slot after the Alakazam exploration did not improve the public
  result.
- The submission completed, and the refreshed public score recovered from the
  initial result.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `tar -tzf artifacts/submissions/s011-final-strongstart-retuned.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 778.0.
