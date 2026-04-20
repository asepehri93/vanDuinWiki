#!/usr/bin/env python3
"""Build dense vectors for each chunk (default: deterministic hash embedding; optional: sentence-transformers)."""
from __future__ import annotations

import argparse
import gzip
import json
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from phase5_retrieval_lib import CHUNKS_JSONL, EMBED_MANIFEST, INDEXES, VECTORS_JSON_GZ, load_chunks


def embed_hash(chunks: list[dict], dim: int) -> tuple[list[list[float]], str]:
    from phase5_retrieval_lib import hash_embed_text

    vecs = [hash_embed_text(c.get("text", ""), dim=dim) for c in chunks]
    return vecs, f"hash_sha256_v1_dim{dim}"


def embed_sentence_transformers(chunks: list[dict], model_name: str) -> tuple[list[list[float]], str]:
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(model_name)
    texts = [c.get("text", "")[:8000] for c in chunks]
    batch = 32
    out: list[list[float]] = []
    for i in range(0, len(texts), batch):
        emb = model.encode(texts[i : i + batch], convert_to_numpy=True)
        out.extend(emb.tolist())
    return out, model_name


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--backend",
        choices=("hash", "sentence_transformers"),
        default="hash",
        help="hash = deterministic stdlib default; sentence_transformers = semantic (extra deps)",
    )
    ap.add_argument("--dim", type=int, default=128, help="Hash embedding dimension (hash backend only)")
    ap.add_argument(
        "--model",
        default="sentence-transformers/all-MiniLM-L6-v2",
        help="SentenceTransformer model id",
    )
    args = ap.parse_args()

    chunks = load_chunks()
    if not chunks:
        raise SystemExit(f"No chunks at {CHUNKS_JSONL}; run build_chunks.py first")

    if args.backend == "hash":
        vectors, model_id = embed_hash(chunks, args.dim)
    else:
        vectors, model_id = embed_sentence_transformers(chunks, args.model)

    INDEXES.mkdir(parents=True, exist_ok=True)
    payload = {
        "model": model_id,
        "dim": len(vectors[0]) if vectors else 0,
        "chunk_ids": [c["chunk_id"] for c in chunks],
        "vectors": vectors,
    }
    raw = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    with gzip.open(VECTORS_JSON_GZ, "wb", compresslevel=6) as f:
        f.write(raw)

    EMBED_MANIFEST.write_text(
        json.dumps(
            {"model": model_id, "dim": payload["dim"], "chunk_count": len(chunks), "backend": args.backend},
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(vectors)} vectors ({payload['dim']}d) -> {VECTORS_JSON_GZ}")


if __name__ == "__main__":
    main()
