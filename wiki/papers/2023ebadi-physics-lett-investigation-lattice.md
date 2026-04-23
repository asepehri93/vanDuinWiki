---
id: paper:2023ebadi-physics-lett-investigation-lattice
type: paper
title: "Investigation of lattice thermal conductivity of α′ borophene and hydrogenated α′-4H borophene using reverse nonequilibrium molecular dynamics simulation"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reactive-md
  - keyword:lammps
  - keyword:nose-hoover
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1016/j.physleta.2023.129155"
year: 2023
authors:
  - "Ali Ebadi"
  - "Mehran Gholipour Shahraki"
  - "Saeed Ghorbanali"
venue: "Phys. Lett. A"
pdf_sha256: "55160e1f3c55a67061e3391c21a1f01b123c650594b65e6a2e28f3e45112e220"
pdf_path: "papers/ReaxFF_others/Borophene_thermal.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2023ebadi-physics-lett-investigation-lattice -->

## Summary

Lattice thermal conductivity (LTC) and thermal anisotropy of two-dimensional α′ borophene and hydrogenated α′-4H borophene are computed at 300 K using reactive molecular dynamics in LAMMPS with a ReaxFF potential, with heat transport evaluated by reverse non-equilibrium molecular dynamics (rNEMD) and the enhanced heat exchange (eHEX) algorithm. The *Phys. Lett. A* abstract motivates the study by noting strong **electronic** **anisotropy** in **borophene** allotropes alongside growing experimental realization of **2D boron** structures, then focuses on how **hydrogenation** and **in-plane orientation** modify **phonon-dominated** **thermal transport** in the **ReaxFF** framework.

## Methods

### Interaction model (A/B)

- **Software:** **LAMMPS** with **ReaxFF** for **borophene** / **hydrogenated borophene** (α′ and **α′-4H** phases as defined in the article).

### Equilibration

- **Relaxation:** **Polak–Ribière conjugate-gradient** structural optimization.
- **Thermostat:** **Nosé–Hoover** at **300 K** for **0.1 ns** with **timestep 0.1 fs**.
- **Structure checks:** **RDF**/**ADF** accumulated over **100 fs** to verify local geometry.

### Thermal transport protocol (B)

- **Method:** **Reverse NEMD** with the **enhanced heat exchange (eHEX)** algorithm.
- **Geometry:** **Periodic** in-plane; **50** slabs along the **heat-flow** direction; **hot/cold** slab energy exchanges impose steady flux; transverse width **~6 nm** for comparing **orientations**.
- **Steady state:** **0.1 ns** at **0.1 fs** in **NESS** before averaging slab **T**; longer **>0.2 ns** segments used to build **temperature profiles**.

### Extraction of κ

**κ** from **Fourier’s law** using imposed **flux**, **area**, and **∇T**; **size scaling** via **κ(L\(_x\)) = κ\(_∞\)/(1 + λ/L\(_x\))** to discuss **finite-length** effects.

### MD application (integrated, same as above detail)

**Engine / code:** **LAMMPS** and **ReaxFF**. **System & composition:** **2D** **α′** and **hydrogenated α′-4H** **borophene**; **PBC** **in-plane**; **rNEMD** with **eHEX** uses **~50** slabs in the **heat-flow** direction, **~6 nm** transverse width, **hot/cold** slab thermostating to impose **flux**. **Timestep 0.1 fs**; **0.1 ns** **Nosé–Hoover** equilibration at **300 K**; **0.1 ns** **NESS** and **>0.2 ns** **temperature** **profile** accumulation as stated. **NVT**-class thermostated segments for the **thermal** workflow; **N/A — NPT** not used in the **κ** setup summarized here. **N/A — barostat / hydrostatic pressure** in this **NEMD** protocol. **N/A — static electric field; N/A — umbrella / metadynamics** for **κ** in this paper’s main line.

## Findings

### Hydrogenation effect

**Hydrogenation** **increases** **LTC** along **armchair** for **α′** vs **pristine** in the authors’ **ReaxFF** **rNEMD** setup.

### Anisotropy

**α′** and **α′-4H** show **strong in-plane thermal anisotropy**.

### Length dependence

**Armchair κ** **increases** with **sample length** in the studied range; **zigzag κ** **decreases** with length—attributed to **defects**, **phonon interference**, and **dispersion** effects along that direction.

The abstract further summarizes that **α′-4H** **hydrogenated** sheets exhibit **higher** **LTC** than **pristine** **α′** along **armchair** in their parametrization, consistent with **hydrogenation** stiffening certain **phonon** branches while preserving strong **in-plane** **anisotropy** between **armchair** and **zigzag** transport directions. **Comparisons** to **DFT**/**experiment** in the text should be read from the **PDF**; **sensitivity** of **κ** to **sample length** is explicit above.

## Limitations

ReaxFF is empirical; absolute κ values and trends should be cross-checked against experiment or higher-level theory where available.

## Relevance to group

Demonstrates **ReaxFF + LAMMPS** thermal transport workflow (rNEMD/eHEX) for **2D boron allotropes**, adjacent to the group’s broader reactive-MD tooling experience.

## Citations and evidence anchors

- DOI: [10.1016/j.physleta.2023.129155](https://doi.org/10.1016/j.physleta.2023.129155)

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
