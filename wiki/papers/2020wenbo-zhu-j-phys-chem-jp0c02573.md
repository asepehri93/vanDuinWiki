---
id: paper:2020wenbo-zhu-j-phys-chem-jp0c02573
type: paper
title: "Development of a Reactive Force Field for Simulations on the Catalytic Conversion of C/H/O Molecules on Cu-Metal and Cu-Oxide Surfaces and Application to Cu/CuO-Based Chemical Looping"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - method:reaxff
  - material:metal-surface
  - task:parameterization
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.0c02573"
year: 2020
authors:
  - "Wenbo Zhu"
  - "Hao Gong"
  - "You Han"
  - "Minhua Zhang"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C 124:12512-12520 (2020)"
pdf_sha256: "3d54d6d748d38086a04d431078447f5f8f50aef3dc77d262844c333c58c83afd"
pdf_path: "papers/Zhu_JPCC_CuCHO_2020.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020wenbo-zhu-j-phys-chem-jp0c02573 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **J. Phys. Chem. C** article identified by `doi`, `title`, and `pdf_path`. Quantitative convergence settings and extended tables appear in the **published PDF** and **Supporting Information**.

## Summary

Zhu *et al.* develop an integrated **Cu/C/H/O Reaxff** for **heterogeneous catalysis** on **Cu** and **Cu oxide** via: **(1)** re-optimizing **Cu** on an **expanded** **cluster** **training** set; **(2)** **merging** with a **C/H/O** field; **(3)** **fitting** **Cu–(C/H/O)** **cross-terms** to **DFT** **binding** and **elementary** **barriers**. They introduce **transition-state** **search** and **path** **tools** on the **Reaxff** **surface**. **LAMMPS** **reactive** **MD** demonstrates **H** transfer and **H₂** / **CHO**-class chemistry on **Cu** and **chemical-looping** **Cu↔CuO** **cases** with **glucose** and **hydrocarbon** **oxidation**. **Adri C. T. van Duin** is a senior author.

## Methods

**1 — MD application.** **LAMMPS** **reactive** **MD** on **Cu(100)**, **(111)**, **(211)** and related **cells** (**Section 3**; **SI** for **supercell** **sizes**). **NVT** with **Berendsen** **thermostat** (**0.1** **ps** **damping** as on **`[[2020wenbo-zhu-j-phys-chem-jp0c02573-2]]`**). **Temperature** **setpoints** include **600 K**, **1000 K**, **1400 K**, **1600 K**, and other **values** in **600–1600 K** depending on **case**; **0.25** **fs** time step where stated; **e.g.** **400** **ps** **gas**-phase **sampling** for **glucose** **+** **Cu** at **1600 K**. **N/A** — **NPT** **production** **stated** in the **short** **summary**—confirm **PDF**; **N/A** — **metadynamics**; **N/A** — **electric** **field**. **PBC** **slab** **models** as in **Figures** **8–14**. **Barostat** **N/A** for **NVT** **bracket** **as** **written** on the **companion** **slug**.

**2 — Force-field training.** **Parent** **Reaxff** **Cu** **subset** + **C/H/O** **library**; **reoptimize** **Cu**; **merge**; **fit** **cross-terms** to **DFT** **data** on **adsorption** and **barriers** (**Section 2**). **QM** **reference** and **training** **targets** as in **Section 3** below. **Optimization** by **Reaxff** **least-squares**-style **updates** in the **Reaxff** **optimizer** **as** **described**; **TS**-aware **sampling** **using** **custom** **Reaxff** **path** **tools**.

**3 — Static QM (DFT reference).** **DMol3**; **GGA** **rPBE**; **ECP**; **unrestricted** **spin**; **4×4×1** **k**-**mesh** **(periodic)**; **0.006** **Ha** **smearing**; **global** **4.5** **Å** **cutoff**; **SCF/geometry** **thresholds** in **Section 2.1**. **Binding** **energies** via the **adsorbate/surface** **partitioning**; **TS** **via** **LST/QST/CG** as **cited**. **N/A** — **hybrid** **functionals** **as** **mainline** in the **excerpt** **curated** **here**.

**4 — Review or non-simulation.** **N/A**

## Findings

**Outcomes and mechanisms.** The **merged** field **reproduces** **DFT** **trends** for **adsorption** and **elementary** **steps** in the **validation** **set**. **MD** **shows** **H** **shuttling** and **H₂** / **CHO**-type **events** on **Cu** **facets** **supporting** **network** **chemistry** at **interfaces**. **CLC** **case** **studies** **differentiate** **fuels** by **detailed** **reaction** **pathways** on **Cu**/**CuO** **as** the **abstract** **claims**.

**Comparisons and sensitivity.** **DFT** **vs** **Reaxff**; **T**-dependent **MD** **cases** (**600–1600** **K** **range** on **illustrative** **systems**).

**Authored limitations and outlook.** **Real** **catalysts** **with** **promoters**, **alloys**, and **coking** are **not** **fully** **captured**; see **## Limitations**.

**Corpus honesty.** **Error** **tables** in **JPCC**/`pdf_path`.

## Limitations

Industrial **catalysts** include **promoters**, **alloys**, and **long-timescale** **coking** not represented in idealized **surface** cells. **ReaxFF** accuracy remains tied to the **training** scope; extrapolation to **new** chemistries requires validation.

## Relevance to group

Extends the group’s **Reaxff** portfolio into **Cu** catalysis and **chemical looping**, combining **parameterization methodology** with **application** trajectories.

## Citations and evidence anchors

- `papers/Zhu_JPCC_CuCHO_2020.pdf`; https://doi.org/10.1021/acs.jpcc.0c02573
- Extract alignment: `normalized/extracts/2020wenbo-zhu-j-phys-chem-jp0c02573_p1-2.txt`

## Related topics

- [[reaxff-family]]
