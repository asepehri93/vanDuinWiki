#!/usr/bin/env python3
"""Rename paper section headings and optionally enrich Methods/Findings from normalized extracts.

- Renames `## One-paragraph summary` → `## Summary` and updates Evidence admonition text.
- When `normalized/extracts/{slug}_p1-2.txt` exists, may append vetted bullets under Methods/Findings
  derived from the article abstract in the extract (heuristic; no LLM generation).

Idempotent: skips files that already contain `<!-- enrich-from-extract:v2 -->`.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI_PAPERS = ROOT / "wiki" / "papers"
EXTRACTS = ROOT / "normalized" / "extracts"

FINDING_SUB = "### Additional results (article abstract)"
ENRICH_MARKER = "<!-- enrich-from-extract:v2 -->"

# Match abstract opening only (avoid matching "ReaxFF" inside the article title block).
ABSTRACT_OPEN = re.compile(
    r"(?m)^\s*(We developed|We present|We study|We report|We consider|We find|Here, we|"
    r"In this (?:paper|study|work),|In this work|The present work|This paper|This work presents|"
    r"Atomistic-scale simulations|Reactive (?:force field|molecular dynamics))\b",
    re.I,
)

BAD_SENTENCE = re.compile(
    r"(?i)(university|department|journal is|owner societies|cite this|doi:|©|view article|"
    r"downloaded by|received \d|accepted \d|published on|rsc\.li|corresponding author|e-mail|"
    r"electronic supplementary|supporting information|y\s+kyung|^\s*Mert Y\.|"
    r"Pennsylvania State|View Journal|PCCP\s*$|PAPER\s*$)",
)

METHOD_KW = re.compile(
    r"(?i)(reaxff|reactive force|force field|dft|density functional|"
    r"molecular dynamics|aimd|training|parameter|optimized|fitted|fit to|monte carlo|"
    r"hybrid mc|simulation|nvt|npt|ensemble|potential energy|parameterization)",
)
FINDING_KW = re.compile(
    r"(?i)(conductivity|diffusion|barrier|demonstrat|show(s)?|found|obtain(ed)?|"
    r"agreement|calculated|predict|reveal|ionic|elastic|modulus|stress|"
    r"fracture|temperature\s+\d|10\s*[\u00d7×]|×\s*10| S\s*cm|cm\s*[\u2212\-]?1)",
)


def fix_ocr_text(s: str) -> str:
    s = re.sub(r"/C2\s*", "× ", s)
    s = re.sub(r"×\s*10\s*/C0\s*(\d+)", r"× 10−\1", s)
    s = re.sub(r"10\s+/C0\s*(\d+)", r"10−\1", s)
    s = re.sub(r"Sc\s+m\s+/C0\s*1", r"S cm−1", s)
    s = re.sub(r"/C0\s*1(?=\s*$)", r"−1", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def junk_sentence(s: str) -> bool:
    if "†" in s or "van Duin *" in s or "van Duin \*" in s:
        return True
    if BAD_SENTENCE.search(s):
        return True
    return False


def extract_abstract_sentences(raw: str) -> list[str]:
    t = raw.replace("\r\n", "\n")
    # ACS-style "ABSTRACT: …" blocks
    if re.search(r"(?m)^\s*ABSTRACT:\s*", t, re.I):
        t = re.split(r"(?i)ABSTRACT:\s*", t, maxsplit=1)[1]
    low = t.lower()
    cut = len(t)
    for marker in (
        "\n1. introduction",
        "\n1 introduction",
        "\n1. int.",
        "\nkeywords",
        "\nkey words",
    ):
        idx = low.find(marker)
        if idx != -1:
            cut = min(cut, idx)
    t = t[:cut]

    m = ABSTRACT_OPEN.search(t)
    if not m:
        m = re.search(
            r"(?m)^\s*(We developed|We present|We report|We study|We consider|We find|"
            r"Here, we|In this work|The present work|This work presents)\b",
            t,
            re.I,
        )
    if not m:
        m = re.search(
            r"\n\s*(We developed|We present|We report|We study|We consider)\b",
            t,
            re.I,
        )
    if not m:
        return []
    t = t[m.start() :]
    t = t.replace("\n", " ")
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(])", t)
    out: list[str] = []
    for p in parts:
        p = fix_ocr_text(p)
        if len(p) < 45 or len(p) > 800:
            continue
        if junk_sentence(p):
            continue
        if p.count(" ") < 7:
            continue
        out.append(p)
    return out


def classify_sentence(s: str) -> str:
    has_num = bool(re.search(r"\d", s))
    m_score = len(METHOD_KW.findall(s))
    f_score = len(FINDING_KW.findall(s)) + (1 if has_num and FINDING_KW.search(s) else 0)
    if m_score == 0 and f_score == 0:
        return "either"
    if m_score > f_score + 0:
        return "method"
    if f_score > m_score:
        return "finding"
    return "either"


def overlaps_existing(sentence: str, corpus: str) -> bool:
    """Skip when the full sentence (normalized whitespace) already appears in the wiki body."""
    s = " ".join(sentence.split()).lower()
    if len(s) < 35:
        return False
    c = " ".join(corpus.split()).lower()
    return s in c


def apply_heading_renames(raw: str) -> str:
    raw = raw.replace("## One-paragraph summary", "## Summary")
    raw = raw.replace(
        "(**One-paragraph summary**, **Methods**, **Findings**",
        "(**Summary**, **Methods**, **Findings**",
    )
    return raw


def enrich_body(raw: str, slug: str) -> tuple[str, bool]:
    if ENRICH_MARKER in raw or "<!-- enrich-from-extract:v1 -->" in raw:
        return raw, False
    ext = EXTRACTS / f"{slug}_p1-2.txt"
    if not ext.is_file():
        return raw, False
    sentences = extract_abstract_sentences(
        ext.read_text(encoding="utf-8", errors="replace")
    )
    if len(sentences) < 2:
        return raw, False

    # Avoid repeating text already in Summary + Methods + Findings
    pre_body = raw
    if "## Summary" in pre_body:
        pre_body = pre_body.split("## Summary", 1)[1]
    if "## Limitations" in pre_body:
        pre_body = pre_body.split("## Limitations", 1)[0]

    method_s: list[str] = []
    finding_s: list[str] = []
    either_s: list[str] = []
    for sent in sentences:
        if overlaps_existing(sent, pre_body):
            continue
        cls = classify_sentence(sent)
        if cls == "method":
            method_s.append(sent)
        elif cls == "finding":
            finding_s.append(sent)
        else:
            either_s.append(sent)

    mid = max(0, len(either_s) // 2)
    method_s.extend(either_s[:mid])
    finding_s.extend(either_s[mid:])

    def bullets(lines: list[str], max_items: int = 10) -> str:
        lines = lines[:max_items]
        if not lines:
            return ""
        return "\n".join(f"- {ln}" for ln in lines)

    mb = bullets(method_s)
    fb = bullets(finding_s)
    if not mb and not fb:
        return raw, False

    out = raw
    if mb:
        block = f"\n\n{ENRICH_MARKER}\n\n{mb}\n"
        out = re.sub(
            r"(## Methods\n)([\s\S]*?)(?=\n## Findings\n)",
            lambda m: m.group(1) + m.group(2).rstrip() + block + "\n",
            out,
            count=1,
        )
    if fb:
        if mb:
            block = f"\n\n{FINDING_SUB}\n\n{fb}\n"
        else:
            block = f"\n\n{ENRICH_MARKER}\n\n{FINDING_SUB}\n\n{fb}\n"
        out = re.sub(
            r"(## Findings\n)([\s\S]*?)(?=\n## Limitations\n|\n## Limitation\n)",
            lambda m: m.group(1) + m.group(2).rstrip() + block + "\n",
            out,
            count=1,
        )
    if out == raw:
        return raw, False
    return out, True


def main() -> None:
    dry = "--dry-run" in sys.argv
    n_rename = 0
    n_enrich = 0
    for path in sorted(WIKI_PAPERS.glob("*.md")):
        if path.name == "index.md":
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        if "type: paper" not in raw[:1200]:
            continue
        new_raw = apply_heading_renames(raw)
        slug = path.stem
        new_raw, did = enrich_body(new_raw, slug)
        if new_raw != raw:
            n_rename += 1
            if did:
                n_enrich += 1
            if not dry:
                path.write_text(new_raw, encoding="utf-8")
    print(
        f"processed paper pages: {n_rename} updated"
        + (f" ({n_enrich} extract-enriched)" if n_enrich else "")
        + (" [dry-run]" if dry else "")
    )


if __name__ == "__main__":
    main()
