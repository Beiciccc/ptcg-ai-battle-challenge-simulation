# 223 Garchomp v28 Exact Control

Date: 2026-08-05 UTC

Local generated package (not committed):
`artifacts/submissions/s223-garchomp-v28-exact-control.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192, 194, 197, 200, 204,
206, 209, 211, 213, 214, 216, 218, 219, and 221

Kaggle submission: `55254454`

Public score: 625.5

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Crustle v29](https://www.kaggle.com/code/jazivxt/crustle-counter-al220-v29-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Garchomp v28 archive as the third 2026-08-05 control.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Screened Crustle as the single exploration profile before restoring the
  mature Garchomp and Archaludon pair.

Candidate screen:
- Exact Crustle v29 completed 11-5 across Garchomp and Archaludon
- Crustle completed 8-0 against Garchomp but only 3-5 against Archaludon
- Crustle went 5-3 from seat zero and 6-2 from seat one without errors or ties
- The 3-5 Archaludon panel failed the predeclared requirement of at least four
  wins against each anchor, so the gate was not relaxed

Validation:
- Archive SHA-256 matched experiments 192, 194, 197, 200, 204, 206, 209, 211,
  213, 214, 216, 218, 219, and 221 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- The prior eight-game direct panel against Archaludon completed 5-3 without
  errors or ties using the same exact archive bytes
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55254454` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before
  moving through 498.9, 600.9, and 625.5.
- At this checkpoint, the fifteen byte-identical official rows read 961.3,
  674.6, 754.0, 684.6, 779.1, 655.0, 758.1, 917.3, 564.4, 689.6, 699.9,
  561.9, 726.7, 634.2, and 625.5.
- Score checkpoint: `2026-08-05 01:35 UTC`.
