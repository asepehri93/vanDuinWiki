---
id: paper:2012lijuan-meng-j-phys-chem-jp212149c
type: paper
title: "Molecular dynamics simulation of chemical vapor deposition: graphene growth on Ni(111)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:graphene-carbon
  - keyword:berendsen-thermostat
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/jp212149c"
year: 2012
authors:
  - "Meng, Lijuan"
  - "Sun, Qing"
  - "Wang, Jinlan"
  - "Ding, Feng"
venue: "Journal of Physical Chemistry C 116 (11), 6097-6102 (2012)"
pdf_sha256: "b05c29e4ad75938853aa9756254f511e580a8c9a0e26c41b574ef524292f4963"
pdf_path: "papers/ReaxFF_others/Meng_Ding_Ni_graphene_JPCC_2012.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012lijuan-meng-j-phys-chem-jp212149c -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For exact numerical values and figures, use the peer-reviewed article.

## Summary

Classical **molecular dynamics** with a **ReaxFF** parametrization for **C/Ni** is used to study **graphene** evolution and growth kinetics on **Ni(111)** at several temperatures. The abstract reports that **low carbon concentration** favors **dissolution of C into Ni**, while **higher concentration** leads to **graphene island** formation; **defect annealing** near **~1000 K** improves island quality; islands can **grow** by incorporating deposited C and forming **hexagons** at edges with **self-healing**—framed as guidance for **CVD** control.

**Corpus note:** another ingest of the same JPCC article is registered as **`[[2012meng-venue-jp212149c]]`** (alternate PDF path).

## Methods


**Force field and integration:** **ReaxFF** for **C/Ni**, using parameters developed for that system and validated against quantum calculations in the cited training work. **Velocity Verlet** integration with **Δt = 0.25 fs** (chosen for stable energy conservation near **T ~ 1000 K**). **Berendsen** thermostat with **100 fs** damping.

**Surface model:** **Four-layer** **Ni(111)** slab, **256 Ni** total (**64** per layer); in-plane orientation uses **x** ∥ **[110]** and **y** along the **[1̄12]** direction (Miller indices as printed in the article); **~20 Å** vacuum along **z**; periodic boundaries in-plane; **bottom** slab layer **fixed** to mimic a semi-infinite bulk.

**Deposition / conditions:** **16**, **32**, or **64** C atoms (**1/8**, **1/4**, **1/2** of a full graphene monolayer over the cell area), **randomly deposited** on the surface. Annealing temperatures **800**, **1000**, **1200**, and **1400 K**; each (**n** C atoms, **T**) labeled **C_n@T** in the article. **Production trajectories** reported in the article use **100 ps** annealing segments at the stated temperatures for structure evolution (e.g., Figure 1 at **1000 K**).

### MD application (ReaxFF CVD-inspired annealing)

**Engine / code:** **Classical molecular dynamics** with **ReaxFF** (`normalized/extracts/2012lijuan-meng-j-phys-chem-jp212149c_p1-2.txt`); **N/A —** standalone program name not recovered from the indexed excerpt—verify **`pdf_path`**.

**System size & composition:** **Four-layer** **Ni(111)** slab with **256 Ni** atoms (**64** per layer) plus **16**, **32**, or **64** deposited **C** atoms.

**Boundaries / periodicity:** **Periodic boundary conditions** in-plane; **~20 Å** vacuum along **z**; **bottom** **Ni** layer **fixed** to mimic a semi-infinite catalyst.

**Ensemble:** **NVT**-style thermal control via a **Berendsen** thermostat (canonical-sampling intent as described in the article).

**Timestep:** **0.25 fs** (**velocity Verlet**).

**Duration / stages:** **100 ps** segments at **1000 K** for the **C**-structure evolution example in Figure 1; other **C_n@T** combinations follow the article’s schedule.

**Thermostat:** **Berendsen** thermostat with **100 fs** damping constant (Section II of the article).

**Barostat / pressure control:** **N/A —** **NPT** barostat not stated for these slab annealing runs.

**Temperature:** **800**, **1000**, **1200**, and **1400 K** labels for the **C_n@T** survey.

**Pressure / stress:** **N/A —** external **pressure** control not described in the indexed excerpt.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not used.

### Force-field training

**N/A —** this work **applies** an existing **C/Ni** **ReaxFF** parametrization with prior **QM** validation as cited in the article; it does not report a new **ReaxFF** fit in **`pdf_path`**.

## Findings

At **low** C loading (**16** atoms at **1000 K** in the discussion excerpt), C **monomers** favor **subsurface** sites because the **surface → subsurface** barrier is only **~0.6 eV**, so **dimers** on the surface are scarce, whereas **dimers** and **trimers** on the surface can lock **Ni** into **bridging** motifs with **large** effective diffusion barriers. At **higher** C loadings, the paper’s abstract-level summary still applies: **low** concentration tends toward **dissolution** into Ni, **high** concentration drives **graphene island** formation, **~1000 K** is highlighted for **defect annealing**, and islands can **grow** by capturing added C and forming **hexagons** at edges with **self-healing**-like behavior—framed as **kinetic** insight for **CVD** control versus prior **static** nucleation studies.

## Limitations

**ReaxFF** is noted in the article as **less accurate than quantum methods** for the same observables; finite **slab** size, **time** span, and **deposition** protocol bound transferability to industrial **CVD**.

## Relevance to group

Independent **ReaxFF** application to **graphene-on-Ni** growth kinetics; useful alongside group work on **reactive carbon** and **metal** interfaces.

## Citations and evidence anchors

- DOI **10.1021/jp212149c** — *J. Phys. Chem. C* **116**, 6097–6102 (2012).
- PDF: `papers/ReaxFF_others/Meng_Ding_Ni_graphene_JPCC_2012.pdf`; extract: `normalized/extracts/2012lijuan-meng-j-phys-chem-jp212149c_p1-2.txt`.

## Related topics

- [[2012meng-venue-jp212149c]]
- [[reaxff-family]]
- [[graphene-nanocarbon]]
