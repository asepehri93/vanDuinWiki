---
id: paper:2021akbarian-venue-paper
type: paper
title: "Understanding physical chemistry of BaxSr1−xTiO3 using ReaxFF molecular dynamics simulations (publisher proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - domain:reaxff-lineage
  - material:perovskite-oxide
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
candidate_tags: []
source_refs: []
doi: "10.1039/D1CP03353K"
year: 2021
authors:
  - "Dooman Akbarian"
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "6dea2d15545e7ea05ba60bf17a4b2158dec911b447fb0d85acb3d5ffdeb09f4f"
pdf_path: "papers/Akbarian_BaSrTiO3_PCCP_2021_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2021akbarian-venue-paper -->

??? info "PDF variant"
    RSC **layout proof** (`d1cp03353k`). Full article text: [[2021akbarian-physical-che-understanding-physical]] (`papers/Akbarian_BaSrTiO3_PCCP_2021.pdf`).

## Summary

The proof PDF `papers/Akbarian_BaSrTiO3_PCCP_2021_galley.pdf` belongs to the PCCP article DOI `10.1039/D1CP03353K`, “Understanding physical chemistry of BaₓSr₁₋ₓTiO₃ using ReaxFF molecular dynamics simulations.” The extract (`normalized/extracts/2021akbarian-venue-paper_p1-2.txt`) is dominated by RSC **layout proof** instructions (online proofing interface, “Edit” button workflow, note that online changes may not appear in the PDF proof). It also includes the **graphical abstract** text block: **“Understanding physical chemistry of BaₓSr₁₋ₓTiO₃ using ReaxFF molecular dynamics simulations”** by Dooman Akbarian, Nadire Nayir, and Adri C. T. van Duin, stating that **barium strontium titanate BSTO** is widely used in nanodevices for **ferroelectric** properties and can be **epitaxially grown on SrTiO₃ (STO)** supports to reduce **lattice and thermal mismatch**. The full scientific narrative—DFT training on bulk, vacancy, and surface data; MD exploration of composition, oxygen vacancies, transition temperatures, polarization, and water on TiO₂-terminated surfaces—is curated on [[2021akbarian-physical-che-understanding-physical]] because the galley text layer foregrounds publisher workflow over continuous article sections.

## Methods

### A — Force-field training / fitting (ReaxFF and related)

- **N/A** to re-derive from this **proof** extract; the **ReaxFF** **training** narrative and **DFT** **reference** data are given on [[2021akbarian-physical-che-understanding-physical]] and the **VOR** **PDF** (see **§C** below for a pointer).

### B — Molecular dynamics, experiments, protocols, and sampling

- **N/A** on this **layout-proof** **slug** to recover **MD** run cards; use [[2021akbarian-physical-che-understanding-physical]] and the **VOR** **PDF** for **LAMMPS** **ReaxFF** **protocols** (**PBC**, **fs** **timestep**, **K** **temperatures**, **ps**/**ns** **duration**, **NVT**/**NPT**, **thermostat**/**barostat**).

### C — Electronic structure / static QM (when reported separately from MD)

ReaxFF energy decomposition, DFT reference sets for STO/BSTO equations of state and defects, and production MD protocols are described on the version-of-record page. The proof extract instead lists operator checklists: author names and affiliations, funding table completeness, editor queries answered, and attachments such as ESI files—useful for provenance auditing but not a substitute for simulation parameters. This duplicate slug should not be used to recover numerical training matrices or thermostat settings.

### D — Review scope, SI/galley notes, and non-primary corpus roles

- **Not applicable:** primary research article unless the **Summary** flags a **review**, **SI-only** register, or **duplicate** PDF (see **Reader notes** / **Limitations**).

This **proof** slug does not duplicate **ReaxFF** **MD** or **DFT** training line items; use [[2021akbarian-physical-che-understanding-physical]] for **Methods** text drawn from the version-of-record **PDF**.

## Findings

The curated sibling page states that increasing strontium content monotonically lowers transition temperature and polarization in the modeled setups, that higher oxygen vacancy concentration suppresses polarization and transition temperature, and that water adsorption on TiO₂-terminated surfaces enhances charge screening and increases initial polarization; those quantitative trends must be verified against the VOR PDF on [[2021akbarian-physical-che-understanding-physical]]. The graphical abstract fragment in the proof extract independently motivates BSTO/STO epitaxy as a practical context for composition-dependent ferroelectric studies, even though full heterostructure device stacks are not the focus of the MD narrative summarized on the sibling entry. Proof-stage subscript formatting (for example BaₓSr₁₋ₓTiO₃) should be checked against the final HTML article before quoting stoichiometry in downstream synthesis pages. **Comparisons** to **laboratory** work must follow the **VOR** on [[2021akbarian-physical-che-understanding-physical]]—this **proof** PDF is for **ingest** **provenance** only.

## Limitations

`extraction_quality: partial` reflects proof boilerplate in extracts. Prefer the VOR PDF for figures and SI links.

## Relevance to group

Van Duin-group extension of perovskite ReaxFF from BaTiO₃ toward BSTO with explicit hydration effects.

BSTO’s sensitivity to both A-site mixing and oxygen nonstoichiometry makes it a demanding training ground for oxide ReaxFF: curators extending this work should capture any additional DFT training sets added after the PCCP issue date in addendum notes rather than silently editing historical parameter claims.

Graphical-abstract text in proofs sometimes uses placeholder stoichiometry formatting; always confirm subscripts against the final HTML article before quoting formulas in theme hubs.

## Reader notes (navigation)

- [[2021akbarian-physical-che-understanding-physical]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: [10.1039/D1CP03353K](https://doi.org/10.1039/D1CP03353K)
