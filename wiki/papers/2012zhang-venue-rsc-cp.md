---
id: paper:2012zhang-venue-rsc-cp
type: paper
title: "Sintering of calcium oxide (CaO) during CO2 chemisorption: a reactive molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:nve-simulation
  - keyword:reactive-md
source_refs: []
doi: "10.1039/c2cp42209c"
year: 2012
authors:
  - "Zhang, Luzheng"
  - "Lu, Yongqi"
  - "Rostam-Abadi, Massoud"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "6cf3aded50e5cb0e2c40975721c5b84d83afeb5033e3b1da7c775cd100f9cef7"
pdf_path: "papers/Others/Zhang_CO2_CaO_PCCP_2012.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012zhang-venue-rsc-cp -->

!!! note "Duplicate PDF registration"

    This slug uses **`papers/Others/Zhang_CO2_CaO_PCCP_2012.pdf`**, a **duplicate path** for the same **PCCP 2012** article as **`[[2012sintering-venue-rsc-cp]]`**. Consolidate manifest entries when feasible; cite **one** `pdf_path` for hygiene.

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi` and `pdf_path`.

## Summary

Calcium oxide is a classical high-temperature CO\(_2\) sorbent, but repeated carbonation–calcination cycles can degrade performance through **particle sintering** and loss of reactive surface area. This **Physical Chemistry Chemical Physics** study uses **ReaxFF** reactive molecular dynamics in the **NVE** ensemble to simulate **two CaO nanospheres** (radius **1.2 nm**) separated by a fixed gap in the presence of CO\(_2\) at **1000 K** or **1500 K**. The simulations show **CO\(_2\)**-driven **neck formation** and **particle expansion** consistent with chemisorption-induced sintering, quantify how **temperature** and **initial separation** alter sintering rate and early CO\(_2\) uptake, and explore **MgO** barriers and **pre-sintered** morphologies as mitigations. The work frames regeneration penalties when sorbents **sinter** during operation.

The **nanoparticle** geometry is intentionally small to make **neck** formation and **carbonation** events observable within **picosecond** trajectories; the authors interpret trends as **mechanistic** indicators rather than **quantitative** **pellet** kinetics at engineering scales.

## Methods


**Geometry.** Two CaO spheres (**r = 1.2 nm**) placed with center-to-center separations **D = 0.3** or **0.5 nm**; simulation cell **4.5 × 6.0 × 4.5 nm** with **200 CO\(_2\)** molecules as stated in the article.

**Protocol.** Energy minimization, short preequilibration (~10 ps), then **NVE** production for **60 ps** with **Δt = 0.1 fs** at **1000 K** or **1500 K**.

**Variants.** Additional runs insert **MgO** barriers between particles and study **readsorption** on **pre-sintered** solids as reported in the main text.

**Reproducibility detail.** Preserve **NVE** microcanonical conditions when comparing runs; switching to **thermostatted** ensembles would change how **exothermic** **carbonation** localizes **temperature** and can alter **sintering** kinetics. Use the same **ReaxFF** parameterization for **Ca–C–O** chemistry as referenced in the article, and verify **CO\(_2\)** **count** and **density** match the published **cell** setup.

### Force-field training

**N/A —** this work **applies** an existing **ReaxFF** parameterization for **Ca–C–O** chemistry (cited in the article); it does **not** report a new **QM** fit in the indexed abstract (`normalized/extracts/2012zhang-venue-rsc-cp_p1-2.txt`).

### MD application (integrated)

**Engine / code:** **Reactive molecular dynamics** with **ReaxFF** (abstract). **N/A —** specific MD engine (e.g. **LAMMPS**) **not** named on the indexed excerpt pages—confirm in **`pdf_path`**.

**System & composition:** Two solid **CaO** nanoparticles modeled as spheres of radius **1.2 nm**, initial center-to-center separations **0.3** and **0.5 nm**, with **CO\(_2\)** present; simulation cell **4.5 × 6.0 × 4.5 nm** with **200 CO\(_2\)** molecules (article body cited on this page).

**Boundaries / periodicity:** **N/A —** full **PBC** description not recovered from the short excerpt; see **`pdf_path`**.

**Ensemble:** **NVE** (abstract).

**Timestep:** **0.1 fs** (article Methods on this page).

**Duration / stages:** Energy minimization, **~10 ps** preequilibration, then **60 ps** **NVE** production (this page); see PDF for any additional staging.

**Thermostat / barostat:** **N/A —** no thermostat or **NPT** barostat (**NVE** production).

**Temperature:** Initial adsorption / sintering conditions explored at **1000 K** and **1500 K** (abstract).

**Pressure:** **N/A —** not stated for these **NVE** nanosphere runs in the indexed text.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not used.

## Findings

**Outcomes:** **CO\(_2\)** drives **particle expansion** and **neck sintering** between **CaO** particles; higher **temperature** (**1500 K** vs **1000 K**) increases expansion and sintering, and a **shorter** initial gap (**0.3** vs **0.5 nm**) yields a **faster** sintering rate during adsorption (abstract). A **larger** separation can yield **greater early CO\(_2\)** uptake because **less** sintering occurs initially (abstract). **Regeneration** (decarbonation) is **harder** for particles already **sintered** at high adsorption **temperature** than for fresh particles (abstract). **MgO** barriers **reduce** **CaO–CaO** sintering in the configurations tested (abstract).

**Comparisons:** Trends are discussed relative to **experimental** motivation on **multi-cycle** **CaO** sorbents in the introduction (full **PDF**).

**Sensitivity:** **Temperature**, **initial particle separation**, **MgO** spacer, and **pre-sintered** morphology.

**Limitations:** **60 ps**, **nanometer**-scale spheres are **early-stage** probes, not reactor-scale pellet kinetics; **ReaxFF** transferability bounds chemistry details.

**Corpus / KB honesty:** Duplicate registration with **`[[2012sintering-venue-rsc-cp]]`**; this slug uses `papers/Others/Zhang_CO2_CaO_PCCP_2012.pdf`—keep manifests consistent.

## Limitations

Nanoscale spherical models and picosecond trajectories capture early-stage kinetics, not reactor-scale pellet mechanics; ReaxFF parameter scope bounds transferability.

## Relevance to group

CO\(_2\) capture **ReaxFF** application; duplicate corpus path only.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1039/c2cp42209c](https://doi.org/10.1039/c2cp42209c) (`papers/Others/Zhang_CO2_CaO_PCCP_2012.pdf`).
- Extract: `normalized/extracts/2012zhang-venue-rsc-cp_p1-2.txt`.
**Duplicate PDF.** Same PCCP article as `[[2012sintering-venue-rsc-cp]]`; use one path for citations.

## Related topics

- [[2012sintering-venue-rsc-cp]]
- [[reaxff-family]]
