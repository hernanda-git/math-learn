"""CLI for math-learn."""
from __future__ import annotations
import argparse
from pathlib import Path

from mathlearn.catalog import ingest
from mathlearn.config import load_config, resolve_math_repo
from mathlearn.index import fts_search
from mathlearn.study import render_study

def cmd_ingest(args: argparse.Namespace) -> int:
    config = load_config(args.config)
    math_repo = resolve_math_repo(config, args.math_repo)
    db_path = Path(config["indexes"]["families"]).resolve()
    search_path = Path(config["indexes"]["fts"]).resolve()
    n = ingest(math_repo, db_path, search_path)
    print(f"Ingested {n} families from {math_repo}")
    print(f"Families DB: {db_path}")
    print(f"Search DB: {search_path}")
    return 0

def cmd_stats(args: argparse.Namespace) -> int:
    import sqlite3
    config = load_config(args.config)
    conn = sqlite3.connect(config["indexes"]["families"])
    total = conn.execute("SELECT COUNT(*) FROM families").fetchone()[0]
    formal = conn.execute("SELECT COUNT(*) FROM families WHERE lean_formalized=1").fetchone()[0]
    mans = conn.execute("SELECT COUNT(*) FROM manuscripts").fetchone()[0]
    subjects = conn.execute("SELECT subject, COUNT(*) FROM families GROUP BY subject ORDER BY COUNT(*) DESC").fetchall()
    conn.close()
    print(f"Families: {total}; manuscripts: {mans}; formalized families: {formal}")
    for s, c in subjects:
        print(f"{s}: {c}")
    return 0

def cmd_search(args: argparse.Namespace) -> int:
    config = load_config(args.config)
    hits = fts_search(Path(config["indexes"]["fts"]).resolve(), args.query, args.limit)
    if not hits:
        print("No matches.")
        return 0
    for h in hits:
        print(f"{h['family_id']}. {h['title']}  (score={h['score']:.3f})")
        print(f"   {h['snip']}")
    return 0

def cmd_study(args: argparse.Namespace) -> int:
    config = load_config(args.config)
    db_path = Path(config["indexes"]["families"]).resolve()
    text = render_study(args.family, db_path)
    out_dir = Path(config["study_output_dir"]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"family-{args.family}.md"
    out_path.write_text(text, encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="mathlearn")
    parser.add_argument("--config", default="config/datasets.json")
    sub = parser.add_subparsers(dest="command", required=True)
    p_ingest = sub.add_parser("ingest")
    p_ingest.add_argument("--math-repo", default=None)
    p_ingest.set_defaults(func=cmd_ingest)

    p_stats = sub.add_parser("stats")
    p_stats.set_defaults(func=cmd_stats)

    p_search = sub.add_parser("search")
    p_search.add_argument("query")
    p_search.add_argument("--limit", type=int, default=20)
    p_search.set_defaults(func=cmd_search)

    p_study = sub.add_parser("study")
    p_study.add_argument("family")
    p_study.set_defaults(func=cmd_study)

    args = parser.parse_args(argv)
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())
