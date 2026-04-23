---
id: paper:2013aikens-venue-si8-2
type: paper
title: "Supporting information: Improved ReaxFF force field parameters for Au–S–C–H systems"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-parameterization
  - keyword:metallic-systems
source_refs: []
doi: "10.1021/jp405992m"
year: 2013
authors:
  - "Aikens, Christine M."
venue: "Supporting information (J. Phys. Chem. A)"
pdf_sha256: "52aa531cacdb93375676d5f4394bd783772d4d12c7549f81c02dae303bb2d46b"
pdf_path: "papers/ReaxFF_others/Bae_Aikens_AuSCH_supplement.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013aikens-venue-si8-2 -->

## Summary

This Supporting Information PDF is a second corpus path (`papers/ReaxFF_others/Bae_Aikens_AuSCH_supplement.pdf`) for the same supplementary bundle as [[2013aikens-venue-si8]], tied to the parent article DOI **`10.1021/jp405992m`** (“Improved ReaxFF Force Field Parameters for Au–S–C–H Systems”). The extract (`normalized/extracts/2013aikens-venue-si8-2_p1-2.txt`) lists **Tables 1S–6S** and **Figures 1S–3S**, including explicit comparisons of **old** versus **NP-specific** parameters and PBE versus ReaxFF bond lengths/angles for Au₂₅(SCH₃)₁₈⁻, Au₃₈(SCH₃)₂₄, and Au₁₄₄(SCH₃)₆₀ clusters, plus PES scans for **S–Au–S** bending in CH₃–S–Au–S–CH₃. The opening table fragment in the extract records representative parameter shifts (for example **Au–S (rσ)** from **2.1505** to **1.9000** and **S–Au–S (Θ₀,₀)** from **20.0000** to **5.0000** in the displayed columns), illustrating how the reparameterization tightens staple bending relative to the legacy set.

## Methods

### Corpus role (duplicate SI path)

Second corpus filename (`papers/ReaxFF_others/Bae_Aikens_AuSCH_supplement.pdf`) for the **same supplementary bundle** as **`[[2013aikens-venue-si8]]`**, parent **DOI `10.1021/jp405992m`**.

### Force-field training (SI)

**Parent FF / elements:** **ReaxFF Au–S–C–H** updates relative to **Järvi et al.**; **Tables 1S–6S** list parameter deltas and **cluster** benchmarks vs **PBE** for **thiolate-protected gold** motifs containing **hundreds of atoms** per particle (extract `2013aikens-venue-si8-2_p1-2.txt`).

**QM reference / training / optimization / benchmarks:** **ADF PBE/TZP/ZORA** and the **parameter optimization** narrative are in the **main article**; the SI supplies **LAMMPS-ready** numeric tables.

### MD application

**Engine / code:** **LAMMPS** is referenced in the SI bundle for downstream **molecular dynamics** users (wiki cross-link to parent article).

**N/A —** **ensemble (NVE/NVT/NPT)**, **timestep** (**fs**), **ps/ns** trajectory schedule, **thermostat**, **barostat**, **temperature**, and **PBC** details for validation **molecular dynamics** are **not** taken from this duplicate SI stub—use **`[[2013bae-venue-jp405992m]]`**.

## Findings

**Outcomes / comparisons:** **Figures/tables** document improved **S–Au–S** bending **PES** behavior and cluster **geometries** vs **DFT** for the **Au–thiolate** benchmarks highlighted in the parent abstract.

**Corpus honesty / limitations:** Treat as a **manifest alias** for **`[[2013aikens-venue-si8]]`**; **byte-compare** PDFs before retiring either path. **PDF** copy/paste can corrupt **exponent** fields in wide tables—verify against the typeset **SI** when importing into **LAMMPS** data files.

## Limitations

Maintaining two filenames for one SI package can confuse manifests; prefer a single canonical path when cleaning the corpus.

## Relevance to group

Auxiliary gold–thiolate ReaxFF data used across nanoparticle and interface simulations in the knowledge base.

When parameter tables span multiple pages, optical character recognition errors occasionally corrupt exponent formatting; always cross-check critical exponents against the main article’s Typeset values or the LaTeX-style tables in the primary JPCA PDF before importing into LAMMPS data files.

If two SI filenames differ only by “_SI” versus “supplement,” prefer whichever file hash matches the publisher’s current download bundle before regenerating `MANIFEST.jsonl` rows.

Theme hubs that mention gold–thiolate parameterization should link this SI stub only as a reproducibility appendix, not as a substitute for the peer-reviewed parameter rationale in the JPCA article body.

## Reader notes (navigation)

- [[2013aikens-venue-si8]]
- [[2013bae-j-phys-chem-jp405992m]]
- [[reaxff-family]]
