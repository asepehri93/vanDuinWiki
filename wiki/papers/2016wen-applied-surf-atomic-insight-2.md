---
id: paper:2016wen-applied-surf-atomic-insight-2
type: paper
title: "Atomic insight into tribochemical wear mechanism of silicon at the Si/SiO2 interface in aqueous environment: Molecular dynamics simulations using ReaxFF reactive force field"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - domain:water-silica-geo
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.apsusc.2016.08.082"
year: 2016
authors:
  - "Jialin Wen"
  - "Tianbao Ma"
  - "Weiwei Zhang"
  - "George Psofogiannakis"
  - "Adri C. T. van Duin"
  - "Lei Chen"
  - "Linmao Qian"
  - "Yuanzhong Hu"
  - "Xinchun Lu"
venue: "Applied Surface Science (2016) 390, 216–223"
pdf_sha256: "53e9ccead3abec2a8148296eda7f6f61325dca8c947d0e20f6540403c9550dd6"
pdf_path: "papers/Wen_App_Surf_Sci_2016.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:water-interfaces
  - keyword:oxide-surface
  - keyword:lammps
---
<!-- id:paper:2016wen-applied-surf-atomic-insight-2 -->

## Summary

**ReaxFF MD** of **tribochemical wear** at a **Si / amorphous SiO\(_2\)** contact in **water**, motivated by **MEMS** aqueous environments and **Si CMP**. The simulations identify **two Si removal pathways**: (i) rupture of stressed **Si–O–Si** bridges on the **Si** side assisted by **H** attachment to **bridging oxygens**, and (ii) breaking **Si–Si** bonds in **Si–Si–O–Si** chains at the interface. **Higher normal pressure** on the **silica** counter-body increases **interfacial Si–O–Si bridge** formation and can increase **Si removal**. **Water** both **oxidizes** Si and, via steric/solvation effects, can **limit** intimate contact.

## Methods

This slug is a **duplicate PDF** (`papers/Wen_App_Surf_Sci_2016.pdf`) for the same **Applied Surface Science** article as **`[[2016wen-applied-surf-atomic-insight]]`** (**DOI** `10.1016/j.apsusc.2016.08.082`). **Methods** match that page: **LAMMPS** **ReaxFF**, **4.26 × 4.26 × 8.0 nm\(^3\)** **PBC** in-plane **slab-on-slab** stack with **300 H\(_2\)O**, **ensemble:** **NVT**; **thermostat:** **Nose–Hoover** at **300 K**; **timestep:** **0.25 fs**; **250 ps** compression equilibration; **1 ns** shear at **10 m/s** (**0.1 Å/ps**); and **2.0 / 4.0 / 6.0 GPa** normal-load series as reported in §2 of the **issue PDF**.

**2 — Force-field training.** **N/A —** merged published **ReaxFF** libraries (**Si/Ge/H** + **water**) with validation in **SI**.

**3 — Static QM.** **N/A —** not used for the wear trajectories.

**4 — Replica / enhanced sampling.** **N/A —** not used.

## Findings

**Outcomes / mechanisms.** The **VOR** page documents **two** **Si** removal channels: **stress-biased Si–O–Si** rupture on the **Si** side with **H** assistance, and **Si–Si** failure within **Si–Si–O–Si** chains tied to **interfacial bridges** (**§3–4** of *Appl. Surf. Sci.* **390**).

**Comparisons.** Removal counts vs **applied normal stress** show **no Si** loss at **2.0 GPa**, **7 Si** at **4.0 GPa**, and **14 Si** at **6.0 GPa** under the **0.3 bond-order** molecular recognition criterion quoted in **`[[2016wen-applied-surf-atomic-insight]]`**.

**Sensitivity / levers.** **Pressure** tunes **bridge-bond** counts and **friction** traces (**Figure 8**), while **interfacial water** simultaneously **oxidizes** Si and can **separate surfaces**, giving the **dual-role** interpretation in **§4**.

**Limitations / outlook.** Same **MD vs AFM velocity** caveats as the **primary** slug; duplicate PDFs should not be treated as independent experiments.

**Corpus honesty.** Prefer **`[[2016wen-applied-surf-atomic-insight]]`** for long-form prose; this page records **alternate SHA-256** provenance for the same **DOI**.
## Limitations

- Simulation scales and speeds may not capture all **real CMP** slurry chemistry (particles, additives) beyond **Si/SiO\(_2\)/water** motifs.
- Wear rates require careful mapping from **atomistic** events to **continuum** removal rates.
- **MEMS** **contacts** can involve **mixed** **oxides**, **organic** **contaminants**, and **electrochemical** **potentials** absent from the **dry/wet** **mechanical** models summarized here.
- **Load** **cycles** and **frequency** in **experiment** can induce **fatigue** and **third-body** **particle** formation not captured in **single-pass** **MD** **shear** protocols.
- **Slurry** **pH** and **ionic** **strength** in **CMP** can alter **oxide** **termination** beyond the **pure-water** **motifs** emphasized in the abstract-level summary.
- **Applied Surface Science** **Simulation** sections list **system** **sizes** and **timesteps** needed to reproduce **reported** **wear** **pathways**.

## Relevance to group

**van Duin-group** coauthored **ReaxFF** tribochemistry paper bridging **silicon MEMS/CMP** applications with **reactive silica–water** chemistry.

## Citations and evidence anchors

- DOI: [10.1016/j.apsusc.2016.08.082](https://doi.org/10.1016/j.apsusc.2016.08.082)
- Text-aligned pointers: `normalized/extracts/2016wen-applied-surf-atomic-insight-2_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
