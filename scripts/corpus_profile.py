#!/usr/bin/env python3
"""
Phase 3 corpus profiling: scan papers/, hash PDFs, extract metadata + first pages text,
assign paper:{slug}, write raw/MANIFEST.jsonl and normalized/papers/{slug}.json,
emit outputs/corpus_profile_*.md, normalized/corpus_summary.json, outputs/ingest_exceptions.md.

Run from repo root: python3 scripts/corpus_profile.py
Requires vendored pypdf at .vendor/pypdf (sys.path).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
VENDOR = REPO_ROOT / ".vendor"
if VENDOR.is_dir():
    sys.path.insert(0, str(VENDOR))

from pypdf import PdfReader  # noqa: E402
from pypdf.errors import PdfReadError  # noqa: E402

STOPWORDS = frozenset(
    "the a an on in at to for of and or as by with from into via over per vs".split()
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def slugify_token(s: str, max_len: int = 32) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    if not s:
        return "x"
    return s[:max_len].rstrip("-")


def year_from_text(*texts: str) -> int | None:
    for t in texts:
        if not t:
            continue
        for m in re.finditer(r"(19|20)\d{2}", t):
            y = int(m.group(0))
            if 1980 <= y <= datetime.now().year + 1:
                return y
    return None


def first_author_slug(author_raw: str | None, filename_stem: str) -> str:
    if author_raw:
        # "Smith, J." or "Smith J" or "J. Smith"
        a = author_raw.split(";")[0].split(" and ")[0].strip()
        if "," in a:
            last = a.split(",")[0].strip()
        else:
            parts = a.split()
            last = parts[-1] if parts else a
        tok = slugify_token(last, 20)
        if tok != "x":
            return tok
    # Filename often Author_Journal_Year
    stem = filename_stem.replace(" ", "_")
    first = stem.split("_")[0] if "_" in stem else stem
    return slugify_token(first, 20) or "unknown"


def title_tokens(title: str | None, max_parts: int = 2) -> str:
    if not title:
        return "paper"
    words = re.findall(r"[A-Za-z][a-z0-9+-]*", title.lower())
    picked: list[str] = []
    for w in words:
        if w in STOPWORDS or len(w) < 2:
            continue
        picked.append(w)
        if len(picked) >= max_parts:
            break
    if not picked:
        picked = [words[0]] if words else ["paper"]
    return "-".join(picked)[:40]


def venue_token(journal: str | None, title: str | None) -> str:
    if journal:
        j = journal.lower()
        for hint in ("jcp", "jctc", "jpcl", "jpcc", "jpc", "pccp", "prb", "prl", "nat", "acs", "angew"):
            if hint in j:
                return hint
        return slugify_token(journal, 12)
    return "venue"


def unique_slug(base: str, seen_slugs: set[str]) -> str:
    b = slugify_token(base, 80) or "paper"
    candidate = b
    n = 2
    while candidate in seen_slugs:
        suffix = f"-{n}"
        candidate = slugify_token(b + suffix, 80) or f"{b}-{n}"
        n += 1
    seen_slugs.add(candidate)
    return candidate


def assign_slug(
    meta: dict[str, Any],
    filename_stem: str,
    seen_slugs: set[str],
) -> str:
    year = meta.get("year")
    if year is None:
        year = year_from_text(filename_stem) or 0
    author = first_author_slug(meta.get("authors"), filename_stem)
    tt = title_tokens(meta.get("title"))
    vt = venue_token(meta.get("venue"), meta.get("title"))
    if year and year > 0:
        base = f"{year}{author}_{vt}-{tt}"
    else:
        base = f"noyear-{author}-{slugify_token(filename_stem, 40)}"
    return unique_slug(base, seen_slugs)


def pdf_info(reader: PdfReader) -> dict[str, Any]:
    out: dict[str, Any] = {
        "title": None,
        "authors": None,
        "subject": None,
        "keywords": None,
        "creator": None,
        "producer": None,
        "creation_date": None,
    }
    meta = reader.metadata
    if meta is None:
        return out
    try:
        out["title"] = getattr(meta, "title", None) or None
        out["authors"] = getattr(meta, "author", None) or None
        out["subject"] = getattr(meta, "subject", None) or None
        out["keywords"] = getattr(meta, "keywords", None) or None
        out["creator"] = getattr(meta, "creator", None) or None
        out["producer"] = getattr(meta, "producer", None) or None
        out["creation_date"] = getattr(meta, "creation_date", None) or None
    except Exception:
        pass
    return out


def extract_first_pages_text(reader: PdfReader, max_pages: int = 2) -> str:
    parts: list[str] = []
    n = min(len(reader.pages), max_pages)
    for i in range(n):
        try:
            t = reader.pages[i].extract_text() or ""
        except Exception:
            t = ""
        parts.append(t)
    return "\n\n".join(parts)


def extraction_quality(meta: dict[str, Any], text: str) -> str:
    has_title = bool(meta.get("title"))
    has_auth = bool(meta.get("authors"))
    text_ok = len(text.strip()) > 200
    if has_title and (has_auth or text_ok):
        return "good"
    if has_title or has_auth or text_ok:
        return "partial"
    if len(text.strip()) > 50:
        return "partial"
    return "poor"


def discover_pdfs(papers_dir: Path) -> list[Path]:
    out: list[Path] = []
    for p in sorted(papers_dir.rglob("*")):
        if not p.is_file():
            continue
        name = p.name
        if name.startswith("._"):
            continue
        if name.lower().endswith(".pdf"):
            out.append(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=REPO_ROOT)
    ap.add_argument("--dry-run", action="store_true", help="Print counts only")
    args = ap.parse_args()
    repo: Path = args.repo.resolve()
    papers_dir = repo / "papers"
    if not papers_dir.is_dir():
        print("Missing papers/", file=sys.stderr)
        return 1

    pdfs = discover_pdfs(papers_dir)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    profile_date = datetime.now(timezone.utc).strftime("%Y-%m")

    hash_to_paths: dict[str, list[str]] = defaultdict(list)
    records: list[dict[str, Any]] = []
    exceptions: list[str] = []

    seen_slugs: set[str] = set()

    for pdf_path in pdfs:
        rel = str(pdf_path.relative_to(repo))
        try:
            digest = sha256_file(pdf_path)
        except OSError as e:
            exceptions.append(f"- **read error** `{rel}`: {e}")
            continue
        hash_to_paths[digest].append(rel)

        meta_plain: dict[str, Any] = {
            "title": None,
            "authors": None,
            "year": None,
            "doi": None,
            "venue": None,
        }
        text_preview = ""
        eq = "unknown"
        try:
            reader = PdfReader(str(pdf_path))
            info = pdf_info(reader)
            meta_plain["title"] = info["title"]
            meta_plain["authors"] = info["authors"]
            meta_plain["venue"] = info.get("subject")  # sometimes journal in subject
            # crude DOI from first pages
            text_preview = extract_first_pages_text(reader, 2)
            cd = info.get("creation_date")
            cd_str = str(cd) if cd is not None else ""
            y = year_from_text(
                cd_str,
                text_preview[:800],
                pdf_path.stem,
            )
            meta_plain["year"] = y
            doi_m = re.search(
                r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", text_preview[:4000]
            ) or re.search(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", pdf_path.stem)
            if doi_m:
                meta_plain["doi"] = doi_m.group(0).rstrip(").,]")

            eq = extraction_quality(
                {"title": info["title"], "authors": info["authors"]},
                text_preview,
            )
        except PdfReadError as e:
            exceptions.append(f"- **PdfReadError** `{rel}`: {e}")
            eq = "poor"
        except Exception as e:
            exceptions.append(f"- **extract error** `{rel}`: {e}")
            eq = "poor"

        if meta_plain.get("year") is None:
            meta_plain["year"] = year_from_text(pdf_path.stem)

        slug = assign_slug(meta_plain, pdf_path.stem, seen_slugs)
        paper_id = f"paper:{slug}"

        rec = {
            "rel_path": rel,
            "digest": digest,
            "slug": slug,
            "paper_id": paper_id,
            "bibliography": {
                "title": meta_plain.get("title"),
                "authors": meta_plain.get("authors"),
                "year": meta_plain.get("year"),
                "doi": meta_plain.get("doi"),
                "venue": meta_plain.get("venue"),
            },
            "extraction_quality": eq,
            "text_preview": text_preview[:8000],
            "ingested_at": now,
        }
        records.append(rec)

    # Dedupe report
    dupes = {h: paths for h, paths in hash_to_paths.items() if len(paths) > 1}
    for h, paths in sorted(dupes.items(), key=lambda x: -len(x[1])):
        exceptions.append(
            f"- **duplicate hash** `{h[:12]}…` ({len(paths)} files): "
            + ", ".join(f"`{p}`" for p in paths[:5])
            + (" …" if len(paths) > 5 else "")
        )

    if args.dry_run:
        print(f"PDFs: {len(pdfs)}, records: {len(records)}, dup groups: {len(dupes)}")
        return 0

    # Write manifest
    manifest_path = repo / "raw" / "MANIFEST.jsonl"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8") as mf:
        for rec in records:
            line = {
                "source_path": rec["rel_path"],
                "sha256": rec["digest"],
                "ingested_at": rec["ingested_at"],
                "paper_id": rec["paper_id"],
                "notes": None,
            }
            mf.write(json.dumps(line, ensure_ascii=False) + "\n")

    # Normalized JSON + optional extract files
    norm_dir = repo / "normalized" / "papers"
    extracts_dir = repo / "normalized" / "extracts"
    extracts_dir.mkdir(parents=True, exist_ok=True)
    norm_dir.mkdir(parents=True, exist_ok=True)

    for rec in records:
        slug = rec["slug"]
        tp = rec.get("text_preview") or ""
        extract_rel = f"normalized/extracts/{slug}_p1-2.txt"
        extract_path = repo / extract_rel
        try:
            extract_path.write_text(tp, encoding="utf-8", errors="replace")
        except OSError:
            pass

        norm_doc = {
            "paper_id": rec["paper_id"],
            "manifest": {
                "source_path": rec["rel_path"],
                "sha256": rec["digest"],
                "ingested_at": rec["ingested_at"],
            },
            "bibliography": {
                "doi": rec["bibliography"].get("doi"),
                "title": rec["bibliography"].get("title"),
                "year": rec["bibliography"].get("year"),
                "authors": rec["bibliography"].get("authors"),
                "venue": rec["bibliography"].get("venue"),
            },
            "pdf_path": rec["rel_path"],
            "extraction": {
                "text_path": extract_rel if extract_path.exists() else None,
                "quality": rec["extraction_quality"],
                "extracted_at": rec["ingested_at"],
                "text_preview_chars": len(tp),
            },
            "entities_mentioned": [],
            "claims": [],
            "wiki_path": f"wiki/papers/{slug}.md",
            "updated": rec["ingested_at"],
        }
        out_json = norm_dir / f"{slug}.json"
        out_json.write_text(
            json.dumps(norm_doc, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    # corpus_summary.json
    years: Counter[int | str] = Counter()
    qualities = Counter()
    title_words: Counter[str] = Counter()
    for rec in records:
        y = rec["bibliography"].get("year")
        if y:
            years[int(y)] += 1
        else:
            years["unknown"] += 1
        qualities[rec["extraction_quality"]] += 1
        t = rec["bibliography"].get("title") or ""
        for w in re.findall(r"[A-Za-z][a-z0-9+-]{3,}", t.lower()):
            if w not in STOPWORDS:
                title_words[w] += 1

    summary = {
        "generated_at": now,
        "profile_version": 1,
        "paper_count": len(records),
        "pdf_files_scanned": len(pdfs),
        "duplicate_hash_groups": len(dupes),
        "years_histogram": {str(k): v for k, v in sorted(years.items(), key=lambda x: (str(x[0]),))},
        "extraction_quality": dict(qualities),
        "top_title_words": title_words.most_common(60),
    }
    (repo / "normalized" / "corpus_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Markdown profile
    prof_path = repo / "outputs" / f"corpus_profile_{profile_date}.md"
    lines = [
        f"# Corpus profile ({profile_date})",
        "",
        f"- Generated: `{now}`",
        f"- Papers registered: **{len(records)}**",
        f"- PDF files scanned: **{len(pdfs)}**",
        f"- Duplicate content hashes: **{len(dupes)}** groups (see ingest_exceptions)",
        "",
        "## Extraction quality",
        "",
        "| Quality | Count |",
        "|---------|-------|",
    ]
    for q, c in sorted(qualities.items(), key=lambda x: -x[1]):
        lines.append(f"| {q} | {c} |")
    lines.extend(["", "## Year distribution (from metadata / text / filename)", "", "| Year | Count |", "|------|-------|"])
    for y, c in sorted(
        ((k, v) for k, v in years.items() if k != "unknown"),
        key=lambda x: (x[0] if isinstance(x[0], int) else 0,),
    ):
        lines.append(f"| {y} | {c} |")
    if "unknown" in years:
        lines.append(f"| unknown | {years['unknown']} |")
    lines.extend(["", "## Top words in PDF titles (metadata)", ""])
    for w, c in title_words.most_common(40):
        lines.append(f"- {w}: {c}")
    lines.extend(
        [
            "",
            "## Artifacts",
            "",
            f"- [`raw/MANIFEST.jsonl`](../raw/MANIFEST.jsonl)",
            f"- [`normalized/corpus_summary.json`](../normalized/corpus_summary.json)",
            f"- One JSON per paper: [`normalized/papers/`](../normalized/papers/)",
            f"- First-two-page text extracts: [`normalized/extracts/`](../normalized/extracts/) (gitignored)",
            "",
        ]
    )
    prof_path.write_text("\n".join(lines), encoding="utf-8")

    # ingest_exceptions.md
    exc_path = repo / "outputs" / "ingest_exceptions.md"
    exc_body = "\n".join(
        [
            "# Ingest exceptions (Phase 3)",
            "",
            f"Generated: `{now}`",
            "",
            "## Notes",
            "",
            "- Duplicate hashes may indicate proofs + final, or copied files; keep manifest rows for each path or dedupe manually.",
            "",
            "## Issues",
            "",
        ]
        + (exceptions if exceptions else ["- None."])
        + ["",]
    )
    exc_path.write_text(exc_body, encoding="utf-8")

    print(f"Wrote {len(records)} manifest rows and normalized records.")
    print(f"Profile: {prof_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
