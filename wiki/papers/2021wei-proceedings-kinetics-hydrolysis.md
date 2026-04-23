---
id: paper:2021wei-proceedings-kinetics-hydrolysis
type: paper
title: "Kinetics for the hydrolysis of Ti(OC3H7)4: A molecular dynamics simulation study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - domain:fuel-combustion
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reactive-md
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1016/j.proci.2020.06.345"
year: 2021
authors:
  - "Jili Wei"
  - "Alireza Ostadhossein"
  - "Shuiqing Li"
  - "Matthias Ihme"
venue: "Proceedings of the Combustion Institute"
pdf_sha256: "747b02b34d988c71475b9472ef738920a6d199f9e82670bec763afe68bbb195d"
pdf_path: "papers/ReaxFF_others/Wei_Ihme_TTIP_ProcCombInst_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2021wei-proceedings-kinetics-hydrolysis -->

## Summary

**Titanium tetraisopropoxide (TTIP)** hydrolysis in high-temperature gas-phase environments governs **TiO₂** nanoparticle formation in flame and combustion synthesis. The authors use **ReaxFF molecular dynamics** (with **LAMMPS** as in the article) to follow atomic-level **TTIP** conversion with **water**, fit a **second-order** hydrolysis rate constant, and trace **Ti-containing** intermediates and clustering before **TiO₂** **nucleation**. The introduction frames spray-flame and aerosol contexts where gas-phase organometallic chemistry controls particle size and phase; this work targets kinetics and mechanisms that are hard to resolve from burner-averaged experiments alone.

## Methods

**1 — MD application (atomistic dynamics).** The paper applies **ReaxFF** molecular dynamics to gas-phase hydrolysis of **TTIP** with **water**, and reports a second-order hydrolysis rate fit at 1 atm:
**k = 1.23×10¹⁴ exp(−11 323/T [K]) mol⁻¹ cm³ s⁻¹**. It also states that simulations span a range of temperatures and pressures to derive kinetics and pathways.

- **Engine / code:** **LAMMPS** with **ReaxFF**.
- **System size & composition:** TTIP + water gas-phase reactive system; atom counts are not reported in the local extract.
- **Boundaries / periodicity:** **N/A — not stated** in `normalized/extracts/2021wei-proceedings-kinetics-hydrolysis_p1-2.txt`.
- **Ensemble (NVE/NVT/NPT):** **N/A — not stated** in the local extract.
- **Timestep:** **N/A — not stated** in the local extract.
- **Duration / stages:** **N/A — not stated** in the local extract.
- **Thermostat:** **N/A — not stated** in the local extract.
- **Barostat:** **N/A — not stated** in the local extract.
- **Temperature:** simulations reported over a temperature range; specific values are in the version-of-record PDF.
- **Pressure:** 1 atm for the reported Arrhenius fit; additional pressures are mentioned but not enumerated in the local extract.
- **Electric field:** **N/A — not used/reported** in the local extract.
- **Replica / enhanced sampling:** **N/A — not reported** in the local extract.

**2 — Force-field training.** **N/A** for a new parameterization reported as the main result of this paper — the work **uses** an established **Ti–O–C–H** **ReaxFF** (training lineage and citations in the article and references).

**3 — Static QM / DFT.** **N/A** as the primary method — the paper is ReaxFF MD–centric; any supporting QM references serve force-field context, not standalone DFT results summarized here.

**4 — Experiments.** **N/A** — simulation and literature positioning; no new laboratory campaign in this paper.

## Findings

**Outcomes and mechanisms.** The abstract reports **k = 1.23×10¹⁴ exp(−11 323/T [K]) mol⁻¹ cm³ s⁻¹** for hydrolysis in the authors’ second-order framework at **1 atm**. **Clusters** form **before** distinct **TiO₂** molecules appear. **Ti**-containing species fall into two families: those with **one or two C–O** bonds versus **carbon-free** species with more than two **Ti–O** bonds, which follow **separate** routes: **oligomerization** via **Ti–O–Ti** bridges (early nanoparticle precursors) or further **decomposition** to smaller units (e.g. **TiO₂**-like fragments) that then join later **growth**. **Ti–O** interactions in clusters are described as stabilizing larger structures by **abstracting water** and **–CₓHᵧ** groups (abstract).

**Comparisons and levers.** The introduction contrasts prior global and one-step TTIP models with the present species-resolved trajectories; **N/A** here for a full tabulation of **T**/**P** sweeps — see the article. **Corpus honesty:** numbers and pathway labels above follow the **abstract** and p1–2 extract; confirm final values and figures in the **PDF**.

## Limitations

**ReaxFF** accuracy for **organometallic** **Ti–O–C** chemistry at **flame** temperatures should be benchmarked against **QM** where available. **Simulation** **sizes** and **times** may not capture full **particle** **coagulation** physics.

The **second-order** rate expression summarized from the abstract is a compact handle for **kinetic** modelers coupling **gas-phase** **TTIP** chemistry to **particle** **nucleation** modules; any **multistep** interpretation should cite the **full** **mechanistic** tables in the **Proceedings** article.

## Relevance to group

Connects **PSU**-affiliated **Ostadhossein** **ReaxFF** work to **combustion** **synthesis** contexts—useful alongside **oxide** **nucleation** and **spray** **flame** papers.

**TTIP** chemistry is also a common **teaching** example for **organometallic** **hydrolysis** in **aerosol** routes to **TiO₂**; this article’s pathway taxonomy helps disambiguate questions about **oligomer** formation versus **molecular** **TiO₂**-like fragments in **gas-phase** simulations.

## Citations and evidence anchors

- DOI [10.1016/j.proci.2020.06.345](https://doi.org/10.1016/j.proci.2020.06.345).
- Excerpt alignment: `normalized/extracts/2021wei-proceedings-kinetics-hydrolysis_p1-2.txt`.

## MAS / retrieval

`paper_keywords` includes **`keyword:combustion`** and **`keyword:thermal-decomposition`** so **flame-synthesis** queries can surface this **TTIP** **hydrolysis** reference even though the chemistry is not **hydrocarbon** **oxidation** in the usual sense.

## Related topics

- [[reaxff-family]]
