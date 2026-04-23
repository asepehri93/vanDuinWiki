---
id: paper:2019fedkin-j-phys-chem-development-reaxff
type: paper
title: "Development of the ReaxFF Methodology for Electrolyte-Water Systems"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:water-interfaces
  - keyword:charge-equilibration
  - keyword:lammps
source_refs: []
doi: "10.1021/acs.jpca.8b10453"
year: 2019
authors:
  - "Mark V. Fedkin"
  - "Yun Kyung Shin"
  - "Nabankur Dasgupta"
  - "Jejoon Yeon"
  - "Weiwei Zhang"
  - "Diana van Duin"
  - "Adri C. T. van Duin"
  - "Kento Mori"
  - "Atsushi Fujiwara"
  - "Masahiko Machida"
  - "Hiroki Nakamura"
  - "Masahiko Okumura"
venue: "J. Phys. Chem. A 2019, 123, 2125-2141"
pdf_sha256: "26218dded91887591679097b7b8a9d2159568e9ea2e0fb6eb2975b146df692ec"
pdf_path: "papers/Fedkin_JPCA_Electrolyte_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019fedkin-j-phys-chem-development-reaxff -->

## Summary

A ReaxFF parameterization is developed for **water plus monovalent electrolytes**: cations Li+, Na+, K+, Cs+ and anions F-, Cl-, I-. Parameters are trained to QM data on cluster geometries, water binding energies, hydration energies, and proton-transfer energetics, then validated with MD on dissociation behavior, RDFs versus DFT, and diffusion trends in alkali hydroxide and chloride solutions across concentration. The **J. Phys. Chem. A** article is a **methods** paper in the **ReaxFF** lineage: it documents how **ion-specific** **bond** terms and **charge** **equilibration** choices are adjusted so that **bulk** **electrolyte** behavior remains consistent with **cluster** **QM** targets, bridging **gas-phase** training data with **condensed-phase** **observables**.

## Methods

**ReaxFF training.** Optimization of M-O/H and X-O/H interactions using QM-derived bond lengths/angles, binding-energy differences for sequential hydration, and proton-transfer paths; builds on transferable H/O water parameters used widely in prior ReaxFF models.

**Validation MD.** Simulations probe ion pairing/dissociation, RDFs for ion-oxygen and ion-hydrogen pairs, and self- and ionic diffusion in electrolyte solutions and crystals as described in the Computational Methods section (section 2.1 onward in the article).

**Software context.** Standard ReaxFF MD workflow as distributed for LAMMPS/PuReMD-class engines (engine choice per group practice; article specifies integrator settings in full text).

**Training scope.** The optimization emphasizes **monovalent** **halides** and **alkali** cations paired with **OH⁻** and **Cl⁻** solutions because those systems anchor **battery**-relevant **electrolyte** chemistry while remaining tractable for **QM** **reference** data generation.

**Bulk validation MD (electrolyte solutions and crystals).** **ReaxFF molecular dynamics** in **LAMMPS** / **PuReMD-class** engines evaluates **ion pairing**, **radial distribution functions**, and **self-/ionic diffusion** in **three-dimensional periodic** **supercells** sized from **dilute** (order **10²–10³ atoms**) to **concentrated** solutions and **ionic crystals** as tabulated in **Computational Methods** (`pdf_path`). **Ensemble:** **NVT** **thermal** equilibration and **production** segments at the **K** setpoints for each **composition**; **timestep** in **fs** and **production** lengths in **ps**/**ns** are given in **§2**. **Thermostat:** type and damping constants appear alongside those runs in the article. **Barostat / hydrostatic pressure control:** **N/A** — validation stays at **constant volume** without **GPa** **stress** servocontrol in the summarized protocol. **External electric field:** **N/A**. **Replica exchange / umbrella / metadynamics:** **N/A** for the bulk **RDF** and **diffusion** trajectories described in the abstract.

## Findings

RDFs for most ion-water pairs align well with DFT references; the parametrization reproduces thermodynamic dissociation trends and concentration-dependent diffusion behavior for the alkali halide/hydroxide sets emphasized in the abstract. The resulting force field is positioned as a basis for larger-scale reactive electrolyte and interfacial simulations.

Downstream **application** papers (for example **Dasgupta** *Comput. Mater. Sci.* **ambient** electrolyte benchmarks) inherit these **parameters**; when **reproducing** those studies, cite **Fedkin** **et al.** for **force-field** **provenance** and copy **timestep**, **thermostat**, and **box** construction from each **application** article.

## Limitations

Training scope limits transfer to divalent-heavy brines or new organics without extension; concentration and finite-size effects still require care.

**Curation note:** downstream **ambient** electrolyte benchmarks (**[[2019dasgupta-computationa-reaxff-molecular]]**) and **supercritical** extensions (**[[2020dasgupta-j-chem-phys-reaxff-molecular]]**) assume this **parameter** **line**—update **this** page’s **bibliography** if the **JPCA** **issue** pagination is re-verified from the **publisher** PDF. **Ion** **parameters** here are **monovalent-first** by design.

## Relevance to group

Core van Duin-group electrolyte ReaxFF line used downstream in application papers (e.g., Dasgupta Comp. Mater. Sci.).

## Citations and evidence anchors

https://doi.org/10.1021/acs.jpca.8b10453

## Related topics

- [[2019dasgupta-computationa-reaxff-molecular]]
- [[reaxff-family]]
