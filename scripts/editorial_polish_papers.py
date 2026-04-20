#!/usr/bin/env python3
"""Editorial pass on wiki/papers/*.md: objective voice, merged extract prose, cleanup.

Run from repo root: python3 scripts/editorial_polish_papers.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "wiki" / "papers"

SUBSTITUTIONS: list[tuple[str, str]] = [
    (r"(?m)^The authors simulate\b", "The study simulates"),
    (r"(?m)^The authors develop\b", "The work develops"),
    (r"(?m)^The authors report\b", "The study reports"),
    (r"(?m)^The authors use\b", "The study uses"),
    (r"(?m)^The authors present\b", "The work presents"),
    (r"(?m)^The authors introduce\b", "The work introduces"),
    (r"(?m)^The authors apply\b", "The study applies"),
    (r"(?m)^The authors run\b", "The study uses large-scale MD to run"),
    (r"(?m)^The authors argue\b", "The analysis suggests"),
    (r"(?m)^The authors find\b", "The simulations show"),
    (r"(?m)^The authors relate\b", "The study relates"),
    (r"(?m)^The authors connect\b", "The work connects"),
    (r"(?m)^The authors benchmark\b", "The study benchmarks"),
    (r"(?i)\bIn this work, the authors have developed\b", "This work develops"),
    (r"(?i)\bthe authors have developed\b", "this work develops"),
    (r"(?m)^The authors declare\b.*\n?", ""),
    (r"(?i)\. The authors ", ". The study "),
    (r"(?i); the authors ", "; the study "),
    (r"(?i): the authors ", ": the study "),
]


def fix_escapes(s: str) -> str:
    s = re.sub(r"ReaxFF\\_SiO", "ReaxFF–SiO", s)
    s = re.sub(r"ReaxFF\_SiO", "ReaxFF–SiO", s)
    s = re.sub(r"\\_GSI", "–GSI", s)
    return s


def neutralize_sentence(t: str) -> str:
    t = re.sub(
        r"^We developed a ReaxFF\b",
        "The work develops a ReaxFF",
        t,
        flags=re.I,
    )
    t = re.sub(r"^We developed\b", "The parametrization extends", t, flags=re.I)
    t = re.sub(r"^We present\b", "The article presents", t, flags=re.I)
    t = re.sub(r"^We report\b", "The study reports", t, flags=re.I)
    t = re.sub(r"^We study\b", "The analysis examines", t, flags=re.I)
    t = re.sub(r"^We find\b", "The simulations show", t, flags=re.I)
    t = re.sub(r"^Using this force field,\s*", "Using this parameterization, ", t, flags=re.I)
    t = re.sub(r"^Using ReaxFF,\s*", "With ReaxFF, ", t, flags=re.I)
    t = re.sub(r"\bour experimental value\b", "the experimental value reported in the article", t, flags=re.I)
    t = re.sub(r"\bour results\b", "the reported results", t, flags=re.I)
    t = re.sub(r"\bwe identified\b", "the simulations identified", t, flags=re.I)
    t = re.sub(r"\bwe obtain(ed)?\b", "the study obtained", t, flags=re.I)
    t = re.sub(r"\bin our simulations\b", "in the reported simulations", t, flags=re.I)
    t = re.sub(r"\bDuring the process of projectile penetration, we\b", "During projectile penetration, the simulations", t, flags=re.I)
    return t


def bullets_to_paragraph(lines: list[str]) -> str:
    parts: list[str] = []
    for raw in lines:
        t = raw.strip()
        if not t.startswith("- "):
            continue
        t = neutralize_sentence(t[2:].strip())
        if not t.endswith((".", "!", "?")):
            t += "."
        parts.append(t)
    if not parts:
        return ""
    return " ".join(parts)


def merge_method_enrich_block(text: str) -> str:
    m = re.search(
        r"<!-- enrich-from-extract:v2 -->\n\n([\s\S]*?)(?=\n## Findings\n)",
        text,
    )
    if not m:
        return text
    bullets_block = m.group(1)
    lines = [ln for ln in bullets_block.splitlines() if ln.strip()]
    para = bullets_to_paragraph(lines)
    if not para:
        return text
    lead = "The article further notes that "
    merged = lead + para[0].lower() + para[1:]
    return text[: m.start()] + merged + "\n" + text[m.end() :]


def merge_additional_results(text: str) -> str:
    m = re.search(
        r"\n### Additional results \(article abstract\)\n\n([\s\S]*?)(?=\n## Limitations\n)",
        text,
    )
    if not m:
        return text
    bullets_block = m.group(1)
    lines = [ln for ln in bullets_block.splitlines() if ln.strip()]
    para = bullets_to_paragraph(lines)
    if not para:
        return text
    lead = "\n\nFrom the abstract: "
    merged = lead + para[0].lower() + para[1:] + "\n"
    return text[: m.start()] + merged + text[m.end() :]


def filter_junk_lines(text: str) -> str:
    out: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        low = s.lower()
        if "author contributions:" in low or "author contributions :" in low:
            continue
        if "to whom correspondence" in low:
            continue
        if "conflict of interest" in low and ("declare" in low or "no conflict" in low):
            continue
        if "the authors declare" in low:
            continue
        if low.startswith("of the four author"):
            continue
        out.append(line)
    return "\n".join(out)


def polish(text: str) -> str:
    text = fix_escapes(text)
    for pat, rep in SUBSTITUTIONS:
        text = re.sub(pat, rep, text)
    text = filter_junk_lines(text)
    if "### Additional results (article abstract)" in text:
        text = merge_additional_results(text)
    if "<!-- enrich-from-extract:v2 -->" in text:
        text = merge_method_enrich_block(text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text


def main() -> None:
    dry = "--dry-run" in sys.argv
    n = 0
    for path in sorted(PAPERS.glob("*.md")):
        if path.name == "index.md":
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        if not raw.startswith("---"):
            continue
        try:
            fm = raw.split("---", 2)[1]
        except IndexError:
            continue
        if "type: paper" not in fm:
            continue
        new = polish(raw)
        if new != raw:
            n += 1
            if not dry:
                path.write_text(new, encoding="utf-8")
    print(f"polished {n} paper files" + (" [dry-run]" if dry else ""))


if __name__ == "__main__":
    main()
