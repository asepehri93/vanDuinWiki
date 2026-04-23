---
id: paper:2016min-polymer-98-2-interfacial-adhesion
type: paper
title: "Interfacial adhesion behavior of polyimides on silica glass: A molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - material:polymer-organic
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1016/j.polymer.2016.06.017"
year: 2016
authors:
  - "Kyoungmin Min"
venue: "Polymer, 98 (2016) 1-10"
pdf_sha256: "e5b67755c589a07aa79b5210b9551b914ac8edac6180627f4daf3948cbdf6c3d"
pdf_path: "papers/ReaxFF_others/Corning_Samsung_polymer_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016min-polymer-98-2-interfacial-adhesion -->

## Summary

Molecular simulations are used to probe how polyimide films adhere to silica glass, motivated by flexible display manufacturing where controlled debonding from carrier glass is critical. Steered molecular dynamics with a reactive force field is used to mimic pulling-induced detachment, yielding potentials of mean force, forces, and pull distances, together with chain conformation and energy decomposition during separation. **Display** **stack** **integration** often uses **polyimide** **on** **glass** **carriers**; **release** **layers** and **adhesion** **balance** determine **yield**, so **atomistic** **pulling** **curves** are interpreted as **screening** tools for **chemistry** choices before **full** **panel-scale** **tests**.

## Methods

**Steered MD (SMD).** **LAMMPS** **ReaxFF** simulations build **polyimide** films on **SiO₂** glass in **3D periodic** hybrid supercells. The protocol first relaxes each hybrid structure in **NVT** for **1 ns** at **300 K**, then switches to **NPT** for **1 ns** at **300 K** and **1 atm**, applying **NPT** only in the **x** and **y** directions to preserve **vacuum** along **z** (**Section 2**). **Nose-Hoover** **thermostat** and **barostat** damping constants are **100 fs** and **1000 fs**, respectively; **velocity Verlet** integration uses **Δt = 0.5 fs**. **Steered molecular dynamics** pulls then run in **NVT** with a constant **50 m/s** pull speed and a **spring constant of 100 kcal/mol/Å²**, after verifying convergence of **PMF** curves with respect to pull speed (**Section 2**). **External electric fields** and **umbrella/replica/metadynamics** are **not** used (**N/A**). **Hydrostatic pressure during the SMD pull** is **N/A** (**NVT** segment).

**Force-field training / static QM.** **N/A** — adhesion **application** study.

## Findings

Lower-coefficient-of-thermal-expansion (CTE) polyimides require higher peak force but shorter pull distance for complete detachment from silica (abstract), a **mechanism** tied to how interfacial chains **react** mechanically because of stronger **adhesion** to glass. **Multiple** polyimide chemistries are **compared** **versus** a common silica glass surface under the same steered-MD framework, giving a **benchmark**-style ranking. **CTE** is the primary sensitivity **lever** for PMF, force, and distance outcomes. **Limitations:** the full article discusses humidity, roughness, and industrial glass variability beyond the abstract—**open** questions for transferring PMFs to **experiment**—see the *Polymer* **PDF**. **Corpus honesty:** quantitative PMF curves should be read from figures in the full text, not inferred from this summary alone.

## Limitations

Local extract coverage is partial; quantitative PMF curves and numerical values should be taken from the full text and figures. **Humidity**, **silanol** **speciation**, and **roughness** on **industrial** **glass** may shift **adhesion** and **failure** **loci** relative to **ideal** **silica** **slabs**. **Pulling** **rates** in **steered** **MD** influence **PMF** **barriers** and should be compared to **experimental** **debond** **speeds** when possible.

## Relevance to group

Demonstrates ReaxFF steered-MD workflows for organic–oxide interfaces relevant to adhesion, packaging, and display substrates.

## Citations and evidence anchors

- DOI: [10.1016/j.polymer.2016.06.017](https://doi.org/10.1016/j.polymer.2016.06.017)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
