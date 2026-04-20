#!/usr/bin/env python3
"""Grade hybrid retrieval against docs/benchmarks/v1_frozen.json (stdlib)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "docs" / "benchmarks" / "v1_frozen.json"
OUTPUT = ROOT / "outputs" / "phase5_retrieval_report.md"

from search_hybrid import search  # noqa: E402


def hit_matches_gold(hit: dict, gold_ids: set[str]) -> bool:
    w = hit.get("wiki_id")
    p = hit.get("paper_id")
    if w and w in gold_ids:
        return True
    if p and p in gold_ids:
        return True
    return False


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=OUTPUT)
    args = ap.parse_args()

    spec = json.loads(BENCHMARK.read_text(encoding="utf-8"))
    k = int(spec.get("k", 10))
    rrf_k = float(spec.get("rrf_k", 60))
    questions = spec.get("questions", [])

    lines: list[str] = []
    lines.append("# Phase 5 retrieval report (automated)")
    lines.append("")
    lines.append(f"- Benchmark: `{BENCHMARK.relative_to(ROOT)}`")
    lines.append(f"- Top-K: **{k}**")
    lines.append("")

    passed = 0
    for q in questions:
        qid = q.get("id", "?")
        text = q.get("text", "")
        gold = set()
        for g in q.get("gold_hits", []):
            if isinstance(g, dict) and "id" in g:
                gold.add(g["id"])
        hits = search(text, top_k=k, rrf_k=rrf_k)
        ok = any(hit_matches_gold(h, gold) for h in hits)
        if ok:
            passed += 1
        status = "PASS" if ok else "FAIL"
        lines.append(f"## {qid} — {status}")
        lines.append("")
        lines.append(f"**Q:** {text}")
        lines.append("")
        lines.append(f"**Gold:** `{gold}`")
        lines.append("")
        lines.append("| rrf | chunk_id | path | wiki_id |")
        lines.append("|-----|----------|------|---------|")
        for h in hits[:k]:
            lines.append(
                f"| {h.get('rrf_score', 0):.4f} | {h.get('chunk_id')} | {h.get('wiki_path')} | {h.get('wiki_id')} |"
            )
        lines.append("")

    total = len(questions)
    rate = (passed / total * 100.0) if total else 0.0
    lines.insert(4, f"- **Pass rate:** {passed}/{total} ({rate:.1f}%)")
    lines.insert(5, "")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.output} — pass {passed}/{total} ({rate:.1f}%)")


if __name__ == "__main__":
    main()
