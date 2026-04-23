---
id: paper:2024chen-nat-reaxff-molecular
type: paper
title: "ReaxFF molecular dynamics simulation and experimental validation of chemical reactions of water and alcohols on SiC surfaces"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:mechanics-tribology
  - method:reaxff
  - material:widegap-semiconductor
  - task:experiment-integrated
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:validation-experiment
  - keyword:nvt-simulation
candidate_tags:
  - "CMP-SiC"
source_refs: []
doi: "10.1016/j.ceramint.2023.11.070"
year: 2024
authors:
  - "Haibo Chen"
  - "Jiapeng Chen"
  - "Jiexiong Wu"
  - "Juanfen Shen"
  - "Yunyun Gu"
  - "Tao Sun"
venue: "Ceram. Int. 50 (2024) 4332–4349"
pdf_sha256: "c9695c32191caabe4e5eb72e36454c17d4a808841f52dbc4b2a807c10fb25485"
pdf_path: "papers/ReaxFF_others/Chen_SiC_water_alcohol_Ceramics_Int_2024_reduced.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024chen-nat-reaxff-molecular -->

!!! note "Filename vs venue"
    The slug contains **nat** but the publication is **Ceramics International** (not Nature-branded).

## Summary

Silicon carbide’s hardness and chemical inertness make wafer processing challenging; chemical mechanical polishing (CMP) is widely used, yet the molecular-level oxidation chemistry of SiC in water versus alcohol-based slurries remains disputed. Chen et al. combine ReaxFF molecular dynamics for solvent films on 6H–SiC (001) with CMP-style experiments, atomic force microscopy, and X-ray photoelectron spectroscopy. The reactive simulations follow bond making and breaking as water and alcohols approach and react with the surface. Experiments compare material removal rates for aqueous versus alcoholic polishing environments and relate morphology and surface chemistry to the simulated reactivity ordering. The introduction motivates alcohol solvents by citing prior fixed-abrasive polishing work where methanol and ethanol improved material removal rate and surface finish relative to aqueous slurries, framing an open question about how hydroxyl-bearing solvents alter SiC surface chemistry compared with water-dominated routes.

## Methods

### ReaxFF interface MD (B)

**6H–SiC (001)** with explicit **water** and **alcohol** solvents at temperatures stated in *Ceram. Int.*; trajectory stages follow **undercoordinated** **Si/C** approach, **adsorption**, **bond cleavage**, and **oxygen** incorporation consistent with the abstract’s **three-stage** oxidation narrative.

### Experiments (CMP + characterization)

**Removal-rate** measurements under controlled **slurry** chemistry; **AFM** morphology; **XPS** **oxide/hydroxide** speciation.

### Reproducibility checklist (primary text)

**ReaxFF** citation, **supercell**/**termination**, **solvent** coverage, **T/P**, **timestep**, **duration**, and **analysis** scripts—see *Ceramics International* **50**, **4332–4349** and **DOI** `10.1016/j.ceramint.2023.11.070` (aligned with **`[[2023chen-nat-reaxff-molecular]]`** for scientific content).

**Interface chemistry stages.** The reactive trajectories are organized into the **three-stage** oxidation narrative stated in the abstract: **undercoordinated** **Si/C** attack by **solvent** species, **Si–C** bond weakening, and growth of **Si–O–Si**-rich **oxidized** networks. **Alcohol** solvents alter **H-bond** donation and **alkoxy**-mediated pathways versus **water-only** films, which the authors connect to differences in **removal rate** between **CMP** conditions.

**MD application (ReaxFF, 6H–SiC (001)).** **LAMMPS**+**ReaxFF** for **6H**–**SiC** (001) **slabs** wetted by **H\(_2\)O** and **alcohol** films: **NVT** equilibration and **production** at **temperature** setpoints in *Ceramics Int.*; **periodic** **PBC** in the **surface** plane, **N/A** for exact **lateral** **supercell** sizes and **atom** counts on this page. **Time step** (≈0.25 **fs** typical of **ReaxFF**; **N/A**—**exact** **fs** in **SI**), **Nosé–Hoover**/**Berendsen** **thermostat** settings, **equilibration** and **ns**-scale (or as stated) **trajectories**—see the **version-of-record** article. **N/A**—**NPT** **barostat**; **N/A**—**external** **E-field**; **N/A**—**metadynamics**; **Hydrostatic** **pressure** **N/A** for **NVT** **slab** films.

## Findings

### Reactivity vs polishing rates

**Simulated** solvent–surface **reactivity** ordering matches **experimental** **removal-rate** ordering.

### Mechanism

**Undercoordination attack → Si–C weakening → Si–O–Si network growth** via **OH/H** migration—supported by **AFM/XPS** trends.

### Alcohol vs water

Frames why **alcohol** slurries can **outperform** **water** in some **fixed-abrasive** CMP settings (**tribochemical** contribution, not abrasion alone).

## Limitations

Real CMP involves particles, fluid flow, and tribological contact pressures beyond flat-surface solvent MD. ReaxFF barriers are approximate relative to quantum methods.

## Relevance to group

External ReaxFF application to wide-bandgap semiconductor aqueous and alcoholic processing—methodologically comparable to group oxide reactive MD studies.

## Citations and evidence anchors

- DOI: `10.1016/j.ceramint.2023.11.070`

## Related topics

- [[reaxff-family]]
