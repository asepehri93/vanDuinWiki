---
id: paper:2019h-s-huang-j-chem-phys-reaxff-reactive
type: paper
title: "ReaxFF reactive force field for molecular dynamics simulations of liquid Cu and Zr metals"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:alloys-metallurgy
  - method:reaxff
  - task:parameterization
  - task:validation
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:eam-potential
  - keyword:lammps
source_refs: []
doi: "10.1063/1.5112794"
year: 2019
authors:
  - "H. S. Huang"
  - "L. Q. Ai"
  - "A. C. T. van Duin"
  - "M. Chen"
  - "Y. J. Lü"
venue: "The Journal of Chemical Physics"
pdf_sha256: "00f0283c2dae54e2c43d73b057c1abc35c7c1831835720975adf0244d73e88da"
pdf_path: "papers/Huang_JCP_2019_CuZr_liquid.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019h-s-huang-j-chem-phys-reaxff-reactive -->

## Evidence and attribution

!!! note "Authority of statements"

    Training grids and validation metrics follow **J. Chem. Phys.** DOI `10.1063/1.5112794` and `normalized/extracts/2019h-s-huang-j-chem-phys-reaxff-reactive_p1-2.txt`.

## Summary

**Liquid metals** underpin **casting**, **fusion** materials, and **alloy** processing, yet **large-scale reactive MD** needs **accurate** yet **cheap** **interatomic models**. This paper develops a **ReaxFF** description for **Cu** and **Zr** **single-element** **liquids** and **crystals**, **fitting** to **VASP PAW-PBE** **equations of state** across **multiple crystal prototypes** (**fcc**, **bcc**, **hcp**, **a15**, **sc**, **dia**) and **low-index surface energies**. **Validation** spans **melting** (**liquid–crystal–liquid sandwich** simulations), **density**, **pair correlation functions**, **self-diffusion**, and **Voronoi** **local order** in **liquid** and **supercooled** regimes, compared to **experiment** and **EAM** references. The **work** is explicitly positioned as expanding **ReaxFF** **metallic** **capabilities** for **elemental** **liquids** where **EAM** may be **accurate** for **structures** yet less **flexible** when **bond-order**-like **effects** matter in **multicomponent** extensions. **For** **corpus** **navigation**, keep this paper linked near **alloy** **solidification** and **liquid-metal** **interface** topics even though the present **fit** is **pure** **Cu** and **Zr**.

## Methods

**DFT:** **PBE** **PAW**, **500–650 eV** cutoffs, **0.2 Å⁻¹** **k**-spacing, tight **SCF/force** tolerances, **15 Å** **slab vacuum**. **ReaxFF:** **bond + overcoordination + vdW** metal formulation with **bond-order** coupling; **least-squares** fit to **DFT** databases. **MD:** **AMS** **ReaxFF** integrator **0.25 fs**, **125 ps** windows; **EAM** baselines in **LAMMPS** (**1 fs**, **1 ns**) using literature **Cu** and **Zr** **EAM** files. **Melting:** **~4116**-atom **Cu** and **~4374**-atom **Zr** **sandwiches**, **NPT** **0 pressure**, **interface** velocity tracked.

**MD validation environments.** **Melting** and liquid benchmarks use **three-dimensional periodic** **supercells** with **~4116** **Cu** or **~4374** **Zr** **atoms** in **sandwich** geometries, **NPT** at **0 pressure** with a **Parrinello–Rahman**-class **barostat** as described in **JCP** (`pdf_path`). **AMS**/**ReaxFF** trajectories use **0.25 fs** **timestep** and **125 ps** windows; **LAMMPS** **EAM** comparisons use **1 fs** and **1 ns** **production**. **Thermostat:** **Nose–Hoover** (or equivalent) details accompany those engines in the article. **Temperature:** **thermal** ramps and **liquid**/**crystal** hold points in **K** follow the schedules tabulated in the article for each element. **External electric field:** **N/A**. **Enhanced sampling:** **N/A** for the quoted melting and **diffusion** benchmarks.

## Findings

**ReaxFF** reproduces **liquid** **g(r)**, **diffusion**, and **interface** behavior for **Cu** and **Zr** over the **temperature** ranges tested. **Melting temperatures** align **more closely** with **experiment** than the **selected EAM** potentials in the authors’ comparison, supporting use of **ReaxFF** for **liquid-metal** scenarios where **bond-order** flexibility matters. **Supercooled** **liquid** metrics and **Voronoi** **local order** further stress-test the **parameterization** beyond **melting** alone.

## Limitations

**Binary Cu–Zr** or **impurity** **chemistry** requires **additional** training data beyond this **elemental** set. **Liquid** **metal** **chemistry** involving **oxidation** is **not** the focus of this **benchmark**. **EAM** comparisons depend on **which** **EAM** **files** are chosen—authors cite **specific** **parameterizations** that may not represent the **latest** **experimental** **consensus** for **pure** **Cu**/**Zr** **melting**. **Archive** the **parameter** **file** **identifiers** used in **your** **LAMMPS** **scripts** when **reproducing** their **tables**.

## Relevance to group

**A. C. T. van Duin** co-authorship adds a **liquid-metal** **ReaxFF** **benchmark** complementary to **oxide** and **organic** lines in the corpus and supports **method** comparisons against **EAM** baselines in **LAMMPS** workflows.

## Citations and evidence anchors

- DOI `10.1063/1.5112794`; `papers/Huang_JCP_2019_CuZr_liquid.pdf`; extract `normalized/extracts/2019h-s-huang-j-chem-phys-reaxff-reactive_p1-2.txt`.

## Related topics

- [[reaxff-family]]
