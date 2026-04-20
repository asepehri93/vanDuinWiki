#!/usr/bin/env python3
"""Hybrid lexical BM25 + dense (hash or ST) with RRF fusion. Stdlib + optional sentence-transformers."""
from __future__ import annotations

import argparse
import gzip
import json
import pickle
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from bm25_okapi import load_bm25
from phase5_retrieval_lib import BM25_PICKLE, EMBED_MANIFEST, VECTORS_JSON_GZ, load_chunks, tokenize


def rrf_fuse(ranked_ids: list[list[str]], k: float = 60.0) -> dict[str, float]:
    scores: dict[str, float] = {}
    for rlist in ranked_ids:
        for rank, cid in enumerate(rlist, start=1):
            scores[cid] = scores.get(cid, 0.0) + 1.0 / (k + rank)
    return scores


def cosine_dense(q: list[float], mat: list[list[float]], top: int) -> list[int]:
    scores: list[tuple[float, int]] = []
    for i, row in enumerate(mat):
        s = sum(a * b for a, b in zip(q, row))
        scores.append((s, i))
    scores.sort(key=lambda x: -x[0])
    return [i for _, i in scores[:top]]


def load_vector_bundle():
    with gzip.open(VECTORS_JSON_GZ, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    return data["vectors"], data.get("model", ""), data["chunk_ids"]


def search(
    query: str,
    top_k: int = 10,
    rrf_k: float = 60.0,
    bm25_top: int = 50,
    dense_top: int = 50,
) -> list[dict]:
    chunks = load_chunks()
    if not chunks:
        raise RuntimeError("No chunks loaded")
    id_to_chunk = {c["chunk_id"]: c for c in chunks}
    chunk_list_ids = [c["chunk_id"] for c in chunks]

    bundle = load_bm25(BM25_PICKLE)
    bm25 = bundle["bm25"]
    qtok = tokenize(query)
    if not qtok:
        qtok = ["_"]
    bm_scores = bm25.get_scores(qtok)
    bm_order = sorted(range(len(bm_scores)), key=lambda i: -bm_scores[i])[:bm25_top]
    bm_ids = [chunk_list_ids[i] for i in bm_order]

    vectors, _model_label, v_chunk_ids = load_vector_bundle()
    if v_chunk_ids != chunk_list_ids:
        raise RuntimeError("chunk order mismatch: rebuild bm25 and vectors together")

    man = json.loads(EMBED_MANIFEST.read_text(encoding="utf-8"))
    backend = man.get("backend", "hash")
    if backend == "hash":
        from phase5_retrieval_lib import hash_embed_text

        dim = len(vectors[0]) if vectors else 128
        qv = hash_embed_text(query, dim=dim)
    else:
        from sentence_transformers import SentenceTransformer

        model_name = man.get("model", "sentence-transformers/all-MiniLM-L6-v2")
        qv = SentenceTransformer(model_name).encode([query], convert_to_numpy=True)[0].tolist()

    dn_order = cosine_dense(qv, vectors, dense_top)
    dn_ids = [chunk_list_ids[i] for i in dn_order]

    fused = rrf_fuse([bm_ids, dn_ids], k=rrf_k)
    best = sorted(fused.keys(), key=lambda x: -fused[x])[:top_k]
    out: list[dict] = []
    for cid in best:
        c = dict(id_to_chunk[cid])
        c["rrf_score"] = fused[cid]
        c["_dense_backend"] = backend
        out.append(c)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Hybrid BM25 + dense search")
    ap.add_argument("query", nargs="+", help="Search query")
    ap.add_argument("--top-k", type=int, default=10)
    ap.add_argument("--rrf-k", type=float, default=60.0)
    args = ap.parse_args()
    q = " ".join(args.query)
    for hit in search(q, top_k=args.top_k, rrf_k=args.rrf_k):
        wid = hit.get("wiki_id") or ""
        pid = hit.get("paper_id") or ""
        print(f"{hit['rrf_score']:.5f}\t{hit['chunk_id']}\t{hit.get('wiki_path')}\twiki_id={wid}\tpaper_id={pid}")


if __name__ == "__main__":
    main()
