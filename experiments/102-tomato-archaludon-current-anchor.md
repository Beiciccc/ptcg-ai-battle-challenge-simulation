# 102 Tomato Archaludon Current Anchor

Date: 2026-07-11 UTC

Local generated package (not committed): `artifacts/submissions/s102-tomato-archaludon-current-anchor.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/03216723e42e-42165967b565/main.py), [deck.csv](../agent_zoo/sources/03216723e42e-42165967b565/deck.csv)

Source SHA256: main.py `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`; deck.csv `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54571211`

Validation episode: `85394214`

Public score: 725.3

Status: complete

Summary:
- Re-submitted the strongest recent Tomato Archaludon package after the
  public-code refresh produced no newer evidence-backed candidate.
- Local validation passed for the archive layout, entrypoint, 60-card deck,
  and three smoke battles from the extracted root.
- Later score refreshes recovered above the initial result but moved below
  the current LLCC guard.

Validation:
- `tar -tzf artifacts/submissions/s102-tomato-archaludon-current-anchor.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- `python tools/smoke_battle.py --games 1 --max-steps 900`

Result:
- Kaggle validation episode `85394214` completed.
- Latest refreshed public score was 725.3.
