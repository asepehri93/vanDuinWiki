---
id: paper:2021akbarian-j-chem-phys-atomistic-scale-insight-2
type: paper
title: "Atomistic-scale insight into the polyethylene electrical breakdown: An eReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:ereaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:dft-static
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1063/5.0033645"
year: 2021
authors:
  - "Dooman Akbarian"
  - "Karthik Ganeshan"
  - "W. H. Hunter Woodward"
  - "Jonathan Moore"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys."
pdf_sha256: "45c1ceaed8d8c33345cde35deddfa81ccd388cf97ee4a7560be27816faf2f7eb"
pdf_path: "papers/Akbarian_JCP_2020_eReaxFF_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021akbarian-j-chem-phys-atomistic-scale-insight-2 -->

## Summary

Cross-linked **polyethylene (XLPE)** is a common **high-voltage** insulator; residual **by-products** from **peroxide curing** may alter **dielectric** reliability. This study uses an **eReaxFF**-based **MD** framework—**explicit electrons** included and **verified against DFT**—to relate **mass density**, **void** content, and **acetophenone**-class additives to **time-dependent dielectric breakdown (TDDB)**. **eReaxFF MD** with explicit electronic variables probes how XLPE by-products (e.g. **acetophenone**), packing density, and void connectivity steer failure times. Simulations report that **higher PE density** increases **TDDB**, whereas **additives with positive electron affinity** such as **acetophenone** can **shorten** **TDDB**. During **breakdown**, **electrons** preferentially **traverse voids** between **electrodes**. The **acetophenone radical anion** markedly **reduces** **reaction barriers** and **exothermicities** of **secondary** reactions compared with **neutral acetophenone**, which the authors connect to accelerated chemical damage pathways alongside electronic transport.

## Methods

### A — Force-field training / fitting (ReaxFF and related)

- **Not stated in this wiki note:** the prior draft did not isolate **force-field** training text here; see **§B–C** and the primary PDF for **ReaxFF** lineage, training sets, and **QM** references used in fitting.

### B — Molecular dynamics, experiments, protocols, and sampling

**Systems:** **Polyethylene** models spanning **density** and **void** distributions; **acetophenone** and derived **radical anion** chemistries as stated in the article, with microstructures chosen to mimic void channels between electrodes.

**MD:** **eReaxFF** **reactive MD** with **inter-electrode** **electric** **field** / **bias** protocols for **TDDB**; **N/A** here to paste full **LAMMPS** input—see **JCP**/**pdf_path** for **3D** **PBC** **PE** **supercells** (stoichiometry and **atom** **count** per case), **NVT**/**NVE** (and **NPT**/**1** **bar** isotropic **pressure** **control** if used), **fs** **timestep**, **K** **temperature** setpoints, **ps**/**ns** **duration**, **Nose**–**Hoover**-class **thermostat**, and how **breakdown** events are detected. **Umbrella** / **metadynamics**—**N/A** unless **SI** states otherwise.

### C — Electronic structure / static QM (when reported separately from MD)

**Model:** **eReaxFF** (extended ReaxFF class treating **electronic** degrees of freedom within the parametrization used here) with **DFT** validation for key **electron attachment** and **reaction energetics**, including checks on species relevant to peroxide-cure residuals.

### D — Review scope, SI/galley notes, and non-primary corpus roles

- **Not applicable:** primary research article unless the **Summary** flags a **review**, **SI-only** register, or **duplicate** PDF (see **Reader notes** / **Limitations**).

## Findings

**Density** and **void** microstructure strongly modulate **breakdown times**. **By-product** species with favorable **electron affinity** can **accelerate** failure. **Void-connected** paths dominate **inter-electrode** **electron** migration in the modeled **breakdown** scenarios. **Radical anions** shift **secondary reaction** kinetics relative to **neutral** precursors, supporting a picture in which both electronic pathway availability and follow-on bond-making chemistry control TDDB trends. **Comparisons** in the **JCP** text pair **eReaxFF** with **DFT** for key **energetics**. **Sensitivity** of **TDDB** to **density**, **voids**, and **additives** (e.g. **acetophenone**) is a main theme. **Limitations** on **engineering** **extrapolation** are **authored** in the **article** and below; **citable** **values** and **protocol** **tables** must be taken from the **VOR** **pdf_path** (this page is a **corpus** **summary** only).

## Limitations

**eReaxFF** approximates **electronic** effects; quantitative **TDDB** lifetimes must be mapped carefully to **engineering** voltage/temperature conditions. Finite cells and short segments capture initiation chemistry more reliably than full device-scale breakdown statistics, so extrapolation to AC waveforms or broad temperature ramps should be treated as qualitative guidance pending targeted validation against experiment or higher-level electronic-structure methods on representative fragments. For **peer-reviewed** **pagination** and **figure** labels, prefer the **JCP** **online** PDF referenced in the bibliography rather than any local proof artifacts if both appear in a workspace.

## Relevance to group

Demonstrates **eReaxFF** for **dielectric breakdown** in **hydrocarbon polymers** with **industrial** (cable) relevance.

## Citations and evidence anchors

- DOI: [10.1063/5.0033645](https://doi.org/10.1063/5.0033645)

## Reader notes (navigation)

- eReaxFF / explicit-electron lineage: [[reaxff-family]]; polymer dielectrics cluster with [[2018vashisth-polymer-158-effect-chemical]].

## Related topics

- [[reaxff-family]]
