# 229 Steel Search-Disabled Exact Calibration

Date: 2026-08-07 UTC

Local generated package (not committed):
`artifacts/submissions/s229-steel-search-disabled-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 173, 175, 198, 201, 208,
210, 225, and 227

Kaggle submission: `55325206`

Public score: 721.1

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Garchomp v28](https://www.kaggle.com/code/jazivxt/garchomp-ex-v28-agents-only)
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact search-disabled Steel archive as the second 2026-08-07
  calibration and complement to experiment 228 Archaludon.
- Preserved the documented compatibility flag, strategy, 60-card deck,
  runtime, and archive bytes.
- Screened the mature Garchomp v28 archive against Archaludon before applying
  the fixed Steel fallback.

Public refresh:
- A new Great Tusk / Crustle run was still executing and had no published
  output archive or score-bound submission at the decision checkpoint
- The latest published PPO candidate remained unchanged from experiment 228
  and still lacked its claimed trained checkpoint
- Neither item supplied verifiable new behavior for this calibration

Candidate screen:
- Garchomp v28 archive SHA-256 was
  `e552dbe5042cf09abb25aeeba8359f4f5b4994a9982c11dcbf7f74a1b4b3aecf`
- The exact archive had previously completed a balanced 6-2 screen against
  Steel without faults
- Eight new seat-alternated games against Archaludon split 4-4
- Garchomp went 2-2 from seat zero and 2-2 from seat one; winning seats also
  split 4-4
- All games completed without errors, ties, timeouts, invalid actions, or
  retries
- Maximum Garchomp decision latency was 0.002 seconds, and the global maximum
  was 0.025 seconds
- The fixed gate required at least 5-3 with at least 2-2 from each candidate
  seat, so the aggregate result failed and selected the unique Steel fallback
- Screen seeds were `2026080772` through `2026080779`

Validation:
- Archive SHA-256 matched experiments 173, 175, 198, 201, 208, 210, 225, and
  227 exactly
- Static and dynamic loader checks selected the final `agent` callable
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
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
- Kaggle accepted the package as submission `55325206` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 721.1.
- At this checkpoint, the nine byte-identical official rows read 966.4, 721.7,
  673.6, 626.7, 827.9, 679.6, 757.4, 693.5, and 721.1.
- The latest two submissions preserve Archaludon and Steel as distinct
  complementary strategy families.
- Score checkpoint: `2026-08-07 13:04 UTC`.
