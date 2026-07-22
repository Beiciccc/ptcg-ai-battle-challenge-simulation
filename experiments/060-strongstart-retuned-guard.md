# 060 Strongstart Retuned Guard

Date: 2026-06-30 UTC

Local generated package (not committed): `artifacts/submissions/s011-final-strongstart-retuned.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/ccffdb6e8565-fd2fc062ffc2/main.py), [deck.csv](../agent_zoo/sources/ccffdb6e8565-fd2fc062ffc2/deck.csv)

Source SHA256: main.py `ccffdb6e85658dedf21dd3f9829b97bc29a1a2a30e986f79054d86796bfdab12`; deck.csv `fd2fc062ffc23c5a4f77f30c05d2fc1d08a7bade73e1dc67e1dd547192fd46b3`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54214538`

Public score: 657.9

Status: complete

Summary:
- Re-submitted the retuned Strong Start guard package as a second decorrelated
  historical profile after the Crustle-specific guard opened weakly.
- Earlier runs of this package had reached the high guard range, while this
  rerun settled in the mid guard range after refresh.
- The final slot should prioritize a different matchup profile with prior
  official validation rather than another same-family reroll.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s011-final-strongstart-retuned.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 657.9.
