---
id: paper:2012saha-venue-jp300581b
type: paper
title: "Carbonization in polyacrylonitrile (PAN) based carbon fibers studied by ReaxFF molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1021/jp300581b"
year: 2012
authors:
  - "Saha, Biswajit"
  - "Schatz, George C."
venue: "Journal of Physical Chemistry B"
pdf_sha256: "138af2f995eb5f6c6a5331ba6c41a06dd5572fe6c67f24ad1f0128bd7375d3fe"
pdf_path: "papers/ReaxFF_others/Saha_Schatz_PAN_JPCB_2012.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012saha-venue-jp300581b -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

**ReaxFF** **MD** probes **carbonization** of a **stabilized PAN**-like **model** (**“B”** in the paper’s Figure 1) at **2500 K** and **2800 K** and at **densities** **1.6** and **2.1 g/cm³** (abstract). Species evolution tracks **N₂**, **H₂**, **NH₃**, **HCN**, **carbon-only** **rings** (five-, six-, seven-membered) and **polycyclic** structures. The abstract notes **five-membered** rings often follow **N₂** release and precede **six-membered** rings, and discusses **elimination** pathways for **gases** versus prior literature, including **alternatives**.

## Methods


**Model:** **Sixteen** **B** molecules (**C32H14N10** per **Figure 1**) in a **periodic** cell; **initial** **density** **1.6** or **2.1 g/cm^3** at **300 K** (cell resized accordingly). **Equilibration:** **300 K**, **60 ps**; **10** **snapshots** (**50-60 ps** window) seed **annealing**. **Annealing:** heat **3000 K** at **10 K/ps** (finds no **reaction** below **2500 K**); **production** **NVT** at **2500 K** or **2800 K** for **500 ps** each (**Berendsen** thermostat, **100 fs** coupling). **Volatiles** (**N2**, **H2**, **NH3**, **HCN**) **removed** every **50 ps** during **constant-T** runs to mimic **open** **system** **mass** **loss**. **Total** trajectory **length** **750 ps** (**2500 K**) or **780 ps** (**2800 K**) including **preheat**. **Integration** settings (including the integration **timestep**) are given in **Section 2** of the article alongside the **ReaxFF** **CHO/N** parameter references; **N/A —** the integration **timestep** value is not recovered from `normalized/extracts/2012saha-venue-jp300581b_p1-2.txt`—read **`pdf_path`**.

### MD application (PAN model carbonization)

**Engine / code:** **ReaxFF** **molecular dynamics**; **N/A —** standalone engine name not recovered from the indexed excerpt—verify **`pdf_path`**.

**System size & composition:** **Sixteen** **B** molecules (**C\(_{32}\)H\(_{14}\)N\(_{10}\)** per **Figure 1**) in a **periodic** cell prepared at **1.6** or **2.1 g/cm³** initial **density** at **300 K**.

**Boundaries / periodicity:** **Periodic** cell with **density** chosen to mimic carbonization **conditions**; **open-system** volatile removal (below) approximates mass loss.

**Ensemble:** **NVT** during **equilibration** and **constant-temperature** **production** segments.

**Timestep:** **N/A —** explicit **Δt** not quoted in the abstract-level extract; **Section 2** of **`pdf_path`** lists integration settings.

**Duration / stages:** **300 K** **equilibration** **60 ps**; **annealing** heat ramp **300 → 3000 K** at **10 K/ps**; **production** **500 ps** at **2500 K** or **2800 K**; volatiles removed every **50 ps**; total protocol **750 ps** (**2500 K**) or **780 ps** (**2800 K**) including preheat as summarized on this page.

**Thermostat:** **Berendsen** thermostat with **100 fs** coupling constant (damping time).

**Barostat / pressure control:** **N/A —** **NPT** barostat not used for the quoted **NVT** pyrolysis protocol.

**Temperature:** **300 K** initial conditioning; **2500 K** and **2800 K** carbonization temperatures; ramp to **3000 K** during **annealing** search.

**Pressure / stress:** **N/A —** not a controlled variable in the summarized protocol.

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** not used.

### Force-field training

**N/A —** uses a published **CHO/N** **ReaxFF** parametrization cited in **Section 2** of **`pdf_path`**; this article focuses on **application** trajectories rather than refitting the field.

## Findings

**Outcomes / mechanisms:** **Carbonization** produces **N\(_2\)**, **H\(_2\)**, **NH\(_3\)**, **HCN**, and **carbon-only** **five/six/seven-membered** rings plus larger **polycycles**; **five-membered** rings often **follow** **N\(_2\)** release and **precede** **six-membered** rings in the reported trajectories.

**Comparisons:** Authors compare **gas** **elimination** routes to prior **literature** mechanisms and note **alternative** pathways consistent with their **ReaxFF** simulations.

**Sensitivity / design levers:** **Temperature** (**2500 K** vs **2800 K**), initial **density** (**1.6** vs **2.1 g/cm³**), and **volatile** removal cadence (**every 50 ps**) steer species evolution and ring formation sequences.

**Limitations / outlook:** The **open-system** removal protocol approximates **mass loss** but is not a full **grand-canonical** treatment; **Section 2** of **`pdf_path`** is authoritative for reproducing integration settings.

**Corpus / KB honesty:** Summaries use **`pdf_path`** and `normalized/extracts/2012saha-venue-jp300581b_p1-2.txt` (abstract/intro heavy); figures and quantitative species timelines require the **PDF**.

## Limitations

**Model** **B** is a **stabilized** **fragment**—not full industrial **fiber** microstructure; **ReaxFF** **CHO**/**N** chemistry accuracy; **extract** does not reproduce all **figures**. **Industrial** **carbonization** includes **furnace** **gradients**, **catalyst** **traces**, and **long** **residence** **times** that are not represented in **nanosecond** **open-system** **MD** at **fixed** **temperature**. **PAN** **precursor** **chemistry** in manufacturing also includes **fiber** **drawing** and **oxidative** **stabilization** steps absent from the **model** **B** **fragment** protocol. **Carbon** **fiber** **microstructure** depends on **spool** **history** and **post-processing** **temperature** **ramps** not represented in **isothermal** **MD** **chunks**. **JPCB** **Section 2** contains the authoritative **integration** and **thermostat** settings for reproducing reported **trajectories**.

## Relevance to group

**Carbon** **precursor** **pyrolysis** with **ReaxFF** parallels group interests in **hydrocarbon**/**solid** **conversion** chemistry.

## Citations and evidence anchors

- DOI **10.1021/jp300581b** — *J. Phys. Chem. B* **116**, 4684–4692 (2012).
- Extract: `normalized/extracts/2012saha-venue-jp300581b_p1-2.txt`.

## Related topics

- [[reaxff-family]]
