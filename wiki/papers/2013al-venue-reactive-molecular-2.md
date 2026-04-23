---
id: paper:2013al-venue-reactive-molecular-2
type: paper
title: "Reactive molecular dynamics simulations of oxygen species in a liquid water layer of interest for plasma medicine"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:water-silica-geo
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:reactive-md
  - keyword:nvt-simulation
source_refs: []
doi: "10.1088/0022-3727/47/2/025205"
year: 2014
authors:
  - "Yusupov, M."
  - "Neyts, E. C."
  - "Simon, P."
  - "Berdiyorov, G."
  - "Snoeckx, R."
  - "van Duin, A. C. T."
  - "Bogaerts, A."
venue: "Journal of Physics D: Applied Physics"
pdf_sha256: "bc07143d9239e0eab0532d022fa499f81c3070a753074cd43b758fdcf22f47c6"
pdf_path: "papers/Yusupov_JPhysD_plasma_medicine_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013al-venue-reactive-molecular-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. The wiki **slug** prefix `2013al-` is a **corpus artifact**; metadata matches **Yusupov et al.** **J. Phys. D** (**2014** PDF filename).

## Summary

**Reactive MD** investigates **O**, **OH**, **HO₂**, and **H₂O₂** interacting with a **liquid** **water** film as a **model** of **biomolecule** surface **layers** in **plasma** **medicine**. The abstract reports **OH**, **HO₂**, and **H₂O₂** can **penetrate** deeply into the **water** layer; **O**, **OH**, and **HO₂** undergo **H-abstraction** from **water**, while **H₂O₂** does **not** in their observations—framed as **transport** and **reaction** constraints for **ROS** reaching **cells**. The **J. Phys. D** study is explicit that **liquid** **water** **slab** geometry is a **deliberate** simplification of **plasma–liquid** **coupling** intended to isolate **downstream** **ROS** **fates** after species enter a **condensed** **phase**.

## Methods


**Potential:** **ReaxFF** **C/H/O/N** **glycine/water** **parameters** (**Rahaman et al.**). **Water slab:** **500** **H2O** in **25 x 25 x 23.93 A** (**1 g/cm^3**); **NVT** **equilibration** **500 ps** at **300 K** (**Bussi** thermostat, **100 fs** coupling); expand to **25 x 25 x 80 A** and **relax** **interfaces** **100 ps**. **Production:** **Delta t = 0.25 fs**; **Bussi** **thermostat**; **z** **drift** **restrained** (**dummy** **atom** vs **water** **COM**, **Figure 1**). **ROS** **impacts:** species **placed** **>=10 A** above the **slab** with **thermal** **velocities** at **300 K**; **O** **trajectories** **>=1.4 ns** in **examples** cited. **Like-species** **ROS** **bundles:** **z ~ 55 A**, **>=7 A** **separation**, **100 ps** **runs**, **five** **replicas** **each**.

**Figure**-linked **protocols** in `papers/Yusupov_JPhysD_plasma_medicine_2014.pdf` document **initial** **ROS** **placement**, **replica** **counts**, and **analysis** **windows** used to classify **penetration** versus **surface** **scavenging** for each **species**.

### Force-field training

**N/A —** applies the published **ReaxFF C/H/O/N** (**Rahaman et al.**) parameter set; no new **QM** refit is reported in the abstract (`normalized/extracts/2013al-venue-reactive-molecular-2_p1-2.txt`).

### MD application (integrated)

**Engine / code:** **Reactive molecular dynamics**; **N/A —** specific package name not on p1–2 excerpt—confirm in **`pdf_path`**.

**System & composition:** **500 H\(_2\)O** molecules in a cell **25 × 25 × 23.93 Å** (density **~1 g cm\(^{-3}\)**), later expanded to **25 × 25 × 80 Å** for interface relaxation (**Methods** in **`pdf_path`**).

**Boundaries / periodicity:** **3D periodic** supercell for the **slab** geometry (**Methods**).

**Ensemble:** **NVT** for equilibration/production as summarized from the article Methods on this page.

**Timestep:** **Δt = 0.25 fs** for production (**Methods**).

**Duration / stages:** **500 ps** **NVT** equilibration at **300 K**; **100 ps** interface relaxation after cell expansion; **ROS** impact trajectories include **≥1.4 ns** examples for **O**; like-species bundles use **100 ps** windows with **five replicas** each (**Methods**/**Figure 1**).

**Thermostat:** **Bussi–Donadio–Parrinello** thermostat, **100 fs** coupling time, during **NVT** equilibration and production (**Methods**).

**Center-of-mass restraint:** **z**-drift restraint tying a **dummy atom** to the water **COM** (**Figure 1**).

**Barostat / pressure:** **N/A — NPT** barostat **not** used for the summarized **NVT** slab protocol.

**Temperature:** **300 K** for equilibration and thermalized **ROS** initial velocities.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A — umbrella / metadynamics** not used; **five** independent **replicas** for selected like-species bundles (**Methods**).

## Findings

**Outcomes:** **OH**, **HO\(_2\)**, and **H\(_2\)O\(_2\)** reach **bulk-like** water regions of the slab; **O**, **OH**, and **HO\(_2\)** drive **hydrogen-abstraction** cascades, whereas **H\(_2\)O\(_2\)** remains **non-dissociative** in the reported water-contact runs (**abstract** alignment + article discussion summarized here). **HO\(_2\)** solution behavior shows rapid **proton shuttling** consistent with **literature equilibrium** constants (**Methods/Results** in **`pdf_path`**).

**Comparisons:** **ROS** fates are contrasted with expectations from **plasma medicine** literature on transport through biofilms (**introduction** chain).

**Sensitivity / levers:** **Penetration vs surface scavenging** depends on species identity (**O** vs **OH** vs **HO\(_2\)** vs **H\(_2\)O\(_2\)**) and initial placement/replica sampling (**Figure 1** protocol).

**Limitations:** **Simplified** planar **water** film; **ReaxFF** accuracy for **O\(_3\)**/**RNS** excluded in this parameterization; **plasma** formation chemistry is **not** simulated—only post-liquid **ROS** + **water**.

**Corpus honesty:** Wiki slug prefix **`2013al-`** is a **corpus artifact**; metadata corresponds to **2014** *J. Phys. D* **`pdf_path`**. Duplicate ingest: **`[[2013al-venue-reactive-molecular]]`**.

## Limitations

See **Findings** (limitations bullet). Prefer this slug’s **`pdf_path`** when reconciling hashes with the **`2013al-venue-reactive-molecular`** PDF path.

## Relevance to group

**Adri C. T. van Duin** coauthored **reactive** **ROS**/**water** simulations for **plasma** **biointerfaces**.

## Citations and evidence anchors

- DOI **10.1088/0022-3727/47/2/025205** — *J. Phys. D: Appl. Phys.* **47**, 025205 (2014).
- PDF: `papers/Yusupov_JPhysD_plasma_medicine_2014.pdf`; extract: `normalized/extracts/2013al-venue-reactive-molecular-2_p1-2.txt`.

## Related topics

- [[reaxff-family]]
