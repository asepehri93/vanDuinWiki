---
id: paper:2016yoon-venue-nn6b03036
type: paper
title: "Atomistic-scale simulations of defect formation in graphene under noble gas ion irradiation"
updated: "2026-04-20"
confidence: med
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
  - "Stephen Jesse"
  - "Xiahan Sang"
  - "Olga S. Ovchinnikova"
  - "Adam J. Rondinone"
  - "Raymond R. Unocic"
  - "Adri C. T. van Duin"
venue: "ACS Nano"
pdf_sha256: "0841b72e219d95fb553133d0a01f8ef46119e33ed435f6fe1b825443d8e8e005"
pdf_path: "papers/Yoon_ACSNano_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016yoon-venue-nn6b03036 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below are **curated summaries** of the **ACS Nano** article identified by **`doi`**, **`title`**, and **`pdf_path`**. Cross-beam comparisons and defect statistics must match the **paper**/**SI**.

## Summary

**ReaxFF molecular dynamics** simulates **noble-gas ion** bombardment of **graphene** with subsequent **thermal** treatment, linking **ion species**, **energy**, and **dose** to **defect** populations and **nanopore** formation. **ORNL** collaborators provide **aberration-corrected STEM** and **helium ion microscopy** trends for qualitative comparison to simulation. The study distinguishes regimes where **Stone–Thrower–Wales (STW)** defects dominate (**He⁺**) versus **monovacancy**-rich damage for heavier ions, and discusses **post-irradiation** **annealing** pathways where **vacancy-like** defects **coalesce** into larger pores.

The work situates **ion irradiation** as a **scalable** route to **nanopore** engineering in **2D** membranes, while emphasizing that **electronic stopping** is not treated explicitly in the **classical** cascade model—an important interpretive caveat when mapping to **microscope** experiments.

## Methods

**1 — MD application (ReaxFF in LAMMPS).** **Engine:** **LAMMPS** **ReaxFF** using **C-2013-class** carbon parameters (**Srinivasan / van Duin 2015** lineage cited in **Methods**) plus **ion–graphene short-range repulsion** fit to **DFT + ZBL** training (**Figure S1**, **`[[2016yoon-venue-microsoft-word]]`**). **Sheet:** periodic **graphene** supercell **~52 × 40 Å\(^2\)** pre-equilibrated at **300 K** with **Nosé–Hoover** thermostats on the sheet; **25 keV** **He\(^+\)**, **Ne\(^+\)**, **Ar\(^+\)**, or **Kr\(^+\)** impacts land in a central **30 × 20 Å\(^2\)** window while **edge regions** remain **300 K** heat sinks. **Cascade segment:** **NVE** microcanonical dynamics during impact with **sub-0.02 fs** timesteps (**0.005–0.02 fs** depending on ion species) to conserve energy during collisions. **Dose delivery:** simulation dose rates (**\(10^{27}\)**, **\(5×10^{25}\)**, **\(3.5×10^{25}\)**, **\(2.4×10^{25}\) ions/cm\(^2\)/s\)** for **He/Ne/Ar/Kr**) are chosen so cascades finish between impacts despite being far faster than laboratory beams (**Methods**). **Annealing:** **He\(^+\)** structures extracted at **\(10^{15}\)**, **\(10^{16}\)**, **\(10^{17}\) ions/cm\(^2\)** are briefly annealed **25 ps at 1500 K** then cooled to **300 K**, followed by a longer **1.25 ns** anneal at **2000 K** to mimic slower laboratory reconstruction; other ions use lower cumulative doses (**\(10^{14}\)–\(2×10^{15}\) ions/cm\(^2\)**) before analogous post-processing (**Methods**). **Barostat:** **N/A —** in-plane periodicity with **NVE** cascades + **thermostatted** edges as described. **Pressure control:** **N/A —** not a hydrostatic **NPT** study; **normal stress** from impacts is handled implicitly by the **collision** protocol rather than a **barostat** target in **GPa**. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** Short-range **ion–C** terms are trained as summarized in **`[[2016yoon-venue-microsoft-word]]`**; the main text references that **SI** for **DFT** settings and parameter tables.

**3 — Static QM.** **DFT/ZBL** data enter only through the **force-field** fit (**SI**), not as standalone production **QM** along the MD trajectory.

**4 — Experiments.** **Aberration-corrected STEM** and **helium-ion microscopy** images/doses are compared qualitatively to simulation morphologies (**Results**).

## Findings

**Dose trends.** Simulations and **STEM**/**He-ion** experiments both show **defect accumulation** and **high-dose amorphization**, with **larger nanopores** and wider **amorphized** patches for **heavier ions** and **higher doses** (**abstract**, **Figures 1–2**).

**Annealing.** Post-irradiation **high-T anneals** allow **vacancy-like** defects to **coalesce** into **extended pores**, matching the **abstract** statement about **relaxation-driven** coarsening.

**Defect statistics.** Across **100**-run samples (**Figure 5**), **He\(^+\)** (**\(10^{16}\) ions/cm\(^2\)** case quoted in text) yields mostly **STW** defects (**~65%**) with smaller **Frenkel** fractions, whereas **Ne\(^+\) / Ar\(^+\) / Kr\(^+\)** runs are dominated by **monovacancies** (**~73%**) because **energy transfer** per impact is higher.

**Mismatches.** The article flags imperfect **Ne\(^+\)** lab/simulation alignment because **accelerating voltage** and **dose** differ between **microscope** conditions and the **MD** protocol (**Results** discussion).

**Corpus honesty.** **Electronic stopping** is deliberately neglected (**Methods**); quantitative **defect percentages** should be copied from **Figure 5** tables in the **PDF**, not from this summary alone.
## Limitations

**Electronic stopping** is neglected; **beam** parameters may differ between **simulation** and **microscopy**. **ReaxFF** cannot capture **charge-state** effects of **ions** in detail.

## Relevance to group

**van Duin**-coauthored **ACS Nano** study on **ReaxFF** for **ion-induced** **graphene** **defect** engineering—links to **nanopore** and **2D materials** themes.

## Citations and evidence anchors

- DOI [10.1021/acsnano.6b03036](https://doi.org/10.1021/acsnano.6b03036); PDF `papers/Yoon_ACSNano_2016.pdf`.
- Excerpt alignment: `normalized/extracts/2016yoon-venue-nn6b03036_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
