---
id: paper:2018jcp-silica-hydrophil-venue-paper
type: paper
title: "The hydrophilic-to-hydrophobic transition in glassy silica is driven by the atomic topology of its surface"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - material:silicate-glass
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:water-interfaces
  - keyword:silica-silicate
  - keyword:lammps
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1063/1.5010934"
year: 2018
authors:
  - "Yingtian Yu"
  - "N. M. Anoop Krishnan"
  - "Morten M. Smedskjaer"
  - "Gaurav Sant"
  - "Mathieu Bauchy"
venue: "J. Chem. Phys."
pdf_sha256: "e150c30b60ee0f13c041848ef40b846e2bccf5ff012ad33a290cc48d250ac366"
pdf_path: "papers/ReaxFF_others/JCP-silica-hydrophilicity.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2018jcp-silica-hydrophil-venue-paper -->

## Summary

Wetting of silica controls friction, dissolution, and chemical durability in aqueous environments, yet linking silanol coverage to atomistic network topology remains contentious. Yu et al. generate artificial glassy silica surfaces with reactive molecular dynamics using the Pitman Si/O/H ReaxFF parameterization in LAMMPS with the user-reaxc package and charge equilibration. They anneal surfaces to different temperatures to vary rigidity and silanol population, then expose the surfaces to water to follow bond-making and bond-breaking events. Topological constraint theory metrics correlate network flexibility with reactivity and hydrophilicity, arguing that higher annealing temperatures yield more stable, less hydrophilic surfaces through lower silanol density rather than through roughness alone. The study explicitly challenges explanations that ascribe wetting shifts solely to geometric roughness without reference to chemical speciation.

## Methods

Simulations employ ReaxFF with QEq charges as described for silica–water chemistry in the article. Glassy silica slabs are prepared with controlled thermal history to modulate surface topology before water contact. Reactive trajectories track dissociative versus molecular water adsorption and subsequent silanol interconversion. Topological constraint theory quantities such as constraints per atom are used alongside chemical descriptors from the trajectories. Analysis couples rigidity percolation ideas with local silanol reactivity metrics extracted from trajectories. Reproducibility requires the cited ReaxFF file, annealing schedules, slab dimensions, water loading, temperature, timestep, and LAMMPS input settings from *J. Chem. Phys.* DOI 10.1063/1.5010934.

**Integrated MD protocol (from article scope; confirm numerics in PDF).** **Engine:** **LAMMPS** with **USER-REAXC** and the **Pitman** **Si/O/H** **ReaxFF** parameterization plus **QEq** charges as reported. **Systems:** artificial **glassy silica** **slabs** with controlled **annealing** **temperature** histories, then **water** exposure to follow dissociative/molecular adsorption and silanol interconversion (**atom** counts, **supercell** vectors, and water loadings in **Methods**). **Boundaries:** **three-dimensional PBC** for slab models unless the article specifies otherwise. **Ensemble / timestep / duration:** **NVT**/**NVE** staging and integration **timestep** in **fs**, **equilibration**/**production** lengths in **ps**/**ns**; **thermostat** coupling (e.g., **Nosé–Hoover** or **Berendsen** as implemented for water contact) is specified in the **JCP** *Methods*—**N/A — exact damping constants and trajectory lengths not transcribed on this page**; use `pdf_path` (corpus `extraction_quality: partial` plus short local extract). **Barostat:** **N/A — NPT** not emphasized for the summarized reactive slab protocol if the article uses fixed-cell **NVT** for water contact—confirm in **PDF**. **Pressure targets:** **N/A — bulk GPa/bar stress control** unless explicitly reported. **Electric field:** **N/A — external electric bias** not part of the wetting study. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not indicated in the indexed abstract.

## Findings

**Outcomes and mechanisms.** The **hydrophilic-to-hydrophobic** shift tracks **silanol** **surface** **density**, which the authors tie to **atomic topology** (topological constraint theory) of the **glassy** **surface** rather than to **roughness** alone. **Water** **adsorption**/**reaction** trajectories link **network rigidity** metrics to **interface** **reactivity**.

**Comparisons.** The discussion contrasts **topology-first** explanations with **roughness**-centric narratives in prior **literature** on **silica** wetting.

**Sensitivity.** **Annealing temperature** modulates **silanol** population and **rigidity**, shifting modeled **hydrophilicity** along the processing sequence.

**Limitations and corpus honesty.** **ReaxFF** parametrization limits quantitative barriers; multicomponent industrial glasses are omitted. This note is grounded in the **JCP** abstract/extract and `pdf_path`; **pagination-level** numerics and full **Methods** tables must be taken from the **PDF** because local text is **partial**.
## Limitations

ReaxFF parametrization choices affect quantitative barriers; industrial glasses contain modifiers not modeled here.

## Relevance to group

Silica–water ReaxFF surface chemistry benchmark adjacent to [[2018jessica-m-rimsza-journal-of-g-chemical-effects]] fracture study.

## Citations and evidence anchors

- DOI: `10.1063/1.5010934`.

## Related topics

- [[2018jessica-m-rimsza-journal-of-g-chemical-effects]]
- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
