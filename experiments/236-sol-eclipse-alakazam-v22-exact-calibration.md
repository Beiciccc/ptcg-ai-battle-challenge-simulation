# 236 Sol Eclipse Alakazam v22 Exact Calibration

Date: 2026-08-09 UTC

Local generated package (not committed):
`artifacts/submissions/s236-sol-eclipse-alakazam-v22-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 193, 230, 232, and 234

Kaggle submission: `55368902`

Public score: 676.4

Status: complete

Sources:
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Visible-Grim Belief Alakazam v23](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-visible-grim-belief-alakazam-v23)
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Leaderboard deck meta](https://www.kaggle.com/code/myso1987/ptcg-ai-battle-leaderboard-deck-meta-by-score-band)
- [PTGC Game](https://www.kaggle.com/code/siddharajkulkarni/ptgc-game)
- [kaggle-environments 1.32.6](https://github.com/Kaggle/kaggle-environments/commit/bded87b0d7879078c726a93a4884d044f79c4eed)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Sol Eclipse Alakazam v22 archive after exact Visible-Grim
  Belief Alakazam v23 failed a fixed panel against Sol and Archaludon.
- Preserved the published policy, 60-card deck, loader entrypoint, current
  runtime, and archive bytes.
- Retained the predeclared Sol fallback without changing any result gate.

Public refresh:
- The latest score-band notebook completed over 2,359 teams and 2,212 unique
  replays, but released only aggregate archetype statistics and no strategy
  archive, source, full deck, or submission mapping.
- Its aggregate output placed Grimmsnarl, Alakazam, and Mega Lucario as the
  three largest overall families; this did not identify an exact candidate.
- PTGC Game remained at v63. A newer public result had no corresponding Code
  version or file hash, while the known archive used random initialized PPO
  weights.
- Discussion, Rules, Evaluation, competition data, and the CABT runtime
  supplied no other material change before the panel was fixed.

Candidate screen:
- Visible-Grim Belief Alakazam v23 archive SHA-256 was
  `81d8a7e00f8955d2be66b58ae03e382a86be90d9f841d4ad2505a0d1445fa38b`.
- The fixed panel used seeds `2026080948` through `2026080963`, with v23 in
  seat zero on even seeds and seat one on odd seeds.
- V23 completed 1-7 against Sol and 5-3 against Archaludon, for 6-10 overall.
- Against Sol, v23 went 0-4 from seat zero and 1-3 from seat one.
- Against Archaludon, v23 went 4-0 from seat zero and 1-3 from seat one.
- Across both anchors, v23 went 4-4 from seat zero and 2-6 from seat one.
- All sixteen games completed on their first execution without errors, ties,
  timeouts, invalid actions, random fallbacks, or retries.
- All 326 reported v23 search calls completed without failure.
- Maximum v23 decision latency was 0.385 seconds, and the global maximum was
  0.445 seconds.
- The fixed gate required at least 11-5 overall, at least 5-3 against each
  anchor, at least 2-2 from every anchor and candidate-seat cell, and at least
  5-3 from each candidate seat overall.
- V23 failed the aggregate, Sol, three anchor-seat-cell, and both overall-seat
  gates, so the exact Sol fallback was retained.

Validation:
- Archive SHA-256 matched experiments 193, 230, 232, and 234 exactly.
- Official resolver keys were `submission_entrypoint`,
  `codex_sol_eclipse_alakazam_v22`, and `_v28_original_agent`.
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
- Kaggle accepted the package as submission `55368902` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 676.4.
- Score checkpoint: `2026-08-09 05:20 UTC`.
