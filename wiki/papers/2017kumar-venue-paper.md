---
id: paper:2017kumar-venue-paper
type: paper
title: "Supporting information: Thermodynamics of alkanethiol self-assembled monolayer assembly on Pd surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:metal-surface
  - method:dft-static
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:catalysis-surface
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1021/acs.langmuir.7b04351"
year: 2018
authors:
  - "Gaurav Kumar"
  - "Timothy Van Cleve"
  - "Jiyun Park"
  - "Adri van Duin"
  - "J. Will Medlin"
  - "Michael J. Janik"
venue: "Langmuir (Supporting Information); companion to DOI 10.1021/acs.langmuir.7b04351"
pdf_sha256: "735bb59b65243e27e81b0e19a38cc5d455a14f174314039937851fcb638e017c"
pdf_path: "papers/Kumar_thiol_Pd_Langmuir_2018_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2017kumar-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes this **Supporting Information** PDF and the short **normalized extract** (`normalized/extracts/2017kumar-venue-paper_p1-2.txt`). For **full DFT setups**, **tables**, and **figures**, use the **SI PDF** together with the **peer-reviewed article** on **alkanethiol SAMs on Pd** ([[2018kumar-langmuir-201-thermodynamics-alkanethiol]]).

## Summary

This corpus entry registers the **Supporting Information** for **Langmuir** work on **alkanethiol/alkanethiolate** assembly on **Pd(111)**, **Pd(100)**, and **Pd(110)**. The SI outlines **high-coverage** binding trends (**Figure S1**), **plane-wave DFT** slab **protocols** (**Table S1**) and **coverage-resolved** **bonding** vs **nonbonding** contributions to **adsorption energies** (**Tables S2A–S2C**), plus **surface free-energy** comparisons for **short vs longer** thiols (**Figure S2**). **Section S4** documents **ReaxFF** extension for **Pd–S** environments, including a **DFT training** comparison on **Figure S3**. **Section S5** gives **DRIFTS** auxiliary figures for **CO** on **Pd** catalysts (**Figures S4–S5**).

## Methods

**1 — MD application.** **N/A — production large-scale MD is not documented in this SI excerpt** (no **LAMMPS**/**GROMACS**-style trajectory protocol is extracted here): the Supporting Information focuses on **DFT slab protocols**, **energy decompositions**, and **ReaxFF vs DFT** benchmarks. For this `method:reaxff` SI registration (MD slots must still be explicit **N/A**): **N/A — periodic boundary conditions** for any hypothetical MD are not stated here; **N/A — ensemble** (**NVE/NVT/NPT**) for MD; **N/A — timestep (fs)** for MD; **N/A — MD trajectory duration (ps/ns)**; **N/A — thermostat** parameters for MD; **N/A — barostat / pressure control** for MD. Retrieve any **SAM dynamics** protocol from the **main article** PDF ([[2018kumar-langmuir-201-thermodynamics-alkanethiol]]).

**2 — Force-field training / fitting (Pd–S ReaxFF extension).** **Section S4** describes extending **ReaxFF** to treat **Pd–S** chemistry using **DFT reference data** across **bulk** and **surface** **sulfur** environments on **Pd(111)**, **Pd(100)**, and **Pd(110)**. **Figure S3** compares **DFT** versus **ReaxFF** **surface adsorption energies** for **sulfur** on the three facets (including **subsurface** and **coverage-based** labels defined in the SI caption).

**3 — Static QM / DFT (slab protocols and energy decomposition).** **Table S1** lists **k-point meshes**, **slab layer counts**, **frozen layers**, and **in-plane supercell** vectors for the **Pd** surface models (third lattice vector **normal to the surface**). **Tables S2A–S2C** decompose **thiolate adsorption energies** on each facet into **bonding** (**\(E_b\)**), **nonbonding** (**\(E_{nb}\)**), and **total** (**\(E_\text{ads}\)**) contributions across **coverages**. **Figure S1** summarizes **very high coverage** binding trends versus **alkyl chain length** on the three facets (covalent / noncovalent / total panels).

**4 — Review / non-simulation framing.** **N/A** for the core DFT/ReaxFF blocks; **Section S5** adds **experimental-style DRIFTS** context for **CO** on **Pd** catalysts (**Figures S4–S5**) as auxiliary characterization relative to the SAM thermodynamics story.

## Findings

**Outcomes and mechanisms (SI-level).** The SI’s **energy decomposition** supports a picture where **chain length**, **facet**, and **coverage** jointly control whether **covalent** versus **noncovalent** contributions dominate **thiolate** binding at **Pd** surfaces—this underpins the **main article’s** interpretation of **SAM** thermodynamics and **chemical potential** trends.

**Comparisons.** **Figure S3** is the direct **DFT vs ReaxFF** benchmark for **S-on-Pd** motifs; the SI text/caption flags where **agreement** is strong and where **multi-coordination** environments are harder to reproduce.

**Sensitivity and design levers.** **Facet** (**111/100/110**), **coverage**, and **alkyl length** (via **Figure S1**/**S2** families) are the primary knobs exposed in the SI tables/figures for how **binding** partitions between **bonding** and **nonbonding** terms.

**Limitations and outlook (as authored).** As **Supporting Information**, this file is **not** a standalone substitute for the **main text** conclusions, pagination, or full discussion of **SAM** assembly kinetics.

**Corpus / PDF honesty.** Treat this slug as **`NON_PRIMARY` SI** per [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md): it registers **`papers/Kumar_thiol_Pd_Langmuir_2018_SI.pdf`**. The **version-of-record article** narrative lives on **`[[2018kumar-langmuir-201-thermodynamics-alkanethiol]]`**; the local **`normalized/extracts/2017kumar-venue-paper_p1-2.txt`** file is **SI front matter** only—**do not** treat it as full coverage of **Tables S1–S4**.

## Limitations

- **SI-only** ingest: **pagination**, **complete** **parameter** lists, and **main-text** **conclusions** are not replaced by this page—use the **article PDF** for the **full** narrative.
- The **local extract** covers **SI front matter** and **section** headings; **deep** **table/figure** values should be checked in the **PDF**.

## Relevance to group

**Co-authored** **PSU / Colorado** study: **van Duin** group involvement in **Pd–S** **ReaxFF** development alongside **DFT**-driven **SAM** **thermodynamics** ([[2018kumar-langmuir-201-thermodynamics-alkanethiol]]).

## Citations and evidence anchors

- **Parent article (DOI):** [https://doi.org/10.1021/acs.langmuir.7b04351](https://doi.org/10.1021/acs.langmuir.7b04351)
- **Full article note:** [[2018kumar-langmuir-201-thermodynamics-alkanethiol]]

## Related topics

- [[2018kumar-langmuir-201-thermodynamics-alkanethiol]]
- [[reaxff-family]]

## Reader notes (navigation)

- This slug tracks **`papers/Kumar_thiol_Pd_Langmuir_2018_SI.pdf`**; the **version-of-record article** is **`2018kumar-langmuir-201-thermodynamics-alkanethiol`**.
