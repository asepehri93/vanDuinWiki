---
id: paper:2019fedkin-x-development-reaxff
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
  - keyword:galley-or-proof-pdf
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
venue: "J. Phys. Chem. A 2019, 123, 2125-2141 (proof PDF in corpus)"
pdf_sha256: "7151580d3fef2df218d7ca9d6404244db639396ab094117c77ceb021b47ce10e"
pdf_path: "papers/Fedkin_JPCA_Electrolyte_2019_proof.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019fedkin-x-development-reaxff -->

Proof-stage **J. Phys. Chem. A** PDF for the Fedkin et al. electrolyte-water ReaxFF parameterization; scientific content matches [[2019fedkin-j-phys-chem-development-reaxff]].

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow the publication identified by `doi`. Prefer the **journal-formatted** PDF on [[2019fedkin-j-phys-chem-development-reaxff]] for pagination and figure quality.

## Summary

A ReaxFF parameterization is developed for water plus monovalent electrolytes: cations Li⁺, Na⁺, K⁺, Cs⁺ and anions F⁻, Cl⁻, I⁻. Parameters are trained to quantum-chemistry data on cluster geometries, water binding energies, hydration energies, and proton-transfer energetics, then validated with molecular dynamics on dissociation behavior, radial distribution functions versus DFT, and diffusion trends in alkali hydroxide and chloride solutions across concentration. The work is positioned as extending **transferable** water models toward **electrolyte** environments relevant to **batteries**, **corrosion**, and **geochemical** brines, where **ion pairing** and **proton transport** must coexist in one reactive framework.

## Methods

### Force-field training and QM reference data (A)

The parametrization extends **general H/O water parameters** from prior transferable ReaxFF water descriptions (cited in the article) by optimizing **M–O/H** and **X–O/H** interactions for **M = Li, Na, K, Cs** and **X = F, Cl, I**. QM-derived training sets include: **bond lengths and angles** for cluster conformations of **M⁺ or X⁻ with water**, **MOH or HX with water**, and **MX with water**; **water binding energies** taken as energy differences between clusters with **n** vs **n − 1** water molecules (most stable structures when multiple arrangements exist); **hydration energies**; and **proton-transfer** energetics along paths relevant to aqueous electrolytes. **DFT/QM** program, functional, basis, and convergence settings follow **section 2** of the journal article—use **[[2019fedkin-j-phys-chem-development-reaxff]]** (version-of-record PDF) for table-level detail when this proof PDF differs in pagination.

### Molecular dynamics validation protocols (B)

**Reactive MD** with the fitted field evaluates **degree of aqueous dissociation / ion pairing**, **radial distribution functions** for **cation or anion with O and H of water** against **DFT** references, and **self-diffusion of water** plus **ionic diffusion** in **alkali metal hydroxide and chloride** solutions over **composition and concentration** ranges reported in the paper. **ReaxFF** integration follows standard **bond-order** and **charge equilibration** schedules for the engine family (**LAMMPS / PuReMD-class** workflows). **Ensemble, timestep, system size, and thermostating** are specified in **Computational Methods** (from **§2.1** onward) in the peer-reviewed article—not duplicated here.

### Note on paper type (D)

This is a **parameterization + bulk validation** study, not a review of experimental electrochemistry databases.

**Bulk validation MD (electrolyte solutions and crystals).** **ReaxFF molecular dynamics** in **LAMMPS** / **PuReMD-class** engines evaluates **ion pairing**, **radial distribution functions**, and **self-/ionic diffusion** in **three-dimensional periodic** **supercells** sized from **dilute** (order **10²–10³ atoms**) to **concentrated** solutions and **ionic crystals** as tabulated in **Computational Methods** (`pdf_path`). **Ensemble:** **NVT** **thermal** equilibration and **production** segments at the **K** setpoints for each **composition**; **timestep** in **fs** and **production** lengths in **ps**/**ns** are given in **§2**. **Thermostat:** type and damping constants appear alongside those runs in the article. **Barostat / hydrostatic pressure control:** **N/A** — validation stays at **constant volume** without **GPa** **stress** servocontrol in the summarized protocol. **External electric field:** **N/A**. **Replica exchange / umbrella / metadynamics:** **N/A** for the bulk **RDF** and **diffusion** trajectories described in the abstract. **Corpus note:** this slug’s **proof** `pdf_path` may differ in **pagination** from the **version-of-record** PDF on [[2019fedkin-j-phys-chem-development-reaxff]].

## Findings

### Mechanisms and trends

**Ion–water structure:** RDFs for most **cation/anion–water** pairs match **DFT** RDFs in the comparison sets. **Dissociation** behavior and **concentration-dependent diffusion** for **alkali halide and hydroxide** solutions follow the trends emphasized for validation. **Cluster-level** targets (binding, hydration, proton transfer) remain **consistent** with **bulk** **RDF** and **transport** observables—the usual bottleneck when moving from **small-cluster** fits to **condensed-phase** electrolytes.

### Limitations and open items

Scope is **monovalent** **Li/Na/K/Cs** and **F/Cl/I** with the stated training corpus; **divalent ions**, **complex organics**, or **battery-specific additives** are not covered without further fitting. **Interfacial** or **electrode** environments are not the primary validation target here.

### Future directions (as framed in the article)

The abstract highlights using the field for **intermediate-to-large** electrolyte systems and **longer** reactive timescales than QM—**device-scale** **conductivity**, **viscosity**, or **SEI** chemistry should cite downstream papers for **cell geometry** and **boundary conditions**, not this bulk parameterization alone.

## Limitations

Training scope limits transfer to divalent-heavy brines or new organics without extension; prefer the **version-of-record** PDF for external citations. Concentration and finite-size effects still require care in application studies. The checked-in **proof** PDF may differ cosmetically from the **issue** PDF in **pagination** and **figure** quality—use the **DOI** landing page when preparing **camera-ready** citations for **external** audiences. **Ion** **conductivity** and **viscosity** comparisons in application studies should cite **simulation** **conditions** (**box** size, **electrode** treatment) documented in downstream papers, not inferred from this methods summary alone.

## Relevance to group

Duplicate ingest for the electrolyte parameterization flagship; use one narrative for automation where possible.

## Citations and evidence anchors

- [https://doi.org/10.1021/acs.jpca.8b10453](https://doi.org/10.1021/acs.jpca.8b10453)

## Reader notes (navigation)

- Primary PDF and full protocol detail: [[2019fedkin-j-phys-chem-development-reaxff]].

## Related topics

- [[2019fedkin-j-phys-chem-development-reaxff]]
- [[reaxff-family]]
