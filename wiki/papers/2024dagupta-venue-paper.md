---
id: paper:2024dagupta-venue-paper
type: paper
title: "Computationally guided synthesis of carbon coated mesoporous silica materials"
updated: "2026-04-22"
confidence: low
canonical_tags:
  - domain:carbon-hydrocarbon
  - material:silicate-glass
  - method:reaxff
  - method:classical-md
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:galley-or-proof-pdf
candidate_tags:
  - "duplicate-of-VOR-carbon-221"
source_refs: []
doi: ""
year: 2024
authors:
  - "Nabankur Dasgupta"
  - "Qian Mao"
  - "Adri C. T. van Duin"
venue: "Carbon (corrected proof PDF in corpus)"
pdf_sha256: "ccece2de0260bcc9b6726c4907fa20bb607da01fc599837643e05faae89ef4de"
pdf_path: "papers/Dagupta_Mao_mesopores_Carbon_2024_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2024dagupta-venue-paper -->

Classical micelle assembly, boosted ReaxFF silica condensation, and high-temperature pyrolysis of several carbon precursors inside pores are combined in a corrected-proof Carbon article on mesoporous silica with in-pore carbon healing.

!!! note "Non-primary article PDF"
    This file is a **corrected proof** PDF for the same study as **`paper:2024dasgupta-carbon-221-2-computationally-guided`** (version-of-record PDF). Use the **VOR** page for **DOI-backed** citation; keep this page for **corpus provenance** of the proof.

## Summary

**Mesoporous silica** synthesis and **pore healing** via **in-pore carbonization** are explored with **non-reactive MD** of **Pluronic L64** self-assembly and **bond-boosted ReaxFF MD** of **silicic acid** condensation, followed by **high-temperature** carbonization of several **precursors** inside pores. The workflow emulates a computationally guided synthesis loop in which soft-matter self-assembly sets mesoscale confinement, reactive silica chemistry locks in pore order, and pyrolytic carbon deposition is compared across feedstocks that differ in oxygen content and aromaticity.

## Methods

### Self-assembly (classical MD)

**Pluronic L64** **micelles** in **water**; **H-bond** partitioning (**hydrophilic** blocks vs **water**).

### Silica condensation (ReaxFF + bond boost)

**ReaxFF** **bond boosting** at **300 K**; **1500 K** **unboosted** runs; **Si(OH)\(_4\)** addition on **micelle** templates.

### Confined carbonization (ReaxFF, high T)

**2200–2600 K** **PE**, **lignite**, **sucrose**, **PET**-like precursors in **silica** pores—**rings**, **H\(_2\)**, **turbostratic** signatures; mirror **thermostat**/**boost**/**ramp** from **`paper:2024dasgupta-carbon-221-2-computationally-guided`**/**VOR** text.

**Observables in high-T trajectories.** The production runs monitor **carbon** **ring** formation, **H\(_2\)** **release** bursts, **sp\(^2\)** content proxies, and whether **tars** **occlude** **pore** openings—metrics reported quantitatively in the **Carbon** article and duplicated here for **proof-PDF** tracking. When citing **exact** **percentages**, prefer the **VOR** page **`[[2024dasgupta-carbon-221-2-computationally-guided]]`** to avoid **proof**/**final** text drift.

**MD application (classical + ReaxFF, multi-temperature).** **LAMMPS** (and classical **MD** for **Pluronic**): **periodic** cells for **self-assembly**; **NVT**/**NPT** as in **main** text; **bond boost**+**ReaxFF** for **300 K** **condensation** and **1500 K** **unboosted** and **2200**–**2600 K** **pyrolysis** segments—**time step** (fs), **ns**-scale (or as stated) **durations**, **Nosé–Hoover** **thermostat**, and **N/A**—**NPT** **Parrinello** **barostat** only if a **pressurized** segment is documented. **N/A**—**external** **E-field**; **bond boost** stands in for **umbrella**-style rare-event **sampling** as an **acceleration** method. **Atom**/**stoichiometry** in **`paper:2024dasgupta-carbon-221-2-computationally-guided`**.

## Findings

**~80%** of **H-bonds** involve **hydrophilic** micelle segments and **water** in the non-reactive model. **>60%** of **silicic acid** additions yield **periodic mesoporous silica** order in the boosted **ReaxFF** runs. **1500 K** **unboosted** condensation **doubles** polymerization rate versus **300 K** **boosted** runs. **Polyethylene** and **high-rank lignite** best form **turbostratic graphene**-like **carbon**; **PE** shows strong **H₂** release and **sp²** content, whereas **sucrose** yields the least **planar** carbon. A **PET**-derived **tar** can **coat** **silica** pores, blocking **silicic acid** ingress in the illustrated **trajectory**. The combined metrics are presented as screening criteria for which carbon precursors heal defects without occluding continued silica condensation.

## Limitations

Prefer **`2024dasgupta-carbon-221-2-computationally-guided`** for **bibliographic** citation; this proof PDF may differ slightly from the **final** **Carbon** layout.

## Relevance to group

**ReaxFF**-driven **silica condensation** and **pyrolytic** **carbon healing** from **Dasgupta/Mao/van Duin** collaboration.

## Citations and evidence anchors

- See **`paper:2024dasgupta-carbon-221-2-computationally-guided`** for **DOI** `10.1016/j.carbon.2024.118891`.

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Proof duplicate of **`[[2024dasgupta-carbon-221-2-computationally-guided]]`**; cite the **VOR** for **DOI**-backed bibliography.
