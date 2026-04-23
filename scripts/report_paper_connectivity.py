#!/usr/bin/env python3
"""Mechanical report: which paper slugs are linked from synthesis wiki trees.

Aligned with docs/PHASE0.md connectivity KPI: a paper counts as "linked" if it
appears referenced from at least one of:
  wiki/concepts/, wiki/materials/, wiki/forcefields/, wiki/protocols/

Optionally report mentions from wiki/debates/ separately (not part of the
strict Phase 0 four-type definition).

Does not generate scientific claims — pattern matching only.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
PAPERS = WIKI / "papers"

SYNTHESIS_DIRS = {
    "concepts": WIKI / "concepts",
    "materials": WIKI / "materials",
    "forcefields": WIKI / "forcefields",
    "protocols": WIKI / "protocols",
}
DEBATES_DIR = WIKI / "debates"


def collect_paper_slugs() -> list[str]:
    slugs = []
    for path in sorted(PAPERS.glob("*.md")):
        if path.name == "index.md":
            continue
        # macOS AppleDouble resource-fork files masquerading as .md
        if path.name.startswith("._"):
            continue
        slugs.append(path.stem)
    return slugs


def read_tree_text(base: Path) -> str:
    if not base.is_dir():
        return ""
    parts: list[str] = []
    for path in sorted(base.rglob("*.md")):
        if "_templates" in path.parts:
            continue
        try:
            parts.append(path.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
    return "\n\n".join(parts)


def slug_mentioned(slug: str, corpus: str) -> bool:
    """Conservative patterns used across the wiki for paper references."""
    if f"[[{slug}]]" in corpus:
        return True
    if f"[[{slug}|" in corpus:
        return True
    if f"papers/{slug}.md" in corpus:
        return True
    if f"../papers/{slug}.md" in corpus:
        return True
    if f"paper:{slug}" in corpus:
        return True
    return False


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--output",
        "-o",
        type=Path,
        default=ROOT / "outputs" / "connectivity_report.md",
        help="Write markdown report here (default: outputs/connectivity_report.md)",
    )
    args = ap.parse_args()

    slugs = collect_paper_slugs()
    texts = {name: read_tree_text(path) for name, path in SYNTHESIS_DIRS.items()}
    debates_text = read_tree_text(DEBATES_DIR)

    linked_core: set[str] = set()
    per_slug_sources: dict[str, list[str]] = defaultdict(list)

    for slug in slugs:
        for name, text in texts.items():
            if slug_mentioned(slug, text):
                linked_core.add(slug)
                per_slug_sources[slug].append(name)

    debates_only: set[str] = set()
    for slug in slugs:
        if slug in linked_core:
            continue
        if slug_mentioned(slug, debates_text):
            debates_only.add(slug)

    linked_debates_any = {s for s in slugs if slug_mentioned(s, debates_text)}
    orphans = [s for s in slugs if s not in linked_core]

    n = len(slugs)
    n_ok = len(linked_core)
    pct = (100.0 * n_ok / n) if n else 0.0

    lines = [
        "# Paper connectivity report (mechanical)",
        "",
        f"Generated from `wiki/papers/*.md` (**{n}** paper notes, excluding `index.md`).",
        "",
        "## Definition (Phase 0 KPI)",
        "",
        "A paper is **connected** if its slug appears in at least one of "
        "`wiki/concepts/`, `wiki/materials/`, `wiki/forcefields/`, `wiki/protocols/` "
        "via common link patterns (`[[slug]]`, `[[slug|...]]`, `papers/slug.md`, `paper:slug`).",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Total paper slugs | {n} |",
        f"| Linked from synthesis (4 dirs) | {n_ok} ({pct:.1f}%) |",
        f"| Orphans (no link from those four) | {len(orphans)} |",
        f"| Mentioned in `wiki/debates/` (any) | {len(linked_debates_any)} |",
        f"| Debates-only (not in four dirs, but in debates) | {len(debates_only)} |",
        "",
        "## Orphans (backlog for Wave 2)",
        "",
    ]

    if orphans:
        for s in sorted(orphans):
            lines.append(f"- `{s}`")
    else:
        lines.append("*(none)*")

    lines.extend(
        [
            "",
            "## Per-slug sources (non-orphans)",
            "",
            "Which synthesis trees reference each slug (multiple = listed in more than one tree):",
            "",
        ]
    )

    for slug in sorted(per_slug_sources.keys()):
        srcs = ", ".join(sorted(per_slug_sources[slug]))
        lines.append(f"- `{slug}` — {srcs}")

    lines.extend(
        [
            "",
            "## Command",
            "",
            "```bash",
            "python3 scripts/report_paper_connectivity.py --output outputs/connectivity_report.md",
            "```",
            "",
        ]
    )

    out = "\n".join(lines) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(out, encoding="utf-8")
    print(f"wrote {args.output} ({n} slugs, {len(orphans)} orphans)")


if __name__ == "__main__":
    main()
