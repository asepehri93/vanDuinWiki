---
id: paper:2014verners-surface-scie-comparative-molecular
type: paper
title: "Comparative molecular dynamics study of fcc-Ni nanoplate stress corrosion in water"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:water-interfaces
  - keyword:metallic-systems
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1016/j.susc.2014.10.017"
year: 2014
authors:
  - "Osvalds Verners"
venue: "Surface Science, 633 (2015) 94-101. doi:10.1016/j.susc.2014.10.017"
pdf_sha256: "5fba3fadc9476256ea036e48ad58f8a36fb7c84a8927efc03eddb8f598aa63c5"
pdf_path: "papers/Verners_SurfSci_2014_Ni_oxide.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014verners-surface-scie-comparative-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For definitive barriers, collective variables, and full staging tables, use the peer-reviewed PDF—not this page alone.

## Summary

Reactive molecular dynamics with ReaxFF and LAMMPS studies stress-assisted corrosion of fcc Ni nanoplates in water under varied temperature, chemistry, loading, and boundary conditions, comparing bare and pre-oxidized surfaces and probing dissolution with DFT and metadynamics. The work emphasizes **stress corrosion** as a **coupled** **mechano-chemical** failure mode: **water** chemistry and **oxide** coverage shift **dislocation** nucleation barriers while **dissolution** channels compete with **plastic** relaxation in **nanoscale** Ni volumes.

## Methods

**MD application (ReaxFF, Ni nanoplates in water).** Simulations use **LAMMPS** with **ReaxFF** as referenced in the article. **fcc** **Ni** **nanoplate** models are solvated in **water**, comparing **bare** versus **pre-oxidized** surfaces under varied loading and boundary conditions; supercell dimensions, **PBC** handling, fixed versus free regions, and atom counts are tabulated in **`papers/Verners_SurfSci_2014_Ni_oxide.pdf`** (**N/A** for full tables on this page). For the baseline pressurized-aqueous protocol summarized in the computational section, the authors report **NPT** integration with **velocity Verlet** at **0.2 fs**, a **Berendsen** thermostat at **300 K** (**100 fs** damping), and **NPT** pressure targeting **0.405 GPa** (**4000 atm**) with **5000 fs** pressure-damping period. Additional **600 K** aqueous runs probe temperature effects, and structures equilibrated at **300 K**, **600 K**, and **900 K** enter comparisons of oxidation level. Equilibration versus production segment lengths are **N/A** for full duplication here. **Electric-field** driving and **replica** sampling are **N/A** for those baseline paths; **well-tempered metadynamics** with reported bias temperature **2700 K** refines a **Ni–water** **dissolution** pathway alongside **DFT** as described in the paper.

**Force-field training.** **N/A**: a published **ReaxFF** for **Ni/O/H** is applied as cited, not newly fitted in this article’s summary scope.

**Static QM.** **DFT** cross-checks and **metadynamics** collective-variable definitions for **Ni dissolution** are in the article (**N/A** for functional/basis/k-mesh transcription on this page).

## Findings

**Water** chemistry, **faster** mechanical loading, and **higher** temperature **lower** dislocation nucleation barriers and **reduce** strength and ductility versus reference **vacuum** or less aggressive aqueous conditions in the modeled **nanoplates**. **Pre-oxidized** surfaces **raise** initial nucleation barriers relative to **bare** surfaces in the same framework. **Stress triaxiality** and **boundary conditions** strongly modulate strength, ductility, and surface reactivity. **Failure** morphology and **stress/strain** distributions show **size-dependent** behavior across the nanoplate models. A **Ni dissolution** pathway from **metadynamics** is **cross-checked** with **DFT** in the study.

## Limitations

High **strain rates**, **nanoscale** specimen sizes, and **idealized** **oxidation** prep may differ from **macroscopic** SCC experiments; **ReaxFF** transferability for **Ni–water** **dissolution** should be checked against newer **DFT** references when available. **Metadynamics** **bias** parameters influence **dissolution** **path** **sampling**; reported **barriers** should be interpreted with the **well-tempered** **settings** and **collective** **variables** defined in the **full** article. **Nanoplate** **sizes** and **aspect** **ratios** change **stress** **triaxiality**; do not extrapolate **failure** **maps** across **length** **scales** without **convergence** tests described in the **paper**.

## Relevance to group

**Reactive MD** benchmark for **metal–water** interfaces under **stress**, adjacent to **battery** and **corrosion** modeling threads that share **ReaxFF** tooling.

## Citations and evidence anchors

- DOI: [10.1016/j.susc.2014.10.017](https://doi.org/10.1016/j.susc.2014.10.017)

## Related topics

- [[reaxff-family]]
