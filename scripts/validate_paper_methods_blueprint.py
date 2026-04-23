#!/usr/bin/env python3
"""Check wiki paper pages against AGENTS.md Methods / Findings blueprints (heuristic).

Emits a markdown backlog: papers that likely need MD, FF-training, and/or DFT prose
but fail slot-coverage checks, plus thin Findings.

This is intentionally conservative: false positives go to the backlog for LLM/human
passes; tune CHECKLIST_* patterns if noise is too high.

Usage:
  python3 scripts/validate_paper_methods_blueprint.py
  python3 scripts/validate_paper_methods_blueprint.py -o outputs/paper_methods_blueprint_backlog.md
  python3 scripts/validate_paper_methods_blueprint.py --write-batches outputs/curation_batches/blueprint-fix-part
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from phase5_retrieval_lib import WIKI, parse_frontmatter

PAPERS = WIKI / "papers"
SKIP = {"index.md"}

# --- Applicability (from canonical_tags) ---

MD_METHOD_TAGS = frozenset(
    {
        "method:reaxff",
        "method:ereaxff",
        "method:classical-md",
        "method:aimd",
        "method:pimd",
        "method:reactive-md-generic",
        "method:enhanced-sampling",
    }
)


def tags_list(meta: dict) -> list[str]:
    t = meta.get("canonical_tags")
    if not isinstance(t, list):
        return []
    return [x for x in t if isinstance(x, str)]


def paper_kw(meta: dict) -> list[str]:
    k = meta.get("paper_keywords")
    if not isinstance(k, list):
        return []
    out = []
    for x in k:
        if isinstance(x, str):
            out.append(x.lower())
        elif isinstance(x, dict) and "keyword" in x:
            out.append(str(x["keyword"]).lower())
    return out


def extract_section(body: str, heading: str, stop_headings: tuple[str, ...]) -> str:
    """Return text from ## {heading} until next ## at same level."""
    start_re = re.compile(rf"^##\s+{re.escape(heading)}\s*$", re.MULTILINE | re.IGNORECASE)
    m = start_re.search(body)
    if not m:
        return ""
    start = m.end()
    rest = body[start:]
    stop_re = re.compile(r"^##\s+", re.MULTILINE)
    m2 = stop_re.search(rest)
    if m2:
        rest = rest[: m2.start()]
    return rest.strip()


def word_count(s: str) -> int:
    return len(re.findall(r"\S+", s))


def slot_match(text: str, patterns: tuple[re.Pattern[str], ...]) -> bool:
    return any(p.search(text) for p in patterns)


def md_barostat_ok(m: str) -> bool:
    if re.search(r"barostat|parrinello|aniso(stropic)?\s+stress", m, re.I):
        return True
    if re.search(r"\bnpt\b", m, re.I):
        return True
    if re.search(r"n/a.{0,60}(barostat|pressure\s+control|hydrostatic)", m, re.I | re.S):
        return True
    if re.search(r"\bnvt\b", m, re.I) and not re.search(r"\bnpt\b", m, re.I):
        return True
    if re.search(r"constant\s+volume", m, re.I):
        return True
    return False


def md_pressure_ok(m: str) -> bool:
    if re.search(r"pressure|stress\s+tensor|\bgpa\b|\bbar\b", m, re.I):
        return True
    if re.search(r"n/a.{0,50}pressure", m, re.I):
        return True
    if re.search(r"\bnpt\b", m, re.I):
        return True
    return False


def md_electric_ok(m: str) -> bool:
    if re.search(r"electric\s+field|efield|mv\s*/\s*cm|v\s*/\s*nm|field\s+coupling", m, re.I):
        return True
    if re.search(r"n/a.{0,50}(electric|field)", m, re.I):
        return True
    # If the study does not invoke fields, do not backlog on this slot.
    if not re.search(r"electric\s+field|efield|external\s+field|bias\s+voltage", m, re.I):
        return True
    return False


