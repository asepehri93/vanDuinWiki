---
id: paper:2020sjtudizhang-gmail-co-venue-paper
type: paper
title: "Supporting information: Controlling the nucleation and growth orientation of nanocrystalline carbon films (plasma-assisted deposition)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-application
  - keyword:monte-carlo-sampling
candidate_tags: []
source_refs: []
doi: ""
year: 2020
authors:
  - "Di Zhang"
venue: "JACS supporting information PDF (Shanghai Jiao Tong University)"
pdf_sha256: "8bc3570f696f2c404be08caf2fde31e93f480c1ddce864eedcbcc6e424c778fb"
pdf_path: "papers/ReaxFF_others/DiZhang_JACS_2020_carbonfilm_growth_SI.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2020sjtudizhang-gmail-co-venue-paper -->

This corpus entry registers the **Supporting Information** PDF for a **JACS** study on **nanocrystalline carbon film** nucleation and growth under **plasma-assisted deposition**, using a **hybrid molecular dynamics / time-stamped force-biased Monte Carlo (MD/tfMC)** workflow with **ReaxFF**-based chemistry for **carbon** and controlled **Ar** co-deposition. The ingest filename reflects a legacy **email-string** artifact; the SI authorship is **Di Zhang** and co-workers at **Shanghai Jiao Tong University** as excerpted.

## Summary

The SI excerpt documents simulation setup for **hybrid MD/tfMC** cycles in which **C** and **Ar** atoms are deposited from the top of the box each cycle. **Experimental** inputs link **carbon deposition rate** and **Ar** ion flux to simulation **C:Ar** flux ratios; simulations explore a **wider Ar flux range** than experiment before converging to about **1:10 C:Ar**. The SI references **tfMC** parameterization, **ReaxFF2013** benchmarks in **LAMMPS**, and **XRD** / **crystallinity** definitions. **N/A** — full quantitative film-property conclusions here; the **main JACS article** holds primary results (DOI not recorded in this stub’s front matter).

## Methods

**1 — MD application and hybrid tfMC.** Potentials including **ReaxFF2013** and alternatives are benchmarked **in LAMMPS** (SI **S3**). The deposition **supercell** (SI **Fig. S1**) is **~15 × 15 × 80 Å** with **PBC** in-plane as specified for the growth box; the substrate is **~17 Å** thick split into **fixed (~3 Å)**, **thermostatic (~6 Å)**, and **free (~8 Å)** layers; the film accumulates many **thousands of atoms** as **C** and **Ar** are added. **C** and **Ar** are incident from **+z** with **xy** randomization; separate **Ar** irradiation tests use a **~45.36 × 26.19 Å** **graphene** patch (edge fixed, center free). **C** and **Ar** are deposited in **MD/tfMC** hybrid cycles. **tfMC** uses temperature **T** and maximum displacement **δ**; the SI gives **δ** screening on graphite (e.g. **573 K** critical **δ ≈ 0.21–0.23**) and a **Timonova**-style **δ–T** scaling (SI **S2**). **OVITO** is used for visualization. **N/A —** NPT, electric field, or enhanced umbrella/metadynamics: not stated in the SI excerpt. **N/A —** full timestep and production ns totals for every stage: confirm the SI PDF; **N/A** — complete thermostat name if the excerpt does not name it. Experimental **C** flux **~1.046×10¹⁹ m⁻² s⁻¹** and **Ar** **~1.0–4.0×10¹⁹ m⁻² s⁻¹** anchor flux targets; C:Ar trends toward **~1:10** in the SI narrative.

**2 — Force-field training.** The SI uses **Reaxff2013**-class descriptions as implemented; **N/A** — a new parameterization in this SI text is not excerpted; parent article holds fitting narrative.

**3 — Static QM.** **N/A** in the indexed SI excerpt for a standalone DFT block.

**4 — Review or non-simulation.** **N/A** — method SI for a research article.

## Findings

**Outcomes and corpus scope.** The excerpt emphasizes **reproducing experimental flux ratios** and documenting the **MD/tfMC** and **Reaxff2013** **LAMMPS** setup. **N/A** in this **SI** note for a full stand-alone set of main-text film metrics—see the **JACS** article (when its slug exists).

**Comparisons and sensitivity.** Links **C:Ar** tuning to both experiment and a wider Ar sweep. **N/A** — new numerical property tables not fully replicated in this **SI**-only wiki summary.

**Limitations.** This wiki page is **SI-only**; the parent **DOI** is missing from front matter until ingest.

**Corpus honesty.** Verify figures (**Fig. S1** etc.) in `pdf_path`; `extraction_quality: partial` marks incomplete automated coverage.

## Limitations

Wiki page is **SI-only**; **methods narrative**, **figures**, and **conclusions** should be completed from the **primary article** PDF when ingested. **DOI** for the parent paper is **not** recorded in this stub’s front matter.

## Relevance to group

Demonstrates corpus practice of registering **SI packages** that contain **ReaxFF + Monte Carlo** hybrid protocols for **carbon thin-film** growth.

## Citations and evidence anchors

Link the parent **`paper:`** slug once the **main article** ingest exists; until then cite the SI file path above.

## Related topics

- [[reaxff-family]]
