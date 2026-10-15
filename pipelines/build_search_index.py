"""Build/rebuild the search index (alias for ingest, which already builds FTS)."""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mathlearn.cli import main
raise SystemExit(main(["ingest", *sys.argv[1:]]))
