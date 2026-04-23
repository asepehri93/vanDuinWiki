---
id: paper:2015rimsza-journal-of-n-molecular-dynamics
type: paper
title: "Molecular dynamics simulations of nanoporous organosilicate glasses using reactive force field (ReaxFF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - method:classical-md
  - material:silicate-glass
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:silica-silicate
  - keyword:npt-simulation
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1016/j.jnoncrysol.2015.04.031"
year: 2016
authors:
  - "J.M. Rimsza"
  - "Lu Deng"
  - "Jincheng Du"
venue: "Journal of Non-Crystalline Solids"
pdf_sha256: "a54fd6fe5b478baed6d6dd01ff6823aae131b7930f8b5d05d05c6161bc678b4f"
pdf_path: "papers/ReaxFF_others/Rimsza_J_NonCrystSolid_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015rimsza-journal-of-n-molecular-dynamics -->

!!! abstract "Year vs slug"
Wiki `id` keeps the **`2015rimsza-…`** slug; the journal assignment is **2016** (`year` above).

## Summary

Rimsza, Deng, and Du construct **nanoporous organosilicate glass (OSG)** models spanning **30–70% porosity** and multiple **pore morphologies**, motivated by **low-κ dielectric** applications where **organic–inorganic** bonding and **randomized porosity** complicate both experiment and simulation (*J. Non-Cryst. Solids*, DOI `10.1016/j.jnoncrysol.2015.04.031`). **Nanoporous silica** precursors are generated with **classical molecular dynamics** using **partial-charge pairwise potentials**, then functionalized by adding **hydroxyl** and **methyl** groups to **dangling bonds** and coordination defects. The hybrid OSG cells are **fully relaxed** with **ReaxFF** molecular dynamics (van Duin formulation cited in the article), after which structural metrics and an **elastic modulus** are extracted. The abstract reports that **Si–O** backbone **bond distances**, **angles**, and **Qₙ** distributions remain **silica-like** after ReaxFF relaxation, that **methyl** geometries remain consistent with **FTIR-informed** expectations, and that **Young’s modulus** falls in **24–31 GPa** at **30%** porosity and **0.5–2.5 GPa** at **70%** porosity—trends described as consistent with prior **experimental** work.

## Methods

The workflow is explicitly **multistep** in the abstract: **nanoporous silica** precursors are built with **classical molecular dynamics** using **partial-charge pairwise (Buckingham-type) potentials** and **randomized** porosity motifs rather than perfectly ordered spherical pores alone, in line with prior nanoporous-silica work cited in the paper. **Hydroxyl** and **methyl** groups are then added to **dangling bonds** and coordination defects to form **organosilicate glass (OSG)** stoichiometries spanning **30–70%** porosity. The hybrid networks are **fully relaxed** with **ReaxFF** MD using the **van Duin** formulation referenced in the article, after which structural metrics and **elastic moduli** are computed (stress–strain or equivalent strained-MD protocol as defined in **Computational methods** on `pdf_path`).

The indexed opening pages do **not** name the classical MD program or list **timestep**, **thermostat**, **NPT** vs **NVT** staging, or trajectory **durations**; those values appear only in the full Methods tables on `pdf_path`. **Temperature:** thermalization and **production** **temperature** targets (**K**) for classical and ReaxFF stages are tabulated on `pdf_path`. **Duration:** **equilibration** and **production** segment lengths (**ps**/**ns**) for each stage appear there as well. **Boundaries:** **3D periodic** supercells as defined in the article. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**.

**Force-field training:** **N/A** — the publication **applies** an established **ReaxFF** parameterization for **Si/O/C/H** organosilicate chemistry; it does not report a new global refit in the abstract framing.

**Static QM / DFT:** **N/A** — **DFT** is not the headline workflow in the abstract; the study is classical + ReaxFF MD.

## Findings

**Structural fidelity:** After ReaxFF relaxation, **bond distances and angles** and **Qₙ** statistics for the **silicate backbone** align with expectations for **dense amorphous silica**, while **methyl** bonding geometries remain consistent with **experimental FTIR** constraints discussed in the introduction (abstract + introduction themes).

**Mechanical trends:** **Young’s modulus** values near **24–31 GPa** (**30%** porosity) and **0.5–2.5 GPa** (**70%** porosity) bracket a wide mechanical range and match previously reported **experimental** scaling for comparable porosity (abstract).

**Design levers:** **Porosity level** and **pore morphology** strongly modulate modulus; **organic termination** chemistry is part of how the models depart from pure nanoporous silica (article discussion).

**Limitations (authored context):** The abstract positions the work as a pragmatic route to **OSG** models where **network connectivity** and **organic content** matter; **CVD** microstructure variability remains only partially captured by simulated **randomized** porosity.

## Limitations

Porosity **morphology** is simulated, not identical to manufacturing **CVD** microstructures. **ReaxFF** accuracy depends on training coverage for **organosilicate** chemistry beyond the cases benchmarked in the article.

## Relevance to group

Demonstrates **ReaxFF relaxation** of **hybrid organic–inorganic dielectric** nanoporous silica models—adjacent to broader **oxide / interface** simulation themes.

## Citations and evidence anchors

DOI `10.1016/j.jnoncrysol.2015.04.031`; opening abstract: `normalized/extracts/2015rimsza-journal-of-n-molecular-dynamics_p1-2.txt`.

## Related topics

- [[reaxff-family]]
