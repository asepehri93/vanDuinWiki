---
id: paper:2015raju-venue-research
type: paper
title: "Reactive force field study of Li/C systems for electrical energy storage"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - domain:carbon-hydrocarbon
  - method:reaxff
  - method:monte-carlo
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/ct501027v"
year: 2015
authors:
  - "Muralikrishna Raju"
  - "P. Ganesh"
  - "Paul R. C. Kent"
  - "Adri C. T. van Duin"
venue: "J. Chem. Theory Comput."
pdf_sha256: "e2e058a05b7d68a246043bb9faa73b9d5147a2dcf46cca40728639dccdb031f6"
pdf_path: "papers/Raju_LiC_2015_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015raju-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi` and `pdf_path`. This ingest is an ACS **proof** layout for the same JCTC article as [[2015raju-venue-ct-2014-01027v]] when that sibling exists.

## Summary

Graphitic carbon remains the dominant Li-ion anode, yet few simulations simultaneously capture Li energetics, staging, and kinetics in graphite and related nanostructures at sizes and concentrations relevant to experiment. Raju, Ganesh, Kent, and van Duin develop a **ReaxFF** parametrization for **Li–C** using **van der Waals–corrected DFT** as the QM reference, then apply it in **grand canonical Monte Carlo (GCMC)** studies of Li intercalation in **perfect graphite** at supercell sizes of order **~1000 atoms**. The reported GCMC voltage profile agrees with known experimental and DFT behavior, and the simulations reproduce **in-plane Li ordering** and **interlayer spacing** associated with **stage I and II** staging. **Defective graphite** with **~1–2%** point and topological vacancy content shifts **Li/C (capacity)** and **voltage** together with signatures of **metallic lithium**, connecting to recent **lithium plating** experiments. Additional model studies on **0D (onion-like)** and **1D (nanorod)** carbon highlight geometry-dependent pathways: a **defective onion-like** particle favors fast charge/discharge via **surface Li adsorption**, whereas a **defect-free nanorod** requires a **critical Li density** at edges before intercalation proceeds.

## Methods

The authors fit **Li–C** interactions within **ReaxFF** using **van der Waals–corrected DFT** as the quantum reference, then apply the field in **grand canonical Monte Carlo (GCMC)** studies of Li intercalation in **perfect graphite** with supercells of order **~1000 atoms** (abstract and Sec. II opening). **ReaxFF** evaluates bonded and nonbonded contributions (bond, valence, torsion, over/under-coordination, lone pair, vdW, Coulomb) with bond orders updated at each MD or minimization step, as summarized in Sec. II.A of the article. GCMC exchanges Li against a reservoir to sample lithiation thermodynamics and staging-related structure. **Defective graphite** models add **point and topological** vacancies at **1–2%** density to probe how **Li/C**, **voltage**, and **metallic Li** signatures shift relative to the perfect lattice. Additional calculations treat **0D** (onion-like) and **1D** (nanorod) carbons to compare **surface Li adsorption** with **edge-limited** intercalation pathways.

**Engine**, **timestep**, **thermostat/barostat** settings for any energy-relaxation or MD segments paired with GCMC, and full **MC sweep** statistics, are given in the **Computational Methods** and **SI** tables on `pdf_path` (and the journal-layout sibling [[2015raju-venue-ct-2014-01027v]])—they are **not** recoverable from the short indexed excerpt used for this page. **System size:** **~1000 atoms** graphite supercells in the GCMC abstract description, plus larger **0D/1D** carbon models as built in the article. **Boundaries:** bulk graphite and nanostructure cells use **3D periodic** supercells as defined there. **Ensemble:** **grand canonical** Li exchange for intercalation sampling; **barostat / hydrostatic pressure control:** **N/A** for the GCMC-centric lithiation workflow as summarized. **Temperature:** isothermal **temperature** setpoints for each reported voltage/staging curve are listed in **Methods** on `pdf_path` (not transcribed from the excerpt here). **Duration:** **production** GCMC sweep counts and any coupled MD **production** segment lengths (**ps**/**ns**) appear in those same tables. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A** (GCMC, not umbrella or replica exchange).

**Force-field training.** **Parent:** reactive **C** framework extended to **Li–C**. **QM reference:** **vdW-corrected DFT** on graphite-related and defective condensed-carbon configurations (introduction). **Training set:** equations of state and intercalation motifs spanning perfect and defective graphitic environments (full enumeration in the article). **Optimization:** ReaxFF refit to those targets using the group’s standard least-squares protocol (software and weights in `pdf_path`). **Validation:** GCMC **voltage** and **staging** observables compared with **experiment** and **DFT** references cited in the abstract.

**Static QM / DFT-only production:** **N/A** — periodic **DFT** supplies training and benchmark data; headline results are **ReaxFF + GCMC**, not standalone AIMD lithiation trajectories.

## Findings

**Perfect graphite:** GCMC with the new Li–C ReaxFF reproduces a **voltage profile** consistent with known **experimental and DFT** results and captures **in-plane ordering** plus **interlayer separations** characteristic of **stage I and II** compounds (abstract).

**Defective graphite:** As **vacancy** content increases toward the **1–2%** regime modeled, **Li/C ratio (capacity)** and **voltage** shift together with behavior linked to **metallic lithium**, interpreted in the article as a microscopic rationalization for **lithium plating** trends seen in recent experiments (abstract).

**Nanostructured carbons:** **0D onion-like** models favor **fast charge/discharge** dominated by **surface Li adsorption**, whereas a **1D defect-free nanorod** requires a **critical Li density** at **edges** before intercalation becomes favorable—illustrating how **geometry and defects** reroute lithiation kinetics within the same force field (abstract).

**Corpus honesty:** This file is a **proof PDF**; prefer the **journal-layout** ingest for pagination-sensitive citations when both exist (`[[2015raju-venue-ct-2014-01027v]]`).

## Limitations

Proof PDFs can show **watermarks**, **color shifts**, or **figure-resolution** differences from the version of record. **Electrolyte**, **SEI**, and **continuum transport** outside the ReaxFF+GCMC stack are outside the paper’s atomistic scope.

## Relevance to group

Flagship **Li-ion anode** reactive modeling led by Raju with van Duin and ORNL coauthors.

## Citations and evidence anchors

- DOI `10.1021/ct501027v`; `pdf_path`: `papers/Raju_LiC_2015_proof.pdf`.
- [[2015raju-venue-ct-2014-01027v]]

## Related topics

- [[reaxff-family]]
