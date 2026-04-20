"""Shared helpers for Phase 5 chunking, search, and evaluation."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INDEXES = ROOT / "indexes"
WIKI = ROOT / "wiki"
CHUNKS_JSONL = INDEXES / "chunks.jsonl"
BM25_PICKLE = INDEXES / "bm25.pkl"
VECTORS_JSON_GZ = INDEXES / "vectors.json.gz"
EMBED_MANIFEST = INDEXES / "embedding_manifest.json"
MANIFEST = INDEXES / "manifest.json"


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL | re.MULTILINE)
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def stable_chunk_id(wiki_path: str, heading: str, index: int) -> str:
    raw = f"{wiki_path}\n{heading}\n{index}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    body = text[m.end() :]
    try:
        import yaml  # type: ignore

        meta = yaml.safe_load(m.group(1)) or {}
        if not isinstance(meta, dict):
            return {}, body
        return meta, body
    except Exception:
        return {}, body


def split_markdown_sections(body: str) -> list[tuple[str, str]]:
    """Return list of (heading, content). Heading '' for preamble before first ##."""
    parts = HEADING_RE.split(body)
    if not parts:
        return [("", body.strip())]
    sections: list[tuple[str, str]] = []
    if parts[0].strip():
        sections.append(("", parts[0].strip()))
    it = iter(parts[1:])
    for h, content in zip(it, it):
        sections.append((h.strip(), content.strip()))
    return sections or [("", body.strip())]


def wiki_id_to_paper_id(wiki_id: str | None) -> str | None:
    if not wiki_id or not isinstance(wiki_id, str):
        return None
    if wiki_id.startswith("paper:"):
        return wiki_id
    return None


def load_chunks() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not CHUNKS_JSONL.is_file():
        return rows
    with CHUNKS_JSONL.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9_]+", text.lower())


def hash_embed_text(text: str, dim: int = 128) -> list[float]:
    """Deterministic bag-of-tokens embedding (stdlib). Not semantic; use sentence-transformers optional path for quality."""
    import hashlib
    import math

    vec = [0.0] * dim
    for tok in tokenize(text):
        h = hashlib.sha256(tok.encode("utf-8")).hexdigest()
        idx = int(h[:8], 16) % dim
        vec[idx] += 1.0
        for i in range(3):
            h2 = hashlib.sha256((tok + "#" + str(i)).encode("utf-8")).hexdigest()
            idx2 = int(h2[:8], 16) % dim
            vec[idx2] += 0.5
    n = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / n for v in vec]
