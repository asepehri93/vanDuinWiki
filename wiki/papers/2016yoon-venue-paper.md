---
id: paper:2016yoon-venue-paper
type: paper
title: "Atomistic-scale simulations of defect formation in graphene under noble gas ion irradiation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.6b03036"
year: 2016
authors:
  - "Kichul Yoon"
  - "Ali Rahnamoun"
  - "Jacob L. Swett"
  - "Vighter Iberi"
  - "David A. Cullen"
  - "Ivan V. Vlassiouk"
  - "Alex Belianinov"
  - "Xiahan Sang"
  - "Olga S. Ovchinnikova"
  - "Adam J. Rondinone"
  - "Raymond R. Unocic"
  - "Adri C. T. van Duin"
venue: "ACS Nano"
pdf_sha256: "c54c9c1ef4d9fb356daeead37bd4da58b7b2350f63a5a73ba4cc95237f7b7dd4"
pdf_path: "papers/Yoon_ACSNano_ASAP.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2016yoon-venue-paper -->

## Summary

This corpus PDF is an ACS **“Just Accepted”** posting of **Yoon et al.**, *ACS Nano*, **DOI `10.1021/acsnano.6b03036`**. The work pairs **ReaxFF molecular dynamics** in **LAMMPS** with **helium ion microscopy** and **aberration-corrected STEM** to relate **noble-gas ion irradiation** of **graphene**—including **post-impact annealing**—to **defect statistics** and **nanopore** formation. The paper stresses how **dose**, **ion species**, and **collision cross section** steer **vacancy-type** damage toward **coalesced pores**, and how **Stone–Thrower–Wales (STW)** motifs dominate under **He\(^+\)** whereas **monovacancy (MV)**-rich statistics appear for heavier noble gases. **Electronic stopping** is omitted in the nuclear-collision treatment, following cited precedent for graphene.

## Methods

**MD (ReaxFF, LAMMPS).** Simulations use **ReaxFF C-2013**-based **carbon** chemistry with **graphene–ion** repulsion augmented by **DFT**-fitted terms and a **Ziegler–Biersack–Littmark** channel as described in **Computational methods and details** (`papers/Yoon_ACSNano_ASAP.pdf`); **SI** holds parameter tables and **DFT** settings (full **functional / basis / k-mesh** tables are **not** transcribed on this page). A periodic **graphene** supercell about **52 × 40 Å²** (thousands of **carbon atoms**) receives **25 keV He\(^+\), Ne\(^+\), Ar\(^+\), Kr\(^+\)** impacts in a central **~30 × 20 Å²** window. **In-plane PBC** apply; **edge** regions are held at **300 K** with a **Nosé–Hoover** **thermostat** while the cascade core runs **NVE** during ballistic impact. Species-dependent **timesteps** of **0.005–0.02 fs** stabilize the cascades. Dose rates of order **10²⁵–10²⁷ ions cm⁻² s⁻¹** (species-dependent) space impacts so each cascade completes before the next. **He\(^+\)** ladders reach **10¹⁵–10¹⁷ ions cm⁻²** cumulative dose, each followed by **1500 K for 25 ps**, cool-down to **300 K**, then **2000 K for 1.25 ns** of reconstruction. **Ne\(^+\)/Ar\(^+\)/Kr\(^+\)** use **10¹⁴–2×10¹⁵ ions cm⁻²**, the same **1500 K / 25 ps** leg, then **3000 K** annealing; the **duration of the 3000 K segment** is **not** recovered from the Methods text checked for this note. **Barostat**, **applied electric fields**, and **replica / enhanced sampling** are **not** used on these fixed-area irradiation legs (cascades plus thermal annealing only). **Hydrostatic pressure** is **not** servo-controlled during those legs (**fixed in-plane** supercell area; **N/A —** no **NPT** **pressure** target in the summarized irradiation protocol).

**Force-field training:** **N/A — not a new ReaxFF fit** in the main article; the study **applies** published **C-2013** chemistry with documented **DFT/ZBL** extensions in **SI**.

**Experiment.** **HIM** (**Zeiss ORION NanoFab**, **~25–27 kV**, **0.191 pA**, **0°** on suspended **CVD graphene**) and **Nion UltraSTEM** **MAADF-STEM** at **60 kV** follow the **Experimental methods and details** block in the same PDF.

## Findings

Post-irradiation **annealing** drives **vacancy-type** defects to **coalesce** into **nanopores**; **heavier ions** and **higher dose** produce **larger pores** and more **amorphized** surroundings, tracking **STEM** trends though some **Ne\(^+\)** sim/expt pairs differ in dose/energy matching. **Defect surveys** report **~65% STW** character for **He\(^+\)**-dominated statistics versus **~73% MV** prevalence for **Ne\(^+\)/Ar\(^+\)/Kr\(^+\)** in the conclusions as summarized in the article. Simulated **sputtering** / removal metrics at **25 keV** (**~0.03** for He up to **~50%** cumulative-style metrics for Kr in the authors’ framing) are contrasted with **single-impact** literature values, attributing gaps to **multi-impact** geometry. **Simulation–experiment** agreement is described as encouraging on **dose** and **morphology** while noting **impurities**, **contamination**, and possible **metal-catalyzed chiseling** in experiment. **Authored limitations** include **dose-rate** mismatch and using **high-T anneals** to stand in for **room-temperature** reconstruction kinetics within **MD** wall times.

## Limitations

**Just Accepted** PDF: prefer the **typeset** **VOR** layout for pagination and final figure quality. This slug’s **`normalized/extracts`** slice is **boilerplate-heavy**; protocol numbers above were taken from **`pdf_path`**.

## Relevance to group

Duplicate **corpus** proof of **van Duin**/**ORNL** **graphene irradiation** collaboration.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acsnano.6b03036` (`papers/Yoon_ACSNano_ASAP.pdf`).

## Related topics

- [[2016yoon-venue-nn6b03036]]
- [[reaxff-family]]
