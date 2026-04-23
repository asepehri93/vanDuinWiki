---
id: paper:2021he-venue-paper
type: paper
title: "Subsurface structural change of silica upon nanoscale physical contact: Chemical plasticity beyond topographic elasticity"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:mechanics-tribology
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:oxide-surface
  - keyword:tribology
  - keyword:reaxff-application
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1016/j.actamat.2021.116694"
year: 2021
authors:
  - "Hongtu He"
  - "Zhe Chen"
  - "Yen-Ting Lin"
  - "Seung Ho Hahn"
  - "Jiaxin Yu"
  - "Adri C. T. van Duin"
  - "Tobias D. Gokus"
  - "Slava V. Rotkin"
  - "Seong H. Kim"
venue: "Acta Materialia (in press as uncorrected proof in corpus; VOR: DOI above)"
pdf_sha256: "b03442e10ca5cecb6ce4f77271423c04b725cfe4311fb35dcdab93132b27b1cd"
pdf_path: "papers/He_Hahn_ActaMat_2021_nanoscale_plasticity_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2021he-venue-paper -->

## Summary

**Nano-FTIR** / **s-SNOM** and **ReaxFF MD** (LAMMPS) are combined to study **fused quartz** under **nanoindentation** and **nanoscratch** with a **diamond** indenter, plus **150 H\(_2\)O** molecules to mirror **~40% RH** lab air. The **Si–O stretch** near **~1100 cm\(^{-1}\)** **red-shifts and broadens** in the **scratch** even when **height** recovers elastically, indicating **sub-Å** **network** changes (chemical plasticity) invisible to topography. **ReaxFF** shows **longer** mean **Si–O** bonds in the **densified** **plastic** zone than in **pristine** glass, so **volume loss** is tied to **bond elongation**, not contraction.

## Methods

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** with the **ReaxFF** implementation for **C/H/O/Si** (diamond + silica) as in Section 2.3; further parameter notes in **Supporting Information** per the article.
- **System & composition:** **Amorphous silica** substrate **5184** Si/O atoms; **diamond** indenter **3515** atoms, **spherical** tip **radius 1.5 nm**; **150** H\(_2\)O between tip and substrate.
- **Boundaries / periodicity:** 3D **PBC** in the supercell used for the scratch model (SI construction).
- **Ensemble:** **NVT** (canonical) for the scratch and post-scratch equilibration segments described.
- **Timestep:** **0.25 fs** throughout the MD in Section 2.3.
- **Duration / stages:** **300 K** equilibration **100 ps**; indenter engaged; **nanoscratch** at **10 GPa** contact pressure, **10 m/s** slip speed, **4 nm** slide; **50 ps** equilibration on the **extracted** substrate; optional **heating 300 K → 1500 K** at **10 K/ps**, **1 ns** hold, **cool 5 K/ps** to **300 K**, then **50 ps** equilibration (annealing protocol in the proof text) before structural analysis of **Si–O** length and **O–Si–O** angle distributions.
- **Thermostat:** **Nosé–Hoover**, **τ = 100 fs** in the quoted NVT runs.
- **Barostat / pressure:** N/A for the main **NVT** scratch segment; **N/A — pressure** not isotropically barostatted in that stage (contact **pressure 10 GPa** is a **load** target in the protocol, not a **hydrostatic** **NPT** barostat setting).
- **Temperature:** **300 K** baselines; **10 K/ps** and **5 K/ps** ramps when the annealing block is used.
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A.

**Experiment (nano-IR):** Fused quartz; **Hysitron** triboindenter; **Berkovich** and **cono-spherical** diamond tips; **5 mN** indent, **3–7 mN** scratch loads, **1 µm/s** speed; **neaSNOM** **nano-FTIR** with **MCT** detection and **interferometric** **amplitude/phase** as in **§2.2**; conversion to **dielectric** / **refractive index** per **tip–sample** models in **SI**.

### 2 — Force-field training

**N/A** — the paper applies **published ReaxFF** for **C/H/O/Si** (and diamond) with details in **SI**; it does not report a new **parameter** **fit** here.

### 3 — Static QM

**N/A** as a new DFT production study; interpretation leans on **literature** **vibrational** assignments for **Si–O** modes (e.g. cited discussion of **~1100 cm\(^{-1}\)**).

### 4 — Review

N/A.

## Findings

- **Spectroscopy:** The main **Si–O** **stretch** feature shifts from **~1100–1120** toward **~1050–1070 cm\(^{-1}\)** and **broadens** from **pristine** **pile-up** to **vertex** / **track** regions, so **subsurface** **chemistry** can change without **residual** **roughness** from **AFM** height.
- **MD vs experiment:** In the **plastic** **densified** **region**, **ReaxFF** **Si–O** bonds are **slightly longer** than in **pristine** glass, matching the **red-shift** / **elongation** narrative; **elastic**-looking **contact** can still show **bond-length** **broadening** in MD.
- **Comparisons:** **Nano-IR** line shapes vs **simulated** **network** **metrics**; **literature** on **silica** under **contact**. **Limitations:** **Proof** **PDF**; **DOI** **10.1016/j.actamat.2021.116694** for the **VOR** **pagination** and **SI**; **tip–sample** **optical** **models** for **nano-FTIR** add **uncertainty** as the authors note.

**Corpus / KB honesty:** This file is a **galley** in `pdf_path`; confirm **page** and **figure** numbers from the **typeset** **Acta Materialia** file when **citing** **externally**.

## Limitations

The repository PDF is an **uncorrected proof**; use the **DOI-resolved** **article** for final **SI** and **pagination**. **Nano-FTIR** **mapping** to **absorbance** uses **model** **approximations** for the **tip–sample** system.

## Relevance to group

**van Duin**-coauthored **joint** **experiment**–**ReaxFF** study of **silica** **tribo**-**chemistry**.

## Citations and evidence anchors

- *Acta Materialia* — DOI [10.1016/j.actamat.2021.116694](https://doi.org/10.1016/j.actamat.2021.116694); **Figs. 1–2** and **Section 2.3** in the ingested proof.

## Related topics

- [[reaxff-family]]
- [[silica-glass-reaxff]]
