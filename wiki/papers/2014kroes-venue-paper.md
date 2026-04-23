---
id: paper:2014kroes-venue-paper
type: paper
title: "Characterizing and understanding divalent adsorbates on carbon nanotubes with ab initio and classical approaches: size, chirality and coverage effects"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:dft-static
  - method:classical-md
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:graphene-carbon
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/ct500701n"
year: 2014
authors:
  - "Kroes, Jaap M. H."
  - "Pietrucci, Fabio"
  - "Curioni, Alessandro"
  - "Andreoni, Wanda"
venue: "Journal of Chemical Theory and Computation"
pdf_sha256: "6980d20d86f36c628c206dea998fec2d40d997b68cf9296f4c6cc1c786585c5b"
pdf_path: "papers/ReaxFF_others/Kroes_JCTC_CNT_oxidation.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2014kroes-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **Just Accepted** PDF header and abstract visible in the extract. Final pagination and editorial changes may differ from the published issue.

## Summary

Large-scale DFT simulations study oxygen chemisorption on single-walled carbon nanotubes across diameters (~0.6–1.5 nm), chiralities, and coverages. Structural and electronic properties plus diffusion barriers depend strongly on both tube radius and adsorbate concentration—simple fixed models are argued to miss this coupling (Just Accepted abstract; extract). The work is positioned as a cautionary map for reactive FF users: chemisorption energetics on curved sp² carbon are not transferable from graphene limits without explicit curvature and coverage dependence. **Sulfur** is treated as an **isoelectronic** adsorbate alongside oxygen in parts of the survey, highlighting **element-specific** **motifs** (**epoxide** vs **ether**) that also shift with **coverage**.

## Methods

### DFT survey of chemisorbed oxygen on SWCNTs

- **Large-scale DFT-PBE** calculations map **oxygen chemisorption** on **single-walled carbon nanotubes** spanning **diameters ~0.6–1.5 nm**, multiple **chiralities**, and **oxygen concentrations ~0.1–1%** (Just Accepted abstract).
- Reported quantities include **relaxed configurations**, **relative stabilities**, **binding energies**, and **hopping barriers**, including **clustering** effects that **stabilize ether (ET)** motifs (abstract).

### Isoelectronic adsorbates

- **Sulfur** is treated as an **isoelectronic** adsorbate alongside **oxygen**, emphasizing **element-specific** preferences (**epoxide vs ether**) and **diffusion** behavior (abstract).

### Classical / reactive comparison

- The authors compare **DFT** results (including multiple **XC** choices where noted) with **ReaxFF** for the same **chemisorption** problem class to expose **agreement** and **large discrepancies** (abstract/introduction excerpt).

### Coverage / ingest note

- Corpus PDF is **Just Accepted**; **k-mesh**, **cutoffs**, and **supercell** dimensions are in **JCTC** Methods—verify against the **final** issue tables before quoting numbers.

### 1 — MD application (this ingest)

- **Headline scope:** **Large-scale DFT** mapping of **oxygen**/**sulfur** **chemisorption** on **SWCNT** models is the primary evidence chain in the **Just Accepted** abstract ingested here; **classical/reactive MD production trajectories** are **not** the centerpiece of the abstract summary.
- **Engine / code:** **Molecular dynamics** engines are **not** the headline tool in the abstract summary; any **MD** validation segments should be read from **JCTC** Methods (**N/A — MD package name not on indexed extract**).
- **System size & composition:** **SWCNT** **supercells** spanning **diameters ~0.6–1.5 nm** with **oxygen concentrations ~0.1–1%** (abstract); **exact atom counts** are **N/A — not on indexed extract page 1**.
- **Boundaries / periodicity:** **Periodic** **nanotube** **supercells** are implied by the **DFT** survey description (**abstract**); **N/A — explicit PBC strings not on indexed extract page 1**.
- **Ensemble:** **NVT**/**NVE**/**NPT** choices for any finite-temperature segments are **N/A — not stated on indexed extract page 1** (read **JCTC** Methods).
- **Timestep / thermostat / duration:** **N/A — headline MD integration settings not on indexed extract page 1** (read **JCTC** Methods for any finite-temperature or MD segments).
- **Barostat / hydrostatic pressure:** **N/A — pressure control for MD not stated on indexed extract page 1** (static **DFT** relaxations dominate the abstract framing).
- **Temperature:** **N/A — explicit MD thermostat temperatures not stated on indexed extract page 1** (see **JCTC** Methods).
- **Replica / enhanced sampling:** **N/A — umbrella/metadynamics not indicated** on indexed extract page 1.

### 2 — Force-field training / classical reactive comparison

- **ReaxFF comparison:** the **abstract** reports **DFT** vs **ReaxFF** comparisons for the same **chemisorption** problem class showing both agreement and large discrepancies; **N/A — which ReaxFF parameterization/build and comparison protocol are not restated on the indexed extract** (article body/SI).

## Findings

### Outcomes and mechanisms

**DFT-PBE** shows **strong dependence** of **structure**, **electronic response**, and **hopping barriers** on **tube diameter** and **oxygen concentration** (Just Accepted abstract). **Clustering** grows with **concentration**, **stabilizing ether (ET) groups** while affecting **barriers** only **modestly**; differences vs **graphene** persist even for **~1.5 nm** tubes.

### Comparisons

**Isoelectronic** **sulfur** vs **oxygen** differs: **sulfur** favors **epoxide (EP)** motifs, **diffuses more easily**, and **closes the gap** faster with concentration (**abstract**). **DFT** vs **ReaxFF** comparisons show both **similarities** and **dramatic discrepancies** for these **chemisorption** problems (**abstract**).

### Sensitivity

**Sensitivity** to **coverage** (**oxygen concentration**) and **curvature** (**tube diameter / chirality**) is the paper’s headline lever in the **abstract** framing.

### Limitations and corpus honesty

Verify **final tables/figures** against the **published JCTC** issue because the corpus PDF is **Just Accepted** (**## Limitations**). **PBE** limitations and any **hybrid/meta-GGA** checks are **not** recoverable from the one-page extract used here—read the full **PDF**.

## Limitations

“Just Accepted” status at ingest—verify numerical tables against the final JCTC issue. DFT-PBE itself omits exact exchange and strong correlation corrections that can shift oxygen binding on curved sp² carbon, so the ReaxFF comparison section should be read as diagnosing force-field gaps relative to a single DFT rung rather than as an absolute experimental benchmark.

## Citations and evidence anchors

- DOI `10.1021/ct500701n` (Just Accepted banner; extract).
- Abstract (extract page 1).

## Reader notes (navigation)

- **DFT vs ReaxFF** on **CNT oxygenation**; carbon hub [[graphene-nanocarbon]]; corpus PDF is **Just Accepted**—verify numbers against final **JCTC** issue ([NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) section D for Just Accepted handling).

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]
