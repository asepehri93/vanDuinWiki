---
id: paper:2017wen-computationa-atomistic-mechanisms
type: paper
title: "Atomistic mechanisms of Si chemical mechanical polishing in aqueous H2O2: ReaxFF reactive molecular dynamics simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:water-interfaces
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2017.02.005"
year: 2017
authors:
  - "Jialin Wen"
  - "Tianbao Ma"
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
  - "Xinchun Lu"
venue: "Computational Materials Science 131, 230–238 (2017)"
pdf_sha256: "08a1262121e30be8566849470d4d8b1da8296d70f460721964bfffa92a5e2a38"
pdf_path: "papers/Wen_Polishing_CompMatSci_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017wen-computationa-atomistic-mechanisms -->

## Summary

Chemical mechanical polishing (CMP) of silicon uses slurry chemistry and mechanical abrasion to planarize wafers; hydrogen peroxide is a common oxidizer in silica-based slurries. This Computational Materials Science article models CMP at the atomistic level with ReaxFF reactive molecular dynamics, placing a silica abrasive asperity in sliding contact with hydrogen-terminated Si(100) in explicit aqueous hydrogen peroxide. The study contrasts peroxide-driven chemistry with pure-water slurries to isolate how pre-oxidation and shear-induced bond rupture contribute to material removal and friction. van Duin and Lu co-authorship ties the paper to the group’s broader silicon–water and tribochemistry portfolio, including standalone water studies on multiple Si facets. CMP slurries are multicomponent industrial fluids; this model isolates oxidizer chemistry on a single facet to build mechanistic intuition before adding pH buffers or surfactants.

## Methods

**Molecular dynamics (reactive).** The article employs **ReaxFF reactive molecular dynamics** to follow a **silica** abrasive sliding on **hydrogen-terminated Si(100)** in explicit **water**, comparing runs **with** and **without aqueous H₂O₂** so oxidizer chemistry can be isolated while **pressure** and **velocity** remain the paired mechanical knobs (the Preston-style emphasis in the introduction). The indexed excerpt does not reproduce supercell dimensions, exact **atom** counts, or integration **timestep** values—those appear in the **Comput. Mater. Sci.** **Methods** of the **PDF** at `pdf_path`. **Periodic** supercell conventions, target **temperature** (**K**) and **thermal** coupling of the Si slab and aqueous film, **NVT**/**NPT** staging, **thermostat** damping, **equilibration** versus production **duration** (ps/ns), and **barostat** usage should be read from the same source; this page does not substitute for those tables.

**Force-field fitting.** **N/A —** the study applies a published **Si/O/H ReaxFF** parameterization suited to silicon oxidation and tribochemistry; it does not report a new parameter fit in this article.

**Static QM / DFT.** **N/A —** trajectories are reactive MD, not on-the-fly **DFT** dynamics (QM cost is cited as prohibitive for sliding wear in the introduction).

**Review scope.** **N/A —** primary application paper; sibling **`[[2017wen-venue-jp6b11310]]`** covers facet-resolved silicon–water adsorption.

## Findings

**Outcomes and mechanisms.** **H₂O₂** **oxidizes** the Si surface before severe asperity contact, promoting interfacial **Si–O–Si** bridges that link the abrasive to the wafer. Once contact occurs, **shear** strains **Si–Si** and **Si–O** bonds until they rupture, ejecting Si-containing fragments consistent with **material removal**. **Reactive** pathways therefore couple **mechanical** work directly into bond scission rather than treating removal as purely abrasive grooving.

**Comparisons.** **Versus** pure **H₂O**, the peroxide slurry yields a more **oxidized** interface, removes more **Si atoms** in the simulated window, and produces a **higher friction** force because stronger **covalent** interfacial contacts must be broken during sliding.

**Sensitivity / design levers.** The introduction stresses that industrial **CMP** depends jointly on **contact pressure** and **sliding velocity** (Preston-type scalings) and that **H₂O₂ concentration** feeds both roughness and removal trends in experiments cited there; the MD portion is constructed to mirror those paired mechanical and chemical controls.

**Limitations / outlook.** Idealized single-asperity geometry and simplified slurry chemistry omit particle polydispersity, buffers, and surfactants present in fabs.

**Corpus honesty.** Quantitative loads, timesteps, and thermostat labels are not in the short indexed excerpt—confirm all protocol numerics from **`papers/Wen_Polishing_CompMatSci_2017.pdf`** before reproducing trajectories.

## Limitations

Single surface orientation and idealized asperity geometry simplify industrial CMP, where particle size distributions, pH buffers, and additives matter. ReaxFF barriers are empirical. Slurry pH shifts acid–base chemistry at the interface beyond the explicit compositions shown in the idealized model.

## Relevance to group

Direct van Duin-group contribution on Si/SiO\(_x\) tribochemistry paired with other silicon–water entries.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2017.02.005](https://doi.org/10.1016/j.commatsci.2017.02.005)

## Related topics

- [[reaxff-family]]
- [[2017wen-venue-jp6b11310]]
