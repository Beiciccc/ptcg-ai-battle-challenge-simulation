from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


def read_table(path: str | Path):
    """Read a parquet/CSV table using the path stem as the logical table name."""
    p = Path(path)
    parquet = p.with_suffix(".parquet")
    csv_path = p.with_suffix(".csv")
    try:
        import pandas as pd
    except Exception as exc:
        if csv_path.exists():
            with csv_path.open(newline="", encoding="utf-8") as f:
                return list(csv.DictReader(f))
        raise RuntimeError("pandas is required to read parquet tables") from exc
    if parquet.exists():
        return pd.read_parquet(parquet)
    if csv_path.exists():
        try:
            return pd.read_csv(csv_path)
        except pd.errors.EmptyDataError:
            return pd.DataFrame()
    return pd.DataFrame()


def write_table(path: str | Path, rows: list[dict[str, Any]], csv_sidecar_max_rows: int = 50000) -> None:
    """Write parquet with zstd when possible, and a small CSV sidecar for inspection."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    csv_path = p.with_suffix(".csv")
    if not rows:
        csv_path.write_text("", encoding="utf-8")
        return
    try:
        import pandas as pd

        df = pd.DataFrame(rows)
        df.to_parquet(p.with_suffix(".parquet"), index=False, compression="zstd")
        if len(df) <= csv_sidecar_max_rows:
            df.to_csv(csv_path, index=False)
    except Exception:
        fieldnames = sorted({key for row in rows for key in row})
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
