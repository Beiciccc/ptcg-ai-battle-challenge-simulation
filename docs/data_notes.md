# Data Notes

Competition files are downloaded with:

```bash
python tools/download_assets.py --light
```

The light download includes:

| File | Local path | Notes |
| --- | --- | --- |
| `EN_Card_Data.csv` | `data/raw/competition/EN_Card_Data.csv` | English card table. Current local snapshot: 2022 rows, 17 columns. |
| `JP_Card_Data.csv` | `data/raw/competition/JP_Card_Data.csv` | Japanese card table with matching row count. |
| `sample_submission/cg/*` | `submission/cg/` | Runtime support files needed for local packaging. |

Large PDF card ID lists are available through:

```bash
python tools/download_assets.py --pdfs
```

Raw files are not committed. Public schema metadata is kept in
`data/metadata/card_schema.csv`.
