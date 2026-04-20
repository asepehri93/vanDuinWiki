"""Minimal BM25Okapi (stdlib only)."""
from __future__ import annotations

import math
import pickle
from collections import Counter
from typing import Any


class BM25Okapi:
    """Okapi BM25 over a tokenized corpus (list of list of str)."""

    def __init__(self, corpus: list[list[str]], k1: float = 1.5, b: float = 0.75) -> None:
        self.k1 = k1
        self.b = b
        self.corpus_size = len(corpus)
        if self.corpus_size == 0:
            raise ValueError("empty corpus")
        self.doc_len = [len(d) for d in corpus]
        self.avgdl = sum(self.doc_len) / self.corpus_size
        self.doc_terms = [Counter(d) for d in corpus]
        df = Counter()
        for d in corpus:
            df.update(set(d))
        self.idf = {}
        for term, freq in df.items():
            self.idf[term] = math.log((self.corpus_size - freq + 0.5) / (freq + 0.5) + 1.0)

    def get_scores(self, query: list[str]) -> list[float]:
        scores = [0.0] * self.corpus_size
        for q in query:
            idf = self.idf.get(q)
            if idf is None or idf <= 0:
                continue
            for i in range(self.corpus_size):
                tf = self.doc_terms[i].get(q, 0)
                if tf == 0:
                    continue
                dl = self.doc_len[i]
                denom = tf + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
                scores[i] += idf * (tf * (self.k1 + 1)) / denom
        return scores


def save_bm25(bundle: dict[str, Any], path: Any) -> None:
    with open(path, "wb") as f:
        pickle.dump(bundle, f, protocol=4)


def load_bm25(path: Any) -> dict[str, Any]:
    with open(path, "rb") as f:
        return pickle.load(f)
