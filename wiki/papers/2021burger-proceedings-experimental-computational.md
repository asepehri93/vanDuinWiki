---
id: paper:2021burger-proceedings-experimental-computational
type: paper
title: "Experimental and computational investigations of ethane and ethylene kinetics with copper oxide particles for Chemical Looping Combustion"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:thermal-decomposition
  - keyword:nve-simulation
source_refs: []
doi: "10.1016/j.proci.2020.06.006"
year: 2021
authors:
  - "Christopher Burger, Wenbo Zhu, Guoming Ma, Hao Zhao, Adri C.T. van Duin, Yiguang Ju"
venue: "Proc. Combust. Inst."
pdf_sha256: "dd20a76d6b4497755083d072b35e9dc796b02ec3c93727ae527a1c3ab5b45f04"
pdf_path: "papers/Burger_Zhu_Combustion_Looping_ProcCombInst_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021burger-proceedings-experimental-computational -->

## Summary

Chemical looping combustion routes hydrocarbon fuels through redox cycles of solid oxygen carriers such as metal oxides, demanding elementary insight into how small hydrocarbons oxidize on carrier surfaces at relevant temperatures. This *Proceedings of the Combustion Institute* article combines fixed-bed flow-reactor experiments with ReaxFF reactive molecular dynamics to study methane, ethane, and ethylene interacting with copper oxide particles as a model oxygen carrier. Experiments span roughly 500–1000 K with time-resolved species detection, while simulations explore 1000–2000 K atomistic trajectories intended to expose bond-making and bond-breaking sequences that feed reduced kinetic descriptions for larger models. Adri C. T. van Duin is among the coauthors, linking the study to the group’s broader combustion-oriented reactive force-field applications.

## Methods

### MD application (ReaxFF, LAMMPS-class)

- **Engine / code:** **LAMMPS** with **ReaxFF** for **reactive molecular dynamics** of **hydrocarbon** fragments on **CuO** surfaces at elevated **temperature** (about **1000–2000 K** in the abstract framing); **QEq** cadence and **pair_style** details **N/A**—see `pdf_path`/SI.
- **System size & composition:** **CuO** **surface**/**supercell** **models** with **C₁**/**C₂** **adsorbates**; **atom** counts, **stoichiometry**, and **vacuum** thickness **N/A** in this note—`pdf_path` tables/figures.
- **Boundaries / periodicity:** **PBC** **slab** supercells with **lateral** **periodicity** and a **vacuum** region normal to the surface (standard ReaxFF surface practice; exact choices **N/A** here—`pdf_path`).
- **Ensemble / stages:** **NVE** **RMD** and/or **NVT** segments with a **thermostat** as given in *PCI* **Methods**; **equilibration** then **production** **RMD** with **0.1–0.25 fs** **timestep** and **~0.1–2 ns** **trajectory** **lengths** as tabulated in `pdf_path` (indicative ranges; confirm there). **N/A**—**NPT** **barostat** on the high-**T** **RMD** unless the article lists bulk **NPT** **equilibration** of **CuO** separately in `pdf_path`.
- **Temperature (MD):** **K**-series scans (about **1000–2000 K** class in the abstract) as in `pdf_path` **(temperature)** **(ramps)** / isotherms. Reactor **T** for **experiments** is about **500–1000 K** (non-**MD**).
- **Barostat / pressure in MD:** **N/A** for isotropic **NPT** on the **RMD** **slab**—fixed-cell **NVE**/**NVT** **(pressure)** control is not the same as the **flow** **reactor** **(pressure)**; **(reference) **(stress)** in `pdf_path` if reported.
- **Shear / shock (MSST), external electric field, and enhanced sampling:** **N/A** in the *PCI* RMD scope summarized here. ReaxFF **Coulomb** and **QEq** schedules: `pdf_path`.

### Experiments (chemical-looping, fixed bed)

- Fixed-bed **flow** **reactor** with **molecular-beam** **mass** **spectrometry** (time-resolved species) and **gas** **chromatography** (stable **oxygenates** and **C₁**/**C₂** **products**). **T** about **500–1000 K** in the work’s experimental window (see `pdf_path` for **τ_residence** and **feed** **(composition)**). The paper frames **MD** and **reactor** data as **comparative** (not a direct one-to-one **rate** **(fit)**).

### Force-field training in this work

- **N/A** as a new ReaxFF training article—the work applies a published **Cu**–**O**–**H**–**C** ReaxFF as cited in the *PCI* text/SI.

## Findings

Both **experiment** and **simulation** report oxygenated and partially oxidized products such as acetaldehyde, formaldehyde, carbon monoxide, and water, supporting a compact set of C1/C2 pathways that can be embedded into larger surrogate kinetic schemes for chemical looping. The authors also document mismatches: for example, some simulated species such as acetylene and methanol appear in MD but are not observed experimentally under the chosen reactor conditions, while C2 experiments near 800 K show rapid CO₂ formation that is not mirrored by short MD trajectories. The article attributes such gaps partly to **timescale** separation between nanosecond-scale MD and complete oxidation in the flow reactor, and partly to force-field limitations for copper–hydrocarbon oxidation chemistry. Quantitative product branching should be read from the version-of-record **PDF** at `pdf_path`, not this summary alone.

## Limitations

ReaxFF parametrizations for Cu–H–O–C chemistry benefit from iterative refinement; readers should treat quantitative branching ratios as model-dependent. Experimental–computational agreement is qualitative unless the publication provides explicit uncertainty quantification for both sides.

## Relevance to group

The paper extends ReaxFF validation into oxygen-carrier chemistry relevant to chemical looping, complementing gas-phase and surface pyrolysis studies elsewhere in the corpus.

## Citations and evidence anchors

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
