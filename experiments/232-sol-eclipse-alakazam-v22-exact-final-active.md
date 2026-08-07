# 232 Sol Eclipse Alakazam v22 Exact Final Active

Date: 2026-08-07 UTC

Local generated package (not committed):
`artifacts/submissions/s232-sol-eclipse-alakazam-v22-exact-final-active.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 193 and 230

Kaggle submission: `55331522`

Public score: 499.3

Status: complete

Sources:
- [Sol Eclipse Alakazam v22](https://www.kaggle.com/code/jazivxt/codex-sol-eclipse-alakazam)
- [Archaludon Metal v28](https://www.kaggle.com/code/jazivxt/archaludon-metal-v28-agents-only)
- [Pokemon Steel](https://www.kaggle.com/code/plamen06/pokemon-steel)
- [kaggle-environments 1.32.6](https://github.com/Kaggle/kaggle-environments/commit/bded87b0d7879078c726a93a4884d044f79c4eed)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Sol Eclipse Alakazam v22 archive as the final active
  complement to experiment 231 Steel.
- Preserved the published policy, 60-card deck, loader entrypoint, current
  runtime, and archive bytes.
- Screened exact Archaludon against Sol and Steel before applying the fixed Sol
  fallback.

Public refresh:
- The new Alakazam/Dudunsparce output remained archive SHA-256
  `4e28ee0b2225e2526c663a593e1ffdef116e94440c13042721c42f2510a8575e`
- Its nested `cg/cg/` runtime still failed the isolated official loader with
  `ModuleNotFoundError: No module named 'cg.api'`
- The exact version was linked to submission `55327124`, but that submission
  exposed no formatted score; page-level scores could not be bound to it
- `kaggle-environments` 1.32.6 changed only the package version after an
  unrelated Kaggriculture update; CABT and loader files were unchanged from
  1.32.5
- Discussion, Rules, Evaluation, and competition data produced no other
  verified material update

Candidate screen:
- Archaludon archive SHA-256 was
  `b7e4e4bf8c964a7a50fea343dbe7a4b4ac5517368d1e5823d5dc563568d02d5d`
- The fixed panel used seeds `2026080812` through `2026080827`, with
  Archaludon in seat zero on even seeds and seat one on odd seeds
- Archaludon completed 2-6 against Sol and 7-1 against Steel, for 9-7 overall
- Against Sol, Archaludon went 1-3 from seat zero and 1-3 from seat one
- Against Steel, Archaludon went 3-1 from seat zero and 4-0 from seat one
- Across both anchors, Archaludon went 4-4 from seat zero and 5-3 from seat one
- All sixteen games completed without errors, ties, timeouts, invalid actions,
  or retries
- Maximum Archaludon decision latency was 0.016 seconds, and the global maximum
  was 0.159 seconds
- The fixed gate required at least 11-5 overall, at least 5-3 against each
  anchor, and at least 2-2 from each candidate seat within each anchor;
  Archaludon failed the aggregate and all three Sol-specific gates

Validation:
- Archive SHA-256 matched experiments 193 and 230 exactly
- Official resolver keys were `_v28_original_agent`,
  `codex_sol_eclipse_alakazam_v22`, and `agent`
- Loader-selected initialization returned each exact submitted 60-card deck
- Clean root Sol archive with `main.py`, `deck.csv`, published metadata, and
  the full current runtime
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Main SHA-256:
  `f31eba2e819ee2b3d46765b4195ea7dab8f32d0b5d09cafd39b3823661f6b5aa`
- Deck SHA-256:
  `8eccc69c3bf7d499f38c6116c33c5fac837050bf0ec71a5a1883f0f20f41ddbc`
- Linux runtime SHA-256:
  `d16244a3157fc55c3314f08dcc7c5179168697d78c105b95c7debd556b764bb7`
- Archive SHA-256:
  `78dde4d68910a7c841a4c989a7e39fe8ae4ec15b0ba278f28b7ba43cdec5476b`

Result:
- Kaggle accepted the package as submission `55331522` and marked it complete.
- Public evaluation remained at the 600.0 initialization baseline before its
  first non-baseline reading of 499.3.
- At this checkpoint, the three byte-identical official rows read 592.8,
  790.8, and 499.3.
- The latest two submissions preserve Steel and Sol Eclipse Alakazam as
  distinct complementary strategy families.
- Score checkpoint: `2026-08-07 18:37 UTC`.
