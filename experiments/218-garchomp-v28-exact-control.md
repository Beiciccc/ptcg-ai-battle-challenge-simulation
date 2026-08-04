# 218 Garchomp v28 Exact Control

Date: 2026-08-04 UTC

Local generated package (not committed):
`artifacts/submissions/s218-garchomp-v28-exact-control.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192, 194, 197, 200, 204,
206, 209, 211, 213, 214, and 216

Kaggle submission: `55225217`

Public score: 473.4

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Garchomp v28 archive as the third 2026-08-04 control.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Rejected a proposed Steel exploration after its fresh matchup result failed
  to support the submission.

Validation:
- Archive SHA-256 matched experiments 192, 194, 197, 200, 204, 206, 209, 211,
  213, 214, and 216 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- Eight fresh seat-alternated games against search-disabled Steel completed
  6-2 for Garchomp without errors or ties
- Garchomp went 3-1 from both seat zero and seat one; the panel split its wins
  evenly between the two seats
- Maximum observed decision latency was 0.001 seconds for both strategies
- Seeds were `2026080432` through `2026080439`
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55225217` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 473.4.
- At this checkpoint, the twelve byte-identical official rows read 961.3,
  674.6, 754.0, 684.6, 779.1, 655.0, 758.1, 917.3, 564.4, 689.6, 699.9,
  and 473.4.
- Score checkpoint: `2026-08-04 01:00 UTC`.
