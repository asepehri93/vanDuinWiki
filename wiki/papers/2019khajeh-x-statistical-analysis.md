---
id: paper:2019khajeh-x-statistical-analysis
type: paper
title: "Statistical Analysis of Tri-Cresyl Phosphate Conversion on an Iron Oxide Surface Using Reactive Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - method:reaxff
  - task:application
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:lammps
  - keyword:tribology
source_refs: []
doi: "10.1021/acs.jpcc.9b02394"
year: 2019
authors:
  - "Arash Khajeh"
  - "Xiaoli Hu"
  - "Karen Mohammadtabar"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "Stephen Berkebile"
  - "Ashlie Martini"
venue: "The Journal of Physical Chemistry C (proof PDF)"
pdf_sha256: "7577ee32ad5d1a633e4c4e5222aefcdf08eb8f65d6b93b3608a63445fdc4fdbc"
pdf_path: "papers/Khajeh_FeO_Phosphate_JPCC_2019_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019khajeh-x-statistical-analysis -->

!!! note "Corpus PDF role"
    This slug tracks an **author proof** PDF (`Khajeh_FeO_Phosphate_JPCC_2019_proof.pdf`). The **typeset journal PDF** and aligned curation live under **[[2019khajeh-j-phys-chem-statistical-analysis]]**; scientific statements below match that work.

## Summary

Aviation lubricant chemistry motivates reactive modeling of **tri-cresyl phosphate (TCP)** on **iron oxide** surfaces under conditions relevant to **film-forming** contacts. The study develops **ReaxFF** parameters for **Fe/P/O** chemistry against **DFT** reference data for **Fe–O–P** bonding, **P/PO** adsorption on iron facets, and related dissociation and angle energetics, then applies the field in **large-scale** **LAMMPS** sampling. Rather than a single short trajectory, the authors launch **100 parallel replicas** with one TCP molecule per cell on a **passivated amorphous iron oxide** substrate, exploring **chemisorption regioisomers** across a **temperature ladder** from **300 K to 700 K**. The central output is **site-resolved statistics** for which TCP atoms form **load-bearing** hetero-bonds to the surface—especially **Fe–C** versus **P=O oxygen** contacts—and how those preferences shift with temperature, contextualized against experimental observations of TCP-derived films in **oxygen-poor** tribological environments.

## Methods

**Force-field training (2).** **ReaxFF** for **Fe/P/O** and **TCP**–**oxide** chemisorption, fit to **DFT** for **Fe–O–P** geometry/energy, **Fe–P** dissociation, **Fe(II)/Fe(III)–O–P** bending, and **P/PO** on **Fe** facets; **ReaxFF** vs **DFT** in the manuscript; parameters in **SI**. **Substrate:** one **passivated amorphous** **iron oxide** slab.

**MD application (1).** **Engine:** **LAMMPS**; **0.25 fs** timestep; **bond order** every **1.25 ps** (cutoff **0.3**). **System:** one **TCP** and one **oxide** slab; **100** replicas (**50** **P=O**-down, **50** **P=O**-up). **Ensemble:** **NVT**; **Nose–Hoover thermostat** on **non-fixed** atoms. **PBC** and fixed **substrate** treatment as in **[[2019khajeh-j-phys-chem-statistical-analysis]]** / **PDF**. **Barostat / servocontrol of pressure:** **N/A** — **NVT**. **Temperature:** **300–700 K** in **100 K** steps, **~1 ns**/stage to plateau; **last ~25 ps** averaged. **Electric field:** **N/A**. **Umbrella / metadynamics / replica exchange:** **N/A** — **parallel** **independent** trajectories only.

**DFT (3).** **Training** **DFT** only; not a static **QM** **application** paper.
## Findings

Among tracked **hetero-bonds** (with **hydrogen-mediated** contacts treated as non-load-bearing for the film-growth metrics), **Fe–C** bonding is the **most probable** contact class, supporting a picture in which **aryl** carbons anchor TCP-derived fragments to the **ferrous** interface. **Overall** TCP–surface bonding **increases** with temperature over the sampled window, but the **dominant reaction sites reorganize**: **aryl C5/C6** positions are favored at **lower** temperatures, whereas **700 K** statistics shift probability toward **P=O** **oxygen** atoms. The **replica ensemble** is essential: **single** short runs cannot explore the **regioisomer** distribution accessible to TCP on a disordered oxide, so the parallel strategy yields **histogram-level** insight that would be invisible from one trajectory alone.

## Limitations

The oxide morphology is a **single** **disordered** realization; **shear**, **load cycling**, and **multi-molecule** crowding typical of full **tribological** contacts are not simulated. **Proof-PDF** pagination may differ slightly from the **version-of-record** PDF on **[[2019khajeh-j-phys-chem-statistical-analysis]]** for locators and figure numbering.

## Reader notes (navigation)

- Version-of-record PDF page: **[[2019khajeh-j-phys-chem-statistical-analysis]]**
- [[reaxff-family]]
