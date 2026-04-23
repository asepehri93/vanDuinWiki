---
id: paper:2017lu-physical-che-development-reactive
type: paper
title: "Development of a reactive force field for the Fe&#x2013;C interaction to investigate the carburization of iron"
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
  - keyword:reactive-md
  - keyword:metallic-systems
  - keyword:classical-ff
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1039/C7CP05958B"
year: 2017
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
venue: "Phys. Chem. Chem. Phys. (2018), 20, 775–783"
pdf_sha256: "b26a3dda1307c311e7da6d3ccc7dedeea38bdb7454ed44eae8ca5c210d94d71a"
pdf_path: "papers/ReaxFF_others/Kuan_Lu_PCCP_2017_FeC.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017lu-physical-che-development-reactive -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, barrier heights, and simulation protocols, use the **peer-reviewed article** and **ESI**—not this page alone. The local text dump used here is only `normalized/extracts/2017lu-physical-che-development-reactive_p1-2.txt` (first pages).

## Summary

This PCCP article introduces an Fe–C–focused ReaxFF parameter set named **RPOIC-2017** for carbon diffusion in \(\alpha\)-Fe, motivated by carburization of iron in catalyst and steel contexts. The parameters build on a subset inherited from earlier ReaxFF-2012-style training aimed at hydrogen chemistry, and are fitted to **first-principles** reference data that include the equation of state of \(\alpha\)-Fe, lattice constants of Fe\(_3\)C and Fe\(_4\)C, periodic iron surfaces with varying carbon coverages, and carbon diffusion barriers in the bulk and on surfaces. The abstract reports that the fitted potential reproduces carbon **diffusion coefficients** and **barriers** more satisfactorily than a **MEAM** treatment used for comparison.

## Methods

**A — Force-field training / fitting:** **RPOIC-2017** **ReaxFF** for **Fe–C**, extending **ReaxFF-2012**-related **Fe–C–H** subsets; **weighted** fit to **QM** data: **α-Fe** **EOS**, **Fe\(_3\)C**/**Fe\(_4\)C** lattices, **C**-covered **surfaces**, **bulk**/**surface** **C** **diffusion** barriers.

**B — Molecular dynamics / sampling:** **LAMMPS** **NVT** validation of **interstitial C diffusion** in **α-Fe** after **conjugate-gradient** relaxation: **Δt = 0.25 fs**, **Berendsen thermostat** with **100 fs** damping constant (as in the authors’ parameter list—verify the unit string in your PDF copy); **MSD**/**Arrhenius** analysis on **8×8×8** and **20×20×20** **α-Fe** supercells over **700–1300 K** (**100 K** steps, **three** independent seeds per state point as described in the article/ESI). **MEAM** (**Laalitha**) comparison trajectories are run in **LAMMPS** per **ESI** (**2 ns** MEAM segments with **1 fs** timestep where explicitly contrasted). **Periodic boundary conditions** (**3D PBC**) apply to the **bcc α-Fe** supercells. **Duration:** **up to 500 ps** maximum **RMD** trajectory length stated in the PCCP Methods for the **ReaxFF** diffusion runs. **N/A — pressure / barostat**: **constant-volume NVT** diffusion sampling—**no** stated **NPT** control during the **MSD** windows.

**C — DFT / static QM:** **First-principles** reference (**VASP**/**PBE** per article) for **training** data.

**D — Review / non-simulation framing:** **Primary** **PCCP** parameterization paper—**not** a review. **Duplicate PDF:** **`[[2017lu-physical-che-development-reactive-2]]`**.

## Findings

**Outcomes and mechanisms.** **RPOIC-2017** is positioned to reproduce **DFT** trends for **carbon diffusion** in **α-Fe** and related **surface** environments more faithfully than the **MEAM** baseline the authors compare against, for both **barriers** and **Arrhenius-derived diffusion coefficients**.

**Comparisons.** Head-to-head **ReaxFF vs MEAM** in **LAMMPS** under the same **NVT** sampling protocol (details in **ESI**) anchors the claim that the **refit** improves **QM agreement** for the targeted **Fe–C** observables.

**Sensitivity / design levers.** **Temperature** (**700–1300 K** window), **supercell size**, and **thermostat/statistics** choices affect extracted **diffusivities**; the paper documents its **MSD** procedure for repeatability.

**Limitations and outlook (as authored).** Training emphasizes **interstitial C in α-Fe**; broader **carburization** chemistries may need **additional** training data beyond the stated scope.

**Corpus / PDF honesty.** This slug uses `papers/ReaxFF_others/Kuan_Lu_PCCP_2017_FeC.pdf`; **`[[2017lu-physical-che-development-reactive-2]]`** duplicates the article under a second filename—keep protocol text **aligned** across siblings.


## Limitations

- Training and validation emphasize **interstitial carbon diffusion in \(\alpha\)-Fe** and related surfaces; transfer to full carbide phases, melt chemistry, or complex gas-phase elementary steps may require additional data.
- The local extract covers only the opening pages; **quantitative** MD results and parameter tables rely on the **full PDF and ESI**.

## Relevance to group

The work is a **downstream application** of the ReaxFF formalism (the introduction cites the original ReaxFF formulation). It is **not** van Duin–group–authored, but it is a clear **Fe–C ReaxFF parameterization** reference for metallurgical and Fischer–Tropsch–adjacent simulations that connect to broader [[reaxff-family]] practice.

## Citations and evidence anchors

- DOI: [10.1039/C7CP05958B](https://doi.org/10.1039/C7CP05958B)
- Text-aligned pointers (partial): `normalized/extracts/2017lu-physical-che-development-reactive_p1-2.txt`

## Reader notes (navigation)

- **Duplicate corpus PDF (same article):** The knowledge base also registers a second file for this publication—[[2017lu-physical-che-development-reactive-2]] (`papers/ReaxFF_others/Lu_PCCP_FeCx_2018.pdf`). Prefer the **version-of-record** PDF from the publisher when citing; treat the two paths as **corpus duplicates** of one PCCP paper.
- **Theme / method links:** [[reaxff-family]]; Fischer–Tropsch / iron carbides connect to [[theme-catalysis-surfaces]] and [[theme-pyrolysis-combustion-organics]] where relevant.

## Related topics

- [[reaxff-family]]
- [[theme-catalysis-surfaces]]
