# 211 Garchomp v28 Exact Calibration

Date: 2026-08-03 UTC

Local generated package (not committed):
`artifacts/submissions/s211-garchomp-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192, 194, 197, 200, 204,
206, and 209

Kaggle submission: `55202725`

Public score: 862.4

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Garchomp v28 archive as the first 2026-08-03 calibration.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Kept the mature exact frontier because the new Grimmsnarl archive lacked a
  direct binding between its current bytes and the displayed score.

Validation:
- Archive SHA-256 matched experiments 192, 194, 197, 200, 204, 206, and 209
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- The byte-identical archive retains non-executable AppleDouble and Python
  cache members; the official loader did not select or import them
- Eight fresh seat-alternated games against Steel completed 5-3 without errors
  or ties
- Garchomp went 2-2 from seat zero and 3-1 from seat one; the panel recorded
  five wins from seat one and three from seat zero
- Maximum observed decision latency was 0.004 seconds for Garchomp and 0.003
  seconds for Steel
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55202725` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 659.7, then moved through 717.0 and 797.4 to
  862.4.
- At this checkpoint, the eight byte-identical official rows read 961.3, 726.3,
  754.0, 684.6, 779.1, 655.0, 758.1, and 862.4.
- Score checkpoint: `2026-08-03 05:20 UTC`.
