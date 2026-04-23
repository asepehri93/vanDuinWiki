---
id: paper:2019tingsi-venue-paper
type: paper
title: "ReaxFF study on the effect of CaO on cellulose pyrolysis"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:lammps
  - keyword:berendsen-thermostat
  - keyword:galley-or-proof-pdf
source_refs: []
doi: "10.1021/acs.energyfuels.9b02583"
year: 2019
authors:
  - "Ting Si"
  - "Kai Huang"
  - "Yuyu Lin"
  - "Mingyan Gu"
venue: "Energy & Fuels (2019, Just Accepted manuscript)"
pdf_sha256: "9ca42ed0a339e9a41c2130eab1d3acf34fb70b3c2d87e65637d2093ec8260c79"
pdf_path: "papers/ReaxFF_others/TingSi_CaO_cellulose_acs.energyfuels_2019.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2019tingsi-venue-paper -->

## Summary

**Cellulose pyrolysis** underpins biofuel and biochar technologies; **alkaline-earth oxides** such as **CaO** are known to alter product distributions in experiments, but atomistic mechanisms coupling **solid CaO** to **depolymerization** chemistry are difficult to isolate. This **Energy & Fuels** study uses **ReaxFF molecular dynamics** in **LAMMPS** to compare **neat cellulose** pyrolysis with **CaO-containing** systems, scanning **temperature**, **heating rate**, and **Ca/C mass ratio**. The ReaxFF parameter lineage is traced to **Pitman / van Duin** fits for **C/H/O** organics with extensions for **metal** interactions as described in the manuscript. The local corpus PDF is a **Just Accepted** manuscript; operators should prefer the **final typeset** article for exact figure numbering and any editorial corrections.

## Methods

The cellulose segment is a large glucose-based oligomer of nominal stoichiometry near C\(_{162}\)H\(_{276}\)O\(_{135}\), packed with Packmol to roughly 0.3 g cm\(^{-3}\) in a periodic box near 25 × 25 × 38.82 Å. Supercells add CaO at varying Ca/C while keeping the remaining protocol elements aligned for comparison. Preparation uses annealing and NVT/NVE equilibration before **accelerated heating** ramps; the abstract reports detailed reaction-path analysis for a heating rate of **20 K ps\(^{-1}\)**, and scans over temperature, heating rate, and Ca/C. Production runs in LAMMPS use a ReaxFF description with a Berendsen thermostat (0.1 ps damping in the main text) and the bond-order and charge conventions referenced to the fit for organics with alkali/alkaline-earth elements. The accelerated programs are a computational way to see bond-breaking within nanosecond trajectories; they are not a literal laboratory heating trace.

**Integration time step, total production time per leg, and whether QEq (or other charge model) is advanced each step:** not stated in the two-page local extract; **N/A** for this page—read the *Energy & Fuels* article and SI. **Barostat / NPT servocontrol:** **N/A** if the pyrolysis leg is NVT or NVE without pressure coupling, as the authors report for the fixed-cell ReaxFF runs. **Electric field:** **N/A** — not used. **Shear / shock:** **N/A**. **Metadynamics / replica exchange / umbrella sampling:** **N/A**; chemistry is advanced by the accelerated-temperature program rather than a separate rare-event method.

## Findings

The abstract and introduction-level summary report that higher temperature and faster heating both promote pyrolysis, that adding CaO **accelerates** breakdown versus neat cellulose, and that increasing Ca/C pins more oxygen-containing groups onto the solid, lowering the *net* C–O bond count in the system relative to the Ca-free case. CO and H\(_2\)O counts are reported to **decrease** after CaO is added (relative to the corresponding neat runs). Glycolaldehyde (C\(_2\)H\(_4\)O\(_2\))—a high-oxygen fragment in cellulose pyrolysis—shows a path-dependent response with Ca/C that the main text develops at 20 K ps\(^{-1}\) for a representative case. All numbers are ReaxFF-model outcomes and should be rechecked in the final typeset *Energy & Fuels* file if a Just Accepted–only local PDF was used during ingest.

## Limitations

**Just Accepted** PDF; **accelerated heating** is non-physical; the manuscript notes neglected **density** effects in setup. Confidence is **med** due to ingest status and partial extraction quality.

## Relevance to group

**Biomass pyrolysis** with **Reaxff** including **alkaline-earth oxide** chemistry, connected to the broader **organics pyrolysis** theme in the corpus.

## Citations and evidence anchors

DOI: [10.1021/acs.energyfuels.9b02583](https://doi.org/10.1021/acs.energyfuels.9b02583)

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
