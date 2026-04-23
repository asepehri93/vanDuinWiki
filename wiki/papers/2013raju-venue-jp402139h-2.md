---
id: paper:2013raju-venue-jp402139h-2
type: paper
title: "ReaxFF reactive force field study of the dissociation of water on titania surfaces"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:water-interfaces
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp402139h"
year: 2013
authors:
  - "Muralikrishna Raju"
  - "Sung-Yup Kim"
  - "Adri C. T. van Duin"
  - "Kristen A. Fichthorn"
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "d37d57bdcb70ae2675992e99ce1872e0be06476abc6db23c2f36ef39c1603a0e"
pdf_path: "papers/Raju_TiO2_water_JPC_C_2013_reduced.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013raju-venue-jp402139h-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

Reactive MD at 300 K examines water adsorption and dissociation on multiple TiO\(_2\) facets—anatase (101), (100), (112), (001), and rutile (110)—across coverages, using a Ti/O/H ReaxFF parametrization. ReaxFF predicts both molecular and dissociated adsorption motifs whose coverage trends reflect a balance between under-coordinated Ti/O sites, water–surface interactions, and water–water networking. Dissociation extents from MD are compared to prior DFT and experimental literature; trends are broadly consistent. The study highlights a correlation between dissociation propensity and hydrogen-bonding to water outside the first layer, tracked via red-shifting of the O–H stretch of adsorbed water.

## Methods

Grounding: `papers/Raju_TiO2_water_JPC_C_2013_reduced.pdf`; `normalized/extracts/2013raju-venue-jp402139h-2_p1-2.txt` (abstract + early Computational Methods).

### 1 — MD application (ReaxFF interfacial water on TiO₂)

- **Engine / code:** **Molecular dynamics** using the **ReaxFF implementation in the ADF computational chemistry package** (Computational Methods excerpt).
- **System size & composition:** **Water** on **periodic TiO\(_2\)** slabs for **anatase (101), (100), (112), (001)** and **rutile (110)** at multiple coverages (abstract). **Exact atom counts** per supercell are **not stated** on the indexed excerpt pages.
- **Boundaries / periodicity:** **Periodic** **TiO\(_2\)** **slab** models (Computational Methods excerpt).
- **Ensemble:** **NVT** (Computational Methods excerpt).
- **Timestep:** **\(\Delta t = 0.25\) fs** (Computational Methods excerpt).
- **Duration / stages:** **500 ps** total per reported protocol with **100 ps** equilibration and **400 ps** production used to quantify dissociation (Computational Methods excerpt).
- **Thermostat:** **Berendsen** thermostat with **100 fs** coupling constant applied to the **whole system** (Computational Methods excerpt).
- **Barostat:** N/A — **NVT** protocol as stated.
- **Temperature:** **300 K** (abstract).
- **Pressure:** N/A — **not a hydrostatic pressure study** in the excerpted Methods opening.
- **Coverage / staging:** Water placed in **random** initial configurations for coverages **0.50, 0.75, 1.0, 1.5, 2.0, and 3.0 ML**, with **ML** defined relative to **five-fold coordinated Ti** counts as in the paper (Computational Methods excerpt). Additional **vacuum spacing / lateral box / coverage / temperature** checks vs selected **DFT**/**experiment** are described later in the article (same excerpt paragraph opening).
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A.

### 2 — Force-field training

N/A — uses a **recently developed Ti/O/H ReaxFF parameter set** referenced in the excerpt, with standard ReaxFF energy-term exposition (eq. 1 discussion) as **context**; the article’s primary contribution here is **MD application + interpretation**, not a new public parametrization workflow in the p1–2 excerpt.

### 3 — Static QM (literature context)

The Introduction surveys prior **DFT** studies of titania–water interfaces (extract); treat those as **background**, not as the headline production engine for this paper’s new MD dataset.

## Findings

- **Outcomes & mechanisms:** ReaxFF predicts **molecular and dissociative** adsorption motifs vs **coverage** with a **complex water distribution** governed by **adsorption-site spacing**, **water–surface** interactions, and **water–water** interactions (abstract). The work quantifies **dissociation** over surfaces and links **dissociation extent** to **H-bond strength** to water **outside** the first adsorbed layer, evidenced by a **red shift** in adsorbed-water **O–H stretch** modes (abstract).
- **Comparisons:** Abstract claims **agreement** with **prior theoretical studies and experiment** for adsorption motifs, and **general agreement** for **dissociation extents** vs **prior DFT** and **experiments**.
- **Sensitivity / design levers:** Explicit **coverage grid** (**0.50–3.0 ML**) and **facet choice** are the primary comparative axes in the excerpted Methods/abstract framing; **temperature** is fixed at **300 K** in the abstract.
- **Limitations & outlook:** N/A — author limitations are **not captured** on p1–2; read Discussion in `pdf_path`.
- **Corpus honesty:** **`paper:2013raju-venue-jp402139h-2`** is the slug this batch uses for **excerpt-backed integrator details**; other DOI-duplicate PDFs in the corpus should be treated as **variants**, not independent protocols.

## Limitations

- Classical reactive FF errors may accumulate for long trajectories or unusual solvation states.
- Specific quantitative dissociation fractions should be read from the paper tables relative to the DFT references used there.

## Relevance to group

Core **TiO\(_2\)–water interface** application of ReaxFF with van Duin-group parametrization, relevant to photocatalysis, environmental interfaces, and oxide wetting.

## Citations and evidence anchors

- DOI: [10.1021/jp402139h](https://doi.org/10.1021/jp402139h)
- Extract: `normalized/extracts/2013raju-venue-jp402139h-2_p1-2.txt`

## Reader notes (navigation)

- Galley duplicate: [[2013raju-venue-research]]

## Related topics

- [[reaxff-family]]
- Titania–aqueous interfaces and photocatalytic oxides
