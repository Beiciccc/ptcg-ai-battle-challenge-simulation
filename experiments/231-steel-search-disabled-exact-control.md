# 231 Steel Search-Disabled Exact Control

Date: 2026-08-07 UTC

Local generated package (not committed):
`artifacts/submissions/s231-steel-search-disabled-exact-control.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 173, 175, 198, 201, 208,
210, 225, 227, and 229

Kaggle submission: `55330939`

Public score: 727.7

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Garchomp v28](https://www.kaggle.com/code/jazivxt/garchomp-ex-v28-agents-only)
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact search-disabled Steel archive as the fourth 2026-08-07
  control and complement to experiment 230 Sol Eclipse Alakazam.
- Preserved the documented compatibility flag, strategy, 60-card deck,
  runtime, and archive bytes.
- Screened exact Garchomp against both active strategy families before keeping
  the fixed Steel fallback.

Public refresh:
- A new public Alakazam/Dudunsparce output produced archive SHA-256
  `4e28ee0b2225e2526c663a593e1ffdef116e94440c13042721c42f2510a8575e`
- The archive had a 60-card deck and no links, duplicate members, or unsafe
  paths, but packaged its runtime under `cg/cg/`
- An isolated official-loader check failed immediately with
  `ModuleNotFoundError: No module named 'cg.api'`
- The exact output also had no verified official submission and score binding,
  so it was not an executable candidate
- Discussion, Rules, Evaluation, competition data, and CABT runtime checks
  produced no other verified material change

Candidate screen:
- Garchomp archive SHA-256 was
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`
- The fixed panel used seeds `2026080796` through `2026080811`, with Garchomp
  in seat zero on even seeds and seat one on odd seeds
- Garchomp completed 5-3 against Sol and 5-3 against Steel, for 10-6 overall
- Against Sol, Garchomp went 2-2 from seat zero and 3-1 from seat one
- Against Steel, Garchomp went 3-1 from seat zero and 2-2 from seat one
- All sixteen games completed without errors, ties, timeouts, invalid actions,
  or retries
- Maximum Garchomp decision latency was 0.002 seconds, and the global maximum
  was 0.200 seconds
- The fixed gate required at least 11-5 overall, so the candidate failed by one
  game; the aggregate gate was not relaxed

Validation:
- Archive SHA-256 matched experiments 173, 175, 198, 201, 208, 210, 225, 227,
  and 229 exactly
- Official resolver keys were `submission_entrypoint_v28_garchomp`,
  `codex_sol_eclipse_alakazam_v22`, and `agent`
- Loader-selected initialization returned each exact submitted 60-card deck
- Clean 11-file Steel archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Search compatibility remained explicitly disabled with `ENABLE_SEARCH=False`
- Main SHA-256:
  `4cc4c469d1c5caced0439cb2db32ad4827a87f7dcc698419bef6c07fc64aedcb`
- Deck SHA-256:
  `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b5c7601e843a9f7269513a1ba9489cc1354a8dbff52e0ddd74f93fa8ff165bf2`

Result:
- Kaggle accepted the package as submission `55330939` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 727.7.
- At this checkpoint, the ten byte-identical official rows read 966.4, 721.7,
  673.6, 626.7, 827.9, 679.6, 757.4, 693.5, 735.9, and 727.7.
- The latest two submissions preserve Sol Eclipse Alakazam and Steel as
  distinct complementary strategy families.
- Score checkpoint: `2026-08-07 18:02 UTC`.
