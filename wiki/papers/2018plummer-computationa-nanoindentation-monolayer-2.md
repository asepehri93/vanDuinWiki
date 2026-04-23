---
id: paper:2018plummer-computationa-nanoindentation-monolayer-2
type: paper
title: 'Nanoindentation of monolayer Tin+1CnTx MXenes via atomistic simulations: The
  role of composition and defects on strength'
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:2d-layered
- domain:mechanics-tribology
- domain:reactive-md
- method:reaxff
- task:application
- scale:atomistic
paper_keywords:
- keyword:reaxff-application
- keyword:lammps
- keyword:2d-materials
- keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: 10.1016/j.commatsci.2018.10.033
year: 2018
authors:
- Gabriel Plummer
- Babak Anasori
- Yury Gogotsi
- Garritt J. Tucker
venue: Computational Materials Science
pdf_sha256: 6ae7eadc064c42911e9123d198b7d952549e81e7be8b8b73cb8c76e83b1c0df9
pdf_path: papers/ReaxFF_others/Plummer_Gogotsi_CompSciMat_MXene_2019.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018plummer-computationa-nanoindentation-monolayer-2 -->

## Summary

Plummer, Anasori, Gogotsi, and Tucker (*Computational Materials Science* **157** (2019) 168–174; DOI `10.1016/j.commatsci.2018.10.033`; available online 8 November 2018) simulate **nanoindentation** of oxygen-terminated **Ti₃C₂O₂** and **Ti₂CO₂** MXene monolayers with **ReaxFF** in **LAMMPS** to extract Young’s moduli and quantify softening from titanium and carbon vacancies. The abstract in the extract states that Young’s moduli for pristine Ti₃C₂O₂ and Ti₂CO₂ are **466 GPa** and **983 GPa**, respectively, and that a defective Ti₃C₂O₂ sample with **1% V_Ti** and **10% V_C** yields **386 ± 31 GPa**, mirroring experimental sensitivity of MXenes to defects and comparing defect-containing Ti₃C₂O₂ to **graphene oxide** moduli for solution-processed 2D materials. The introduction recounts MXenes’ 2011 discovery, selective etching of MAX phases, and application spaces (energy storage, composites, membranes, sensors), motivating fundamental mechanical characterization.

## Methods
**1 — MD application (simulated nanoindentation).** **ReaxFF** (**Ti₃C₂Tₓ**-compatible parametrization cited in *Computational Materials Science*) is used in **LAMMPS** with **QEq-style** charge equilibration and documented nonbond cutoffs (see article). **PBC:** **periodic in-plane** **monolayer** cells of **oxygen-terminated Ti₃C₂O₂** and **Ti₂CO₂**; a **rigid spherical indenter (10 nm diameter)** advances at **10 m·s⁻¹** along the surface normal while recording **force–displacement** curves (**OVITO** visualization). **Ensemble:** **NVT** at **1 K** to suppress thermal noise during modulus extraction. **Timestep:** **0.25 fs**. **Defect models:** additional **Ti₃C₂O₂** cells include **~1 % Ti vacancies** and **~10 % C vacancies** simultaneously as in the abstract. **Duration / staging:** follow the staged **relaxation + indentation** protocol in the paper (exact **ps/ns** windows in **Methods**/**figures**). **Thermostat / temperature control:** same protocol as the sibling page: **1 K** held during indentation in the **canonical (NVT) ensemble** with details in `papers/ReaxFF_others/Plummer_Anasori_Gogotsi_MXene_indentation_2019.pdf`. **Barostat / pressure:** **N/A —** **NVT** indentation without hydrostatic **NPT** barostat control. **Electric fields / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** applies a published **MXene** **ReaxFF** parametrization with **DFT** training heritage referenced in the article.

**3 — Static QM.** **N/A —** not a DFT-only study.

**Corpus / duplicate note:** same DOI and simulation definition as **[[2018plummer-computationa-nanoindentation-monolayer]]**; only `pdf_path` / SHA differ in this manifest.

## Findings
**Outcomes:** reported **Young’s moduli** are **~466 GPa** (**pristine Ti₃C₂O₂**) and **~983 GPa** (**pristine Ti₂CO₂**); combined **Ti + C** vacancies reduce **Ti₃C₂O₂** to **~386 ± 31 GPa** in the quoted defective model.

**Comparisons:** defective **Ti₃C₂O₂** is compared to **graphene oxide** moduli cited for **solution-processed** **2D** materials.

**Sensitivity:** **composition** (**n+1,n** family member) and **vacancy loading** strongly shift stiffness extracted from **indentation** slopes.

**Limitations:** **1 K** sampling suppresses **thermal** effects; **rigid indenter** + **classical** **ReaxFF** omit explicit **electronic** plasticity.

**Corpus honesty:** moduli and defect percentages are taken from the **abstract** on `pdf_path`; verify against **Comput. Mater. Sci.** tables.

## Limitations

Low temperature (1 K) suppresses thermal phonon effects; the rigid indenter and empirical potential omit explicit electronic plasticity and may over- or under-estimate defect interactions at room temperature.

Indentation at cryogenic temperatures isolates mechanical stiffening from thermally activated defect migration, which is useful for comparing potentials but diverges from room-temperature experiments unless thermal effects are explicitly reintroduced in follow-on work. Readers should treat the quoted moduli as comparative screening metrics within the article’s model assumptions rather than as direct predictions of ambient nanoindentation experiments on exfoliated MXene flakes.

## Relevance to group

Demonstrates ReaxFF-based indentation workflows for MXene mechanical screening relevant to 2D carbide mechanics literature in the knowledge base.

## Reader notes (navigation)

- Canonical duplicate: [[2018plummer-computationa-nanoindentation-monolayer]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: [10.1016/j.commatsci.2018.10.033](https://doi.org/10.1016/j.commatsci.2018.10.033)
