---
id: paper:2018haesun-park-chem-mater-0-adiabatic-nonadiabatic
type: paper
title: "Adiabatic and Nonadiabatic Charge Transport in Li–S Batteries"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:dft-static
  - task:application
  - material:sulfur-cathode
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:batteries-interfaces
  - keyword:qm-training-data
candidate_tags: []
source_refs: []
doi: "10.1021/acs.chemmater.7b04618"
year: 2018
authors:
  - "Haesun Park"
  - "Nitin Kumar"
  - "Marko Melander"
  - "Tejs Vegge"
  - "Juan Maria Garcia Lastra"
  - "Donald J. Siegel"
venue: "Chem. Mater."
pdf_sha256: "4a18704d1f119a4c7937b16531650c718c421e80cf3d5f63ade6a75d57cda64d"
pdf_path: "papers/Others/Kumar_LiS_acs.chemmater_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018haesun-park-chem-mater-0-adiabatic-nonadiabatic -->

## Summary

Hybrid-functional and **constrained DFT** calculations are used to clarify **electronic and ionic transport** in **α-sulfur** and **Li\(_2\)S**, the insulating redox end members in Li–S cells. The study contrasts **adiabatic** vs **nonadiabatic** charge transfer: **Li\(_2\)S** is treated as **adiabatic** (standard DFT adequate for hops), whereas **S\(_8\)** ring–ring transitions require **nonadiabatic** treatment—**conventional DFT** can **overestimate** charge-transfer rates by orders of magnitude. Polaronic carriers (holes dominant in Li\(_2\)S; delocalized holes and localized electron polarons in α-S) have **very low equilibrium concentrations** but **sufficient mobility** to matter for practical sulfur loadings.

Broader motivation is that **Li–S** cathodes are limited by **shuttle** chemistry and poor **electronic** conduction in **S\(_8\)** and **Li\(_2\)S**; clarifying whether charge transport is **Marcus-like** and adiabatic in both phases versus **nonadiabatic** in **S\(_8\)** sets expectations for rate-limiting steps in thick-electrode models.

## Methods

- **Electronic structure:** Primarily **VASP** with **hybrid functionals** (e.g. **HSE**) for bulk and defects; **PAW** pseudopotentials; **plane-wave cutoffs** ~**450–500 eV**; **spin-polarized** calculations; **Γ-centered k-point meshes** with density reduced for large α-S **supercells** (see article tables).
- **Supercells:** **α-S** conventional cell (**128** atoms) and **Li\(_2\)S** **96-atom** supercell from **2×2×2** replication; lattice dimensions for α-S from prior **vdW-DF** relaxation where noted; forces converged to **0.04 eV/Å** (α-S) and **0.01 eV/Å** (Li\(_2\)S).
- **Defect space:** Many **vacancy, interstitial, and polaron** configurations (charged/neutral); **formation energies**; **Frenkel** and **Schottky** defects for Li\(_2\)S.
- **Nonadiabatic / localization:** **Constrained DFT (cDFT)** implemented in **GPAW** using **PBE** and grid spacing ~**0.16 Å** to build localized diabatic states and coupling; analysis of **Marcus-type** rates comparing adiabatic vs cDFT-based approaches for sulfur.
- **Properties computed (reported observables):** **formation energy** trends, **barrier** estimates along reaction coordinates, **electronic structure** / **band** alignment where tabulated, and **charge-transfer** / **Marcus** rate metrics from **cDFT** vs standard **DFT** (verify every number in the **Chem. Mater.** **PDF**).

## Findings

- **Li\(_2\)S:** Charge transport is **adiabatic**; **hole polarons on S** are key; carriers have **extremely low equilibrium concentrations** but **mobilities** still relevant for high energy-density targets.
- **α-S:** **Ring-to-ring** transitions are **nonadiabatic**; **standard DFT** overestimates transfer rates by up to **~100×** relative to the constrained/nonadiabatic analysis; **delocalized holes** and **localized electron polarons** dominate mobility discussions.
- Connecting to cells: **low equilibrium carrier concentrations** contribute to **sluggish** transport in both end members; increasing **hole concentrations** is discussed as a strategy to improve performance.
- **Comparisons / limitations / PDF:** The authors **compare** **adiabatic** DFT rate estimates to **cDFT**-based **nonadiabatic** rates for **α-S** (orders-of-magnitude gap) and tie **Li\(_2\)S** transport to **hole polaron** **mechanisms**. **Hybrid functionals** and **finite supercell** charged-defect corrections introduce **uncertainty**; device-relevant amorphous sulfur morphologies exceed the idealized bulk models. Verify all **barriers** and **concentrations** against the **PDF** (`pdf_path`).

## Limitations

Functional choices (**HSE** cost vs **PBE/cDFT**); finite supercells and **charged defect** corrections; **α-S** amorphous/molecular real cathodes differ from idealized bulk models.

## Relevance to group

**DFT transport** benchmark for **S/Li\(_2\)S**—complements **ReaxFF** electrolyte and interface kinetics elsewhere in the corpus.

## Citations and evidence anchors

- DOI: `10.1021/acs.chemmater.7b04618`.

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
