---
id: paper:2015dbm-venue-microsoft-word
type: paper
title: "Atomistic investigation of ablation of amorphous polystyrene under femtosecond laser pulse"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reactive-md-generic
  - material:polymer-organic
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:polymer
  - keyword:reactive-md
  - keyword:classical-ff
source_refs: []
doi: "10.1007/s11433-014-5587-x"
year: 2015
authors:
  - "Huang YanHua"
  - "Song ChengWei"
  - "Zhang JunJie"
  - "Sun Tao"
venue: "Science China Physics, Mechanics & Astronomy"
pdf_sha256: "32c72329c568f039930211dd423f2bf21b5abab3fddc87802df80b1464a7dabf"
pdf_path: "papers/Others/Wang_AIREBO_polystyterene_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015dbm-venue-microsoft-word -->

## Summary

Femtosecond laser processing of polymers is used in micromachining and fusion targets, but experimental diagnostics struggle to resolve atomic-scale mechanisms during the pulse. Huang et al. report atomistic molecular dynamics of femtosecond laser ablation of amorphous polystyrene, emphasizing full atomistic chains with pendant phenyl groups rather than coarse-grained bead models. They vary laser pulse intensity as an extrinsic control and molecular architecture—placement of phenyl side groups—as an intrinsic control, linking microscopic deformation modes to macroscopic ablation response. The introduction notes prior coarse-grained breathing-sphere polymer models and argues that full atomistic polystyrene is needed to resolve chain-level motions during ultrafast heating.

## Methods

### MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** **molecular dynamics** with **velocity-Verlet** integration using the **AIREBO** potential for **full-atomistic polystyrene** (Huang *et al.*, *Sci. China Phys. Mech. Astron.* **58**, 037002 (2015)).
- **System size & composition:** **488** atactic polystyrene chains assembled into an **amorphous** substrate of approximate dimensions **8 nm × 16 nm × 8 nm** (x/y/z) with mass density **~814.7 kg m⁻³**; additional runs compare **isotactic**, **syndiotactic**, and **atactic** tacticities at the same modeling level.
- **Boundaries / constraints:** **PBC in x and z**; **free surface in y**; the **bottom 1 nm** of the substrate is **fixed** during ablation to anchor the film.
- **Pre-ablation conditioning:** substrates are relaxed at **0 bar** and **30 K** for **50 ps** before laser exposure (Section 2).
- **Laser coupling protocol (photothermal MD):** the authors mimic a **photothermal** picture by **depositing kinetic energy equal to photon energy** onto atoms in an **irradiated region** during the **short laser pulse**, with an **intensive** control parameter (documented in Section 2/equations) that sets how strongly energy is coupled into the irradiated volume; this is **not** an explicit two-temperature electronic-fluid solve in the excerpted Methods text.
- **Timestep:** **0.1 fs** integration with **AIREBO** (as stated in Section 2).
- **Stages:** an **irradiation** stage is followed by an **adsorbed-energy dissipation** stage tracked for **multi-ps** relaxation (e.g., temperature and thickness evolution discussed around **0–10 ps** in the text/figures).
- **Ensemble:** the dynamics segments after pre-conditioning are propagated in the **microcanonical (NVE)** ensemble (as stated in the *Sci. China* article text), consistent with energy-injection ablation followed by **internal energy redistribution** without an external **thermostat** during the hot **MD** stages.
- **Thermostat / barostat / pressure:** **constant-volume** **NVE** dynamics implies **no Parrinello–Rahman barostat** and **no hydrostatic pressure control**; external **GPa**/**bar** **stress** loading is **N/A —** not part of the laser **MD** protocol (pre-ablation relaxation uses **0 bar** target as stated).
- **Shear / shock / fields:** **N/A —** no sustained mechanical shear; **electric-field** effects enter only indirectly through the **laser** coupling model.

### Force-field training

**N/A —** uses the published **AIREBO** hydrocarbon reactive potential (cited from the original AIREBO reference).

### Static QM / DFT

**N/A —** not used as an on-the-fly engine in this MD study.

## Findings

- **Dual removal modes:** ablation-induced removal proceeds by **surface evaporation** (ejection of chains/clusters) and **bulk expansion** with **void** formation, consistent with the abstract and Section 3 discussion.
- **Microscopic deformation:** **inter-chain sliding** and **intra-chain** conformational change (including **phenyl** dihedral rotations highlighted for an ejected chain case) accompany energy dissipation.
- **Intensity thresholding (atactic case):** tabulated **LF/MF/HF** laser-intensity cases show a **threshold** below which little **length increment / clustering** occurs, and above which **substrate lengthening**, **voiding**, and **cluster counts** rise sharply (Table 1 in the PDF).
- **Tacticity lever:** under the same nominal pulse conditions, **isotactic** samples show the **largest** post-pulse temperatures/length increments in the reported table, indicating **molecular architecture** changes ablation severity through packing and heat accommodation.

## Limitations

Energy is deposited as **prescribed atomic kinetic-energy boosts** in a **photothermal** MD picture, so **explicit electronic dynamics**, **chromophore-specific** absorption, and **wavelength-dependent** effects are not modeled at first-principles fidelity.

## Relevance to group

Illustrates reactive or bond-order hydrocarbon modeling for extreme heating distinct from typical ReaxFF combustion training sets—useful contrast in the polymer laser niche.

## Related topics

- [[reaxff-family]]
