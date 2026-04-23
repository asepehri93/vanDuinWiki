---
id: paper:2013grossman-venue-acs-nn
type: paper
title: "The impact of functionalization on the stability, work function, and photoluminescence of reduced graphene oxide"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - method:classical-md
  - method:dft-static
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:graphene-carbon
  - keyword:dft-static
  - keyword:reactive-md
source_refs: []
doi: "10.1021/nn305507p"
year: 2013
authors:
  - "Kumar, Priyank V."
  - "Bernardi, Marco"
  - "Grossman, Jeffrey C."
venue: "ACS Nano"
pdf_sha256: "c2ea609adffd18aaf789fbcdd99e3da249a7321b0206eb94177aea0736171db1"
pdf_path: "papers/ReaxFF_others/Grossman_group_ACS_Nano_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013grossman-venue-acs-nn -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

Combines **classical MD** and **DFT** on ensembles of **reduced graphene oxide (rGO)** models to separate how **oxygen-containing functional groups** (carbonyl, hydroxyl, epoxy, ether motifs in the study’s structural library) influence **thermodynamic stability**, **work function**, and **photoluminescence** trends. The analysis emphasizes **metastability** of certain **carbonyl-rich** compositions and their propensity to evolve toward other oxygen/carbon hybridization states, linking microscopic group distributions to **optoelectronic** observables relevant to thin-film devices. The study is motivated by **tunable** rGO electronic properties in **device** stacks where reduction level and oxygen motif mix are process-controlled.

## Methods

**1 — MD application (atomistic dynamics).** **Engine / code:** **Classical molecular dynamics** with a **reactive force field** (see **`pdf_path`** **Methods** for the specific potential form and software). **System size & composition:** **>360** disordered **rGO** supercells, each with **>200 atoms**, generated from **nine** initial **graphene oxide (GO)** compositions with **O** contents of **15**, **20**, and **25 at.%** and **epoxy**:**hydroxyl** ratios **3:2** and **2:3** (abstract / **Figure 1a** narrative in `normalized/extracts/2013grossman-venue-acs-nn_p1-2.txt`). **Boundaries / periodicity:** **periodic** sheet **supercells** with **PBC** consistent with the **MD** reduction workflow described in the article (confirm cell vectors in **`pdf_path`**). **Protocol / temperature:** thermal reduction of **GO** at **1500 K** using **MD** (**Figure 1a** schematic in the extract), followed by **DFT** relaxation/characterization. **Ensemble / timestep / duration / thermostat / barostat:** **N/A —** not restated numerically in the indexed **p1–2** excerpt; copy from **`pdf_path`** **Methods** (likely **NVT**-class annealing for reduction, but confirm). **Pressure:** **N/A —** not stated as an **MD** control variable in the excerpt. **Electric field:** **N/A —**. **Replica / enhanced sampling:** **N/A —**.

**2 — Force-field training.** **N/A —** uses a published **reactive** **classical** potential as a **computational synthesis** tool rather than fitting a new **ReaxFF** line in this article.

**3 — Static QM / DFT.** **Plane-wave** **DFT** relaxes **MD**-generated **rGO** cells and supports **reaction** energetics among oxygen moieties, **work function** trends, **electronic structure**, and **PL**-related analyses (**Methods** in **`pdf_path`** for **functional**, **PAW**/**pseudopotential** treatment, cutoff, **k**-mesh, and SCF convergence).

## Findings

**1 — Outcomes & mechanisms.** **Carbonyl-rich rGO** is described as **metastable** at **300 K**, with spontaneous **carbonyl→hydroxyl** **reaction** pathways near **carbon vacancies** and **holes**, rationalizing evolution toward **hydroxyl-rich**, lower-defect arrangements in the sampled ensemble.

**2 — Comparisons.** The study is positioned against prior **experimental** challenges in characterizing disordered **rGO** and uses **DFT** across a large structural ensemble to connect motifs to observables (see **`pdf_path`** for **literature** discussion).

**3 — Sensitivity & design levers.** For fixed **oxygen** content, varying **epoxy**, **hydroxyl**, and **carbonyl** fractions tunes the **work function** by up to **~2.5 eV** and shifts **PL** peak energies in the authors’ **DFT** analysis (abstract / extract).

**4 — Limitations & outlook.** Disorder is stylized and **DFT** approximations plus finite ensemble sizes limit quantitative **PL** predictions; wet-processing environments may require additional modeling layers beyond the gas-phase reduction **MD** step noted in the article discussion.

**5 — Corpus honesty.** Ground claims in **`pdf_path`** and `normalized/extracts/2013grossman-venue-acs-nn_p1-2.txt`; this corpus filename is a convenience path for the **ACS Nano** article (**DOI** in front matter).

## Limitations

- Model disorder is necessarily stylized; DFT approximations and ensemble sizes limit quantitative PL predictions.
- **Water** and **solvent** environments present in some experiments are omitted in the gas-phase **MD** reduction step, so direct quantitative agreement with wet-processed rGO may require additional modeling layers.

## Relevance to group

**Not ReaxFF-based**; corpus **rGO** electronic-structure reference adjacent to graphene-oxide **ReaxFF** applications elsewhere in the knowledge base.

## Citations and evidence anchors

- Abstract and results: property decomposition by functional group (ACS Nano; DOI above).

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]
