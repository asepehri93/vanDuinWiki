---
id: paper:2016tomas-carbon-109-2-graphitization-amorphous
type: paper
title: "Graphitization of amorphous carbons: A comparative study of interatomic potentials"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - method:classical-md
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2016.08.024"
year: 2016
authors:
  - "Carla de Tomas"
  - "Irene Suarez-Martinez"
  - "Nigel A. Marks"
venue: "Carbon (2016) 109, 681–693"
pdf_sha256: "de80f8b9408fcc5f2826aaadc3f30e2beb21ea61c5413255b6b1e7d1943c2905"
pdf_path: "papers/ReaxFF_others/Thomas_Marks_Carbon_comparison_Carbon_2016.pdf"
extraction_quality: "good"
group_affiliation: false
paper_keywords:
  - keyword:lammps
  - keyword:reaxff-application
  - keyword:classical-ff
  - keyword:graphene-carbon
---
<!-- id:paper:2016tomas-carbon-109-2-graphitization-amorphous -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

A **fair, single-code** comparison of **six** widely used **carbon potentials**—**Tersoff**, **REBO-II**, **ReaxFF**, **EDIP**, **LCBOP-I**, and **COMB3**—all run via **LAMMPS**. The authors note that many carbon potentials exist in the literature but usability in community MD software matters in practice; here every model is exercised **as implemented in LAMMPS** without author-side modifications, and the long-range **AIREBO** extension is mentioned as unavailable during their debugging window, which excludes that family from the six-way benchmark. **Liquid quenching** generates **amorphous carbon** at several densities, providing a stringent test of whether each potential reproduces the experimental relation between density and hybridization content; subsequent **high-temperature annealing** probes **graphitization** and tests each potential’s **transferability** for **bond making/breaking** and **structural evolution** toward layered sp²-rich motifs.

## Methods

Comparative **classical / reactive MD** in **LAMMPS** benchmarks published carbon models—**not** a new reactive parametrization.

**1 — MD application (shared protocol).** **Engine:** **LAMMPS** for **Tersoff**, **REBO-II**, **ReaxFF**, **EDIP**, **LCBOP-I**, and **COMB3** **as shipped** (no author-side forks). **AIREBO:** **N/A —** excluded because **LAMMPS AIREBO** routines were **buggy / unusable** during the authors’ tests. **System:** **32,768 carbon atoms** on a slightly randomized simple-cubic lattice at each target **density** (**1.5, 2.0, 2.5, 3.0 g/cm\(^3\)**). **Boundaries:** **three-dimensional PBC** on the bulk supercells described in *Carbon* **109** §3. **Liquid creation:** randomized lattice collapses and melts; **Tersoff / REBO / EDIP** follow **NVE** for the first **0.25 ps** then apply a thermostat to reach **\(T_\mathrm{liquid}\)**, whereas **ReaxFF / LCBOP-I / COMB3** thermostats are engaged from the start to avoid runaway heating. **Liquid \(T_\mathrm{liquid}\):** **6000 K** for **REBO-II**, **EDIP**, **ReaxFF**, **COMB3**; **8000 K** for **Tersoff** and **LCBOP-I**; **liquid hold** **5 ps** (**15 ps** for **LCBOP-I**). **Quench to a-C:** **1 ps** cool to **300 K**, **4 ps** equilibration at **300 K** before analysis. **Annealing:** up to **400 ps** at case-specific **\(T_\mathrm{anneal}\)** chosen from MSD diagnostics (tabulated with melt/anneal temperatures in the paper’s **Table 2**). **Ensembles:** **NVT** for the density-series amorphous/graphitization legs described above. **Timesteps:** **0.05 fs** during liquid creation (**0.01 fs** for **LCBOP-I**); **0.2 fs** thereafter except **ReaxFF** uses **0.1 fs** for annealing. **Barostat / pressure:** **N/A —** cells are prepared at **fixed target densities** in **NVT**, not stress-controlled **NPT**. **Electric field:** **N/A —** not used. **Enhanced sampling:** **N/A —** conventional MD only.

**2 — Force-field training.** **N/A —** published parameter sets are **evaluated**, not refit here.

**3 — Static QM.** **N/A —** not used.

**4 — Post-MD analysis.** **Conjugate-gradient** energy minimization precedes structural metrics; **coordination** (**1.85 Å** cutoff), **Franzblau** ring statistics, **RDFs**, and **Debye \(I(s)\)** (treating the supercell as an isolated cluster for diffraction) follow §3 of the article.
## Findings

**Outcomes.** After the **shared melt–quench–anneal** pipeline, the six potentials show a **wide spread** in **sp\(^2\)** fraction, **RDF** shape, **morphology**, **ring statistics**, and **002**-related **graphitization** metrics. **No single model** is uniformly best; some are **particularly poor** for these tests.

**Comparisons.** **Amorphous sp\(^3\)** vs **density** diverges from cited experiment most strongly at high density (**Figure 2**; **Table 3** lists coordination fractions at **a-C** and at **200 / 400 ps** anneal checkpoints). **COMB3** low-density **a-C** shows excess **triangular** motifs compared with the other five potentials (**Figure 3–4** narrative).

**Sensitivity / levers.** Observables depend on **target density** and on **\(T_\mathrm{liquid}\) / \(T_\mathrm{anneal}\)** choices, which must differ among potentials because effective **melting points** differ.

**Limitations / outlook (authored).** The authors relate poor **transferability** to **functional-form** details and outline needs for **next-generation carbon** potentials.

**Corpus honesty.** This page does not duplicate **Table 2–3** numerics; see the **PDF** for exact percentages and diffraction curves.

## Limitations

- “Fair comparison” still depends on **parameter files** and **LAMMPS** variant details for each potential family.
- Reactive potentials may need different **timestep/temperature** practical limits; the paper should be consulted for run parameters.

## Relevance to group

Benchmark-style study placing **ReaxFF** alongside other carbon reactive/classical models—useful when judging **when ReaxFF is appropriate** for **amorphous carbon** and **graphitization** scenarios.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2016.08.024](https://doi.org/10.1016/j.carbon.2016.08.024)
- Text-aligned pointers: `normalized/extracts/2016tomas-carbon-109-2-graphitization-amorphous_p1-2.txt`

## Reader notes (navigation)

- Carbon FF comparison cluster: [[graphene-nanocarbon]], [[reaxff-family]]; related benchmark: [[2015kroes-venue-ct5b00292]].

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
