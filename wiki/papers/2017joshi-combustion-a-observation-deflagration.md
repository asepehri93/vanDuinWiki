---
id: paper:2017joshi-combustion-a-observation-deflagration
type: paper
title: "Observation of deflagration wave in energetic materials using reactive molecular dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reactive-md
  - domain:organics-polymers-pyrolysis
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:energetic-materials
  - keyword:combustion
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nve-simulation
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1016/j.combustflame.2017.05.009"
year: 2017
authors:
  - "Kaushik Joshi"
  - "Santanu Chaudhuri"
venue: "Combustion and Flame"
pdf_sha256: "43bd8bc488004038854e085cf2c8edd1cd09a41b8f5276cf5ac7ef7fbb43d614"
pdf_path: "papers/ReaxFF_others/Joshi_RDX_deflagration_CombFlame_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017joshi-combustion-a-observation-deflagration -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction pathways, and flux analyses, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Continuum models of condensed-phase energetic materials often rely on simplified chemistry at combustion fronts, while atomistic detail of a moving deflagration wave remains difficult to treat uniformly across systems. This work uses **ReaxFF-based reactive molecular dynamics** in LAMMPS to study thermally initiated **deflagration in crystalline RDX**, mapping trajectories onto **Eulerian control volumes** to obtain mass, energy, and chemical fluxes across the front. The authors describe a transition from ignition to a **self-sustaining deflagration** when mass transport at the front overtakes thermal transport during propagation, accompanied by a sharp temperature rise and increased density of unreacted solid ahead of the front. Reported energy flux across the propagating front is said to agree with prior heat-of-explosion estimates. Chemical analysis in the paper emphasizes **inter- and intramolecular hydrogen transfer**, formation of short-lived heavier **polyradicals** (analogous to nonvolatile residue discussed elsewhere), and a front composition described as molten RDX with radicals and **intact triazine** motifs.

## Methods

**A — Force-field training / fitting:** **ReaxFF** for **RDX** chemistry using the **Wood et al.** parametrization cited in the article—**no** new fitting in this **Combustion and Flame** contribution.

**B — Molecular dynamics / sampling:** **LAMMPS** **ReaxFF** on **γ-RDX** **supercell** (**PBC**). **Hot spot** (**~144** molecules) gets **short** **high-T** pulse under **NVT** while **bulk** remains **NVE**; then **full-cell NVE** (**0.1 fs**) to mimic **adiabatic** response. **Post-process:** **Eulerian** **control volumes** for **mass**, **energy**, **species** **fluxes** across **deflagration** front.

**C — DFT / static QM:** **Not** the engine for deflagration trajectories summarized here.

**D — Review / non-simulation framing:** **Application** paper mapping **atomistic** fronts to **continuum**-style **flux** language—**not** a methods review.

**Engine:** **LAMMPS** **ReaxFF** on **γ-RDX** **supercell** with **PBC**. **System:** **crystalline RDX** supercell with a **hot-spot** subset (**~144** molecules) receiving a **short** **high-T** pulse under **NVT** while the remainder is **NVE**, followed by **full-cell NVE** propagation (**Combustion and Flame** **Methods**). **Timestep:** **0.1 fs** for the **NVE** propagation quoted on this page. **Thermostat:** **NVT** segment on the **hot spot** only (thermostat family/damping in **PDF**). **Duration / staging:** total **simulation time** after initiation and **equilibration** splits are **not** transcribed here—use **`pdf_path`**. **Barostat / pressure:** **N/A —** **NVE**/**NVT** **deflagration** protocol without **NPT** control in the summary. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

## Findings

The mapped fluxes support a picture in which a self-sustaining deflagration arises once mass transport at the front exceeds thermal transport, with the temperature spike and densification of cold material ahead of the front called out as signatures. Energy flux through the front is consistent with earlier heat-of-explosion-scale expectations in their analysis. The chemistry at the front is dominated by H-transfer chemistry and polyradical buildup, with triazine rings persisting within the described reactive mixture.

**Comparisons.** **Energy flux** at the front is compared to **literature** **heat-of-explosion**-scale estimates as cited in the article.

**Corpus / PDF honesty.** **Flux** thresholds and full **species** tables should be taken from **`pdf_path`** / extract pointers, not from this summary alone.

## Limitations

- A single initiation protocol and finite supercell restrict generality to other microstructures, defects, or initiation modes.
- ReaxFF chemistry is approximate under the extreme temperatures and densities of a deflagration front; interpretation relies on the chosen parameter set.
- Connection to continuum propellant models remains via conceptual comparison rather than direct coupling.

## Relevance to group

Illustrates **ReaxFF + LAMMPS** applied to **condensed-phase energetic materials** and **reaction-front diagnostics**—useful alongside other reactive-MD combustion and decomposition work in the knowledge base.

## Citations and evidence anchors

- DOI: [10.1016/j.combustflame.2017.05.009](https://doi.org/10.1016/j.combustflame.2017.05.009)
- Text-aligned pointers: `normalized/extracts/2017joshi-combustion-a-observation-deflagration_p1-2.txt`

## Reader notes (navigation)

- **Theme hub:** [[theme-pyrolysis-combustion-organics]]
- **Force-field overview:** [[reaxff-family]]
- **Corpus index:** [[paper-index-by-domain]], [[paper-index-by-year]] (tags `domain:fuel-combustion`, `method:reaxff`).

## Related topics

- [[reaxff-family]]
- RDX and condensed-phase deflagration (reactive MD literature cross-links via theme hub above)
