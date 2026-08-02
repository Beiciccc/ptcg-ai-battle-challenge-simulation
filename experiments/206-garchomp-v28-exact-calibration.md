# 206 Garchomp v28 Exact Calibration

Date: 2026-08-02 UTC

Local generated package (not committed):
`artifacts/submissions/s206-garchomp-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192, 194, 197, 200, and 204

Kaggle submission: `55173906`

Public score: 655.0

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Garchomp v28 archive as the first 2026-08-02 calibration.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Retained the established Garchomp and Archaludon frontier because the new
  public archives lacked direct archive-to-score evidence.

Validation:
- Archive SHA-256 matched experiments 192, 194, 197, 200, and 204 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- The byte-identical archive retains non-executable AppleDouble and Python
  cache members; the official loader did not select or import them
- Eight fresh seat-alternated games against Archaludon completed 7-1 without
  errors or ties
- Garchomp went 3-1 from seat zero and 4-0 from seat one; the panel recorded
  five wins from seat one and three from seat zero
- Maximum observed decision latency was 0.002 seconds for Garchomp and 0.027
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
- Kaggle accepted the package as submission `55173906` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 726.2, then moved through 829.9, 735.5, and
  722.3 to 655.0.
- At this checkpoint, the six byte-identical official rows read 961.3, 726.3,
  754.0, 684.6, 779.1, and 655.0.
- The latest two submissions preserve Archaludon and Garchomp as distinct
  complementary strategy families.
- Score checkpoint: `2026-08-02 01:27 UTC`.
