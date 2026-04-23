---
id: paper:2015islam-physical-che-interactions-hydrogen
type: paper
title: "Interactions of hydrogen with the iron and iron carbide interfaces: a ReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:alloys-metallurgy
  - method:reaxff
  - method:monte-carlo
  - task:application
  - task:validation
  - scale:atomistic
source_refs: []
doi: "10.1039/C5CP06108C"
year: 2016
authors:
  - "Md Mahbubul Islam"
  - "Chenyu Zou"
  - "Adri C. T. van Duin"
  - "Sumathy Raman"
venue: "Physical Chemistry Chemical Physics 2016, 18, 761–771"
pdf_sha256: "916b398c5c01518367cdc80093961e6de634edbff50304efec4645548ae86b1e"
pdf_path: "papers/Islam_FeC_PCCP_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015islam-physical-che-interactions-hydrogen -->

## Summary

Islam *et al.* use a **merged and refit ReaxFF Fe/C/H** model to study **hydrogen embrittlement**-relevant scenarios in **α-iron (ferrite)**, **Fe\(_3\)C (cementite)**, and **ferrite–cementite** interfaces, including **hydrogen diffusion** coefficients in the bulk phases, **hydrogen accumulation** at an interface with a **vacancy cluster**, **work-of-separation** trends versus **hydrogen content**, and **nanovoid / vacancy-cluster** behavior explored in part with a **grand canonical Monte Carlo (GCMC)** vacancy-swap scheme. The parameter line merges the **Fischer–Tropsch Fe/C/H** training of **Zou, van Duin, Sorescu** with updated **carbon** parameters from **Srinivasan, van Duin, Ganesh**, followed by a **refit of Fe–C** interactions against the **original training manifold** as stated in the article.

## Methods

**Force-field training (Fe/C/H merge + refit).** The baseline **Fe/C/H** description follows the **Fischer–Tropsch**-oriented parametrization of **Zou, van Duin, and Sorescu** (*Top. Catal.* 2012) for **iron**, **carbide**, and **hydrocarbon-surface** training targets. **Carbon** parameters are updated to the **Srinivasan–van Duin–Ganesh** line (*J. Phys. Chem. A* 2015), and **Fe–C** bonds and selected **Fe–C–H** angle terms are **refit** so that errors relative to the **original training data** remain at the same level as the pre-merge field (tables of key parameters appear in the paper/ESI).

**MD application — hydrogen diffusion in bulk phases.** **NVT** molecular dynamics with **Δt = 0.25 fs** and a thermostat **damping constant of 500 fs** (as written in the article) is used to extract **hydrogen diffusion coefficients** in **bcc iron** and **cementite** at **300, 400, 500, and 600 K**. Supercells up to **18 × 18 × 18** bcc unit cells are explored with **hydrogen concentration** ranging from **10⁻⁴** to **10⁻²** (H:Fe ratio definition in the paper). **PBC** is used in all directions; **conjugate-gradient** relaxation precedes production sampling as described.

**MD application — vacancy void + interface models.** Additional **NVT** setups treat **hydrogen** in **α-iron** containing a **spherical void** (**10 Å** diameter) carved from an **8 × 8 × 8** supercell with **20** hydrogen atoms (protocol in Section 4.3), and **ferrite–cementite** interface models used for **work-of-separation** calculations versus **hydrogen loading**.

**Grand canonical / Monte Carlo vacancy sampling.** A **GCMC**-style **vacancy swap** move (Metropolis acceptance) on an **8 × 8 × 8** **α-iron** supercell initialized with **50** **monovacancies** explores **vacancy clustering** motifs; moves swap **vacancy** content with **lattice sites** when energetically favored, as described in the text around Fig. 6.

Diffusion and interface segments use **multi-nanosecond** **NVT** horizons (exact durations per figure in *PCCP*). **Barostat / NPT pressure control, applied electric fields, and umbrella or replica-exchange MD:** **N/A —** not used in the **constant-volume** protocols summarized above. **MD engine (package name):** **N/A —** the publisher **PDF** text layer searched for this curation does **not** name an MD code (only **ReaxFF**-based protocols); confirm in the **ESI** if a specific integrator package is required for reproduction.

## Findings

**Diffusion and solvation trends.** The paper reports **hydrogen diffusion coefficients** for **ferrite** and **cementite** across the **temperature** and **concentration** grids above, and discusses **site preference** (**T-site vs O-site**) and **barrier** estimates for **T–T** and **T–O–T** hops compared to literature **DFT**.

**Interfaces and decohesion.** **Work of separation** for the **ferrite–cementite** interface **decreases** with increasing **interfacial hydrogen** content, supporting a **hydrogen-induced decohesion** interpretation; **MD** trajectories show **hydrogen accumulation** at the interface, described as **consistent with experimental** expectations.

**Defect clustering.** The **GCMC** section reports coalescence into **large vacancy clusters** (sizes quoted in the figure caption/text), linked qualitatively to **nanovoid** formation evidence discussed by the authors.

## Limitations

- HE mechanisms (**HELP vs HEDE**, trap distributions) remain debated; this paper contributes **atomistic** evidence for a subset of hypotheses.
- Corpus slug uses **2015** while the downloaded PDF header shows **2016** publication metadata; cite by **DOI**.

## Relevance to group

**Adri C. T. van Duin** co-authorship; extends **ReaxFF** to **steel-relevant Fe/C/H** interfaces with direct ties to **hydrogen damage** problems in infrastructure and refining.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1039/C5CP06108C](https://doi.org/10.1039/C5CP06108C)

## Related topics

- [[reaxff-family]]
