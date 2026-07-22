# 049 Pilkwang 0628 Metal Tempo

Date: 2026-06-28 UTC

Local generated package (not committed): `artifacts/submissions/s047-pilkwang-0628-metal-tempo.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/a4c53101be30-42165967b565/main.py), [deck.csv](../agent_zoo/sources/a4c53101be30-42165967b565/deck.csv)

Source SHA256: main.py `a4c53101be301c181bd477204a72c0e5cba65fddd34d8cd0ec4d36e4b41c9518`; deck.csv `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54152832`

Public score: 738.0

Status: complete

Summary:
- Tested the 2026-06-28 public meta snapshot's Metal tempo pressure profile.
- The candidate was chosen because public field notes highlighted Archaludon and
  metal tempo as a strong conversion lane against the visible meta.
- The accepted submission recovered after refresh and became the third-best
  result in this five-submission batch.

Validation:
- `python tools/check_submission_entrypoint.py $TEMP_DIR/main.py`
- `python tools/check_deck.py $TEMP_DIR/deck.csv`
- `tar -tzf artifacts/submissions/s047-pilkwang-0628-metal-tempo.tar.gz`
- `PYTHONPATH=src pytest -q -p no:cacheprovider`

Result:
- Kaggle validation completed.
- Latest refreshed public score was 738.0.
