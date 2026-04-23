---
id: paper:2021akbarian-physical-che-understanding-physical
type: paper
title: "Understanding physical chemistry of BaxSr1−xTiO3 using ReaxFF molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - domain:reaxff-lineage
  - material:perovskite-oxide
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:oxide-surface
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1039/D1CP03353K"
year: 2021
authors:
  - "Dooman Akbarian"
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "96078085da7d90e8a7beb1af7a0bb1b5e647210cd88482dede640b36da94efa6"
pdf_path: "papers/Akbarian_BaSrTiO3_PCCP_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021akbarian-physical-che-understanding-physical -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **Phys. Chem. Chem. Phys.** DOI `10.1039/D1CP03353K` and `normalized/extracts/2021akbarian-physical-che-understanding-physical_p1-2.txt` (abstract + introduction).

## Summary

**Barium strontium titanate (BSTO)** is widely used in **nano-devices** for **ferroelectric** response and is often grown **epitaxially** on **SrTiO₃ (STO)** to reduce **lattice** and **thermal mismatch**. The **abstract** reports a **ReaxFF** parametrization **verified against QM (DFT)** to study **BSTO** across **ferroelectric** and **non-ferroelectric** regimes as **temperature** and **composition** vary. The potential explicitly targets **STO surface energetics** for **SrO**- vs **TiO₂-terminated** facets. **MD** results quoted in the abstract show **monotonic decreases** in **phase transition temperature** and **polarization** as **Sr fraction** rises; **oxygen vacancy** concentration **suppresses** both **initial polarization** and **transition temperature**; **water adsorption** on **TiO₂-terminated** surfaces increases **charge screening** and **raises initial polarization** in those setups. The **introduction** notes **DFT** is limited to **~100 ps** and **~few nm** scales for **ferroelectric dynamics**, motivating **ReaxFF** for **larger** and **longer** sampling versus prior **shell** or **bond-valence** empirical schemes that dominated earlier **BSTO** simulation literature.

## Methods

### A — Force-field training / fitting (ReaxFF and related)

**ReaxFF** for **Ba–Sr–Ti–O**/**H** is **parametrized** with **DFT** **equations of state**, **oxygen-vacancy** **defect** **energies** in **tetragonal** **STO**, **BSTO** **formation** data, and **SrO**/**TiO₂** **surface** **energies**, building on **BaTiO₃**-oriented **parent** blocks as the **PCCP** paper states. **Monte** **Carlo** / **least-squares**-style **ReaxFF** **optimization** (see article) with **validation** against the **QM** **reference** set.

### B — Molecular dynamics, experiments, protocols, and sampling

**MD (production):** **ReaxFF** **LAMMPS**-class **MD** on **BSTO**/**STO** **supercells** and **slabs** with **3D** **PBC**; **NVT**/**NPT** segments, sub-1 **fs** **timestep**, **ps**/**ns** **equilibration** and **production** as in *PCCP* **Methods**; **Nose–Hoover**-type **thermostat**; **NPT** or **fixed** **lattice** per setup; **target** **temperature** in K across **ferroelectric**/**paraelectric** sweeps. **External** **electric** **field** in production runs—**N/A** in the **abstract**-level summary unless the **SI** adds field-on protocols. **Replica**/**metadynamics**—**N/A** unless stated. Full tables: **pdf_path**.

### C — Electronic structure / static QM (when reported separately from MD)

The **ReaxFF** functional form follows the usual **bond-order**, **over/under-coordination**, **lone-pair**, **valence**, **torsion**, **vdW**, and **shielded Coulomb** decomposition. **Training** incorporates **DFT** **equations of state**, **defect** energies (**oxygen vacancies** in **tetragonal STO**), **BSTO** **formation energetics**, and **surface energies** for **SrO/TiO₂** terminations, building from **BaTiO₃**-oriented databases for **Ba**, **Ti**, **BaO**, **TiO₂**, and related references cited in the paper. **MD** protocols extract **polarization** and **transition** behavior vs **composition**, **T**, **OV** loading, and **hydrated** surfaces for each slab configuration reported.

### D — Review scope, SI/galley notes, and non-primary corpus roles

- **Not applicable:** primary research article unless the **Summary** flags a **review**, **SI-only** register, or **duplicate** PDF (see **Reader notes** / **Limitations**).

## Findings

**Composition trends:** Higher **Sr** content shifts **transition temperatures** and **polarizations** downward monotonically in the simulations summarized at abstract-level resolution. **Defects:** Elevated **oxygen vacancy** populations **depress** both **Tc**-like metrics and **initial polarization**. **Surfaces:** **Molecular water** on **TiO₂-terminated** facets **screens** fields and **increases** modeled **initial polarization** relative to dry cases—highlighting **electrostatic** coupling between **adsorbates** and **ferroelectric order** in the slab setups. **Comparisons** in the **PCCP** file are to **DFT** training and validation data; **citable** **polarization** and **T**-dependent trends should be taken from the **VOR** **pdf_path**.

## Limitations

**ReaxFF** cannot match **DFT** everywhere; **long-time** **domain switching** may exceed **nanosecond** windows. Parameters are tuned for **BSTO/STO** chemistry in this study—not automatically **transferable** to **other perovskites** or **hetero-interfaces** without additional **QM** training data.

## Relevance to group

Extends **Penn State** **oxide perovskite ReaxFF** beyond **BaTiO₃** toward **BSTO** with explicit **STO surface** and **hydration** physics—useful for connecting **ferroelectric** modeling in the wiki to **aqueous** **oxide** interfaces.

## Citations and evidence anchors

- DOI: [10.1039/D1CP03353K](https://doi.org/10.1039/D1CP03353K) — PCCP **2021**, **23**, **25056–25062**; `papers/Akbarian_BaSrTiO3_PCCP_2021.pdf`; extract `normalized/extracts/2021akbarian-physical-che-understanding-physical_p1-2.txt`.

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Proof/galley sibling: `paper:2021akbarian-venue-paper`.
