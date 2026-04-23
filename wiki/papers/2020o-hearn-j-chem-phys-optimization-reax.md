---
id: paper:2020o-hearn-j-chem-phys-optimization-reax
type: paper
title: "Optimization of the Reax force field for the lithium-oxygen system using a high fidelity charge model"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:mechanics-tribology
  - domain:batteries-electrochemistry
  - method:reaxff
  - method:ereaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:charge-equilibration
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1063/5.0014406"
year: 2020
authors:
  - "Kurt A. O'Hearn"
  - "Michael W. Swift"
  - "Jialin Liu"
  - "Ilias Magoulas"
  - "Piotr Piecuch"
  - "Adri C. T. van Duin"
  - "H. Metin Aktulga"
  - "Yue Qi"
venue: "The Journal of Chemical Physics"
pdf_sha256: "aeea9b56cbe0872eda16377539c8fe0a7e2c43c2b60eb4573c7c849f1eff4878"
pdf_path: "papers/OHearn_JCP2020_Li2O_ACKS2_4archive.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020o-hearn-j-chem-phys-optimization-reax -->


**ACKS2-enabled ReaxFF** for **Li-O** is trained on **DFT**, **MRCI**, and **MRCI+Q** bond-breaking data with **genetic optimization**, then used in **LAMMPS** (ACKS2-enabled branch) for **Li2O** melt and **fracture** tests vs the **2016 QEq** ReaxFF parameterization.

## Summary

The paper targets unphysical partial charges during ionic bond cleavage in reactive MD by replacing EEM/QEq-style equilibration with **atom-condensed Kohn-Sham DFT to second order (ACKS2)** charge coupling inside ReaxFF. The new fit improves charge evolution along Li-O stretch dissociation and yields more realistic mechanical response than the 2016 QEq Li-O parameter set, yet **still does not reproduce full brittle fracture** in the slab tests shown.

## Methods

- **Reference data:** Training/validation sets include DFT and multireference **MRCI / MRCI+Q** dissociation curves for Li-O-containing motifs (detailed in the article).
- **Optimization:** **Genetic algorithm** (OGOLEM workflow as described) to optimize ReaxFF parameters against the quantum references.
- **MD engine:** **LAMMPS** with the authors' **ACKS2** branch for charge updates during MD.
- **Integration checks:** Bulk **Li2O** cubes relaxed in **NPT** at **0 pressure**, **300 K** (**40 ps** reported in one protocol block); **NVE** tests establish **0.25 fs** as the stable timestep (used consistently thereafter).
- **Fracture protocol:** Notched **Li2O** slabs equilibrated with **NPT**, then strained under **NVT** plane-strain loading at **300 K** (geometry and strain rate in article).

**1 — MD application (atomistic dynamics).** **Engine / code:** **LAMMPS** with the authors’ **ACKS2**-enabled **ReaxFF** branch. **System size & composition:** **Li₂O** **bulk** supercells (melt tests) and **notched** **fracture** **slab** supercells; atom counts and dimensions in the **PDF** (`pdf_path`). **Boundaries / periodicity:** **PBC** in **3D** for the bulk **melt**; the **fracture** **setup** uses the **in-plane** **PBC** and **free** **surfaces** normal to the **tensile** **axis** as in the article’s **figures**. **Ensemble:** **NVE** for **0.25 fs** **timestep** **stability** checks; **NPT** for **0**-pressure **equilibration** of **Li₂O** at **300 K** (**~40 ps** in one **protocol** line); **NVT** for **plane-strain** **fracture** at **300 K**. **Thermostat:** the published protocol specifies integrators/ensembles for 300 K **NPT** and **NVT** stages; copy **thermostat** type and **damping** from `pdf_path` when reproducing. **Barostat: N/A —** during the **NVT** **fracture** **segment**; **NPT** applies only in **melt** **preequilibration**. **Pressure: N/A —** explicit **stress** control in **NVE**; **0** **GPa** target in **NPT** **melt** **preequilibration**. **Electric field: N/A —** not used. **Shear / shock: N/A** as a driver beyond the **prescribed** **strain** protocol. **Replica / enhanced sampling: N/A —** not used.

**2 — Force-field training (ReaxFF + ACKS2).** **Parent FF / elements:** **ReaxFF** for **Li–O**, compared **head-to-head** to a **2016 QEq**-based **Li–O** parameter set. **QM reference:** **DFT** and **MRCI / MRCI+Q** **Li–O** **dissociation** and **reaction** data (code and **basis** / **active-space** details in the article and **SI**). **Training set:** **Bond-breaking** and **charge-response** **targets** along **Li–O** **coordinates** and related entries in the **fit** (per **article**). **Optimization:** **Genetic** **algorithm** in the **OGOLEM**-style **workflow** described in the text. **Reference data after fitting:** **Li₂O** **melt** and **fracture** **benchmarks** in **LAMMPS** to stress-test **QEq** vs **ACKS2** **on** the **same** **cells**.

## Findings

- **Outcomes & mechanisms:** **ACKS2 ReaxFF** reproduces training-set **charges** and **bond-breaking** trends substantially better than **2016 QEq** for the Li–O stretches highlighted; **NPT melt** of crystalline **Li2O** shows qualitatively different **amorphization**/**volume** response between ACKS2 vs 2016 QEq (including **RDF** signatures discussed in the paper).
- **Comparisons:** Head-to-head comparison against the **2016 QEq** parameterization on the same **Li2O** melt and **fracture** test cells frames where **charge fidelity** changes observables.
- **Sensitivity & design levers:** **Temperature** is fixed at **300 K** in the showcased melt/fracture benchmarks; strain rate and **slab** notch geometry enter the **fracture** phenomenology as reported in the article.
- **Limitations & outlook (as authored):** Fracture simulations still exhibit **residual ductile character** vs expected brittleness; charge fixes help but do not fully solve fracture phenomenology in the showcased setups—the article frames remaining gaps as motivation for further reactive-model development.
- **Corpus / KB honesty:** This page condenses **version-of-record**-style claims from `pdf_path` with **good** `extraction_quality`; line-level thermostat/barostat labels should be confirmed against the **PDF** if reproducing protocols exactly.

## Limitations

Accepted-manuscript PDF in corpus may differ slightly from final typesetting; fracture outcomes remain sensitive to classical reactive FF limits and simulation size/rate. **ACKS2** improves **charge response** along dissociation coordinates, but **brittle vs ductile** fracture remains a stringent test that can expose remaining **classical** limitations beyond charge models alone.

## Relevance to group

van Duin as co-author (parameterization lineage); MSU/Brown collaboration on charge fidelity for ionic ceramics. Pair with other **Li–O** / **solid electrolyte** parameterization notes when comparing **QEq** vs **ACKS2** charge pathways in reactive simulations.

## Reader notes (navigation)

- [[2020o-hearn-j-chem-phys-optimization-reax-2]] (proof duplicate PDF)
- [[reaxff-family]]
- Compare **LAMMPS** branch requirements for **ACKS2** charge updates when reproducing the fracture tests.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
