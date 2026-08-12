# 227 Steel Search-Disabled Exact Calibration

Date: 2026-08-06 UTC

Local generated package (not committed):
`artifacts/submissions/s227-steel-search-disabled-exact-calibration.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 173, 175, 198, 201, 208,
210, and 225

Kaggle submission: `55304949`

Public score: 693.5

Status: complete

Sources:
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [Grimmsnarl V16](https://www.kaggle.com/code/tetsutani/grimmsnarl-ex-damage-transfer-control?scriptVersionId=340409708)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact search-disabled Steel archive as the second 2026-08-06
  calibration and complement to experiment 226 Archaludon.
- Preserved the documented compatibility flag, strategy, 60-card deck,
  runtime, and archive bytes.
- Audited Grimmsnarl V16 as a distinct guard-layer variant before applying the
  fixed insufficient-evidence fallback.

Candidate audit:
- Grimmsnarl V16 archive SHA-256 was
  `46bb3180e7b15e41aff60f52b18300aad1ca65d1840464d15e4d30fcac9b57ba`
- Its published output was bound to completed submission `55275925` and a
  773.2 public-score checkpoint
- V16 preserved the V15 deck, model, weights, base strategy, and runtime while
  adding five legal-action guard modules after the base decision
- Fallback-path line tracing performed a filesystem resolution on every traced
  event, imposing pathological overhead and distorting the matchup screen
- One game completed under the distorted instrumentation and a second began;
  neither was accepted as performance evidence, and no seed was rerun
- The fixed rule classified the incomplete panel as insufficient evidence and
  selected the unique Steel fallback

Validation:
- Archive SHA-256 matched experiments 173, 175, 198, 201, 208, 210, and 225
  exactly
- Static and dynamic loader checks selected the final `agent` callable
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Search compatibility remained explicitly disabled with `ENABLE_SEARCH=False`
- A separate eight-game Steel versus Garchomp diagnostic completed 2-6 without
  errors or ties; both profiles split their results evenly across seats
- Maximum observed decision latency was 0.002 seconds in that valid diagnostic
- Diagnostic seeds were `2026080600` through `2026080607`
- Main SHA-256:
  `4cc4c469d1c5caced0439cb2db32ad4827a87f7dcc698419bef6c07fc64aedcb`
- Deck SHA-256:
  `fbe6ab59992260b0d6774abed19469be315521b5ed0546de8c20f329607693e6`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `b5c7601e843a9f7269513a1ba9489cc1354a8dbff52e0ddd74f93fa8ff165bf2`

Result:
- Kaggle accepted the package as submission `55304949` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before
  moving through 526.5, 581.8, and 700.3 to 693.5.
- At this checkpoint, the eight byte-identical official rows read 966.4,
  721.7, 673.6, 626.7, 827.9, 679.6, 757.4, and 693.5.
- The latest two submissions preserve Archaludon and Steel as distinct
  complementary strategy families.
- Score checkpoint: `2026-08-07 12:41 UTC`.
