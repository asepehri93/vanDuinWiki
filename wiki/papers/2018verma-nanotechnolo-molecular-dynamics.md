---
id: paper:2018verma-nanotechnolo-molecular-dynamics
type: paper
title: Molecular dynamics based simulations to study the fracture strength of monolayer
  graphene oxide
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:carbon-hydrocarbon
- domain:mechanics-tribology
- domain:reactive-md
- material:graphene-carbon-nano
- method:reaxff
- scale:atomistic
- task:application
paper_keywords:
- keyword:graphene-carbon
- keyword:reaxff-application
- keyword:lammps
- keyword:charge-equilibration
candidate_tags: []
source_refs: []
doi: 10.1088/1361-6528/aaa8bb
year: 2018
authors:
- Akarsh Verma
- Avinash Parashar
venue: Nanotechnology
pdf_sha256: 2f731c87e0125e9902ecd7c59bbdf40a035fac77b4c92f04db56f77794035845
pdf_path: papers/ReaxFF_others/Verma_2018_Nanotechnology_29_115706.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018verma-nanotechnolo-molecular-dynamics -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the Nanotechnology article identified by `doi`, `title`, and `pdf_path`.

## Summary

**Mode-I fracture toughness** of **monolayer graphene oxide (GO)** is estimated with **ReaxFF MD (LAMMPS)** using **Chenoweth**-type CHO parameters. Central **cracks** along **zigzag** vs **armchair** directions are studied with staged oxidation: **hydroxyl**, **epoxide**, and **carboxyl** groups separately, non-functionalized crack tips, and **combined** functionalization. **\(K_{IC}\)** is extracted from virial stress and crack geometry at the **first bond rupture**; results emphasize strong dependence on **coverage** and **spatial distribution** of oxygen groups.

## Methods

- **Engine / potential:** **LAMMPS** **ReaxFF** (Chenoweth et al. parameters cited); neighbor cutoff **4.5 Å**, hydrogen-bond cutoff **6 Å**; **QEq**-style charge updates **every 10** timesteps.
- **Geometry:** Monolayer sheet ~**270 × 270 Å** (~**27 468** atoms), **in-plane PBC**; central crack **2a = 2.7 nm** after convergence tests; sheet outer dimensions **~10×** crack length to mitigate finite-size effects.
- **Mechanical test:** Relax **12.5 ps** at **1 K** (**NPT**), then **uniaxial** tension along **x (ZZ)** or **y (AC)** at strain rate **10\(^{-3}\) ps\(^{-1}\)** with **NPT** (**zero** transverse stress); effective thickness **7.5 Å** (functionalized) vs **3.35 Å** (pristine) for stress intensity normalization.
- **Timestep:** **N/A — integration timestep in fs** is not recovered cleanly from the **Nanotechnology** PDF text extraction used here; confirm the value printed in the **Methods** of **`papers/ReaxFF_others/Verma_2018_Nanotechnology_29_115706.pdf`** (the relaxation and tensile segments above are stated in **ps**).
- **Thermostat / barostat:** **NPT** is used for relaxation and tensile loading with **zero** lateral stress as described in the article; the **PDF** body does not spell out a **thermostat** brand in the excerpted simulation paragraph—cite the issue text if a specific algorithm is required for reproduction.
- **Post-processing:** Virial stress formula in paper; **OVITO** for visualization.

- **Electric field / replica / metadynamics:** **N/A — not used** (mode-I tensile **NPT** fracture protocol only).
## Findings

- **Validation:** Pristine graphene **\(K_{IC}\)** (**~3.69** MPa·m\(^{1/2}\) ZZ; **~3.26** MPa·m\(^{1/2}\) AC) aligns with cited MD and experimental ranges.
- **Hydroxyl coverage:** Tabled **\(K_{IC}\)** decreases/increases with coverage and direction (e.g. **25–75%** OH examples in the paper); failure morphologies show **blunting**, **chain formation**, and **water** formation near crack tips at high strain.
- **Epoxide / carboxyl / combined:** Trends differ by group type and placement (detailed per §3); overall conclusion: **distribution and concentration** of functional groups **strongly** alter fracture response.

## Limitations

Single-temperature (**1 K**) fracture runs reduce thermal broadening but omit finite-temperature noise; ReaxFF uncertainty for oxidized carbon chemistry remains. **Crack-tip** chemistry can be sensitive to **water** and **environmental** **species** not included in the dry **GO** models discussed in the article. **Finite** **system** sizes and **periodic** **images** can also perturb **stress** fields near **cracks** compared to **macroscopic** **notch** tests. **Functional-group** **distributions** in **real** **GO** may be **spatially** **correlated** at scales larger than the **simulation** **cell** used for **fracture** **benchmarks**. **Nanotechnology** **tables** list **orientation-resolved** **toughness** metrics that should be cited when comparing to **other** **oxidized** **graphene** **studies**.

## Relevance to group

Mechanical **benchmark** for **oxidized graphene** using **ReaxFF** in **LAMMPS**—useful cross-reference for **defect** and **functionalization** effects on **carbon** **nanostructure** **toughness** in the broader corpus.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
