---
id: paper:2017anoop-venue-untitled
type: paper
title: "Enthalpy Landscape Dictates the Irradiation-Induced Disordering of Quartz"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reactive-md
  - material:silicate-glass
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reactive-md
  - keyword:silica-silicate
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevX.7.031019"
year: 2017
authors:
  - "N. M. Anoop Krishnan"
  - "Bu Wang"
  - "Yingtian Yu"
  - "Yann Le Pape"
  - "Gaurav Sant"
  - "Mathieu Bauchy"
venue: "Phys. Rev. X"
pdf_sha256: "e5adbb7ba014b8282f65d7c9564e70eacd2d7c0c9c0aac5c339b17e66c100ff9"
pdf_path: "papers/ReaxFF_others/Anoop_IrradiationQuartz_PRX2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017anoop-venue-untitled -->

## Summary

Under irradiation, minerals accumulate structural defects until the atomic network becomes disordered and eventually saturates. Anoop Krishnan et al. (*Phys. Rev. X* **7**, **031019**, **2017**) use **reactive molecular dynamics (RMD)** of **α-quartz** to argue that the **topography of the enthalpy landscape** controls both how irradiation disorder initiates and when it stops accumulating. The authors distinguish irradiation-induced disorder from vitrification: prior to saturation, irradiated quartz accesses **forbidden regions** of the enthalpy landscape that cannot be reached by simply heating and cooling a melt. They further show that saturation occurs when the system reaches a **local landscape region** corresponding to the configuration of an **allowable liquid**, where **barrier heights** drop sharply so relaxation can erase additional damage attempts, yielding a **defect-saturated disordered state**.

## Methods

**RMD (LAMMPS, §II).** **PRX** **7**, **031019** (`papers/ReaxFF_others/Anoop_IrradiationQuartz_PRX2017.pdf`) models neutron damage by promoting a random lattice atom to a **600 eV PKA** (the article also cites **300 eV** and **1000 eV** contexts) with **Si/O** selection weighted by **neutron cross sections**. **Ballistic cascades** run inside a **10 Å** **NVE** sphere while the exterior stays at **300 K** via a **Nosé–Hoover thermostat**; **variable timesteps** handle violent collisions, otherwise **Δt = 0.5 fs**. Each cascade lasts **~20 ps** until energy/temperature equilibrate, followed by **5 ps** of **NPT** relaxation at **300 K** and **zero pressure**. Cycles repeat until **enthalpy** and **density** saturate. **Supercell dimensions**, **total atom count**, **full PBC** description, **electric fields**, and **enhanced sampling** are **not** restated in the indexed extract beyond this **NVE** sphere plus **NPT** leg.

**Force-field training:** **N/A —** applies the same **SiO₂** **ReaxFF** family used in the authors’ irradiation series; the **PRX** article emphasizes **landscape** analysis rather than refitting.

**Static QM / DFT:** **N/A —** not a standalone **DFT** production study in the excerpted opening.

## Findings

Irradiated **α-quartz** explores **enthalpy-landscape** basins **inaccessible** to simple **melt-quench** glass formation, supporting a qualitative distinction between **irradiation amorphization** and **vitrification** as **kinetic** pathways. After enough dose the network approaches a **liquid-like** basin with **low barriers**, so further impacts **fail to accumulate** damage—mirroring experimental **saturation** curves discussed in the article. **Compared** to **vitrified** references, the key claim is **non-equivalence** of damage **mechanisms** even when **density** or **enthalpy** look superficially similar. **Sensitivity** to **dose** (number of **PKA** cycles) controls when the **landscape** argument kicks in relative to **recrystallization**-prone damage at lower dose. **Limitations** in the discussion include **MD flux** versus reactor conditions, **sub-MeV PKA** energies versus some experiments, and sluggish **O** diffusion between cascades at **300 K**. **Uncertainty** in any numerical **barrier** should be resolved from the **published figures/tables** and **`pdf_path`**, not this wiki summary alone.

## Limitations

RMD cannot reach reactor timescales or MeV ion energies directly; barrier and basin analyses depend on the collective-variable construction in the article. Readers should take numerical barrier heights and saturation criteria from the published figures and tables.

## Relevance to group

Theoretical structure of **irradiation damage** in silica linked to **landscape** concepts—adjacent to reactive MD practice on quartz.

## Citations and evidence anchors

- DOI: `10.1103/PhysRevX.7.031019`.

## Related topics

- [[2017anoop-venue-paper]]
- [[reaxff-family]]
