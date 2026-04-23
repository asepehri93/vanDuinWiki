---
id: paper:2022c-cile-a-c-chazot-nano-lett-0-molecular-alignment
type: paper
title: "Molecular Alignment of a Meta-Aramid on Carbon Nanotubes by In Situ Interfacial Polymerization"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - material:polymer-organic
  - material:graphene-carbon-nano
  - method:classical-md
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:polymer
  - keyword:graphene-carbon
candidate_tags: []
source_refs: []
doi: "10.1021/acs.nanolett.1c03866"
year: 2022
authors:
  - "Cécile A. C. Chazot"
  - "Behzad Damirchi"
  - "Byeongdu Lee"
  - "Adri C. T. van Duin"
  - "A. John Hart"
venue: "Nano Lett."
pdf_sha256: "e33e118b6ea2a3ee194b220f88af37d0eede47a586556ee20a32abacc431fe07"
pdf_path: "papers/Chazot_Damirchi_CNT_polymers_Nano_Letters_2022_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022c-cile-a-c-chazot-nano-lett-0-molecular-alignment -->

## Summary

**CNT**–polymer composites gain performance when **polymer** chains organize at **nanotube** surfaces, but conventional **melt** or **solution** mixing often yields **nonuniform** coverage and **aggregation**. The *Nano Lett.* letter reports **capillary infiltration** combined with **in situ interfacial polymerization** (**ISIP**) to coat **buckypaper** CNT networks with a **conformal** **meta-aramid** (**PMPI**) **sheath**, using **m-phenylenediamine** and **isophthaloyl chloride** across an **organic–aqueous** interface. **FTIR** and **Raman** track **aromatic** and **amide** modes versus loading. **Classical MD** relates **π–π** alignment of **aromatic** rings **parallel** to **CNT** walls to the measured **spectroscopic** shifts, distinguishing **edge-on** versus **face-on** stacking signatures. Microscopy shows **smooth**, **layered** sheaths whose **thickness** scales with **monomer** supply, motivating future **mechanical** characterization of the **nanocomposite** architecture.

## Methods

**1 — MD application (atomistic dynamics).** **Engine / code: LAMMPS** (or the **package** named in *Nano Lett.*) for **classical** **MD** of the **condensation** **interphase** near the **CNT** in the **organic**-rich **region** of the **ISIP** stack. **System** models include **buckypaper**-like **CNT** **geometries** (**cylindrical** and **collapsed** **variants** in **SI**-level comparisons as reported), with **PBC** **appropriate** to the **interfacial** **patch**; **atom** counts, **box** **vectors**, and **excluded** **reactive** **polymerization** **kinetics** (equilibrium-**biased** **snapshots** rather than full **condensation** **kinetics**) are in the **PDF**. **Ensemble, timestep, duration:** **NVT**-class **sampling** with **timestep** and **equilibration**/**production** **durations** stated in the **Computational** section; **thermostat** (e.g. **Nosé–Hoover**-type) and **damping** **constants** are **per** the **article** (this summary does not duplicate every number). **Barostat:** **N/A** for the **interfacial** **slab** **protocols** described as **NVT**-like **interphase** **models**; **NPT** **N/A** unless the **paper** **explicitly** **invokes** **anisotropic** **pressure** (check **VOR**). **Temperature:** set to **room**-temperature **or** **stated** **isotherm** in the **MD** **Methods**. **Pressure, external electric field, enhanced sampling: N/A** as **independent** **MD** **control** **parameters** in the **main** **classical** **protocol** described for **order** **metrics**; **Herman’s** **orientation** **functions** and **aromatic** **normal** **distributions** are **post-processed** from **trajectories**.

**2 — Force-field training.** **N/A** — the study **uses** an **established** **classical** **FF** (see **force** **field** **name** and **charge** **model** in the **article**); it does not report a new **reactive** or **ReaxFF** **fit** here.

**3 — Static QM / DFT-only.** **N/A** as a dominant new **QM** **campaign**; the **theory** **contribution** is **MD**-guided **order** **analysis** plus **FTIR**/**Raman** **correlation**.

**4 — Experiments and characterization.** **ISIP** of **m-phenylenediamine** and **isophthaloyl chloride** across a **cyclohexanone**–**water** **interface** on **CNT** **networks**; **FTIR** and **Raman** of **aromatic** and **amide** **bands** vs **loading**; **microscopy** of **sheath** **morphology** and **thickness** **vs** **monomer** **flux**. The **capillary** **infiltration** + **ISIP** **combination** targets **conformal** **PMPI** **sheaths** on **buckypaper** that are hard to match by **melt** or **post-mix** **compounding** alone.

## Findings

**Outcomes and mechanisms.** **Imaging** shows **smooth** **layered** **sheaths** whose **thickness** **scales** with **monomer** **supply**. **Classical** **MD** supports **face-on**/**edge-on**-aware **π–π** **stacking** of **PMPI** **aromatics** **parallel** to **CNT** **sidewalls** in the **first** **layer**, with **more** **disordered** **chains** **away** from the **wall** in the **model** **geometries** **analyzed**. **FTIR**/**Raman** show **concentration**-dependent **redshifts** and **splittings** of **in-plane** **aromatic** **modes** consistent with **strong** **π–π** **interactions** that **attenuate** with **growing** **coating** **thickness**; **NH–π**-related **features** **move** **less** than **π–π** **bands**, as expected if **H-bonding**-like **coupling** is **weaker** than **stacking** **thermodynamics** in their **interpretation**.

**Comparisons.** **Spectroscopy** and **MD** **order** **metrics** are **cross-compared**; **collapsed** vs **cylindrical** **CNT** **geometries** (where **reported** in **SI**-class **materials**) help **separate** **curvature** **effects** from **generic** **interfacial** **alignment**.

**Sensitivity and levers.** **Polymer** **loading**/**thickness** and **interfacial** **monomer** **availability** are the main **knobs** tying **order** to **signal** in both **simulation** and **experiment**.

**Limitations.** **Classical** **MD** **omits** **fully** **reactive** **polycondensation** **kinetics**; **equilibrium**-**biased** **snapshots** do not **replace** **measured** **reaction** **rates** (see **`## Limitations`**).
## Limitations

Classical MD omits full reactive polymerization kinetics; experimental mixtures include collapsed and cylindrical CNTs complicating universal quantitative comparison. **ISIP** **kinetics**—**diffusion**-limited **monomer** **supply** versus **fast** **interfacial** **polycondensation**—are only partially represented in **equilibrium**-biased **MD** **snapshots**, so **quantitative** **growth** **rates** should be taken from **experiment**, not from the **simulation** **patch** alone.

## Relevance to group

van Duin-group MD supports interpretation of polymer–nanotube ordering for high-performance composites.

## Citations and evidence anchors

- DOI: [10.1021/acs.nanolett.1c03866](https://doi.org/10.1021/acs.nanolett.1c03866)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
