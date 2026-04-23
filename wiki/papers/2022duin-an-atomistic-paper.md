---
id: paper:2022duin-an-atomistic-paper
type: paper
title: "Oxidation and hydrogenation of monolayer MoS2 with compositing agent under environmental exposure: ReaxFF Mo/Ti/Au/O/S/H force field development and applications"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - material:tmd
  - domain:mechanics-tribology
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:2d-materials
  - keyword:thermal-decomposition
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.3389/fnano.2022.1034795"
year: 2022
authors:
  - "Qian Mao"
  - "Yuwei Zhang"
  - "Malgorzata Kowalik"
  - "Nadire Nayir"
  - "Michael Chandross"
  - "Adri C. T. van Duin"
venue: "Frontiers in Nanotechnology"
pdf_sha256: "7692adbc7f58dbd464955f2cbb75aa5e37d4958e841cc7a73680a6de2bcf7951"
pdf_path: "papers/Mao_MoS2_TiO2_Frontiers_Nano_2022_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2022duin-an-atomistic-paper -->

## Summary

This entry mirrors **[[2022mao-venue-fnano-2022-1034795]]** (same **DOI** and scientific content) but ingests the **Frontiers galley** PDF (`papers/Mao_MoS2_TiO2_Frontiers_Nano_2022_galley.pdf`) with **`extraction_quality: partial`**. Prefer the **VOR** page for figures and SI cross-references unless you specifically need this file’s provenance.

The article develops a **Mo/Ti/Au/O/S/H ReaxFF** and applies **AMS** reactive MD to **monolayer MoS\(_2\)** oxidation and hydrogenation with **Ti** clusters under **O\(_2\)** / **H\(_2\)O** (and related) environments, including high-temperature ramps used to access reaction pathways on MD time scales. This slug exists to preserve manifest provenance for the galley bytes while keeping the scientific narrative aligned with the Frontiers version-of-record page.

## Methods

**Canonical curation and PDF:** use [[2022mao-venue-fnano-2022-1034795]] for the full Methods/Results and version-of-record pagination. This slug’s `pdf_path` is the **Frontiers galley** `papers/Mao_MoS2_TiO2_Frontiers_Nano_2022_galley.pdf` (`extraction_quality: partial`); copy all numerical settings from the VOR/DOI PDF, not the galley alone.

**1 — MD application (atomistic dynamics).** The article uses **ReaxFF**-based **reactive** **MD** in LAMMPS-class / AMS-annotated **workflows** (exact program strings in the VOR) on monolayer **MoS\(_2\)** (pristine and defective), with or without a **Ti\(_{20}\)** **cluster** and with **O\(_2\)** / **H\(_2\)** and **H\(_2\)**O-relevant **environments** at elevated **reactant** **density** to access chemistry on nanosecond time scales. **3D** **PBC** on the in-plane supercell; confirm the **Z** dimension / vacuum in the VOR. **Protocol (recalled from the article curation in this repo):** minimization → **NVT** at **300 K** for **\(\sim 500\,\text{ps}\)** equilibration → heat to **3000 K** **NVT** with **\(\Delta t = 0.1\,\text{fs}\)**; optional **\(\sim 1000\,\text{K}\)** annealing segments. Thermostat and damping: see VOR. **Barostat: N/A** in the headline **NVT** **ramp-heavy** **protocol** (re-check VOR if a pressure-coupled segment is reported). **Electric field: N/A.** **Enhanced sampling: N/A** (no umbrella/Metadynamics in this note unless the VOR states otherwise). ReaxFF **QEq** and **nonbond** **cutoff** **policy** per the Frontiers Methods. Post-process with VMD/OVITO; bond/fragment ID cutoffs (e.g. Mo–S \(\sim 3.0\,\)Å) are in the VOR and are not re-stated here for this partial galley ingest.

**2 — Force-field training.** A new **Mo/Ti/Au/O/S/H** **ReaxFF** **line** (DFT/DFTB **training** **set**, **optimization**, **element** **scope**) is on the VOR page; this duplicate slug does not duplicate the fit tables.

**3 — Static QM / DFT (parametrization).** DFT/DFTB **benchmarks** for **ReaxFF** **fitting** are documented on the **VOR**; this galley **manifest** note does not expand them.

**4 — Experiments. N/A** — computational work with device-processing **motivation** in the VOR.

## Findings

**Outcomes and mechanisms.** Simulations report temperature-dependent **oxidation/hydrogenation** sequences: **S** removal, **O** incorporation, and **Ti–O/S** interactions that compete with **MoS\(_2\)** **degradation**; **Ti\(_{20}\)** **clusters** mediate **O** **transfer** and local reconstruction relative to **pristine** **MoS\(_2\)** under the same thermal ramps. **Quantitative** **barriers** and full **reaction** **networks** should be read from the VOR/SI—this **galley** **ingest** is **not** a substitute for the typeset **PDF**. Treat **\(\sim 3000\,\)K\)** **NVT** **\(\Delta t=0.1\,\)fs\)** **windows** as deliberately aggressive **rare-event** sampling, not literal ambient-device oxidation kinetics (see `## Limitations`).

**Comparisons and levers.** Pristine **vs** defective **MoS\(_2\)**; with **vs** without **Ti\(_{20}\)**; gas **composition**, **density**, and **thermal** **ramps** in the VOR. **Quantitative** **barriers** and full **reaction** **graphs** are read from the VOR/SI, not this galley file.

## Limitations

Proof-stage PDF; extreme heating rates and small system sizes probe pathways relevant to high-temperature oxidation rather than ambient kinetics directly. This slug preserves **manifest** linkage to **`papers/Mao_MoS2_TiO2_Frontiers_Nano_2022_galley.pdf`**; narrative **figures**, **timestep** tables, and **QM** benchmarks should be taken from **`[[2022mao-venue-fnano-2022-1034795]]`** or the **DOI** landing page when **pagination** matters for citations.

## Relevance to group

Core van Duin-group ReaxFF development for TMD tribology/chemistry with explicit Ti/Au additives.

## Citations and evidence anchors

- [10.3389/fnano.2022.1034795](https://doi.org/10.3389/fnano.2022.1034795)

## Reader notes (navigation)

- Canonical curated page with full extraction: [[2022mao-venue-fnano-2022-1034795]]. 2D TMD hub: [[theme-2d-epitaxy-growth]]. Galley duplicate policy: [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) · [local](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (Frontiers alternate path).

## Related topics

- [[2022mao-venue-fnano-2022-1034795]]
- [[reaxff-family]]
- [[theme-2d-epitaxy-growth]]
