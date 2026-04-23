---
id: paper:2024fthenakis-venue-porous-carbon
type: paper
title: "Porous carbon nitride fullerenes: a novel family of porous cage molecules"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:dft-static
  - method:reaxff
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:reaxff-application
  - keyword:graphene-carbon
candidate_tags:
  - "arXiv-2410.07822"
source_refs: []
doi: ""
year: 2024
authors:
  - "Zacharias G. Fthenakis"
  - "Nektarios N. Lathiotakis"
venue: "Preprint/arXiv 2410.07822 (cond-mat.mtrl-sci); verify any journal VOR separately"
pdf_sha256: "84d0caf8125a584651af300f7bdff9cf87f9e2b3721d835a62e91fc40ce9b351"
pdf_path: "papers/ReaxFF_others/Fthenakis_CN_fullerenes_2024.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024fthenakis-venue-porous-carbon -->

## Summary

Fthenakis and Lathiotakis introduce **porous carbon nitride fullerenes (PCNFs)** as **zero-dimensional** analogues of **two-dimensional porous graphitic carbon nitrides**, paralleling how **icosahedral fullerenes** relate to **graphene**. They highlight two representatives—**C₆₀N₆₀** (class-I **Goldberg** branch) and **C₁₂₀N₆₀** (class-II branch)—and use **density functional theory** for **structures**, **vibrational** analysis, and **electronic** properties. **ReaxFF molecular dynamics** provides **thermal stability** estimates by heating the cages. The work is archived as **arXiv:2410.07822**; a **journal DOI** was not registered in this wiki’s front matter at curation time. The introduction explains that only (n,0) and (n,n) Goldberg polyhedra retain full icosahedral symmetry, so designing symmetric PCNFs requires introducing multiple pores into icosahedral fullerene precursors while preserving that symmetry class.

## Methods

### Static DFT on cage structures (C)

**DFT** relaxation of **icosahedral**/**Goldberg** **PCNF** candidates; **normal modes** for **mechanical** stability; **electronic** properties per **arXiv:2410.07822**/**preprint** text. **Functional** (PBE- or as named in the **Methods**), **DFT** **dispersion** correction if used, **plane-wave**/**PAW** **cutoff**/**k-mesh**—**N/A** to duplicate the **preprint** tables on this page; **structures** are relaxed **cages**; **properties** include **gap**, **frequencies**, and **stability** **metrics**.

### Thermal stability (ReaxFF MD) (B)

**ReaxFF** **high-T** dynamics on relaxed cages—abstract cites **C\(_{60}\)N\(_{60}\)** stable **≫1000 K**, **C\(_{120}\)N\(_{60}\)** **≫2000 K**; **thermostat**, **Δt**, **ffield** in **`papers/ReaxFF_others/Fthenakis_CN_fullerenes_2024.pdf`**.

**Simulation caveats.** **Thermal** stability thresholds from **ReaxFF** depend on the **parameterization** for **C/N** bonding and **three-body** terms; the preprint pairs these **MD** scans with **DFT** **phonon** analyses to argue **mechanical** stability of the **proposed** **cages**. Any **journal** **VOR** may refine **numerical** thresholds—check updated **DOI** if assigned after curation.

**MD application (ReaxFF heating of cages).** **LAMMPS**-style **molecular dynamics**+**ReaxFF** (see **arXiv:2410.07822**/**PDF**) on **isolated** **cage** **supercells** of **C\(_{60}\)N\(_{60}\)** and **C\(_{120}\)N\(_{60}\)** (total **atom** counts per **stoichiometry** in the **preprint**) in **NVT** (or as stated) with **Nosé–Hoover**-class **heating** ramps: **N/A** for exact **time step** (fs), **duration** of **heating** segments (ps), and **K**/s **ramp** on this stub—`papers/ReaxFF_others/Fthenakis_CN_fullerenes_2024.pdf`. **Periodic** **PBC** for **isolated** **cage**+vacuum; **N/A**—**NPT** **Parrinello** **barostat**; **N/A**—**E-field**; **N/A**—**metadynamics**. **Hydrostatic** **pressure** **N/A** for free **molecular** **cage** **NVT**.

## Findings

The abstract states that **DFT** supplies **structural**, **vibrational**, and **electronic** properties for the **PCNF** candidates, while **ReaxFF MD** probes **thermal** degradation. **Vibrational** analysis supports **mechanical stability** of the **proposed cages** within DFT. **ReaxFF** simulations indicate **substantial thermal robustness** for both **C₆₀N₆₀** and **C₁₂₀N₆₀**, with the larger cage surviving higher temperatures in their tests. The discussion outlines **precursor** ideas for possible **bottom-up** synthesis routes connecting to **porous g-C\(_x\)N\(_y\)** chemistry.

**Comparisons, sensitivity, corpus note.** **DFT**+**vibrational** data **compared** to **stability** metrics from **heating** **RMD**; **sensitivity** to **temperature** in **K** is explicit in the **abstract** (C\(_{60}\)N\(_{60}\) vs C\(_{120}\)N\(_{60}\)). **arXiv**-only **preprint**—treat as **low**-provenance for **reactive** **thresholds** until a **DOI** lands.

## Limitations

The **Introduction** also explains **porous g-C\(_n\)N\(_m\)** motifs in terms of **pyridinic** versus **graphitic** nitrogen placement around **pores**, and notes **nearest-neighbor** nitrogen placement penalties—details that matter when judging whether **PCNF** compositions are **plausible** relative to **2D** cousins. **Preprints** may differ from a **peer-reviewed** version; readers should check for an updated **DOI**. **ReaxFF** thermal thresholds are **force-field dependent** and should be cross-checked with **DFT/AIMD** or experiment when stakes are high. **van Duin** is **not** an author; this paper is filed as **methodological context** for **reactive carbon nitride** modeling.

**Confidence rationale:** `med`—preprint + ReaxFF thermal claims need VOR confirmation for `high`.

## Reader notes (navigation)

- [[reaxff-family]]
- [[graphene-nanocarbon]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[reaxff-family]]
