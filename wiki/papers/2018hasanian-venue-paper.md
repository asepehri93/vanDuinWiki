---
id: paper:2018hasanian-venue-paper
type: paper
title: 'Hydrogenation and defect formation control the strength and ductility of MoS\(_2\) nanosheets: Reactive molecular dynamics simulation (publisher proof PDF)'
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - task:application
  - material:tmd
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1016/j.eml.2018.05.008"
year: 2018
authors:
  - "Mostafa Hasanian"
  - "Bohayra Mortazavi"
  - "Alireza Ostadhossein"
  - "Timon Rabczuk"
  - "Adri C. T. van Duin"
venue: "Extreme Mechanics Letters (Elsevier proof PDF)"
pdf_sha256: "7955b54f5e619b1da06ef7c4877771ba1a567ce7f96eb5d3b874f9b5d4bb474f"
pdf_path: "papers/Hasanian_ExtremeMechLett_2018_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2018hasanian-venue-paper -->

??? info "PDF variant"
    Elsevier **proof** PDF. Full curated protocols and quantitative stress–strain discussion are on [[2018hasanian-extreme-mech-hydrogenation-defect]] (`papers/Hasanian_ExtremeMechLett_2018.pdf`).

## Summary

The galley PDF `papers/Hasanian_ExtremeMechLett_2018_galley.pdf` corresponds to the *Extreme Mechanics Letters* article DOI `10.1016/j.eml.2018.05.008`, “Hydrogenation and defect formation control the strength and ductility of MoS₂ nanosheets: Reactive molecular dynamics simulation.” The extract (`normalized/extracts/2018hasanian-venue-paper_p1-2.txt`) begins with Elsevier proofing notices (“changes made in the online proofing system… are not reflected in this PDF”) and an in-press citation line directing readers to the DOI above. The **abstract** reproduced there states that two-dimensional MoS₂ attracts attention for solar cells, photocatalysis, lithium-ion batteries, nanoelectronics, and electrocatalysis, and—like other 2D materials—can be tuned by chemical functionalization and defects. The authors state an objective to explore mechanical properties of **hydrogen-functionalized** single-layer MoS₂ and to analyze **several defect types** on mechanical response at **room temperature** using **ReaxFF**. They report that increasing hydrogen adatom or defect content significantly affects elastic modulus, tensile strength, stretchability, and failure behavior, and that the simulations provide guidance for designing nanodevices with hydrogenated and defective MoS₂. (A copyediting query visible in the online proof text asks whether a “better word” than “stretchability” is preferred, reflecting publisher workflow rather than physics content.)

## Methods

Per the **Elsevier proof** **PDF** (`pdf_path`) and the **version-of-record** article (**[[2018hasanian-extreme-mech-hydrogenation-defect]]**), **reactive MD** uses **LAMMPS** with **Mo–S–H ReaxFF** (Ostadhossein et al.) on **single-layer 2H-MoS\(_2\)** **supercells** (e.g. **8280** **atoms** for the pristine case on the VOR page) with **periodic boundary conditions** in-plane as detailed on [[2018hasanian-extreme-mech-hydrogenation-defect]]. **Room-temperature** (**~300 K**) **NPT** **equilibration** uses **Nosé–Hoover** **thermostat** and **barostat** damping values quoted on the VOR page, followed by **uniaxial** loading at **1×10⁹ s⁻¹** with **0.25 fs** **timestep** and **virial** stress averaging intervals listed there. **Monovacancy** motifs follow the **Zhou** taxonomy. **N/A — reproduce final figure labels** from this **proof** file alone—use the non-galley **PDF** for pagination-sensitive citations.

## Findings

**Outcomes (abstract-level, proof PDF):** hydrogen adatoms and **several defect types** materially change **elastic modulus**, **tensile strength**, **stretchability**, and **failure** behavior for **single-layer MoS\(_2\)** at **room temperature** in the authors’ **ReaxFF** workflow.

**Mechanistic detail & numbers:** **N/A —** stress–strain curves, **S–S** pairing after yield, and **virial** stress magnitudes are **not** extracted from this **galley** file in the corpus; read **`[[2018hasanian-extreme-mech-hydrogenation-defect]]`** for the **curated** quantitative discussion.

**Comparisons / sensitivity:** **N/A —** the proof excerpt does not restate **experimental** comparisons beyond motivating context in the full article.

**Limitations / outlook:** **Proof** PDFs can carry copyediting queries and non-final typography; **corpus honesty:** prefer the **VOR** **PDF** on the sibling wiki page for **figure** numbering and **pagination**.

**Corpus / KB:** this slug exists for **manifest** provenance of the **galley** bytes; **duplicate** of **`[[2018hasanian-extreme-mech-hydrogenation-defect]]`** for scientific interpretation.

## Limitations

Proof PDFs can include editorial queries and differ cosmetically from the final XML. Prefer the non-galley PDF for stable figure numbering.

## Relevance to group

Direct van Duin-group collaboration on TMD mechanics with ReaxFF.

## Reader notes (navigation)

- [[2018hasanian-extreme-mech-hydrogenation-defect]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: `10.1016/j.eml.2018.05.008`.
