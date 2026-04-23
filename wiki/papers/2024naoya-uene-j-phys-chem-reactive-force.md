---
id: paper:2024naoya-uene-j-phys-chem-reactive-force
type: paper
title: "Reactive Force Field Molecular Dynamics Studies of the Initial Growth of Boron Nitride Using BCl3 and NH3 by Atomic Layer Deposition"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:catalysis-surfaces
  - domain:reactive-md
  - material:hexagonal-boron-nitride
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.3c06704"
year: 2024
authors:
  - "Naoya Uene"
  - "Takuya Mabuchi"
  - "Masaru Zaitsu"
  - "Shigeo Yasuhara"
  - "Adri C. T. van Duin"
  - "Takashi Tokumasu"
venue: "J. Phys. Chem. C 128, 1075–1086 (2024)"
pdf_sha256: "b14124f29f7821562d223f0153fa2cf17a621b9e2abb2f772d19ac84d08f13e3"
pdf_path: "papers/Uene_2024_BN_BCl3_JPC.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024naoya-uene-j-phys-chem-reactive-force -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Develops a **ReaxFF** description for **BN ALD** from **BCl\(_3\)** + **NH\(_3\)**, trains bonded/geometry-sensitive terms against **DFT**, and runs **cycle-resolved ReaxFF MD** mimicking **pulse–purge ALD** steps. The growth story is decomposed into **surface diffusion**, **BN cluster nucleation/growth**, **HCl formation/diffusion/desorption**, and temperature-sensitive **competition** between **3D cluster growth** vs **2D film growth** across five simulated cycles. **Substrate temperature** modulates **initial growth mode** and **film thickness**—too-high **T** accelerates **desorption** of gases/clusters, suppressing film thickening in the regimes explored. **Industrial** **ALD** of **h-BN** is motivated by **dielectric** and **diffusion-barrier** applications; **BCl\(_3\)/NH\(_3\)** chemistry is **highly reactive**, so **atomistic** models must treat **halogen** **byproducts** explicitly.

## Methods

- **QM reference / ReaxFF training:** Parameters are trained against **density functional theory** data describing **BCl\(_3\)** geometries and **BCl\(_3\)**/**NH\(_3\)** **surface** reactions that produce **BN** films and **HCl** (abstract and §2 opening in `normalized/extracts/2024naoya-uene-j-phys-chem-reactive-force_p1-2.txt`). The peer-reviewed article specifies the **DFT** program, **functional**, **basis/cutoffs**, and training sets; those details are **not fully reproduced** in the short checked-in extract (truncated mid-§2.1).
- **ALD cycle in ReaxFF MD:** The process is modeled as **four** repeated steps: **(1)** **BCl\(_3\)** pulse, **(2)** first purge, **(3)** **NH\(_3\)** pulse, **(4)** second purge (abstract). The abstract reports **five** simulated **ALD** cycles.
- **Growth decomposition (abstract):** **(i)** **BCl\(_3\)**/**NH\(_3\)** **surface diffusion**, **(ii)** **BN** cluster **formation/growth**, **(iii)** **HCl** formation, **(iv)** **HCl** surface diffusion, **(v)** **HCl** desorption.
- **Reactive MD implementation:** **ReaxFF** **bond-order** dynamics as described in §2.1 of the article; **integration timestep**, **thermostat**, **substrate** **supercell** size, and **temperature** setpoints for each pulse are given in the full **PDF** at `pdf_path`—consult it for values not stated in the extract on disk.

**1 — MD application (ReaxFF production).** **Engine / code:** ReaxFF **reactive MD** (§2.1; LAMMPS-class usage is typical for this corpus—confirm in the VOR **PDF**). **System and boundaries:** BCl\(_3\) and NH\(_3\) on a **surface** slab with **PBC** as defined in *Computational Methods*; **atom counts**, full **cell** vectors, and layer counts are **not** in the short **p1–2** extract (truncated mid-§2.1). **Cycle protocol (abstract):** **(1)** BCl\(_3\) pulse, **(2)** first purge, **(3)** NH\(_3\) pulse, **(4)** second purge, repeated for **five** **ALD** cycles. **Stages (abstract):** (i) **surface diffusion**, (ii) **BN** **cluster** nucleation/growth, (iii) **HCl** formation, (iv) **HCl** diffusion, (v) **HCl** desorption. **Ensemble, timestep, thermostat, total trajectory length, barostat, stress, E-field, enhanced sampling:** **N/A in this page summary** — the indexed excerpt does not list **NVT** **thermostat** coupling, **fs** **timestep**, or **ps**/**ns** **duration** of each **pulse**/**purge** (total **production** **time** per **cycle** is in the **full** **article** at **`pdf_path`**). **N/A** — no **NPT**/**barostat**, external **electric field**, or **umbrella/metadynamics** protocol is stated in the **abstract**-level text summarized here (confirm negation in the full article if needed).

**2 — Force-field training.** **Parent:** ReaxFF parameterization for **B/N/Cl/H** and **BN** from **BCl\(_3\)/NH\(_3\)** **surface** reactions. **QM reference:** **DFT** (program, functional, basis, cutoffs) in §2 for **BCl\(_3\)** and surface pathways to **BN** and **HCl**—**full tables not in the p1–2 extract on disk**. **Training set and optimization:** QM **bond/angle/energy** targets and iterative ReaxFF refinement (see article §2–3). **Reference / validation data:** DFT (primary); experimental comparisons as cited by the authors.

**3 — Static QM** — DFT is the **reference for fitting**, not a separate static-only **results** paper; detailed settings are in the article text/SI.
## Findings

**Outcomes and growth modes.** Across **five** **ALD** cycles, simulations report **coexisting** **3D** **cluster** growth and **2D** **film** growth. **HCl** formation, surface diffusion, and desorption couple to **BN** coalescence.

**Comparisons and levers (temperature).** **Substrate temperature** shifts the balance: **moderate** **T** supports **BN** **cluster** formation/growth, while **excess** **T** increases **desorption** of **gas-phase** species and **BN** **clusters**, **reducing** net **film** **thickening** in the regimes highlighted in the **abstract**—so precursor flux alone does not control smoothness if **byproduct** removal is too fast.

**Authored limitations.** Chamber-scale **fluid**/**reactor** **physics** and long-time **industrial** **ALD** are outside the **periodic** **slab** model (see **`## Limitations`**).
## Limitations

Simulation duration/cycles are still far below industrial wafer-scale times; surface models omit full reactor fluid dynamics—ALD **macroscale coupling** is named as future work in the abstract.

**Chamber** **wall** **reactions**, **precursor** **parasitic** **CVD**, and **wafer** **temperature** **nonuniformity** during **pump/purge** cycles are not represented in the **periodic** **slab** **ALD** **loop**; use the **ReaxFF** **trends** as **relative** **comparisons** between **temperature** **setpoints** rather than **absolute** **Å/cycle** **numbers** for **production** **tools**.

## Relevance to group

Industrial **ALD** collaboration (**Japan Advanced Chemicals / Tohoku**) with **van Duin** co-authorship; complements gas-phase **BN** synthesis papers (**[[20220000-0002-1558-1560-x-reaxff-force]]**) with a **surface-process** viewpoint.

## Citations and evidence anchors

https://doi.org/10.1021/acs.jpcc.3c06704 — Abstract (~pp. 1–2) lists ALD loop stages and growth steps (i–v).

## Related topics

- [[2023uene-venue-paper]]
- [[20220000-0002-1558-1560-x-reaxff-force]]
- [[reaxff-family]]
