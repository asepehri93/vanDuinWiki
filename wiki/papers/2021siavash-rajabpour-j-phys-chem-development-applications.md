---
id: paper:2021siavash-rajabpour-j-phys-chem-development-applications
type: paper
title: "Development and Applications of ReaxFF Reactive Force Fields for Group-III Gas-Phase Precursors and Surface Reactions with Graphene in Metal–Organic Chemical Vapor Deposition Synthesis"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - domain:2d-layered
  - material:graphene-carbon-nano
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:graphene-carbon
  - keyword:catalysis-surface
  - keyword:thermal-decomposition
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.1c01965"
year: 2021
authors:
  - "Siavash Rajabpour"
  - "Qian Mao"
  - "Nadire Nayir"
  - "Joshua A. Robinson"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "17bcdfb2f433040e3477bb59c639fd2ce14639b9b66561f2b679e844e95520da"
pdf_path: "papers/Rajadpour_JPC_C_2021_GaIn_graphene.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2021siavash-rajabpour-j-phys-chem-development-applications -->

## Summary

The work develops two ReaxFF parameterizations, **GaCH-2020** and **InCH-2020**, aimed at metal–organic chemical vapor deposition (MOCVD) scenarios: gas-phase chemistry of trimethylgallium (TMGa) and trimethylindium (TMIn), and interactions of those precursors with pristine and defective graphene. The motivation is scalable two-dimensional growth of group-III materials where fully quantum simulations are too small and short, whereas reactive large-scale MD is needed to capture precursor decomposition and cluster formation on carbon supports. The **J. Phys. Chem. C** article positions **Ga/In** **precursor** **chemistry** as a **bottleneck** for **interpretable** **2D** **growth** **models** that must span **gas-phase** **pyrolysis** and **surface** **attachment**.

## Methods

**1 — MD application.** **GaCH-2020** and **InCH-2020** are exercised in **LAMMPS** **molecular dynamics** to study (i) **TMGa** / **TMIn** **pyrolysis** in the gas **phase** and (ii) **nucleation** on **pristine** and **defective** **graphene** (monovacancy, **armchair** / **zigzag** edges, bilayer motifs) with **3D** **PBC** **slab**/**supercell** **models** and 10³+ **atoms** as in *J. Phys. Chem. C*. **NVT** trajectories with a **thermostat**, **timestep** in **fs**, and **ps**–**ns** **equilibration**/**production** are specified in the article; **temperature** ramp protocols **compare** high- and low-**T** **behaviors** for **precursor** **decomposition** and **cluster** **growth**. **N/A —** constant **Hydrostatic** **pressure** control in the **summarized** runs; **N/A — external** **electric** **field**; **N/A — umbrella** in the workflows highlighted here (standard **NVT** ReaxFF production).

**2 — Force-field training.** **ReaxFF** **forms** (Eq. (1)-style **bond/angle/…** decomposition) for **Ga/In/C/H** and **In/C/H** are **fit** to **DFT** **reference** **energies**, **geometries**, and **reaction** paths for **TMGa**/**TMIn** fragments, **decomposition** **channels**, and **graphene** **reactions**. **Parameter** **optimi**zation and **weighting** follow the group’s ReaxFF practice; **reaction** **lists** and **files** are in the **main** text / **SI**.

**3 — Experiments. N/A —** the published study is **computational** (plus literature context for **MOCVD**), not a new **laboratory** program.
## Findings

The parametrizations support mapping processing conditions under which TMGa/TMIn pyrolysis yields nanoclusters with low impurity content. On graphene, Ga-functionalized monovacancies can steer directional Ga cluster growth through covalent attachment. Under the growth conditions examined, Ga on armchair-edged graphene shows a higher growth ratio than In and can form a spread two-dimensional thin layer between graphene edges, whereas the comparison to In highlights system-dependent selectivity of cluster morphology and spreading.

The **authors** relate **edge** **symmetry** and **vacancy** **chemistry** to **anisotropic** **cluster** **spreading** trends that would be **opaque** in **purely** **continuum** **growth** **models**.

**Comparisons, sensitivity, corpus.** The paper **compares** **Ga** and **In** on **armchair** vs **zigzag** **substrates**; **temperature** and **precursor** **chemistry** set which **decomposition** paths dominate. All **kinetic** **numbers** belong to the **PDF**/**SI**, not this summary alone.

## Limitations

The investigation is framed around group-III metals on graphene; extending to full nitride MOCVD would require incorporating nitrogen chemistry and additional defect models beyond those treated here.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

Contributes ReaxFF development and large-scale reactive MD for III–V precursor chemistry interfacing with graphene, aligned with the group’s reactive MD and 2D materials work.

## Reader notes (navigation)

- [[reaxff-family]]
- [[graphene-nanocarbon]]
