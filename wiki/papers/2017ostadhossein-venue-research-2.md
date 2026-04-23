---
id: paper:2017ostadhossein-venue-research-2
type: paper
title: "ReaxFF Reactive Force-Field Study of Molybdenum Disulfide (MoS₂) — galley PDF"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - task:parameterization
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:2d-materials
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:lammps
source_refs: []
doi: "10.1021/acs.jpclett.6b02902"
year: 2017
authors:
  - "Alireza Ostadhossein"
  - "Ali Rahnamoun"
  - "Yuanxi Wang"
  - "Peng Zhao"
  - "Sulin Zhang"
  - "Vincent H. Crespi"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "f1497981a3ba30f20dfcf48aeff00d9fc55996fc3ae8b8717b3367f02bf8db70"
pdf_path: "papers/Ostadhossein_MoS2_JPC_Letters_2017_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017ostadhossein-venue-research-2 -->

!!! note "Corpus PDF role"
    **Galley/proof-style** duplicate of the JPCL letter; **VOR** PDF: **`Ostadhossein_MoS2_JPC_Letters_2017.pdf`** on **[[2017ostadhossein-venue-research]]**.

## Summary

**Molybdenum disulfide** in the **2H** semiconducting polytype is a canonical **transition-metal dichalcogenide**, but **reactive** simulations of **defects**, **phase transitions**, and **mechanics** need a **bond-order** potential trained on **Mo/S/H** chemistry with both **molecular** and **periodic** references. Prior **metal/chalcogen** **ReaxFF** efforts in the broader literature often emphasize either **mechanics** or **chemistry**; this letter aims for a **joint** fit suitable for **mechano-chemical** questions such as **vacancy** migration under **strain**. This letter introduces a **Mo/S/H ReaxFF** fit to **Jaguar** **B3LYP/LAV3P\*\*** molecular data and **VASP** **PBE** **PAW** periodic data (**400 eV** cutoff, **Γ-centered** k-grids, force thresholds **<0.02 eV/Å**), including **bilayer** spacing scans with constrained **Mo** planes and **NEB** barriers where needed. The functional form combines bonded, torsion, lone-pair, over/under-coordination, **vdW**, and **Coulomb** contributions (Eq. 4 in the paper). Applications span **vacancy** formation and **migration**, **2H↔1T** pathways, **ripplocation** defects and coupling to **sulfur vacancies**, and **elastic** response under **uniaxial/biaxial** strain with **in-plane** periodic boundary conditions.

## Methods

**Force-field training / fitting.** **Identical** to **`[[2017ostadhossein-venue-research]]`**: **Mo/S/H ReaxFF** trained against **Jaguar B3LYP/LAV3P\*\*** molecular data and **VASP PBE-PAW** periodic benchmarks (**400 eV**, **Γ-centered** k-sampling, **<0.02 eV Å⁻¹** force criterion), with **SI** parts **I–III** archiving **BIOGRF** clusters, **parameter tables**, and **`trainset.in` weights**.

**MD application (atomistic dynamics).** **Same** **LAMMPS**/**ReaxFF** **molecular dynamics** and **force-field NEB** applications described on the **VOR** page (**[[2017ostadhossein-venue-research]]**): **in-plane periodic MoS₂** supercells under **uniaxial/biaxial** strain, **defect**, **ripplocation**, and **2H↔1T** pathway sampling. **Galley-only caveat:** per-cell **ensemble**, **thermostat**, **timestep**, and **production** **MD** **duration** should be read from the **VOR** PDF/SI if locators differ—this duplicate entry does **not** supersede **`[[2017ostadhossein-venue-research]]`** for machine-checked MD metadata. **Atom** budgets follow the **VOR** structures figure-by-figure. **Equilibration / staging:** **equilibration** plus **production** segments follow the **VOR** figure captions (**ps**-scale relaxations and longer **production** windows as cited there). **Temperature / pressure:** **thermal** and **stress** targets mirror the **VOR** MD panels (**hydrostatic pressure control** **N/A —** not separately re-tabulated on this duplicate page). **Barostat:** **N/A —** any optional **NPT** snippets are documented on the **VOR** page rather than re-listed here.

**Static QM / DFT.** **Identical** **Jaguar/VASP** training and validation sets as the **VOR** page.

**Review / non-simulation framing.** **Galley/proof-style** duplicate PDF; **canonical prose** maintenance target is **`[[2017ostadhossein-venue-research]]`**.

## Findings

**Outcomes & mechanisms.** Matches the **VOR** summary: the **Mo/S/H ReaxFF** reproduces selected **DFT/experimental** **2H MoS₂** benchmarks while enabling **vacancy**, **ripplocation**, **2H–1T**, and **mechanical** studies at reactive FF cost.

**Comparisons.** Same **DFT**/**experiment** positioning as **`[[2017ostadhossein-venue-research]]`**.

**Sensitivity & design levers.** **Strain state** and **defect** population remain the primary levers highlighted in the letter.

**Limitations & outlook (as authored).** **Galley** pagination may differ from the **VOR**; barrier **down-scaling** vs **DFT** cautions mirror the parent page.

**Corpus / KB honesty.** Use **`[[2017ostadhossein-venue-research]]`** for DOI-grounded MD tables; this slug exists only to document alternate **PDF bytes**.

## Limitations

**DFT** band-gap limitations apply; the focus is **structural energetics** rather than **excited-state** physics. **Galley** pagination may differ from **[[2017ostadhossein-venue-research]]** for locators. Repository automation maps this stable `paper_id` to `normalized/papers/2017ostadhossein-venue-research-2.json` and the repo-relative `pdf_path`. Where `extraction_quality` is partial, the tracked PDF and DOI remain the quantitative authority over short local extracts.

## Reader notes (navigation)

- Version-of-record page: **[[2017ostadhossein-venue-research]]**
- SI companion slugs (if used): **[[2017ostadhossein-venue-microsoft-word]]**, **[[2017ostadhossein-venue-microsoft-word-2]]**, **[[2017ostadhossein-venue-microsoft-word-3]]**
- [[reaxff-family]]
