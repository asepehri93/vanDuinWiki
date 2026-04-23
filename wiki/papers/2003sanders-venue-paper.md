---
id: paper:2003sanders-venue-paper
type: paper
title: "Interatomic potentials for SiO₂ including bond-bending terms"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:oxides-ceramics
  - method:classical-md
  - material:silicate-glass
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/C39840001271"
year: 1984
authors:
  - "M. J. Sanders"
  - "M. Leslie"
  - "C. R. A. Catlow"
venue: "J. Chem. Soc., Chem. Commun."
pdf_sha256: "11cba43b4ee0718ef43d47f3370099f67618b7a8b473acab2ec90da3662ea8b5"
pdf_path: "papers/Others/Sanders_Leslie_Catlow_JChemSoc_SiO2_1984.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2003sanders-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Sanders, Leslie, and Catlow extend **classical Born-model** **silicate** potentials by adding explicit **O–Si–O bond-bending** contributions so that **α-quartz** and other **SiO\(_2\)** **polymorphs** can be described without the well-known failures of **pure two-body central-force** models. The short-range **Si–O** and **O–O** interactions use a **Buckingham** form, while each **O–Si–O** angle receives a **quadratic** penalty \(E_B = K_B(\theta - \theta_0)^2\) with \(\theta_0\) set to the **tetrahedral** value (**109.47°**) to represent the **directional** component of **sp\(^3\)**-like bonding at silicon. **Oxygen** **shell-model** **polarizability** is retained so **dielectric** and **lattice-dynamic** data can be fit simultaneously. The **Chem. Commun.** communication argues that this extension yields **quantitative** agreement with **experimental** **elastic constants**, **dielectric tensors**, and **phonon-related** checks for **quartz**, whereas a **two-body-only shell model** fit to the same data remains **inferior** (including poor **phonon dispersion** behavior noted in the text).

## Methods


**Potential fitting / static lattice tests (checklist A/C)**—this **Chem. Commun.** note develops a **rigid-ion / shell** **SiO\(_2\)** model and validates it with **lattice dynamics** and **property** calculations; **no finite-temperature MD** protocol is reported.

### Functional form / lineage

- **Short-range:** **Buckingham** interactions for **Si–O** and **O–O**; **oxygen** treated with the **shell model** for **polarizability** (as in prior **Catlow**/**Sanders** **silicate** work referenced in the communication).
- **Directionality:** explicit **O–Si–O** **bond-bending** term **\(E_B = K_B(\theta-\theta_0)^2\)** with **\(\theta_0=109.47^\circ\)** to capture **tetrahedral** constraints beyond **two-body** **central** forces.

### Training / optimization

- **Fitting:** **least-squares** adjustment of **\(K_B\)**, **shell** parameters, and **Buckingham** coefficients against **experimental** **α-quartz** data (elastic, dielectric, structural) with **internal** coordinates relaxed in the fit (Sec./tables in the communication).
- **Lattice dynamics:** **first** and **second** derivatives constructed for **phonon** / **dispersion** evaluation as described in the paper (used to contrast **bond-bending** vs **two-body-only** fits).

### Transferability tests (static / 0 K)

- **Pressure:** **α-quartz** under **hydrostatic pressure**—tabulated **Si–O–Si** angles vs **pressure** (**kbar**) in the communication.
- **Polymorph survey:** parameters carried to **α-cristobalite**, **coesite**, and **tridymite** to probe **transferability** of the **bond-bending** extension.

### MD application (not reported)

This **Chem. Commun.** note develops and tests a **lattice-dynamics** / static-lattice model; it does **not** report finite-temperature **molecular dynamics** production trajectories. **N/A — MD engine**; **N/A — atom count** as a dynamical simulation cell; **N/A — PBC** for MD; **N/A — NVE/NVT/NPT** MD ensemble; **N/A — timestep**; **N/A — MD duration**; **N/A — thermostat**; **N/A — barostat** (hydrostatic **pressure** enters the **static** **α-quartz** survey in the communication, not an MD barostat); **N/A — MD temperature** schedule; **N/A — MD stress control**; **N/A — electric field** in MD; **N/A — enhanced sampling**. Grounding: `papers/Others/Sanders_Leslie_Catlow_JChemSoc_SiO2_1984.pdf`, `normalized/extracts/2003sanders-venue-paper_p1-2.txt`.

### Force-field training (QM reference)

The communication emphasizes **experimental** **α-quartz** targets plus **lattice-dynamics** derivatives. **QM / DFT reference:** **N/A —** the indexed summary does not cite a **DFT** training database for this **1984** shell-model fit (contrast with modern **plane-wave** fits); parameters are adjusted by **least-squares** against **experimental** elastic, dielectric, and structural data together with **phonon** checks, as described in the primary PDF.

## Findings

For **α-quartz**, the **bond-bending** model reproduces the **experimental** **elastic constants** and **static**/**high-frequency** **dielectric** entries in the authors’ **Table 2** far better than the **two-body-only** counterpart fit to the same training set. **Phonon dispersion** for **α-quartz** is described as agreeing well with experiment when **bond-bending** is included, in contrast to the **central-force-only** parametrization. **Pressure-dependent** **Si–O–Si** angles also track measured trends (table of **kbar** versus angle in the communication). The authors conclude that **bond-bending** terms can often be **grafted** onto existing **central-force** **shell** models without refitting the **repulsive** **Si–O** parameters, simplifying adoption in **zeolite** and **feldspar** simulations.

## Limitations

The model remains **fixed-charge** / **shell** **ionic** mechanics—**reactive** **bond formation**, **proton** transport, and **covalent** **charge** redistribution require **ReaxFF** or **QM** methods. **`extraction_quality`** is **partial** in metadata because some corpus tooling predates clean full-text extracts; consult **`papers/Others/Sanders_Leslie_Catlow_JChemSoc_SiO2_1984.pdf`** for tables.

## Relevance to group

Historical **silica** **FF** lineage relevant to **oxide** and **silicate** simulation traditions that intersect **ReaxFF** **Si/O** parameterization literature.

## Citations and evidence anchors

- **DOI:** https://doi.org/10.1039/C39840001271 — *J. Chem. Soc., Chem. Commun.*, **1271** (1984).

## Related topics

- [[reaxff-family]]
