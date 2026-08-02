# 209 Garchomp v28 Final Pair Exact

Date: 2026-08-02 UTC

Local generated package (not committed):
`artifacts/submissions/s209-garchomp-v28-final-pair-exact.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192, 194, 197, 200, 204,
and 206

Kaggle submission: `55174424`

Public score: 843.5

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Garchomp v28 archive as the first member of the final pair.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Submitted Garchomp before the last slot because its repeated-score path is
  more variable than the alternative mature families.

Validation:
- Archive SHA-256 matched experiments 192, 194, 197, 200, 204, and 206 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- The byte-identical archive retains non-executable AppleDouble and Python
  cache members; the official loader did not select or import them
- Eight fresh seat-alternated games against Crustle completed 2-6 without
  errors or ties, confirming the established Crustle matchup risk
- Both strategies went 1-3 against the opponent from each seat, while total
  wins split evenly between seat zero and seat one
- Maximum observed decision latency was 0.003 seconds for Garchomp and 0.002
  seconds for Crustle
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55174424` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 692.1, then moved through 794.9 and 728.3 to
  843.5.
- At this checkpoint, the seven byte-identical official rows read 961.3, 726.3,
  754.0, 684.6, 779.1, 655.0, and 843.5.
- Score checkpoint: `2026-08-02 01:27 UTC`.
