---
id: paper:2020sheth-journal-of-n-influence-acid
type: paper
title: "Influence of acid leaching surface treatment on indentation cracking of soda lime silicate glass"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - material:silicate-glass
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:berendsen-thermostat
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:nvt-simulation
  - keyword:oxide-surface
  - keyword:reaxff-application
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1016/j.jnoncrysol.2020.120144"
year: 2020
authors:
  - "Nisha Sheth"
venue: "Journal of Non-Crystalline Solids, 543 (2020) 120144"
pdf_sha256: "ef78d15be361766cc257cf719b39cb78afc063ca3e3c38f3090d4b3d761cdfec"
pdf_path: "papers/Sheth_JNonCrystSol_2020_Acid_Leaching.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020sheth-journal-of-n-influence-acid -->

## Summary

**Acid leaching** of soda lime silicate (SLS) increases **apparent** crack resistance at the treated surface during Vickers indentation relative to a polished baseline; combined **dry** vs **humid** **N₂** tests and **ReaxFF** reactive **molecular dynamics** in **ADF** link **humidity**-dependent **radial** cracking to water transport through the leached layer and to pressure-driven restructuring of the near-surface **silica** network. Past work showed that water or acid soaking can raise the mechanical strength of SLS glasses. This study extends that story with **controlled** **environments** and **atomistic** **load** **mimics** (see **## Methods**). Vickers tests in controlled environments show humidity-dependent radial cracking, implicating water transport through the leached layer in crack propagation to the surface. Reactive MD with ReaxFF indicates that the leached layer can undergo mechanochemical reactions under indentation load, increasing bridging-oxygen connectivity in the silica network and hindering transport of environmental water toward subsurface crack tips. The authors propose that load-driven restructuring in the leached layer lowers the kinetics of water delivery to critical flaws, producing the observed enhancement in apparent crack resistance.

## Methods

- **Experiments:** **Vickers** indentation on acid-leached soda lime silicate (SLS) glass in a chamber with **dry** or **humid** nitrogen (abstract cites **~90% RH** for the humid case). A **1.96 N** load is used in the discussion tying indent depth to the modeled stress state (see article for full indentation and imaging protocol).
- **Reactive MD (PDF):** **Na/Si/O/H ReaxFF** as implemented in the **Amsterdam Density Functional (ADF)** package; integration with **Verlet**, **time step 0.25 fs**, **Berendsen** thermostat (**100 fs** damping) and barostat (**5 ps** damping) where NPT is used.
- **Model system:** Acid-leached region built from a **70:30 mol% SiO2:Na2O** glass in a **~4.30 x 4.37 x 12.05 nm** periodic cell (**758** of **1200** Na+ in top/bottom thirds exchanged for **H+** to mimic leaching). Initial **NVT** equilibration at **300 K** (**0.25 ns**) yields a silanol-enriched surface.
- **Indentation mimic:** **NPT** at **300 K** with hydrostatic pressures **0.1, 0.5, 1, 5, and 10 GPa** for **100 ps**; condensed water from reactions removed, then **1 atm**, **300 K** **NPT** **25 ps** before analysis of network/water transport.

**MD details (leached-glass + pressure ramp).** **PBC** **~4.3 × 4.4 × 12.05 nm** **cell**; **Na⁺** **→** **H⁺** **exchange** in **top/bottom** **thirds** **(758/1200)**. **NVT** **0.25** **ns** at **300** **K**; then **NPT** **sweeps** with **Berendsen** **thermostat** (**100** **fs** **damping**) and **barostat** (**5** **ps** **damping**) at **0.1–10** **GPa** per **100** **ps**; final **1** **atm** **NPT** **25** **ps** before **bridging-oxygen** / **water** **transport** **analysis**. **Electric** **field: N/A** —. **Umbrella** / **replica: N/A** —.

## Findings

- Acid leaching **increases apparent crack resistance** of the treated SLS surface during indentation relative to the untreated case under the reported conditions.
- **Radial cracking** under Vickers indentation shows a **humidity dependence**, supporting a role for **water transport through the leached layer** in crack growth paths to the surface.
- Reactive MD indicates **pressure-induced mechanochemical reactions** in the leached layer during loading that **increase bridging-oxygen connectivity** in the near-surface silica network.
- Those structural changes are argued to **impede molecular water transport** from the environment toward the subsurface crack tip, motivating a hypothesis that **reduced water transport kinetics** to flaws explains the **enhanced apparent crack resistance** of the acid-leached surface.

## Limitations

Local PDF extraction in the corpus is **pages 1–2–oriented**; full numerical indentation loads, simulation cell sizes, thermostat/ensemble choices, and run lengths should be taken from the **version-of-record PDF** and any **supporting information** when extending this note.

## Relevance to group

Adri C. T. van Duin is a co-author; the work couples **glass surface chemistry**, **mechanics**, and **ReaxFF**-based reactive simulation for an engineering glass system.

## Citations and evidence anchors

- DOI: `10.1016/j.jnoncrysol.2020.120144`

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
