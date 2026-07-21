# 152 Roman V10 Current Code Probe

Date: 2026-07-21 UTC

Package: `artifacts/submissions/s152-roman-v10-current-code-probe.tar.gz`

Kaggle submission: `54865427`

Public score: 447.0

Status: complete

Source:
- [Strong Start Baseline Agent V10](https://www.kaggle.com/code/romanrozen/strong-start-baseline-agent-v10-lb-950)

Summary:
- Tested the exact runnable archive published by the current Roman V10 Code
  version as a new strategy-family probe.
- The policy combines Mega Lucario with Hariyama, Lunatone, and Solrock and
  includes a bounded search route plus a Crustle-oriented Hariyama branch.
- Preserved every published archive byte so the public result is tied to the
  source artifact rather than a local rebuild.

Validation:
- Exact-byte copy of the published `submission.tar.gz`
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Final top-level function: `agent`
- 60-card deck check
- Six isolated extracted-archive smoke battles completed in 157, 156, 137,
  152, 144, and 141 steps
- Two-orientation comparisons completed without runtime errors: 1-7 against
  experiment 150 and 2-6 against experiment 151
- Packaged engine binaries match the current competition sample
- Main SHA-256: `a81eab3eb761af95da2ddf70a67d6078897a2cd698dae4a7b6ea92de070fad2b`
- Deck SHA-256: `2a541d7bf3d9e6b36037123f53f4dfef6348223f79fd27095dafc602a5357c19`
- Archive SHA-256: `957f9773b0f459409a15bb1062bddf05c378093a9b8a0a09e4b9341128514731`

Result:
- Kaggle accepted the package and marked submission `54865427` complete.
- Public evaluation moved from the 600.0 baseline to 498.5 and then 447.0; the
  source notebook title is not treated as independently verified leaderboard
  evidence.
- Score checkpoint: `2026-07-21 01:17 UTC`.
