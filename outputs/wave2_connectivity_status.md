# Phase 4 Wave 2 — mechanical connectivity (2026-04-20)

- **Tool:** `python3 scripts/report_paper_connectivity.py`
- **Result:** **1278/1278** paper slugs linked from `wiki/concepts/`, `materials/`, `forcefields/`, or `protocols/` — see [`connectivity_report.md`](connectivity_report.md).
- **Fix applied:** Ten paper pages had **invalid YAML** in `title:` (double-quoted strings with LaTeX-style `\(` escapes). Titles were switched to **single-quoted** scalars so `yaml.safe_load` succeeds and [`scripts/generate_papers_indexes.py`](../scripts/generate_papers_indexes.py) includes every paper in the by-year / by-domain tables.
- **Deeper Wave 2 work (optional):** Expand narrative “Literature review (this knowledge base)” sections on theme hubs per [`docs/MASTER_PLAN.md`](../docs/MASTER_PLAN.md); mechanical link KPI is already satisfied.
