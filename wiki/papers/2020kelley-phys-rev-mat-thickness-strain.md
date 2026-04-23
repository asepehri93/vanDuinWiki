---
id: paper:2020kelley-phys-rev-mat-thickness-strain
type: paper
title: "Thickness and strain dependence of piezoelectric coefficient in BaTiO3 thin films"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:ferroelectrics-polar
  - domain:reaxff-lineage
  - material:perovskite-oxide
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:validation-experiment
  - keyword:oxide-surface
  - keyword:lammps
source_refs: []
doi: "10.1103/PhysRevMaterials.4.024407"
year: 2020
authors:
  - "K. P. Kelley"
  - "D. E. Yilmaz"
  - "L. Collins"
  - "Y. Sharma"
  - "H. N. Lee"
  - "D. Akbarian"
  - "A. C. T. van Duin"
  - "P. Ganesh"
  - "R. K. Vasudevan"
venue: "Phys. Rev. Materials 4, 024407 (2020)"
pdf_sha256: "fd8154a6cf7f1f7881079452d99a55a54588d6fd7aa2e7ec65f253c0fa41f266"
pdf_path: "papers/KelleyPhysRevMaterials_2020_BaTiO3.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020kelley-phys-rev-mat-thickness-strain -->

## Summary

**Piezoresponse force microscopy (PFM)** with **interferometric displacement sensing (IDS)** is used to quantify **converse piezoelectric coefficients (d₃₃)** in **epitaxial BaTiO₃** films on **(001) SrTiO₃** as thickness varies from **~10 nm to ~80 nm**. Experiments show a **strong thickness-driven drop** in **d₃₃** for ultrathin films. **ReaxFF-based MD** with an **ab initio–derived BaTiO₃** parameterization explains the trend via **thickness- and strain-dependent** evolution of **depolarization-field screening** regions under applied electric fields. The study connects **device-relevant** **ultrathin** **ferroelectric** metrics to **atomistic** **screening** physics that are difficult to sample with **DFT** alone at similar **length scales**.

## Methods

**Experiment (epitaxial BTO, PFM/IDS).** **BaTiO₃ (BTO)** films are grown by **pulsed laser deposition** on **(001) SrTiO₃** with a **~5 nm SrRuO₃** **bottom electrode** (thickness **series 10–80 nm** in the **abstract** / **intro**). **AFM** and **X-ray** **reciprocal-space** **mapping** characterize **morphology** and **in-plane** **strain** **vs** **thickness**. **Piezoresponse** is mapped with **band-excitation** **PFM**; **quantitative** **d₃₃** use **interferometric displacement sensing (IDS)** to **limit** **spurious** **electrostatic** **contamination** of the **mechanical** **response** (see **Phys. Rev. Materials** **article** and **Supplement**).

**1 — MD application (ReaxFF on BTO under E).** The paper uses **ReaxFF-based MD** with a **recent fully ab initio–derived** **BTO** **parameter set** in the **ReaxFF** **form** to study **thickness-** and **strain-dependent** **depolarization-field** **screening** under **applied** **electric** **fields** (context in **abstract** and **Sec. I** of the **PDF**). **N/A —** this note does not transcribe **LAMMPS**-level **input** **(ensemble, timestep, supercell** **thickness,** **number of** **unit** **cells,** **PBC,** **thermostat,** **barostat)**; take those from the **main** **text** and **SI** of `pdf_path`. **Duration / production** **length** in **ps** or **ns** for the **ReaxFF** **runs** is **specified** in the **article**/**SI** (not tabulated in this **wiki**). **Target** **temperature** in **K** for the **MD** **stages** is **in** the **source** (not **copied** here). **Barostat / pressure for MD:** **N/A** or **stated in PDF** for any **NPT** **stages**—**confirm** in **source**. **External electric field in MD:** **yes** in the **sense** of the **manuscript** (applied **E** to probe **ferroelectric** **response** / **screening**), not **N/A**. **Shear / shock / enhanced sampling:** **N/A —** not the **stated** **focus** in the **abstract**-level **summary** here.

**2 — Force-field training.** **N/A —** the **BTO** **ReaxFF** is adopted as a **prior ab initio–derived** set; this article is **not** a new ReaxFF fit (it cites that parameterization).

**3 — Static QM / DFT-only.** **N/A —** the **contribution** is **experiment** + **ReaxFF** **dynamics** for **screening** **physics**, not a new **static** **DFT** **benchmark** in this **article** as the **lead** result.

## Findings

**Outcomes, comparisons, and mechanisms.** **IDS**-based **d₃₃** is about **20.5 pm/V** for the **~80 nm** film and falls to **under ~2 pm/V** for the **~10 nm** film in the same epitaxial series (values as stated in the **Phys. Rev. Materials** abstract and body). **PFM** and **Strain/structure** ( **RSM** ) track **higher** **in-plane** **compressive** **strain** in **thinner** **BTO** on this **stack**, **co-plotted** with **piezoresponse**. **ReaxFF** **MD** is reported to show a **thicker** **screening** **region** of **the** **depolarization** **field** in **ultrathin** **BTO** under **compressive** **in-plane** **strain** when an **E**-**field** is **applied**, i.e. **interfacial** / **screening** **physics** is **tied** to the **d₃₃** **trend** **(not** **a** **single** **intrinsic** **coefficient** only).

**Sensitivity, limitations, corpus honesty.** **d₃₃** **at** the **ultrathin** **extreme** is **gated** by **how** **E**-**induced** **bound** **charge** is **screened** ( **thickness-** and **strain-dependent** in the **ReaxFF** **story**). **Classical** **ReaxFF** does **not** **recover** full **DFT-**-**level** **electronic** **polarization**; **PFM/IDS** **uncertainties** and **tip**-**field** **effects** stay **in** the **measured**-**data** **discussion** of the **source**.

## Limitations

Classical reactive MD cannot capture full **electronic** polarization changes at the DFT level; quantitative agreement relies on the fitted **ReaxFF** surface/screening physics encoded in the parameterization. **PFM** **quantification** also depends on **tip** **calibration** and **electrostatic** **artifacts**; the article’s **IDS** **protocol** is intended to mitigate **spurious** **piezoresponse**, but **cross-lab** **absolute** **d₃₃** comparisons still require **careful** **metadata**. **Strain** **maps** from **X-ray** **reciprocal-space** **mapping** should be co-registered with **film** **thickness** when interpreting **MD** **screening** **thickness** trends. **Electrode** **geometry** in **PFM** may couple to **domain** **patterns** not represented in **periodic** **MD** **cells**.

## Relevance to group

Joint **ORNL + PSU (van Duin)** effort tying **ferroelectric thin-film** measurements to **ReaxFF** modeling of **screening** and **strain**—a template for **perovskite** functional property studies in the wiki.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevMaterials.4.024407](https://doi.org/10.1103/PhysRevMaterials.4.024407)

## Related topics

- [[reaxff-family]]
- [[2020hou-j-appl-phys-two-dimensional-hybrid]]
