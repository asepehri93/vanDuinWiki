---
id: paper:2018plummer-computationa-nanoindentation-monolayer
type: paper
title: 'Nanoindentation of monolayer Tin+1CnTx MXenes via atomistic simulations: The
  role of composition and defects on strength'
updated: "2026-04-20"
confidence: med
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
pdf_sha256: 97941d6257b44b5d144b20d5181acf59c84771e63e043d83e24617300a3dc9b8
pdf_path: papers/ReaxFF_others/Plummer_Anasori_Gogotsi_MXene_indentation_2019.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018plummer-computationa-nanoindentation-monolayer -->

## Summary

**MXenes**—**2D transition-metal carbides/nitrides**—are promising **solution-processable** conductors; **mechanical** properties depend on **composition**, **surface termination**, and **defects**. This work performs **ReaxFF-based simulated nanoindentation** in **LAMMPS** on **oxygen-terminated** **Ti₃C₂O₂** and **Ti₂CO₂** **monolayers**, extracting **Young’s moduli** from **force–displacement** curves for **pristine** sheets and sheets with **Ti** and **C vacancies**. **OVITO** visualizes **deformation** modes. The study positions **defect-containing** **MXenes** against **graphene oxide** benchmarks for **modulus** in **wet-chemistry** **2D** processing contexts. The **simulated** **indentation** workflow parallels **nanoindentation** interpretations used in **experiments**, enabling **direct** comparison to **mechanically** **tested** **MXene** **flakes** when **defect** populations are **documented**. **Compositional** **comparisons** between **Ti₃C₂O₂** and **Ti₂CO₂** illustrate how **MXene** **family** members can differ **sharply** in **stiffness**, motivating **property** maps that treat **termination** and **stoichiometry** as **first-class** variables alongside **defect** density.

## Methods
**1 — MD application (simulated nanoindentation).** **ReaxFF** (**Ti₃C₂Tₓ**-compatible parametrization cited in *Computational Materials Science*) is used in **LAMMPS** with **QEq-style** charge equilibration and documented nonbond cutoffs (see article). **PBC:** **periodic in-plane** **monolayer** cells of **oxygen-terminated Ti₃C₂O₂** and **Ti₂CO₂**; a **rigid spherical indenter (10 nm diameter)** advances at **10 m·s⁻¹** along the surface normal while recording **force–displacement** curves (**OVITO** visualization). **Ensemble:** **NVT** at **1 K** to suppress thermal noise during modulus extraction. **Timestep:** **0.25 fs**. **Defect models:** additional **Ti₃C₂O₂** cells include **~1 % Ti vacancies** and **~10 % C vacancies** simultaneously as in the abstract. **Duration / staging:** follow the staged **relaxation + indentation** protocol in the paper (exact **ps/ns** windows in **Methods**/**figures**). **Thermostat / temperature control:** the manuscript states the **temperature was maintained at 1 K** throughout indentation within the **canonical (NVT) ensemble** (see *Comput. Mater. Sci.* Methods for the corresponding LAMMPS controls). **Barostat / pressure:** **N/A —** **NVT** indentation without hydrostatic **NPT** barostat control. **Electric fields / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** applies a published **MXene** **ReaxFF** parametrization with **DFT** training heritage referenced in the article.

**3 — Static QM.** **N/A —** not a DFT-only study.

## Findings
**Outcomes:** reported **Young’s moduli** are **~466 GPa** (**pristine Ti₃C₂O₂**) and **~983 GPa** (**pristine Ti₂CO₂**); combined **Ti + C** vacancies reduce **Ti₃C₂O₂** to **~386 ± 31 GPa** in the quoted defective model.

**Comparisons:** defective **Ti₃C₂O₂** is compared to **graphene oxide** moduli cited for **solution-processed** **2D** materials.

**Sensitivity:** **composition** (**n+1,n** family member) and **vacancy loading** strongly shift stiffness extracted from **indentation** slopes.

**Limitations:** **1 K** sampling suppresses **thermal** effects; **rigid indenter** + **classical** **ReaxFF** omit explicit **electronic** plasticity.

**Corpus honesty:** moduli and defect percentages are taken from the **abstract** on `pdf_path`; verify against **Comput. Mater. Sci.** tables.

## Limitations

**1 K** indentation suppresses **thermal** **phonon** contributions; **rigid indenter** and **classical** **ReaxFF** omit **explicit** **electronic** **plasticity** and **charge transfer** beyond the model. **MXene** **terminations** beyond **O** are not exhaustively sampled here. **Young’s modulus** extraction from **indentation** **curves** depends on **contact** **radius** definitions and **elastic** **assumptions**—use the **article** **analysis** pipeline when **comparing** to **experiment**. **MXene** **literature** evolves quickly; treat **numerical** **moduli** as **illustrative** **ReaxFF** **predictions** unless **paired** with **experimental** **mechanical** **datasets** from the **same** **synthesis** **generation**. **Indentation** **rate** effects are **not** explored across **orders of magnitude** in the excerpted **protocol** summary shown on this wiki page alone.

## Relevance to group

Demonstrates **ReaxFF** **nanoindentation** protocols for **MXene** **mechanical screening** alongside **2D** **TMD** and **carbon** mechanics pages; useful when contrasting **solution-processable** **carbide** sheets with **oxide** **ceramic** **simulations** in the corpus.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2018.10.033](https://doi.org/10.1016/j.commatsci.2018.10.033) — `papers/ReaxFF_others/Plummer_Anasori_Gogotsi_MXene_indentation_2019.pdf`; extract `normalized/extracts/2018plummer-computationa-nanoindentation-monolayer_p1-2.txt`.

## Related topics

- [[reaxff-family]]
