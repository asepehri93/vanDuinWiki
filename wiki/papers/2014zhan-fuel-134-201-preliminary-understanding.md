---
id: paper:2014zhan-fuel-134-201-preliminary-understanding
type: paper
title: "Preliminary understanding of initial reaction process for subbituminous coal pyrolysis with molecular dynamics simulation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - domain:carbon-hydrocarbon
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:berendsen-thermostat
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2014.06.005"
year: 2014
authors:
  - "Jin-Hui Zhan"
  - "Rongcheng Wu"
  - "Xiaoxing Liu"
  - "Shiqiu Gao"
  - "Guangwen Xu"
venue: "Fuel"
pdf_sha256: "9bb184016da1a0cecf86c2434558fe6ab2ff2ffeb38d13a57fea8c9ed7542f60"
pdf_path: "papers/ReaxFF_others/Preliminary understanding of initial reaction process for subbituminous coal pyrolysis with molecular dynamics simu.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014zhan-fuel-134-201-preliminary-understanding -->

## Summary

**Subbituminous coal** pyrolysis releases a complex mixture of **light gases** and **tars** whose **early bond-breaking** chemistry sets downstream **soot** and **liquid** yields. **Zhan** et al. build a **three-dimensional Hatcher-type subbituminous** structural model and follow **initial thermal decomposition** with **ReaxFF molecular dynamics**, augmented by **DFT** on representative **radicals** to clarify **homolytic** versus **heterolytic** character where the force field is ambiguous. The **Fuel** article focuses on **first-nanosecond** chemistry accessible to **reactive MD**, emphasizing **CO**, **CO\(_2\)**, **CH\(_4\)**, and **H\(_2\)** formation routes rather than full **char** maturation.

## Methods

**MD application (subbituminous coal pyrolysis onset).** The authors build a **three-dimensional Hatcher-type subbituminous** coal model (composition, atom count, and cell vectors in **`papers/ReaxFF_others/Preliminary understanding of initial reaction process for subbituminous coal pyrolysis with molecular dynamics simu.pdf`**) and run **ReaxFF** **molecular dynamics** in a **PBC** bulk cell. After annealing (**10** **NVT** cycles **300–1300 K**), they equilibrate with **NPT** near **300 K** to **0.78 g cm\(^{-3}\)** at **0.2 GPa** (**Berendsen** barostat, **500 fs** damping), relax **10 ps** **NVT** at **300 K**, then use a staged heating scan **300–2800 K** to bracket bond-cleavage **onset** before **1 ns** **NVT** production segments at selected high temperatures (**velocity Verlet**, **0.25 fs**; **Berendsen** thermostat, **100 fs** damping). **Electric fields**, **replica** sampling, and **shock** loading are **N/A** for this protocol.

**Force-field training.** **N/A** — a published **ReaxFF** parametrization for coal-like **C/H/O** chemistry is applied as cited, not refitted here.

**Static QM (spot checks).** **DFT** on representative **radicals** and **fragmentation** steps supports interpretation where **ReaxFF** ambiguity arises; full functional, basis, and **k**-sampling settings are in the journal **Methods** (**N/A** to tabulate on this page).

## Findings

**Initial** pyrolysis favors scission of comparatively **weak C–C** and **C–O** bridges embedded in the macromolecular model. **CO** tracks **decarbonylation** from **carbonyl** groups, while **CO\(_2\)** emerges from **hydrogen-transfer** sequences coupled to **carboxyl** **decarboxylation**. **CH\(_4\)** arises when **methyl-like** radicals abstract **H** from **hydroxyl** sites, and **H\(_2\)** forms by **recombination** of **H** atoms released across functional groups. A **C\(_9\)H\(_9\)O** radical appears as a **hub** en route to **cresol-type** products when **H-donor** environments persist. The authors relate these pathways to **prior experimental** signatures cited in their references. Because the **Hatcher** model is a **coarse** **macromolecular** **surrogate**, absolute **yield** predictions should be treated as **qualitative** indicators of **early** **product** **distribution** rather than **quantitative** **kinetic** **models** for **industrial** **reactors**.

## Limitations

**Nanosecond** trajectories capture **onset** chemistry but not **slow** **cross-linking** or **mass-transfer** limited release in reactors. **ReaxFF** errors on **barriers** should be **spot-checked** with **QM** for quantitative **Arrhenius** parameters.

## Relevance to group

Provides **corpus** context for **reactive hydrocarbon** systems adjacent to **van Duin**-line **combustion** and **pyrolysis** applications, though authorship is external to the host group.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1016/j.fuel.2014.06.005](https://doi.org/10.1016/j.fuel.2014.06.005)

## Related topics

- [[reaxff-family]]
