# 213 Garchomp v28 Exact Control

Date: 2026-08-03 UTC

Local generated package (not committed):
`artifacts/submissions/s213-garchomp-v28-exact-control.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192, 194, 197, 200, 204,
206, 209, and 211

Kaggle submission: `55203145`

Public score: 564.4

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Garchomp v28 archive as the third 2026-08-03 control.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Used the mature control after the newly published Grimmsnarl candidate failed
  the predeclared two-anchor validation threshold.

Validation:
- Archive SHA-256 matched experiments 192, 194, 197, 200, 204, 206, 209, and
  211 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- The byte-identical archive retains non-executable AppleDouble and Python
  cache members; the official loader did not select or import them
- Eight fresh seat-alternated games against the Grimmsnarl candidate completed
  6-2 without errors or ties
- Garchomp went 2-2 from seat zero and 4-0 from seat one; the panel recorded
  six wins from seat one and two from seat zero
- The Grimmsnarl candidate completed 7-9 across the Garchomp and Archaludon
  anchor panels and was not submitted
- Maximum observed decision latency was 0.036 seconds for Garchomp and 0.124
  seconds for Grimmsnarl
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55203145` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 506.9, then moved through 707.4, 648.9, and
  601.8 to 564.4.
- At this checkpoint, the nine byte-identical official rows read 961.3, 726.3,
  754.0, 684.6, 779.1, 655.0, 758.1, 917.3, and 506.9.
- Score checkpoint: `2026-08-03 06:04 UTC`.
