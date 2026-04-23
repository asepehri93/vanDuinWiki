---
id: paper:2017berdiyorov-applied-surf-effect-surface
type: paper
title: "Effect of surface termination on ion intercalation selectivity of bilayer Ti₃C₂T₂ (T = F, O and OH) MXene"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:dft-static
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1016/j.apsusc.2017.04.195"
year: 2017
authors:
  - "Golibjon R. Berdiyorov"
  - "Khaled A. Mahmoud"
venue: "Appl. Surf. Sci."
pdf_sha256: "ea0be1345c0ee47ce734e91a228abacf51b576906942b5e073f279397639809f"
pdf_path: "papers/ReaxFF_others/Berdiyorov_MXene_AppSuSci_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017berdiyorov-applied-surf-effect-surface -->

## Summary

MXene electrodes and membranes exploit interlayer galleries that can swell or contract when ions and solvents intercalate, so predicting how surface chemistry steers interlayer spacing is central to selectivity and transport modeling. Berdiyorov and Mahmoud study bilayer Ti₃C₂T₂ with T = F, O, or OH using density functional theory for intercalation energetics and ReaxFF molecular dynamics to capture finite-temperature interlayer distance response. They compare pristine bilayers to functionalized bilayers when anions and cations are inserted, focusing on how termination reverses qualitative trends in gallery expansion versus contraction. The abstract frames the problem as intercalation selectivity: functionalization changes whether gallery opening tracks anions similarly to cations, which matters when designing MXene stacks for ion sieving or pseudocapacitive charge storage.

## Methods

**Static QM (DFT).** **PBE** **GGA** exchange–correlation with **Grimme D2**-type **dispersion** on **PBE**; calculations use **Atomistix ToolKit** with an **8×8×8** **k**-mesh, **150 Ry** real-space mesh cutoff, **DZP** numerical orbitals, and convergence thresholds **10⁻⁴ eV** (energy) and **0.01 eV/Å** (forces). **Supercells** are bilayer **Ti₃C₂T₂** with **T = none, F, O, OH**, **>10 Å** vacuum along the layer normal, and relaxed in-plane dimensions on the order of **a ≈ 3.145 Å**, **b ≈ 5.457 Å**, **c ≈ 20 Å** (reported relaxed values). **In-plane PBC** apply; the stack is isolated from its periodic image by vacuum in the normal direction. **Intercalants** include **Cl⁻**, **Na⁺**, **K⁺**, **Li⁺**, **Mg²⁺**, **Ca²⁺**, **Al³⁺**, and **As⁵⁺**, with high formal charges treated via the article’s **compensation-charge** scheme.

**DFT-based MD** runs use the **NVT** ensemble, **Δt = 0.5 fs**, and a **Nosé–Hoover chain** thermostat (*Appl. Surf. Sci.* §2). **Barostat / stress control** for those **DFT-MD** segments is **not emphasized** on the pages indexed for this note (canonical **NVT** thermal sampling of **d(t)** at fixed cell).

**MD application (ReaxFF).** **ReaxFF** employs a **Ti₃C₂(OH)₂ / water / K⁺**-oriented parameterization from prior work (cited in the article). The **minimal bilayer gallery** places **one ion** and **one water** between layers (Fig. 1 schematic in the paper). The abstract reports that **finite-temperature** **ReaxFF MD** reproduces the **qualitative sign change** in **interlayer spacing** vs intercalant type seen in **DFT-MD** after **surface functionalization**. **ReaxFF** run settings (**code**, **timestep**, **target T**, **duration**, **barostat**, **E-field**, **enhanced sampling**) appear in *Appl. Surf. Sci.* **§2–3** and are **not transcribed** on this wiki page.

**Force-field training** is **N/A**: an **existing** **ReaxFF** set is **applied**, not refitted here.

**MD blueprint honesty.** **DFT-MD** details above include **NVT**, **timestep**, and **Nosé–Hoover** thermostat language from the indexed *Appl. Surf. Sci.* text. **ReaxFF MD** trajectories are expected to use **PBC** bilayer cells analogous to the **DFT** setup; **LAMMPS** (or the code named in the paper) should be confirmed in **§2–3**. **Production duration** (**ps**/**ns**), any **NPT**/**barostat** segment for **ReaxFF**, **target pressure**, and **electric-field**/**enhanced-sampling** knobs are **N/A** on this page unless copied from the **PDF**.

## Findings

**Outcomes and mechanism readout (authors’ framing).** For **pristine** bilayer **Ti₃C₂**, the **minimum-energy interlayer spacing** trends toward **larger** **d** when either **anions** or **cations** are intercalated (together with a **water** molecule in the gallery model of Fig. 1). After **surface functionalization** (**F**, **O**, **OH** terminations), the **response reverses qualitatively**: **d** **increases** with **anion** insertion but **contracts** under **cation** insertion, with **stronger contraction** as the **cation charge state** increases—most pronounced for **Ti₃C₂O₂** in the abstract’s summary.

**Comparisons.** The study contrasts **pristine** vs **functionalized** bilayers across the **same ion set**, and reports that the **sign change** in **d** vs intercalant type is **reproduced in both DFT-based MD and ReaxFF MD** (abstract), i.e. **finite-temperature** modeling agrees with the **static** **DFT** **E(d)** picture on this qualitative point.

**Sensitivity and design levers.** **Termination chemistry** (**T**) and **ion formal charge** are the dominant knobs in the reported trends; **injecting extra electrons** to the layers is also discussed in the article as amplifying contraction effects (see *Appl. Surf. Sci.* discussion).

**Limitations and outlook (as implied by scope).** The bilayer **+ single ion + one water** construct is intentionally minimal; **multilayer stacks**, **concentrated electrolytes**, and **long-time ion transport** are outside what the abstract claims. **Force-field** transferability for **highly charged** intercalants should be checked against experiment when used for **engineering** estimates.

Quantitative **E(d)** curves, **d_min** tables, and time series **d(t)** are in the **peer-reviewed PDF** and figures.

## Limitations

Solvent-explicit electrochemical environments and long-time diffusion statistics require larger models and may expose force-field limitations outside the fitted ion–surface chemistry.

## Relevance to group

Pairs DFT with ReaxFF for MXene ion intercalation—useful cross-reference for 2D electrochemical materials modeling.

## Citations and evidence anchors

- DOI: `10.1016/j.apsusc.2017.04.195`.

## Related topics

- [[reaxff-family]]
