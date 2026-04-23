---
id: paper:2012meng-venue-jp212149c
type: paper
title: "Molecular dynamics simulation of chemical vapor deposition: graphene growth on Ni(111)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1021/jp212149c"
year: 2012
authors: []
venue: "Journal of Physical Chemistry C"
pdf_sha256: "18b83c002592c88b8d6751e03b53a570011b04a9a9e57ae59239b2937455fa81"
pdf_path: "papers/ReaxFF_others/Meng_Ni_graphene_JPC_2012.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012meng-venue-jp212149c -->

ReaxFF MD on a four-layer Ni(111) slab explores carbon coverage, annealing temperature, and edge-limited graphene island growth during a CVD-inspired setup.

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi` and `pdf_path`. Prefer **`[[2012lijuan-meng-j-phys-chem-jp212149c]]`** for author-resolved front matter when both pages describe the same article.

## Summary

**Corpus note:** this slug uses **`papers/ReaxFF_others/Meng_Ni_graphene_JPC_2012.pdf`**; the same **JPCC 2012** work is curated under **`[[2012lijuan-meng-j-phys-chem-jp212149c]]`** with full author metadata. The paper applies **ReaxFF** **MD** to **graphene** **CVD** on **Ni(111)**, reporting **concentration-dependent** C behavior (**dissolution** vs **island** formation), **defect annealing** near **~1000 K**, and **island growth** with **edge hexagon** formation and **self-healing**. The study belongs to the broader literature on catalytic graphene growth where carbon supply rate and substrate solubility jointly determine whether carbon resides in solution versus precipitates as flakes.

## Methods


Same article as **`[[2012lijuan-meng-j-phys-chem-jp212149c]]`**; methodology in the **PDF** (`pdf_path`): **ReaxFF** **C/Ni** (**velocity Verlet**, **Delta t = 0.25 fs**; **Berendsen** thermostat, **100 fs** damping). **Surface:** **four-layer** **Ni(111)** slab, **256 Ni** total, **x** along **[110]**, **y** along **[1-12]** (Miller indices as printed), **~20 A** vacuum along **z**, **bottom** layer **fixed**. **Deposition:** **16**, **32**, or **64** **C** atoms (**1/8**, **1/4**, **1/2** monolayer coverage), random placement; annealing labels **C_n@T** with **T = 800**, **1000**, **1200**, **1400 K**. Representative production segments include **100 ps** trajectories at **1000 K** in **Figure 1** of the article. Coverage sweeps isolate how much carbon remains on the surface after annealing versus how much has dissolved into the Ni slab at each temperature label.

### MD application (same article as `[[2012lijuan-meng-j-phys-chem-jp212149c]]`)

**Engine / code:** **Classical molecular dynamics** with **ReaxFF**; **N/A —** standalone program name not repeated on this duplicate ingest page—see sibling note and **`pdf_path`**.

**System size & composition:** **Four-layer** **Ni(111)** slab, **256 Ni** atoms, with **16/32/64** **C** atoms deposited randomly.

**Boundaries / periodicity:** In-plane **PBC**, **~20 Å** vacuum along **z**, **bottom** layer **fixed**.

**Ensemble:** **NVT** with **Berendsen** thermal control (as in Section II of the article).

**Timestep:** **0.25 fs** (**velocity Verlet**).

**Duration / stages:** **100 ps** evolution segments at **1000 K** for Figure 1–style comparisons; full matrix of **C_n@T** runs in **`pdf_path`**.

**Thermostat:** **Berendsen** with **100 fs** damping constant.

**Barostat / pressure control:** **N/A —** **NPT** not stated for these slab runs.

**Temperature:** **800–1400 K** annealing labels.

**Pressure / stress:** **N/A —** not a controlled variable in the excerpted description.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not used.

### Force-field training

**N/A —** applies published **C/Ni** **ReaxFF** parameters (see sibling page for citations).

## Findings

**Outcomes / mechanisms:** At low **C** coverage, **C** adatoms tend to dissolve into **Ni**, whereas higher coverages nucleate **graphene** islands. **Defect annealing** is most efficient near **~1000 K** in the surveyed setups. **Island growth** proceeds by capturing newly deposited **C** at edges with **hexagon** formation and local **self-healing** rearrangements.

**Comparisons:** The article contrasts **low** vs **high** **C** concentration behavior and relates **MD** observations to prior **static** nucleation literature (see **`pdf_path`**).

**Sensitivity / design levers:** **Temperature** (**800–1400 K** labels) and **C** loading (**16/32/64** atoms) jointly control whether **C** remains in solution, nucleates islands, or anneals defects.

**Limitations / outlook:** **ReaxFF** accuracy vs **QM** and finite **slab/time** approximations are discussed in the article; see sibling **`[[2012lijuan-meng-j-phys-chem-jp212149c]]`** for the fuller limitation paragraph.

**Corpus / KB honesty:** Duplicate **PDF** ingest (`pdf_path` differs from the sibling page); scientific claims should be checked against **`papers/ReaxFF_others/Meng_Ni_graphene_JPC_2012.pdf`** and/or the sibling **`[[2012lijuan-meng-j-phys-chem-jp212149c]]`** entry.

## Limitations

Duplicate PDF path in corpus; scientific limits are as discussed on the sibling page (**ReaxFF** accuracy, finite **MD** setup).

## Relevance to group

Duplicate bundle for an external **graphene CVD** **ReaxFF** study.

## Citations and evidence anchors

- DOI **10.1021/jp212149c**.
- Extract: `normalized/extracts/2012meng-venue-jp212149c_p1-2.txt`.

## Related topics

- [[2012lijuan-meng-j-phys-chem-jp212149c]]
- [[reaxff-family]]

