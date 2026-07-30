# 194 Garchomp v28 Exact Replication

Date: 2026-07-30 UTC

Local generated package (not committed):
`artifacts/submissions/s194-garchomp-v28-exact-replication.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiment 192

Kaggle submission: `55098359`

Public score: 676.0

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact experiment 192 Garchomp v28 entry-fixed archive after its
  independent public evaluation exceeded 950.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Used the independent result to measure public-path variance before selecting
  the final active pair.

Validation:
- Archive SHA-256 matched experiment 192 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- The prior 48-game anchor panel completed 32-16 without errors
- Twenty-four fresh extended-panel games completed without errors
- Extended results: 4-4 against Rising Tide Alakazam, 6-2 against Archaludon
  v28, and 1-7 against Crustle v29
- The Crustle result identified a material counter risk and supported a
  complementary final strategy family
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Windows runtime SHA-256:
  `eae88634e26dc31d94150a4d8202fc9d32596b8c688ef67e14cb4088cd4d5771`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Linux ARM64 runtime SHA-256:
  `1670740b73fab46586fd25c0a1f96608ea75b1f39381d66a0b8d9486bea6d4a2`
- macOS runtime SHA-256:
  `7a157f045d333f99d1996d49c12bdbdd148072a619af246385c7295518776e30`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55098359` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline to 676.0.
- The byte-identical experiments 192 and 194 reached 961.3 and 676.0 at the
  same checkpoint, confirming substantial early rating variance.
- Score checkpoint: `2026-07-30 03:35 UTC`.
