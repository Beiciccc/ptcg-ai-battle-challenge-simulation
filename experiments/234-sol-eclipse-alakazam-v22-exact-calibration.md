# 234 Sol Eclipse Alakazam v22 Exact Calibration

Date: 2026-08-09 UTC

Local generated package (not committed):
`artifacts/submissions/s234-sol-eclipse-alakazam-v22-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 193, 230, and 232

Kaggle submission: `55368172`

Public score: 721.5

Status: complete

Sources:
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28)
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [PTGC Game](https://www.kaggle.com/code/siddharajkulkarni/ptgc-game)
- [kaggle-environments 1.32.6](https://github.com/Kaggle/kaggle-environments/commit/bded87b0d7879078c726a93a4884d044f79c4eed)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Sol Eclipse Alakazam v22 archive after it passed a new
  fixed panel against Garchomp and Archaludon.
- Preserved the published policy, 60-card deck, loader entrypoint, current
  runtime, and archive bytes.
- Kept Sol as a distinct strategy family after the preceding Steel result.

Public refresh:
- PTGC Game v63 produced a valid root archive and a strongly time-associated
  public result, but instantiated an untrained random-weight PPO network and
  supplied no byte-level submission binding.
- The latest score-band notebook remained in progress with only older
  aggregate outputs and no submission archive.
- Discussion, Rules, Evaluation, competition data, and CABT supplied no other
  material change after experiment 233.

Candidate screen:
- Sol archive SHA-256 was
  `78dde4d68910a7c841a4c989a7e39fe8ae4ec15b0ba278f28b7ba43cdec5476b`.
- The fixed panel used seeds `2026080916` through `2026080931`, with Sol in
  seat zero on even seeds and seat one on odd seeds.
- Sol completed 5-3 against Garchomp and 7-1 against Archaludon, for 12-4
  overall.
- Against Garchomp, Sol went 2-2 from seat zero and 3-1 from seat one.
- Against Archaludon, Sol went 4-0 from seat zero and 3-1 from seat one.
- Across both anchors, Sol went 6-2 from seat zero and 6-2 from seat one.
- All sixteen games completed on their first execution without errors, ties,
  timeouts, invalid actions, random fallbacks, or retries.
- Maximum Sol decision latency was 0.358 seconds, and the global maximum was
  also 0.358 seconds.
- The fixed gate required at least 11-5 overall, at least 5-3 against each
  anchor, at least 2-2 from every anchor and candidate-seat cell, and at least
  5-3 from each candidate seat overall; Sol passed every gate.

Validation:
- Archive SHA-256 matched experiments 193, 230, and 232 exactly.
- Official resolver keys were `codex_sol_eclipse_alakazam_v22`,
  `submission_entrypoint_v28_garchomp`, and `_v28_original_agent`.
- Loader-selected initialization returned each exact submitted 60-card deck.
- Clean root archive with `main.py`, `deck.csv`, published metadata, and the
  full current runtime.
- No duplicate members, links, unsafe paths, or nested archive root.
- Main SHA-256:
  `f31eba2e819ee2b3d46765b4195ea7dab8f32d0b5d09cafd39b3823661f6b5aa`
- Deck SHA-256:
  `8eccc69c3bf7d499f38c6116c33c5fac837050bf0ec71a5a1883f0f20f41ddbc`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `78dde4d68910a7c841a4c989a7e39fe8ae4ec15b0ba278f28b7ba43cdec5476b`

Result:
- Kaggle accepted the package as submission `55368172` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 721.5.
- Score checkpoint: `2026-08-09 04:52 UTC`.
