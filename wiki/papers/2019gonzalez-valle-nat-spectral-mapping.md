---
id: paper:2019gonzalez-valle-nat-spectral-mapping
type: paper
title: "Spectral mapping of thermal transport across SiC-water interfaces"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:classical-md
  - task:application
  - material:widegap-semiconductor
candidate_tags: []
paper_keywords:
  - keyword:water-interfaces
  - keyword:classical-ff
  - keyword:nve-simulation
  - keyword:lammps
  - keyword:validation-experiment
source_refs: []
doi: "10.1016/j.ijheatmasstransfer.2018.11.101"
year: 2019
authors:
  - "C. Ulises Gonzalez-Valle"
  - "Bladimir Ramos-Alvarado"
venue: "International Journal of Heat and Mass Transfer"
pdf_sha256: "2eec90e6b7a47b11fdadee5c8b02ff890d1c93b545d427e024817d8c83f3d637"
pdf_path: "papers/Others/Gonzalez_Valle_water_SiC_IntJHeatTransfer_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019gonzalez-valle-nat-spectral-mapping -->

## Summary

**Nonequilibrium molecular dynamics (NEMD)** with **spectral heat-flux mapping** analyzes **thermal boundary conductance (TBC)** between **3C–SiC** and **water** for **C- vs Si-terminated (100)** and **(111)** surfaces under **hydrophobic vs hydrophilic** **LJ** tuning. The **International Journal of Heat and Mass Transfer** article (**DOI** **10.1016/j.ijheatmasstransfer.2018.11.101**) decomposes **interfacial** **heat** **flux** into **frequency-resolved** **contributions** **q(ω)** and relates **mode** **overlap** integrals to **temperature-jump** **thermal** **boundary** **conductance**, letting the authors compare **wetting** **trends**, **phonon** **density** **of** **states**, and **spectral** **transport** **anisotropy** across **four** **termination** **cases**. **Low-frequency** modes dominate transport for several terminations, while **Si-terminated SiC(111)** shows notable **high-frequency** contributions. **Out-of-plane** vibrational components carry most of the **interfacial heat flux**; **in-plane** fractions are smaller—especially on **(111)**—and correlate with **interfacial liquid structure** and **DOS overlap** more cleanly than with **interfacial bonding strength** alone.

## Methods

### Classical water and SiC bulk models (A/B)

**Water:** **SPC/E**, **rigid** (**SHAKE**), **PPPM** electrostatics (accuracy **10⁻⁶**). **SiC:** **MEAM** for **Si–Si, C–C, Si–C**; **solid–liquid** coupling via **12–6 Lennard-Jones** on **Si–O** and **C–O** only (**C–O** **r** and **ε** fixed; **Si–O** **ε** scanned **0.005–0.025 eV** at fixed **Si–O** **r = 2.63 Å** to span **wetting**).

### NEMD geometry and protocol (B)

**Cells:** two **SiC** slabs sandwiching **~6 nm** water; **slab** **~10 nm** long (**z**); cross section **2.62×2.62 nm²** (**100**) or **2.78×2.67 nm²** (**111**); **fixed** outer layers; **1.5 nm** **hot/cold** **NEMD** regions.

**Workflow (LAMMPS + VMD):** minimize → **NVT 300 K, 1 ns** (**Nosé–Hoover**, **0.1 ps** τ) → **NVE 1 ns** sanity check → **5 ns** NEMD relax → **5 ns** production (sample **25 ps**).

**Spectral binning:** **q(ω)** is accumulated in **frequency** bins after **5 ns** **NEMD** **relaxation** and **5 ns** **production**, with **25 ps** **chunks** used for **time** **averaging** of **interfacial** **heat** **flux** spectra as stated in the **Methods** section of the article.

### Analysis

**Spectral heat flux** **q(ω)** from **force–velocity** correlations; **DOS** from **VACF**; **TBC** from **temperature-jump** fits.

### ReaxFF / reactive training (A)

**Not used**—**non-reactive** **MEAM** + **LJ** interface study.

**Integration parameters (NEMD).** **LAMMPS** **molecular dynamics** on **SiC**/**water** **slabs** uses **periodic** in-plane **PBC** with fixed outer layers, sandwiching **~6 nm** water between **~10 nm** **slabs** (cross sections stated above). **Workflow:** **NVT** at **300 K** for **1 ns** with **Nose–Hoover** thermostat (**0.1 ps** time constant) → **NVE** sanity **1 ns** → **5 ns** **NEMD** relaxation → **5 ns** **production** with **25 ps** chunks for spectral averaging. **Timestep:** the article’s **Methods** tabulate the stable **timestep** in **fs** for **MEAM**/**SPC/E** stability (see `pdf_path` if not repeated here). **Barostat / hydrostatic pressure:** **N/A** — fixed lateral dimensions without **GPa** **pressure** servo in the summarized **NEMD** path. **External electric field:** **N/A**. **Enhanced sampling:** **N/A**.

## Findings

### Comparisons and sensitivity

**Literature context:** the article contrasts **TBC** trends with prior **wettability** scaling arguments (e.g., contact-angle–based correlations in the **literature**) and shows cases where **DOS overlap** aligns better with **thermal boundary conductance** than **bond strength** alone. **Sensitivity:** **Si–O Lennard-Jones ε** scans (**0.005–0.025 eV**) modulate wetting and, through **phonon** overlap, shift **q(ω)** and **TBC** between **hydrophilic** and **hydrophobic** **(100)**/**(111)** terminations. **Temperature:** **300 K** liquid preparation before **NEMD** establishes the **thermal** boundary conditions quoted above.

### Limitations and corpus honesty

Rigid **SPC/E** water and empirical **SiC–water** **LJ** coupling omit polarization and **quantum** effects that could matter for some interfaces—limitations stated in the article discussion. **PDF-grounded detail:** numeric **timestep** and any auxiliary **pressure**/stress controls beyond this summary appear only in the **Methods** of `pdf_path`; this page does not invent missing numbers.

### Mechanisms

**TBC** correlates with **phonon DOS overlap** **S** more cleanly than **wettability** alone; **Si-terminated (100)** hydrophilic cases show among the **strongest S**/**highest TBC** vs **hydrophobic C-terminated (100)**. **Out-of-plane** modes dominate **q(ω)** on (**100**); **in-plane** fraction drops on (**111**). **Si-terminated (111)** can contribute **high-ω** **DOS** beyond the bulk **gap**; **C-terminated** surfaces concentrate **q(ω)** at lower **THz** cutoffs than **Si-terminated** on the same plane. **Depletion length** reconciles **TBC** scatter vs contact-angle expectations.


## Limitations

Empirical **SiC–water LJ** coupling is minimal; rigid **SPC/E** omits **quantum**/**polarization** effects for some interfaces.

## Relevance to group

Penn State **MNE** collaboration on **nanoscale thermal transport** at **solid–liquid** interfaces.

## Citations and evidence anchors

- `papers/Others/Gonzalez_Valle_water_SiC_IntJHeatTransfer_2019.pdf`

## Related topics

- [[reaxff-family]]
