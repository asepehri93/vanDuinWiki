---
id: paper:2019kowalik-venue-bez-tytu
type: paper
title: "Study of high density polyethylene (HDPE) pyrolysis with reactive molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - material:polymer-organic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:reactive-md
source_refs: []
doi: "10.1016/j.polymdegradstab.2014.03.022"
year: 2014
authors:
  - "Xiaolong Liu"
  - "Xiaoxia Li"
  - "Jian Liu"
  - "Ze Wang"
  - "Bin Kong"
  - "Xiaomin Gong"
  - "Xiaozhen Yang"
  - "Weigang Lin"
  - "Li Guo"
venue: "Polym. Degrad. Stab. 104 (2014) 62–70"
pdf_sha256: "4df103d19ebc7cb166048b2f911672aecb9986a82a7ea84e89ef0056720212b3"
pdf_path: "papers/ReaxFF_others/Study of high density polyethylene (HDPE) pyrolysis with reactive molecular dynamics.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019kowalik-venue-bez-tytu -->

## Evidence and attribution

!!! warning "Slug / manifest mismatch"

    The wiki **`paper_id` slug** references **Kowalik**, but the registered **PDF** is **Liu *et al.*** in ***Polym. Degrad. Stab.*** **2014** (**HDPE** **pyrolysis** with **ReaxFF**). Front matter above matches the **actual article**; rename **`paper_id`** only via a **governed** migration.

## Summary

This article applies **ReaxFF molecular dynamics** to **high-density polyethylene (HDPE)** **pyrolysis** using a **7216-atom** model system—the authors state this as a **first** **ReaxFF** application to **HDPE** pyrolysis at this scale in their abstract. Simulations run in the **NVT** ensemble for **250 ps** total sampling across **2000–3000 K** conditions. **Primary gas** formation pathways are extracted with a post-processing tool **VARMD** that decodes **reaction** events from trajectories.

The work compares **simulated** **product** distributions and **global** **kinetics** (via an **ωC31** kinetic framework described in the paper) to **Py-GC/MS** experiments and **literature** data on **polyethylene** **thermolysis**. The abstract reports that predicted **~90% mass-loss** times fall near **experimental** ranges from the literature, and that detailed **reaction** networks from trajectories agree **broadly** with prior mechanistic literature.

## Methods

### 1 — MD application (RMD, ReaxFF, LAMMPS)

**Engine:** **LAMMPS** **reax** **package** (*Polym. Degrad. Stab.* **2.1.2**). **FF:** **ReaxFF** in the **van** **Duin** **formulation** (as **cited** in the **Introduction**; **C/H** **parameters** for **alkanes** in that **lineage**). **System / composition:** **bulk** **HDPE** **(8** **PE** **chains,** **n=150,** **ρ≈1.0 g/cm³)**, **7216** **atoms** in a **cubic** **PBC** **box** (edge **~38.2 Å** after **DREIDING/Amorphous** **Cell** **construction** as **described**). **Ensemble:** **NVT**; **Nose–Hoover**-type **thermostat** (paper: **Nosé**–**Hoover** with **damping** **0.1** **ps**). **Timestep:** **0.25** **fs**. **Protocol:** one **RMD** **trajectory** at each temperature **2000 K, 2125 K, 2250 K, 2375 K, 2500 K, 2750 K, 3000 K** for **250** **ps**; **PBC** in all **directions** as **in** the **PE** **cell**. **Barostat / servocontrol of mean pressure:** **N/A** — **NVT** only. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**—single **RMD** **trajetories** **at** each **T**. **Analysis:** **VARMD** to **list** **elementary** **reactions** from **trajectories**; **kinetic** **treatment** via **ωC\(_{31}\)** **(paper)** **and** **comparison** to **Py-GC/MS** **+** **literature**.

### 2 — Force-field training

**N/A** — **uses** **established** **ReaxFF**; **DREIDING** appears **only** for **initial** **cell** **build** and **minimization**, not **RMD** **dynamics**.

### 3 — Static QM / DFT

**N/A** — the **contribution** is **ReaxFF** **RMD**; **no** **DFT** **reoptimization** in **this** **2014** **work**.
## Findings

The authors present **atom-resolved** **scission** pathways for **HDPE** at high temperature and argue that **ReaxFF MD** is a **practical** tool for **mechanism** mining despite **high-T** acceleration inherent to short **MD** windows. **Overall** kinetics from the **ωC31** analysis are used to estimate **timescales** for deep **conversion**, matching **order-of-magnitude** **experimental** **thermolysis** timescales cited in the abstract.

## Limitations

Short **trajectories** and **high temperatures** accelerate chemistry beyond typical **lab** **ramp** rates. **ReaxFF** uncertainty affects **branching** selectivity among **radical** pathways. The **slug** mismatch complicates corpus **discovery** until metadata is normalized.

**VARMD**-style decoding is the paper’s distinguishing feature: it converts **reactive** trajectories into **human-auditable** reaction lists, which is valuable for building **mechanism** diagrams for **polymer** **pyrolysis** even when absolute **rates** remain **scale**-sensitive.

## Relevance to group

**Polymer** **pyrolysis** benchmark using **ReaxFF** + **VARMD**-style analysis—complements **hydrocarbon** **combustion** and **pyrolysis** papers in the broader **ReaxFF** corpus.

## Citations and evidence anchors

- DOI [10.1016/j.polymdegradstab.2014.03.022](https://doi.org/10.1016/j.polymdegradstab.2014.03.022); *Polym. Degrad. Stab.* **104** (2014) **62–70**.
- Corpus PDF: `papers/ReaxFF_others/Study of high density polyethylene (HDPE) pyrolysis with reactive molecular dynamics.pdf`.
- Excerpt alignment: `normalized/extracts/2019kowalik-venue-bez-tytu_p1-2.txt`.

## Reader notes (extended)

If you need a **bibliography** export, prefer **`doi`** + **Polym. Degrad. Stab.** metadata above rather than the **filename** stem, which reflects historical ingest naming rather than authorship.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
