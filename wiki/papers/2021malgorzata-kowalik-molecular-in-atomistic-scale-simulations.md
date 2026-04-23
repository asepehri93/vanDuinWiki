---
id: paper:2021malgorzata-kowalik-molecular-in-atomistic-scale-simulations
type: paper
title: "Atomistic-scale simulations on graphene bending near a copper surface"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:2d-layered
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:graphene-carbon
  - keyword:batteries-interfaces
  - keyword:reaxff-application
  - keyword:npt-simulation
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.3390/catal11020208"
year: 2021
authors:
  - "Malgorzata Kowalik"
  - "Md Jamil Hossain"
  - "Aditya Lele"
  - "Wenbo Zhu"
  - "Riju Banerjee"
  - "Tomotaroh Granzier-Nakajima"
  - "Mauricio Terrones"
  - "Eric W. Hudson"
  - "Adri C. T. van Duin"
venue: "Catalysts 2021, 11(2), 208"
pdf_sha256: "95662d8a20d72d036b306ddda25526d98417dfbd9252fb92b2d9e6788f3b4543"
pdf_path: "papers/Kowalik_Catalysts_2021_Graphene_Cu.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021malgorzata-kowalik-molecular-in-atomistic-scale-simulations -->

## Summary

ReaxFF reactive MD is used to study graphene bending in vacuum and on Cu surfaces, comparing **two** published ReaxFF parameter sets for graphene/Cu (including the **Zhu 2020** set with **Srinivasan 2015** carbon parameters cited in the paper). The authors report bending stiffness, binding of H and Cu adatoms, and the **draping angle** of graphene over Cu step edges; simulated draping angles agree with scanning-tunneling-microscopy-based experiments, supporting the newer parameterization for collector–anode interface modeling. The motivation is **battery-relevant**: **current collectors** and **anodes** often place **graphene** or **carbon** coatings next to **Cu**, where **mechanical draping** and **adatom** binding influence **interfacial** stability during **cycling**.

## Methods

**MD application (ReaxFF, ADF).** The Catalysts article (Section 2) reports all main **ReaxFF** trajectories in **ADF** (not LAMMPS): **velocity Verlet** integration, **time step 0.1 fs**, and **3D periodic boundary conditions**. **Thermostat / barostat:** **Berendsen** thermostat with a **100 fs** coupling constant in **NVT**; in **NPT** the **Berendsen barostat** keeps the system at **zero pressure** with a **100 ps** pressure coupling constant.

**System size, protocol, and ensembles (from the same section).** *Free-standing graphene:* **~8.3 × 5.8 nm** with **~2000 C atoms**—energy minimization, **NPT at 5 K** to show thermal rippling, then **NPT** annealing from **1500 K** to **77 K** at **1.2 K/ps** and a **100 ps** hold at **77 K** (Section 2.1). *Long ribbons:* **20, 40, and 80 nm** lengths, **NPT** relaxation at **300 K**, heating to **1300 K** or **2000 K** at **10 K/ps** with a **100 ps** plateau, then **NVT at 77 K** (Section 2.2). *Graphene on Cu (Zhu 2020 / Srinivasan 2015 C):* rippled free-standing structure placed on a **Cu** surface; annealing compared before/after in Figure 3 (Section 2.3). *Step edges (draping angle):* a **40 nm** ribbon on **Cu** with **6**- vs **12-**layer-high steps; **NVT at 300 K** for up to **500 ps** to establish one- or two-sided contact with the terraces; angles extracted from the last 10 structures with **ImageJ** and compared to **STM** linecuts (Sections 2.4–2.5).

**ReaxFF parameter lines compared** include **CHON-2019** (Srinivasan *et al.* 2015 C parameters in the **CHO-2016 / CHON-2019** lineage) versus legacy **CHO-2008** (Chenoweth *et al.*) for mechanical and hydrogenation tests, and the **Zhu 2020** **Cu–C** field with Srinivasan **C** for **Cu** interfaces.

**Blueprint line items. Boundaries / periodicity:** 3D **PBC** in all cases as stated. **Ensemble:** **NPT** for isotropic or zero-pressure relaxations/anneals; **NVT** for confined 77 K stages and 300 K step–edge production. **Timestep 0.1 fs**; **durations** as in the subsections above. **Temperature:** 5, 77, 300, 1300, 1500, and 2000 K in the different protocols. **Barostat** — only in **NPT** steps (**0** target pressure in those segments). **NVT** step-edge runs: **N/A** separate barostat. **Pressure — N/A** as an **independent** control in **NVT** step-edge segments. **Electric field — N/A.** **Shock / shear / replica / metadynamics — N/A.** **Electrostatics / ReaxFF QEq** — default ReaxFF/ADF treatment; *standard* ReaxFF charge training limits are discussed vs **eReaxFF** in the Introduction, not a separate numerical Ewald block.

**Force-field training — N/A** (uses published parameter sets; no *de novo* fit in this work).

**Static QM / DFT — N/A** for production MD; DFT from **Yi *et al.*** is comparison literature for hydrogenation (Section 2.5), not a separate pipeline here.

## Findings

**Outcomes and mechanisms.** **CHON-2019** reproduces the reference **potential energy per atom** for annealed ribbons better than **CHO-2008** (Section 2.2). Placing rippled graphene on **Cu** with the **Zhu 2020** set alters the annealed conformation relative to the free sheet because of strong **Cu–C** contact at bend regions (Figure 3). **Draping angles** from the **40 nm** step-edge systems are about **28° ± 4°** (6 Cu layers) and **30° ± 5°** (12 layers); **STM** linecuts on CVD **graphene** on **Cu** give **32° ± 3°**—taken in the paper as support for the ReaxFF **Cu–C** interface (Section 2.4–2.5). **Hydrogenation and Cu-atom binding (Section 2.5, Tables 1–3):** **CHON-2019** aligns better with **DFT (Yi *et al.*) for one-sided** hydrogenation and with **4Hc**/**4Hb** ordering; **CHO-2008** is weaker on those distinctions.

**Comparisons vs experiment / reference QM.** ReaxFF vs **DFT** tables for H chemisorption; **Zhu 2020**+ReaxFF draping vs **STM** for step angles.

**Sensitivity and levers.** **Ribbon length** and **heating path** (1300 vs 2000 K) change ripple multiplicity; **step height** switches one- vs two-sided **draping** within the 500 ps **NVT@300 K** window; parameter set (**CHON-2019** vs **CHO-2008**) shifts mechanical and H-binding metrics.

**Limitations (as stated).** The authors flag that **ReaxFF** is not trained for high-fidelity **charge** distributions and point to **eReaxFF** as a way to add explicit electronic response (Introduction).

## Limitations

Reactive MD captures mechanics and binding trends but not quantitative electronic structure or charge transport across the interface. **Step-edge** **geometries** in experiment include **substrate** **miscut** and **oxide** **contamination** that are simplified in **ideal** **Cu** **terraces**; **draping** comparisons should therefore emphasize **trends** and **relative** **parameter-set** performance rather than **sub-Å** **absolute** agreement without **surface** **reconstruction** studies. **Hydrogen** **adatom** **tests** probe **local** **binding**; **electrochemical** **environments** may introduce **additional** **adlayers** not represented in **vacuum** **benchmarks**.

## Relevance to group

Direct van Duin-group application of ReaxFF to **battery-relevant** graphene–Cu interfaces.

## Citations and evidence anchors

- Catalysts **11**(2), 208 (2021); DOI 10.3390/catal11020208 — Section 2 (simulation techniques) and results for bending/draping.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
