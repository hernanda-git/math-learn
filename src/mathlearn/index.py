"""Search helpers over the FTS index."""
from __future__ import annotations
import sqlite3
from pathlib import Path

def fts_search(db_path: Path, query: str, limit: int = 20) -> list[dict]:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            "SELECT family_id, title, snippet(docs,2,'[',']','...',12) AS snip, bm25(docs) AS score "
            "FROM docs WHERE docs MATCH ? ORDER BY score LIMIT ?",
            (query, limit),
        ).fetchall()
    except sqlite3.Error:
        rows = []
    conn.close()
    return [dict(r) for r in rows]
