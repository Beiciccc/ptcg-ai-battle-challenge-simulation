# 241 Archaludon v28 Exact Fallback

Date: 2026-08-11 UTC

Local generated package (not committed):
`artifacts/submissions/s238-archaludon-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: exact current-runtime fallback after a fresh Sol v22 panel

Kaggle submission: `55421203`

Public score: 700.0

Status: complete

Sources:
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Garchomp v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-entryfix)
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-tested the exact Sol v22 package against current exact Garchomp and
  Archaludon anchors with a new 16-game fixed panel.
- Sol completed 1-7 against Garchomp and 4-4 against Archaludon, finishing
  5-11 overall and failing the declared gates.
- The fixed Archaludon fallback was submitted without changing its policy,
  deck, runtime, loader entrypoint, or archive bytes.

Public refresh:
- No new external Code, Discussion, rules, evaluation, data, or runtime
  change established a distinct actionable candidate before the panel was
  fixed.
- Older Tien/Mega Lucario proposals were excluded because their exact current
  archive identity and runtime evidence were not available in the repository.

Candidate screen:
- Sol archive SHA-256: `78dde4d68910a7c841a4c989a7e39fe8ae4ec15b0ba278f28b7ba43cdec5476b`.
- Garchomp archive SHA-256: `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`.
- Archaludon archive SHA-256: `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`.
- The panel used seeds `2026081150` through `2026081165`, alternating the
  candidate seat on even and odd seeds.
- Sol completed 1-7 against Garchomp and 4-4 against Archaludon, with no
  errors or draws. Its maximum observed decision latency was below one second.
- The fixed gate required at least 11-5 overall, at least 5-3 against each
  anchor, at least 2-2 from every anchor-seat cell, and at least 5-3 from each
  candidate seat overall. Sol failed the aggregate and anchor gates.

Validation:
- The submitted fallback archive passed the required entrypoint, 60-card
  deck, current Linux runtime, safe-member, duplicate-member, and link checks.
- Main SHA-256: `085f399dadf5e15d0e89c13ad4288e22a727514a5b95f538877eb804f970962e`.
- Deck SHA-256: `bb3d2c7167975be58701bb5b74b88d83c8eb6510b829b7a73219cafa14ad1ed7`.
- Linux runtime SHA-256: `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`.
- Archive SHA-256: `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`.

Result:
- Kaggle accepted the fallback as submission `55421203` and marked it
  complete. The official row was the only new row after the quota check.
- Public evaluation moved from the 600.0 initialization baseline to 700.0.
- Score checkpoint: `2026-08-11 02:44 UTC`.
