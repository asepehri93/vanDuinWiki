---
id: paper:2013heptane-venue-jp311498u
type: paper
title: "A reactive molecular dynamics study of n-heptane pyrolysis at high temperature (alternate corpus PDF)"
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
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:thermal-decomposition
source_refs: []
doi: "10.1021/jp311498u"
year: 2013
authors:
  - "Ding, Junxia"
  - "Zhang, Liang"
  - "Zhang, Yan"
  - "Han, Ke-Li"
venue: "The Journal of Physical Chemistry A"
pdf_sha256: "a9e68bd79482cfba5ec946fd1153457d121e48281cc2f036f5191260811a1905"
pdf_path: "papers/ReaxFF_others/Heptane_pyrolysis_JPCA_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013heptane-venue-jp311498u -->

Alternate **corpus PDF** bytes for **Ding et al., J. Phys. Chem. A** on ReaxFF pyrolysis of **n-heptane** (**DOI `10.1021/jp311498u`**); one curated science narrative lives on [[2013ding-venue-jp311498u]].

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the publication identified by `doi`. Full section-level detail aligns with [[2013ding-venue-jp311498u]].

## Summary

ReaxFF-based reactive molecular dynamics studies gas-phase pyrolysis of n-heptane at very high simulated temperatures (multi-thousand Kelvin). The work emphasizes a radical-dominated mechanism with unimolecular C–C fission as the principal initiation channel, nonuniform scission along the chain (central C–C bonds preferentially), and qualitative consistency with Rice–Kossiakoff-style organization. Apparent activation energies from simulation kinetics fall near 43–54 kcal mol⁻¹ over the sampled temperature window, described as broadly consistent with experimental high-temperature pyrolysis literature.

The article contrasts single-molecule unimolecular cells with multimolecular periodic boxes to probe bimolecular channels and product distributions, acknowledging that the very high simulated temperatures accelerate chemistry relative to engine-relevant conditions while still allowing comparison to literature pyrolysis product trends.


## Methods

**1 — MD application.** Reactive **molecular dynamics** uses the **ReaxFF** implementation with **C/H/O** parameters from **van Duin** and **Chenoweth** without modification (**papers/ReaxFF_others/Heptane_pyrolysis_JPCA_2013.pdf**; same science as [[2013ding-venue-jp311498u]]). **Engine:** **LAMMPS**-class **RMD** workflow as in the article. **System:** one **n-heptane** molecule (**C₇H₁₆**, **23 atoms**) in a **20 Å** cubic cell for unimolecular pyrolysis; multimolecular boxes pack **16** molecules (total **atom** count scales accordingly) with **PBC**. **Ensemble:** **NVT**. **Timestep:** **0.1 fs**. **Thermostat:** **Berendsen**-style coupling with **0.05 ps** damping as reported. **Temperature:** multi-thousand-**K** pyrolysis window with rate analysis at **2400–3000 K** in the multimolecular workflow. **Species detection:** bond-order cutoff **0.3**. **Barostat / hydrostatic pressure:** **N/A** — **constant-volume** **NVT** legs described above. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A** — brute-force **MD** trajectories (no umbrella/metadynamics/replica exchange summarized here). **Duration:** **ps**/**ns** segment lengths for equilibration vs production as tabulated in the **PDF** (not retyped here).

**2 — Force-field training.** **N/A** — this entry applies the published **C/H/O** **ReaxFF** library; parameter fitting is not the focus of this pyrolysis application paper.

**3 — Static QM.** **N/A** — not the primary methodology for the pyrolysis study summarized here.

## Findings

**Outcomes & mechanisms:** Pyrolysis is **radical**-dominated with **unimolecular** **C–C** fission as the main initiation channel; **central** **C–C** bonds cleave preferentially over terminal bonds in the sampled statistics. **Multimolecular** product distributions overlap key species from **experimental** pyrolysis literature despite higher simulated **temperature**.

**Comparisons:** Apparent **activation** energies **43.02–54.49 kcal mol⁻¹** over **2400–3000 K** are discussed against **experimental** high-**temperature** cracking references in the article.

**Sensitivity / design levers:** **Temperature** window and uni- vs multimolecular cell choice change product channels and inferred kinetics; dense-phase chemistry would require additional intermolecular pathways beyond the gas-phase cells summarized.

**Limitations & outlook:** Very high simulated **temperature** accelerates chemistry relative to engine-relevant conditions; short trajectories may miss slow channels—see authored discussion in the **PDF**.

**Corpus honesty:** This slug is an alternate **corpus** **PDF** for **DOI** `10.1021/jp311498u`; confirm numbers against the **version-of-record** narrative on [[2013ding-venue-jp311498u]] if **pagination** differs.

## Limitations

Two PDFs with different SHA-256 values may reflect publisher layout differences; cite the **DOI**, not a specific file hash, for external scholarship. High temperatures and short timescales limit direct comparison to lower-temperature engine chemistry.

## Relevance to group

Manifest bookkeeping for an alternate acquisition path for the same hydrocarbon ReaxFF pyrolysis reference.

## Citations and evidence anchors

- Published DOI: [10.1021/jp311498u](https://doi.org/10.1021/jp311498u)

## Reader notes (navigation)

- Primary corpus PDF: [[2013ding-venue-jp311498u]].

## Related topics

- [[2013ding-venue-jp311498u]]
- [[theme-pyrolysis-combustion-organics]]
- [[reaxff-family]]
