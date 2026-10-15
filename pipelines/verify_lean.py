"""Print Lean-formalization audit summary."""
from __future__ import annotations
import sqlite3
from pathlib import Path
config_path = Path(__file__).resolve().parents[1] / "config" / "datasets.json"
import json
cfg = json.loads(config_path.read_text())
conn = sqlite3.connect((Path.cwd() / cfg["indexes"]["families"]).resolve())
for row in conn.execute("SELECT family_id,title,lean_sources FROM families WHERE lean_formalized=1 ORDER BY family_id"):
    print(row[0], row[1], "->", row[2])
print("count:", conn.execute("SELECT COUNT(*) FROM families WHERE lean_formalized=1").fetchone()[0])
conn.close()
