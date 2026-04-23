---
id: paper:2021zare-physical-che-reactive-force
type: paper
title: "Reactive force fields for aqueous and interfacial magnesium carbonate formation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - domain:water-silica-geo
  - material:oxide
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:water-interfaces
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1039/D1CP02627E"
year: 2021
authors:
  - "Siavash Zare"
  - "Mohammad Javad Abdolhosseini Qomi"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "91bd92524c213e99f12e1bb5551fe2a34ab9baafce9b645963cef01baafdfc01"
pdf_path: "papers/ReaxFF_others/MgCO3_Irvine_PCCP_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2021zare-physical-che-reactive-force -->

## Summary

Aqueous **magnesium carbonate** mineralization is a multistep problem coupling **Mg²⁺ hydration**, **carbonate/bicarbonate speciation**, and **rearrangements at mineral–water interfaces**. This *Physical Chemistry Chemical Physics* article develops **Mg/C/O/H ReaxFF** parameterizations in two coupled flavors: a **bulk aqueous** field that treats **Mg²⁺** with fixed integer charge and uses **nonbonded** interactions plus **Buckingham** terms to ionic oxygen/hydrogen partners, and an **interfacial** field tailored for **minerals** and **mineral–water** contacts where surface chemistry dominates. The work targets scenarios relevant to **CO₂ mineralization** and low-temperature magnesite formation where interfacial water structure and proton transfer are first-order physics.

## Methods

**2 — Force-field training (Mg/C/O/H).** The authors build **ReaxFF** in two **coupled** parts: a **bulk aqueous** set with **Mg²⁺** on **fixed** **integer** **charge** and **nonbonded** + **Buckingham** **O**/**H** **partners**, and an **interfacial** set for **minerals** and **mineral–water** **contacts**. **QM** training data include **brucite**, **magnesite**, **magnesia**, **MgH\(_2\)**, **Mg\(_2\)C** **crystals**, **Mg²⁺–(H\(_2\)O)\(_n\)** **clusters**, **ion pairs**, and **water** on **mineral** **surfaces**; see *PCCP* for **DFT** level, weights, and **optimization** workflow.

**1 — MD application (ReaxFF in LAMMPS).** **Reactive** **MD** of **forsterite–(H\(_2\)O)** and **brucite–(H\(_2\)O)** with **HCO\(_3\)\(aq\)\)**-related **interfacial** speciation, tracking **H**-transfer, **HCO\(_3\)\(^-\)**→**CO\(_3\)\(^{2-}\)**-like evolution, and **interlayer** **OH\(...\)\)** **dynamics** (see abstract: **~0.22 eV** “attachment” **G**-barrier language; exact definition in article). This wiki note is grounded in abstract-level reporting, so MD protocol slots are marked explicitly: **Ensemble: N/A (NVE/NVT/NPT mode not stated in indexed text); Duration/stages: N/A (not stated); Barostat: N/A (not stated); Temperature schedule: N/A (not stated); Pressure control/target: N/A (not stated)**. **Engine:** LAMMPS (as reported). **System focus:** mineral-water interfaces noted above. **Timestep, thermostat details, boundary conditions, and atom counts: N/A (not stated in indexed text)**. **Electric / bias field and enhanced sampling (umbrella/metadynamics): N/A** in abstract-level scope.

**3 — Static DFT (standalone production work).** **N/A** — the paper’s **new** DFT is embedded in the **ReaxFF** **training/validation** pipeline rather than a separate large **static** **study** summarized here.

**4 — Experiments.** **N/A** — **CO\(_2\)** **mineralization** discussion references **literature** **experiments**; the authors’ new evidence is **ReaxFF**-based.

## Findings

**Outcomes and mechanisms.** At the **forsterite–water** interface with **bicarbonate**, **ReaxFF** **MD** shows **long-range proton transfer** that drives **bicarbonate** toward **carbonate**; the **abstract** reports a **~0.22 eV** **G**-barrier for **carbonate** **attachment** to **Mg** sites, **comparable in magnitude** to **aqueous** **Mg²⁺**–**CO\(_3\)\(^{2-}\)** **ion pairing** in the same model. **Hydroxide** **diffusivity** in the interfacial water is **anisotropic** and **heterogeneous** (abstract). The authors use these results to discuss **magnesite** **nucleation** at **low** **T** in **H\(_2\)O-poor**, **CO\(_2\)\)**-rich interfacial conditions consistent with **cited** **experiments**. **N/A** in this note to list every water layer or all **H**-bond statistics — see **PCCP** **figures**/**SI**. **Comparisons** to **literature** and **outlook** are in the main text.

## Limitations

**Fixed** Mg charge omits **polarizable-ion** physics that may matter in highly charged electric double layers or unusual solvation states; users should validate edge cases against higher-level electronic structure where feasible.

## Reproducibility notes

Mineral nucleation runs should archive **pH/CO₂** effective driving forces as implemented in the classical ensemble (even if implicit), **water density** near interfaces, and how **carbonate** species are initialized—proton-transfer cascades can depend on starting speciation. When reporting **0.22 eV** barriers, cite the **sampling** method used for free energies (biasing vs umbrella) as stated in the article.

For **forsterite** surfaces, confirm that the modeled surface orientation and **Mg/O** termination match the experimental samples discussed—different cleavage planes expose distinct Mg densities and can change carbonate docking statistics even with the same force field. If comparing **brucite** versus **forsterite** interfacial water diffusivities, report **water layer** thickness and **shear** vs **normal** sampling windows separately—anisotropy can be a property of the analysis slab, not only the mineral.

## Reader notes (navigation)

- [[reaxff-family]]
