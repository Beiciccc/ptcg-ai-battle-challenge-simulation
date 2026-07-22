# 114 Tomato Archaludon Current Probe

Date: 2026-07-13 UTC

Local generated package (not committed): `artifacts/submissions/s114-tomato-archaludon-current-probe.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/03216723e42e-42165967b565/main.py), [deck.csv](../agent_zoo/sources/03216723e42e-42165967b565/deck.csv)

Source SHA256: main.py `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`; deck.csv `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54626692`

Validation episode: `85659212`

Public score: 910.9

Status: complete

Summary:
- Re-submitted the validated Tomato Archaludon package as the third
  current-day probe.
- Local validation passed for the nine-file archive layout, entrypoint,
  60-card deck, and three smoke battles from the extracted root.
- Later score refreshes rose above 900 and led the current-day comparison.

Validation:
- `tar -tzf artifacts/submissions/s114-tomato-archaludon-current-probe.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85659212` completed.
- Latest refreshed public score was 910.9.
