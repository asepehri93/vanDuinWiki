---
id: paper:2020taehoon-park-journal-of-s-investigation-silicon
type: paper
title: "Investigation of Silicon Carbide Oxidation Mechanism Using ReaxFF Molecular Dynamics Simulation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - method:reaxff
  - material:widegap-semiconductor
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:lammps
  - keyword:nve-simulation
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.2514/1.A34669"
year: 2020
authors:
  - "Taehoon Park"
  - "Chanwook Park"
  - "Jiwon Jung"
  - "Gun Jin Yun"
venue: "Journal of Spacecraft and Rockets (2020)"
pdf_sha256: "f1cb085bdec3d5d10869184e0bcbdbf30a85eb2336614b006d4816cf9156b139"
pdf_path: "papers/ReaxFF_others/2020.07 Investigation of Silicon Carbide Oxidation Mechanism Using ReaxFF Molecular Dynamics Simulation.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020taehoon-park-journal-of-s-investigation-silicon -->

**Atomic oxygen (AO)** **collision** simulations on **3C–SiC** surfaces with **(100)**, **(110)**, and **(111)** orientations use **ReaxFF** (Si/C/O parametrization after **Vashisth et al.**) in **LAMMPS**, comparing **NVE** and **NVT** thermal protocols to probe **temperature-dependent** **oxidation** sensitivity and mechanism.

## Summary

The work addresses **SiC** oxidation under conditions relevant to **low-Earth-orbit** **atomic oxygen** exposure for **thermal protection** materials. **LAMMPS** **ReaxFF** **MD** reports **orientation-dependent** reactivity and **mechanistic** changes with **temperature** and thermal protocol when AO impacts **3C–SiC** surfaces. **N/A** in this short summary for tabulated barrier heights—readers should cross-check the PDF.

## Methods

**1 — MD application.** **LAMMPS** with the **Vashisth** **Si/C/O ReaxFF**; **Materials Studio 2017** builds **3C-SiC** **(100)**, **(110)**, **(111)** **Si-terminated** slabs with **~15 Å** vacuum; **Table 1** gives periodic **xy** boxes, **~1728–1800** atoms per case, and dimensions (e.g. **(100) ~26×26×41 Å**). **NVT** at **300 K** for **40,000** steps to equilibrate the slab with a **thermostat** (see VOR for type). **AO deposition:** **0.25 fs** time step; **periodic x, y**; **fixed z**; **NVE** AO beam with **`fix deposit`**, one AO every **800** steps, initial height **~15 Å**, velocity **-7 km/s**; **2 Å** **fixed** bottom; sputtered/eroded atoms **deleted** per article protocol. **Production** compares **NVE** vs **NVT** on the slab; **(100)** **NVT** scans at **600, 900, 1200, 1800, 2000 K** to compare to **NVE** heating. **N/A** — NPT: **NVE/NVT** protocols only. **N/A** — metadynamics / umbrella sampling. **N/A** — electric field. **Barostat:** **N/A** (no NPT in excerpt). **Normal pressure in GPa** sense: **N/A** — beam impact, not NPT *hydrostatic* pressurization. **N/A** — if thermostat not named for a given sub-stage, confirm the PDF; Berendsen/Nosé-Hoover labels appear in the VOR for thermostatted segments as stated in the text.

**2 — Force-field training.** **N/A** — the study **uses** the **published** **Vashisth** field; the article cites its lineage rather than a new global fit in this work.

**3 — Static QM.** **N/A** — not a DFT-paper focus beyond what supports the chosen Reaxff.

**4 — Review or non-simulation.** **N/A** — research article with MD.

## Findings

**Outcomes and mechanisms.** **(100)**, **(110)**, and **(111)** **3C–SiC** show **orientation-dependent** oxidation and product evolution under the **AO** impact protocol. **NVE**- vs **NVT**-based treatment leads to **qualitative** and **quantitative** differences in inferred mechanisms for some facets and temperatures, as the authors report.

**Comparisons and sensitivity.** **Temperature** sweeps on **(100)**; facet-to-facet **comparison** is central.

**Authored limitations.** The discussion contrasts **complex** **SiC** **oxidation** to simpler **Si** oxidation. **N/A** — long-time oxide growth in **LEO** without high-flux acceleration.

**Corpus honesty.** **Beam** **flux** is **higher** than true **LEO** in part of the text’s compromise; use `pdf_path` for exact statements.

## Limitations

**Beam**/**collision** MD simplifies **real LEO** flux, **charging**, and **long-time** oxide growth; **ReaxFF** accuracy for **hyperthermal** AO energies should be checked against **QM** benchmarks where available.

## Relevance to group

Application of **community ReaxFF** (**Vashisth**) to **SiC** **space-environment** oxidation—a common **reactive MD** use case for **wide-gap** ceramics.

## Citations and evidence anchors

- DOI: `10.2514/1.A34669`

## Related topics

- [[reaxff-family]]
