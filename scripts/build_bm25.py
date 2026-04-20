#!/usr/bin/env python3
"""Build BM25 index from indexes/chunks.jsonl (stdlib BM25)."""
from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from bm25_okapi import BM25Okapi, save_bm25
from phase5_retrieval_lib import BM25_PICKLE, INDEXES, load_chunks, tokenize


def main() -> None:
    chunks = load_chunks()
    if not chunks:
        raise SystemExit("No chunks; run build_chunks.py first")
    corpus = [tokenize(c.get("text", "")) for c in chunks]
    corpus = [t if t else ["_"] for t in corpus]
    bm25 = BM25Okapi(corpus)
    INDEXES.mkdir(parents=True, exist_ok=True)
    save_bm25(
        {
            "bm25": bm25,
            "chunk_ids": [c["chunk_id"] for c in chunks],
        },
        BM25_PICKLE,
    )
    print(f"wrote BM25 for {len(chunks)} chunks -> {BM25_PICKLE}")


if __name__ == "__main__":
    main()
