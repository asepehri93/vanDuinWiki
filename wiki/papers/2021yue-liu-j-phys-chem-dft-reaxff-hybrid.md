---
id: paper:2021yue-liu-j-phys-chem-dft-reaxff-hybrid
type: paper
title: "The DFT-ReaxFF Hybrid Reactive Dynamics Method with Application to the Reductive Decomposition Reaction of the TFSI and DOL Electrolyte at a Lithium–Metal Anode Surface"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - method:aimd
  - method:reaxff
  - material:li-metal-anode
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:aimd
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.0c03720"
year: 2021
authors:
  - "Yue Liu"
  - "Peiping Yu"
  - "Yu Wu"
  - "Hao Yang"
  - "Miao Xie"
  - "Liyuan Huai"
  - "William A. Goddard III"
  - "Tao Cheng"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "9119a4fb1546c9806df8218cdea6cb1428f96727d8d8c57ddb5c13b18be9605a"
pdf_path: "papers/ReaxFF_others/Liu_AIMD_REaxFF_jpclett_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2021yue-liu-j-phys-chem-dft-reaxff-hybrid -->

## Summary

**Lithium metal** anodes promote electrolyte reduction, **solid-electrolyte interphase (SEI)** nucleation, and ongoing electrolyte consumption chemistry that controls safety and cycle life. **Ab initio molecular dynamics (AIMD)** can capture early bond-breaking events with high fidelity but rarely reaches **nanosecond** cumulative times needed to see coupling between multiple solvent fragments and salt anions near the electrode. This *Journal of Physical Chemistry Letters* paper introduces **HAIR** (**H**ybrid **AI**MD + **R**eaxFF), a protocol that **interleaves** AIMD segments with **ReaxFF** reactive MD segments to extend accessible simulated time by about an **order of magnitude** relative to AIMD-only trajectories while preserving quantum accuracy in the windows where electronic-structure errors would be largest.

## Methods

**1 — MD application (HAIR: AIMD + ReaxFF).** The authors introduce **HAIR** (**H**ybrid **AI**MD + **R**eaxFF): **AIMD** segments for accuracy where **bond making/breaking** and **reduction** of **TFSI** and solvent matter, with **ReaxFF** **LAMMPS**-style **reactive MD** **interspersed** to extend cumulative time. The **abstract** states the hybrid extends accessible time **by a factor of ~10×** compared with **AIMD**-only, enabling chemistry toward the **~1 ns** range relevant to **SEI** inception that **AIMD** alone cannot reach. **System:** **Li** **metal** surface with **LiTFSI** in **1,3-dioxolane (DOL)**. The protocol uses **PBC** slab/cell models and **NVT**-style **AIMD** in the **QM** legs with **ReaxFF** in the **classical** legs (see article). **Ensemble, timestep, thermostat, ReaxFF schedule, total trajectory length:** **N/A in this short wiki note** — full DFT **functional**/**basis**, **Nose**–**Hoover** or related **thermostat** parameters, and **handoff** **cadence** are in *J. Phys. Chem. Lett.* **Methods** and **SI** (p1-2 extract does not list every numerical). **Temperature:** **N/A in the indexed p1-2 extract**; use the version-of-record **Methods/SI** for explicit **K** values used in AIMD and hybrid segments. **Barostat / pressure control:** **N/A** in typical confined electrode cells — see **PDF** for any anisotropic or **NPT** use. **Electric (bias) field:** **N/A** in abstract-level summary. **Shear / shock / umbrella / metadynamics:** **N/A** — not the stated focus.

**2 — Force-field training.** **N/A** as a new **ReaxFF** fit paper — the work **applies** an existing **ReaxFF** parametrization for this electrolyte class together with **AIMD**; parameter provenance in the article.

**3 — Static QM (AIMD block).** **DFT**-based **AIMD** in the **QM** windows: **functional, basis, k-sampling, charge/spin, timestep** in **AI**MD — **N/A to duplicate here**; use the **PDF**.

**4 — Experiments.** **N/A** for new lab work in this paper; **DOL** products are compared to **experimental** reports in the text.

## Findings

**Outcomes and mechanisms.** **HAIR** reproduces **TFSI** **decomposition** seen in prior **AIMD** and, with extended sampling, also captures **DOL** reactivity, including **ring-opening** to products such as **CO**, **CH₂O**, and **C₂H₄** that the authors connect to **experiment** (abstract). The central claim is **methodological**: a **hybrid** schedule can increase simulated **reactive** time toward **SEI** timescales while **retaining** **AIMD** where the force field would be least trustworthy.

**Comparisons, sensitivity, outlook.** **N/A** in this note to restate all **AIMD**-only vs **HAIR** **baselines** and every **T**/**coverage** point — the letter text and **SI** hold the quantitative comparison. **Corpus honesty:** the local p1–2 extract states the main **HAIR** claims; barrier heights and full product statistics require the **version-of-record** **PDF**/**SI**.

## Limitations

Windowing between AIMD and ReaxFF requires **validation** for each new chemistry (salt, solvent, additives); transferability is not automatic across electrolyte formulations.

## Reproducibility notes

HAIR studies should log **AIMD/DFT** settings (functional, timestep, thermostat) and the **handshake** geometry at each switch point, because small strain or surface reconstruction differences can alter subsequent ReaxFF chemistry. For **Li metal**, slab thickness and **dipole** corrections can interact with electrolyte polarity—note whether the published protocol used **charged** cells or neutral fragments.

Because **DOL** chemistry includes **ring-opening** and **radical-like** intermediates depending on reduction stage, archive the **oxidation state** assumptions implicit in the ReaxFF parameterization for oxygen-bearing fragments; mismatches between QM and ReaxFF oxidation states at handoff are a common hidden failure mode in hybrid workflows. Where possible, attach **trajectory snippets** at handoff frames showing **energy** continuity checks between AIMD and ReaxFF segments for the same nuclear geometry.

## Reader notes (navigation)

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
