# Architecture

- External read-only source: `openai/math` (C:/Workspace/math).
- Local derived state: `data/processed/*.sqlite` and study packs.
- Agents operate via contracts in `AGENTS.md`, not implicit memory.
- Search: SQLite FTS5 now; optional embedding backend behind a small interface.
- Dataset management: config-driven paths + sparse checkout helpers.
