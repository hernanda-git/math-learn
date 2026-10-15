"""Path and configuration helpers."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

DEFAULT_CONFIG = Path("config/datasets.json")

def load_config(path: Path | str = DEFAULT_CONFIG) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(p)
    return json.loads(p.read_text(encoding="utf-8"))

def resolve_math_repo(config: dict[str, Any], override: str | None = None) -> Path:
    raw = override or config.get("math_repo", "../math")
    p = Path(raw)
    if not p.is_absolute():
        # resolve relative to cwd or repo root; prefer cwd
        p = (Path.cwd() / p).resolve()
    if not (p / "CONTENTS.md").exists():
        raise FileNotFoundError(f"Math repo not found at {p}")
    return p
