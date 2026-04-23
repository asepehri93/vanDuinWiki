---
id: paper:2012weismiller-proceedings-using-molecular
type: paper
title: "Using molecular dynamics simulations with a ReaxFF reactive force field to develop a kinetic mechanism for ammonia borane oxidation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:reactive-md
  - keyword:dft-static
  - keyword:nvt-simulation
source_refs: []
doi: "10.1016/j.proci.2012.06.030"
year: 2012
authors:
  - "Weismiller, M. R."
  - "Russo, M. F., Jr."
  - "van Duin, A. C. T."
  - "Yetter, R. A."
venue: "Proceedings of the Combustion Institute"
pdf_sha256: "2e0c82204bb96c5fe9b615c62ae0ce1b81cb2fd5afc2a37b8ea7dc1cf5087390"
pdf_path: "papers/Weismiller_AB_oxidation_ProcCombInst_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2012weismiller-proceedings-using-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

**Ammonia borane (NH₃BH₃)** combines high **hydrogen** content with propellant-relevant chemistry; this work uses **ReaxFF MD** of **AB** oxidation to build an **elementary kinetic mechanism** for **continuum** models **without** prior **experimental** rate data for every step. The abstract’s pathway picture is **sequential** **H₂** loss from gas-phase **AB**, reaction of **H₂** with **O₂**, **oxygen** attack on **boron**-bearing fragments, **B–N** cleavage, and equilibrium products including **H₂O**, **HOBO**, and **N₂**. **DFT** supplies missing **thermochemistry**, **collision theory** gives first **rate** estimates, and **CHEMKIN** closed-reactor **constant-pressure, constant-energy** runs are reported **consistent** with the atomistic trajectories.

## Methods


**ReaxFF** for **NH₃BH₃** oxidation uses the prior parameterization (ref. [11] in the article). The introduction contrasts **nonreactive** **FFs** (e.g., **MM3**, general **DREIDING**-class models) that cannot break bonds with **ReaxFF**’s **bond-order** updates each timestep as **interatomic** distances evolve—enabling **large** **reacting** cells that remain intractable for **fully** **quantum** **dynamics**. Reactive **MD** identifies elementary sequences: two **H₂** eliminations from **AB**, **O₂** attack on boron-bearing fragments, **B–N** cleavage, and **H₂O** / **HOBO** / **N₂** products. **DFT** supplies missing thermochemical data; **collision theory** gives first rate estimates; **Jaguar B3LYP/6-311G** locates the transition state for the second **H₂** loss from **H₂NBH₂** (Eq. 9). A reduced mechanism is implemented in **CHEMKIN** for a closed reactor at fixed pressure/energy. Illustrative **NVT** heating ramps use **20 AB + 45 O₂** in a **2.5 nm** periodic cube at **0.00522 K/fs** (Figure 3).

### MD application (ReaxFF oxidation trajectories + illustrative ramps)

**Engine / code:** **ReaxFF** **molecular dynamics**; **N/A —** specific **MD** engine string not recovered from `normalized/extracts/2012weismiller-proceedings-using-molecular_p1-2.txt`—verify **`pdf_path`**.

**System size & composition:** Illustrative **gas-phase** cells such as **20** **NH\(_3\)BH\(_3\)** + **45** **O\(_2\)** in a **2.5 nm** periodic cube (**Figure 3** protocol on this page); larger reacting cells are discussed qualitatively in the introduction.

**Boundaries / periodicity:** **Three-dimensional periodic** cube for the **Figure 3** ramp example.

**Ensemble:** **NVT** for the documented heating-ramp illustration; broader **MD** stages in the mechanism survey follow **`pdf_path`**.

**Timestep:** **N/A —** **Δt** not recovered from the indexed excerpt; verify **`pdf_path`**.

**Duration / stages:** **Multi-stage** temperature ramps at **0.00522 K/fs** for the **Figure 3** illustration; overall **MD** segment lengths for the full mechanism survey are in **`pdf_path`**.

**Thermostat:** **N/A —** thermostat details for all **MD** segments are not excerpted on pages **1–2**; verify **`pdf_path`**.

**Barostat / pressure control:** **N/A —** **NPT** not stated for the quoted **NVT** ramp demo.

**Temperature:** **NVT** heating ramp control as in **Figure 3**; absolute temperature ranges for all production segments are tabulated in the article.

**Pressure / stress:** **CHEMKIN** closed-reactor demos use **constant pressure**/**energy** controls as stated in the abstract; **N/A —** this is continuum-level rather than atomistic **stress** control.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not used.

### Force-field training (prior ReaxFF for NH\(_3\)BH\(_3\) oxidation)

**Parent FF / elements:** Uses the existing **NH\(_3\)BH\(_3\)** oxidation **ReaxFF** parametrization cited as ref. **[11]** in the article.

**QM reference:** **DFT** (**Jaguar B3LYP/6-311G**) for selected thermochemistry and a **TS** search for the second **H\(_2\)** loss from **H\(_2\)NBH\(_2\)** (Eq. 9).

**Training set / reference data:** **N/A —** full training-set listing is not excerpted here; it lives in the prior parametrization reference.

**Optimization:** **N/A —** new **ReaxFF** optimization is not reported in this proceedings article.

**Reference data used:** **DFT** thermochemistry, **collision-theory** rate estimates, **ReaxFF** trajectories, and **CHEMKIN** reactor consistency checks as described in the abstract.

## Findings

**Outcomes / mechanisms:** **ReaxFF** trajectories support a sequential picture: two **H\(_2\)** eliminations from **AB**, **O\(_2\)** attack on **B**-bearing fragments, **B–N** cleavage, and equilibrium products including **H\(_2\)O**, **HOBO**, and **N\(_2\)**.

**Comparisons:** **CHEMKIN** closed-reactor **constant-pressure, constant-energy** runs are reported **consistent** with the atomistic **MD** observations; **DFT** supplies missing thermochemistry relative to experimentally sparse elementary rates.

**Sensitivity / design levers:** **Temperature** ramps (**K/fs** protocol in **Figure 3**) modulate which intermediates dominate along the oxidation sequence.

**Limitations / outlook:** **ReaxFF** combustion chemistry accuracy and the scope of the **reduced** **CHEMKIN** mechanism remain limitations acknowledged implicitly by the multi-method workflow.

**Corpus / KB honesty:** Grounded in **`pdf_path`** and `normalized/extracts/2012weismiller-proceedings-using-molecular_p1-2.txt` (front-matter heavy); **Proc. Combust. Inst.** **34** pages hold complete tables.

The introduction additionally contrasts **AB** with **pyrophoric** **boranes** as a **solid**, **easily stored** hydrogen carrier for propulsion studies, motivating the combined **DFT + MD + CHEMKIN** workflow when elementary **experimental** rates are sparse.

## Limitations

**ReaxFF** **combustion** chemistry accuracy; **reduced** **mechanism** scope; **Proceedings** **page** year **2013** vs **submission** **2012**.

## Relevance to group

**Adri C. T. van Duin** coauthored; **ReaxFF**/**combustion** **kinetics** for **boron**-**nitrogen** **fuels**.

## Citations and evidence anchors

- DOI **10.1016/j.proci.2012.06.030** — *Proc. Combust. Inst.* **34**, 3489–3497 (2013).
- Extract: `normalized/extracts/2012weismiller-proceedings-using-molecular_p1-2.txt`.

## Related topics

- [[reaxff-family]]
