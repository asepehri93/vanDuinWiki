---
id: paper:2020hahn-venue-atomistic-understanding
type: paper
title: "Atomistic understanding of surface wear process of sodium silicate glass in dry versus humid environments"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - method:reaxff
  - material:silicate-glass
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:tribology
  - keyword:water-interfaces
  - keyword:reaxff-application
  - keyword:lammps
source_refs: []
doi: "10.1111/jace.17008"
year: 2020
authors:
  - "Seung Ho Hahn"
  - "Hongshen Liu"
  - "Seong H. Kim"
  - "Adri C. T. van Duin"
venue: "J. Am. Ceram. Soc."
pdf_sha256: "d161ecdc1704167bea2c85601726eae52f9c124592e7d55d70c9b28c76b87cd8"
pdf_path: "papers/Hahn_Surface_Wear_JACerS_2020.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020hahn-venue-atomistic-understanding -->

## Summary

**Glass wear** in humid environments is often attributed to **stress corrosion** and **hydrolysis**, but atomistic mechanisms coupling **shear**, **water**, and **network modifiers** such as **Na⁺** remain under-resolved. Hahn, Liu, Kim, and van Duin simulate **sodium silicate** versus **silica** counterfaces with **ReaxFF molecular dynamics**, contrasting **dry** and **humid** sliding where **interfacial water** is treated explicitly. The study focuses on how **Si–O–Si bridging bonds** form across the interface under shear and how **sodium** participates in **hydrolytic** pathways that generate **hydroxyl**-rich surfaces.

## Methods

The authors prepare **amorphous** **Na–Si–O** and **SiO₂** **slab**-like **supercells** (thousands of **atoms**), then impose **sliding** with **PBC** in the shear plane as in *J. Am. Ceram. Soc.* **Molecular dynamics** in **LAMMPS** with **ReaxFF**; **NVT** or equivalent **thermostat**-controlled **temperature** (stated in **K** in the paper); **timestep** in **femtoseconds**; **duration** of **nanoseconds**-scale **production** relative to the shear protocol. **N/A** for **NPT** **barostat** / **GPa** **hydrostatic pressure** in typical shear stages—confirm in PDF. **Humid** cases add **H₂O** at the interface; **N/A — electric field**; **N/A — metadynamics**. Analysis tracks **bond** formation, **subsurface** mixing, and **hydroxylation** under **load**.

## Findings

Under **dry** shear, simulations show **aggressive wear** accompanied by **interfacial Si–O–Si bridges** that couple the two bodies and transmit stress into the **subsurface**, promoting **plastic** rearrangement and **material transfer**. Adding **interfacial water** suppresses formation of these **bridging** motifs, consistent with **lower wear** in **humid** conditions within the same modeling framework. **Leachable Na⁺** facilitates **water-driven** reactions that produce **silanol**-rich layers; the manuscript discusses how this **modifier-assisted hydrolysis** alters the **mechanochemical** balance compared with **pure silica** contacts. The **Introduction** highlights a broader experimental puzzle: some **sodium-bearing** **silicate** glasses show **improved** wear resistance as **relative humidity** rises—contrary to naïve **stress-corrosion** expectations—whereas several **non-leachable** glasses instead show **monotonic** wear increases with humidity; the **atomistic** study is positioned to rationalize such contrasts through **ion leaching** and **interfacial chemistry** rather than humidity alone.

**Post-processing** in the article separates **wear** **fragments** by **connectivity** to each **slab** so **third-body** **formation** can be quantified as a function of **RH** and **composition**.

## Limitations

ReaxFF remains empirical: transferability to other glass compositions, exact load/velocity mapping to experiment, and long-time wear volumes require the caveats stated in the paper.

For **retrieval**, pair this entry with **bulk** **hydrated** **silica** mechanics (**[[2019mei-acta-materia-effects-water]]**) when questions ask how **water** **speciation** differs between **volume** and **sliding** **interface** environments.

## Relevance to group

Core **tribochemistry / glass wear** reference from the **van Duin** collaboration—pairs naturally with other **Si–O** and **mechanochemical** entries in the corpus.

## Reader notes (navigation)

Cross-link **hydrated silica** mechanical entries such as **`[[2019mei-acta-materia-effects-water]]`** when questions separate **bulk** water speciation from **interfacial** wear chemistry. **Load** and **sliding speed** ranges in the publication define where **ReaxFF** remains tractable; extrapolate to **MPa** contacts only with explicit **multiscale** justification.

## Citations and evidence anchors

- DOI: [10.1111/jace.17008](https://doi.org/10.1111/jace.17008)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
