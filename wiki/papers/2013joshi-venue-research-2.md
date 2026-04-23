---
id: paper:2013joshi-venue-research-2
type: paper
title: "Molecular dynamics study on the influence of additives on the high-temperature structural and acidic properties of ZSM-5 zeolite (galley PDF)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - domain:fuel-combustion
  - method:reaxff
  - material:zeolite-porous
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:silica-silicate
  - keyword:thermal-decomposition
  - keyword:catalysis-surface
source_refs: []
doi: "10.1021/ef3020124"
year: 2013
authors:
  - "Kaushik L. Joshi"
  - "Adri C. T. van Duin"
venue: "Energy & Fuels"
pdf_sha256: "8b16eb394f1ebf04fbbeaf97b689471086e8c519450ef1b367aa3ad40e74dc63"
pdf_path: "papers/Joshi_vanDuin_EnergyFuels2013_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013joshi-venue-research-2 -->

## Evidence and attribution

!!! note "Galley duplicate"

    This ingest registers a **publisher galley/proof** PDF for the same article as **`[[2013josh-venue-ef3020124]]`**. The scientific account below duplicates the **version-of-record** summary.

## Summary

ReaxFF reactive molecular dynamics in the NPT ensemble probes thermal stability and melting-like collapse of ZSM-5 frameworks with different dopants and hydration states, including silicalite, Al- and Fe-doped HZSM-5, hydrated variants, and combinations. A Lindemann-style criterion tracks loss of crystalline pore structure during heating. Network disruption is tied to water-mediated proton transfer to bridging oxygens versus Al/Fe-mediated pathways involving acidic protons and metal migration, including motion of embedded Fe clusters at high temperature. Heating-rate sensitivity is explored by varying hold times after 100 K temperature jumps, showing that slower effective heating lowers apparent melting points toward experimental expectations.

## Methods

Same **Energy Fuels** protocol as **[[2013josh-venue-ef3020124]]**; this slug tracks the **galley** **`papers/Joshi_vanDuin_EnergyFuels2013_galley.pdf`**.

**1 — MD application.** **Reactive molecular dynamics** with **ReaxFF**; **LAMMPS**-class integration as in the **article** (see **VOR** page for engine string). **System:** **ZSM-5** **supercells** spanning **silicalite**, **Al-doped HZSM-5** (**Si/Al ~ 18:1**), **Fe-doped** cells with **Fe\(_{13}\)** clusters, **hydrated** variants, and **Al/Fe/water** combinations—**atom** totals per setup in **PDF** tables. **PBC** **periodic** zeolite cells. **Ensemble:** **NPT** (**abstract**). **Timestep:** **0.25 fs**, **velocity Verlet**. **Stages:** **500 K** **equilibration**; **100 K** heating jumps with **1.25–12.5 ps** holds; **Lindemann** melting criterion (>~3× jump). **Thermostat / barostat:** **Berendsen**-style **NPT** coupling per **`paper_keywords`** and **Methods** narrative—confirm damping in **VOR** **PDF**. **Temperature:** up to **~3500 K** stability window in **abstract**. **Pressure:** **NPT** **hydrostatic pressure** target as in **Methods**. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**.

**2 — Force-field training.** **QM**-referenced **ReaxFF** optimization for **Si/Al/Fe/O/H** (parabolic single-parameter search).

**3 — Static QM.** **N/A** — **QM** supplies training data.


## Findings

Most frameworks remain intact until very high temperature on accessible timescales (the abstract cites stability up to roughly 3500 K before channel collapse). Water promotes Si–O–Si disruption via proton transfer to bridging oxygens, whereas Al/Fe cases emphasize acidic-site chemistry and metal diffusion, including Fe hopping between oxygen sites. Faster heating (shorter holds) yields higher apparent melting temperatures than slower heating, explained by incomplete exploration of phase space near coexistence. Above about 1000 K, cleavage of Al–O(H)–Si linkages forms terminal hydroxyls, reducing Brønsted acidity and weakening the framework relevant to cracking chemistry.

Simulated frameworks include silicalite, Al-doped HZSM-5 with randomized Si/Al near 18:1 and Brønsted protons on bridging oxygens, Fe-doped ZSM-5 hosting a pre-optimized Fe\(_{13}\) cluster, hydrated zeolites, and combined Al/Fe/water permutations, enabling direct comparison of how each additive pathway attacks the aluminosilicate network during the same heating ladder.

## Limitations

Galley PDFs may lack final pagination and figure quality. Nanosecond trajectories still undershoot industrial cracking timescales.

## Relevance to group

van Duin-group **zeolite** **ReaxFF** on thermal stability; this slug tracks publisher **proof** provenance.

## Reader notes (navigation)

- VOR article: [[2013josh-venue-ef3020124]]

## Citations and evidence anchors

- DOI: [10.1021/ef3020124](https://doi.org/10.1021/ef3020124)

## Related topics

- [[reaxff-family]]
