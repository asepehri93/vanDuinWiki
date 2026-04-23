---
id: paper:2021mojtabavi-acs-wafer-scale-lateral
type: paper
title: "Wafer-scale lateral self-assembly of mosaic Ti3C2Tx MXene monolayer films"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:water-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.0c06393"
year: 2021
authors:
  - "Mehrnaz Mojtabavi"
  - "Armin VahidMohammadi"
  - "Karthik Ganeshan"
  - "Davoud Hejazi"
  - "Sina Shahbazmohamadi"
  - "Swastik Kar"
  - "Adri C. T. van Duin"
  - "Meni Wanunu"
venue: "ACS Nano 2021, 15, 625–636"
pdf_sha256: "4f066bcea653aab298d46958e3c78c2ce94d2d96490d3acc4b5f61aeff6b0cfb"
pdf_path: "papers/Mojtabavi_Ganesh_ACS_Nano_2021_MXene_monolayers.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021mojtabavi-acs-wafer-scale-lateral -->

## Summary

Mojtabavi *et al.* demonstrate **wafer-scale** self-assembly of **Ti\(_3\)C\(_2\)T\(_x\)** **MXene** monolayers into **mosaic** flake films with high coverage, using a **liquid/liquid interfacial** route that can transfer films to **Si** or glass substrates for device-oriented characterization. The experimental core combines controlled **etching/dispersion** of **MXene** from **Ti\(_3\)AlC\(_2\)** precursors (including **MILD**-type processing as described in **Methods**) with **interfacial trapping** that laterally orders flakes without requiring specialized **Langmuir** barrier hardware in the same way as classic **LB** workflows. **ReaxFF molecular dynamics** supplies an atomistic explanation for why **MXene–solvent interactions** stabilize flakes at an **immiscible** solvent interface, providing **interaction energy** trends that rationalize experimental **yield** and **coverage** sensitivities. **Adri C. T. van Duin** is a coauthor, connecting the study to the group’s **interface** modeling expertise.

## Methods

**Experiments (MXene + wafer-scale films).** **Ti\(_3\)C\(_2\)T\(_x\)** MXene is prepared and suspended using **MILD**-type or related etch/dispersion protocols detailed in *ACS Nano* (MAX precursor **Ti\(_3\)AlC\(_2\)**, etc.). A **liquid–liquid** interfacial self-assembly route (refined from prior work cited in the article) condenses monolayer-rich flakes and enables transfer to **Si** or **glass** substrates. Characterization on **3-inch** (and scale-up) wafers includes **optical**/reflectance images, **AFM** for thickness, **TEM/SEM** morphology, **Raman** and **ellipsometry** mapping, and **sheet resistance** vs number of **layer-by-layer** depositions. The abstract reports **<10% void** area in optimized **monolayer** films by the cited microscopy.

**MD application (ReaxFF molecular dynamics, interface support).** The *ACS Nano* main text and Table S2 describe **ReaxFF molecular dynamics** (the **MD engine**—e.g. **LAMMPS**-class integration as in related **ReaxFF** distributions—is specified in the **Supporting Information**). A **21.56 × 26.67 Å²** **Ti₃C₂**-type **MXene** **slab** is equilibrated in **bulk** **water** under **NVT** at **500 K** to form **–OH** edge terminations, then desolvated. **Ternary** cells (**chloroform / methanol / water, 1:8 by volume**), **43.15 × 46.47 × 16.87 Å³**, place **edge-terminated** **MXene** at the water↔**chloroform** **interface** or in a single phase; a separate **orthorhombic** “edge-free” **MXene** tile (**26.25 × 30.30 Å** in **xy**; **z ≈ 40 Å** per solvent) separates immiscible solvents for energy sampling. For the edge-free configurations: **NPT** equilibration **100 ps** (**P = 1 atm, T = 300 K**, **Berendsen** barostat/thermostat, damping **5000** and **100** fs, respectively) followed by **NVT** **500 ps**; running-average potential energy uses a **~150 ps** window. A longer **NPT (1 atm, 300 K)** run of **1 ns** with the same **Berendsen** controls is used in the discussion of **methanol** diffusion to the **–OH**-terminated **MXene** (Figure S12 / main text at **p. 630**). **3D PBC** in all **cells**. **Shear, shock, electric field, replica, metadynamics — N/A** for the documented benchmarks.

**Static QM. N/A** (no standalone DFT production section; ReaxFF parameter file per SI).

**FF reparameterization. N/A** (existing ReaxFF; SI Table S2).

## Findings

**Outcomes and mechanisms.** Interfacial assembly yields **mosaic** monolayer **Ti\(_3\)C\(_2\)T\(_x\)** films with high coverage and controllable **bilayer**/**trilayer** build-up, with **optical** and **sheet-resistance** metrics consistent with layer count. ReaxFF MD is presented as an **interfacial stabilization** mechanism: the flake–solvent energetics favor **trapping** at the **immiscible** solvent interface, the prerequisite in the paper’s account for **lateral** ordering.

**Comparisons.** The article contrasts this **barrier-free** interface method with more instrument-heavy **Langmuir** approaches and with prior **air–water** versions that can suffer from convection/variable thickness during deposition; numerical comparisons should be read from the primary PDF and figures.

**Limitations of the MD layer.** The reactive MD is **qualitative/energetic** support for interface **trapping** and **reorganization**, not a full **device** transport model; **T\(_x\)** **termination** **heterogeneity** remains a process variable.

## Limitations

**ReaxFF** does not provide **electronic band structures** or **defect** physics at **DFT** accuracy; **MXene** surface terminations (**T\(_x\)**) vary with processing. **Wafer-scale** metrics include **microscopy** void fractions that are not atomistically resolved here.

## Reader notes (navigation)

Pair with **2D** **battery** and **conductive film** pages carefully—**MXene** applications span **energy storage** and **EMI shielding**, but this article’s evidence is **assembly + MD** interface stabilization.

## Relevance to group

Combines **ReaxFF** **interface** modeling with experimental **MXene** assembly (**van Duin** co-author).

## Citations and evidence anchors

- ACS Nano **15**, 625–636 (2021); DOI **10.1021/acsnano.0c06393** — **Materials and Methods** and **Results**.

## Related topics

- [[reaxff-family]]
- [[2d-tmds-mos2-ws2]]

