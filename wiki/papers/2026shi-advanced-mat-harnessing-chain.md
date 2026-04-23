---
id: paper:2026shi-advanced-mat-harnessing-chain
type: paper
title: "Harnessing chain mobility via protonation for tough and isotropic hydrogel"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - material:polymer-organic
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:nvt-simulation
  - keyword:polymer
  - keyword:dft-static
source_refs: []
doi: "10.1002/adma.202517407"
year: 2026
authors:
  - "Pengju Shi"
  - "Muqing Si"
  - "Zishang Lin"
  - "Qian Mao"
  - "Sidi Duan"
  - "Zixiao Liu"
  - "Wen Hong"
  - "Mason Possinger"
  - "Yichen Yan"
  - "Chi Chen"
  - "Ping He"
  - "Xiaobing Zuo"
  - "Hua Zhou"
  - "Adri van Duin"
  - "Ximin He"
venue: "Advanced Materials"
pdf_sha256: "8cfd6cff123a7031dcc0cee2e599c980a706f72025a24f6d1400bf91f9bbcfde"
pdf_path: "papers/Shi_Si_Lin_Mao_Hydrogel_Advanced_Materials_2026.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2026shi-advanced-mat-harnessing-chain -->

## Summary

Ultra-tough, isotropic poly(vinyl alcohol) hydrogels are prepared by sequential acidification, freeze-thawing, and salting-out. Reactive MD with a ReaxFF C/H/O/Li/Na/K/Cl/I parametrization (reparameterized from prior reports) probes protonation and hydrogen-bond network evolution for a PVA dimer in water versus HCl solution, alongside DFT (Jaguar) checks on hydrogen-bond strengths in model dimers and experimental mechanics and microstructure.

## Methods

Primary source: `papers/Shi_Si_Lin_Mao_Hydrogel_Advanced_Materials_2026.pdf`.

**Experimental.** PVA hydrogels processed with controlled HCl in precursor, freeze-thaw (FT) and salting-out (SO) steps; mechanical testing (tensile, fatigue, notch tests), SEM, DSC, SAXS, mercury porosimetry, optical and FLIM imaging, NMR on protonation, and extended protocols in Supporting Information.

**Reactive MD.** ReaxFF C/H/O/Li/Na/K/Cl/I (reparameterized from cited ReaxFF electrolyte-water and biomolecule work). PVA dimer with 20 OH groups in neutral water versus acidic HCl solution: initial NVT equilibration at 300 K for 2.0 ns; second NVT segment at 253 K for 2.0 ns to capture low-temperature hydrogen-bond network evolution. Three replicate trajectories for hydrogen-bond statistics as stated. Additional dry C3H7OH dimer minimizations compare ReaxFF and DFT hydrogen-bond strengths for defined protonation cases; Mulliken charge analysis on shared protons with increasing explicit water molecules.

**DFT.** Non-periodic Jaguar DFT calculations on small alcohol dimers for hydrogen-bond energetics in neutral and protonated cases.

**Association modeling.** Flory-Huggins lattice hydrogen-bond counting (Text S2 in SI) ties acid concentration to PVA-PVA versus PVA-water hydrogen-bond populations.

**1 — MD application (atomistic dynamics).** LAMMPS ReaxFF **molecular dynamics** of a **PVA dimer** (20 OH groups) in **H₂O** vs **HCl** (order **~100+** **atoms** with solvation per PDF); **3D** **PBC**; two **2.0 ns** **NVT** **stages** at **300** **K** and **253** **K** with **Berendsen** or **Nose**–**Hoover** **thermostat** (per **SI**); **3** **replicate** **trajectories**; **fs** **time** **step** in the **PDF** (not on this one-line blurb). **N/A** — **NPT** **barostat** for the PVA-dimer line. **N/A** — **static** **E-field** in MD. **N/A** — **replica** or **metadynamics**. **Flory**-**Huggins** in **Text S2** is **lattice** **(not** **MD**).

**2 — Force-field training (application of reparametrized C/H/O/Li/Na/K/Cl/I ReaxFF from cited lines).** **N/A** — this paper reuses/extends a prior **ReaxFF** with **Jaguar** **DFT** **spot** **checks** on **dimers**.

**3 — Static QM / DFT (Jaguar dimer H-bond energetics).** See **DFT** paragraph. **4 — Review** — **N/A.**
## Findings

- Reported optimized PVA-SO hydrogel reaches tensile strength 29.5 MPa, stretchability 2683%, and toughness 424 MJ m^-3 among isotropic hydrogels in the article's comparison.
- MD shows acid-catalyzed proton transfer forming H3O+ and protonated PVA-OH2+, with greater chain curling in acid at 253 K versus neutral water and similar inter-chain hydrogen-bond counts when protonated sites are included, supporting homogenized chain conformations before salting-out fixes dense hydrogen-bonded domains.
- DFT validates qualitative ReaxFF trends for dimer hydrogen-bond strengths in selected cases; the manuscript notes explicit limits of gas-phase dimer models versus full solvation dynamics.
- Experiments correlate acidification with reduced premature crystallization during freeze-thaw, higher transparency, and modulated pore and crystallinity signatures before salting-out builds tough networks.

- **Caveat / comparison:** DFT dimer **gas**-phase **models** **vs** full **solvated** **MD**—see `## Limitations` and the manuscript on **solvated** **network** **mechanics**.

## Limitations

Residual salt and dehydration sensitivity are noted in the article as practical limits; ReaxFF provides qualitative protonation and HB trends with DFT spot checks.

## Relevance to group

Adri van Duin contributes reactive MD and DFT validation of protonation and hydrogen-bond behavior for the PVA processing hypothesis.

## Citations and evidence anchors

DOI: `10.1002/adma.202517407`.

## Related topics

- [[reaxff-family]]
