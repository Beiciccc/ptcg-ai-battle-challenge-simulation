# 219 Garchomp v28 Final Pair Exact

Date: 2026-08-04 UTC

Local generated package (not committed):
`artifacts/submissions/s219-garchomp-v28-final-pair-exact.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192, 194, 197, 200, 204,
206, 209, 211, 213, 214, 216, and 218

Kaggle submission: `55225333`

Public score: 711.6

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Garchomp v28 archive as the first member of the final pair.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Kept the mature Garchomp profile after experiment 218 recovered from its
  first low public reading.

Validation:
- Archive SHA-256 matched experiments 192, 194, 197, 200, 204, 206, 209, 211,
  213, 214, 216, and 218 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- Eight fresh seat-alternated games against Archaludon split 4-4 without errors
  or ties
- Garchomp went 2-2 from both seat zero and seat one; the panel recorded four
  wins from each seat
- Maximum observed decision latency was 0.002 seconds for Garchomp and 0.022
  seconds for Archaludon
- Seeds were `2026080440` through `2026080447`
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55225333` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 711.6.
- At this checkpoint, the thirteen byte-identical official rows read 961.3,
  674.6, 754.0, 684.6, 779.1, 655.0, 758.1, 917.3, 564.4, 689.6, 699.9,
  684.9, and 711.6.
- Score checkpoint: `2026-08-04 01:09 UTC`.
