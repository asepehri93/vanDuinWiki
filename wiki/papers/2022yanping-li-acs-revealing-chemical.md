---
id: paper:2022yanping-li-acs-revealing-chemical
type: paper
title: "Revealing the Chemical Reaction Properties of a SiHCl3 Pyrolysis System by the ReaxFF Molecular Dynamics Method"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
  - domain:catalysis-surfaces
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acsomega.1c03998"
year: 2022
authors:
  - "Yanping Li"
  - "Dazhou Yan"
  - "Tao Yang"
  - "Guosheng Wen"
  - "Xin Yao"
venue: "ACS Omega 2022, 7, 3900–3916"
pdf_sha256: "8d0681e1d24179a0af4ff7035fae94027f429ba678f0ae7cbdb5fa616c929116"
pdf_path: "papers/ReaxFF_others/Li_SiClH_ACS_Omega_2022.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022yanping-li-acs-revealing-chemical -->

## Summary

Trichlorosilane pyrolysis underlies industrial polysilicon chemical vapor deposition, where gas-phase radical chemistry and silicon cluster growth pathways set precursor utilization and impurity incorporation. Industrial silane chemistry is complicated by parallel channels that also produce chlorosilane byproducts such as silicon tetrachloride and dichlorosilane, motivating mechanistic studies that go beyond a handful of pre-defined elementary steps. This *ACS Omega* article applies ReaxFF molecular dynamics to gas-phase SiHCl₃ decomposition between 1000 K and 2000 K, tracking temperature-dependent reaction networks, intermediate populations, and energy partitioning among vibrational, rotational, and chemical channels. The authors relate time evolution of partial energy contributions to the evolving distribution of intermediates over the simulated windows. The analysis emphasizes how low-temperature chemistry supports richer intermediate manifolds with larger silicon aggregates, whereas high-temperature chemistry simplifies pathways while increasing populations of small fragments such as SiHCl₂ and HCl. The abstract further notes that trichlorosilane can participate as a frequent participant in elementary events not only as a primary reactant but also as a product-like species once temperatures exceed about 1300 K, which erodes simple one-way decay pictures. The work positions atomistic reactive modeling as a complement to reactor engineering models that typically rely on reduced kinetics fit to bulk measurements.

## Methods

### Reactive force field (A)

- **Model:** **ReaxFF** for **Si/H/Cl** gas-phase chemistry appropriate to **SiHCl\(_3\)** **pyrolysis** (parameter lineage and validation references appear in *ACS Omega* **Methods**).

### High-temperature molecular dynamics (B)

- **Engine:** ReaxFF MD (typically **LAMMPS** in comparable studies—confirm in the PDF).
- **Systems:** **Periodic** or **cluster** cells as defined in the article, with initial conditions representing **SiHCl\(_3\)** (and evolving product) mixtures.
- **Temperature program:** **1000–2000 K** bracket where **bond-breaking** and **recombination** compete differently.
- **Sampling / analysis:** Time series of **species populations**, **silicon cluster** sizes, counts of **elementary events**, and **energy** partitioning among **vibrational**, **rotational**, and **chemical** channels (per article).
- **Numerics in the article:** **Cell** size/**density**, **timestep**, **ensemble**, **thermostat**, **ps**/**ns** **trajectory** length, and **Coulomb**/**QEq** settings for **1000–2000 K** **SiHCl\(_3\)** **pyrolysis** are in *ACS Omega* **Methods**/**SI**.

### MD application (gas-phase pyrolysis)

**Engine / code:** **ReaxFF** **RMD** (typically **LAMMPS**). **System:** **Si/H/Cl** **gas** **supercell** or cluster (periodic or finite as in the **paper**; **stoichiometry** and **atom** count as reported). **Temperature** program: **1000–2000 K** as specified. **N/A** — no **NPT** **barostat** or **hydrostatic** **pressure** path called out in this summary if runs are **constant-volume**; **N/A** — no **shock** or static **external electric field**; **N/A** — no **metadynamics** or **replica** **sampling** beyond the reported **MD**; **N/A** — no **continuum** **fluid** **dynamics** or **reactor** **wall** in the same **trajectory** set. **Ensemble**, **timestep (fs)**, and **duration** per **VOR**/**SI**.

## Findings

### Low vs high temperature networks

Below about **1300 K**, trajectories can build **large silicon-containing clusters** (**>5 Si**), including **polycyclic** motifs appearing **late** in time; **low-T** networks exhibit **more distinct intermediates** and **more elementary reaction events** than **high-T** networks under the authors’ protocols.

### High-temperature network topology

At higher temperatures, **smaller fragments** dominate and **interconversion** is faster; the **maximum Si count** carried by a single **molecule/radical** tends to be **larger** at **lower T** in their runs.

### SiHCl\(_3\) as reactant and “product-like” participant

Above ~**1300 K**, **SiHCl\(_3\)** appears both as a **primary reactant** and as a **frequently regenerated** species in the network, undermining **one-way** **decay** pictures.

### Modeling utility

The authors position the atomistic **reaction graph** as guidance for **reduced kinetics** in **chlorosilane/CVD** reactor modeling (outside full **fluid dynamics**, which is not simulated).

## Limitations

ReaxFF accuracy for chlorinated silane chemistry should be validated against quantum benchmarks cited in the paper; the simulations omit fluid dynamics, boundary layers, and surface chemistry present in real CVD reactors.

## Relevance to group

The study demonstrates ReaxFF pyrolysis network elucidation for silicon precursor chemistry, adjacent to semiconductor process and combustion-adjacent reactive modeling themes in the corpus.

## MAS / retrieval notes

For CVD or chlorosilane pyrolysis queries, anchor answers to the 1000–2000 K window and species-tracking methodology described in the article; caution that reactor fluid dynamics and surface chemistry are absent from the gas-phase MD model. Cross-link keyword facets `thermal-decomposition` and `reactive-md` when building chunk metadata.

## Citations and evidence anchors

- DOI: [10.1021/acsomega.1c03998](https://doi.org/10.1021/acsomega.1c03998)

## Related topics

- [[reaxff-family]]
