# 202 Visible-Grim Belief Alakazam v23 Exact Replication

Date: 2026-08-01 UTC

Local generated package (not committed):
`artifacts/submissions/s202-visible-grim-belief-alakazam-v23-exact-replication.tar.gz`

Official upload filename: `submission.tar.gz`

Reproducibility: byte-identical rerun of experiments 187 and 190

Kaggle submission: `55154480`

Public score: 591.3

Status: complete

Sources:
- [Visible-Grim Belief Alakazam v23](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-visible-grim-belief-alakazam-v23)
- [Competition data](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle/data)

Summary:
- Re-ran the exact Visible-Grim Belief Alakazam v23 archive as a distinct
  strategy family after experiment 201 Steel.
- Preserved the public policy, 60-card deck, loader entrypoint, packaged
  runtime, and archive bytes.
- Measured current counter coverage against Archaludon, Crustle, and Rocket
  Spidops before submission.

Validation:
- Archive SHA-256 matched experiments 187 and 190 exactly
- Static and dynamic loader checks selected `submission_entrypoint`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- The exact archive retains its pre-Program22 packaged runtime
- Twenty-four fresh seat-alternated games completed 11-13 without errors
- Matchup results: 4-4 against Archaludon, 3-5 against Crustle, and 4-4
  against Rocket Spidops
- All 622 observed search calls completed without failures
- Maximum observed decision latency was 0.386 seconds
- Main SHA-256:
  `b44c68f9d25bda71b2c00dc5300f4548089a49765a364d5d978bd541079d54c7`
- Deck SHA-256:
  `0598646548d081832ec311c15fdc369b32c6f5e63175b0cfd1904d21fd082451`
- Linux runtime SHA-256:
  `feafd4046b2f688bdb33a4972c139b78e13e243ab5707ece52c43cf39a34b887`
- Archive SHA-256:
  `81d8a7e00f8955d2be66b58ae03e382a86be90d9f841d4ad2505a0d1445fa38b`

Result:
- Kaggle accepted the package as submission `55154480` and marked it complete.
- Public evaluation moved from the 600.0 initialization baseline through 686.9,
  597.9, and 659.0 before reaching 591.3.
- At this checkpoint, the three byte-identical official rows read 802.1,
  715.7, and 591.3.
- Score checkpoint: `2026-08-02 01:27 UTC`.
