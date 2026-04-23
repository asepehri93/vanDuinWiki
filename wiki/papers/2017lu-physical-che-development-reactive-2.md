---
id: paper:2017lu-physical-che-development-reactive-2
type: paper
title: "Development of a reactive force field for the Fe–C interaction to investigate the carburization of iron"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1039/C7CP05958B"
year: 2018
authors:
  - "Kuan Lu"
  - "Chun-Fang Huo"
  - "Wen-Ping Guo"
  - "Xing-Wu Liu"
  - "Yuwei Zhou"
  - "Qing Peng"
  - "Yong Yang"
  - "Yong-Wang Li"
  - "Xiao-Dong Wen"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "a56d67e0ee2089fd7d2617803a558f290edfac1bdb0860801e24fe22216cb416"
pdf_path: "papers/ReaxFF_others/Lu_PCCP_FeCx_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017lu-physical-che-development-reactive-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the PCCP article identified by `doi`, `title`, and `pdf_path`. Numerical barriers, diffusion coefficients, and fitting details should be verified in the **published paper** and **ESI** (referenced in the article).

## Summary

Carburization of iron underpins iron-based catalysts (e.g. Fischer–Tropsch), steel processing, and carbon nanotube growth; reliable **Fe–C** reactivity is needed for large-scale MD. The authors introduce **RPOIC-2017**, a **ReaxFF** parameter set for Fe–C focused on carbon diffusion in \(\alpha\)-Fe, building on inherited **ReaxFF-2012**-related parameters aimed at hydrogen chemistry. **RPOIC-2017** is trained to **VASP PBE** data: equations of state of \(\alpha\)-Fe, lattice constants of Fe\(_3\)C and Fe\(_4\)C, carbon-covered surface supercells, and carbon diffusion barriers in bulk and on surfaces. **LAMMPS** MD validates interstitial carbon diffusion versus **MEAM** (Laalitha parameterization); the authors report closer agreement with DFT for barriers and diffusion coefficients than the MEAM baseline they quote.

## Methods

**A — Force-field training / fitting:** **RPOIC-2017** **ReaxFF** trained to **VASP PBE** data: **α-Fe** **EOS**, **Fe\(_3\)C**/**Fe\(_4\)C**, **C**-covered **surfaces**, **bulk**/**surface** **diffusion** barriers—inherits **ReaxFF-2012**-related **Fe–H** subsets then **reoptimizes** for **C** in **α-Fe**.

**B — Molecular dynamics / sampling:** **LAMMPS** **NVT** after **CG** relax: **0.25 fs**, **Berendsen** (**100 fs** damping); **MSD**/**Arrhenius** on **8×8×8** and **20×20×20** **α-Fe** supercells with **periodic boundary conditions**, **700–1300 K** (**100 K** steps). **MEAM** (**Laalitha**) comparison in **LAMMPS** per **ESI** (**1 fs**, **2 ns** segments as stated for MEAM). **Duration:** **up to 500 ps** for the **ReaxFF RMD** trajectories. **N/A — pressure / barostat** during **NVT** **MSD** sampling.

**C — DFT / static QM:** **PBE** training set as above.

**D — Review / non-simulation framing:** **Primary** **PCCP** article—duplicate corpus path vs **`[[2017lu-physical-che-development-reactive]]`**.

## Findings

**Outcomes and mechanisms.** **RPOIC-2017** reproduces **DFT** trends for **carbon diffusion** in **α-Fe** more closely than the **MEAM** potential used for comparison, for both **barriers** and **Arrhenius-derived diffusion coefficients**.

**Comparisons.** The **ReaxFF vs MEAM** comparison is run under the same **LAMMPS NVT** workflow documented in the article/ESI (**0.25 fs**, **Berendsen** thermostat, **700–1300 K** MSD windows).

**Sensitivity / design levers.** **Temperature**, **supercell size**, and **statistical replication** are the main knobs controlling **MSD** noise and extracted **Arrhenius** parameters.

**Limitations and outlook (as authored).** The parameterization targets **Fe–C** diffusion phenomena; **multi-species** industrial **FT** networks may require merges with other reactive parameter sets.

**Corpus / PDF honesty.** Duplicate ingest: **`Lu_PCCP_FeCx_2018.pdf`** vs **`Kuan_Lu_PCCP_2017_FeC.pdf`** on **`[[2017lu-physical-che-development-reactive]]`**—mirror substantive edits across siblings.


## Limitations

- Parameterization targets **Fe–C** diffusion and related structures; transfer to full Fischer–Tropsch or multi-species pipelines may require additional training or merging with other ReaxFF sets.
- **Berendsen** thermostat and finite MD lengths affect precise transport statistics; long-time defect equilibria may need longer runs or enhanced sampling.
- Comparison is against a selected **MEAM** baseline; other empirical models could behave differently.

## Relevance to group

Cites **A. C. T. van Duin** and co-workers’ ReaxFF lineage and extends **Fe/C/H**-related work toward **carbon diffusion** in iron—useful cross-reference for **steel**, **catalysis**, and **ReaxFF** parameterization practice in the corpus.

## Citations and evidence anchors

- DOI: [10.1039/C7CP05958B](https://doi.org/10.1039/C7CP05958B)
- ESI (potential definitions, MSD/barrier procedures): linked from the publisher page via the article’s ESI notice.
- Text pointers: `normalized/extracts/2017lu-physical-che-development-reactive-2_p1-2.txt`.

## Reader notes (navigation)

- **Duplicate corpus PDF (same article):** This entry uses `papers/ReaxFF_others/Lu_PCCP_FeCx_2018.pdf`. The same PCCP paper is curated on [[2017lu-physical-che-development-reactive]] (`papers/ReaxFF_others/Kuan_Lu_PCCP_2017_FeC.pdf`). Treat as one publication, two ingested binaries.
- **Force-field overview:** [[reaxff-family]]
- **Themes:** Fischer–Tropsch / iron carbides connect to [[theme-catalysis-surfaces]] and [[theme-pyrolysis-combustion-organics]] where relevant.

## Related topics

- [[reaxff-family]]
- [[theme-catalysis-surfaces]]
