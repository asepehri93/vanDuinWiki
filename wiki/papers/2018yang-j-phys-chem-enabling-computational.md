---
id: paper:2018yang-j-phys-chem-enabling-computational
type: paper
title: Enabling Computational Design of ZIFs Using ReaxFF
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:methods-software
- material:zeolite-porous
- method:reaxff
- task:application
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
venue: J. Phys. Chem. B 2018, 122, 9616–9624
pdf_sha256: 19f06853f13174da01e0dad19f8f1da2975be5428325fa389bb1e9ad13428435
pdf_path: papers/Yang_ZIF_JPC_B_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018yang-j-phys-chem-enabling-computational -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Zeolitic imidazolate frameworks (ZIFs) increasingly require simulations that handle **bond breaking/forming** (melts, defects, chemical stability), beyond classical nonreactive FF applications. This paper demonstrates ReaxFF on representative ZIFs: melt–quench of ZIF-4 reproduces glassy **aZIF-4** structure, density, thermal response, and pore morphology consistent with experiment and ab initio MD; ZIF-62 melting highlights ligand chemistry (benzimidazolate) effects on melting trends; ZIF-77 with electron-withdrawing substituents illustrates how electronic/steric balance shifts predicted melting and chemical stability. The overarching claim is that ReaxFF’s cost and transferability can support computational screening of disordered and defect-laden ZIF behavior.

ZIF glasses are challenging for fixed-bond force fields because linker scission and metal–linker reorganization accompany vitrification.

## Methods

### ReaxFF molecular dynamics (ZIF chemistry)

- **Force field / code:** ReaxFF parametrization for **Zn–Co–C–H–O–N** ZIF chemistry from **ref 38** in the article, implemented in **LAMMPS**; **0.25 fs** timestep (`normalized/extracts/2018yang-j-phys-chem-enabling-computational_p1-2.txt` and the parallel proof-ingest extract for [[2018yang-j-phys-chem-enabling-computational-2]] align on LAMMPS usage).
- **Initial structures:** crystalline **ZIF-4**, **ZIF-62**, and **ZIF-77** from the **CSD**; equilibrated at **10 K** with a **Berendsen** thermostat before heating.
- **Thermal protocol (overview):** **ZIF-4** and **ZIF-62** are heated to **300 K** in **2.5 ps** under **NPT** (**Nosé–Hoover** thermostat/barostat), then ramped toward melting (**1500 K** within **12.5 ps** per Methods). **ZIF-77** is heated from **10 K** to **900 K** at the rate stated for that composition.
- **Glass formation (ZIF-4):** the **ZIF-4** melt is **quenched to 300 K** within **12.5 ps** in **NPT** to obtain **a_gZIF-4** glass.

- **Boundaries / periodicity:** bulk **ZIF** crystals and their high-temperature melts are simulated in **three-dimensional periodic** supercells with **LAMMPS** (**PBC** on the **CSD**-derived unit cells, as standard for framework **MD**).

### Validation and analysis

- Comparisons target **experimental** glass metrics and **FPMD** benchmarks where cited; bond-order/coordination diagnostics track **framework disordering**, **ligand chemistry**, and **melting**.

- **Replica / metadynamics / applied E-field:** **N/A — not used** in the **ZIF** melt–quench **ReaxFF** protocols summarized above.
## Findings

- **ZIF-4 melt–quench:** ReaxFF reproduces **structure**, **density**, **thermal** properties, and **pore morphology** of **a_gZIF-4** in strong agreement with **experiment** and **FPMD** (abstract-level summary; see article for quantitative tables).
- **ZIF-62:** **benzimidazolate** substitution shifts **melting** trends through the balance of **electronic** and **steric** effects noted in the abstract.
- **ZIF-77:** **−NO₂** substituents can **lower** **Zn–N**-linked melting trends in the ReaxFF picture, but the framework tends toward **oxidation/decomposition**, so it is a **poor glass former**—illustrating a **stability vs processability** trade-off.
- **Broader point:** reactive MD fills a gap where **AIMD** is costly but **nonreactive** MOF force fields cannot represent **bond rearrangement** during **melts**, **defects**, or **chemical** failure—supporting **screening** narratives in the article.

Pair this page with MOF/ZIF theme hubs when routing questions about vitrification versus crystalline stability.

## Limitations

- Transferability across full ZIF chemical space still requires validation per family; reactive FF accuracy for complex organometallic linkers must be checked against higher-level benchmarks.

## Relevance to group

Key **MOF/ZIF + ReaxFF** capability demonstration from the van Duin and Mauro collaboration—important for porous framework entries in the wiki.

## Reader notes (navigation)

- **Cluster:** [[theme-porous-mof-zeolite]] — **ZIF1** gold in [`V1_FROZEN`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/benchmarks/V1_FROZEN.md).

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcb.8b08094](https://doi.org/10.1021/acs.jpcb.8b08094)
- Abstract: `normalized/extracts/2018yang-j-phys-chem-enabling-computational_p1-2.txt`

## Related topics

- [[reaxff-family]]
- ZIF glasses and melt–quench reactive MD
- Metal–organic frameworks beyond fixed-bond force fields
