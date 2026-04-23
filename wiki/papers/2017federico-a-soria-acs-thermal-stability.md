---
id: paper:2017federico-a-soria-acs-thermal-stability
type: paper
title: "Thermal stability of organic monolayers grafted to Si(111): insights from ReaxFF reactive molecular dynamics simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - material:widegap-semiconductor
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.7b05444"
year: 2017
authors:
  - "Federico A. Soria"
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
  - "Eduardo M. Patrito"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "cb8bc2c9c1cc66c28fa8ff113a4dda9384b364543bfe4226edd4b59fd54a0c51"
pdf_path: "papers/Soria_Organic_Silicon_ACS_AMI_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017federico-a-soria-acs-thermal-stability -->

ReaxFF reactive MD heats Si(111) surfaces grafted with n-alkyl (half coverage) or small unsaturated hydrocarbons (full coverage) to map radical-driven dehydrogenation, fragment desorption, and hydrogen passivation during thermal annealing.

## Summary

The authors simulate thermal decomposition of hydrocarbon monolayers covalently attached to Si(111) using a Si/C/H ReaxFF parametrization for surface-organic chemistry. Homolytic Si–C bond cleavage generates silyl radicals that propagate dehydrogenation and desorbing fragments. Flexible n-alkyl chains primarily undergo β-hydrogen elimination toward 1-alkenes, but lower grafting density permits deeper backbone dehydrogenation. Rigid propynyl and propenyl substituents hinder certain hydrogen abstractions and raise effective stability relative to saturated chains. As organic coverage is lost, the surface trends toward hydrogen-terminated silicon. The study is relevant to thermal budgets during semiconductor processing and hybrid organic–inorganic devices where monolayer integrity sets electronic passivation.

## Methods

**A — Force-field training / fitting:** **Si/C/H ReaxFF** parametrization for **surface–organic** chemistry on **silicon** is used as documented in the article (**no** new fit campaign summarized on this page).

**B — Molecular dynamics / reactive sampling:** **Reactive MD** on **Si(111)** with **50%** coverage **n-alkyl** (**ethyl**–**decyl**) and **full**-coverage **methyl**, **propynyl**, **propenyl** grafts. **Thermal ramps** and **holds**, **thermostat**, **timestep**, and **duration** are specified in the journal **Methods**. Analysis follows **bond-order** events, **radical** populations on **lattice** sites, and **desorbing** species.

**C — DFT / static QM:** **Not** the primary engine for annealing trajectories here—**ReaxFF** carries **reactive** **thermal decomposition**.

**D — Review / non-simulation framing:** **Primary** **ACS Appl. Mater. Interfaces** study of **monolayer** **thermal stability**—not a literature review.

**Engine:** **ReaxFF** **reactive MD** on **Si(111)** **hydrocarbon** monolayers as in **Methods** of the article. **System:** **50%**-coverage **n-alkyl** (**ethyl–decyl**) and **full**-coverage **methyl**, **propynyl**, **propenyl** grafts; **atom counts** and **supercell vectors** are given in the **PDF**. **Boundaries / periodicity:** **N/A —** not restated on this wiki page (expect **3D PBC** **slab** conventions typical for **Si(111)** **ReaxFF** anneals—confirm in-source). **Ensemble / timestep / thermostat / barostat / production length:** **N/A —** thermal **ramps**, **hold temperatures**, **timestep (fs)**, **thermostat** choice/damping, and **NVT vs NPT** segments are **not** copied here—use **`pdf_path`**. **Pressure:** **N/A —** not emphasized for the **surface annealing** protocol summarized. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

## Findings

Silyl radicals produced by Si–C homolysis control overall dehydrogenation kinetics, so mechanisms are not reducible to single-silicon β-elimination pictures alone. Dominant decomposition channels involve two neighboring lattice silicon centers rather than an isolated site. For n-alkyl chains, abstraction at the β carbon is most common, yet at lower coverage chain flexibility permits hydrogen stripping from interior CH₂ units and even terminal methyl groups on long chains. Propynyl and propenyl rigidity blocks some abstraction pathways accessible to saturated chains, yielding higher relative thermal stability. Throughout decomposition, Si–H bond formation accumulates until the surface approaches hydrogen-passivated silicon. Desorbing fragments reported in the article include small alkenes and hydrogen-rich species whose identities tie back to the radical cascade initiated at Si–C scission.

## Limitations

Barrier heights and effective onset temperatures depend on the ReaxFF parametrization; quantitative comparison with experiment requires the measurements cited in the original paper.

## Relevance to group

Van Duin-group contribution on organic monolayer stability at silicon interfaces, relevant to passivation, microelectronics processing, and hybrid organic–inorganic materials.

## Citations and evidence anchors

- DOI: [10.1021/acsami.7b05444](https://doi.org/10.1021/acsami.7b05444)

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Revised in **Stage A / wave 004 / batch 08**.
