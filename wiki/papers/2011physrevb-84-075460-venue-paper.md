---
id: paper:2011physrevb-84-075460-venue-paper
type: paper
title: "Reparameterization of the REBO-CHO potential for graphene oxide molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:2d-layered, material:graphene-carbon-nano, method:classical-md, task:parameterization, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.84.075460"
year: 2011
authors: ["Fonseca, Alexandre F.", "Lee, Geunsik", "Borders, Tammie L.", "Zhang, Hengji", "Kemper, Travis W.", "Shan, Tzu-Ray", "Sinnott, Susan B.", "Cho, Kyeongjae"]
venue: "Physical Review B"
pdf_sha256: "c249f461a3e1484ee4c9756c350c34131b67f28864c0f6af8ddaf920f7a0c8af"
pdf_path: "papers/Others/PhysRevB.84.075460.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2011physrevb-84-075460-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **Physical Review B** article modifies the **second-generation REBO-CHO** reactive empirical bond-order potential (carbon/hydrogen/oxygen) to better describe **graphene oxide (GO)**. Using **DFT** as reference data, the parameterization optimizes terms governing **oxygen binding to graphene** and **C–O bond distances**, focusing changes on the **bond-order term** so prior REBO-CHO training for other uses is largely preserved. The introduction positions GO as technologically relevant (e.g., reduction routes to graphene, battery electrodes mentioned in context) and contrasts **REBO efficiency** with **ReaxFF/DFT** cost for large-scale GO simulations.

## Methods

This **Phys. Rev. B** article **reparameterizes** the **second-generation REBO-CHO** reactive bond-order potential (C/H/O) to better describe **graphene oxide (GO)**. The abstract states the strategy: use **density-functional theory (DFT)** reference data to **optimize** REBO-CHO, focusing changes on the **bond-order term** so prior REBO-CHO training for other targets is **largely preserved**. The introduction positions GO as technologically relevant (e.g. reduction routes to graphene, battery electrodes mentioned in passing) and contrasts **REBO efficiency** with **ReaxFF/DFT** cost for large-scale GO simulations.

**1 — MD application (benchmark MD using REBO-CHO).** The paper’s roadmap includes **classical MD** tests with the modified REBO-CHO on **GO samples** (sections referenced in the excerpt). **N/A —** MD **engine**, **ensemble**, **timestep**, **thermostat/barostat**, **temperature/pressure**, **system sizes**, and **PBC** are **not stated** in `normalized/extracts/2011physrevb-84-075460-venue-paper_p1-2.txt`—consult **`pdf_path`**.

**2 — Force-field training.** **Parent FF:** **second-generation REBO** lineage extended to **oxygen** (**Ni et al.** extension cited in the article header) forming **REBO-CHO**. **QM reference:** **DFT** supplies **oxygen binding energies to graphene** and **equilibrium C–O distances** used in the fit (abstract). **Optimization scope:** **bond-order term** modification is the explicit optimization lever. **Training / validation structures:** **GO** test systems are introduced in Sec. III in the PDF (not reproduced in the short extract). **N/A —** detailed **DFT functional**, **basis**, **k-mesh**, and optimizer weights are beyond the indexed excerpt.

**3 — Static QM / DFT.** **DFT** is the **reference** engine for energetics/structures feeding the reparameterization; full computational settings belong in the PDF Methods section.

**Checklist closure (indexed pages).** **Engine / code:** the article centers on **classical molecular dynamics** with **REBO-CHO**; **N/A — LAMMPS**/**GROMACS** package name not stated on pp. 1–2. **System / composition:** **GO** samples with **C/H/O** **stoichiometry** per Sec. III in the PDF; **atom** counts: **N/A —** not excerpted here. **Ensemble:** **N/A — NVT**/**NPT**/**NVE** not stated on pp. 1–2. **Duration / stages:** **N/A — equilibration**/**production** lengths for MD benchmarks not stated on pp. 1–2.

## Findings

**Problem statement.** Prior **REBO-CHO** is reported—via the authors’ preliminary tests cited in the introduction—to be **unsuitable** for **GO** as-is, motivating a targeted refit.

**Proposed remedy (abstract).** The authors claim the discrepancies can be addressed by **recalculating/modifying only the bond-order term**, preserving the rest of the REBO-CHO construction where it already worked.

**Planned comparisons (paper outline on indexed pages).** The manuscript compares **DFT vs REBO-CHO** for **oxygen binding energies**, **equilibrium C–O distances**, and **other GO properties**, then describes tests of the **modified** REBO-CHO (section roadmap summarized in the excerpt).

**Corpus honesty.** `extraction_quality` is **partial**; quantitative error tables and full GO test matrices are in **`pdf_path`**, not the pp. 1–2 extract.

**Mechanistic outcome (parameterization target).** The excerpt frames **oxygen** interactions with **graphene** (**binding energy**, **C–O distance**) as the key **reaction** quantities corrected by the **bond-order** refit—i.e., **oxidation**/**surface chemistry** behavior for **GO** models.

**Comparisons.** The paper is organized around **DFT vs REBO-CHO** comparisons for those **energies**/**distances** plus additional **GO properties** in later sections.

**Sensitivity / levers.** The abstract emphasizes that only the **bond-order** sector is refit so other REBO-CHO behaviors are preserved—an explicit **design lever** for transfer vs refit scope.

**Limitations / outlook.** **However**, REBO still lacks explicit **charge** dynamics compared with **ReaxFF**; the introduction flags efficiency tradeoffs that may limit chemistry captured for some **GO** states.

## Limitations

- This is **REBO**, not ReaxFF; transferability across oxygen chemistries and defects should be validated case-by-case.
- Extract is **partial**; quantitative error tables and full GO test cases are not captured in pages 1–2 alone.

## Relevance to group

Useful cross-reference for **reactive carbon–oxygen classical potentials** and GO modeling choices adjacent to ReaxFF-centric workflows.

## Citations and evidence anchors

- Title page and Secs. I–II introduction: motivation, REBO vs ReaxFF discussion, GO focus (Phys. Rev. B 84, 075460; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
