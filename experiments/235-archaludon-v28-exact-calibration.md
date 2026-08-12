# 235 Archaludon v28 Exact Calibration

Date: 2026-08-09 UTC

Local generated package (not committed):
`artifacts/submissions/s235-archaludon-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiment 228 and its established
Archaludon lineage

Kaggle submission: `55368546`

Public score: 693.5

Status: complete

Sources:
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Crustle Counter v29](https://www.kaggle.com/code/jazivxt/crustle-counter-al220-v29-agents-only)
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [kaggle-environments 1.32.6](https://github.com/Kaggle/kaggle-environments/commit/bded87b0d7879078c726a93a4884d044f79c4eed)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Archaludon Metal v28 archive after exact Crustle failed a
  fixed panel against Sol and Steel.
- Preserved the published policy, 60-card deck, loader entrypoint, current
  runtime, and archive bytes.
- Retained Archaludon as the predeclared fallback without changing any gate
  after observing the results.

Public refresh:
- No new public Code output established a distinct executable candidate after
  experiment 234.
- The latest score-band notebook remained in progress with only older
  aggregate output, while the public PPO archive remained random initialized
  and lacked byte-level score binding.
- Discussion, Rules, Evaluation, competition data, and the CABT runtime
  supplied no material change before the panel was fixed.

Candidate screen:
- Crustle archive SHA-256 was
  `c342491c38afe44941efb366dbb212825381f3de64b286170029f7db1e795a16`.
- The fixed panel used seeds `2026080932` through `2026080947`, with Crustle
  in seat zero on even seeds and seat one on odd seeds.
- Crustle completed 6-2 against Sol and 2-6 against Steel, for 8-8 overall.
- Against Sol, Crustle went 2-2 from seat zero and 4-0 from seat one.
- Against Steel, Crustle went 1-3 from each seat.
- Across both anchors, Crustle went 3-5 from seat zero and 5-3 from seat one.
- All sixteen games completed on their first execution without errors, ties,
  timeouts, invalid actions, random fallbacks, or retries.
- Maximum Crustle decision latency was 0.001 seconds, and the global maximum
  was 0.238 seconds.
- The fixed gate required at least 11-5 overall, at least 5-3 against each
  anchor, at least 2-2 from every anchor and candidate-seat cell, and at least
  5-3 from each candidate seat overall.
- Crustle failed the aggregate, Steel, both Steel-seat-cell, and overall
  seat-zero gates, so the exact Archaludon fallback was retained.

Validation:
- Archive SHA-256 matched experiment 228 and the established Archaludon
  lineage exactly.
- Official resolver keys were `_v29_original_agent`,
  `codex_sol_eclipse_alakazam_v22`, `agent`, and `_v28_original_agent`.
- Loader-selected initialization returned each exact submitted 60-card deck.
- Clean root archive with `main.py`, `deck.csv`, published helper files, and
  the full current runtime.
- No duplicate members, links, unsafe paths, or nested archive root.
- Main SHA-256:
  `085f399dadf5e15d0e89c13ad4288e22a727514a5b95f538877eb804f970962e`
- Deck SHA-256:
  `bb3d2c7167975be58701bb5b74b88d83c8eb6510b829b7a73219cafa14ad1ed7`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`

Result:
- Kaggle accepted the package as submission `55368546` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 693.5.
- Score checkpoint: `2026-08-09 05:08 UTC`.
