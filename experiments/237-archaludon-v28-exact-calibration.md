# 237 Archaludon v28 Exact Calibration

Date: 2026-08-09 UTC

Local generated package (not committed):
`artifacts/submissions/s237-archaludon-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 228 and 235 and their
established Archaludon lineage

Kaggle submission: `55369101`

Public score: 691.1

Status: complete

Sources:
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Grimmsnarl V16](https://www.kaggle.com/code/tetsutani/grimmsnarl-ex-damage-transfer-control?scriptVersionId=340409708)
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28)
- [Leaderboard deck meta](https://www.kaggle.com/code/myso1987/ptcg-ai-battle-leaderboard-deck-meta-by-score-band)
- [kaggle-environments 1.32.6](https://github.com/Kaggle/kaggle-environments/commit/bded87b0d7879078c726a93a4884d044f79c4eed)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Archaludon Metal v28 archive after score-bound Grimmsnarl
  v16 failed a fixed panel against Sol and Garchomp.
- Preserved every strategy, deck, helper, weight, runtime, and archive byte.
- Retained the predeclared Archaludon fallback without using aggregate deck
  popularity or moving public scores to alter the decision.

Public refresh:
- The completed score-band analysis reported Grimmsnarl as 19.58% of its
  aggregate sample and 45.8% of the 900-999 band, supporting a direct test of
  the exact score-bound Grimmsnarl candidate rather than automatic selection.
- The notebook remained at v28 and released no strategy archive, full deck,
  or submission mapping.
- PTGC Game remained at v63 with its previously audited random initialized PPO
  archive and no newer Code output.
- No newer Code archive, Discussion update, rule, evaluation, data, or CABT
  runtime change appeared before the panel was fixed.

Candidate screen:
- Grimmsnarl v16 archive SHA-256 was
  `46bb3180e7b15e41aff60f52b18300aad1ca65d1840464d15e4d30fcac9b57ba`.
- Its published output was bound to completed submission `55275925` and a
  773.2 public-score checkpoint.
- The fixed panel used seeds `2026080964` through `2026080979`, with
  Grimmsnarl in seat zero on even seeds and seat one on odd seeds.
- Grimmsnarl completed 3-5 against Sol and 4-4 against Garchomp, for 7-9
  overall.
- Against Sol, Grimmsnarl went 1-3 from seat zero and 2-2 from seat one.
- Against Garchomp, Grimmsnarl went 3-1 from seat zero and 1-3 from seat one.
- Across both anchors, Grimmsnarl went 4-4 from seat zero and 3-5 from seat
  one.
- All sixteen games completed on their first execution without errors, ties,
  timeouts, invalid actions, random fallbacks, or retries.
- Maximum Grimmsnarl decision latency was 0.248 seconds, and the global maximum
  was 0.861 seconds.
- The fixed gate required at least 11-5 overall, at least 5-3 against each
  anchor, at least 2-2 from every anchor and candidate-seat cell, and at least
  5-3 from each candidate seat overall.
- Grimmsnarl failed the aggregate, both anchor, two anchor-seat-cell, and both
  overall-seat gates, so the exact Archaludon fallback was retained.

Validation:
- Archive SHA-256 matched experiments 228 and 235 and the established
  Archaludon lineage exactly.
- Official resolver keys were `agent`, `codex_sol_eclipse_alakazam_v22`,
  `submission_entrypoint_v28_garchomp`, and `_v28_original_agent`.
- The Archaludon callable retained function name `agent` while the loader
  exposed the selected base function through key `_v28_original_agent`.
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
- Kaggle accepted the package as submission `55369101` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 691.1.
- Score checkpoint: `2026-08-09 05:32 UTC`.
