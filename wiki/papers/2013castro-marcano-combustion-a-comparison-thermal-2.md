---
id: paper:2013castro-marcano-combustion-a-comparison-thermal-2
type: paper
title: "Comparison of thermal and catalytic cracking of 1-heptene from ReaxFF reactive molecular dynamics simulations (Elsevier author proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:combustion
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:lammps
source_refs: []
doi: "10.1016/j.combustflame.2012.12.007"
year: 2013
authors:
  - "Castro-Marcano, Fidel"
  - "van Duin, Adri C. T."
venue: "Combustion and Flame"
pdf_sha256: "745724fc7f003929f0173dc8d1cabafa7e2af918656a8d72b34394c572d7d18a"
pdf_path: "papers/Castro_CombFlame_heptene_proof_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013castro-marcano-combustion-a-comparison-thermal-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    This PDF is an **Elsevier author proof** with **query forms** and **line numbers**. Prefer **`[[2013castro-marcano-combustion-a-comparison-thermal]]`** for stable pagination and the **issue** text.

!!! abstract "Corpus role"

**Elsevier author proof** of the **Combustion and Flame** **1-heptene** cracking paper; same DOI as the **online** article page.

## Summary

This ingest is an **Elsevier author proof** PDF (query sheet **Q1/Q2** on author names and heading hierarchy) for **Castro-Marcano & van Duin**, *Combustion and Flame*, studying **ReaxFF reactive molecular dynamics** of **1-heptene** cracking over **amorphous silica**, **hydrated amorphous silica**, and **amorphous aluminosilicate** nanoparticles at **1750, 1850, and 1950 K** (DOI [10.1016/j.combustflame.2012.12.007](https://doi.org/10.1016/j.combustflame.2012.12.007)). The **abstract** motivates **endothermic catalytic cracking** for **thermal management** in high-speed engines: regenerative cooling may require **additional heat sink** beyond sensible heating, which **hydrocarbon cracking** can supply, but mechanisms remain incompletely resolved. Simulations use **large interface systems (~2250 atoms)** with **~100 heptene molecules** surrounding an oxide particle (**extract**). The maintained technical narrative and stable pagination for citation are on **`[[2013castro-marcano-combustion-a-comparison-thermal]]`** (version of record).

## Methods

The **abstract** specifies **ReaxFF** simulations at three temperatures on the large **oxide–hydrocarbon** interfaces described above. The **introduction** contrasts **thermal** vs **catalytic** cracking contexts (including **supercritical** fuel pressures **~4–7 MPa** relevant to cooling circuits) and notes that **alkene** initiation can involve **carbenium-ion** pathways under **refinery** conditions, whereas **high-pressure** **supercritical** regimes differ. **LAMMPS** integration with **Chenoweth-type** **C/H/O** **ReaxFF** parameters, **0.25 fs** timestep, **Berendsen** thermostats, and **~5000 ps** production segments are recorded on the **VOR** page; this **proof** may differ in **lineation** and contains **publisher queries**, not additional science.

**1 — MD application (atomistic dynamics; consolidated with [[2013castro-marcano-combustion-a-comparison-thermal]] where this proof omits tables):**

- **Engine / code:** **LAMMPS** for **ReaxFF** reactive **molecular dynamics** using the **C/H/O** parameterization cited on the VOR page.
- **System size & composition:** Order **~2250 atoms** with on the order of **~100** **1-heptene** molecules surrounding an **amorphous** **oxide** nanoparticle (**silica**, hydrated silica, or **aluminosilicate** variants per the abstract).
- **Boundaries / periodicity:** **Three-dimensional periodic boundary conditions** (**PBC**) on the simulation supercell (condensed-phase **ReaxFF** setup consistent with the cubic-cell description on the VOR page).
- **Ensemble:** **NVT**-style constant-volume high-temperature sampling with **Berendsen** thermostat coupling as summarized on the VOR page (**N/A** for any separate **NPT** production leg if not reproduced in this proof excerpt).
- **Timestep:** **0.25 fs** integration step (VOR page).
- **Duration / stages:** **~5000 ps** production segments after staged heating (VOR page); exact ramp tables may differ between **proof** and **issue** PDFs.
- **Thermostat:** **Berendsen** thermostat with the damping/time constant quoted on the VOR page.
- **Barostat:** **N/A** — production protocol summarized as **constant-volume** **NVT** **MD** without Parrinello–Rahman **pressure** control.
- **Temperature:** **1750 K**, **1850 K**, and **1950 K** production windows from the abstract.
- **Pressure:** **N/A** — no hydrostatic **pressure** target stated for the **NVT** production segments in the proof extract (the introduction motivates **MPa**-scale **supercritical** fluid **pressure** as physical context for engines, distinct from the MD barostat coupling).
- **Electric field:** **N/A** — no applied **electric field** in the protocol described.
- **Replica / enhanced sampling:** **N/A** — no umbrella sampling, metadynamics, or replica exchange reported.

**2 — Force-field training:** **N/A** — published **ReaxFF** parameter set application (no new **parameterization** workflow central to this article).

**3 — Static QM:** **N/A** — not the focus of the summarized protocol.

## Findings

**1 — Outcomes & mechanisms:** Per the **abstract** (proof extract), **heptene** cracking proceeds through a **complex reaction network** producing **hydrogen** and **C\(_1\)–C\(_7\)** hydrocarbon products. **Trajectory analysis** distinguishes **initiation chemistry** for **thermal** vs **catalytic** pathways: **thermal** cracking is described as initiated primarily by **C–C bond scission** followed by **free-radical** propagation, whereas **catalytic** cracking emphasizes **C–C scission** together with **protonation** and **dehydrogenation** at the **oxide** interface.

**2 — Comparisons:** Product families are described as **consistent with experimental** hydrocarbon **cracking** **literature** at a qualitative level in the abstract framing.

**3 — Sensitivity & design levers:** The study scans **oxide** composition (dry vs hydrated silica vs aluminosilicate) and **temperature** (**1750–1950 K**) as the primary simulation **levers** called out in the abstract.

**4 — Limitations & outlook (as authored / editorial):** The abstract positions **ReaxFF** as a tool for **complex** high-temperature chemistry while leaving quantitative benchmarking to the full article discussion; **proof** PDFs may carry **publisher queries** unrelated to additional science.

**5 — Corpus / KB honesty:** This page is an **Elsevier author proof** PDF; **pagination** and **lineation** may differ from the **version-of-record** PDF. For **quantitative** product distributions, **reaction graphs**, and stable locators, use **`[[2013castro-marcano-combustion-a-comparison-thermal]]`** rather than inferring from **query-sheet** pages here.

## Limitations

**Proof** PDFs can differ in **layout**, **figure** placement, and **minor** wording from the **final** issue; **query sheets** are not citable content.

## Relevance to group

Workflow duplicate for the **van Duin** co-authored **aviation-fuel-relevant** **ReaxFF** cracking study.

## Citations and evidence anchors

- DOI: [10.1016/j.combustflame.2012.12.007](https://doi.org/10.1016/j.combustflame.2012.12.007)

## Reader notes (navigation)

- Version of record: [[2013castro-marcano-combustion-a-comparison-thermal]]

## Related topics

- [[2013castro-marcano-combustion-a-comparison-thermal]]
- [[theme-pyrolysis-combustion-organics]]
- [[reaxff-family]]
