# 023 Crustle Specific High Diversity Reroll

Date: 2026-06-21

Local generated package (not committed): `artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/main.py), [deck.csv](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/deck.csv)

Source SHA256: main.py `6de341ae762f15a7d926f5359e783e189bf25d5a0cff5ec69f78a954d0bdb6d3`; deck.csv `9c2647bd80d51bfd9cf89c74026e6a53607903b94cae9c235fad0c2128aad3aa`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53907042`

Public score: 828.6

Status: complete

Summary:
- Re-submitted the historical Crustle-specific policy and wall deck package as
  a high-diversity repair slot after the first 2026-06-21 guard reroll scored
  weakly.
- The submission completed, and the refreshed public score recovered strongly
  from the initial result but stayed below the historical best run.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`
- `tar -tzf artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 828.6.
