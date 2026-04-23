---
id: paper:2014berdiyorov-venue-paper
type: paper
title: "Stabilized silicene within bilayer graphene: A proposal based on molecular dynamics and density-functional tight-binding calculations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reactive-md
  - material:graphene-carbon-nano
  - method:reaxff
  - method:semiempirical-tightbinding
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:lammps
  - keyword:reactive-md
  - keyword:nose-hoover
source_refs: []
doi: "10.1103/PhysRevB.89.024107"
year: 2014
authors:
  - "G. R. Berdiyorov"
  - "M. Neek-Amal"
  - "F. M. Peeters"
  - "Adri C. T. van Duin"
venue: "Phys. Rev. B"
pdf_sha256: "40be519cfdf34eaae337712c0d3e51c19ae2d8d98a6291ba1ca21bc8defec57f"
pdf_path: "papers/Berdiyorov_graph_silicene_PRB_2014.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2014berdiyorov-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. A **proof** duplicate may exist under **`paper:2014berdiyorov-venue-paper-2`**; prefer this entry for the **version-of-record** DOI.

## Summary

**ReaxFF MD** with **DFTB** cross-checks study **Si** **intercalated** between **bilayer graphene**. The abstract argues that **confinement** yields **planar** **Si** clusters that would be **unfavorable** in vacuum, while **larger** clusters adopt **buckled honeycomb** **silicene-like** order **weakly** bound to **graphene** by **vdW** interactions, **stable** **above** **room temperature**. **Higher T** leads to **sp³** **diamond-like** **3D** **Si** **precipitates**. Connections to **epitaxial** **graphene** on **SiC** and **H-storage** ideas are mentioned in the discussion. The **Phys. Rev. B** study is framed as exploring **stabilization** routes for **metastable** **2D Si** motifs that are **hard to isolate** **free-standing**.

## Methods

- **ReaxFF MD (LAMMPS):** **Si/C/H** reactive simulations of **Si** intercalated between **bilayer graphene** (see article for supercell construction). One protocol **randomizes** isolated **Si** positions, then **ramps temperature** at **20 K/ps** from **0 to 2000 K** to mimic high-temperature intercalation and subsequent **quench** behavior. A second protocol **equilibrates**, then **heats** to **2000 K** at **4 K/ps** in an **NPT** ensemble using **Nosé–Hoover** thermostat/barostat; after reaching target **T**, **constant-temperature MD** runs **500 ps** to assess **thermal stability** of **Si** motifs (**Phys. Rev. B** Methods section).
- **DFTB MD:** **Independent** tight-binding dynamics **cross-check** **structural** outcomes (especially **silicene-like** vs **3D Si** motifs) against **ReaxFF**.

**Supercell** **vectors**, **interlayer** **spacing**, **ramp** **rates**, and **diagnostic** **timelines** for **silicene** **formation** are specified in `papers/Berdiyorov_graph_silicene_PRB_2014.pdf` with **comparison** plots to **DFTB**.

**1 — MD application (atomistic dynamics).** **Engine / code:** **LAMMPS** with **ReaxFF** (`normalized/extracts/2014berdiyorov-venue-paper_p1-2.txt` cites **LAMMPS** [37]); **DFTB/MD** cross-checks (**DFTB** as in article). **System:** **Si** intercalated in **AB-stacked bilayer graphene** supercells (article). **Boundaries:** **3D PBC** for **bilayer graphene** sandwich cells; interlayer spacing and in-plane lattice vectors **PDF-grounded**. **Protocols (from article text summarized here):** (i) randomized **Si** positions then **heat 0→2000 K** at **20 K/ps**; (ii) equilibrate, then **NPT** heat to **2000 K** at **4 K/ps** with **Nosé–Hoover** thermostat and barostat, then **500 ps** at target **T** to probe **thermal stability**. **Timestep:** **N/A — not duplicated numerically** on this wiki page (see **Phys. Rev. B** Methods). **Temperature:** ramps to **2000 K** as above; stability **beyond room temperature** discussed in abstract. **Pressure:** **NPT** in the second protocol. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training:** **N/A —** applies **ReaxFF** parameters derived in prior **QM** literature (article framing), not a new fit documented here.

**3 — Static QM / DFT-only:** **N/A —** **DFTB** dynamics are **tight-binding**, not plane-wave **DFT** production runs, though **DFTB** is **QM-derived** (article).

## Findings

- **vdW confinement** between **graphene sheets** stabilizes **planar / lightly buckled Si clusters** that are **high-energy in vacuum**, and can evolve toward **honeycomb silicene-like** order **above room temperature** in the reported simulations.
- **Elevated temperature** drives **Si** toward **sp³-bonded three-dimensional** precipitates inside the **graphene sandwich**, consistent with a **thermally activated** transition away from **metastable 2D Si**.

The **discussion** links **simulated** **pathways** to **possible** **experimental** **signatures** when **Si** is **supplied** under **vdW** **confinement**, while cautioning on **kinetic** **accessibility** versus **ideal** **MD** **heating** **protocols**.

## Limitations

- **ReaxFF** **Si–C** parameter accuracy limits **quantitative** **barriers**; **DFTB** used as a **secondary** test.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

**Adri C. T. van Duin** coauthors; **ReaxFF** application to **2D** **heterostructures** involving **Si** and **graphene**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1103/PhysRevB.89.024107` (`papers/Berdiyorov_graph_silicene_PRB_2014.pdf`).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
