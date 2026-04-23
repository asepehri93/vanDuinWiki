---
id: paper:2018chen-nat-nanomanufacturing-silicon
type: paper
title: "Nanomanufacturing of silicon surface with a single atomic layer precision via mechanochemical reactions"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - material:widegap-semiconductor
  - method:classical-md
  - task:experiment-integrated
paper_keywords:
  - keyword:tribology
  - keyword:water-interfaces
  - keyword:validation-experiment
  - keyword:lammps
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1038/s41467-018-03930-5"
year: 2018
authors:
  - "Lei Chen"
  - "Jialin Wen"
  - "Peng Zhang"
  - "Bingjun Yu"
  - "Cheng Chen"
  - "Tianbao Ma"
  - "Xinchun Lu"
  - "Seong H. Kim"
  - "Linmao Qian"
venue: "Nature Communications 9, 1542 (2018)"
pdf_sha256: "adcf8cca3b16baad4bd47cc023372dc05b7ed195be87997fff4f57e5022358f3"
pdf_path: "papers/ReaxFF_others/Chen, Wen et al., Nanomanufacturing of silicon surface with a single atomic layer precision via mechanochemical reactions, Nature Communications, 2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018chen-nat-nanomanufacturing-silicon -->

## Summary

Mask-free scanning-probe patterning can reshape silicon surfaces with nanometer precision, offering localized engineering without photolithography masks. Chen et al. (*Nat. Commun.* **9**, **1542**, **2018**) report humidity-controlled scanning-probe wear on single-crystal Si(100) in which a nanoscale water film mediates shear-driven mechanochemistry that removes approximately one atomic layer per pass under gentle loading. The experimental campaign spans controlled humidity, normal load, and scan speed windows that separate mild tribochemical wear from deeper damage. High-resolution transmission electron microscopy documents step heights near a single Si(100) layer and limited subsurface disorder within the mild-wear regime. Complementary ReaxFF molecular dynamics in LAMMPS resolves Si–O bridge formation and subsequent Si–Si bond cleavage sequences, supporting a picture of sequential layer-by-layer removal rather than brittle fracture through many layers at once.

## Methods

Experiments combine scanning-probe indentation and sliding on Si(100) with humidity-controlled water activity, reporting normal loads, scan speeds, and environmental conditions in the main text and figures of the PDF referenced by `pdf_path`. HRTEM (Fig. 2 and Supplementary Information) documents step heights and crystallinity beneath patterned regions.

**Reactive MD (ReaxFF / LAMMPS):** Simulations use a hydroxyl-terminated amorphous silica tip with radius near **30 Å** contacting a layered **Si(100)** substrate partitioned into fixed, thermostatted, and Newtonian regions. The **periodic** cell includes roughly **1600** water molecules (**~10⁴ atoms** total including substrate) forming about a **1 nm** film, **0.25 fs** **timestep** with velocity-Verlet integration, **Langevin** thermostats with **100 fs** damping on thermostat layers, and **NVT**-like thermal control of the heat-sink regions at **300 K** (ambient conditions stated in *Nat. Commun.* **Methods**). **Production** sliding segments reach **multi-ns** cumulative sampling across the load sweep (**Supplementary Fig. 12**). **Barostat / pressure:** **N/A —** no **NPT** **barostat**; normal **stress** enters through the rigid tip **load** (**nN**) rather than a **GPa** hydrostatic target.

## Findings

**Mechanism / outcomes:** **Reactive** trajectories show **water-mediated** **Si–O** bridge **formation** prior to **Si–Si** bond **scission**, producing removal step heights near **1.4 Å** consistent with single-layer **Si(100)** terraces.

**Comparisons:** **HRTEM** **compared** to simulated **removal** depths supports mild-wear **tribochemical** control versus deeper **damage** at higher **load**/**scan speed**.

**Sensitivity:** **Humidity**, tip **load** (**10–60 nN**), and **10 m s⁻¹** scan speed separate mild single-layer removal from deeper disruption in the published parameter window.

**Limitations / outlook:** The **Discussion** notes elevated **simulation** speeds/loads versus many lab **AFM** maps; **meniscus** physics is reduced to a finite water film.

**Corpus honesty:** Values follow the **Nature Communications** **PDF** at `pdf_path`; confirm thermostat region thicknesses if updating to newer **ReaxFF** builds.

## Limitations

Simulation loads and scan speeds are elevated relative to many laboratory atomic-force maps so that rare bond-breaking events occur within affordable trajectory lengths; extrapolation to industrial manufacturing throughput, tip durability, and long-run surface roughness evolution is therefore not attempted in the original study. Environmental humidity is modeled as a finite water film rather than full vapor–liquid equilibrium at the meniscus scale. Tip chemistry beyond the parametrized Si/O/H subset is not resolved explicitly in the published ReaxFF model.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
