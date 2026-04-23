---
id: paper:2018roghayyeh-lotfi-j-phys-chem-molecular-dynamics
type: paper
title: Molecular Dynamics Simulations of Perfluoropolyether Lubricant Degradation
  in the Presence of Oxygen, Water, and Oxide Nanoparticles using a ReaxFF Reactive
  Force Field
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:mechanics-tribology
- domain:reactive-md
- domain:oxides-ceramics
- method:reaxff
- task:application
- scale:atomistic
paper_keywords:
- keyword:tribology
- keyword:reaxff-application
- keyword:oxide-surface
- keyword:water-interfaces
- keyword:reactive-md
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcc.7b09660
year: 2018
authors:
- Roghayyeh Lotfi
- Adri C. T. van Duin
- Mousumi Mani Biswas
venue: J. Phys. Chem. C
pdf_sha256: 74b8ffeb41f2e47e699009775c829abe4245488de8c326c78038e5fa27f3ec88
pdf_path: papers/Lotfi_CF_OxideNP_JPC_C_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018roghayyeh-lotfi-j-phys-chem-molecular-dynamics -->

## Summary

**Heat-assisted magnetic recording (HAMR)** pushes **disk** temperatures high enough to threaten **perfluoropolyether (PFPE)** **lubricants**, especially in the presence of **humidity** and **oxide** **contaminants** at the **head–media** interface. **Industry** **context** matters for interpreting the **1500 K** **simulation** **temperature**: the **goal** is not to **mimic** **steady** **disk** **temperatures** but to **sample** **rare** **bond-breaking** **events** within **accessible** **trajectory** **lengths**, analogous to **accelerated** **life** **testing** in **reliability** **engineering**. **Lotfi**, **van Duin**, and **Biswas** simulate **nine** **Demnum-class D4OH** strands with **O\(_2\)**, **H\(_2\)O**, and **SiO\(_2\)**, **goethite FeO(OH)**, or **Fe\(_2\)O\(_3\)** **nanoparticles** using **ReaxFF MD** at **1500 K** to accelerate **C–O** and **C–F** **bond** **scission** chemistry. **Nanoparticles** appear **untreated**, **dry-air-treated**, or **wet-air-treated** to mimic **ambient** **exposure** pathways relevant to **Western Digital**-style **HDD** manufacturing concerns.

## Methods
**1 — MD application (PFPE degradation).** **ReaxFF** simulations of **nine Demnum-class D4OH** strands are run with **O₂**, **H₂O**, and **oxide nanoparticles** (**SiO₂**, **goethite FeO(OH)**, **Fe₂O₃**) using **ADF**/**LAMMPS-class ReaxFF integration** as described in *J. Phys. Chem. C* (package name appears as **ADF** in the abstract/methods excerpt: **“All MD simulations were performed with the ADF package”**). **Ensemble:** **NVT** at **1500 K** for the accelerated degradation chemistry. **Timestep:** **0.1 fs** (selected timestep in the article). **Thermostat:** **Berendsen** with **250 fs** damping constant as quoted. **Nanoparticles:** **16 Å** diameter **silica** example size appears in the methods discussion; surfaces are prepared **untreated**, **dry-air pretreated**, or **wet-air pretreated**. **Trajectory lengths:** representative segments include **500 000** steps (**~50 ps**) and **1 000 000** steps (**~100 ps**) at **1500 K** for specific degradation stages quoted in the paper. **PBC:** **three-dimensional PBC** for gas+NP+strand supercells. **Barostat / pressure:** **N/A —** **NVT** gas-phase cells without **NPT** barostat in the excerpted protocol. **Electric fields / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** applies a published **C/F/O/H** (**PFPE** + oxide) **ReaxFF** parametrization.

**3 — Experiments / continuum.** **N/A —** motivation references **HDD** tribology literature rather than new experiments here.

## Findings
**Outcomes / mechanisms:** **Water** strongly accelerates **D4OH** degradation versus **O₂**-only environments at the **1500 K** accelerated conditions; **any nanoparticle** presence accelerates chemistry versus gas-only controls. **Untreated SiO₂** and **goethite** outperform their **dry/wet-air passivated** counterparts in degradation rate, whereas **wet-air-treated Fe₂O₃** gives the strongest acceleration among the **iron-oxide** cases studied.

**Comparisons:** trends are discussed relative to **industry HDD/HAMR** humidity concerns and prior **PFPE** degradation literature.

**Sensitivity:** **NP chemistry**, **pretreatment**, and **humidity** are primary levers; **1500 K** is a **computational acceleration** temperature.

**Limitations:** device-relevant **temperatures** and **shear** are not fully captured by the high-**T** gas-cell protocol.

**Corpus honesty:** numbers above come from **`papers/Lotfi_CF_OxideNP_JPC_C_2018.pdf`**; confirm wording against your **VOR** PDF.

## Limitations

Single high temperature and short timescales probe accelerated chemistry; quantitative rates may not map linearly to device temperatures without extrapolation.

## Relevance to group

Adri C. T. van Duin co-authors; demonstrates ReaxFF for PFPE tribochemistry with oxide contaminants.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.7b09660](https://doi.org/10.1021/acs.jpcc.7b09660) — *J. Phys. Chem. C* **122**, 2684–2695 (2018).

## Related topics

- [[reaxff-family]]
