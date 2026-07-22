# 116 Tomato Archaludon Final Active

Date: 2026-07-13 UTC

Local generated package (not committed): `artifacts/submissions/s116-tomato-archaludon-final-active.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/03216723e42e-42165967b565/main.py), [deck.csv](../agent_zoo/sources/03216723e42e-42165967b565/deck.csv)

Source SHA256: main.py `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`; deck.csv `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54626933`

Validation episode: `85660609`

Public score: 840.9

Status: complete

Summary:
- Re-submitted the validated Tomato Archaludon package as the second final
  active profile after the current-day probe rose above 900.
- Local validation passed for the nine-file archive layout, entrypoint,
  60-card deck, and three smoke battles. The Linux archive remained unchanged
  while local engine compatibility was used for macOS smoke validation.
- Mature score refreshes recovered into the high guard range and completed the
  Stable LLCC plus Tomato pair.

Validation:
- `tar -tzf artifacts/submissions/s116-tomato-archaludon-final-active.tar.gz`
- `python tools/check_submission_entrypoint.py`
- `python tools/check_deck.py`
- Three seeded smoke battles using the matching local engine binary
- Archive SHA-256 matched experiment 110: `e7e1e346054f6d482e1b890b8a67eb68fd7bc167a6a5642bbe516287c2eb2486`

Result:
- Kaggle validation episode `85660609` completed.
- Mature public score was 840.9.
