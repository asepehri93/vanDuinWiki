---
id: paper:2016roghayyeh-lotfi-j-phys-chem-jp6b09729
type: paper
title: "A reactive force field study on the interaction of lubricant with diamond-like carbon structures"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b09729"
year: 2016
authors:
  - "Roghayyeh Lotfi"
  - "ASM Jonayat"
  - "Adri C. T. van Duin"
  - "Mousumi M. Biswas"
  - "Robert Hempstead"
venue: "J. Phys. Chem. C"
pdf_sha256: "5bb03f8337b93824d8a3106ce81c56ac06144a0005f7c11ffd061af1ef417a5c"
pdf_path: "papers/Lotfi_2016_DLC_paper.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016roghayyeh-lotfi-j-phys-chem-jp6b09729 -->

## Summary

Hard-disk interfaces rely on nanometer-thin perfluoropolyether (PFPE) lubricants to limit wear and friction between flying heads and rotating media; heat-assisted recording and tighter head–media spacing increase sensitivity to lubricant desorption and chemical degradation. This *Journal of Physical Chemistry C* article applies ReaxFF molecular dynamics to the Demnum-class PFPE **D4OH** interacting with diamond-like carbon (DLC) films intended to mimic protective overcoats, comparing neat DLC with hydrogenated DLC and nitrogen-containing hydrogenated DLC (DLC:H:N) variants. Industrial motivation is underscored by coauthors from Western Digital, while Adri C. T. van Duin leads the reactive force-field modeling at Penn State. The narrative ties lubricant spreading kinetics and thermal/chemical degradation networks to the local bonding character of each DLC class, arguing that surface functionalization changes not only mechanical contact but also the radical and fragmentation chemistry accessible during reactive trajectories.

## Methods

**1 — MD application (ReaxFF).** **Diamond-like carbon (DLC)** films are built by **melting** an initial **carbon-diamond** arrangement in an **Ar-filled** cell at **7500 K**, **cooling** to **3000 K**, then running **constant-pressure (NPT) MD** to relax **volume** and **internal stress**. **Hydrogenated DLC (DLC:H)** is grown by **pyrolyzing ethylene** as a carbon source with **Ar** present. **DLC:H:N** is obtained by **heating DLC:H** with **N\(_2\)**, tuning **Ar** and **N\(_2\)** inventories so that the model approaches reported **H/N/C** composition and **sp\(^2\)/sp\(^3\)** targets. The abstract reports final **sp\(^3\):sp\(^2\)** ratios of **27.3%** (DLC) and **31.7%** (DLC:H:N), with **H** and **N** contents of **17.9%** and **13.7%**, respectively, in the **nitrogen-functionalized** film. **Lubricant** simulations place a droplet of **nine D4OH** PFPE strands on **DLC** and **DLC:H:N** substrates and follow **spreading** and **degradation** chemistry relative to **bulk** lubricant reference runs. **Timestep**, **thermostat** and further **temperature/pressure** schedules after film preparation, **production** lengths, **electrostatic** settings, and any **shear** protocol for spreading are **N/A —** not captured in the indexed excerpt; use **`pdf_path`**. **Electric fields** and **enhanced sampling** are **N/A —** not indicated in that excerpt.

**2 — Force-field training.** **N/A —** the study **applies** **ReaxFF** for **C/H/O/F** plus **DLC** chemistry; it is not a new parametrization paper.

**3 — Static QM / DFT.** **N/A —** headline results are **classical reactive MD**.

Cells use **PBC** with **Ar** during melt/quench; post-build **NPT** relaxation adjusts volume and stress before lubricant-on-substrate stages. **Molecular dynamics** after film build continues with **ReaxFF** as in the article; **NVT**/**NPT** staging after relaxation, **timestep** (fs), **equilibration**/**production run** lengths (ps/ns) for droplet **spreading** and degradation, **thermostat** and **barostat**/**pressure** targets, and target **temperature** (K) schedules are **N/A —** not captured in the indexed excerpt—confirm in **`pdf_path`**. **Electric field** driving and **umbrella**/**metadynamics**/**replica-exchange** sampling are **N/A —** not indicated there.

## Findings

**Outcomes.** **D4OH** **spreads faster** on the **nonfunctionalized DLC** surface than on **DLC:H:N** under the reported protocols. **Both** substrates change **PFPE degradation** chemistry compared to **bulk** lubricant-only simulations, so **substrate composition** enters degradation networks alongside **temperature** and any **mechanical** driving treated in the article.

**Mechanistic attribution.** The authors connect faster spreading on **DLC** versus **DLC:H:N** to differences in **surface–lubricant** interaction and **functionalization** (see discussion in **J. Phys. Chem. C**).

Industrial **DLC** microstructures and **deposition** histories are richer than the **melt-quench** training cells; treat reported **sp\(^2\)/sp\(^3\)** and composition as **model targets** aligned with the paper’s narrative, not universal device descriptors.

## Limitations

Sputtered or plasma-deposited industrial DLC films exhibit broader structural disorder and impurity chemistry than melt-quench training cells; extrapolating every degradation channel to device lifetimes requires validation against experiment. ReaxFF captures ground-state reactive events but not electronic excitations or laser heating paths relevant to some recording physics scenarios.

## Relevance to group

Combines **ReaxFF** with **tribology**/**storage** materials problems coauthored by **van Duin**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpcc.6b09729` (`papers/Lotfi_2016_DLC_paper.pdf`).

## Related topics

- [[reaxff-family]]
