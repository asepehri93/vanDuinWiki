---
id: paper:2014zhang-venue-research
type: paper
title: "Development of a ReaxFF Reactive Force Field for Tetrabutylphosphonium Glycinate/CO2 Mixtures"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:nvt-simulation
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1021/jp5054277"
year: 2014
authors:
  - "Bo Zhang"
  - "Adri C. T. van Duin"
  - "J. Karl Johnson"
venue: "J. Phys. Chem. B"
pdf_sha256: "e7bb5e5930b6656bdf3a47e9eeecc53cec6e789b7692d7d22776cb1952df3546"
pdf_path: "papers/Zhang_Johnson_IL_CO2_capture_JPC_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014zhang-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

## Summary

This Journal of Physical Chemistry B article develops a ReaxFF parametrization for the ionic liquid tetrabutylphosphonium glycinate interacting with carbon dioxide, denoted [P(C\(_4\))\(_4\)][Gly], motivated by tunable CO\(_2\) capture in ionic liquids spanning physisorption through chemisorption. The glycinate anion contains both carboxylate and amine-like functionality, so the authors expect simultaneous physical, complexation, and reactive interactions with CO\(_2\). The training set combines periodic density functional theory pathways for CO\(_2\) reacting with the anion in the condensed phase, condensed-phase molecular dynamics configurations, gas-phase ion–CO\(_2\) interactions, and gas-phase cluster models for intra-ion interactions. Bo Zhang, Adri C. T. van Duin, and J. Karl Johnson validate the optimized force field against QM references and selected experimental trends. The introduction further motivates ionic-liquid CO\(_2\) capture by comparing aqueous amine scrubbing costs and solvent degradation to the tunability of ionic liquid–CO\(_2\) interaction strengths, and it explains why simple nonreactive force fields are insufficient when chemisorption and charge-transfer complexes appear, motivating a unified reactive treatment such as ReaxFF for simultaneous physisorption and reaction pathways. Experimental context for phosphonium amino-acid ionic liquids includes supported-IL formats that mitigate viscosity limitations during uptake, with spectroscopic evidence for carbamate-like products discussed in the cited primary literature.

## Methods

Training-set construction for the reactive parametrization follows the abstract: **periodic DFT** pathways for **CO\(_2\)** reacting with the **glycinate** anion in the condensed phase, **condensed-phase MD** snapshots for structural diversity, and **gas-phase cluster** models capturing **ion–CO\(_2\)** and **intra-ion** interactions. After fitting, production molecular dynamics is carried out in **LAMMPS**. The methods section reports **NpT** equilibration and density measurements using a **0.5 fs** timestep with **Nosé–Hoover** thermostat (**50 fs** damping) and **Nosé–Hoover** barostat (**500 fs** damping) at **1 atm**, supplemented by **NVT** segments and short **NVE** segments at **0.25 fs** timestep for energy conservation checks. These protocols are used to compare **ReaxFF**-based structural sampling with **DFT**-based molecular dynamics distributions for key intermolecular coordinates, emphasizing distribution-level agreement for the **C(CO\(_2\))–N(anion)** distance and **CO\(_2\)** bending angle rather than single average bond lengths.

**MD application (distribution + density benchmarks).** Production **MD** uses **LAMMPS** with **NpT** equilibration/density measurements at **0.5 fs** using **Nosé–Hoover** thermostat (**50 fs** damping) and **Nosé–Hoover** barostat (**500 fs** damping) at **1 atm**, supplemented by **NVT** segments and short **NVE** energy-conservation checks at **0.25 fs** (methods summary on this page). System sizes, full staging tables, trajectory lengths, and electrostatic/cutoff conventions are **N/A** here—see **`papers/Zhang_Johnson_IL_CO2_capture_JPC_2014.pdf`**.

**Force-field training (IL + CO\(_2\) ReaxFF).** Training-set composition matches the abstract (condensed-phase **DFT** pathways, **MD** snapshots, gas-phase clusters) as summarized in **`## Summary`**; optimization software, weights, and full **QM** settings are **N/A** on this page (**PDF**/**SI**).

**Static QM.** **Periodic DFT** pathways and **DFT-based MD** anchor training/validation (abstract + methods); detailed **DFT** protocols are **N/A** for transcription here.

## Findings

The optimized ReaxFF parametrization is reported to capture essential features of both physical and chemical interactions between CO\(_2\) and [P(C\(_4\))\(_4\)][Gly] relative to the QM training data and selected comparisons to van der Waals-corrected DFT or classical descriptions where applicable. Probability distributions for the distance between the carbon atom of CO\(_2\) and the nitrogen atom of the anion, and for the CO\(_2\) bending angle, agree in broad terms between ReaxFF MD and DFT-based MD at the thermodynamic states considered, supporting the claim that the parametrization captures chemisorption motifs and thermal fluctuations sampled in the condensed-phase reference simulations. The authors further predict that mixture density increases with CO\(_2\) concentration up to at least 50 mol % CO\(_2\), attributing part of the densification to the comparatively small effective volume occupied by chemisorbed CO\(_2\) species. They note that this density trend may be tested experimentally.

## Limitations

Transferability to other **ionic-liquid** chemistries requires retraining; **long-time** **diffusion** and **viscosity** are not the sole focus of the parametrization exercise emphasized in the abstract.

## Relevance to group

**van Duin** co-authorship on **ReaxFF** for **CO\(_2\)** **capture** in **phosphonium glycinate** melts—bridges **reactive** **IL** simulation to **separation** applications.

## Citations and evidence anchors

- DOI: [10.1021/jp5054277](https://doi.org/10.1021/jp5054277)
- `normalized/extracts/2014zhang-venue-research_p1-2.txt`

## Reader notes (navigation)

- Ionic liquids + CO\(_2\): separation / capture thread; [[reaxff-family]] (van Duin co-author).

## Related topics

- [[reaxff-family]]
