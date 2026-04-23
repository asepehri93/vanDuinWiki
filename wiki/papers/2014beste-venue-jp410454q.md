---
id: paper:2014beste-venue-jp410454q
type: paper
title: "ReaxFF study of the oxidation of lignin model compounds for the most common linkages in softwood in view of carbon fiber production"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:combustion
  - keyword:polymer
  - keyword:lammps
source_refs: []
doi: "10.1021/jp410454q"
year: 2014
authors:
  - "Ariana Beste"
venue: "J. Phys. Chem. A"
pdf_sha256: "3de738174b0a9e921f212c477ef95cbcffcae1468b8f56809dad1aa5596deb17"
pdf_path: "papers/ReaxFF_others/Beste_JPCA_2014_lignin.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014beste-venue-jp410454q -->

## Summary

**Lignin** is a major **biopolymer** component in woody biomass and an important precursor route to **carbon fibers**, but **oxidative stabilization** chemistry in **air** must convert the precursor toward **infusible** networks before **carbonization**. Understanding **linkage-dependent** oxidation is therefore central to processing windows and property control. This **J. Phys. Chem. A** article uses **ReaxFF MD** to study **oxidative thermal conversion** of **dilignol** models representing **seven** common **softwood** **linkage classes**, extracting **effective activation energies** for conversion, analyzing **formaldehyde** formation channels, characterizing **fragmentation** patterns, and tracking **average carbon oxidation states** as functions of **temperature**. The scientific goal is to connect **primary lignin chemistry** to **stabilization** motifs argued to promote **rigid crosslinks** beneficial prior to **carbonization**, using a **small-molecule** surrogate set rather than full lignin macromolecules. For **carbon fiber** processing, this matters because **oxidative stabilization** is an intentional **crosslinking** stage that sets the **graphitization** pathway; the paper therefore emphasizes not only **fragmentation** but also **rigidifying** connections that can lock in **fused-ring** motifs before **high-temperature** carbonization. Readers should treat each **linkage** model as a controlled probe of **local** chemistry rather than a stand-in for full **lignin** architecture. The article’s comparative design is its main utility for the knowledge base: it makes **softwood** **linkage** identity an explicit independent variable when discussing **oxidative stabilization** chemistry. Use the **JPCA** article tables for Arrhenius parameters and species assignments.

## Methods

### Molecular models (lignin linkages)

- The study constructs **seven dilignol prototypes**, each representing a dominant **softwood** **linkage class**, to isolate **linkage-dependent** oxidation chemistry (article design described in the abstract).

### Reactive MD protocol (ReaxFF in LAMMPS)

- **ReaxFF MD** is executed in **LAMMPS** using the **ReaxFF** parameterization cited in the paper (version/parameter file references in **JPCA** Methods).
- **Integration:** **Δt = 0.1–0.25 fs** depending on simulation stage; **Berendsen** thermostats appear where noted in Methods.
- **Thermal protocol:** **oxidative cook-off** simulations use **~233 K/ps** heating ramps as stated in the article’s **Methods** section.

### Analysis

- Post-processing extracts **effective activation energies** for **oxidative conversion**, tracks **formaldehyde** channels, catalogs **fragmentation** patterns, and computes **average carbon oxidation state** vs **temperature** (abstract).

### Scope limits

- Models are **small-molecule surrogates** for **lignin** chemistry—not full macromolecular fibers—so transport and morphological effects are out of scope.

**1 — MD application (atomistic dynamics).** **Engine / code:** **LAMMPS** with **ReaxFF** (`papers/ReaxFF_others/Beste_JPCA_2014_lignin.pdf`). **System:** **seven** gas-phase **dilignol** prototypes plus **O₂** in **3D PBC** cells (**atom counts** in **JPCA** Methods). **Boundaries:** **3D PBC** gas-phase boxes. **Ensemble / thermostat:** **NVT**-class runs with **Berendsen** thermostats during **oxidative heating** ramps (**~233 K/ps** ramp rate stated in article Methods). **Timestep:** **0.1–0.25 fs** depending on stage (**Methods**). **Duration / stages:** multi-stage **oxidative cook-off** trajectories as tabulated in the article (**N/A — full stage table not copied** here). **Barostat / bulk pressure:** **N/A —** **NVT** gas-phase protocol in this summary layer. **Temperature:** high-temperature oxidative windows per article (exact ranges **PDF-grounded**). **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training:** **N/A —** uses **ReaxFF** parameterizations for **hydrocarbons** and **oxygenates** as cited from prior work (abstract / introduction in extract), not a new fit in this paper.

## Findings

The study reports **effective activation energies** for **oxidative conversion** of each linkage model and tracks **formaldehyde** formation pathways alongside **fragmentation** outcomes. **Average carbon oxidation states** evolve with **temperature** in linkage-specific ways, and several pathways produce **cyclic rigid connections** argued to mirror **stabilization chemistry** needed before **carbonization**. **Linkage identity** strongly steers which **crosslinking** channels dominate in the ReaxFF trajectories, supporting a narrative that **softwood** linkage distributions could alter **oxidative** outcomes even when overall **O\(_2\)** exposure is similar. The article’s value for the knowledge base is therefore comparative: it provides a **per-linkage** catalog of **activation** trends and **fragmentation** families that can be used to prioritize experiments when feedstock composition shifts.

## Limitations

**Model compounds** cannot capture full **lignin** heterogeneity and **spatial** transport in fibers. **ReaxFF** accuracy for **oxygenate** chemistry should be judged using the paper’s own benchmarks.

## Relevance to group

**Biomass pyrolysis/oxidation** **ReaxFF** application parallel to **fuel** and **polymer** decomposition studies in the corpus.

## Citations and evidence anchors

- **DOI:** [10.1021/jp410454q](https://doi.org/10.1021/jp410454q) (`papers/ReaxFF_others/Beste_JPCA_2014_lignin.pdf`).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
