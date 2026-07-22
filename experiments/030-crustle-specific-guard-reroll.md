# 030 Crustle Specific Guard Reroll

Date: 2026-06-22

Local generated package (not committed): `artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/main.py), [deck.csv](../agent_zoo/sources/6de341ae762f-9c2647bd80d5/deck.csv)

Source SHA256: main.py `6de341ae762f15a7d926f5359e783e189bf25d5a0cff5ec69f78a954d0bdb6d3`; deck.csv `9c2647bd80d51bfd9cf89c74026e6a53607903b94cae9c235fad0c2128aad3aa`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `53945532`

Public score: 782.1

Status: complete

Summary:
- Re-submitted the Crustle-specific guard package as the first final latest-two
  slot after the 2026-06-22 public-code candidates and Lucario-search reroll
  started below the prior guard scores.
- The submission completed, and the refreshed public score recovered into the
  guard range.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s010-resubmit-crustle-specific.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 782.1.
