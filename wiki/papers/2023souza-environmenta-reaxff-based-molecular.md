---
id: paper:2023souza-environmenta-reaxff-based-molecular
type: paper
title: "A ReaxFF-based molecular dynamics study of the destruction of PFAS due to ultrasound"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:reactive-md
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:thermal-decomposition
  - keyword:water-interfaces
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1016/j.envpol.2023.122026"
year: 2023
authors:
  - "Bruno Bezerra de Souza"
  - "Shaini Aluthgun Hewage"
  - "Jitendra A. Kewalramani"
  - "Adri C. T. van Duin"
  - "Jay N. Meegoda"
venue: "Environ. Pollut."
pdf_sha256: "9c68e7001f840656f0a1704dcf1a007b4668d3492d0e475660e1a56268ac73b5"
pdf_path: "papers/deSouza_PFAS_ultrasound_EnvPoll_2023.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023souza-environmenta-reaxff-based-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the *Environmental Pollution* article identified by `doi`, `title`, and `pdf_path`.

## Summary

Per- and polyfluoroalkyl substances (**PFAS**) persist in the environment; **ultrasound** with **cavitation** is investigated experimentally as a degradation route, but atomistic insight into **bond scission** under extreme local conditions is scarce. This work uses **ReaxFF molecular dynamics** in **LAMMPS** to mimic **cavitational** chemistry by **high-temperature** reactive trajectories for **perfluorinated** species (including **PFOA-class** chemistry in the paper) in several gas-phase environments—**water vapor**, **O\(_2\)**, **N\(_2\)**, and **air**—spanning **373–5000 K**. The goal is to map **destruction mechanisms**, **fragment populations**, and the extent of **defluorination** / **mineralization** over nanosecond windows at the highest temperatures explored.

The modeling strategy is **explicitly** a **thermolytic** **proxy**: the authors elevate **temperature** to access **reactive** **timescales** compatible with ReaxFF MD rather than simulating **acoustic** **fields** and **bubble** **collapse** **explicitly**.

## Methods

**Design (proxy for sonochemistry).** The work does **not** resolve **acoustic** **fields** or **nano**–**bubble** **collapse**; it uses **NVT** **ReaxFF** in **LAMMPS** to approximate **cavitational** “**hot**-**spot**” **chemistry** with **extreme** **T** in **defined** **gas** **mixtures**, as described in *Environmental Pollution* and **Table S1** (SI).

### 1 — MD application (ReaxFF, LAMMPS, NVT)

- **Engine / code:** **ReaxFF** through **LAMMPS**; **PFOA**- and **PFOS**-centered **boxes** in the *Methods* use **10** **molecules** of each **+** **1000** **H\(_2\)O** in a **~383.6 Å** **cubic** **cell** **at** **water**-**vapor** **density** matched to **100 °C** **saturated** **vapor** (see *Env. Pollut.* and **Table S1** for all **O\(_2\)**/**N\(_2\)**/**“air”** **variants**).
- **Boundaries / PBC:** **Cubic** **PBC**; **N/A** — **not** a **condensed** **water** **phase** at **ambient** **P** for the **5000** **K** “**implosion**”-**analog** **runs**.
- **Ensemble, timing:** **Minimization** → **NVT** **equilibration** **20** **ps** (article reports **T** and **1** **atm** for the **stated** **preequilibration** case) → **NVT** **8** **ns** “**production**” with **T** in **~373.15**–**5000** **K** (full matrix in **Table S1**). The authors state **8** **ns** is chosen in part so **5,000** **K** **PFOA/PFOS** runs **fully** **degrade** within a **comparable** **window** across **cases**.
- **Timestep / integrator, thermostat:** **N/A** in the **1–2**-**page** **extract**—confirm **time** **step** and **thermostat** **damping** from the full **elsevier** **PDF/**SI**; **N/A** — the wiki does not invent a **0.25** **fs** **default** for this work.
- **Barostat, pressure, electric field, enhanced sampling:** **NVT**-**centric**; **1** **atm** appears in the equilibration sentence; **N/A** — **NPT** **or** **external** **E-** field not used; **N/A** — no **metadynamics** or **rare-****event** **reweighting** beyond **high-**T **MD**.

**Corpus honesty:** **Extreme**-**science** **computing** **context** in the article—**gas**-**phase**, **high**-**T** trajectories are a **proxy** for **sonochemical** **hot** spots, not a resolved **fluid** **dynamics** model of **MHz** **ultrasound** or **bubble** **collapse**.

**System size (slot coverage).** The *Env. Pol.* **paper** **lists** **10** **PFOA** (or **PFOS**) **+** **1000** **H₂O** in the **cubic** **vapor** **cell** **(thousands** of **atoms** per **box**; see **Table S1** for **larger** **O₂**/**N₂**/**air** **cases**).

## Findings

The authors report **greater than 98%** modeled **PFAS degradation** within **8 ns** at **5000 K** in **water vapor**, described as consistent with **micro/nanobubble implosion** chemistry in their framing. **C\(_1\)** and **C\(_2\)** **fluoro-radical** products dominate among small fragments over the simulated period and are argued to **limit complete mineralization efficiency** relative to full conversion to benign products. Trajectory chemistry is linked to **mineralization** narratives in the abstract with reference to experimental sonochemical observations.

**Environmental caveat.** High-**T** **gas-phase** trajectories do not resolve **aqueous** **solvation** at **ambient** conditions; extrapolation to **real** **sonochemical** **reactors** should treat these results as **mechanistic** hints rather than quantitative **rate** predictions.

**Byproduct chemistry.** Dominance of **small** **fluorinated** **radicals** in the **high-T** **limit** informs **toxicity** and **complete** **mineralization** discussions: even when parent **PFAS** **molecules** **fragment**, **short** **fluorinated** **species** may persist and require **secondary** **treatment** pathways not captured here.

**Group link.** **van Duin** coauthorship connects the study to broader **reactive** **MD** expertise on **halogenated** **organics** and **combustion**-adjacent chemistry, useful when cross-walking to **ReaxFF** **parameter** **lineages** validated for **C–F** **bonds**.

## Limitations

Extreme temperatures are a **proxy** for cavitation hotspots; the model omits explicit **ultrasound** propagation, **bubble** dynamics, and **solvation** at ambient conditions. ReaxFF kinetics are approximate for fluorocarbon chemistry.

## Relevance to group

**Adri C. T. van Duin** co-authors; demonstrates **ReaxFF** for **environmental** **PFAS** degradation pathways.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1016/j.envpol.2023.122026](https://doi.org/10.1016/j.envpol.2023.122026) (`papers/deSouza_PFAS_ultrasound_EnvPoll_2023.pdf`).

## Reproducibility and corpus locators

This note documents **where** to find primary evidence in-repo; it does **not** add new scientific claims beyond the cited publication.

**Normalized layer.** When present, `normalized/papers/{slug}.json` mirrors manifest hashes, bibliography fields, and extraction pointers; if `pdf_path` or PDF bytes change, follow `AGENTS.md` and `docs/PHASE3_RUNBOOK.md` to re-profile rather than editing PDFs in place.

**Authority chain.** For numerical settings (cutoffs, timesteps, ensembles, kinetics), use the peer-reviewed PDF (and publisher Supporting Information) as the authoritative source; this wiki summarizes for navigation and retrieval.

## Related topics

- [[reaxff-family]]
