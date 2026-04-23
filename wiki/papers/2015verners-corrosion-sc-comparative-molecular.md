---
id: paper:2015verners-corrosion-sc-comparative-molecular
type: paper
title: "Comparative molecular dynamics study of fcc-Al hydrogen embrittlement"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - material:alloy-bulk
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:reactive-md
  - keyword:metallic-systems
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.corsci.2015.05.008"
year: 2015
authors:
  - "Osvalds Verners"
  - "George Psofogiannakis"
  - "Adri C. T. van Duin"
venue: "Corrosion Science"
pdf_sha256: "53d713a486a21c81bf690fe6bbf3eef9f45fe0432402a16295fcc0d5486a49ee"
pdf_path: "papers/Verners_AlH_CorrosionScience_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2015verners-corrosion-sc-comparative-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **published** **Corrosion Science** article identified by `doi` and `pdf_path`. Duplicate **proof** ingests: [[2015verners-corrosion-sc-comparative-molecular-2]], [[2015verners-corrosion-sc-comparative-molecular-3]].

## Summary

**Reactive MD (ReaxFF via LAMMPS)** probes **hydrogen embrittlement** in **fcc Al** **nanoslabs** with **oxidized** surfaces and **notched** **Al/Al₂O₃** interfaces, comparing **H** distributions tied to **initial vacancies** vs **random bulk H**. Simulations connect **H diffusion**, **plasticity**, **dislocation** activity, and **void**/ **decohesion** motifs to **environmentally assisted** **failure** scenarios. The **corrosion** framing emphasizes **hydrogen** uptake scenarios that can accompany **oxide**-covered **Al** in **aqueous** or **humid** service environments, translated here into **atomistic** **loading** tests.

## Methods

**LAMMPS ReaxFF** (`papers/Verners_AlH_CorrosionScience_2015.pdf`, §2) simulates a **3D periodic** oxidized **fcc Al** nanoslab (**~15.23 nm × 0.977 nm** in-plane along **[1̄10]** and **[11̄2]**, **~12.34 nm** metal thickness) with **(111)** faces covered by **~1.271 nm** amorphous **Al₂O₃**, a **notch** on one oxide face, and defined **Al/Al₂O₃** stacking. **162 H** atoms are placed either on **162 Al vacancies** (paired) or **randomly in bulk Al** without vacancies—both **strongly supersaturated** cases. **Plane-stress-like** tensile cycling applies **0.25%** strain along **[1̄10]** over **0.5 ps** with **2.5 ps** relaxations at **5 × 10⁻⁶ fs⁻¹** nominal rate, **0.2 fs** timestep, **573 K**, **NPT** with the strained dimension fixed and lateral stresses relaxed to **0 Pa** via **Nosé–Hoover** thermostat (**100 fs** damping) and barostat (**10,000 fs** lateral pressure damping, three-chain volume coupling as referenced). No electric field or enhanced sampling is reported.

**Force-field training:** The study merges published **Al/O**, **Al/H**, **O/H**, and **Al/O/H** ReaxFF subsets (Table 1) and **extends Al/H** with **VASP GGA-PBE PAW** data on **32-atom fcc Al** supercells (**350 eV** cutoff, **9×9×9** **k**-mesh, **Methfessel–Paxton σ = 0.2**) for interstitial **H**, **vacancy–H**, and diffusion-related energies—**targeted augmentation**, not a full new global parametrization. Bulk **Al** elastic and stacking-fault metrics are checked against **DFT** and experiment in the validation table.

**Static QM / DFT:** The **VASP PBE** bulk **Al/H** reference set above supports the ReaxFF extension; there is no separate large-scale non-ReaxFF MD stage.

## Findings

Simulations show **H**-dependent **decohesion**, **void growth**, and **H-enhanced dislocation emission / slip** depending on initial **H** placement and defects (`papers/Verners_AlH_CorrosionScience_2015.pdf`). The abstract reports **vacancy-associated H** lowers **effective H diffusivity** versus **random bulk H**. ReaxFF elastic and fault metrics are compared to **DFT** and experiment in the validation table. Under identical **573 K** cycling, **vacancy-paired vs random bulk H** shifts the balance between plastic and decohesion-dominated failure. The Discussion stresses **nanoscale slab** limits and **ReaxFF** chemistry bounds for macroscopic **hydrogen embrittlement** inference. For numbers and timelines prefer this **version-of-record** PDF; duplicate corpus paths are [[2015verners-corrosion-sc-comparative-molecular-2]] and [[2015verners-corrosion-sc-comparative-molecular-3]].

## Limitations

- **Nanoscale** **slabs** omit **macroscopic** **crack** **plastic zones** and **complex** **microstructures**.
- **ReaxFF** **oxidation**/**hydride** chemistry remains **parameterization-bound**.
- **Strain-rate** and **loading** **mode** choices in **nanoscale** **MD** may not map one-to-one onto **compact-tension** or **fatigue** experiments.

## Relevance to group

**Penn State** **ReaxFF** application to **Al** **hydrogen** **embrittlement** with **industrial** **corrosion** framing.

## Citations and evidence anchors

- **DOI:** `10.1016/j.corsci.2015.05.008` — `papers/Verners_AlH_CorrosionScience_2015.pdf`.

## Related topics

- [[2015verners-corrosion-sc-comparative-molecular-2]]
- [[2015verners-corrosion-sc-comparative-molecular-3]]
- [[reaxff-family]]
