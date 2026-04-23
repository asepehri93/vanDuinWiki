---
id: paper:2014addou-venue-acs-nn
type: paper
title: "Influence of hydroxyls on Pd atom mobility and clustering on rutile TiO₂(110)-(1×1)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - material:oxide
  - material:metal-surface
  - method:dft-static
  - method:monte-carlo
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:dft-static
  - keyword:monte-carlo-sampling
  - keyword:catalysis-surface
  - keyword:oxide-surface
  - keyword:reaxff-application
source_refs: []
doi: "10.1021/nn501817w"
year: 2014
authors:
  - "Rafik Addou"
  - "Thomas P. Senftle"
  - "Nolan O'Connor"
  - "Michael J. Janik"
  - "Adri C. T. van Duin"
  - "Matthias Batzill"
venue: "ACS Nano"
pdf_sha256: "f1cb40d950aad514cc948287bc1312bb84f5a4c77e6d1c05165e02bd827f03bc"
pdf_path: "papers/Addou_Senftle_ACS_nano_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014addou-venue-acs-nn -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. STM images, barriers, and cluster statistics must be read from the article.

## Summary

**STM**, **DFT**, **kinetic Monte Carlo**, and **ReaxFF-based Monte Carlo** study **Pd** adatom diffusion and sintering on **hydroxylated** versus **clean rutile TiO₂(110)-(1×1)**. The abstract reports that **small (1–3 atom) Pd clusters** persist near **300 K** on **hydroxylated** surfaces whereas **larger** clusters form on **bare** **TiO₂** under comparable conditions; **DFT** gives **stronger binding** near **OH** and **higher diffusion barriers** on the hydroxylated surface, with **ReaxFF MC** extending **H chemistry** during aggregation (`papers/Addou_Senftle_ACS_nano_2014.pdf`).

## Methods

### Scanning probe experiments

- **STM** follows **Pd** vapor deposition on **rutile TiO₂(110)-(1×1)** prepared **with vs without** interfacial **hydroxyls**; preparation includes **annealing/dosing** steps described in the **Experimental** section (**Summary**).

### Density functional theory (kinetic inputs)

- **DFT** **total-energy** calculations provide **Pd adatom binding** sites and **surface diffusion barriers** on **pristine** versus **hydroxylated** **TiO₂(110)**.
- **Barrier** and **binding** data feed **kinetic Monte Carlo** rates for large-scale **aggregation** trends (Methods for **DFT** code, **k-points**, and **XC** functional).

### ReaxFF Monte Carlo (explicit hydrogen chemistry)

- **NVT Monte Carlo** with **ReaxFF** extends atomistic modeling to **H spillover**, **Pd hydride** formation, and **H stripping** from **surface OH** by **Pd** clusters—effects not captured by **DFT+kMC** alone in the authors’ workflow (**Summary**).

### Coverage note

- **Temperature**, **coverage**, and **deposition flux** details belong to the **ACS Nano** article; do not infer numerical **barriers** from this wiki page alone.

**1 — MD application (atomistic dynamics).** **Engine / code:** headline dynamics are **kinetic Monte Carlo** on **DFT** rates plus **ReaxFF NVT Monte Carlo** for **H**-containing events; standalone **production MD** in **LAMMPS**/**GROMACS** is **N/A — not the stated headline workflow** on this summary layer (see article for any auxiliary trajectories). **System:** **Pd** on **TiO₂(110)** slabs with tunable **OH**; **atom counts** **PDF-grounded**. **Boundaries:** **slab**, **in-plane PBC**; normal **vacuum gap N/A here — confirm in PDF**. **Ensemble:** **NVT MC** (**ReaxFF** stage); **DFT** segments are **0 K** relaxations. **Thermostat:** **N/A —** the **ReaxFF** stage is **Monte Carlo** at prescribed **temperature**, not continuous **MD** with a **Berendsen**/**Nosé–Hoover** damping parameter on this summary layer (see **ACS Nano** for any auxiliary **MD** thermostat settings). **Timestep / barostat / pressure:** **N/A —** **MC** and **static DFT** dominate the summarized protocol (no **NPT** hydrostatic control described here). **Temperature:** **~300 K** cluster comparisons (**abstract**). **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**3 — Static QM / DFT-only.** **DFT** supplies **binding** sites and **diffusion barriers** for **Pd** on pristine vs hydroxylated **TiO₂(110)**; **functional**, **basis**, and **k-mesh** choices are in the **Experimental / computational** sections of the article (**N/A — not duplicated** on this page).

## Findings

- On **hydroxylated** surfaces, **DFT** reports **stronger Pd binding** near **OH** and **higher diffusion barriers**, so **kMC/ReaxFF** reproduce **small (1–3 atom) clusters** that remain **stable near 300 K**, whereas **bare** **TiO₂(110)** yields **much larger** clusters under similar deposition.
- **ReaxFF MC** shows **sub-nm Pd clusters can adsorb H** stripped from **TiO₂–OH**, **depleting OH** and **removing** the **diffusion impediment**, explaining the **bimodal** size distributions (**small clusters at low coverage**, **large clusters** once OH is titrated off).
- **Compared to experiment:** **STM** cluster sizes on **hydroxylated** vs **clean** surfaces anchor the **DFT/kMC/ReaxFF** story (**Summary**).
- **Sensitivity:** **OH coverage** and **Pd** **flux** control whether **OH-stabilized** **small clusters** persist versus **coarsening** (**Findings**).
- **Limitations / outlook:** **UHV** models omit **ambient water** and **support** **complexity** (**## Limitations**).
- **Corpus note:** numerical **barriers** belong to the **ACS Nano** **PDF**, not this short wiki layer.

## Limitations

- **Model** **UHV**-like surfaces vs **real** **wet** catalysts; **ReaxFF** accuracy for **Pd–oxide** is **method-dependent** (validated in-article to the extent described).

## Relevance to group

**Adri C. T. van Duin** and **Thomas P. Senftle** link **ReaxFF** to **supported catalyst** **sintering** on **TiO₂**, a recurring **oxide–metal** theme.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/nn501817w` (`papers/Addou_Senftle_ACS_nano_2014.pdf`).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