def md_enhanced_ok(m: str) -> bool:
    if re.search(
        r"umbrella|metadynamics|replica\s+exchange|accelerated\s+dynamics|hyperdynamics|"
        r"blue\s*moon|rare\s+event|commit\s+tor|bond\s+boost",
        m,
        re.I,
    ):
        return True
    if re.search(r"n/a.{0,50}(umbrella|metadynamic|replica|enhanced)", m, re.I):
        return True
    if not re.search(
        r"umbrella|metadynamics|replica\s+exchange|hyperdynamics|accelerated\s+dynamics", m, re.I
    ):
        return True
    return False


# Precompiled MD slot patterns (Methods text, case-insensitive via inline flags)
def md_slots(methods: str) -> dict[str, bool]:
    m = methods
    return {
        "engine": slot_match(
            m,
            (
                re.compile(r"lammps|gromacs|cp2k|\bnamd\b|\baimd\b|vasp.*md|cpmd|md\s+package", re.I),
                re.compile(r"molecular\s+dynamics|reactive\s+md|\bRMD\b", re.I),
            ),
        ),
        "system": slot_match(
            m,
            (
                re.compile(r"\batoms?\b|supercell|slab|stoichiometry|composition|unit\s+cell", re.I),
                re.compile(r"\b\d{2,5}\b.*\batoms?\b|\bnm\b", re.I),
            ),
        ),
        "boundary": slot_match(
            m,
            (
                re.compile(r"periodic|pbc|boundary|fixed\s+layer|frozen\s+atoms|non-?periodic", re.I),
            ),
        ),
        "ensemble": slot_match(m, (re.compile(r"\bnve\b|\bnvt\b|\bnpt\b|\bnph\b|microcanonical|canonical", re.I),)),
        "timestep": slot_match(
            m,
            (
                re.compile(r"time\s*step|timestep|\bfs\b|femtosecond|picosecond", re.I),
                re.compile(r"0\.\d+\s*fs", re.I),
            ),
        ),
        "duration": slot_match(
            m,
            (
                re.compile(r"\bps\b|\bns\b|equilibrat|production\s+run|multi-?stage|anneal", re.I),
                re.compile(r"duration|length\s+of|for\s+\d+", re.I),
            ),
        ),
        "thermostat": slot_match(
            m,
            (
                re.compile(
                    r"thermostat|berendsen|nose-?hoover|bussi|langevin|andersen|csvr", re.I
                ),
            ),
        ),
        "barostat": md_barostat_ok(m),
        "temperature": slot_match(
            m,
            (
                re.compile(r"\d+\s*K|temperature|thermal|hot|cold|anneal", re.I),
            ),
        ),
        "pressure": md_pressure_ok(m),
        "electric_field": md_electric_ok(m),
        "enhanced_sampling": md_enhanced_ok(m),
    }


def ff_slots(methods: str) -> dict[str, bool]:
    m = methods
    return {
        "parent_ff": slot_match(
            m,
            (
                re.compile(r"reaxff|force\s*field|parameter\s*set|comb\d|potential", re.I),
                re.compile(r"parent|starting|baseline|prior\s+parameter", re.I),
            ),
        ),
        "qm_reference": slot_match(
            m,
            (
                re.compile(r"\bDFT\b|density\s+functional|vasp|gaussian|qe\b|quantum\s+espresso", re.I),
                re.compile(r"PBE|B3LYP|LDA|hybrid|basis\s*set|k-?point|k-?mesh|cutoff", re.I),
            ),
        ),
        "training_set": slot_match(
            m,
            (
                re.compile(r"training|reference\s+data|reaction\s+set|equation\s+of\s+state|bulk\s+oxide", re.I),
                re.compile(r"structures?\s+(used|in)|fitting\s+set|data\s+set", re.I),
            ),
        ),
        "optimization": slot_match(
            m,
            (
                re.compile(r"genetic\s+algorithm|CMA-ES|least\s+squares|optimi[sz]e|parameter\s+fit", re.I),
                re.compile(r"parrex|reaxff\s+fit", re.I),
            ),
        ),
        "reference_data": slot_match(
            m,
            (
                re.compile(r"DFT|QM|experiment|benchmark|validation\s+set|reference\s+energ", re.I),
            ),
        ),
    }


