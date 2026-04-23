---
id: paper:2019ashraf-j-phys-chem-reactive-molecular
type: paper
title: "Reactive Molecular Dynamics Simulations of the Atomic Oxygen Impact on Epoxies with Different Chemistries"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - material:polymer-organic
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:polymer
source_refs: []
doi: "10.1021/acs.jpcc.9b03739"
year: 2019
authors:
  - "Chowdhury Ashraf; Aniruddh Vashisth; Charles E. Bakis; Adri C. T. van Duin"
venue: "J. Phys. Chem. C 2019.123:15145-15156"
pdf_sha256: "c866735dc9a8d1140590c4887175fac23663716f86e838c4ef62a3609e8baebf"
pdf_path: "papers/Ashraf_JPC_C_2019_polymeroxidation.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2019ashraf-j-phys-chem-reactive-molecular -->

## Summary

ReaxFF molecular dynamics is used to simulate hypervelocity atomic oxygen (AO) impact on cross-linked thermosetting epoxy networks built with an accelerated ReaxFF cross-linking workflow. The work compares chemistries (including aromatic vs aliphatic curatives), cross-link density, and temperature, and relates network structure to erosion resistance under AO impact relevant to low Earth orbit environments. **LEO** **AO** flux is **oxidizing** and **energetic** enough to **etch** **organic** **binders** in **composites**; the paper frames **atomistic** **erosion** as a **chemistry**-selective process where **network** **topology** and **aromatic** content modulate **bond** **scission** rates under repeated **hypervelocity** **O** impacts.

## Methods

**Force field and LEO AO representation.** The study uses **ReaxFF** reactive MD to treat **hypervelocity atomic oxygen (AO)** impacts on **cross-linked thermosetting epoxy** networks. The introduction frames **AO** speeds near **~7–8 km s⁻¹**, corresponding to roughly **~4.5–5 eV** per oxygen atom at reported **flux** orders of **~10¹⁴–10¹⁵ atoms cm⁻² s⁻¹**. The authors emphasize **short-range repulsive training** in the **ReaxFF** parameterization used here, arguing that omitting repulsion can **overpredict** **AO damage**.

**Network construction (Accelerated ReaxFF cross-linking).** Epoxy slabs are built using the **Accelerated ReaxFF** cross-linking workflow (**restraint-assisted** barrier crossing with geometric cutoffs), intended to better respect **reaction barriers** compared with naive **distance-only** bond-formation recipes.

**MD application (LAMMPS).** **Engine / code:** simulations are performed with **LAMMPS** (as stated in the article). **Boundaries / periodicity:** epoxy slabs use **3D periodic boundary conditions (PBC)** in the plane of the slab with **free surface** along the **AO** approach direction, supplemented by the **reflective wall** treatment along **z** described in the computational details to confine atoms without unphysical loss through **boundaries**. **Pre-bombardment thermalization:** an **NVT** segment at **300 K** for **30 ps** stabilizes slab temperature after preparation. **Thermostat:** **NVT** equilibration uses a LAMMPS **thermostat** with coupling parameters given in the computational details (**PDF**). **AO bombardment segment:** an **NVE** trajectory follows, with **200** oxygen atoms initialized along **−z** with **~15 Å** spacing and **7.4 km s⁻¹** impact velocity (sign chosen so impacts occur into the slab), yielding **~200 fs** between successive impacts at the nominal spacing; the production **NVE** segment is **40 ps** with an integration timestep of **0.00005 ps** (**0.05 fs**) as reported in the computational details. **Barostat / pressure control:** **N/A —** the quoted bombardment protocol is **NVE** with **fixed box** considerations tied to the **AO train** setup rather than **NPT** stress control. **Electric fields / enhanced sampling:** **N/A —** not part of the summarized AO impact protocol.

**Design of experiments in simulation.** The authors compare **epoxide**/**curative** chemistries (including **aromatic vs cycloaliphatic vs aliphatic** curatives), vary **percent cross-linking** (including **0%, 50%, and 84%** cases discussed with **damage penetration depth** tables), and vary **slab temperature** (**103 K**, **300 K**, **396 K**) for selected systems.

**Analysis.** Post-impact diagnostics include **normalized mass loss**, **AO penetration depth distributions**, **small-molecule** counts (**H₂O**, **CO**, **OH**, **CH₂O**), and mechanistic snapshots of **bond rupture** pathways as reported in the figures.
## Findings

Epoxies cured with aromatic components show higher resistance to AO damage, attributed in part to stable aromatic moieties. Lower cross-link density and higher temperature accelerate disintegration. The study argues ReaxFF AO simulations can rank epoxy chemistries for spacecraft exposure scenarios when parametrization includes the relevant repulsive interactions.

**Ranking insight:** when **repulsive** **O–substrate** terms are included, **relative** **stability** orders among **curatives** align more closely with **mechanistic** expectations (**ring** stabilization vs **aliphatic** **backbone** vulnerability) than when only **bonded** **ReaxFF** terms from **ambient** chemistry training are used.

**Sensitivity / levers.** **Cross-linking** strongly affects **mass loss** and **AO penetration depth** (the paper reports representative **damage penetration depths** at **t = 40 ps** for selected **bisA/DETDA** cross-linking cases). **Slab temperature** shifts degradation kinetics: the **103 K** case shows the **least** mass loss and a **sharper** near-surface AO trapping profile relative to **300 K**/**396 K** in the plotted comparisons.

**Comparisons / validation posture.** The manuscript ties observed **fragmentation** trends to **bond dissociation energy** arguments and compares **ReaxFF BDEs** to **literature** values where noted; it positions the work as extending prior **AO + polymer** reactive MD studies by treating **cross-linked** networks rather than monomer slabs alone.

**Authored limitations (scope).** The study isolates **AO** chemistry and does not attempt to model concurrent **UV**, **electrons**, or **micrometeorite** damage channels noted as additional LEO degradation modes in the introduction.
## Limitations

Computational cost limits system sizes and exposure statistics; LEO flux and fluence are represented at the simulation-impact level rather than full mission dose. **UV** **photons**, **electron** **bombardment**, and **contaminant** **layers** on **flight** **hardware** can alter **erosion** **rates** relative to **pure** **AO** **impacts** modeled here.

## Relevance to group

van Duin group; reactive MD for polymer durability under atomic oxygen.

## Citations and evidence anchors

https://doi.org/10.1021/acs.jpcc.9b03739

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
