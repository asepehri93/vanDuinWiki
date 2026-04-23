---
id: paper:2020mojtabavi-x-wafer-scale-lateral
type: paper
title: "Wafer-scale lateral self-assembly of mosaic Ti₃C₂Tₓ MXene monolayer films"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:2d-materials
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.0c06393"
year: 2020
authors:
  - "Mehrnaz Mojtabavi"
  - "Armin VahidMohammadi"
  - "Karthik Ganeshan"
  - "Davoud Hejazi"
  - "Sina Shahbazmohamadi"
  - "Swastik Kar"
  - "Adri C. T. van Duin"
  - "Meni Wanunu"
venue: "ACS Nano"
pdf_sha256: "376b52bef453167f8f59812ac250ceb5097c1f41a33a648aa4bc44ddb606accd"
pdf_path: "papers/Mojtabavi_Ganeshan_ACS_Nano_2021_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020mojtabavi-x-wafer-scale-lateral -->

Experimental wafer-scale assembly of **Ti₃C₂Tₓ** MXene monolayers at a **liquid–liquid** interface is combined with **ReaxFF MD** (AMS/SCM) to rationalize flake–solvent interactions and interfacial stability.

## Summary

A lateral self-assembly route deposits mosaic monolayer MXene films from immiscible solvents, with transfer to **Si** or **glass** yielding large-area films characterized by TEM/SEM/AFM, Raman mapping, ellipsometry, and sheet resistance. ReaxFF simulations probe MXene–solvent configurations relevant to interfacial trapping and energy trends that support assembly.

The abstract frames bottom-up assembly as requiring control of surroundings so interfacial energetics drive ordering, and states that ReaxFF MD clarifies flake–solvent interactions and stability at the immiscible liquid interface as a prerequisite for interfacial self-assembly. Multiscale characterization ties mosaic texture to uniform thickness, homogeneous optical response, and centimeter-scale electrical conductivity for transferred films.

Readers should verify numerical values, units, and section references against the peer-reviewed PDF and any Supporting Information, especially when extracts or galley PDFs truncate tables.

## Methods

- **Experiments:** MXene processing, liquid–liquid assembly, substrate transfer, and multiscale structural/optical/electrical characterization (see article and Supporting Information).
- **ReaxFF molecular dynamics (AMS suite, SCM):** Ti₃C₂ MXene–**chloroform/methanol/water** chemistry modeled by extending the cited Ti₃C₂ MXene ReaxFF with **Cl/C/H/O** parameters and adjusted **Ti/O/H** terms for surface defects and (de)protonation kinetics (full parameter notes in **SI Table S2** per the paper).
- **Setup:** Edge-terminated MXene slab equilibrated in bulk water at **500 K** (NVT) to populate −OH terminations; adsorbed water stripped; solvents initialized in periodic cells (~**43 × 46 × 17 Å³**) with MXene placed at the water–chloroform interface or within a solvent.
- **Dynamics:** **NPT** at **P = 1 atm**, **T = 300 K** for **1 ns** (Berendsen barostat and thermostat with **5000 fs** and **100 fs** damping as stated); additional **NPT 100 ps** equilibration then **NVT 500 ps** production for energy statistics on orthogonalized edge-free slabs (**26 × 30 Å²** in-plane, **40 Å** solvent slabs along **z**). Potential-energy running averages use a **150 ps** window. **Integration time step (fs),** full **E-field**-**driven** **(MV/cm)** **dynamics,** and **QEq** **update** **(ReaxFF)**: not fully transcribed on this page—**N/A** **details**; **load** the **VOR** **+** **SI** **(including** **SI** **Table** **S2** for **parameters**). **2 —** **de** **novo** **ReaxFF** **fit** **paper:** **N/A** **(extends** **prior** **param** **set**). **3 —** **static** **DFT**-**only** **headline:** **N/A**. **Shear,** **shock,** **umbrella,** **replica,** **metadynamics,** **hyperdynamics,** **CVHD,** **rare**-**event** **(unless** **the** **PDF** **names** **one**)**:** **N/A** **(not** **in** the **excerpted** **bullets** here). **E-field** in **ReaxFF** ( **static** / **AC** ) **(MD**): **N/A** **(not** **part** of **this** **short** **list**; **the** **ACS** **Nano** **VOR** **+** **SI** **gives** any **E**-**field**-**in**-**FF** **notes** if **applicable**)**.**

## Findings

- Wafer-scale films show high monolayer coverage, mosaic texture, and **cm-scale** conductivity relevant to device concepts.
- Simulations support that solvent–MXene interactions stabilize flakes at the **immiscible liquid interface**, consistent with the assembly mechanism.
- Bilayer/trilayer stacking from successive depositions is reported with correlated optical transmission and sheet resistance trends.

**Corpus honesty:** `pdf_path` uses a **galley**-**dated** **filename**; for **definitive** **figures,** **Ω,** and **n**-**m**-**scale** **metrics,** use the **version-of-record** **ACS** **Nano** file **(and** **SI,** e.g. **S2** for **ReaxFF** **notes**)**.**

## Limitations

Galley-dated PDF filename; ReaxFF parameter extensions for chlorinated solvents are specialized—transferability to other MXene chemistries or edge states requires separate validation.

## Relevance to group

van Duin co-authorship; ReaxFF parameterization and MD performed with **FIRST EFRC** acknowledgment in the article.

## Reader notes (navigation)

- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
