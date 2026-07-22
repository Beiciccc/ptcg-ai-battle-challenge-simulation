# 128 Tomato Archaludon Current Anchor

Date: 2026-07-16 UTC

Local generated package (not committed): `artifacts/submissions/s128-tomato-archaludon-current-anchor.tar.gz`

Source commit: [f46b15b](https://github.com/Beiciccc/ptcg-ai-battle-challenge-simulation/commit/f46b15bfa6d2ab5eb2de3996d84837ea38a08cd0)

Source files: [main.py](../agent_zoo/sources/03216723e42e-42165967b565/main.py), [deck.csv](../agent_zoo/sources/03216723e42e-42165967b565/deck.csv)

Source SHA256: main.py `03216723e42e8dffa67a5ded172f23512a3f1f0540205cc815e8fd90dd3a3313`; deck.csv `42165967b565dd42ec426ecccfe79bfa7d72aa8306590e149dface0ee8bd530e`

Reproducibility: exact source snapshot; Kaggle runtime required

Kaggle submission: `54748778`

Validation episode: `86203346`

Public score: 618.2

Status: complete

Summary:
- Re-submitted Tomato Archaludon as the second current-day strategy family
  after the Alakazam anchor showed substantial score movement.
- The archive bytes matched experiments 114, 116, 118, 120, 123, and 126
  exactly.
- The validation episode completed, and repeated public score refreshes
  demonstrated substantial validation variance.

Validation:
- Clean nine-file archive with `main.py`, `deck.csv`, and seven runtime files
- Final top-level function: `agent`
- 60-card deck check
- Three seeded smoke battles completed in 152, 124, and 154 steps
- Maximum observed main-decision wall time: 0.001 seconds
- Archive SHA-256: `e7e1e346054f6d482e1b890b8a67eb68fd7bc167a6a5642bbe516287c2eb2486`

Result:
- Kaggle validation episode `86203346` completed.
- Current public score is 618.2.
