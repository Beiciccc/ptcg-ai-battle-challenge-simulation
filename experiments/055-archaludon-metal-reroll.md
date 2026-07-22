# 055 Archaludon Metal Reroll

Date: 2026-06-29 UTC

Local generated package (not committed): `artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/a4c53101be30-fbe6ab599922/main.py), [deck.csv](../agent_zoo/sources/a4c53101be30-fbe6ab599922/deck.csv)

Source SHA256: main.py `a4c53101be301c181bd477204a72c0e5cba65fddd34d8cd0ec4d36e4b41c9518`; deck.csv `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54182907`

Public score: 1030.6

Status: complete

Summary:
- Re-submitted the 2026-06-29 Archaludon metal-tempo challenger after experiment
  052 refreshed to 813.1.
- The reroll tested whether the new Metal tempo lane could reproduce a high
  public score under the current live pool.
- The accepted submission recovered strongly after refresh and became the best
  observed result so far.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 1030.6.
