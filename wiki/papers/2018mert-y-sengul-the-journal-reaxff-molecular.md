---
id: paper:2018mert-y-sengul-the-journal-reaxff-molecular
type: paper
title: ReaxFF molecular dynamics simulation of intermolecular structure formation
  in acetic acid-water mixtures at elevated temperatures and pressures
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:water-silica-geo
- domain:reactive-md
- domain:reaxff-lineage
- material:polymer-organic
- method:reaxff
- method:enhanced-sampling
- task:application
- scale:atomistic
paper_keywords:
- keyword:reaxff-application
- keyword:water-interfaces
- keyword:enhanced-sampling
- keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: 10.1063/1.5025932
year: 2018
authors:
- Mert Y. Sengul
- Clive A. Randall
- Adri C. T. van Duin
venue: J. Chem. Phys. 2018, 148, 164506
pdf_sha256: daeb3e1add7e37d52b00533624e790b6a9336af8f8b4fcb04eded8c3439c224f
pdf_path: papers/Sengul_aceticacid_water_JCP_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018mert-y-sengul-the-journal-reaxff-molecular -->

## Summary

Acetic acid and water mix in technologically relevant ways—from acid catalysis to solution processing—and their hydrogen-bonded aggregates depend on temperature, pressure, and composition. This Journal of Chemical Physics article presents ReaxFF molecular dynamics of acetic acid–water mixtures across acid mole fractions down to \(x_{\mathrm{HAc}} \ge 0.2\), spanning ambient and near-critical conditions. The authors use metadynamics to refine the free-energy profile for acid dissociation and adjust the ReaxFF dissociation energy accordingly, seeking internal consistency between enhanced-sampling estimates and the reactive force field’s treatment of proton transfer. Randall and van Duin co-authorship ties the work to dielectric and ceramic processing communities interested in aqueous organic chemistry at high temperature. Near-critical water–organic mixtures also appear in green chemistry solvent discussions; the paper’s structural diagnostics (RDFs, cluster lifetimes) support interpreting those environments at atomistic resolution.

## Methods

**ReaxFF-based molecular dynamics** (bulk **liquid** and **supercritical** regimes) samples **radial distribution functions**, **hydrogen-bonded clusters**, and **bonding** patterns for **acetic acid–water** mixtures with **\(1.0 \ge x_{\mathrm{HAc}} \ge 0.2\)** across **ambient** and **near-critical** states described in the abstract (`papers/Sengul_aceticacid_water_JCP_2018.pdf`). **Metadynamics** on the **acetic acid dissociation** coordinate supplies a **dissociation free energy** used to **reoptimize** the ReaxFF **dissociation energy** (abstract). **Engine / code:** **N/A — MD package name** not on the indexed excerpt (`normalized/extracts/2018mert-y-sengul-the-journal-reaxff-molecular_p1-2.txt`). **System & PBC:** periodic **supercells** of the mixture compositions in **Methods** (**atom** totals there). **Ensemble / thermostat / barostat / timestep:** **N/A — not transcribed** here; the article spans both **ambient** and **critical** conditions where **pressure** control matters—confirm **NPT** targets and **barostat** choices in **Methods**. **Duration / stages:** **equilibration** and **production** segments with lengths in **ps**/**ns** are tabulated in **Methods** (not duplicated on this excerpt-based page). **Temperature:** **ambient** vs **critical-region** **temperature** sweeps are central to the abstract’s structural claims. **Electric field:** **N/A — not used**. **Enhanced sampling:** **metadynamics** is used for the **dissociation** free-energy refinement noted above (not umbrella/replica exchange in the indexed abstract framing). **Duration / stages:** bulk mixture **equilibration** followed by **production** **MD** at each (**T**, **P**, composition) state point; cumulative trajectory lengths and the integration **timestep** (**fs**) are tabulated in *J. Chem. Phys.* §2 (`papers/Sengul_aceticacid_water_JCP_2018.pdf`)—**N/A — exact ns** not restated from the indexed excerpt alone.
## Findings

At ambient conditions, dominant aggregates shift between acetic-acid-rich and water-rich motifs as composition changes; cyclic dimers and chain-like hydrogen-bonded clusters appear in acid-rich regimes and diminish as water content rises. Under near-critical conditions, longer-range correlations weaken and acid–acid versus water–water ordering becomes more disordered compared with ambient RDF fingerprints, as summarized in the abstract and figures. These trends are interpreted as signatures of how supercritical-like environments disrupt molecular clustering relative to room-temperature hydrogen-bond networks. The metadynamics refinement of the acid dissociation free-energy profile is the methodological centerpiece: it ties the reactive force field’s proton-transfer energetics to a statistically sampled reaction coordinate rather than relying on a single-point gas-phase estimate.

## Limitations

Near-critical sampling is demanding; finite-size effects and simulation length can bias cluster statistics. ReaxFF proton-transfer barriers should be checked against experiment or higher-level electronic structure where quantitative rates matter. Metadynamics parameters influence the inferred dissociation free energy; sensitivity checks belong in the original article. Barostat choices near the critical point affect density fluctuations and cluster statistics.

## Relevance to group

Group-linked ReaxFF application to aqueous organic mixtures with metadynamics-informed parameter consistency.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1063/1.5025932](https://doi.org/10.1063/1.5025932)

## Related topics

- [[reaxff-family]]
