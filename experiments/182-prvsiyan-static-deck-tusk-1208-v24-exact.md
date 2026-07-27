# 182 Static-Deck Tusk 1208 v24 Exact Public Output

Date: 2026-07-27 UTC

Local generated package (not committed):
`artifacts/submissions/s182-prvsiyan-static-deck-tusk-1208-v24-exact.tar.gz`

Reproducibility: exact byte-for-byte public Code output

Kaggle submission: `55024176`

Public score: 709.4

Status: complete

Sources:
- [Static-Deck Tusk 1208 v24](https://www.kaggle.com/code/prvsiyan/ptcg-ai-battle-static-deck-tusk-1208-v24)
- [Visible Field Router v3](https://www.kaggle.com/code/prvsiyan/ptcg-visible-field-router-v3)
- [Leaderboard deck meta by score band](https://www.kaggle.com/code/myso1987/ptcg-ai-battle-leaderboard-deck-meta-by-score-band)

Summary:
- Preserved every byte of the public v24 archive.
- Used the same Great Tusk / Crustle deck as experiment 181 without its
  visible-field routing overrides.
- Treated the package as a same-deck control for measuring the routing changes.

Validation:
- Archive SHA-256 matched the downloaded public Code output exactly
- Static entrypoint check selected the unique final `agent`
- Loader-selected initialization returned the exact submitted 60-card deck
- Clean 11-file archive with `main.py`, `deck.csv`, and nine runtime files
- No links, cache files, AppleDouble files, unsafe paths, or nested archive root
- Four loader-aware mirror games completed without errors
- Eight games against Visible-Grim Alakazam completed 6-2
- Eight games against current-runtime Steel completed 3-5
- Eight games against replay-trained Grimmsnarl completed 2-6
- Eight games against Mega Lucario Prize-Pressure completed 5-3
- Maximum observed Static Tusk decision latency was 0.084 seconds
- Main SHA-256:
  `8f2fa9c432642cd07b1fa10246aa200bbd2713b94cbc8a98d902419ff4ad18c8`
- Deck SHA-256:
  `6415396d35c0f4b3d69ee6c231337968cc9f2d5d0767de801346d6f412c18e62`
- Windows runtime SHA-256:
  `a3a401d0f5ccc3474b9c8a7a2431920c4b728d28105a510aa6927ad6283e5cf7`
- Linux runtime SHA-256:
  `feafd4046b2f688bdb33a4972c139b78e13e243ab5707ece52c43cf39a34b887`
- Linux ARM64 runtime SHA-256:
  `116750365a1043f0d95e200bb283c042753cdbd44c7d16331827ad0a44df0553`
- macOS runtime SHA-256:
  `00154aee7d3071451096c929c52da9f9af360a2821e686671097f5011e5a5d95`
- Archive SHA-256:
  `41dbcf52e48cf86357e826694ff9726a75c7e4afdee5fe6eede540d066dea7c9`

Result:
- Kaggle accepted the package and marked submission `55024176` complete.
- Public evaluation moved from 600.0 through 759.3 to 709.4 as additional
  validation battles accumulated.
- Score checkpoint: `2026-07-27 09:19 UTC`.
