---
id: paper:2018yang-j-phys-chem-enabling-computational-2
type: paper
title: Enabling Computational Design of ZIFs Using ReaxFF
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:reaxff-lineage
- material:zeolite-porous
- method:reaxff
- task:application
- task:method-development
- scale:atomistic
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcb.8b08094
year: 2018
authors:
- Yongjian Yang
- Yun Kyung Shin
- Shichun Li
- Thomas D. Bennett
- Adri C. T. van Duin
- John C. Mauro
venue: J. Phys. Chem. B
pdf_sha256: 602cf1f2144e6c8bf9160f6a6fa1dafe01873ee7a2f6bdd5598975ea3b924bd7
pdf_path: papers/Yang_ZIF_JPC_B_2018_proof.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018yang-j-phys-chem-enabling-computational-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **J. Phys. Chem. B** article lays out a **ReaxFF-first modeling strategy** aimed at **computationally assisted design** of **zeolitic imidazolate frameworks (ZIFs)**, emphasizing **bond-making/breaking** events that matter during **processing**, **mechanical loading**, or **guest–framework** interactions that **fixed-bond** MOF-FFs may mishandle. **Coauthors** span **Penn State reactive simulation** (**Yang**, **Shin**, **van Duin**) and **glass / disordered framework** expertise (**Mauro**, **Bennett**), reflecting the paper’s **materials-informatics** angle on **ZIF** chemistry. The ingested file is an **ACS proof** PDF for the **JPCB** article. **ZIF** processing can involve **solvent** **evaporation**, **mechanical** **compaction**, or **defect** **annealing** steps where **lattice** **FFs** that freeze **topology** miss **failure** modes that **ReaxFF** can represent.

## Methods

### ReaxFF molecular dynamics (ZIF chemistry)

- **Force field / code:** ReaxFF parametrization for **Zn–Co–C–H–O–N** ZIF chemistry taken from **ref 38** in the article, implemented in **LAMMPS** (`normalized/extracts/2018yang-j-phys-chem-enabling-computational-2_p1-2.txt` confirms LAMMPS usage and **0.25 fs** integration).
- **Initial structures:** crystalline **ZIF-4**, **ZIF-62**, and **ZIF-77** configurations from the **Cambridge Structural Database (CSD)**; equilibrated at **10 K** with a **Berendsen** thermostat before heating sequences.
- **Thermal protocol (overview):** **ZIF-4** and **ZIF-62** are heated to **300 K** in **2.5 ps** under **NPT** with **Nosé–Hoover** thermostat/barostat, then ramped toward melting (**1500 K** within **12.5 ps** in the excerpted Methods paragraph). **ZIF-77** is heated from **10 K** to **900 K** at the same heating-rate convention stated in the article for that composition.
- **Glass formation (ZIF-4):** after high-temperature sampling, the **ZIF-4** melt is **quenched to 300 K** within **12.5 ps** in **NPT** to form an **a_gZIF-4** glass (timings from the Methods excerpt).

- **Boundaries / periodicity:** bulk **ZIF** crystals and melts use **three-dimensional periodic boundary conditions** (**PBC**) in **LAMMPS** on **CSD**-sourced cells, matching the **VOR** protocol on **`[[2018yang-j-phys-chem-enabling-computational]]`**.

### Validation and analysis

- Comparisons target **experimental** glass metrics and selected **first-principles MD** benchmarks where cited (see article for tables/figures); bond-order and coordination diagnostics are used to monitor **framework disordering**, **ligand decomposition**, and **melting** events.

- **Replica / metadynamics / applied E-field:** **N/A — not used** for the **ZIF** melt–quench **ReaxFF** workflows summarized here.
## Findings

- **ZIF-4 melt–quench:** ReaxFF reproduces key **structural signatures** of the **glassy** product (**a_gZIF-4**), including **density**, **thermal** response, and **pore morphology**, in strong agreement with **experiment** and **FPMD** references summarized in the abstract.
- **ZIF-62 melting:** simulations capture how **electronic vs steric** effects of the **benzimidazolate** substituent shift **melting temperature** relative to ZIF-4-like chemistry (abstract-level claim; see article for quantitative **T_m** discussion).
- **ZIF-77 (nitro-functionalized linker):** ReaxFF extrapolations suggest **electron-withdrawing −NO₂** motifs can **lower** **Zn–N**-linked melting trends, but the framework is prone to **oxidation/decomposition**, making it a **poor glass former** in practice—highlighting a **stability vs processability** trade-off for computational screening.
- **Take-home for design loops:** because ReaxFF captures **bond breaking/forming** during **high-temperature** and **disordered** ZIF states, it supports screening scenarios (glass formation, defect engineering, chemical resilience) that are **inaccessible** to nonreactive MOF force fields—at the cost of **parameterization specificity** to the trained chemistries.

## Limitations

- **MOF/ZIF** parameterization is **chemically specific**; **transfer** to new **linkers/metals** requires **re-fitting** or **validation**.
- **Proof PDF** pagination may differ slightly from the **final** issue page numbers.

**Curation note:** this slug registers **ACS proof** bytes per the **non-primary** catalog; for **stable** **bibliography** and **figure** numbering, prefer the **VOR** PDF from DOI `10.1021/acs.jpcb.8b08094` when available locally. **ZIF** **processing** simulations in the article should be read alongside **MOF-FF** **elastic** baselines when scoping **non-reactive** versus **reactive** **budgets**. **Penn State** **reactive** **simulation** authorship (**Yang**, **Shin**, **van Duin**) signals continuity with broader **MOF** **failure** studies in the corpus.

## Relevance to group

Foundational **ZIF + Reaxff** methodology paper in the **group’s porous framework** portfolio.

## Citations and evidence anchors

- **DOI:** [10.1021/acs.jpcb.8b08094](https://doi.org/10.1021/acs.jpcb.8b08094) (`papers/Yang_ZIF_JPC_B_2018_proof.pdf`).

## Reader notes (navigation)

- **Corpus catalog (proof PDF):** [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (entry **2018yang-j-phys-chem-enabling-computational-2**)

## Related topics

- [[reaxff-family]]
