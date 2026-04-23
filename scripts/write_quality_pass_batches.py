#!/usr/bin/env python3
"""Emit slug lists for final paper wiki quality pass: 5 waves × 15 parts (deterministic)."""

from __future__ import annotations

import argparse
from pathlib import Path


def chunk_list(lst: list, n: int) -> list[list]:
    if n <= 0:
        raise ValueError("n must be positive")
    size, rem = divmod(len(lst), n)
    out: list[list] = []
    i = 0
    for j in range(n):
        take = size + (1 if j < rem else 0)
        out.append(lst[i : i + take])
        i += take
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--wiki-papers",
        type=Path,
        default=Path("wiki/papers"),
        help="Directory of paper markdown files",
    )
    p.add_argument(
        "--out-dir",
        type=Path,
        default=Path("outputs/curation_batches"),
        help="Where to write quality-final-wave*-part-*-of-15.txt",
    )
    p.add_argument("--waves", type=int, default=5)
    p.add_argument("--parts", type=int, default=15)
    args = p.parse_args()

    stems = sorted(
        x.stem
        for x in args.wiki_papers.glob("*.md")
        if not x.name.startswith("._") and not x.stem.startswith("._")
    )
    if not stems:
        raise SystemExit(f"No .md under {args.wiki_papers}")

    waves = chunk_list(stems, args.waves)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    for wi, wave_slugs in enumerate(waves, start=1):
        parts = chunk_list(wave_slugs, args.parts)
        for pi, part in enumerate(parts, start=1):
            path = args.out_dir / f"quality-final-wave{wi}-part{pi:02d}-of-{args.parts}.txt"
            path.write_text("\n".join(part) + ("\n" if part else ""), encoding="utf-8")
            print(f"wrote {path} ({len(part)} slugs)")

    total = sum(len(w) for w in waves)
    print(f"total slugs: {total} ({args.waves} waves × up to {args.parts} parts)")


if __name__ == "__main__":
    main()
