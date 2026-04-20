#!/usr/bin/env python3
"""Sync mechanical fields in wiki/papers/*.md from normalized/papers/{slug}.json.

Updates: pdf_sha256, pdf_path, extraction_quality (and doi/year when missing in wiki).

Run after: python3 scripts/corpus_profile.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki" / "papers"
NORM = ROOT / "normalized" / "papers"

try:
    import yaml
except ImportError:
    yaml = None


def set_scalar_line(fm_text: str, key: str, value) -> str:
    if value is None:
        return fm_text
    if isinstance(value, bool):
        yaml_val = "true" if value else "false"
    elif isinstance(value, int):
        yaml_val = str(value)
    else:
        yaml_val = json.dumps(str(value), ensure_ascii=False)
    pat = re.compile(rf"^(?P<k>{re.escape(key)}:)\s*.+$", re.M)
    if pat.search(fm_text):
        return pat.sub(rf"\g<k> {yaml_val}", fm_text, count=1)
    return fm_text


def sync_file(wpath: Path, dry: bool) -> bool:
    slug = wpath.stem
    jpath = NORM / f"{slug}.json"
    if not jpath.is_file():
        return False
    data = json.loads(jpath.read_text(encoding="utf-8"))
    bib = data.get("bibliography") or {}
    man = data.get("manifest") or {}
    ext = data.get("extraction") or {}
    raw = wpath.read_text(encoding="utf-8", errors="replace")
    if not raw.startswith("---"):
        return False
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return False
    fm = parts[1]
    body = parts[2]

    new_fm = fm
    new_fm = set_scalar_line(new_fm, "pdf_sha256", man.get("sha256") or "")
    new_fm = set_scalar_line(new_fm, "pdf_path", data.get("pdf_path") or "")
    new_fm = set_scalar_line(new_fm, "extraction_quality", ext.get("quality") or "unknown")

    if yaml and bib.get("doi"):
        meta = yaml.safe_load(fm) or {}
        if not (meta.get("doi") or "").strip():
            new_fm = set_scalar_line(new_fm, "doi", bib["doi"])
    if yaml and bib.get("year"):
        meta = yaml.safe_load(fm) or {}
        if not meta.get("year"):
            new_fm = set_scalar_line(new_fm, "year", int(bib["year"]))

    if new_fm == fm:
        return False
    if not dry:
        wpath.write_text(f"---{new_fm}---{body}", encoding="utf-8")
    return True


def main() -> None:
    dry = "--dry-run" in sys.argv
    n = 0
    for wpath in sorted(WIKI.glob("*.md")):
        if wpath.name in ("index.md",) or wpath.name.startswith("._"):
            continue
        if sync_file(wpath, dry):
            n += 1
    print(f"sync_wiki_paper_frontmatter: updated {n} files" + (" [dry-run]" if dry else ""))


if __name__ == "__main__":
    main()
