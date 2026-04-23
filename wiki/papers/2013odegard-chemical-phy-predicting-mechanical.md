---
id: paper:2013odegard-chemical-phy-predicting-mechanical
type: paper
title: "Predicting mechanical response of crosslinked epoxy using ReaxFF"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - material:polymer-organic
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:validation-experiment
source_refs: []
doi: "10.1016/j.cplett.2013.11.036"
year: 2014
authors:
  - "Gregory M. Odegard"
  - "Benjamin D. Jensen"
  - "S. Gowtham"
  - "Jianyang Wu"
  - "Jianying He"
  - "Zhiliang Zhang"
venue: "Chemical Physics Letters"
pdf_sha256: "482745c20e057561b9bf4a1715368cf98efd596d228c6817777494c4097a1e91"
pdf_path: "papers/ReaxFF_others/Odegard Jensen epoxy paper.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013odegard-chemical-phy-predicting-mechanical -->

## Evidence and attribution

!!! note "Evidence"

    Prose below summarizes the **Chemical Physics Letters** article (**DOI `10.1016/j.cplett.2013.11.036`**, **2014** volume **591**, **175–178**). **`year`** in front matter follows the **publication** year (**2014**); the slug retains **2013** from ingest. A second PDF is `paper:2013odegard-chemical-phy-predicting-mechanical-2`.

## Summary

**ReaxFF MD** predicts **elastic stiffness** and **yield** for a **crosslinked epoxy** built from **EPON 862** and **DETDA**, comparing to **experimental** mechanical data on the same chemistry. Despite **strain-rate** gaps between **MD** and **experiment**, **elastic** and **yield** responses are reported to **align closely**, arguing that an **existing** hydrocarbon-style **ReaxFF** parameter set can be **repurposed** for **bulk epoxy** without a full refit (within the scope tested). The **Chem. Phys. Lett.** letter is explicitly a **proof-of-concept** that **reactive** **FFs** can bridge **network** **polymer** **mechanics** when **crosslink** **topology** is treated explicitly.

## Methods

**EPON 862** (**diglycidyl ether of bisphenol F**) and **DETDA** (**diethyltoluenediamine**) were modeled at **2:1** **EPON:DETDA** stoichiometry. **Five** independent crosslinked samples (**72** **EPON 862** + **36** **DETDA** per cell, **4284** atoms each) were built in **LAMMPS**: pre-reactive **monomer** variants were placed at **0.004 g cc\(^{-1}\)** and compressed to **~1.2 g cc\(^{-1}\)** at **300 K** over **4 ns** in **NVT** using the **OPLS-AA** force field, then **crosslinked** via **`fix bond/create`** with **7.0 Å** cutoff, reaching **~85%** crosslink density after **1 ns** **NVT**.

The networks were switched to **ReaxFF** (**Liu et al.** parameterization cited), warmed **0→300 K** over **100 ps** with **0.1 fs** timestep, then **NPT**-equilibrated **100 ps** at **300 K** (**Berendsen** barostat) to **~1.2 g cc\(^{-1}\)** average density. **Mechanical** loading simulations used **ReaxFF** to extract **elastic** properties and **yield** compared to **experimental** values on the same chemistry.

**Strain** **protocols**, **stress** **definitions**, and **replicate** **statistics** across the **five** **networks** are specified in **`papers/ReaxFF_others/Odegard Jensen epoxy paper.pdf`** alongside **experimental** **moduli**/**yield** **references**.

**Boundaries / periodicity:** **Three-dimensional PBC** **bulk** cells are implied by **crosslinked** **network** construction in **LAMMPS** (letter protocol). **Electric field / enhanced sampling:** **N/A —** not used for the quoted **mechanical** extraction workflow.

## Findings

**ReaxFF** **MD** predicts **elastic stiffness** and **yield** in **close agreement** with **measured** epoxy properties for this formulation. Despite large **strain-rate** separation between **simulation** and **experiment**, the letter argues the **elastic/yield** responses can be **correlated** across timescales using the authors’ analysis framework.

The **authors** position the **results** as motivating **reactive** **FF** **mechanics** for **thermosets** where **bond scission** may matter at **higher strain** than probed here.

**Sensitivity / design levers:** **Strain rate** in **MD** is orders of magnitude faster than **macroscopic** mechanical tests; the letter nevertheless argues **elastic** and **yield** responses can be **correlated** across timescales for this **formulation**.

**Corpus honesty:** Slug retains **2013** from ingest while **`year: 2014`** matches **Chem. Phys. Lett.** **591**, **175–178**; sibling PDF: **`[[2013odegard-chemical-phy-predicting-mechanical-2]]`**.

## Limitations

A dedicated **epoxy-specific** ReaxFF reparameterization would be ideal for new chemistries; results are for one **formulation** and loading mode.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Reader notes (navigation)

- [[reaxff-family]]
