# 216 Garchomp v28 Exact Calibration

Date: 2026-08-04 UTC

Local generated package (not committed):
`artifacts/submissions/s216-garchomp-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192, 194, 197, 200, 204,
206, 209, 211, 213, and 214

Kaggle submission: `55224851`

Public score: 699.9

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)
- [Grimmsnarl Damage Transfer Control](https://www.kaggle.com/code/tetsutani/grimmsnarl-ex-damage-transfer-control)
- [Strong Start Baseline](https://www.kaggle.com/code/romanrozen/strong-start-baseline-agent-v10-lb-950)
- [1084.5 Baseline](https://www.kaggle.com/code/makthanithin/pokemon-tcg-ai-battle-1084-5-baseline)

Summary:
- Re-ran the exact Garchomp v28 archive as the first 2026-08-04 calibration.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Screened three refreshed public outputs before retaining the mature exact
  Garchomp profile.

Candidate screen:
- The refreshed Strong Start output was byte-equivalent at the policy and deck
  level to the previously tested Sol Eclipse Alakazam strategy
- The refreshed 1084.5 output retained the previously observed Maktha policy
  and deck, while its current linked public result did not support the title
- The updated Grimmsnarl archive used new policy and model bytes, but completed
  only 1-15 across fresh Garchomp and Archaludon anchor panels
- The competition data refresh corrected English card text while the game
  engine and packaged Program22 runtime remained unchanged

Validation:
- Archive SHA-256 matched experiments 192, 194, 197, 200, 204, 206, 209, 211,
  213, and 214 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- Eight fresh seat-alternated games against Archaludon completed 5-3 without
  errors or ties
- Garchomp went 3-1 from seat zero and 2-2 from seat one; the panel recorded
  five wins from seat zero and three from seat one
- Maximum observed decision latency was 0.004 seconds for Garchomp and 0.025
  seconds for Archaludon
- Seeds were `2026080416` through `2026080423`
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55224851` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 708.4, then moved through 610.2 and 721.9 to
  769.0 and 699.9.
- At this checkpoint, the eleven byte-identical official rows read 961.3,
  674.6, 754.0, 684.6, 779.1, 655.0, 758.1, 917.3, 564.4, 689.6, and 699.9.
- Score checkpoint: `2026-08-04 01:00 UTC`.
