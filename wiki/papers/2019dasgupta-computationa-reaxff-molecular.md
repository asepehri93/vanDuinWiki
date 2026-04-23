---
id: paper:2019dasgupta-computationa-reaxff-molecular
type: paper
title: "ReaxFF molecular dynamics simulations on the structure and dynamics of electrolyte water systems at ambient temperature"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:nvt-simulation
  - keyword:lammps
source_refs: []
doi: "10.1016/j.commatsci.2019.109349"
year: 2019
authors:
  - "Nabankur Dasgupta"
  - "Yun Kyung Shin"
  - "Mark V. Fedkin"
  - "Adri C. T. van Duin"
venue: "Computational Materials Science, 172 (2020) 109349 (published 2020; manuscript 2019)"
pdf_sha256: "7a62c0375b508f19e0517f0c9e49209b41d13c0a848cc0995cfd02a3e6ae151b"
pdf_path: "papers/Nabankur_2019_CompMatSci_electrolyte.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019dasgupta-computationa-reaxff-molecular -->

## Summary

ReaxFF MD studies aqueous LiCl, NaCl, and KCl at 1, 3, and 5 M (plus pure water) using the Fedkin et al. electrolyte-water parameterization. The work targets atomistic structure and dynamics of concentrated electrolytes at ambient temperature—settings relevant to electrochemical interface modeling where water reorganizes around alkali cations and halide anions. Structural metrics (RDFs, angles in the first solvation shell), hydrogen-bond and reorientational dynamics, residence times, and diffusion coefficients are compared among salts and against ab initio and non-reactive references where cited. The authors relate transient species (metal hydroxides/chlorides) to observed diffusion trends and argue concentration always reduces water mobility in the regimes studied without strong ion specificity, framing the results as a force-field-level map of how salt identity and strength couple to water mobility.

## Methods

**Systems.** **Molecular dynamics (MD)** cells use **1000 water molecules** for pure water or **700 water molecules** plus stoichiometric salt for electrolytes; **atom counts** follow from those water counts plus the ions listed for each target **1–5 M** **LiCl**, **NaCl**, and **KCl** composition in **Table 1**. **Box volumes** are set from **ion van der Waals radii** and the target concentration as described in **Computational details**.

**Protocol.** The article reports **energy minimization**, **compression**, gradual **heating to 300 K**, **100 ps** equilibration at **300 K**, then **0.5 ns** production; dynamical analyses use the **last 200 ps**. Integration uses **Velocity Verlet** with a **0.25 fs** timestep. **Periodic boundary conditions (PBC)** are used for the bulk liquid cells.

**Thermostat / ensemble.** Temperature is controlled with a **Berendsen thermostat** (**100 fs** damping constant, as stated in the article). The workflow is **constant-volume** sampling at **~300 K**, i.e., **NVT**-equivalent thermal control without a variable cell.

**Pressure / barostat.** **N/A — hydrostatic pressure** servocontrol (**NPT** barostat) is **not used**; the box volume is fixed to match target **molarity** rather than a **GPa**/**bar** pressure target.

**Reactive model.** Simulations use the **Fedkin et al.** **electrolyte–water ReaxFF** parameterization, retaining **bond-order** updates that allow **speciation** beyond fixed-charge water models (including formation/dissolution motifs discussed in the Results).

**Engine / code.** **LAMMPS** for **ReaxFF** integration (same stack as other Fedkin-line electrolyte–water papers; confirm build/version strings in the **Comput. Mater. Sci.** **PDF**/**SI** if needed).

**Electric fields / enhanced sampling.** **N/A —** bulk electrolyte benchmarking without applied field or rare-event biasing in the summarized protocol.

**Analysis.** RDFs, angular distributions, ion–water residence times, hydrogen-bond lifetimes, reorientational correlation functions, and diffusion coefficients from **MSD**-based analysis consistent with the **200 ps** analysis window.
## Findings

ReaxFF reproduces solvation-shell structure and angular behavior in reasonable agreement with literature/DFT references. Ion-specific and concentration effects on water dynamics are dissected; ReaxFF captures formation/dissolution of some ionic aggregates over trajectories, used to rationalize diffusion. The study reports that, within the modeled conditions, increasing salt concentration reduces water self-diffusivity without the ion specificity suggested by some simpler pictures, and the discussion ties those trends to the evolving population of contact-ion-pair motifs and transient hydroxide/chloride-containing species observed along individual trajectories.

## Limitations

Sub-nanosecond segments and finite-size effects; force-field dependence inherited from the 2019 electrolyte parameterization.

## Relevance to group

van Duin group application paper building directly on Fedkin JPCA electrolyte ReaxFF.

## Citations and evidence anchors

https://doi.org/10.1016/j.commatsci.2019.109349

## Reader notes (navigation)

- Electrolyte parameterization context: [[2019fedkin-j-phys-chem-development-reaxff]]; broader aqueous interfaces: [[batteries-interfaces-reaxff]].
- Elsevier in-press duplicate PDF is catalogued under [`2019dasgupta-computationa-reaxff-molecular-2`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) in the non-primary article list.

## Related topics

- [[2019fedkin-j-phys-chem-development-reaxff]]
- [[reaxff-family]]
