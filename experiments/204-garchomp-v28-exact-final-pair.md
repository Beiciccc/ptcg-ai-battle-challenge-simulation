# 204 Garchomp v28 Exact Final Pair

Date: 2026-08-01 UTC

Local generated package (not committed):
`artifacts/submissions/s204-garchomp-v28-exact-final-pair.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192, 194, 197, and 200

Kaggle submission: `55154791`

Public score: 779.1

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Garchomp v28 archive as the first member of the final
  Garchomp and Archaludon pair.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Selected Garchomp for its repeated official observations and complementary
  matchup coverage with Archaludon.

Validation:
- Archive SHA-256 matched experiments 192, 194, 197, and 200 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- The byte-identical archive retains non-executable AppleDouble and Python
  cache members; the official loader did not select or import them
- The prior 48-game anchor panel completed 32-16 without errors
- Eight fresh seat-alternated games against Archaludon completed 6-2 without
  errors, ties, or material seat bias
- Maximum observed decision latency was 0.018 seconds for Garchomp and 0.045
  seconds for Archaludon
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55154791` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before
  moving through 722.6, 758.9, 895.5, and 939.7 before reaching 779.1.
- At this checkpoint, the five byte-identical official rows read 961.3, 726.3,
  754.0, 684.6, and 779.1.
- The latest two submissions preserve Archaludon and Garchomp as distinct
  strategy families.
- Score checkpoint: `2026-08-02 01:15 UTC`.
