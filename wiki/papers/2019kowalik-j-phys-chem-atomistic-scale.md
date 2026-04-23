---
id: paper:2019kowalik-j-phys-chem-atomistic-scale
type: paper
title: "Atomistic Scale Analysis of the Carbonization Process for C/H/O/N-Based Polymers with the ReaxFF Reactive Force Field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:parameterization
  - task:application
  - material:polymer-organic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:thermal-decomposition
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1021/acs.jpcb.9b04298"
year: 2019
authors:
  - "Malgorzata Kowalik"
  - "Chowdhury Ashraf"
  - "Behzad Damirchi"
  - "Dooman Akbarian"
  - "Siavash Rajabpour"
  - "Adri C. T. van Duin"
venue: "The Journal of Physical Chemistry B"
pdf_sha256: "f2db870163892f5aea3531087b7cc29bdb54221b7bce6de0a26fb9a1813091c2"
pdf_path: "papers/Kowalik_JPCB_2019_CHON_polymer.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019kowalik-j-phys-chem-atomistic-scale -->

CHON-2019 extends CHO-2016 with nitrogen parameters fit to DFT so ReaxFF can follow polyacrylonitrile and PBO carbonization, including N₂ release and ring statistics, in ADF-driven reactive MD.

## Summary

The authors develop CHON-2019 by adding nitrogen-containing bond and angle terms to the CHO-2016 ReaxFF baseline using density-functional reference data, with adjustments that remove the valence-angle correction when nitrogen participates (restoring linear HCN) and strengthen the N₂ triple bond relative to CHON-2010. Reactive simulations in the ADF ReaxFF engine study carbonization of ideal ladder polyacrylonitrile (PAN), oxidized PAN, and poly(p-phenylene benzobisoxazole) (PBO) after preequilibration at 300 K, heating at 10 K/ps to 2800 K, and holding 900 ps in NVT to monitor N₂, small gases, and five-, six-, and seven-membered carbon rings as graphitic precursors.

## Methods

### ReaxFF training and QM targets (A)

**CHON-2019** extends **CHO-2016** with **nitrogen** parameters fit to **DFT** data: **N₂** energetics, **N-containing** **bond/angle** terms, and **interactions** of **N₂** with **radicals** formed during carbonization; specific **valence** adjustments include removing the **valence-angle correction** when **N** participates (restoring **linear HCN**) and strengthening the **N₂** triple bond vs older **CHON-2010** behavior (see article/SI).

### Polymer initial structures and equilibration (B)

**Precursors:** ideal **ladder PAN**, **oxidized PAN**, and **PBO** models. Cells are compressed to **~1.6 g/cm³**, **NVT**-equilibrated **100 ps** at **300 K** from independent snapshots; **Figure 3** contrasts **random** vs **aligned** chain packings where discussed.

### Reactive MD carbonization protocol (B)

**ADF** **ReaxFF** **RMD** integration: **Berendsen thermostat** (**100 fs** coupling), **0.25 fs** timestep, **bond-order cutoff 0.3**, **PBC**; **heating** **10 K/ps** to **2800 K**, then **900 ps** **NVT** production (shock **T** exceeds typical **furnace** ramps to increase reaction events in **sub-ns** windows). **System size (atoms)** and **cell** metrics: **PDF** **Tables** / **SI**. **Barostat / servocontrol of pressure:** **N/A** — **NVT** after heating. **Electric field:** **N/A**. **Umbrella / metadynamics / replica exchange:** **N/A** — direct **RMD** only. Visualization in **VMD**.

### Static QM beyond training (C)

**DFT** details for the **training** corpus appear in the article; this paper’s **result** section is **trajectory**-centric.
## Findings

### Mechanisms

**Oxidized PAN** produces **more six-membered rings** than **ladder PAN** under identical protocols—**oxygen** steers early **graphenic** nucleation. **N₂ release** traces differ **ladder** vs **oxidized PAN**; **PBO** differs due to its **heterocyclic** backbone. **5-/7-membered** rings plateau near **500 ps** while **6-membered** rings grow to **~60%** of ring motifs by **900 ps**.

### Limitations

**2800 K** **shock heating** accelerates chemistry beyond **industrial** **carbonization** schedules. Parameter scope follows the **training** chemistry emphasized in the article.

## Limitations

The 2800 K shock heating schedule accelerates chemistry beyond typical furnace pyrolysis and can overestimate reaction rates relative to experiment. Parameter training emphasizes gas-phase kinetics targets, so condensed-phase quantitative agreement should be checked case by case. The abstract and introduction frame CHON-2019 as extending CHO-2016 so nitrogen release and heterocyclic backbone chemistry in aerospace precursors can be followed without switching force fields mid-simulation.

## Relevance to group

**van Duin**-group **CHON** **ReaxFF** for **carbon** **fiber** **precursor** **pyrolysis** **pathways**.

## Citations and evidence anchors

- `papers/Kowalik_JPCB_2019_CHON_polymer.pdf`

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- **Proof** sibling: [[2019kowalik-x-atomistic-scale]] (same **DOI**).
