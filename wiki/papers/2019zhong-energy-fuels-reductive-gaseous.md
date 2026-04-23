---
id: paper:2019zhong-energy-fuels-reductive-gaseous
type: paper
title: "Reductive Gaseous (H2/NH3) Desulfurization and Gasification of High-Sulfur Petroleum Coke via Reactive Force Field Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:nvt-simulation
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1021/acs.energyfuels.9b01425"
year: 2019
authors:
  - "Zhong, Qifan"
  - "Zhang, Yu"
  - "Shabnam, Sharmin"
  - "Xiao, Jin"
  - "van Duin, Adri C. T."
  - "Mathews, Jonathan P."
venue: "Energy Fuels"
pdf_sha256: "c359b1b7236975c13fc0edb57f8b0e0357300f1edff93bae6e87c4c8f2be39bc"
pdf_path: "papers/Zhong_EnergyFuels_Coke_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2019zhong-energy-fuels-reductive-gaseous -->

!!! abstract "Scope"

ReaxFF molecular dynamics of high-sulfur petroleum coke under hydrodesulfurizing hydrogen versus ammonia-rich environments at high temperature, tracking sulfur and nitrogen speciation and gasification products.

## Summary

High-sulfur petroleum coke is a challenging feedstock for carbon products; reductive gas-phase treatments such as hydrodesulfurization and ammonia-based routes are candidate desulfurization pathways. The paper compares atomistic transitions of a petcoke model under reactive force field molecular dynamics in hydrogen-rich versus ammonia-rich conditions, focusing on sulfur and nitrogen removal sequences, byproduct gases, and differences in residual heteroatom content tied to ammonia incorporation into the carbonaceous matrix.

Opening context emphasizes that high-sulfur coke complicates manufacture of carbon materials and that comparing **H\(_2\)**- versus **NH\(_3\)**-rich environments requires tracking not only sulfur volatilization but also nitrogen retention pathways when ammonia-derived fragments incorporate into the solid carbon scaffold during high-temperature reactive MD.


Readers should verify numerical values, units, and section references against the peer-reviewed PDF and any Supporting Information, especially when extracts or galley PDFs truncate tables.

## Methods

**Engine, system, and boundaries (ReaxFF petcoke + reductant gas, LAMMPS).** The abstract and introduction describe **NVT** high-temperature trajectories of a high-sulfur “Qingdao” petcoke model (**2550 atoms** in the manuscript’s construction, drawn from prior work on the same structural model) in contact with a large gaseous bath on the order of **~5000** molecules, under **3D** periodic boundary conditions, with **S/N removal and gasification** contrasted for **H\(_2\)-rich (HDS-like)** and **NH\(_3\)-rich** feeds. The reported production segment is **3000 K** for **250 ps** at **constant volume**; the work cites prior ReaxFF petcoke studies for comparable **NVT** high-\(T\) practice.

**Time step, thermostat damping, and exact gas stoichiometry per case:** not reproduced in the short p1-2 extract; **N/A** for those scalars on this page—use *Energy Fuels* Methods and the SI. **Barostat (NPT):** **N/A** for the high-\(T\) NVT leg described. **Strain, shock, applied electric field:** **N/A**. **Rare-event or enhanced-sampling add-ons (metadynamics, hyperdynamics, etc.):** **N/A** in the one-window 3000 K / 250 ps description unless the full text adds another stage.

**Force-field line (parameterization, not a new training paper).** The study applies an existing ReaxFF C/H/O/S/N framework in the line of work cited in the paper; a full re-fit workflow is not the main claim. **N/A** — for new genetic/CMA-ES reoptimization tables on this page.

**DFT or continuum reactor modeling.** **N/A** — the contribution is ReaxFF MD of the coke and gas.

## Findings

Under the simulated hydrodesulfurization conditions, sulfur and nitrogen transformations proceed through the sequences summarized in the abstract (including formation of H₂S and HCN among stable gas-phase products). Ammonia desulfurization shows broadly similar sulfur/nitrogen evolution to hydrodesulfurization when hydrogen supplied by NH₃ decomposition is abundant, but direct bonding of nitrogen-containing fragments to carbon increases coke-bound nitrogen and can raise solid yield relative to hydrogen-only treatment. The authors emphasize final stable **gas**-phase **species** such as **HCN** and **H₂S** and discuss **implications** when **N** **reintegrates** into the **carbon** **residue**. **Sensitivity** is to **H₂**-rich vs **NH₃**-**rich** **gaseous** **feeds** at a **single** high **T** in the **stated** **reactive** **MD**; **reactor**-scale **kinetics** and **pore** **transport** are **outside** the **trajectory** **span**. **Corpus honesty:** confirm **all** **numbers** in the *Energy Fuels* **PDF**; this note does **not** add **independent** **kinetics** beyond the **source**.

## Limitations

High-temperature, short-duration reactive MD captures reactivity trends but not reactor-scale mass transport, pressure effects, or long-time coking chemistry; ReaxFF parameter scope should be checked for the specific heteroatom chemistries probed.

## Relevance to group

Van Duin-group ReaxFF application to fossil carbonaceous feeds and heteroatom removal, adjacent to other petcoke gasification studies in the corpus.

## Citations and evidence anchors

- https://doi.org/10.1021/acs.energyfuels.9b01425

## Related topics

- [[reaxff-family]]
