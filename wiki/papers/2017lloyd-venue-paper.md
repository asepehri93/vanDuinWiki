---
id: paper:2017lloyd-venue-paper
type: paper
title: "Reaction pathways in atomistic models of thin film growth"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:oxides-ceramics
  - domain:alloys-metallurgy
  - method:monte-carlo
  - method:reaxff
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:method-development
  - keyword:lammps
  - keyword:metallic-systems
  - keyword:oxide-surface
  - keyword:reaxff-application
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1063/1.4986402"
year: 2017
authors:
  - "Adam L. Lloyd"
  - "Ying Zhou"
  - "Miao Yu"
  - "Chris Scott"
  - "Roger Smith"
  - "Steven D. Kenny"
venue: "J. Chem. Phys."
pdf_sha256: "aae3a81ec88c88d75dd26a368487a54c5e92794f928acbf10e7bf6765a961d0a"
pdf_path: "papers/ReaxFF_others/Lloyd_AKMC_Ag_ZnO_JCP_2017.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2017lloyd-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For barriers, rates, and case-study parameters, rely on the **JCP article** and any full text under `papers/`—local extraction is **partial** (first pages only).

## Summary

Thin-film growth involves diffusive and concerted atomic moves on or near a substrate; at experimental deposition rates, brute-force molecular dynamics cannot reach the relevant timescales because of the Arrhenius separation between MD timesteps (\(\sim 10^{-15}\) s) and growth events. This perspective introduces **adaptive kinetic Monte Carlo (AKMC)**: from each local minimum, transition rates to neighboring states are estimated, events (including deposition) are sampled probabilistically, and the clock advances by \(\Delta t = -\ln u / \sum_i R_i\). Adaptations for frequent low-barrier moves are discussed. Worked examples include Ag on Ag(100) and ZnO growth using a **ReaxFF** parametrization for ZnO with **LAMMPS**-based energy evaluations, illustrating how AKMC catalogs complex, non-intuitive pathways (exchange, concerted hops, cluster moves) for metals and metallic oxides.

## Methods

**1 — MD application (where MD appears vs AKMC).** The perspective’s **primary method** is **adaptive kinetic Monte Carlo (AKMC)**: from each **local minimum**, **escape pathways** are explored using **harmonic transition-state theory**-style treatments and **energy/force calls** (the **ZnO** growth illustration uses **LAMMPS-evaluated ReaxFF energies**). **Conventional MD** appears mainly as a **cross-check** where **Ag on Ag(100)** dynamics overlap **AKMC** predictions at **300 K** on accessible MD timescales, using **periodic boundary conditions** for the **surface slab** models described in the perspective. **N/A — single unified MD production protocol** (timestep, multi-ns trajectory, thermostat damping): the article is not a benchmark **NVT/NPT** study of one slab; it instead **contrasts** AKMC with **MD**, **TAD**, **hyperdynamics**, and **parallel replica** for **rare-event** surface kinetics. **N/A — barostat / macroscopic pressure control** in AKMC framing: the focus is **event catalogs** and **rates**, not constant-pressure MD of a bulk reservoir.

**2 — Force-field training / fitting.** **Worked ZnO example:** uses a **published ReaxFF** parameterization for **ZnO** (cited) as the **interatomic model** inside **AKMC** moves—**no** new **QM refit** is performed in this perspective.

**3 — Static QM / DFT.** **N/A — standalone DFT production protocol**: DFT enters as **literature context** for **barriers** and **materials** systems, not as the paper’s own **ab initio** workflow.

**4 — Review / non-simulation framing.** **JCP perspective** on **rare-event algorithms** for **thin-film growth**; the **Methods** substance is **literature scope + algorithmic comparison**, per **`AGENTS.md` block 4**.

## Findings

AKMC exposes rare-event pathways that are impractical to sample with long MD at experimental fluxes. The Ag and ZnO illustrations show qualitative consistency with MD where timescales overlap, while extending to regimes relevant to deposition rates; the discussion stresses the need to enumerate pathways up to barriers set by the competition between diffusion and arrival kinetics (order \(\sim 0.6\) eV for a representative surface area at 300 K and \(\sim 10\) monolayers per second, as stated in the paper).

## Limitations

- Summary here draws on a **partial** text extract; barrier values, supercell sizes, and AKMC parameters for each figure should be taken from the **full PDF**.
- AKMC accuracy depends on completeness of the event catalog and on the quality of the interatomic model (EAM/EMT vs **ReaxFF** for oxides); transferability to new chemistries is not automatic.
- Work is **methodological** and illustrative rather than a single-material benchmark against experiment.

## Relevance to group

Not authored by the van Duin group. It is still useful corpus context: **ReaxFF** is used as the reactive engine in the **ZnO** growth example alongside AKMC, showing how reactive force fields plug into rare-event surface kinetics workflows that complement reactive MD studies elsewhere in the knowledge base.

## Citations and evidence anchors

- DOI: [10.1063/1.4986402](https://doi.org/10.1063/1.4986402)
- Text-aligned pointers: `normalized/extracts/2017lloyd-venue-paper_p1-2.txt` (introduction and AKMC formulation).

## Reader notes (navigation)

- **Force-field context:** [[reaxff-family]] — ZnO growth example uses a ReaxFF parametrization cited in the article.
- **Methods / rare events:** complements standard reactive MD when experimental time scales are out of reach for MD alone.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
