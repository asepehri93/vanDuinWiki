#!/usr/bin/env python3
"""Build indexes/chunks.jsonl from wiki markdown and optionally normalized extracts."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from phase5_retrieval_lib import (
    CHUNKS_JSONL,
    INDEXES,
    MANIFEST,
    ROOT,
    WIKI,
    parse_frontmatter,
    split_markdown_sections,
    stable_chunk_id,
    wiki_id_to_paper_id,
)


def iter_wiki_md_files() -> list[Path]:
    out: list[Path] = []
    for p in sorted(WIKI.rglob("*.md")):
        rel = p.relative_to(ROOT)
        parts = rel.parts
        if "_templates" in parts:
            continue
        out.append(p)
    return out


def chunk_wiki_file(path: Path) -> list[dict]:
    rel = path.relative_to(ROOT).as_posix()
    raw = path.read_text(encoding="utf-8", errors="replace")
    meta, body = parse_frontmatter(raw)
    wiki_id = meta.get("id") if isinstance(meta.get("id"), str) else None
    page_type = meta.get("type") if isinstance(meta.get("type"), str) else None
    paper_id = wiki_id_to_paper_id(wiki_id)

    sections = split_markdown_sections(body)
    chunks: list[dict] = []
    for i, (heading, text) in enumerate(sections):
        if not text.strip():
            continue
        cid = stable_chunk_id(rel, heading, i)
        chunks.append(
            {
                "chunk_id": cid,
                "source_type": "wiki",
                "wiki_path": rel,
                "wiki_id": wiki_id,
                "page_type": page_type,
                "paper_id": paper_id,
                "section_heading": heading,
                "chunk_index": i,
                "text": text.strip(),
            }
        )
    return chunks


def chunk_extract(path: Path) -> list[dict]:
    """One chunk per extract file (p1-2 preview)."""
    rel = path.relative_to(ROOT).as_posix()
    stem = path.name
    if not stem.endswith("_p1-2.txt"):
        return []
    slug = stem[: -len("_p1-2.txt")]
    raw = path.read_text(encoding="utf-8", errors="replace")
    wiki_id = f"paper:{slug}"
    cid = stable_chunk_id(rel, "extract_p1-2", 0)
    return [
        {
            "chunk_id": cid,
            "source_type": "extract",
            "wiki_path": rel,
            "wiki_id": wiki_id,
            "page_type": "paper",
            "paper_id": wiki_id,
            "section_heading": "extract_p1-2",
            "chunk_index": 0,
            "text": raw.strip()[:50000],
        }
    ]


def main() -> None:
    ap = argparse.ArgumentParser(description="Build Phase 5 chunk jsonl.")
    ap.add_argument(
        "--include-extracts",
        action="store_true",
        help="Include normalized/extracts/*_p1-2.txt when present",
    )
    args = ap.parse_args()

    INDEXES.mkdir(parents=True, exist_ok=True)
    all_chunks: list[dict] = []

    for f in iter_wiki_md_files():
        all_chunks.extend(chunk_wiki_file(f))

    if args.include_extracts:
        ext_dir = ROOT / "normalized" / "extracts"
        if ext_dir.is_dir():
            for p in sorted(ext_dir.glob("*_p1-2.txt")):
                all_chunks.extend(chunk_extract(p))

    with CHUNKS_JSONL.open("w", encoding="utf-8") as out:
        for c in all_chunks:
            out.write(json.dumps(c, ensure_ascii=False) + "\n")

    MANIFEST.write_text(
        json.dumps(
            {
                "built_at": datetime.now(timezone.utc).isoformat(),
                "chunk_count": len(all_chunks),
                "include_extracts": args.include_extracts,
                "script": "build_chunks.py",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(all_chunks)} chunks -> {CHUNKS_JSONL}")


if __name__ == "__main__":
    main()
