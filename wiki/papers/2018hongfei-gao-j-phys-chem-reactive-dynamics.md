---
id: paper:2018hongfei-gao-j-phys-chem-reactive-dynamics
type: paper
title: "Reactive dynamics simulation study on the pyrolysis of polymer precursors to generate amorphous silicon oxycarbide structures"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - material:silicate-glass
  - scale:atomistic
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:nvt-simulation
  - keyword:silica-silicate
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.7b12287"
year: 2018
authors:
  - "Hongfei Gao"
  - "Hongjie Wang"
  - "Zihao Zhao"
  - "Min Niu"
  - "Lei Su"
  - "Yin Wei"
venue: "J. Phys. Chem. C"
pdf_sha256: "2617568f37032b74476d47ea0e11ad23536877b8a36d19f39ef1e6233db0791e"
pdf_path: "papers/ReaxFF_others/Gao_SiCOH_JPC_C_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018hongfei-gao-j-phys-chem-reactive-dynamics -->

## Summary

**Silicon oxycarbide (SiOC)** glasses combine **oxidic** and **carbidic** bonding in amorphous networks attractive for high-temperature materials, often synthesized by **pyrolyzing** **silicon-containing polymers** such as **polymethylhydrosiloxane (PMHS)** and **hyperbranched polycarbosilane (HPCS)**. This **Journal of Physical Chemistry C** article uses **ReaxFF reactive molecular dynamics** to pyrolyze mixed **PMHS + HPCS** models toward a **dense amorphous SiOC** solid. A practical challenge is mimicking **mass loss** on simulation timescales; the authors apply a **shell script** to remove dominant gas molecules (**H\(_2\)**, **CH\(_4\)**) during **NVT** segments to approximate experimental outgassing, then **compress** and **equilibrate** the residual solid. **Radial distribution functions (RDFs)** are used to compare **Si–O**, **Si–C**, **C–C**, and **Si–Si** correlations against experimental constraints cited in the paper.

## Methods

**Software / interactions:** **Reactive molecular dynamics** with **ReaxFF** (**C/Si/H/O**) in **LAMMPS**; Section 2 documents **Gaussian** checks of selected **Si–C/O** bond and angle **energies** against **quantum chemistry** references.

**System and boundaries:** Initial models combine **PMHS** + **HPCS** polymer backbones in **3D PBC** **supercells** whose **atom** totals and box sizes follow Section 2 / **Table 1** of the **JPCC** **PDF**.

**Protocol:** Pyrolysis stages use **NVT** **MD** with **thermostat** settings, integration **timestep** (fractional **fs**), and **equilibration**/**production** **run** lengths in **ps** reported in Section 2 of the **JPCC** **PDF**; the abstract notes **NVT-MD** segments coupled to a script that deletes dominant **H\(_2\)** and **CH\(_4\)** to mimic experimental mass loss. **Compression** plus room-**temperature** relaxation yields dense **amorphous SiOC**; **RDF** analysis quantifies short- and medium-range order. **N/A — NPT barostat** and **N/A — imposed hydrostatic pressure** during the quoted **NVT** pyrolysis windows.

## Findings

**Outcomes & mechanisms:** **H\(_2\)** and **CH\(_4\)** dominate **gas** products under the **NVT** + scripted **removal** protocol; **decomposition** and **bond redistribution** lead to a **dense amorphous SiOC** network after **compression** and **relaxation**.

**Comparisons:** **radial distribution functions** for **Si–O**, **Si–C**, **C–C**, and **Si–Si** correlations are reported to **agree** with **experimental** constraints summarized in the article (operators should verify peak positions against **Figures** in **`pdf_path`**).

**Sensitivity:** final **oxygen** balance and **carbon** partitioning depend on how aggressively **CH\(_4\)**/**H\(_2\)** are **deleted** and on the **heating** schedule—**reproduction** requires copying the **script** logic from **Sec. 2** / **SI**, not only the **ReaxFF** file.

**Limitations / outlook:** **ReaxFF** **accuracy** and **short** **simulation** timescales relative to furnace **pyrolysis**; **periodic** cells omit **open** **boundary** **outgassing** except via the **heuristic** deletion scheme.

**Corpus honesty:** **timestep**/**thermostat** numbers must be taken from the **full PDF** if absent above; this page is **not** a substitute for **Sec. 2** tables.

## Limitations

**Empirical ReaxFF** accuracy; simulation timescales remain far shorter than industrial pyrolysis; **gas deletion** is a modeling artifact requiring sensitivity analysis.

## Reader notes (MAS / retrieval)

Use for **SiOC** **pyrolysis** questions mentioning **PMHS/HPCS** mixtures and **RDF** validation against experiments.

## Relevance to group

**Polymer-derived SiOC** **ReaxFF** workflow comparable to **silica/silicate** ceramic formation studies elsewhere in the corpus.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpcc.7b12287`.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
