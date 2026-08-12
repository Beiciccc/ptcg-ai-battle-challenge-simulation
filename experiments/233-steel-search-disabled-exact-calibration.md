# 233 Steel Search-Disabled Exact Calibration

Date: 2026-08-09 UTC

Local generated package (not committed):
`artifacts/submissions/s233-steel-search-disabled-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 173, 175, 198, 201,
208, 210, 225, 227, 229, and 231

Kaggle submission: `55367653`

Public score: 662.6

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Garchomp GPU v28](https://www.kaggle.com/code/jazivxt/garchomp-gpu-v28)
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Meta Snapshot 06-29](https://www.kaggle.com/code/makthanithin/pok-mon-tcg-ai-battle-meta-snapshot-06-29)
- [kaggle-environments 1.32.6](https://github.com/Kaggle/kaggle-environments/commit/bded87b0d7879078c726a93a4884d044f79c4eed)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact search-disabled Steel archive after exact Garchomp missed
  two fixed matchup gates.
- Preserved the published policy, 60-card deck, loader entrypoint, current
  runtime, and archive bytes.
- Screened all public Code, Discussion, rules, evaluation, data, and runtime
  changes before fixing the matchup panel.

Public refresh:
- Meta Snapshot v111 produced archive SHA-256
  `342a5a4a6728556a1a87ad406118fa027d90d6e1b7718817d7c28c6c1f6c8fed`
  and completed shortly before an author submission scored 699.5.
- Its `main.py` and `deck.csv` were byte-identical to the established
  Archaludon Metal Tempo source used by earlier experiments, so the update did
  not establish new strategy behavior.
- A newer PTGC Game output required an unbundled `ppo_agent.pt` file at its
  first decision, while the 1084.5 Baseline remained in error and the latest
  score-band notebook remained an aggregate analysis.
- Two updated Discussion topics covered local setup and Bench protection;
  neither changed the simulator contract or supplied an executable strategy.
- Rules, Evaluation, competition data, and the CABT runtime were unchanged.

Candidate screen:
- Garchomp archive SHA-256 was
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`.
- The fixed panel used seeds `2026080900` through `2026080915`, with Garchomp
  in seat zero on even seeds and seat one on odd seeds.
- Garchomp completed 5-3 against Sol and 5-3 against Steel, for 10-6 overall.
- Against each anchor, Garchomp went 3-1 from seat zero and 2-2 from seat one.
- Across both anchors, Garchomp went 6-2 from seat zero and 4-4 from seat one.
- All sixteen games completed on their first execution without errors, ties,
  timeouts, invalid actions, random fallbacks, or retries.
- Maximum Garchomp decision latency was 0.006 seconds, and the global maximum
  was 0.254 seconds.
- The fixed gate required at least 11-5 overall, at least 5-3 against each
  anchor, at least 2-2 from every anchor and candidate-seat cell, and at least
  5-3 from each candidate seat overall.
- Garchomp failed the aggregate gate and the overall seat-one gate, so neither
  gate was relaxed and the exact Steel fallback was retained.

Validation:
- Archive SHA-256 matched the prior Steel experiments exactly.
- Official resolver keys were `submission_entrypoint_v28_garchomp`,
  `codex_sol_eclipse_alakazam_v22`, and `agent`.
- Loader-selected initialization returned each exact submitted 60-card deck.
- Clean root archive with `main.py`, `deck.csv`, and the full current runtime.
- No duplicate members, links, unsafe paths, or nested archive root.
- Main SHA-256:
  `4cc4c469fd15ddfce16e108698b47556515748223993e272fb0e1236eb2ed03b`
- Deck SHA-256:
  `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b5c7601e843a9f7269513a1ba9489cc1354a8dbff52e0ddd74f93fa8ff165bf2`

Result:
- Kaggle accepted the package as submission `55367653` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 662.6.
- Score checkpoint: `2026-08-09 04:32 UTC`.
