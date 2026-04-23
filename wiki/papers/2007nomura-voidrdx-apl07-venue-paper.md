---
id: paper:2007nomura-voidrdx-apl07-venue-paper
type: paper
title: "Reactive nanojets: Nanostructure-enhanced chemical reactions in a defected energetic crystal"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:shock-compression
  - keyword:energetic-materials
  - keyword:method-development
  - keyword:reactive-md
canonical_tags:
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.2804557"
year: 2007
authors:
  - "Ken-ichi Nomura"
  - "Rajiv K. Kalia"
  - "Aiichiro Nakano"
  - "Priya Vashishta"
venue: "Applied Physics Letters 91, 183109 (2007)"
pdf_sha256: "a9b03b6e9b9396b64c059ba02d2c40bbf6a38b64e090ac1b7897d40490266584"
pdf_path: "papers/ReaxFF_others/Nomura-VoidRDX-APL07.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2007nomura-voidrdx-apl07-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **Applied Physics Letters** article identified by `doi`. Shock speeds, timings, and velocities are taken from the **abstract and extract** as printed.

## Summary

The authors report **million-atom** reactive MD of **shock initiation** in an **RDX** single crystal containing a **nanometer-scale spherical void**, using **REAXFF** with a **fast reactive force field (F-REAXFF)** algorithm for large-scale parallelism. Planar shocks with particle velocities **\(V_p = 1\)** and **\(3\ \mathrm{km\,s^{-1}}\)** interact with an **8 nm diameter** void in a setup described in the paper. Simulations show a **nanojet** that **focuses** past the void, **void-assisted** chemistry beyond the **perfect-crystal** case, and a **pinning–depinning** **shock front** at the void with a related **localization–delocalization** pattern in **vibrational energy** when **\(V_p\)** increases.

## Methods


The study uses **million-atom** **F-REAXFF** (fast parallel ReaxFF) MD with **bond orders** and **charge equilibration** as in the authors’ prior ReaxFF framework. The sample is a **single-crystal RDX** (C\(_3\)H\(_6\)O\(_6\)N\(_6\)) slab with an **8 nm**-diameter spherical **void** (molecules removed within **4 nm** of the cell center); crystal axes align with \([100]\), \([010]\), \([001]\). After introducing the void, the system is relaxed **3.5 ps** at **5 K**; **periodic** boundaries along **\(y,z\)** are then removed to expose **\(yz\)** free surfaces, followed by **2 ps** at **5 K**. The full box (including vacuum) measures **358.50 \(\times\) 213.06 \(\times\) 203.82** Å\(^3\). **Planar shocks** along \([100]\) use a **momentum mirror** and initial bulk translation **\(-V_p\)** toward the mirror, with **\(V_p = 1\)** and **\(3\)** km s\(^{-1}\). The short **APL** letter does **not** state the integration timestep or MD software build in the extracted text. Analysis covers molecular **velocity** fields, **shock-front** pinning/depinning, **jet** speeds, **vibrational temperature** maps, and **fragment** populations (bond order \(> 0.3\) for connectivity).

**MD checklist (letter + extract):** **molecular dynamics** at **million-atom** scale with **F-REAXFF**; **N/A — specific MD package** name in the indexed excerpt. **System:** **RDX** crystal with **~million atoms** in the cell dimensions quoted above. **Boundaries:** **periodic** along shock propagation initially, then **non-periodic** **\(yz\)** faces after cutting **PBC** as described. **Ensemble / thermostat / barostat:** **N/A — NVE/NVT/NPT** labels and **thermostat** details not stated for the shock drive in the short extract (relaxation segments at **5 K** are time-stamped). **Timestep:** **N/A — \(\Delta t\)** not in the indexed letter text. **Duration / stages:** **3.5 ps** + **2 ps** relaxation windows quoted; shock interaction times **~2–5 ps** discussed in figure captions—see PDF. **Temperature:** **5 K** relaxation; post-shock **vibrational temperature** fields analyzed. **Pressure / stress:** **shock** loading via **\(V_p\)** (**1** and **3 km s\(^{-1}\)**), not hydrostatic **NPT**. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**.

## Findings

When the shock reaches the void, molecules jet from the upstream wall, focus into a narrow beam, and strike the downstream wall; maximum jet speeds reach about 3 km s\(^{-1}\) at \(V_p = 1\) km s\(^{-1}\) and about 9 km s\(^{-1}\) at \(V_p = 3\) km s\(^{-1}\), exceeding the \(\sim 2V_p\) ejection speed expected for a planar surface because of void geometry and jet focusing. The shock front exhibits pinning versus depinning: at \(V_p = 1\) km s\(^{-1}\) the front bends around the void (about 3.2–5 ps in the figure discussion) before bypassing it, whereas at \(V_p = 3\) km s\(^{-1}\) the front remains straighter while crossing the void (about 2.0–3.2 ps), and jet molecules can catch up with the shock. After collapse a ring-shaped secondary shock emanates from the void. Localized vibrational heating accompanies jet flow into the void, supporting **hotspot** formation and **enhanced chemistry** relative to a perfect crystal without void-mediated collisions. **Corpus honesty:** `extraction_quality` is **partial**; confirm timings and fields in **`pdf_path`**.

## Limitations

- `extraction_quality` is **partial** in the normalized record; rely on the PDF for figure-accurate timings and field maps.
- Reactive FF shock chemistry involves strong **extrapolation**; quantitative reaction pathways should be traced to the article’s analysis sections.

## Relevance to group

Demonstrates **large-scale ReaxFF-class reactive dynamics** for **energetic materials** under shock loading—adjacent to the group’s reactive MD interests even though authorship is external.

## Citations and evidence anchors

- DOI: `10.1063/1.2804557` (cleaned from manifest artifacts).
- PDF: `papers/ReaxFF_others/Nomura-VoidRDX-APL07.pdf`.
- Extract: `normalized/extracts/2007nomura-voidrdx-apl07-venue-paper_p1-2.txt`.

## Related topics

- [[reaxff-family]]
