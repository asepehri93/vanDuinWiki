---
id: paper:2018khajeh-langmuir-201-mechanochemical-association
type: paper
title: "Mechanochemical Association Reaction of Interfacial Molecules Driven by Shear"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:tribology
  - keyword:reactive-md
  - keyword:oxide-surface
  - keyword:lammps
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.langmuir.8b00315"
year: 2018
authors:
  - "Arash Khajeh"
  - "Xin He"
  - "Jejoon Yeon"
  - "Seong H. Kim"
  - "Ashlie Martini"
venue: "Langmuir 2018, 34, 5971–5977"
pdf_sha256: "6c84bf921ece7535a63dd2b87bdfaf0a469878311ac9bbcb4dad29219928f9ae"
pdf_path: "papers/ReaxFF_others/Khajeh_Mechanochem_Langmuir_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018khajeh-langmuir-201-mechanochemical-association -->

## Summary

Combines **vapor-phase lubrication** experiments on **α-pinene** between **hydroxylated** versus **dehydroxylated silica** with **ReaxFF molecular dynamics** in **LAMMPS** (postprocessed with **OVITO**) to interpret **shear-induced polymerization**. The work emphasizes **oxidative chemisorption** from the **oxide surface** as an activation step and **ether-forming association** between activated species, linking **molecular distortion** to **mechanochemical** activation. **Tribopolymer** formation is treated as a **stress-biased** reaction pathway: **shear** concentrates **strain** near **asperity** contacts where **oxygen** transfer from **silica** can initiate **radical-like** intermediates that would be rare under **thermal** equilibrium alone.

## Methods

- **Experiments:** Reciprocating **ball-on-flat** tribometer; **hydroxylated** (RCA-1 + UV/ozone) vs **dehydroxylated** (450 °C, N₂) **silicon**; **borosilicate** counter-balls; **α-pinene** at **30–40%** of saturation; **4 mm/s** sliding; **AFM** of products; **XPS** of carbon environments; reported **Hertzian** contact pressure **0.32 GPa** in a representative condition in the article.
- **Simulations:** **ReaxFF** MD in **LAMMPS**; workflow includes **energy minimization**, **compression**, and **sliding** stages (see Fig. 1 in the paper); additional numerical settings in **Supporting Information**.
- **Analysis:** **Contact** **stress** and **temperature** estimates justify treating **flash heating** as secondary for the cited **sliding speed** window.

**Simulation protocol (MD application).** **LAMMPS** **ReaxFF** trajectories follow **energy minimization**, **compression**, and **sliding** stages (**Fig. 1**); **PBC** **supercells** represent the **silica**/**α-pinene** **interface** with **atom** counts and **slab** dimensions in **Methods**/**SI**. **Ensemble / thermostat / timestep / duration:** reported in **Supporting Information**—this summary defers exact **NVT**/**NVE** staging, **timestep** (**fs**), and **production** **ns** values to `pdf_path`. **Barostat:** **N/A — NPT** bulk **pressure** control not the focus of the shear cell as summarized. **Hydrostatic pressure targets:** **N/A** for the quoted **tribology** protocol beyond **contact** **stress** analysis (**0.32 GPa** **Hertzian** example in **experiment**). **Electric field:** **N/A — bias** not applied in **MD**. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not indicated.

## Findings

**Outcomes.** **Shear** promotes **oxidative** activation of **α-pinene** via **oxygen** transfer from **silica**, then **ether** **linkages** between **activated** and neighboring molecules—a **mechanochemical** route distinct from purely **thermal** **decomposition**.

**Comparisons.** **Dehydroxylated** **silicon** shows higher **tribopolymer** yield and **friction** than **hydroxylated** surfaces under the same **VPL** window, aligning **experiment** with higher **surface** **reactivity**.

**Sensitivity.** **Surface** **hydroxyl** **coverage**, **sliding speed** (**4 mm/s** in **experiment**), and **vapor** **saturation** (**30–40%**) modulate **film** formation.

**Limitations and PDF grounding.** **ReaxFF** needs **system-specific validation**; **flash temperature** estimates are secondary but **interface** chemistry remains **complex**. Detailed **MD** controls: **`pdf_path`**.
## Limitations

- **ReaxFF** requires **system-specific validation**; the paper notes this explicitly for **new chemistries**.
- **Flash temperature** rise from friction is estimated as **small** in the reported sliding condition, but **interface** conditions remain **complex** and **time-dependent**.

**Curation note:** the **Langmuir** article sits in the same **silica** / **organic** **tribochemistry** cluster as **[[2019chen-venue-science-journals]]** (graphite steps) and **[[theme-oxides-silica-ceramics]]**; retrieval agents should prefer **DOI-linked** pagination over ad-hoc figure numbers if the local PDF is updated. Experimental **VPL** conditions deliberately avoid full **liquid** films so that **vapor-phase** chemistry dominates the **shear** interface. **XPS** **C 1s** assignments in the article distinguish **ether** **products** from **residual** **hydrocarbon** backgrounds.

## Relevance to group

Demonstrates **ReaxFF** used alongside **tribology** experiments on **silica/organics**, relevant to **interface chemistry** under **shear**.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acs.langmuir.8b00315](https://doi.org/10.1021/acs.langmuir.8b00315)

## Reader notes (navigation)

- [[theme-oxides-silica-ceramics]]

## Related topics

- [[reaxff-family]]
