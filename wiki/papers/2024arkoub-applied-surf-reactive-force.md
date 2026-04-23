---
id: paper:2024arkoub-applied-surf-reactive-force
type: paper
title: "A reactive force field approach to modeling corrosion of NiCr alloys in molten FLiNaK salts"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - material:alloy-bulk
  - task:parameterization
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:lammps
  - keyword:nvt-simulation
candidate_tags:
  - "molten-salt-reactor"
source_refs: []
doi: "10.1016/j.apsusc.2024.159627"
year: 2024
authors:
  - "Hamdy Arkoub"
  - "Swarit Dwivedi"
  - "Adri C. T. van Duin"
  - "Miaomiao Jin"
venue: "Appl. Surf. Sci. 655 (2024) 159627"
pdf_sha256: "2689bf7eeb4a811c6442458d6143fa3a8871371cc2dd7188a8d97e323726d3f3"
pdf_path: "papers/Arkoub_Dwivedi_FLiNaK_salts_AppSurfSci_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024arkoub-applied-surf-reactive-force -->

## Summary

Arkoub, Dwivedi, van Duin, and Jin present an **Applied Surface Science** article (DOI `10.1016/j.apsusc.2024.159627`) that develops a **ReaxFF** description for **Ni–Cr** alloys interacting with **multicomponent molten fluorides**, focusing on **FLiNaK**-class salts relevant to **molten salt reactor** technologies. The motivation is **compatibility**: **Ni-based** structural alloys are candidate materials for high-temperature **fluoride** circuits, yet **corrosion**—often involving **Cr** **depletion** and **interfacial** **speciation**—is difficult to probe **in situ** at **liquid** **salt** **interfaces**. By fitting **ReaxFF** to **first-principles** data for **F** interactions with **metal** surfaces and **molten** **salt** bonding motifs, the authors aim to make **atomistic** **reactive MD** a complement to **electrochemical** and **gravimetric** tests, supplying **mechanistic** hypotheses about **dissolution** pathways and **electrical double layer** structure that continuum models rarely resolve.

## Methods

### ReaxFF training (A)

**DFT** targets: **Ni**, **Cr**, **Li/Na/K/F** **EOS**/**reactions** for **FLiNaK**-relevant stoichiometries.

### Alloy–melt reactive MD (B)

**Ni–Cr** **slabs** + **molten** **fluoride** melts (**NVT**-style per keywords); **RDFs**/structure vs **experiment**/literature; **Li** fraction sweeps for **EDL**/**speciation** vs **Cr** **release**—**Δt**, **T**, **duration** in **`papers/Arkoub_Dwivedi_FLiNaK_salts_AppSurfSci_2024.pdf`**.

**Electrode–electrolyte observables.** The simulations emphasize **interfacial** **Cr** **release** as a function of **melt** composition and **electrical double layer** structure, comparing **radial distribution functions** for **F⁻**/**Li⁺** layering near **Ni**/**Cr** **terminations** with literature expectations for **molten** **fluoride** **salts**. Readers should copy **alloy** compositions (**Ni**/**Cr** ratio), **surface** **facet**, **melt** **stoichiometry**, and **thermostat** settings from the **Methods** section when reproducing reported trends.

**MD application (alloy, molten FLiNaK).** **LAMMPS**+**ReaxFF** on **Ni–Cr** **slabs** wetted by **FLiNaK** **melt** cells—**NVT** as in **Appl. Surf. Sci.** **2024** (keywords); **N/A** for untranscribed **atom** counts, **3D** **PBC**/**slab** vacuum thickness, **time step** (fs), **Nosé–Hoover**/**Berendsen** **thermostat** parameters, and **ps**/**ns** **equilibration**/**production** segments—see **`papers/Arkoub_Dwivedi_FLiNaK_salts_AppSurfSci_2024.pdf`**. **N/A**—**NPT** **barostat** if **isobaric** control is not used. **Melt** **temperature** is the operating window given in the article. **N/A**—macroscopic **external electric** **field**; **N/A**—**umbrella**; **Hydrostatic** **stress** in **NPT** segments **N/A** unless the paper used **NPT**—per **full** **text**.

## Findings

The authors report that **ReaxFF** simulations capture **Cr dissolution** behavior consistent with **fluoride**-mediated **corrosion** phenomenology and strong sensitivity to both **alloy** composition and **melt** chemistry. A highlighted mechanistic motif is that **higher Li content** can promote a **more compact electrical double layer** at the interface, which **mitigates** **Cr dissolution** in the modeled scenarios—linking **electrostatic** **interfacial** structure to **macroscopic** **corrosion** propensity within the force-field approximation. The paper positions these **atomistic** pathways as especially valuable where **experimental** access to **reactive** **interface** chemistry is limited, while stressing that **absolute** **rates** and **long-time** **kinetics** must be interpreted with **ReaxFF** uncertainties inherited from **training** coverage and **DFT** reference choices. **Corrosion** **stakeholders** should pair these **MD** **insights** with **continuum** **mass-transport** and **electrode** **polarization** models when extrapolating to **engineering** **lifing**, because **atomistic** **segments** rarely span **hours** of **real** **time** or **macroscopic** **crevice** **geometries**. **FLiNaK** **composition** shifts (e.g., **impurity** **halides**, **oxide** **carryover**) remain an **operational** **variable** that any **single** **parameter** sweep in the article only partially samples.

## Relevance to group

**ReaxFF** deployment for **nuclear molten-salt** materials compatibility with **Ni-based** alloys—application-forward extension of reactive **metal/halide** chemistry.

## Citations and evidence anchors

- DOI: `10.1016/j.apsusc.2024.159627`

## Related topics

- [[reaxff-family]]
