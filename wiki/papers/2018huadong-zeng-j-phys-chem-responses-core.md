---
id: paper:2018huadong-zeng-j-phys-chem-responses-core
type: paper
title: 'Responses of core–shell Al/Al\(_2\)O\(_3\) nanoparticles to heating: ReaxFF molecular dynamics simulations'
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:metal-surface
  - domain:fuel-combustion
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.8b01088"
year: 2018
authors:
  - "HuaDong Zeng"
  - "XinLu Cheng"
  - "ChaoYang Zhang"
  - "ZhiPeng Lu"
venue: "J. Phys. Chem. C"
pdf_sha256: "741c3b04ef5ab41b8d8c20ea85a7c97b7642bb45524ae76dba4d3fa1b3c02b55"
pdf_path: "papers/ReaxFF_others/Zeng_AlO_JPCC_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018huadong-zeng-j-phys-chem-responses-core -->

## Summary

**Reactive MD** with **ReaxFF** in **LAMMPS** follows **core–shell Al / amorphous Al\(_2\)O\(_3\)** **nanoparticles** heated to **2000 K** to probe **oxidation**, **melting**, and **mass ejection** relevant to **Al combustion**. **Aluminum cores ~4 nm** are coated with **amorphous alumina shells** of thickness **δ = 0.6–1.0 nm** (~**2334** **Al** atoms in **fcc** core; **~14.8k** atoms total for **δ = 1 nm**, **~6.6 nm** diameter) with an initial **~0.3 nm** **void** between core and shell. Simulations show **oxygen** **in-diffusion** through the shell, **Al** migration, **alumina** **melting** (**~1153 K** for **1 nm** shell, **higher** for **thicker** shells), and ejection of small **(AlO)\(_n\)** **clusters** (**n ≈ 3–5**) interpreted as **nano-detonation**-like events. **Mean-square displacement** analysis highlights **O** motion as the **early** rate-limiting ingress step. The article also discusses how **electric fields** may couple to **diffusion**-limited steps relevant to **ignition** of **passivated** **Al** powders—connecting **atomistic** transport to **practical** **combustion** contexts beyond **thermal** **heating** alone. **Readers** should treat **cluster** **ejection** **counts** and **melting** **temperatures** as **model-dependent** outcomes that must be cross-checked against the **full** **results** section for **exact** **numerical** **thresholds** and **statistical** **sampling** windows.

## Methods

**Force-field training (ReaxFF Al/O).** The study uses published **ReaxFF** parameters for **Al/O** chemistry from **Shin *et al.*** and **Rahaman *et al.*** with **QEq**-style dynamic charges, as cited in *J. Phys. Chem. C*; **N/A — new parameter fit in this paper** — the work applies an existing parametrization to **core–shell** **nanoparticle** heating.

**MD application (core–shell nanoparticle heating).** Simulations are **ReaxFF molecular dynamics** in **LAMMPS** on **finite**, **nonperiodic** **core–shell** **Al / amorphous Al\(_2\)O\(_3\)** **nanoparticles** (order **10⁴** **atoms** for a **~1 nm** shell: **~2334** **fcc** **Al** core atoms and **~14.8k** atoms total in the abstract’s **δ = 1 nm** example). **Ensemble:** **NVT** with a **Nosé–Hoover** thermostat (**20 fs** damping). **Timestep:** **0.2 fs**. **Thermal protocol:** relaxation near **300 K**, then a **100 K/ps** ramp to **2000 K** with a **100 ps** hold at the peak temperature (staging and any equilibration edits must be confirmed in `pdf_path`). **Barostat:** **N/A — NPT** — isolated **NP** models are heated at **constant volume** in **NVT**. **Pressure:** **N/A — target stress (bar/GPa)** — not imposed beyond thermostat control on the finite cluster. **Electric field:** the article discusses **electric-field–coupled** diffusion as **ignition** context for **passivated** **Al** powders; **N/A — explicit EFIELD-driven MD protocol** in the indexed summary unless the full **PDF** documents biased dynamics separate from the **thermal** ramp. **Shear / shock:** **N/A**. **Replica / enhanced sampling:** **N/A — umbrella sampling, metadynamics, or replica exchange** for these trajectories.

**Analysis.** **Mean-square displacement** and related diagnostics compare **O** versus **Al** transport; **melting** and **cluster ejection** thresholds are tracked versus **oxide** shell thickness **δ**.

**Experiments.** **N/A — wet-lab experiments** — the publication is **computational**; experimental comparisons appear as **literature** context for **Al** combustion and **passivation**.

## Findings

**Outcomes and mechanisms.** Inward **O** diffusion is the early rate-limiting ingress step relative to **Al** mixing; mean-square displacement analysis supports **O** motion ahead of extensive core reaction. **(AlO)\(_n\)** clusters (**n ≈ 3–5**) eject at later stages, interpreted in the article as **nano-detonation**-like events. **Alumina** **melting** is reported near **1153 K** for a **1 nm** shell, with **higher** apparent melting temperatures for **thicker** **δ**. A **void** opens when the shell melts, discussed alongside **experimental** evidence cited in the article.

**Comparisons and sensitivity.** **Interface** diffusivities during the ramp depend **weakly** on shell thickness **δ**, whereas post-heating diffusivities **decrease** as **δ** increases. Trends are framed relative to prior **diffusion-limited** versus **melt-dispersion** ignition pictures in the **literature** reviewed in the paper.

**Limitations and corpus honesty.** **ReaxFF** training scope for **Al/O** and rapid **100 K/ps** heating may omit slower **quasi-equilibrium** pathways. Quantitative reuse should follow cluster definitions and sampling windows in the **peer-reviewed PDF** (`pdf_path`); the local extract `normalized/extracts/2018huadong-zeng-j-phys-chem-responses-core_p1-2.txt` aligns with the abstract but is not a substitute for **Results** tables.
## Limitations

**ReaxFF** training scope for **Al/O**; **rapid** heating may skip **quasi-equilibrium** pathways; **nonperiodic** **NP** models omit **bulk** **oxidation** **environments**. **Cluster ejection** diagnostics depend on **visual** **thresholds** for **(AlO)\(_n\)** **fragments**—confirm **cluster** **definitions** in the **article** before **quantitative** reuse.

## Relevance to group

**Al combustion** / **core–shell oxidation** **ReaxFF** application adjacent to **energetic** **Al** literature and **nano-aluminum** ignition studies. The **nonperiodic** **nanoparticle** setup mirrors other **finite-cluster** **oxidation** simulations in the corpus where **surface-to-volume** ratios dominate **burn** phenomenology.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpcc.8b01088` — `papers/ReaxFF_others/Zeng_AlO_JPCC_2018.pdf`; extract `normalized/extracts/2018huadong-zeng-j-phys-chem-responses-core_p1-2.txt`.

## Related topics

- [[reaxff-family]]
