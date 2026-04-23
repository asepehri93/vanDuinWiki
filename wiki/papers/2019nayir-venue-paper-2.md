---
id: paper:2019nayir-venue-paper-2
type: paper
title: "Development of the ReaxFF Reactive Force Field for Inherent Point Defects in the Si/Silica System (publisher proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - task:parameterization
  - task:validation
  - material:silicate-glass
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.9b01481"
year: 2019
authors:
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
  - "Sakir Erkoc"
venue: "J. Phys. Chem. A"
pdf_sha256: "0b7991cd34895da73cd30a0abbfc4833fc5594e694c5cf712d44f643e2d97251"
pdf_path: "papers/Nayir_JPC_C_SiOx_2019_edit_trace.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2019nayir-venue-paper-2 -->

## Evidence and attribution

!!! note "Editorial proof / edit trace"

    This PDF contains **publisher query markup** overlaid on the **J. Phys. Chem. A** article also summarized under **`[[2019nayir-j-phys-chem-development-reaxff-2]]`**. Scientific content is duplicated from that **version-of-record** page; this slug records **`papers/Nayir_JPC_C_SiOx_2019_edit_trace.pdf`** for provenance. A separate SI-focused ingest exists as **`[[2019nayir-venue-paper]]`** per [`NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Summary

The peer-reviewed article reoptimizes ReaxFF parameters for Si/O/H with emphasis on oxygen interstitials in crystalline silicon, migration pathways, and oxidation chemistry at amorphous silica–silicon interfaces. The prior SiOH(2010) parameterization spuriously allowed deep oxygen superdiffusion at 300 K; the new “ReaxFFpresent” set reproduces bond-centered hopping of oxygen in silicon with a barrier near 64.8 kcal mol⁻¹ in the abstract’s comparison to DFT and experiment, and restores physically plausible temperature thresholds for significant diffusion. Annealing tests on a-SiO₂/Si stacks recover interfacial oxygen transport behavior closer to literature expectations.

## Methods

**PDF note.** This file is a **publisher proof / edit-trace** duplicate of the J. Phys. Chem. A article; for stable figures and numbers use **`[[2019nayir-j-phys-chem-development-reaxff-2]]`** and the clean **VOR** PDF, not the overlay markup here.

**1 — MD application (ReaxFF).** The article reports **reactive MD** to validate **O** **diffusion** in **bulk Si**, **a-SiO₂** behavior, and **a-SiO₂/Si** **stack** **annealing** after the **ReaxFF** refit. **Engine:** **ReaxFF**-style workflows in **LAMMPS** / **ADF** contexts as stated in the main text. **System / boundary / ensemble / timestep / thermostat / duration:** take from the main article and SI (this proof PDF is **not** the primary protocol source); **N/A** to list line-by-line on this **galley** slug. **Barostat / pressure in MD:** **N/A** unless the main text used **NPT** for a stated segment—confirm on the VOR. **Electric field, shear, enhanced sampling:** **N/A** in the abstract-level summary on this page.

**2 — Force-field training (Si/O/H).** The work **reoptimizes** **ReaxFF** **Si/O/H** for **O** **interstitials** and **interface** oxidation, starting from prior **Si**/**silica** **fits**; **DFT** **training** sets and **CMA-ES** (or related) **optimization** are in the main paper. The abstract contrasts **ReaxFFpresent** with **SiOH(2010)** and reports a **bond-centered** **O** barrier near **~64.8 kcal/mol** vs **DFT**/**literature** in their comparison. **Reference** **QM** and **validation** data are specified in the article; this proof page does not replace the typeset **Table**/**SI** line numbers.

**3 — Static QM / DFT-only block.** As used in **training** and **benchmarks** in the main paper, not re-derived here. **N/A** as a standalone DFT **Methods** list on this slug.

**4 — Review.** **N/A.**

**MD details (galley honesty).** **Atom** counts, **supercell** sizes, **3D** **PBC**, **NVT**/**NPT** **ensemble**, **timestep** **fs**, **equilibration**/**production** **ns**, **thermostat** parameters, and **barostat**/ **pressure** **GPa** targets are given in the **main** **VOR** **PDF**—**N/A** to recopy from this **edit**-**trace** file; **molecular** **dynamics** in **LAMMPS**/ADF as in the **article**.
## Findings

O migration in bulk Si proceeds via bond-centered hops in the (110) plane with an asymmetric saddle geometry; significant diffusion initiates above roughly 1400 K in their analysis, with diffusion coefficients tracking experimental trends. Amorphous silica density matches experiment closely. The revised force field removes the unphysical room-temperature superdiffusion artifact of SiOH(2010).

Interface annealing tests demonstrate that the new parametrization preserves realistic oxygen transport between amorphous silica and silicon without spurious low-temperature leakage, which is critical for gate-stack and oxidation simulations used throughout the Si technology path.

## Limitations

Proof PDF may contain duplicated lines from editorial tooling; cite figures from the clean article PDF. Parameter transfer to alkali-bearing glasses requires separate tests.

## Corpus notes

Link resolution in Obsidian should prefer **`[[2019nayir-j-phys-chem-development-reaxff-2]]`** for readers who need stable figure references; keep this slug for editorial-trace provenance only.

If automated PDF text extraction reintroduces duplicated lines into `normalized/extracts`, strip those artifacts with `scripts/strip_paste_artifacts.py` before regenerating chunks, per `AGENTS.md` hygiene guidance.

## Relevance to group

Core **Si/SiO₂** defect parametrization for oxidation and gate-stack modeling; this slug is **non-primary** file packaging only.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.9b01481](https://doi.org/10.1021/acs.jpca.9b01481)
- Canonical wiki: [[2019nayir-j-phys-chem-development-reaxff-2]]

## Related topics

- [[reaxff-family]]
- [[2019nayir-j-phys-chem-development-reaxff-2]]
