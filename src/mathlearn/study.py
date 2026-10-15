"""Study-pack rendering."""
from __future__ import annotations
import sqlite3
from pathlib import Path

def render_study(family_id: str, db_path: Path) -> str:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    fam = conn.execute("SELECT * FROM families WHERE family_id=?", (family_id,)).fetchone()
    if fam is None:
        conn.close()
        raise KeyError(family_id)
    mans = conn.execute("SELECT title, path FROM manuscripts WHERE family_id=?", (family_id,)).fetchall()
    conn.close()
    lines = [
        f"# Family {fam['family_id']}: {fam['title']}",
        "",
        f"- Subject: {fam['subject']}",
        f"- Manuscripts: {fam['manuscript_count']}",
        f"- Lean formalized: {'yes' if fam['lean_formalized'] else 'unknown/no'}",
        "",
        "## Catalog description",
        "",
        fam["description"] or "_No description captured._",
        "",
        "## Constituent manuscripts",
        "",
    ]
    for m in mans:
        lines.append(f"- {m['title']} (`{m['path']}`)")
    if fam["lean_sources"]:
        lines += ["", "## Lean sources", ""]
        for src in fam["lean_sources"].split(";"):
            if src:
                lines.append(f"- `{src}`")
    lines += [
        "",
        "## To learn (agent pipeline)",
        "",
        "1. TheoremExtractor: statement + hypotheses + construction.",
        "2. ProofCritic: verify each claim against source.",
        "3. LeanVerifier: record formal declarations.",
        "4. Tutor: mental model + prerequisites.",
        "5. Quizzer: 3 questions + answer key.",
    ]
    return "\n".join(lines) + "\n"
