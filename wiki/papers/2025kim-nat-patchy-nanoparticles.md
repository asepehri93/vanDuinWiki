---
id: paper:2025kim-nat-patchy-nanoparticles
type: paper
title: "Patchy nanoparticles by atomic stencilling"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:methods-software
  - material:metal-surface
  - material:polymer-organic
  - method:classical-md
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
source_refs: []
paper_keywords:
  - keyword:polymer
  - keyword:metallic-systems
  - keyword:dft-static
  - keyword:validation-experiment
doi: "10.1038/s41586-025-09605-8"
year: 2025
authors:
  - "Ahyoung Kim"
  - "Chansong Kim"
  - "Tommy Waltmann"
  - "Thi Vo"
  - "Eun Mi Kim"
  - "Junseok Kim"
  - "Yu-Tsun Shao"
  - "Aaron Michelson"
  - "John R. Crockett"
  - "Falon C. Kalutantirige"
  - "Eric Yang"
  - "Lehan Yao"
  - "Chu-Yun Hwang"
  - "Yugang Zhang"
  - "Yu-Shen Liu"
  - "Hyosung An"
  - "Zirui Gao"
  - "Jiyeon Kim"
  - "Sohini Mandal"
  - "David A. Muller"
  - "Kristen A. Fichthorn"
  - "Sharon C. Glotzer"
  - "Qian Chen"
venue: "Nature 646, 592–601 (2025)"
pdf_sha256: "771a13e8da77318708d05cb2f4ee4244ddb9e1ee37962885c1ede7f29434c8d4"
pdf_path: "papers/Others/Ficthorn_et_al_Nature_2025_stenciling.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025kim-nat-patchy-nanoparticles -->

## Summary

**Patchy colloids**—particles with directional interactions—are prized for **self-assembly**, but synthesizing **anisotropic patches** on **noble-metal** nanoparticles with **high yield** and **facet control** remains difficult. Kim *et al.* introduce **atomic stencilling**: **iodide** forms **facet-selective submonolayers** on **gold** nanoparticles that **mask** selected surface areas, after which **ligand-mediated polymer grafting** deposits **polymer “paint”** only on **exposed** facets. The experimental platform is paired with **electron microscopy**, **DFT** of **iodide** and **2-naphthalenethiol (2-NAT)** **coadsorption**, **molecular dynamics**, and **polymer scaling theory** to interpret how **mask geometry** translates to **patch layout**. **Kristen A. Fichthorn** (Penn State) is a corresponding author; local corpus text for this entry is supplemented by **`normalized/extracts/2025kim-nat-patchy-nanoparticles_p1-2.txt`**.

## Methods

The workflow has three coupled pieces. **Masking** relies on **halide** adsorption differences across **Au** facets; the authors study **co-adsorption** of **iodide** with **2-NAT** where **DFT** shows strong **facet dependence**, rationalizing which regions remain available for subsequent chemistry. **Painting** uses **ligand-mediated grafting** to grow polymers on **unmasked Au**, translating atomic-scale stencil patterns into **mesoscale** polymer domains. The team scans **nanoparticle shape**, **iodide concentration**, **ligand concentration**, and **grafting temperature** as knobs. **Theory** combines **multiscale polymer scaling** arguments with **MD** simulations run **alongside** experiments to predict **patch placement** and **interparticle** valency. **N/A** on this page for **molecular dynamics** **package**, **NVE**/**NVT**/**NPT** label, **time step** (**fs**), **ps**/**ns** **trajectory** length, **PBC** **slab** **atom** counts, **thermostat** details, and **barostat** where not in the **abstract**-level summary (see *Nature* **main text** and **SI**). **N/A** — external **electric** **field** protocol. **N/A** — **replica** **exchange** in the **enhanced sampling** sense (not part of the summary here).
## Findings

The authors report a **library** of more than **twenty** patchy nanoparticle **morphologies**, including **seventeen** motifs produced at **>80% yield** under their surveyed conditions. Beyond simple **facet caps**, they describe **hybrid face–vertex** patterns, **web-like** patches, and **symmetry-broken** arrangements that emerge from stencil geometry—often anticipated by **theory + MD** before observation. When particles are sufficiently **monodisperse**, **patch–patch** interactions drive **millimeter-scale**, **non–close-packed superlattices**, demonstrating that **atomic stencilling** can couple **Ångström-scale** adsorption differences to **device-scale** order. The **Fichthorn** group’s involvement highlights **surface thermodynamics** and **kinetic** modeling connections familiar from **Penn State** **heterogeneous** catalysis and **nanoparticle** growth studies, even though this paper’s emphasis is **synthetic patterning** rather than **reactive** **bond-order** dynamics. **Corpus:** figures and full **sensitivity** sweeps (e.g. **grafting** **temperature**, **iodide** **concentration**) are in the **VOR** **PDF**/**SI**, not excerpted in full on this page.

## Limitations

This work is **not** a **ReaxFF** study; reactive bond-order dynamics are not the primary tool. The short **p1–2** extract omits full **SI** simulation settings; readers should use the **Nature** article and **supplementary information** for complete numerical protocols. **Colloidal** assembly outcomes may additionally depend on **solvent** and **ionic strength** not emphasized in the abstract-level summary here.

## Relevance to group

Penn State **theory / simulation** (Fichthorn) connection for **nanoparticle surface** and **polymer** physics adjacent to **reactive MD** themes.

## Citations and evidence anchors

https://doi.org/10.1038/s41586-025-09605-8 — *Nature* **646**, 592–601 (2025).

## Reader notes (navigation)

- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
