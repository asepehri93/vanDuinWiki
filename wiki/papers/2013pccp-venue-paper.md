---
id: paper:2013pccp-venue-paper
type: paper
title: "Exploring the conformational and reactive dynamics of biomolecules in solution using an extended version of the glycine reactive force field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:reactive-md
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:polymer
  - keyword:water-interfaces
  - keyword:method-development
  - keyword:reactive-md
source_refs: []
doi: "10.1039/C3CP51931G"
year: 2013
authors:
  - "Susanna Monti"
  - "Alessandro Corozzi"
  - "Peter Fristrup"
  - "Kaushik L. Joshi"
  - "Yun Kyung Shin"
  - "Peter Oelschlaeger"
  - "Adri C. T. van Duin"
  - "Vincenzo Barone"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "8cdba6c25eee600e045edde2215e275e1edc94ce29577904a4ba690a9a011a17"
pdf_path: "papers/PCCP_Monti_ReaxFF_Peptides_accepted.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013pccp-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. For definitive numerical values and schemes, use the peer-reviewed article.

## Summary

This work extends an existing ReaxFF parameterization for glycine into a broader reactive model for peptides and proteins, aimed at protonation-state changes and reaction pathways involving amino acids in solution. The expansion adds a large quantum-mechanical training set (hundreds of systems) spanning all amino acids and selected short peptides. On sub-nanosecond trajectories (about 500 ps), ReaxFF predictions for representative biomolecular test cases—including capped amino acids, small peptides, and compact proteins—are compared to non-reactive classical simulations and to experimental benchmarks where available, including pharmaceutically motivated examples.

## Methods

Grounding: `papers/PCCP_Monti_ReaxFF_Peptides_accepted.pdf`; `normalized/extracts/2013pccp-venue-paper_p1-2.txt` (abstract-level only).

### 1 — MD application (ReaxFF validation trajectories)

The abstract reports **molecular dynamics** validation of the extended ReaxFF protein model on a **relatively short time scale (~500 ps)** for well-characterized test cases including **capped amino acids**, **peptides**, and **small proteins**, including **reaction mechanisms** connected to the **pharmaceutical** sector, compared to **classical non-reactive simulations** and **experimental** reference data.

- **Engine / code:** N/A — MD program and integrator are **not named** in the indexed excerpt; confirm in the full PDF (`pdf_path`).
- **System size & composition:** Test systems are described qualitatively as **capped amino acids**, **peptides**, and **small proteins** (abstract); **atom counts and stoichiometries** are not in the p1–2 excerpt.
- **Boundaries / periodicity:** N/A — **PBC vs cluster** details are **not stated** in the indexed excerpt.
- **Ensemble:** N/A — **NVE/NVT/NPT** choice is **not stated** in the indexed excerpt.
- **Timestep:** N/A — **timestep (fs)** is **not stated** in the indexed excerpt.
- **Duration / stages:** **~500 ps** validation trajectories are stated in the abstract for the performance assessment window.
- **Thermostat / barostat:** N/A — **thermostat/barostat types and coupling constants** are **not stated** in the indexed excerpt.
- **Temperature:** N/A — explicit **temperature setpoints** for the validation MD are **not stated** in the indexed excerpt.
- **Pressure:** N/A — **hydrostatic pressure control** is **not stated** in the indexed excerpt.
- **Electric field:** N/A — **not used** per abstract scope.
- **Replica / enhanced sampling:** N/A — **not stated** in the indexed excerpt.

### 2 — Force-field training (ReaxFF extension for peptides/proteins)

- **Parent FF / elements:** Reactive **ReaxFF-based** description framed as an **expansion** of **previously reported glycine parameters** for peptide/protein simulations (abstract).
- **QM reference:** The training expansion is built from **quantum mechanical calculations** on **>500 molecular systems** (abstract); **program, functional, basis, and k-sampling** used for that QM reference set are **not stated** in the indexed excerpt—see the article Methods in `pdf_path`.
- **Training set:** Adds **>500** QM-characterized systems including **all amino acids** and **some short peptide structures** to the training set (abstract).
- **Optimization:** N/A — **fitting/optimization workflow and software** are **not stated** in the indexed excerpt.
- **Reference data / validation:** Post-training assessment compares ReaxFF predictions to **non-reactive classical MD** and **experimental** benchmarks on the **~500 ps** validation window (abstract).

## Findings

- **Outcomes & mechanisms:** The abstract states that **good agreement** is obtained between ReaxFF-predicted **conformations and kinetics** and the **reference classical simulations and experimental data** for the highlighted test cases spanning capped amino acids, peptides, small proteins, and pharmaceutically motivated mechanisms.
- **Comparisons:** Direct comparisons are framed against **classical non-reactive MD** and **experiment** on the same test cases (abstract).
- **Sensitivity / design levers:** N/A — **parameter sweeps** (temperature, ionic strength, pH, etc.) are **not summarized** in the indexed excerpt beyond the qualitative validation framing.
- **Limitations & outlook:** The abstract’s validation is explicitly on a **short (~500 ps) time scale**, which inherently limits claims about **slow** conformational transitions and **rare** reactive events without longer sampling in the primary text.
- **Corpus honesty:** This page is grounded on an **RSC accepted manuscript** PDF and a **short metadata-aligned extract**; **integrator, thermostat, system sizes, and QM training details** must be taken from the **full PDF** when needed for reproduction.

## Limitations

- Short (hundreds of ps) trajectories do not resolve slow folding or rare conformational transitions.
- Reactive FF accuracy is training-set dependent; transfer to uncommon chemistries or unusual protonation environments may require additional refinement.

## Relevance to group

Foundational **ReaxFF-for-biomolecules** line from the van Duin group (with collaborators), connecting reactive hydrocarbon/organic frameworks to practical peptide and protein-scale simulations.

## Citations and evidence anchors

- DOI: [10.1039/C3CP51931G](https://doi.org/10.1039/C3CP51931G)
- Text-aligned pointer: `normalized/extracts/2013pccp-venue-paper_p1-2.txt`

## Reader notes (navigation)

- **Corpus note:** The ingested PDF is an RSC **Accepted Manuscript**; wording may differ slightly from the final edited issue PDF.

## Related topics

- [[reaxff-family]]
- Reactive models for organics and aqueous biomolecular chemistry
