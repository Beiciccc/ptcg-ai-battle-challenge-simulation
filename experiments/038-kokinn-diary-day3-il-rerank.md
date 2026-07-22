# 038 Kokinn Diary Day3 IL Rerank

Date: 2026-06-24

Local generated package (not committed): `artifacts/submissions/s038-kokinn-diary-day3-il-rerank.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/277e535bc522-8e7519fa37f0/main.py), [deck.csv](../agent_zoo/sources/277e535bc522-8e7519fa37f0/deck.csv)

Source SHA256: main.py `277e535bc52277cfdaaa7b69abe15dc194b96085a4131b07ab7c7b22363e1347`; deck.csv `8e7519fa37f05af6960f6872e8abb28dcff12b8516977145d528036b63fa05d1`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54010287`

Public score: 619.5

Status: complete

Summary:
- Tested the public Kokinn Diary Day 3 candidate, which distills a rule-based
  teacher into a small imitation-rerank layer and keeps the heuristic fallback.
- The candidate was submitted as the first 2026-06-24 exploration slot after the
  Naoto reroll returned a weak public score.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s038-kokinn-diary-day3-il-rerank.tar.gz`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 619.5.
