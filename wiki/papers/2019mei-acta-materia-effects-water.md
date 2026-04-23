---
id: paper:2019mei-acta-materia-effects-water
type: paper
title: "Effects of water on the mechanical properties of silica glass using molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:mechanics-tribology
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:silicate-glass
  - scale:atomistic
paper_keywords:
  - keyword:lammps
  - keyword:water-interfaces
  - keyword:silica-silicate
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1016/j.actamat.2019.07.049"
year: 2019
authors:
  - "Hai Mei"
  - "Yongjian Yang"
  - "Adri C. T. van Duin"
  - "Susan B. Sinnott"
  - "John C. Mauro"
  - "Lisheng Liu"
  - "Zhengyi Fu"
venue: "Acta Materialia"
pdf_sha256: "16302b2280d36b2729c884a8d3ce0d60d87bd76f03d075478de722b9e68de006"
pdf_path: "papers/Mei_ActaMat_SiO2_MechanicalProperties_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019mei-acta-materia-effects-water -->

## Summary

Silicate glasses can contain **water** either as **molecular H₂O** trapped in the network or as **hydroxyls** formed by **hydrolysis** of **Si–O–Si** bridges; experiments show both species alter **mechanical** response, but isolating their roles is challenging when both are present. Mei *et al.* use **ReaxFF molecular dynamics** in **LAMMPS** with the **Yeon** *et al.* **Si/O/H** parameterization—developed for **load-driven silica hydrolysis**—to prepare **bulk silica glass** samples with controlled **in-network** **molecular water** versus **hydroxyl** content, then subject them to **mechanical** tests that resolve **elastic moduli**, **strength**, **fracture toughness**, and **network** metrics (**Si–O** distances, **Si–O–Si** angles). The **Acta Materialia** study is explicitly about **decoupling** **speciation**: **molecular** **water** can **plasticize** without fully **depolymerizing** the network, whereas **hydroxyls** **cut** **bridging** **bonds** and reduce **connectivity** more directly.

## Methods

**1 — MD application (atomistic dynamics).** **Molecular dynamics** is run in **LAMMPS** with the **Yeon** *et al.* **ReaxFF** **Si/O/H** parameterization developed for **load-driven** **silica** **hydrolysis**; **structures** are visualized in **OVITO** (per **§2** of *Acta Materialia*). **System / composition:** the **compact-tension** **(CT)** **silica** **block** in **Fig.** **1a** has **in-plane** **extents** **~22** **nm** and **~2.3** **nm** **thickness** after **replication**, with **O(10⁴)–O(10⁵)** **Si/O** **atoms** depending on **defect**/**crack** **content** and **replication** factors detailed in the **Acta** **article**. **Pure** **silica** **glass** is **prepared** and **densified** with a **0.5 fs** integration **timestep**; **subsequent** **mechanical** and **reactive** **segments** use **0.25 fs** as stated in the **Simulation** **details** section. **Thermostat** **(NVT):** the **paper** **uses** **NVT** **integration** for **the** **quoted** **anneal** and **deformation** **stages**; the **family** and **damping** **(Berendsen**-**style** or **Nosé–Hoover**)** **are** **given** **in** the **VOR** **PDF** **(see** **§2**; **not** **repeated** here **in** full). After **controlled** **introduction** of **molecular** **H₂O** vs **hydroxyl** **speciation** in the **network**, samples are **relaxed** at **600 K** in **NVT** for **1 ns** (see the **600** **K** **NVT** **anneal** and **glass** **density** **~2.07 g cm⁻³** in the paper). **Mechanical** **testing** includes **compact** **tension** (CT) and **uniaxial**-**tension**-derived **quantities** (e.g. **Young’s** **modulus** from **~1%** **true** **strain** **linear** **fits**; **critical** **tensile** **stresses** at a **10⁹ s⁻¹** **strain** **rate** in the **CT** **geometry** as tabulated in the article). **PBC** and **plane** **strain** / **loading** **directions** follow the **sketches** in **Figs. 1–3**; see the **PDF** for **sample** **dimensions** and **water** **content** **labels** (**samples** **1–3** and **variants** in **Tables**). **NVT**-centric **aging** and **NVT** **mechanical** **pulls** are used for the **quoted** **β**-**relaxed** / **deformed** **states**; any **NPT** **holds** (if present for **preparation**) should be read from the **full** **Methods** in the **PDF**—**barostat**-led **mean** **pressure** **targets** are **not** the **focus** of the **abstract**-level **summary** here. **Static** **external** **electric** **field:** **N/A**. **Replica** / **metadynamics:** **N/A**.

**2 — Force-field training:** **N/A** in this paper’s **core**—the authors **adopt** the **published** **Yeon** **ReaxFF** **fit** to **Si/O/H** **load**-**dependent** **chemistry** rather than **re-optimizing** **parameters** *de novo*.

**3 — Static QM / DFT:** **N/A** as a **first-principles** **mechanical** **protocol**; **ReaxFF** is the **active** **potential** in the **reported** **trajectories**.
## Findings

**Molecular water** can **increase Young’s modulus** at **low** water content, whereas **hydroxyls** **decrease** modulus under the surveyed compositions. **Hydroxyls** reduce **strength** and **fracture toughness** by **breaking network connectivity**; **molecular water** weakens the glass by driving the **silica network** toward **strained** configurations **before** external stress is applied. In **tension**, **stress–strain plateaus** in **molecular-water**-containing samples coincide with **Si–O** bond rupture followed by **silanol** formation, and **molecular water** lowers the **critical stress** where the plateau begins relative to drier baselines in the model. The authors relate these trends to **microstructural** indicators—**Si–O** bond lengths and **Si–O–Si** angles—so that mechanical softening is tied to **measurable** network distortions rather than to a black-box “water effect.”

Readers building **retrieval** clusters should pair this page with **fracture**-focused **silica** entries (for example **Rimsza** *JGR* subcritical fracture) when questions span **bulk** modulus versus **crack**-tip chemistry.

## Limitations

System sizes and strain rates follow MD constraints; quantitative agreement with macroscopic fracture tests requires upscaling. Operators curating **brittle fracture** benchmarks should pair this entry with **continuum** **corrosion** models when translating to **component** lifetimes. **Water** contents explored in the article should be interpreted relative to the **glass** synthesis pathway assumed in the simulations, not as universal **service** environments.

## Relevance to group

Demonstrates ReaxFF-based mechanical testing of hydrated silica with van Duin-parameter lineage tied to prior silica–water reactivity work.

## Citations and evidence anchors

- DOI: [10.1016/j.actamat.2019.07.049](https://doi.org/10.1016/j.actamat.2019.07.049)

## Related topics

- [[reaxff-family]]