def dft_slots(methods: str) -> dict[str, bool]:
    m = methods
    return {
        "functional": slot_match(m, (re.compile(r"functional|PBE|B3LYP|LDA|SCAN|r2SCAN|meta-?GGA", re.I),)),
        "dispersion": slot_match(
            m,
            (
                re.compile(r"dispersion|DFT-?D\d|vdW|van\s+der\s+waals|Grimme|n/a.{0,40}dispersion", re.I),
            ),
        ),
        "basis": slot_match(m, (re.compile(r"basis\s*set|plane-?wave|PAW|localized\s+basis", re.I),)),
        "k_sampling": slot_match(m, (re.compile(r"k-?point|k-?mesh|Brillouin|Γ-?only", re.I),)),
        "structures_pathways": slot_match(
            m,
            (
                re.compile(r"geometry|structure|pathway|NEB|transition\s+state|reaction\s+coordinate", re.I),
            ),
        ),
        "properties": slot_match(
            m,
            (
                re.compile(r"energy|barrier|frequency|DOS|band\s+gap|formation\s+energy|property", re.I),
            ),
        ),
    }


def findings_buckets(findings: str) -> dict[str, bool]:
    f = findings
    return {
        "outcomes_mechanisms": slot_match(
            f,
            (
                re.compile(
                    r"mechanism|kinetic|barrier|diffusion|interface|adsorb|react|growth|"
                    r"cluster|terrace|oxid|reduc|decompos",
                    re.I,
                ),
            ),
        ),
        "comparisons": slot_match(
            f,
            (
                re.compile(r"experiment|compared|agreement|benchmark|versus|vs\.|literature", re.I),
            ),
        ),
        "sensitivity": slot_match(
            f,
            (
                re.compile(
                    r"temperature|coverage|field|pressure|concentration|cycle|thickness|strain|"
                    r"rate|doping",
                    re.I,
                ),
            ),
        ),
        "limitations_outlook": slot_match(
            f,
            (
                re.compile(
                    r"limitation|caveat|future\s+work|open\s+question|however|although|uncertain", re.I
                ),
            ),
        ),
        "corpus_honesty": slot_match(
            f,
            (
                re.compile(
                    r"extract|galley|SI-?only|version-?of-?record|canonical|PDF|not\s+stated|"
                    r"proof\s+PDF|duplicate\s+PDF",
                    re.I,
                ),
            ),
        ),
    }


