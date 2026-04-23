---
id: paper:2016hong-venue-jp6b00786
type: paper
title: "Atomistic-scale analysis of carbon coating and its effect on the oxidation of aluminum nanoparticles by ReaxFF molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - method:reaxff
  - material:oxide
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b00786"
year: 2016
authors:
  - "Sungwook Hong"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "0d4a4f29a408a9ebdddd4d7b9865ac139f424a5a32e9659cf72bbb76f07dc1f4"
pdf_path: "papers/Hong_AlCOx_JPCC_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2016hong-venue-jp6b00786 -->

## Summary

An **Al/C ReaxFF** is developed against **QM training sets** and exercised in **ReaxFF MD** to study **hydrocarbon-derived carbon coatings** on **aluminum nanoparticles (ANPs)** and their influence on **subsequent oxidation**. Simulations report **hydrogen transfer to Al sites**, **C–C bond-preserving** binding modes for some precursors, and **precursor-dependent carbon layer growth**. **Oxidation** of **coated** particles is compared to **bare** ANPs, highlighting **reduced reactivity at low temperature** but **high susceptibility once the coating is disrupted at elevated temperature**, consistent with the **experimental literature** cited in the article.

## Methods

This slug points at **`papers/Hong_AlCOx_JPCC_2016.pdf`**; narrative and locator notes for the same **DOI** also appear on [[2016hong-venue-research]] (**ACS proof** bytes). The protocol text below matches that article.

**Force-field training (ReaxFF for Al/C/H/O):** **QM training (periodic):** **VASP** **GGA-PBE** with **PAW**, **400 eV** cutoff; **Al(111)** slabs (**6 layers**, lower layers fixed) for hydrocarbon adsorption/decomposition; **k-meshes** including **8×8×8** (bulk **Al\(_4\)C\(_3\)**) and **5×5×1** (slab adsorbates); **NEB** (**L-BFGS**, **3 images**) for barriers. **QM clusters:** **Jaguar** **B3LYP/6-311G** for nonperiodic **Al/C/H/O** geometries; bond/angle scans for **Al–C** dissociation and distortion. **ReaxFF optimization:** sequential refinement of **Al–C**, **Al/H**, and angle/off-diagonal terms to QM targets; **ReaxFF-NEB** cross-checks vs **DFT-NEB** on selected pathways.

**MD application (coatings and oxidation):** **Engine:** **ADF** for **ReaxFF molecular dynamics** (same protocol as [[2016hong-venue-research]]). **Ensemble / controls:** **NVT** with **Berendsen** thermostat (**100 fs** damping); **timestep 0.1 fs** (authors cite high **T** up to **~3000 K**). **Coating cycles:** **864-atom** Al nanoparticle in **45×45×45 Å³** with **350** gas molecules per cycle; **ANP at 300 K**, hydrocarbon gas **2500 K for 15 ps**, then cool to **300 K in 8.5 ps**; repeated; **ethylene**, **ethane**, **acetylene** compared. **Oxidation:** coated ANP with **600 O\(_2\)** in **60×60×60 Å³**; **300 K vs 3000 K** runs to **150 ps** with elevated **O\(_2\)** density **~0.15 g/cm³** to accelerate chemistry in short windows. **Barostat / hydrostatic pressure control:** **N/A — NVT oxidation and coating stages** in the summarized protocol. **Electric field / enhanced sampling:** **N/A — not used** in the summarized protocol.

**Static QM / DFT:** covered under the **VASP/Jaguar** training blocks above (not a separate post-hoc DFT results section for the oxidation trajectories).

## Findings

- **ReaxFF** reproduces **Al/C interaction energies** from **QM** for the training comparisons presented, and **qualitatively** captures **hydrocarbon binding** and **surface reaction** sequences on **bare ANPs** (**abstract**).
- **Carbon layer growth** depends strongly on which **hydrocarbon precursors** are used (**abstract**).
- **Coatings** form with **H** migration to **Al** sites while often **preserving C–C** connectivity during deposition stages in the summarized trajectories (**abstract**).
- **Carbon-coated ANPs** are **less reactive** at **low temperature** but become **highly susceptible** to **oxidation** when the **coating** is **removed** or disrupted at **elevated temperature**—trends described as **consistent with experimental literature** in the abstract.

## Limitations

- **Combustion-relevant** conditions span **pressure, size polydispersity, and oxide polymorphism** beyond any single MD study.
- **ReaxFF** cannot capture **electronically excited** or **plasma-driven** chemistry without additional extensions.
- If **`Hong_AlCOx_JPCC_2016.pdf`** pagination differs from the ACS proof on [[2016hong-venue-research]], prefer the **journal version-of-record** for locators.

## Relevance to group

Core **Hong + van Duin** line on **energetic Al nanoparticles** and **passivation engineering**, tightly coupled to **ReaxFF parameterization practice**.

## Citations and evidence anchors

- Abstract in `papers/Hong_AlCOx_JPCC_2016.pdf`; **DOI:** `10.1021/acs.jpcc.6b00786`.

## Related topics

- [[2016hong-venue-research]]
- [[reaxff-family]]
