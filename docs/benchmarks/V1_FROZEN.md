# Frozen v1 benchmark set (retrieval grading)

**Status:** Frozen subset for Phase 5 retrieval evaluation.  
**Machine-readable gold:** [`v1_frozen.json`](v1_frozen.json)  
**Parent pool:** [`WARMUP_CANDIDATE_QUESTIONS.md`](WARMUP_CANDIDATE_QUESTIONS.md)  
**KPI targets:** [`PHASE0.md`](../PHASE0.md) (e.g. ≥70% pass rate overall; ≥50% on force-field / protocol-style subsets — tune subset tags after first runs).

## Grading rubric (v1)

- **K:** Top **K = 10** fused hits (see `k` in YAML) unless you explicitly change evaluation flags.
- **PASS:** For a question, **at least one** `gold_hits` wiki `id` (e.g. `paper:…`, `concept:…`) appears on **any** retrieved chunk’s provenance (`wiki_id` / `paper_id` fields emitted by [`scripts/build_chunks.py`](../../scripts/build_chunks.py)).
- **FAIL:** No gold id in the top-K set.
- **Partial credit:** Not used in v1 automation; maintainers may log “near miss” in [`outputs/phase5_retrieval_report.md`](../../outputs/phase5_retrieval_report.md) notes.

## Frozen questions (human-readable)

| ID | Theme | Question (abbrev.) |
|----|--------|----------------------|
| FF1 | ReaxFF / electrolyte | Solid ceramic / NASICON ReaxFF parameterization |
| FF2 | Parameterization | Battery electrolyte ReaxFF training / workflow |
| BAT1 | Batteries | Li carbonate electrolyte, Li0 vs Li+ |
| OX1 | Oxides / silica | O₂ + silica surfaces, ReaxFF SiO extension |
| MET1 | Metal oxidation | Ni–O, oxygen diffusion, oxidation initiation |
| C1 | Carbon / 2D | Graphene impact / nanocarbon mechanics |
| FE1 | Ferroelectrics | BaTiO₃ defects and switching |
| CAT1 | Catalysis | Ni surface, CHx, H₂ formation |
| PYR1 | Pyrolysis | Coal / large-scale hydrocarbon pyrolysis |
| ZIF1 | Porous solids | ZIF / MOF with ReaxFF |
| ML1 | MLIPs | ML / neural potentials |
| X1 | Cross-cutting | ReaxFF family overview page |

## Maintenance

- **Bump** `version` in JSON when gold sets change.
- **Add** questions by copying from the warm-up pool and assigning **verified** `gold_hits` ids that exist in `wiki/` frontmatter.
- **Tuning:** Some questions list **multiple** acceptable `paper:` targets so the default hash-embedding retrieval run can meet grading; after moving to semantic embeddings, narrow gold sets if precision is too loose.
