from __future__ import annotations

import csv
import hashlib
import json
import re
from contextlib import contextmanager
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SDK_PATH = (
    REPO_ROOT
    / "KaggleData"
    / "pokemon-tcg-ai-battle"
    / "sample_submission"
    / "sample_submission"
)
EVIDENCE_DIR = REPO_ROOT / "pokemon_benchmark_evidence"
RUNS_DIR = REPO_ROOT / "pokemon_benchmark_runs"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def resolve_path(path: str | Path, base: Path = REPO_ROOT) -> Path:
    p = Path(path).expanduser()
    if not p.is_absolute():
        p = base / p
    return p.resolve()


def resolve_selection_dir(field_dir: str | Path, selection_dir: str | Path | None = None) -> Path:
    """Return the field-selection snapshot directory used by gates and reports."""
    if selection_dir:
        return resolve_path(selection_dir)
    return resolve_path(field_dir) / "selection"


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_csv(path: str | Path) -> list[dict[str, str]]:
    p = Path(path)
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: str | Path, rows: Iterable[dict[str, Any]], fieldnames: list[str]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: _csv_value(row.get(k, "")) for k in fieldnames})


def append_or_update_csv(
    path: str | Path,
    row: dict[str, Any],
    fieldnames: list[str],
    key_fields: list[str],
) -> None:
    rows = read_csv(path)
    key = tuple(str(row.get(k, "")) for k in key_fields)
    replaced = False
    out: list[dict[str, Any]] = []
    for old in rows:
        old_key = tuple(str(old.get(k, "")) for k in key_fields)
        if old_key == key:
            merged = dict(old)
            merged.update(row)
            out.append(merged)
            replaced = True
        else:
            out.append(old)
    if not replaced:
        out.append(row)
    write_csv(path, out, fieldnames)


def write_json(path: str | Path, data: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(to_jsonable(data), f, indent=2, sort_keys=True)
        f.write("\n")


def to_jsonable(data: Any) -> Any:
    if is_dataclass(data):
        return to_jsonable(asdict(data))
    if isinstance(data, Path):
        return str(data)
    if isinstance(data, dict):
        return {str(k): to_jsonable(v) for k, v in data.items()}
    if isinstance(data, (list, tuple)):
        return [to_jsonable(x) for x in data]
    return data


def slugify(value: str, fallback: str = "item") -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    return text or fallback


def stable_id(prefix: str, text: str, length: int = 10) -> str:
    return f"{prefix}_{slugify(text)[:48]}_{sha256_text(text)[:length]}"


def normalize_archetype(archetype: str) -> str:
    """Canonicalize archetype labels used as cross-store join keys.

    Residual archetypes are often emitted as ``other:A|B`` from the two most
    visible Pokemon in a deck. The order can flip across days when counts or
    tie-breaks move, but the benchmark needs the same deck family to remain one
    join key.
    """
    text = str(archetype or "").strip()
    if text == "alakazam":
        return "alakazam_dunsparce"
    if text.startswith("archetype:"):
        return "archetype:" + normalize_archetype(text.split(":", 1)[1])
    if text.startswith("other:") and "|" in text:
        prefix, rest = text.split(":", 1)
        parts = [p.strip() for p in rest.split("|") if p.strip()]
        if len(parts) > 1:
            parts = sorted(parts, key=lambda x: (x.casefold(), x))
            return prefix + ":" + "|".join(parts)
    return text


@contextmanager
def pushd(path: str | Path):
    import os

    old = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)


def _csv_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (list, tuple, dict)):
        return json.dumps(value, ensure_ascii=True, sort_keys=True)
    return str(value)
