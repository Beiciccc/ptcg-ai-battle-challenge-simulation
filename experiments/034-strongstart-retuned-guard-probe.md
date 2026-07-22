# 034 Strongstart Retuned Guard Probe

Date: 2026-06-23

Local generated package (not committed): `artifacts/submissions/s011-final-strongstart-retuned.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/ccffdb6e8565-fd2fc062ffc2/main.py), [deck.csv](../agent_zoo/sources/ccffdb6e8565-fd2fc062ffc2/deck.csv)

Source SHA256: main.py `ccffdb6e85658dedf21dd3f9829b97bc29a1a2a30e986f79054d86796bfdab12`; deck.csv `fd2fc062ffc23c5a4f77f30c05d2fc1d08a7bade73e1dc67e1dd547192fd46b3`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53961368`

Public score: 686.7

Status: complete

Summary:
- Re-submitted the retuned Strong Start guard package as an upside probe after
  the Naoto and Lucario-search rerolls.
- The submission completed, and the refreshed public score recovered but stayed
  below the Naoto reroll.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s011-final-strongstart-retuned.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 686.7.