def analyze_paper(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    meta, body = parse_frontmatter(raw)
    slug = path.stem
    if meta.get("type") != "paper":
        return {"slug": slug, "skip": True}

    tags = set(tags_list(meta))
    methods = extract_section(body, "Methods", ())
    findings = extract_section(body, "Findings", ())

    review = "task:review" in tags

    needs_md = bool(tags & MD_METHOD_TAGS)
    needs_ff = "task:parameterization" in tags or any(
        "parameter" in k or "reaxff-parameterization" in k for k in paper_kw(meta)
    )
    needs_dft_only = (
        "method:dft-static" in tags
        and not (tags & MD_METHOD_TAGS)
        and "task:parameterization" not in tags
    )

    issues: list[str] = []

    if review:
        if word_count(methods) < 80:
            issues.append("review: Methods section thin (<80 words)")
        if word_count(findings) < 80:
            issues.append("review: Findings section thin (<80 words)")
    else:
        if needs_md:
            md = md_slots(methods)
            missing = [k for k, v in md.items() if not v]
            if missing:
                issues.append("MD blueprint gaps: " + ", ".join(missing))
        if needs_ff:
            ff = ff_slots(methods)
            missing = [k for k, v in ff.items() if not v]
            if len(missing) >= 3:
                issues.append("FF-training blueprint gaps: " + ", ".join(missing))
        if needs_dft_only:
            df = dft_slots(methods)
            missing = [k for k, v in df.items() if not v]
            if missing:
                issues.append("DFT-only blueprint gaps: " + ", ".join(missing))

        fb = findings_buckets(findings)
        thin = [k for k, v in fb.items() if not v]
        if len(thin) >= 4:
            issues.append("Findings blueprint gaps: " + ", ".join(thin))
        if word_count(findings) < 90 and len(thin) >= 3:
            issues.append(f"Findings short ({word_count(findings)} words) with multiple missing buckets")

    return {
        "slug": slug,
        "skip": False,
        "needs_md": needs_md,
        "needs_ff": needs_ff,
        "needs_dft_only": needs_dft_only,
        "review": review,
        "issues": issues,
        "fail": bool(issues),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "outputs" / "paper_methods_blueprint_backlog.md",
    )
    ap.add_argument(
        "--write-batches",
        type=Path,
        default=None,
        help="Prefix path; writes blueprint-fix-part-NN-of-15.txt (NN=01..15)",
    )
    ap.add_argument(
        "--check-slug",
        type=str,
        default=None,
        help="Validate one slug, print JSON line to stdout, exit 0 pass / 1 fail",
    )
    args = ap.parse_args()

    if args.check_slug:
        path = PAPERS / f"{args.check_slug}.md"
        if not path.is_file():
            print(f'{{"slug":"{args.check_slug}","error":"missing_file"}}')
            sys.exit(1)
        r = analyze_paper(path)
        import json as _json

        print(_json.dumps(r, ensure_ascii=False))
        sys.exit(1 if r.get("fail") else 0)

    results: list[dict] = []
    for path in sorted(PAPERS.glob("*.md")):
        if path.name in SKIP or path.name.startswith("._"):
            continue
        r = analyze_paper(path)
        if r.get("skip"):
            continue
        results.append(r)

    failed = [r for r in results if r["fail"]]
    failed.sort(key=lambda r: r["slug"])

    lines = [
        "# Paper Methods / Findings blueprint backlog",
        "",
        "Generated by `scripts/validate_paper_methods_blueprint.py` (heuristic slot coverage vs [`AGENTS.md`](../AGENTS.md) blueprints).",
        "",
        f"- **Total `paper:` pages scanned:** {len(results)}",
        f"- **Failing at least one check:** {len(failed)}",
        "",
        "Repair: for each slug, edit `## Methods` / `## Findings` so every applicable checklist line is **filled** or **`N/A — …`** per AGENTS, then re-run this script.",
        "",
        "## Failed papers",
        "",
        "| Slug | Flags | Issues |",
        "|------|-------|--------|",
    ]
    for r in failed:
        flags = []
        if r["review"]:
            flags.append("review")
        if r["needs_md"]:
            flags.append("MD")
        if r["needs_ff"]:
            flags.append("FF")
        if r["needs_dft_only"]:
            flags.append("DFT-only")
        iss = " ; ".join(r["issues"]).replace("|", "\\|")
        lines.append(f"| `{r['slug']}` | {', '.join(flags) or '—'} | {iss} |")

    lines.append("")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {args.output} — {len(failed)} failing of {len(results)}", file=sys.stderr)

    if args.write_batches and failed:
        n = len(failed)
        parts = 15
        base, extra = divmod(n, parts)
        sizes = [base + (1 if i < extra else 0) for i in range(parts)]
        idx = 0
        for part in range(1, parts + 1):
            sz = sizes[part - 1]
            chunk = [failed[idx + i]["slug"] for i in range(sz)]
            idx += sz
            out = Path(str(args.write_batches) + f"-{part:02d}-of-15.txt")
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text("\n".join(chunk) + ("\n" if chunk else ""), encoding="utf-8")
            print(f"wrote {out} ({len(chunk)} slugs)", file=sys.stderr)


if __name__ == "__main__":
    main()
