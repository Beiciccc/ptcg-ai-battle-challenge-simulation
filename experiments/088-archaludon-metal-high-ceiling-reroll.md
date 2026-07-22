# 088 Archaludon Metal High Ceiling Reroll

Date: 2026-07-08 UTC

Local generated package (not committed): `artifacts/submissions/s088-archaludon-metal-high-ceiling-reroll.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/a4c53101be30-fbe6ab599922/main.py), [deck.csv](../agent_zoo/sources/a4c53101be30-fbe6ab599922/deck.csv)

Source SHA256: main.py `a4c53101be301c181bd477204a72c0e5cba65fddd34d8cd0ec4d36e4b41c9518`; deck.csv `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54457364`

Validation episode: `84815933`

Public score: 614.2

Status: complete

Summary:
- Re-submitted the Archaludon metal high-ceiling package after experiment 085
  became the latest best result from the prior cycle.
- Latest refresh stayed below recent Archaludon guard references.
- The next slot shifts to the Tomato Archaludon guard profile for score-curve
  diversity.

Validation:
- `tar -tzf artifacts/submissions/s088-archaludon-metal-high-ceiling-reroll.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation episode `84815933` completed.
- Latest refreshed public score was 614.2.
