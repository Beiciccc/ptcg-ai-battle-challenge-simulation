# 238 Archaludon v28 Exact Calibration

Date: 2026-08-11 UTC

Local generated package (not committed):
`artifacts/submissions/s238-archaludon-v28-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 228, 235, and 237

Kaggle submission: `55420644`

Public score: 710.6

Status: complete

Sources:
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Leaderboard deck meta](https://www.kaggle.com/code/myso1987/ptcg-ai-battle-leaderboard-deck-meta-by-score-band)
- [PTGC Game](https://www.kaggle.com/code/siddharajkulkarni/ptgc-game)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Archaludon Metal v28 archive after exact Steel failed the
  aggregate gate by one game in a fresh panel against Sol and Archaludon.
- Preserved the published policy, 60-card deck, loader entrypoint, current
  runtime, and archive bytes.
- Retained Archaludon as the predeclared fallback without changing any gate.

Public refresh:
- A newer meta snapshot archive was executable but byte-identical at the
  source and deck level to an established Archaludon strategy, so it did not
  establish a new behavior.
- A newer PTGC Game archive had no official score binding; the known public
  output remained unsuitable as a byte-bound candidate.
- New Discussion topics covered team-page display, deck input errors, local
  observation, rules questions, and card-text offsets; none changed the
  competition contract.
- Rules, Evaluation, competition data, and the CABT runtime showed no
  material change before the panel was fixed.

Candidate screen:
- Steel archive SHA-256 was
  `b5c7601e843a9f7269513a1ba9489cc1354a8dbff52e0ddd74f93fa8ff165bf2`.
- The fixed panel used seeds `2026081100` through `2026081115`, with Steel in
  seat zero on even seeds and seat one on odd seeds.
- Steel completed 5-3 against Sol and 5-3 against Archaludon, for 10-6
  overall.
- Against Sol, Steel went 3-1 from seat zero and 2-2 from seat one.
- Against Archaludon, Steel went 2-2 from seat zero and 3-1 from seat one.
- Across both anchors, Steel went 5-3 from seat zero and 5-3 from seat one.
- All sixteen games completed on their first execution without errors, ties,
  timeouts, invalid actions, random fallbacks, or retries.
- Steel search-disabled calls remained at zero.
- Maximum Steel decision latency was 0.002 seconds, and the global maximum was
  0.241 seconds.
- The fixed gate required at least 11-5 overall, at least 5-3 against each
  anchor, at least 2-2 from every anchor and candidate-seat cell, and at least
  5-3 from each candidate seat overall.
- Steel failed only the aggregate gate at 10-6, so the exact Archaludon
  fallback was retained.

Validation:
- Archive SHA-256 matched the established Steel lineage exactly.
- Official resolver keys were `agent`, `codex_sol_eclipse_alakazam_v22`, and
  `_v28_original_agent`.
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
- Kaggle accepted the package as submission `55420644` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 710.6.
- Score checkpoint: `2026-08-11 02:10 UTC`.
