# 057 Archaludon Metal Guard

Date: 2026-06-30 UTC

Local generated package (not committed): `artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/a4c53101be30-fbe6ab599922/main.py), [deck.csv](../agent_zoo/sources/a4c53101be30-fbe6ab599922/deck.csv)

Source SHA256: main.py `a4c53101be301c181bd477204a72c0e5cba65fddd34d8cd0ec4d36e4b41c9518`; deck.csv `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54214287`

Public score: 677.2

Status: complete

Summary:
- Re-submitted the Archaludon metal-tempo package after experiment 055 refreshed
  above 1000.
- The package remains the strongest observed public result so far, with prior
  runs at 1030.6 and 813.1.
- The accepted submission stayed below the strongest prior Archaludon results,
  so the next slot diversified with a historical high-ceiling guard package
  before deciding whether to reroll this lane again.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s052-pilkwang-0629-archaludon-metal.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 677.2.
