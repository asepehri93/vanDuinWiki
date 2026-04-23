---
id: paper:20210000-0002-1686-065x-x-development-applications
type: paper
title: "Development and Applications of ReaxFF Reactive Force Fields for Group-III Gas-Phase Precursors and Surface Reactions with Graphene in MOCVD Synthesis"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:galley-or-proof-pdf
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
pdf_sha256: "f2f70626d4a1dc4606d3968846dce3582a8eb4a063306fecff394c36d3167a77"
pdf_path: "papers/Rajadpour_JPC_C_2021_GaIn_graphene_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20210000-0002-1686-065x-x-development-applications -->

This JPCC study introduces two ReaxFF parameter sets, GaCH-2020 and InCH-2020, for trimethylgallium and trimethylindium chemistry in metal–organic chemical vapor deposition (MOCVD) scenarios, including gas-phase decomposition and interactions with graphene substrates.

## Summary

GaCH-2020 and InCH-2020 extend the ReaxFF bond-order framework to Ga–C/H and In–C/H organometallic chemistry together with graphene surface reactions so that reactive molecular dynamics can probe MOCVD-like thermal decomposition of TMGa and TMIn toward Ga- and In-rich nanoclusters with low carbonaceous impurity content. The authors apply the new potentials to map how processing conditions affect cluster purity from precursor pyrolysis and to survey cluster formation on graphene that contains vacancies and zigzag versus armchair edge terminations. They report that graphene with Ga-functionalized monovacancies can template directional Ga cluster growth through covalent pathways, and that under selected growth conditions Ga on armchair-edged bilayer graphene not only grows faster than In but can spread into a thin two-dimensional layer between edges.

## Methods

**1 — MD application.** **ReaxFF** **reactive MD** (standard **LAMMPS**-compatible implementation in the JPCC article) covers **gas-phase** **TMGa** and **TMIn** **pyrolysis** and **graphene**-supported **deposition** on **pristine**, **monovacancy**, and **edge**-terminated **(zigzag** vs **armchair)** **sheets**, including **bilayer** **armchair** **geometries** where discussed. **3D** **PBC** **supercells**; **NVT** **heating** and **isothermal** **stages**; sub-**1** **fs** **timestep**; **Nose–Hoover**-type **thermostat**; **NPT** **only** if the **article** **pressurizes** **vapor** **cells** (see **VOR**—**N/A** here to quote **bar** **values**). **Duration:** **ps**-scale and longer **equilibration** and **production** segments per the JPCC **Methods** (exact **ns** spans in the **VOR**/**SI**). **Temperature** in K for ramped and held stages drives **pyrolysis** and **coalescence**. **Electric** **field**; **replica** **/ enhanced** **sampling** — **N/A** in the summarized **protocol** scope.

**2 — Force-field training.** **GaCH-2020** and **InCH-2020** **parameter** **sets** add **Ga**/**In**–**C**/**H** + **graphene**-**C** **interactions**; **EEM** **charges**; **QM** **reference** set for **organo**-**Group-III** **+** **carbon** (training **data** and **ReaxFF** **optimization** workflow in **Methods/SI**).

**3 — Static QM.** **DFT** data underpinning the fit are summarized in the main **J. Phys. Chem. C** paper; **N/A** as a pure **DFT**-only study.

**4 — Galley.** The registered **pdf_path** is a **galley**—confirm **table** and **run** **parameters** against the **VOR** **file**.

## Findings

**Pyrolysis and purity:** **Thermal** and **compositional** **windows** are identified in which **Ga**/**In** **clusters** form with **low** **carbon-rich** **byproduct** **content** relative to less selective **channels**. **Graphene**-**templated** **morphology:** **Ga** **covalent** **attachment** at **monovacancy** **sites** supports **anisotropic** **Ga** **growth** vs. more **isotropic** **nucleation** on **clean** **basin** **areas**. On **armchair-edged bilayer graphene**, the authors report **faster** **Ga** **accumulation** than **In** and, under selected conditions, a **spread-out** two-dimensional **Ga** sheet between edge boundaries. **Comparisons** are intra-study (Ga vs In, edge vs vacancy). **Limitations:** nitride-containing (NH\(_3\), N-doped) CVD is explicitly excluded from the parametrization scope; the ingested corpus PDF is a **galley** (see **## Limitations**).

## Limitations

Group-III nitride chemistry is not included; the authors note that extending the model with nitrogen-containing training data is a natural next step. The ingested corpus PDF is an ACS galley; final pagination and minor editorial details should be checked against the version of record.

## Relevance to group

The work links Penn State ReaxFF development to III–V precursor chemistry and graphene-templated growth, complementing nitride and transition-metal dichalcogenide studies elsewhere in the knowledge base.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.1c01965](https://doi.org/10.1021/acs.jpcc.1c01965)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]

## Reader notes (navigation)

- `paper_keywords` includes **`keyword:galley-or-proof-pdf`**.
