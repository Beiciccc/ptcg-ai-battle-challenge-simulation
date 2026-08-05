# 221 Garchomp v28 Exact Calibration

Date: 2026-08-05 UTC

Local generated package (not committed):
`artifacts/submissions/s221-garchomp-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 192, 194, 197, 200, 204,
206, 209, 211, 213, 214, 216, 218, and 219

Kaggle submission: `55253711`

Public score: 672.9

Status: complete

Sources:
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28-agents-only)
- [Grimmsnarl Damage Transfer Control](https://www.kaggle.com/code/tetsutani/grimmsnarl-ex-damage-transfer-control)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Garchomp v28 archive as the first 2026-08-05 calibration.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Screened two newly score-bound Grimmsnarl versions before retaining the
  mature Garchomp and Archaludon pair.

Candidate screen:
- Grimmsnarl V13 archive SHA-256
  `27747153113a87c48f7333a78cbe61f5ca4308190aa1d730581303aa9a109df3`
  was directly bound to an 846.3 public result
- Grimmsnarl V14 archive SHA-256
  `36575bed01b1b070c25f5ad519f7f9c9feebbd4f14c4ad68622be4507cd099a3`
  was directly bound to a 778.9 public result
- V14 passed archive, loader, deck, model, and Program22 checks but completed
  only 7-9 across Garchomp and Archaludon, including 1-7 against Archaludon
- The CABT environment tree and packaged Program22 runtime remained unchanged

Validation:
- Archive SHA-256 matched experiments 192, 194, 197, 200, 204, 206, 209, 211,
  213, 214, 216, 218, and 219 exactly
- Static and dynamic loader checks selected `submission_entrypoint_v28_garchomp`
- Loader-selected initialization returned the exact submitted 60-card deck
- No duplicate members, links, unsafe paths, or nested archive root
- Eight fresh seat-alternated games against Archaludon completed 5-3 without
  errors or ties
- Garchomp went 2-2 from seat zero and 3-1 from seat one; the panel recorded
  three wins from seat zero and five from seat one
- Maximum observed decision latency was 0.002 seconds for Garchomp and 0.023
  seconds for Archaludon
- Seeds were `2026080516` through `2026080523`
- Main SHA-256:
  `37a0aad5cfac56b90162b0a50ef02ad1eec9353a7e2fc9a168b6f0e66830e5eb`
- Deck SHA-256:
  `6a4da49026b58ecb3ea608afbb9222ba4b2e55bce8350519c226eec60a96fcf7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`

Result:
- Kaggle accepted the package as submission `55253711` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 734.7, then moved through 843.2, 775.7, and
  717.6 to 672.9.
- At this checkpoint, the fourteen byte-identical official rows read 961.3,
  674.6, 754.0, 684.6, 779.1, 655.0, 758.1, 917.3, 564.4, 689.6, 699.9,
  561.9, 726.7, and 672.9.
- Score checkpoint: `2026-08-05 01:05 UTC`.
