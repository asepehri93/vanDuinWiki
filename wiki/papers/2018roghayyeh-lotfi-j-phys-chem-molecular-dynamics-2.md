---
id: paper:2018roghayyeh-lotfi-j-phys-chem-molecular-dynamics-2
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
pdf_sha256: 30076823a9db83558b8572fa9a60106b6eb089b4dfc47a92940bf4ba1e96f0b3
pdf_path: papers/Lotfi_Lubricant_surfaces_JPC_C_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018roghayyeh-lotfi-j-phys-chem-molecular-dynamics-2 -->

## Summary

This slug registers an alternate **PDF** (`Lotfi_Lubricant_surfaces_JPC_C_2018.pdf`) for the same **J. Phys. Chem. C** article as **`[[2018roghayyeh-lotfi-j-phys-chem-molecular-dynamics]]`**, **DOI [10.1021/acs.jpcc.7b09660](https://doi.org/10.1021/acs.jpcc.7b09660)**, **volume 122**, pages **2684–2695** (2018). The work addresses **perfluoropolyether (PFPE)** **D4OH** lubricant **degradation** in **hard disk drive**-relevant environments using **ReaxFF reactive MD**. Simulations place **nine D4OH strands** with gas-phase **O₂** and **H₂O** and with **oxide nanoparticles** (**SiO₂**, **goethite** **FeO(OH)**, **Fe₂O₃**) at **T = 1500 K** to accelerate bond-making and bond-breaking. Nanoparticles appear in three **surface treatments**: **(1)** **untreated** fragments cut from crystals; **(2)** **dry-air** pretreatment; **(3)** **wet-air** pretreatment—intended to mimic realistic contamination and humidity. Motivation ties to **heat-assisted magnetic recording (HAMR)**, where elevated temperatures and contaminants can accelerate lubricant loss at the head–disk interface. The introduction in the article reviews **PFPE** chemistries (**Fomblin**/**Demnum** families), places **D4OH** in the **Demnum** class with specified end groups, and frames degradation modes relevant to HDD reliability (thermal, catalytic, mechanical shear, and electron-mediated pathways) before presenting the **1500 K** accelerated MD strategy.

## Methods
**1 — MD application (PFPE degradation).** **ReaxFF** simulations of **nine Demnum-class D4OH** strands are run with **O₂**, **H₂O**, and **oxide nanoparticles** (**SiO₂**, **goethite FeO(OH)**, **Fe₂O₃**) using **ADF**/**LAMMPS-class ReaxFF integration** as described in *J. Phys. Chem. C* (package name appears as **ADF** in the abstract/methods excerpt: **“All MD simulations were performed with the ADF package”**). **Ensemble:** **NVT** at **1500 K** for the accelerated degradation chemistry. **Timestep:** **0.1 fs** (selected timestep in the article). **Thermostat:** **Berendsen** with **250 fs** damping constant as quoted. **Nanoparticles:** **16 Å** diameter **silica** example size appears in the methods discussion; surfaces are prepared **untreated**, **dry-air pretreated**, or **wet-air pretreated**. **Trajectory lengths:** representative segments include **500 000** steps (**~50 ps**) and **1 000 000** steps (**~100 ps**) at **1500 K** for specific degradation stages quoted in the paper. **PBC:** **three-dimensional PBC** for gas+NP+strand supercells. **Barostat / pressure:** **N/A —** **NVT** gas-phase cells without **NPT** barostat in the excerpted protocol. **Electric fields / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** applies a published **C/F/O/H** (**PFPE** + oxide) **ReaxFF** parametrization.

**3 — Experiments / continuum.** **N/A —** motivation references **HDD** tribology literature rather than new experiments here.

**Duplicate PDF note:** manifest alternate bytes at `papers/Lotfi_Lubricant_surfaces_JPC_C_2018.pdf` for the same article as **[[2018roghayyeh-lotfi-j-phys-chem-molecular-dynamics]]**.

## Findings
**Outcomes / mechanisms:** **Water** strongly accelerates **D4OH** degradation versus **O₂**-only environments at the **1500 K** accelerated conditions; **any nanoparticle** presence accelerates chemistry versus gas-only controls. **Untreated SiO₂** and **goethite** outperform their **dry/wet-air passivated** counterparts in degradation rate, whereas **wet-air-treated Fe₂O₃** gives the strongest acceleration among the **iron-oxide** cases studied.

**Comparisons:** trends are discussed relative to **industry HDD/HAMR** humidity concerns and prior **PFPE** degradation literature.

**Sensitivity:** **NP chemistry**, **pretreatment**, and **humidity** are primary levers; **1500 K** is a **computational acceleration** temperature.

**Limitations:** device-relevant **temperatures** and **shear** are not fully captured by the high-**T** gas-cell protocol.

**Corpus honesty:** numbers above come from **`papers/Lotfi_CF_OxideNP_JPC_C_2018.pdf`**; confirm wording against your **VOR** PDF.

**Corpus honesty:** same scientific content as sibling slug; cite whichever **PDF** your tree mounts.

## Limitations

Duplicate **PDF** paths should be consolidated when safe for provenance. **1500 K** is a **computational acceleration** temperature; quantitative rates are not direct device predictions without extrapolation. **HAMR** device temperatures and **shear**-driven chemistry are not fully captured by gas-phase **NP** + **strand** setups alone, so the study is best read as a **compositional** screen of **humidity**, **O₂**, and **oxide** effects on **PFPE** scission propensity.

## Relevance to group

**Adri C. T. van Duin** co-authors; **ReaxFF** application to **PFPE** **tribochemistry** with **oxide** contaminants and **humidity**.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.7b09660](https://doi.org/10.1021/acs.jpcc.7b09660)
- Journal: *J. Phys. Chem. C* **122**, 2684–2695 (2018).

## Reader notes (navigation)

- Sibling PDF: [[2018roghayyeh-lotfi-j-phys-chem-molecular-dynamics]]

## Related topics

- [[2018roghayyeh-lotfi-j-phys-chem-molecular-dynamics]]
- [[reaxff-family]]
