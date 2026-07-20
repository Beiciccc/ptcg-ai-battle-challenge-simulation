# 147 Fishcat V9 Attention All3D Code Probe

Date: 2026-07-20 UTC

Package: `artifacts/submissions/s147-fishcat-v9-attention-all3d-exact-code-output.tar.gz`

Kaggle submission: `54843697`

Public score: 726.8

Status: complete

Source:
- [PTCG V9 Attention All3D End-to-End](https://www.kaggle.com/code/fishcat37/ptcg-v9-attention-all3d-end-to-end)

Summary:
- Tested the exact runnable archive published by the V9 Attention All3D Code
  notebook as a new policy-family probe.
- The package contains a compact behavior-cloning checkpoint and CPU inference
  path trained by the source notebook from its published episode dataset.
- Preserved the Code output archive byte-for-byte so the public result is tied
  to the published artifact rather than a local rebuild.

Validation:
- Exact-byte copy of the published `v9_output/submission.tar.gz`
- Clean 13-file archive root with `main.py`, `deck.csv`, `model.pt`,
  `bc_agent.py`, and nine runtime files
- No links, AppleDouble files, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Three isolated extracted-archive smoke battles completed in 45, 82, and 130
  steps against the packaged runtime
- Packaged engine binaries match the current competition sample
- Main SHA-256: `be26faf23c05ab4cca7bf0b2fd41416a9f3b65317ffecaf88e8692cbd6fae977`
- Deck SHA-256: `b4464eb525a25e6598a972d00efc5e5b5156372e77f51853f4076d8ebb34fd7d`
- Model SHA-256: `daa17631615ef0cbb7c640e02c6c0dc6e4042d624d27fd77b3ca98f1970e7659`
- Archive SHA-256: `526b26dea80c1607bc92430ff6695308709282d2a823fdbbeaaea81364475834`

Result:
- Kaggle accepted the package and marked submission `54843697` complete.
- Public evaluation moved through 600.0, 766.9, and 791.4 before reaching
  726.8 as validation battles accumulated.
- Score checkpoint: `2026-07-20 03:44 UTC`.
