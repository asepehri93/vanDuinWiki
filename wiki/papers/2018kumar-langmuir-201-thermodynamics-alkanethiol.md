---
id: paper:2018kumar-langmuir-201-thermodynamics-alkanethiol
type: paper
title: "Thermodynamics of Alkanethiol Self-Assembled Monolayer Assembly on Pd Surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reactive-md
  - domain:reaxff-lineage
  - material:metal-surface
  - method:dft-static
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:catalysis-surface
  - keyword:metallic-systems
  - keyword:validation-experiment
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
venue: "Langmuir 2018, 34, 6346–6357"
pdf_sha256: "5d1aa479ce781fbf48c376bcc492e6179a21685c81b428952c658b8c8e930601"
pdf_path: "papers/Kumar_thiol_Pd_Langmuir_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018kumar-langmuir-201-thermodynamics-alkanethiol -->

## Summary

Uses **dispersion-corrected DFT** to compute **alkanethiolate SAM** energetics and **preferred coverages** on **Pd(111)**, **Pd(100)**, and **Pd(110)** as a function of **chain length** and **thiol chemical potential**, linking **dispersion** interactions among **alkyl tails** to **coverage transitions**. **Temperature-dependent CO DRIFTS** experiments probe **weakened CO binding** as **thiolate coverage** increases, and the paper discusses **preliminary multiscale** modeling with **ReaxFF** for the **Pd–thiol** system. The **Langmuir** study is positioned at the interface of **surface science** and **catalysis**: **thiolate** **SAMs** poison **Pd** sites for small-molecule adsorption, yet the **thermodynamic** **phase diagram** of **SAM** **coverage** versus **chemical potential** is **facet-dependent**, so **nanoparticle** **shapes** under **saturating** **thiol** environments may differ from **vacuum** **Wulff** constructions without **adsorbate** **effects**.

## Methods

- **DFT:** **vdW-corrected** supercell calculations of **thiolates** on **Pd** facets; **binding energies** decomposed into **covalent** vs **noncovalent** contributions as reported; **Wulff** constructions used to discuss **particle** shape under **thiol saturation**.
- **Experiment:** **CO DRIFTS** vs **temperature** for **CO** on **thiol-covered** Pd surfaces at varying **SAM** densities.
- **Reactive FF:** **ReaxFF** results described as **preliminary multiscale** coupling (see article text for scope).
- **Coverage models:** **Grand-potential**-style comparisons across **facets** identify **transitions** (e.g., toward **1/2 ML**) where **tail** **packing** and **metal–S** **bonding** trade off.

The article also references **preliminary ReaxFF**/**multiscale** coupling for **Pd–thiol** chemistry; **N/A — full LAMMPS protocol tables** (**timestep**, **production ns**, **thermostat**) are not the main deliverable—use `pdf_path` if extended **MD** appears beyond the **DFT** core. For the **DFT-led** **SAM** phase diagram, **three-dimensional periodic boundary conditions (PBC)** enclose **Pd(111)**, **Pd(100)**, and **Pd(110)** **slab** supercells. **N/A — NVT/NVE/NPT molecular dynamics** production runs are not documented for the primary **coverage** models—static **0 K** **DFT** minimizations supply the **energies**. **DFT** **stress** tensors and cell **relaxation** follow the **plane-wave** program setup in **Methods**; **N/A — constant-stress NPT classical MD** is not part of the summarized workflow. **Barostat:** **N/A — NPT MD** not used in the **DFT** core. **Electric field:** **N/A — bias MD** not reported. **Replica / enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange MD** not reported.

## Findings

**Outcomes (DFT).** **Pd(111)** favors **1/3 ML** thiolate coverage in the equilibrium construction; **Pd(100)**/**(110)** show **coverage** increases with **thiol chemical potential**, including moves toward **1/2 ML** depending on **facet** and **chain length**.

**Comparisons.** **CO DRIFTS** **experiments** track **weakened CO** binding as **SAM** **density** rises, matching weakened **CO**/**O**/**H** **adsorption** in **DFT** with increasing **thiolate coverage**.

**Sensitivity.** **Chain length** tunes when **vdW** **tail** interactions compete with **facet-specific** **metal–S** bonding, shifting predicted **Wulff** shapes (**cubic** dominance on **Pd(100)** at **saturation**).

**Limitations and PDF grounding.** **ReaxFF** portions are explicitly **preliminary**; **DFT** **dispersion** treatment and **coverage** models should be taken from the **Langmuir** **PDF** and **SI** sibling **[[2017kumar-venue-paper]]** when needed.
## Limitations

- **ReaxFF** discussion is explicitly **preliminary** relative to the **DFT** core of the paper; quantitative agreement across **all facets** may require **further** **parameterization** and **validation**.

**Curation note:** the **SI**-only corpus sibling [[2017kumar-venue-paper]] holds extra **tables** referenced in the article; keep **DFT** **coverages** and **DRIFTS** interpretations on this **primary** **article** page unless the SI adds genuinely new numerical data.

## Relevance to group

**Group-authored** **Pd–SAM** **thermodynamics** bridging **DFT**, **spectroscopy**, and **ReaxFF**-oriented **multiscale** follow-on.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acs.langmuir.7b04351](https://doi.org/10.1021/acs.langmuir.7b04351)

## Reader notes (navigation)

- Supporting information (corpus PDF, cataloged): [[2017kumar-venue-paper]] — see [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (section A)

## Related topics

- [[reaxff-family]]
