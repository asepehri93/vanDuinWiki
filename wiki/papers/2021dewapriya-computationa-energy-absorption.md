---
id: paper:2021dewapriya-computationa-energy-absorption
type: paper
title: "Energy absorption mechanisms of nanoscopic multilayer structures under ballistic impact loading"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:alloys-metallurgy
  - method:classical-md
  - material:alloy-bulk
  - material:polymer-organic
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:classical-ff
  - keyword:lammps
  - keyword:shock-compression
  - keyword:msst
  - keyword:hugoniot
source_refs: []
doi: "10.1016/j.commatsci.2021.110504"
year: 2021
authors:
  - "M.A.N. Dewapriya, R.E. Miller"
venue: "Comput. Mater. Sci. 195 (2021) 110504"
pdf_sha256: "fe22eb2c242c1b55086c8ab3edd2a65e137d4b6e197c4ae7151ed254c5005e3c"
pdf_path: "papers/Others/Denapria_ballistic_impact_CompMatSci_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021dewapriya-computationa-energy-absorption -->


## Summary

Large-scale **molecular dynamics** in **LAMMPS** studies ballistic **impact** of **rigid** **nanoscale** projectiles on ultrathin **aluminum** and **polyurea** **films** and their **multilayers**. The interatomic model combines **EAM** **aluminum** with **PCFF** plus the **Interface Force Field (IFF)** for **polyurea** **nonbonded** and **cross-link** **behavior** as defined in the article. **MSST** **Hugoniot** **validation** on **NPT**-equilibrated (≈**300** **K**) **cubic** ~5 **nm** **supercell**s **precedes** **NEMD** **ballistic** **impact** in **NVE** **NEMD** at about **1.5** **km** **s⁻¹** on the named stacks (Al3, Pu3, Al3_Pu3_3) with **polyurea** on the strike or back **face** as the **manuscript** describes. The work emphasizes how **layer** order and **tensile** **release**-wave **reverberation** **affect** **absorbed** **energy** in these **nanolaminate** **targets**.

## Methods

### Interatomic models and Hugoniot validation (MSST, NPT preshock)

EAM **aluminum** and **PCFF**+**IFF** **polyurea** follow the *Comput. Mater. Sci.* 195:110504 reference set. **Cubic** **≈**5 **nm** **supercell**s undergo **NPT** **equilibration** at **300** **K** and are then **shock**-loaded with the multi-scale **shock** **technique** **MSST** along **z** with **shock** speed **\(U_s\)** **above** the **bulk** sound speed. **Hugoniot** **\(U_s\)**–**\(U_p\)** behavior is compared in the text to **Wang–Li** and **Nellis** **aluminum** and **Mock** **polyurea** **shock** data. **N/A** for a *de novo* **ReaxFF**/QM reparameterization study: these are **classical** **FF**s from the **literature** per the **citations**.

### MD application (ballistic NEMD in LAMMPS)

- **Engine / code:** **LAMMPS** **molecular** **dynamics** models **rigid** **cylindrical** **projectiles** (~7.7 **nm** **diameter**, ~8.1 **nm** **height**) **impacting** **multilayer** **targets** (Al3, Pu3, Al3_Pu3_3), **varying** which **face** **carries** **polyurea** on the **striker** side, default **1.5** **km** **s⁻¹** **unless** a **velocity** **sweep** changes it. The **target** **disk** is ~43 **nm** **across** with a **fixed** **outer** **rim** and a **~**40 **nm** deformable **interior**; in-plane **PBC**; full **atom** **counts** and all dimensions in `pdf_path`.
- **Ensemble, timestep, duration, thermostat, barostat, pressure, temperature:** after **MSST** **Hugoniot** **stages**, **NEMD** **impact** uses **NVE** **NEMD** **production** (no **Nose**–**Hoover** or **Berendsen** **thermostat** during that **NVE** **segment**); the **Hugoniot** leg is **NPT** **(300** **K)**-class **equilibration** **before** **shock** **(see** the **NVT**/**NPT** **vs** **NVE** **split** in `pdf_path`. **Time** **step** in **fs** and run **ps** / **ns** in the **10-step** protocol: **article** and **SI**.
- **Shock, stress, barostat, pressure, temperature:** **virial** **stress** and **shock** **pressure** (time-**averaged** in **2.5** **fs** windows) **in** the **stated** protocol; local **temperature** under the **striker** with center-of-**mass** subtractions as in the **manuscript**. **GPa**-scale **stress** (continuum data in the text) and **1** **bar** reference for **NPT** **preshock** **cell**; **N/A** for **NPT** **Parrinello**–**Rahman** **barostat** **during** the **NVE** **NEMD** **impact** **leg**.
- **Shear, electric field, umbrella, metadynamics, replica exchange:** **NEMD** **impact** after **MSST** as the **paper** **defines**; **electric** **field** and **replica**/**umbrella** **sampling** **N/A** in the summarized protocol. Optional **bi-crystal** **Al** **models** in the **publication** probe **grain**-**boundary** **effects**.

## Findings

Nanoscale **simulations** show a **polyurea** **strike** **face** is associated with **lower** **damage** **relative** to a back-face **polyurea** **arrangement** where **shock** **reverberation** **weakens** the **polyurea** in **thinner** **films** in the **trends** the **authors** report. **Shock** **pressure** and adiabatic **heating** **increase** as **aluminum** or **polyurea** **films** **thin** in the **stated** **scans**. **Perforation** **tracks** two **resistance** **stages** **tied** to **tensile** **release** after **shock** **reflection** at **free** **surfaces**; **nanometer**-**scale** **striker** **diameter** **affects** **absorbed** **energy** in the **NEMD** **curves**. **MSST** **\(U_s\)**–**\(U_p\)** relations for Al and **polyurea** **rationalize** **wave** **reverberation** **arrival** **and** **timing** **next** to **NEMD** **deformation** **features**; **laboratory** **ballistic** limits **differ** in the **authored** **Limitations**. Citable **numerical** data live in the **VOR** **PDF** in `pdf_path`—**extract**-thin **web** text here is a **summary** only.

## Limitations

Reactive bond breaking is not fully enabled in the polymer model (PCFF_IFF); projectile rigidity neglects penetrator deformation. Nanoscale conditions differ from macroscopic ballistic tests emphasized in the introduction.

## Relevance to group

Non-ReaxFF atomistic mechanics paper in the corpus; useful contrast to reactive MD workflows elsewhere. The **MSST** Hugoniot validation step is a concrete hook for comparing **continuum shock** relations against **atomistic** wave structure in nanoscale targets.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1016/j.commatsci.2021.110504](https://doi.org/10.1016/j.commatsci.2021.110504)

## Related topics

- [[theme-reactive-md-corpus]] (contrasts **non-ReaxFF** **classical MD** / **MSST** Hugoniot validation with reactive workflows elsewhere in the KB)
