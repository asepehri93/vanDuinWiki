---
id: paper:2022lee-npj-computat-dynamic-observation-2
type: paper
title: "Dynamic observation of dendrite growth on lithium metal anode during battery charging/discharging cycles"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:li-metal-anode
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:lammps
  - keyword:charge-equilibration
source_refs: []
doi: "10.1038/s41524-022-00788-6"
year: 2022
authors:
  - "Hae Gon Lee"
  - "Se Young Kim"
  - "Joon Sang Lee"
venue: "npj Comput. Mater."
pdf_sha256: "bd9172d87f3763ac8731ed6ddea7adf1f23344d3a8b67900a906188c5be9b96b"
pdf_path: "papers/ReaxFF_others/Lee_npjCompMat_Li_dendrite.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022lee-npj-computat-dynamic-observation-2 -->

## Summary

**Reactive MD** with **ReaxFF** is coupled to **EChemDID** (electrochemical dynamics with an implicit electronic degree of freedom) to model **Li-metal** anodes under **cyclic voltage** with **bond-making/breaking** at the **SEI**/**electrolyte** interface. The protocol aims to capture **morphological evolution** of **dead Li** and **dendrites** during repeated **charge/discharge** with **interfacial** chemistry—notably using **realistic** electrode **voltage** driving fields rather than ad hoc uniform fields on electrolyte alone. A case study adds **HF** to an **ethylene carbonate (EC)**-based organic electrolyte, reporting that **beneficial decomposition** chemistry yields a **protective interphase** that **suppresses** large **volume swings** and **parasitic** degradation. The **npj** article frames the problem as **time-resolved** **interface** **evolution**: **SEI** **species** **redistribute** across **cycles**, and **dendrite** **morphology** is tracked as an **emergent** **consequence** of **coupled** **electrochemical** driving and **reactive** **bond** **events**, rather than as a **purely** **geometric** **Li** **plating** **instability** in a **nonreactive** **electrolyte** model.

## Methods

- **Reactive dynamics:** **ReaxFF MD** for bond-order chemistry at the **Li**/**organic electrolyte** interface.
- **Electrochemistry:** **EChemDID** to propagate **electrochemical** variables consistent with applied **cyclic potentials** (see article for implementation details, timestep, and system dimensions).
- **Additive study:** **HF**-containing **EC** electrolyte vs. reference cases to probe **SEI** formation and **dendrite** suppression.
- **Analysis:** **Trajectory** **post-processing** emphasizes **morphological** **markers** for **dead** **Li** and **filament** **growth** tied to **local** **composition** **changes** in the **organic** **phase** and at **Li** **surfaces** as **cycles** **accumulate** (see **npj** figures for definitions).

**MD + EChemDID:** **Engine: LAMMPS** **ReaxFF**; **Li** | **organic** **electrolyte** **interfacial** **cells** with **3D** **PBC**; **NVT** with **~0.25 fs** (or **stated**) **timestep**; **cyclic** **voltage** / **electrode** **potential** **(EChemDID)** as **equivalent** **to** **time-dependent** **bias** **(battery-relevant** **E**/**potential** **driving**); **ps**–**ns** **cumulative** **sampling**; **Nose–Hoover**-class **thermostat** at set **temperature** in **K**; **barostat** **N/A** if **fixed** **box**; **hydrostatic** **pressure** **N/A** unless **NPT**; **N/A** **replica** **exchange**; **Supercell** **atom** **counts** and **box** **geometry** in the **npj** **Methods**/**figures** (not restated here).

## Findings

**Outcomes: time-resolved** **dendrite** / **dead** **Li** **morphology** under **cyclic** **EChemDID** **driving**; **HF**+**EC** case shows **SEI** **chemistry** that **passivates** vs. **baseline**. **Comparisons: versus** **additive**-**free** **baseline** in the **paper**; **not** direct **experiment** **morphology** **fit**. **Sensitivity: voltage** **cycling** and **local** **HF**-**catalyzed** **reactions**. **Limitations:** **size**/**time** **vs** real **cells**—**authored** **caveats** in *npj*. **Corpus: duplicate** **pdf_path**; same **narrative** as **sibling** **[[2022lee-npj-computat-dynamic-observation]]** **(identical** **DOI/SHA-256**).

Simulations provide **time-resolved** visualization of **dendrite** and **dead-Li** growth tied to **interfacial** reactions. The **HF** additive scenario shows **passivating** films that **limit** detrimental expansion and **side reactions** compared to the baseline description in the paper. The **npj Comput. Mater.** framing emphasizes **cyclic** **electrode** **potentials** with **EChemDID** so that **electrolyte** chemistry and **Li** **deposition** evolve under **battery-relevant** driving rather than static **interfacial** snapshots alone; readers should map reported **morphology** trends back to the **HF**-containing **EC** **electrolyte** case highlighted in the abstract versus any **additive-free** baseline the authors include.


## Limitations

System sizes/timescales remain below macroscopic cells; quantitative voltage windows should be validated against experiment. **Duplicate** **PDF** registration in this corpus (see Reader notes) does not change the **scientific** text—only **filename** provenance.

## Relevance to group

Shows **ReaxFF + EChemDID** workflow for **Li-metal** **electrodeposition**—aligned with **battery** interface modeling in the broader corpus.

## Citations and evidence anchors

- DOI: [10.1038/s41524-022-00788-6](https://doi.org/10.1038/s41524-022-00788-6)

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]

## Reader notes (navigation)

- **Corpus catalog (duplicate registration):** [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) · [local](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (entries **2022lee-npj-computat-dynamic-observation** / **-2**)
- Sibling slug: [[2022lee-npj-computat-dynamic-observation]] (identical SHA-256 and DOI; alternate `pdf_path` filename)
