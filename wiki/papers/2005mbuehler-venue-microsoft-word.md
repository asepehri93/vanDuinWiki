---
id: paper:2005mbuehler-venue-microsoft-word
type: paper
title: "Formation of water at a Pt(111) surface: A study using reactive force fields (ReaxFF)"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:catalysis-surface
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
  - keyword:qm-training-data
  - keyword:water-interfaces
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - material:metal-surface
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2005
authors:
  - "Markus J. Buehler"
  - "Adri C. T. van Duin"
  - "Timo Jacob"
  - "Yunhee Jang"
  - "Boris Berinov"
  - "William A. Goddard III"
venue: "MRS Proceedings (submitted, Fall 2005)"
pdf_sha256: "79b8675a6e7b1c8eafa48b14f0d9bb209bebb169fbbefebd4724b447e62b18c6"
pdf_path: "papers/Buehler_Pt_H2O_MRS_Proceedings_2005.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2005mbuehler-venue-microsoft-word -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `title`, and `pdf_path` in the front matter above (no DOI in the normalized record). They are **not** new primary claims by this wiki.

    For **definitive** numerical values, barriers, and mechanisms, use the **PDF** and optional records under `normalized/papers/`—not this page alone.

## Summary

This MRS Proceedings submission reports finite-temperature atomistic molecular dynamics of water formation from O\(_2\) and H\(_2\) at a Pt(111) surface using a reactive ReaxFF model trained on quantum-mechanical data for the O/H–Pt system. The work contrasts gas-phase stoichiometric H\(_2\)/O\(_2\) mixtures with catalyzed chemistry at Pt, extracts rate information from repeated trajectories, and compares an estimated activation energy for water formation with a barrier from restraint-driven MD at the surface. Simulations used a preliminary parameterization of the O/H–Pt force field still under development.

## Methods


### ReaxFF model / training context (checklist A)

- **System chemistry:** **O/H** interaction with **Pt(111)** using a **ReaxFF** parameterization trained against **QM** data for **O/Pt** and **H/Pt** **dissociation**, **chemisorption**, and related **reaction** energetics (authors flag the fit as **preliminary**; **QM** citations include **Jacob**/**Goddard**-family work as referenced in the PDF).
- **Surface setup:** periodic **Pt(111)** slab with **gas-phase** **H\(_2\)**/**O\(_2\)** mixtures at controlled **partial pressures** (**Fig. 1** workflow in the proceedings article).

### Molecular dynamics (checklist B)

- **Engine / integrator:** **NVT** **MD** with **ReaxFF**; **velocity Verlet**; **timestep** **\(\Delta t = 0.25\)** **fs**; **Berendsen** thermostat (values/damping as stated in the PDF).
- **Stages:** **energy minimization**; short **nonreactive** **FF** segment to avoid spurious early **chemistry**; switch to **ReaxFF** for **production** dynamics.
- **Sampling:** **10** independent trajectories per reported **(T, P)** point with different initial conditions; **nanosecond**-scale accessible in the reported runs (MRS Proceedings PDF).
- **Kinetics analysis:** **water** formation **rates** vs **temperature** via **Arrhenius** plot; separate **restraint**/**constrained** **MD** along a reaction path used to estimate a **barrier** for comparison to the **Arrhenius** **\(E_a\)**.

### Not stated in the short corpus extract

Full **supercell** dimensions, **thermostat** coupling constants, and **k-space**/**electrostatic** settings for the **slab**—confirm in **`papers/Buehler_Pt_H2O_MRS_Proceedings_2005.pdf`**.

**MD protocol (integrated):** **molecular dynamics** uses **ReaxFF** for **O/H** on **Pt(111)** with **velocity Verlet** integration. **N/A — MD package name** in the short excerpt—verify the proceedings PDF. **System:** periodic **Pt(111)** **slab** with **gas-phase** **H\(_2\)**/**O\(_2\)** (partial pressures as in **Fig. 1** workflow). **Boundaries / periodicity:** **periodic** **slab** geometry as stated; **N/A — full lateral supercell vectors** in this wiki summary. **Ensemble:** **NVT**. **Timestep:** **\(\Delta t = 0.25\)** **fs** as stated above. **Duration / stages:** **energy minimization**; short **nonreactive** segment; **production** **ReaxFF** dynamics; **10** independent trajectories per **(T, P)** point; **nanosecond**-scale access stated in the wiki summary—confirm exact **ps**/**ns** splits in the PDF. **Thermostat:** **Berendsen**; **N/A — coupling time constant** in the indexed text. **Barostat:** **N/A — NPT** not stated (**NVT**). **Temperature:** sampled across an **Arrhenius** ladder as in the proceedings manuscript—**N/A — single canonical T** line not reproduced here without reopening **`pdf_path`**. **Pressure / stress:** **partial pressures** of reactants are part of the setup; **N/A — MD stress tensor** control details in the excerpt. **Electric field:** **N/A** for MD beyond chemistry on the surface. **Replica / enhanced sampling:** **N/A**.

## Findings

- **Reactivity contrast:** **uncatalyzed** stoichiometric **H\(_2\)/O\(_2\)** mixtures can react **violently** (**“explosive”** in the authors’ wording) in the simulation cell, whereas **Pt(111)** enables **controlled**, **faster** **water** formation consistent with **catalytic** acceleration (discussion in the proceedings manuscript).
- **Kinetics:** **Arrhenius** analysis of trajectory-derived rates gives an activation energy for **water** formation of **~12 kcal/mol**, described as **consistent** with a **barrier** from **restraint**/**constrained** **surface** **MD** in the same **preliminary** **ReaxFF** framework.
- **Limitations (authors):** **O/H–Pt** **ReaxFF** is explicitly **preliminary**; quantitative barriers/rates should be treated as **illustrative** pending later **refitted** potentials.

## Limitations

- The extract and abstract emphasize a **preliminary** ReaxFF for O/H–Pt; quantitative agreement should be interpreted in that context.
- Provenance is a proceedings submission PDF; there is no DOI in the normalized bibliography—locators should be taken from the PDF if needed.

## Relevance to group

Co-authorship by **Adri C. T. van Duin** links this early ReaxFF application directly to the group’s reactive force-field lineage; it illustrates large-scale reactive MD for surface catalysis (Pt/water) adjacent to QM training data.

## Citations and evidence anchors

- Local PDF: `papers/Buehler_Pt_H2O_MRS_Proceedings_2005.pdf` (manifest hash in front matter).
- Normalized extract: `normalized/extracts/2005mbuehler-venue-microsoft-word_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[theme-catalysis-surfaces]]
