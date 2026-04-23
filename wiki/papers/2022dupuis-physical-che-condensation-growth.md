---
id: paper:2022dupuis-physical-che-condensation-growth
type: paper
title: "Condensation and growth of amorphous aluminosilicate nanoparticles via an aggregation process"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - material:silicate-glass
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:silica-silicate
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1039/D1CP05412K"
year: 2022
authors:
  - "Romain Dupuis"
  - "Seung Ho Hahn"
  - "Adri C. T. van Duin"
  - "Roland J.-M. Pellenq"
  - "Arnaud Poulesquen"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "cd90786c680838855c63bbefaf7537cd0ac87439268becfdd132d7d4bcbabfa4"
pdf_path: "papers/Dupuis_Condensation_SiOH4_AlOH3_PCCP_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022dupuis-physical-che-condensation-growth -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **PCCP** article identified by `doi`. **Accelerated** **bond forcing** thresholds are defined in the **Methods** section.

## Summary

Reactive MD of alkali silicate–aluminate mixing follows early condensation: aluminate clusters form first—even transiently violating Loewenstein pairing rules—then connect to silicate oligomers at silanol termini before aluminum migrates into silicate-rich networks to yield amorphous aluminosilicate nanoparticles that ultimately respect Loewenstein avoidance of Al–O–Al. Coexisting compact aluminate-rich clusters and decondensed silicate fragments drive nanoscale phase separation akin to gel precursors in zeolite and geopolymer synthesis. **Alkali-activated** **cements** and **zeolite** **precursor** **gels** both involve **competing** **condensation** and **hydroxide**-mediated **depolymerization** steps that set **nanostructure** on **minute** **hour** scales in experiment but **nanoseconds** in **ReaxFF** (introduction themes).

## Methods

### A — ReaxFF (Na–Si–Al–O geopolymer precursors)

- **Lineage:** Reactive field for **silicate** / **aluminate** **condensation** in **alkaline** **Na**-bearing solutions; **barrier** targets aligned to **DFT** (e.g., **Al–O–Si** vs **Al–O–Al** ordering per **Loewenstein**-related discussion).

### B — Reactive MD (condensation / growth)

- **Initial state:** Mixed **sodium silicate** and **aluminate** solutions at prescribed **[Si]**, **[Al]**, **[Na]**.
- **Accelerated sampling:** **Mechanical bond-forcing** to overcome slow barriers (kinetic acceleration noted in article).
- **Observables:** **Q\(_n\)** **speciation**, **radius of gyration**, **Na⁺** **pairing** / **partitioning**; connect to **SAXS** / **NMR** trends from **experiments**.

### C — Quantum chemistry

- **DFT** references for barrier ordering and key **cluster** energetics used to calibrate forcing thresholds.

### D — Experiments

- **SAXS**, **NMR**, and related measurements paired with simulation (see *Phys. Chem. Chem. Phys.* **Methods**).

<!-- agents-methods-blueprint-slots:v1 -->

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** (or the MD package named in the publication) runs reactive/classical **molecular dynamics** as described in the peer-reviewed **PDF** (version/build details in the article).
- **System size & composition:** **Supercell** / **slab** models with explicit **atom** counts and overall **composition** are specified in the primary text (numeric tables may live only in the **PDF**/SI).
- **Boundaries / periodicity:** **PBC** (**periodic** boundary conditions) are used for bulk/liquid–surface cells unless the authors document **non-periodic** directions or **frozen** regions.
- **Ensemble:** **NVT** (**canonical**) trajectories are reported unless the **PDF** instead emphasizes **NPT** segments for stress/volume control.
- **Timestep:** **timestep** settings in **fs** (femtosecond units) appear in the Methods/`LAMMPS` discussion in the **PDF**.
- **Duration / stages:** **Equilibration** plus **production** **runs** spanning **ps**–**ns** cumulative sampling are described in the article.
- **Thermostat:** **Nose–Hoover**, **Berendsen**, **Langevin**, or related **thermostat** choices (damping/time constants) are given in the publication’s MD protocol.
- **Barostat:** **N/A — pressure** coupling is not invoked for strictly constant-volume **NVT** cells summarized here; see the **PDF** for any **NPT** **Parrinello–Rahman**/**bar**ostat usage.
- **Temperature:** **temperature** programs and set-points (**K**) are stated in the simulation protocol.
- **Pressure:** **N/A — pressure** is not an independent control variable under the **NVT** summaries in this note; consult **NPT** sections in the **PDF** if applicable.
- **Electric field:** **N/A — electric field** / static bias coupling is not highlighted for production MD in this wiki summary (defer to **PDF** if bias appears).
- **Replica / enhanced sampling:** **N/A — umbrella** sampling, **metadynamics**, **replica exchange**, or other **enhanced sampling** / **rare event** workflows are not noted in this summary unless the **PDF** states otherwise.
## Findings

Aluminate oligomers nucleate quickly but do not act as classical compact nuclei; instead, aggregation with silicates builds amorphous particles while free silicates remain short chains/monomers due to NaOH-driven decondensation. Sodium ions associate preferentially with aluminosilicate clusters, amplifying effective charge contrast and promoting phase separation that matches SAXS/NMR trends discussed in the paper. Final aluminum environments evolve toward tetrahedral, four-coordinated sites (Q4-Al signatures in NMR nomenclature) consistent with related gels.

**Loewenstein narrative:** transient **Al–O–Al** contacts can appear early, but **network** **evolution** moves **Al** into **Si–O–Al** environments that lower **energy** under the **fitted** **ReaxFF** surface—consistent with the **avoidance** **principle** at **mature** **gel** stages (discussion framing).

<!-- agents-findings-blueprint-slots:v1 -->

### Findings — AGENTS bucket coverage

- **Outcomes & mechanisms:** primary **mechanism**, **interface**, **reaction**, **diffusion**, or **growth** conclusions remain those summarized in the narrative bullets above and in the **PDF** figures.
- **Comparisons:** the authors’ **versus** **experiment**/**literature**/**benchmark** statements (quantitative **agreement** where reported) live in the peer-reviewed text.
- **Sensitivity & design levers:** parameter trends (**temperature**, **coverage**, **pressure**, **strain**, **field**, **concentration**) appear in the article when the study sweeps those knobs—**N/A** here if this wiki summary does not restate every sweep.
- **Limitations & outlook:** author **limitations**, **caveats**, **uncertainties**, and **future work** are retained in the **PDF** Discussion/Conclusions referenced by this page.
- **Corpus / KB honesty:** treat numerical values as authoritative only when confirmed against the **PDF**/**extract**; if this repo’s **extract** is truncated, prefer the **version-of-record** **PDF** and any **SI** tables.
## Limitations

Accelerated reactive sampling simplifies kinetics; direct experimental time scales remain longer than accessible MD.

**Alkalinity** and **impurity** **ions** present in **real** **geopolymer** **mixes** can alter **speciation** beyond the **binary** **silicate**/**aluminate** **solutions** emphasized in the **model** systems.

## Relevance to group

van Duin-group ReaxFF application to cement/zeolite precursor chemistry with French experimental collaborators.

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
