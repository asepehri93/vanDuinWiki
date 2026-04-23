---
id: paper:2012sintering-venue-rsc-cp
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
pdf_sha256: "a02918ca867467640bb63470db41615631e648ce0d3cb935b93bad010098a83a"
pdf_path: "papers/Others/Sintering of calcium oxide (CaO) during CO2 chemisorption_ a reactive molecular dynamics study.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012sintering-venue-rsc-cp -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi` and `pdf_path`.

## Summary

**ReaxFF** **NVE** simulations study **sintering** of two **solid** **CaO** particles **with** and **without** **CO₂** **chemisorption** at **1000 K** and **1500 K** and separations **0.3** and **0.5 nm** (abstract). **Particle expansion** during **CO₂** uptake is attributed to **CaO–CaO** **sintering**; **higher** **adsorption** **temperature** increases **expansion**/**sintering**; **shorter** **separation** yields **faster** **sintering**. Larger **initial** **separation** correlates with **higher** **CO₂** **uptake** via **less** **sintering**. **Regeneration** (**CO₂** **adsorption** on **pre-sintered** **CaO**) is reported **harder** than on **fresh** **CaO**. **MgO** as a **barrier** **reduces** **CaO** **sintering** during **chemisorption** in the model.

**Corpus note:** the same **PCCP** article is ingested as **`[[2012zhang-venue-rsc-cp]]`** (alternate PDF filename).

CaO-based sorbents for CO\(_2\) capture can agglomerate during carbonation, degrading capacity and pressure drop in looping processes. The two-particle **ReaxFF** model isolates how chemisorption-driven neck growth competes with uptake when particles start farther apart, and it probes regeneration on pre-sintered solids versus fresh oxide—qualitative levers for composite pellet design with inert spacers such as **MgO**. Consult **`pdf_path`** and any **Supporting Information** for authoritative tables, figures, and numerical diagnostics.

## Methods


**ReaxFF** **MD** (**NVE** **production**): **spherical** **CaO** (and **MgO** **barrier** cases) **particles** (**r = 1.2 nm**) from **Materials Studio** primitive **cells**; **two** **particles** along **Y** at **D = 0.3 nm** or **0.5 nm** in a **4.5 x 6.0 x 4.5 nm** box with **200** **CO2** molecules (**1544** **atoms** total for the **baseline** **CaO-CaO+CO2** case). **Minimize** then **~10 ps** **equilibration** without **reaction**; **NVE** **60 ps** at **1000 K** or **1500 K**, **Delta t = 0.1 fs**, **trajectory** **every** **200** **steps** (**0.2 ps**). **Pre-sintered** **regeneration** runs use **CaO** **particles** **sintered** in **prior** **NVE** **without** **CO2**.

### MD application (two-particle CaO + CO\(_2\))

**Engine / code:** **Reactive molecular dynamics** with **ReaxFF** (`normalized/extracts/2012sintering-venue-rsc-cp_p1-2.txt`); **N/A —** standalone package name not recovered from the indexed excerpt—verify **`pdf_path`**.

**System size & composition:** Two **spherical** **CaO** particles (**r = 1.2 nm**) from **Materials Studio** primitives, separated by **D = 0.3 nm** or **0.5 nm** along **Y** inside a **4.5 × 6.0 × 4.5 nm** cell with **200** **CO\(_2\)** molecules (**1544** atoms for the baseline **CaO–CaO + CO\(_2\)** case); **MgO** **barrier** variants per article.

**Boundaries / periodicity:** **Three-dimensional periodic** simulation box as sized above (standard **ReaxFF** condensed-phase setup—confirm boundary treatment in **`pdf_path`** if non-cubic symmetries matter).

**Ensemble:** **NVE** for the quoted **production** segments.

**Timestep:** **0.1 fs** with trajectory dumps every **200** steps (**0.2 ps**).

**Duration / stages:** **Energy minimization**, **~10 ps** **equilibration** without reaction, then **60 ps** **NVE** at **1000 K** or **1500 K**; regeneration workflow uses **pre-sintered** particles prepared in prior **NVE** without **CO\(_2\)**.

**Thermostat:** **N/A —** **NVE** production segments do not use a stochastic thermostat; any thermal preparation details are in **`pdf_path`**.

**Barostat / pressure control:** **N/A —** **NPT** barostat not stated for these **NVE** runs.

**Temperature:** **1000 K** and **1500 K** adsorption/sintering conditions in the abstract-level summary.

**Pressure / stress:** **N/A —** external **hydrostatic pressure** control not highlighted in the excerpted protocol.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not used.

### Force-field training

**N/A —** applies a **ReaxFF** parametrization for **CaO**/**CO\(_2\)** chemistry as cited in **`pdf_path`**; this article reports **application** trajectories rather than a new fit.

## Findings

**Outcomes / mechanisms:** **CO\(_2\)** **chemisorption** swells particles and promotes **CaO–CaO** neck **sintering**; **1500 K** runs sinter faster than **1000 K**, and **0.3 nm** gaps sinter sooner than **0.5 nm** gaps under comparable conditions.

**Comparisons:** **Regeneration** (adsorption on **pre-sintered** **CaO**) is harder than on **fresh** **CaO** in the modeled protocol.

**Sensitivity / design levers:** **Adsorption temperature**, initial inter-particle **separation**, and inclusion of **MgO** spacers modulate sintering extent and early **CO\(_2\)** uptake.

**Limitations / outlook:** Idealized **two-particle** geometry and **ReaxFF** chemistry limits are discussed qualitatively in the article; not a full **reactor**/**pellet** model.

**Corpus / KB honesty:** Grounded in **`pdf_path`** and `normalized/extracts/2012sintering-venue-rsc-cp_p1-2.txt`; prefer **`[[2012zhang-venue-rsc-cp]]`** if you need the sibling ingest metadata.

## Limitations

**Idealized** **two-particle** **geometry**; **ReaxFF** for **CaO**/**carbonate** chemistry; not a full **reactor** **pellet** model.

## Relevance to group

**ReaxFF** application to **oxide** **sorbents** and **CO₂** **chemistry**—adjacent to **energy** **materials** modeling.

## Citations and evidence anchors

- DOI **10.1039/c2cp42209c** — *Phys. Chem. Chem. Phys.* **14**, 16633–16643 (2012).
- Extract: `normalized/extracts/2012sintering-venue-rsc-cp_p1-2.txt`.

## Related topics

- [[2012zhang-venue-rsc-cp]]
- [[reaxff-family]]
