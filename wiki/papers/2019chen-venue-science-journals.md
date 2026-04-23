---
id: paper:2019chen-venue-science-journals
type: paper
title: "Chemical and physical origins of friction on surfaces with atomic steps"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:water-silica-geo
  - material:graphene-carbon-nano
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:tribology
  - keyword:graphene-carbon
  - keyword:oxide-surface
  - keyword:reactive-md
  - keyword:validation-experiment
source_refs: []
doi: "10.1126/sciadv.aaw0513"
year: 2019
authors:
  - "Zhe Chen"
  - "Arash Khajeh"
  - "Ashlie Martini"
  - "Seong H. Kim"
venue: "Science Advances 5, eaaw0513 (2019)"
pdf_sha256: "42b173d73e7a606f6c95cdb7a307c8c3f723c4a6eb9dc35916023af96538aa29"
pdf_path: "papers/ReaxFF_others/Chen_Martini_Kim_Science_Advances_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019chen-venue-science-journals -->

## Summary

Macroscale **tribology** often separates **adhesion**, **roughness**, and **shearing**, but at **atomic steps** on **graphite** the relevant physics mixes **topography** with **contact chemistry**. Chen, Khajeh, Martini, and Kim report **atomic force microscopy (AFM)** friction loops for a **silica** probe sliding on **graphite** that contains a **single-layer graphene step** (~**0.34 nm** height) under **dry nitrogen**. **Terraces** exhibit **superlubric**-like friction, whereas traversing the **step edge**—especially in **step-up** geometry—raises dissipation by about **two orders of magnitude**. Complementary **ReaxFF** simulations of the **silica/graphite** contact reproduce the qualitative separation between **basal** and **step** sliding and are used to **partition** lateral forces into **mechanical** versus **bond-making/breaking** contributions near the discontinuity. The **Science Advances** framing connects **nanoscale** **superlubricity** on **atomically smooth** **basal** planes to **engineering** contexts where **step edges** are unavoidable—**CVD** **graphene**, **exfoliated** **flakes**, or **wear** **particles** on **graphitic** **substrates**.

## Methods

**AFM experiments (dry N₂).** Friction measurements use **contact-mode AFM** on **tape-exfoliated ZYA-grade HOPG** with naturally occurring **single-layer graphene step edges** (~**0.34 nm** height). Tests use a **Si** probe (vendor/nominal parameters are listed in the article), in a **dry N₂** environment from a **nitrogen generator** with a reported dew point around **−35 °C** (corresponding to roughly **200–300 ppm** water at atmospheric pressure in the article text). **Normal loads** span about **7.3–36.7 nN**, with **contact pressures** estimated around **~1.6–2.8 GPa** (**Hertz**) and **~1.9–2.9 GPa** (**DMT**) as stated. **Sliding speeds** span about **0.25–2 µm/s** at room temperature.

**Reactive MD (ReaxFF + LAMMPS).** **Engine / code:** simulations are run in **LAMMPS** with a **ReaxFF** description cited in the article. **System / geometry:** the model uses an **amorphous silica** tip constructed by **melt–quench** of **cristobalite** (**4000 K** melt, slow quench; **0.02 K/fs** heating/cooling rate as quoted), shaped as a **semicircular disc** tip with reported **radius/thickness/height** (~**2.5 / 1.5 / 1.5 nm**), with **hydroxyl/hydrogen** passivation of undercoordinated surface sites and the **top 0.5 nm** of the tip treated as a **rigid body**. The **graphite** substrate includes an **armchair** **monolayer step** terminated with **alternating –OH/H** on the edge, with **two mobile graphene layers** on each terrace side to reduce cost while retaining step chemistry. **Boundary conditions:** during sliding, the article reports **boundary constraints** on the **graphite** substrate (side edges **fixed** in all directions as stated in **Materials and Methods**), consistent with a finite **sliding cell** setup described around **fig. S2**.

**Ensemble / thermostat / temperature.** **NVT** at **~300 K** using a **Langevin thermostat** on all atoms that are **not fixed or rigid**.

**Protocol stages.** Each simulation includes: (**i**) minimization + equilibration with tip far from substrate; (**ii**) approach at **10 m/s** until the lowest tip atom is **0.2 nm** from the top substrate layer; (**iii**) apply **normal load** on the rigid tip region and **equilibrate 120 ps**; (**iv**) **slide** at **10 m/s** along **X** using a **harmonic spring** (**6 N/m** stiffness). **Loads** explored include **5, 7.5, 10, 12.5, and 15 nN**, mapping to roughly **~2.1–4.8 GPa** contact pressure using the article’s **real atomic contact area** definition. **Substrate boundaries:** side boundaries of graphite are **fixed** during sliding. **Post-processing:** **Fourier filtering** is applied to noisy lateral-force traces; **hydrogen-bond** counting follows the **Guàrdia et al.** logic cited in the article.

**Timestep.** **N/A —** an explicit integration **timestep** was not located in the **main-text Methods** span extracted for this curation pass (confirm in **Science Advances** supplementary text if required for reproduction).

**Barostat / bulk pressure coupling.** **N/A —** the quoted protocol is **NVT** + **loaded/slid** nanoscale contact mechanics rather than bulk **NPT** servocontrol.

**Electric fields / enhanced sampling.** **N/A —** not part of the summarized MD workflow.
## Findings

On **basal** regions the **coefficient of friction** remains near **0.003** for the cited load/adhesion decomposition—consistent with **superlow** friction on **atomically smooth** graphite. **Step-up** sliding yields **μ ≈ 0.1**, approaching **boundary-lubricated** organic friction despite **dry N₂**, highlighting how a **single atomic defect** can dominate dissipation. **Step-down** curves exhibit **hysteresis** and more complex stick–slip structure. The authors argue **classical** **Prandtl–Tomlinson** models with only **geometric** barriers (for example **Ehrlich–Schwoebel**-type step-crossing penalties) are insufficient without the **chemical** interaction channel that **ReaxFF** captures at the step edge. Practically, the paper motivates **reactive** contact models wherever **silica** tips encounter **undercoordinated** **carbon** at **steps**, not only for **graphite** but as a template for **oxide–carbon** interfaces more broadly.
- **Dry** **N₂** conditions isolate **tip–surface** chemistry from **water**-mediated pathways; humid AFM extensions would test **passivation** of **dangling** **bonds**.

**MD–experiment correspondence.** The article reports **qualitative** agreement between **AFM** and **ReaxFF** trends across **basal vs step** kinematics, and uses simulation-derived **shear strain**/**hydrogen-bond** metrics to separate **physical** vs **chemical** contributions near the **step edge** (see the **Science Advances** figures cited in the PDF).

## Limitations

Single tip chemistry and dry N2 environment; generalization to humid or reactive lubricants requires further study. Future work that adds **water** layers at the **silica/graphite** contact would test whether **superlubricity** persists when **hydrogen-bonded** networks can form at the step.

## Relevance to group

Kim/Martini collaborations; same graphite friction theme as related ACS papers in the corpus.

## Reader notes (navigation)

See **`[[2019arash-khajeh-acs-effect-ambient]]`** for adjacent **graphite** **tribology** entries in this knowledge base when building comparative **retrieval** clusters.

## Citations and evidence anchors

https://doi.org/10.1126/sciadv.aaw0513

## Related topics

- [[2019arash-khajeh-acs-effect-ambient]]
- [[reaxff-family]]
