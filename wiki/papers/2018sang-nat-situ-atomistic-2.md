---
id: paper:2018sang-nat-situ-atomistic-2
type: paper
title: In situ atomistic insight into the growth mechanisms of single layer 2D transition
  metal carbides
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:2d-layered
- domain:reactive-md
- method:reaxff
- method:dft-static
- task:experiment-integrated
- scale:atomistic
paper_keywords:
- keyword:reaxff-application
- keyword:2d-materials
- keyword:validation-experiment
- keyword:monte-carlo-sampling
candidate_tags: []
source_refs: []
doi: 10.1038/s41467-018-04610-0
year: 2018
authors:
- Xiahan Sang
- Yu Xie
- Dundar E. Yilmaz
- Roghayyeh Lotfi
- Mohamed Alhabeb
- Alireza Ostadhossein
- Babak Anasori
- Weiwei Sun
- Xufan Li
- Kai Xiao
- Paul R.C. Kent
- Adri C.T. van Duin
- Yury Gogotsi
- Raymond R. Unocic
venue: Nature Communications
pdf_sha256: 52db2edc70553f6e8afc255c5f1d7c3035272e9dcdf27f7026a2623cc22125e0
pdf_path: papers/Xiahan_Nature_Comm_MXene_defect_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018sang-nat-situ-atomistic-2 -->

!!! note "Duplicate PDF registration"

    This slug ingests **`papers/Xiahan_Nature_Comm_MXene_defect_2018.pdf`**. The same **Nature Communications** article (DOI **10.1038/s41467-018-04610-0**) is curated under **`[[2018sang-nat-situ-atomistic]]`** with the alternate path **`papers/Sang_Nature_Comm_MXene_defect_2018.pdf`**. Prefer **one** canonical `pdf_path` for citation hygiene when manifests are reconciled.

## Summary

In situ aberration-corrected scanning transmission electron microscopy (STEM) with heating reveals homoepitaxial growth of hexagonal TiC adlayers on defunctionalized Ti\(_3\)C\(_2\) MXene above roughly 500 °C, producing Ti\(_4\)C\(_3\)- and Ti\(_5\)C\(_4\)-like local compositions. Density functional theory and ReaxFF-based hybrid Monte Carlo and molecular dynamics (fbMC/MD) simulations interpret adatom diffusion, binding strengths, and step energies, supporting a Frank–van der Merwe growth mode for layered TiC on the MXene template. Electron energy-loss spectroscopy distinguishes carbon-rich adlayers from bare titanium metal, complementing the atomistic picture of carbon addition during growth.

This slug duplicates **`[[2018sang-nat-situ-atomistic]]`** under a different **`pdf_path`**; the **scientific** story is unchanged. Readers should prefer **one** canonical file for **checksum** hygiene in manifests while using either page for navigation.

## Methods

**Microscopy.** Experiments use a Nion UltraSTEM 100 with Protochips Fusion heating holders near \(10^{-9}\) Torr base pressure; Ti\(_3\)C\(_2\)T\(_x\) flakes are annealed while imaging. Beam–thermal coupling is discussed in the article because the electron beam can assist local chemistry.

**Spectroscopy.** EELS provides elemental contrast for C versus Ti in growing adlayers.

**Theory.** DFT supercells evaluate adsorption and step energetics for h-TiC on Ti\(_3\)C\(_2\). ReaxFF fbMC/MD captures bond-making and bond-breaking events during growth at elevated temperature.

**Atomistic modeling (DFT + ReaxFF fbMC/MD).** The article couples **DFT** supercells on **Ti\(_3\)C\(_2\)** with **h-TiC** adlayer models for adsorption, step-edge, and binding energetics, and uses **ReaxFF-based hybrid force-biased Monte Carlo / molecular dynamics (fbMC/MD)** to sample bond-making and bond-breaking during homoepitaxial growth. fbMC/MD alternates **Monte Carlo** bond events with **MD** propagation to access rare reactive steps at temperatures relevant to the experiments; reproducing published kinetics requires matching the **ReaxFF** parameter file, **timestep**, **temperature** schedule, and fbMC attempt frequencies in *Nature Communications* **Methods** / **SI**. **Engine / code:** reactive **molecular dynamics** with **ReaxFF** in the publication’s fbMC/MD workflow (**N/A — LAMMPS vs other engine** not restated in the indexed excerpt used here). **System / composition:** periodic **slab**/**supercell** models of the MXene template and adlayers (**N/A — atom counts and lateral cell vectors** in article/SI). **Boundaries:** **three-dimensional periodic boundary conditions (PBC)**. **Ensemble / timestep / duration:** **N/A — explicit NVE/NVT/NPT labels, integration timestep (fs), and total sampled time** not recovered from the p1–2 extract; use **Methods**/**SI**. **Thermostat / barostat:** **N/A — not in the indexed excerpt** for the fbMC/MD segment. **Temperature:** targets thermal conditions for high-temperature growth discussed alongside experiment. **Hydrostatic pressure control:** **N/A — not used** in the atomistic growth models summarized here. **Electric field in MD:** **N/A — not used** (STEM beam treated experimentally, not as a classical MD bias). **Enhanced sampling:** **fbMC/MD** (MC bond moves + MD); **N/A — umbrella / metadynamics / replica exchange** not indicated in the indexed text.
## Findings

Frank–van der Merwe growth of TiC monolayers proceeds with Ti and C supplied from the flake; h-TiC adlayers appear above 500 °C with beam assistance and at 1000 °C under thermal driving alone in the conditions reported. DFT highlights low adatom diffusion barriers, high surface energies for certain h-Ti facets, step-edge penalties, and strong h-TiC binding that favor layered addition rather than isolated islanding. EELS supports carbon-rich adlayers relative to metallic titanium patches.

**Duplicate-PDF finding.** The corpus stores **two** valid paths to the same article; operators should not treat differences in **file** **name** as differences in **scientific** content unless manifests explicitly split versions.

**Cross-scale consistency.** The paper’s argument combines **in situ** **microscopy** evidence for **layer** **addition**, **EELS** contrast for **carbon** enrichment, **DFT** **step** and **adsorption** energetics, and **fbMC/MD** **kinetics**. Readers should treat each layer as **mutually** **supporting** rather than independently sufficient: **microscopy** shows **morphology**, **DFT** supplies **relative** **energies** for candidate pathways, and **reactive** **MD** addresses **bond** **events** at finite **temperature**.

**Beam vs thermal driving.** Because **STEM** can **assist** **local** chemistry, the article distinguishes conditions where **adlayers** appear with **beam** help near **500 °C** from more **thermally** dominated regimes at **1000 °C**; reproducing the narrative requires citing the **exact** **experimental** **protocols** on the canonical page.

## Limitations

Electron-beam effects overlap with thermal driving forces; duplicate PDFs should be consolidated in the manifest. Full numerical settings appear in the main article and SI on the canonical slug.

## Relevance to group

van Duin group coauthors (Yilmaz, Lotfi, Ostadhossein, van Duin); this page records **alternate PDF bytes** for the same DOI.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1038/s41467-018-04610-0](https://doi.org/10.1038/s41467-018-04610-0)

## Reader notes (navigation)

- Canonical narrative hub: **`[[2018sang-nat-situ-atomistic]]`**
**Duplicate PDF.** Prefer one canonical `pdf_path` per DOI in manifests; simulation settings match `[[2018sang-nat-situ-atomistic]]`.

## Related topics

- [[2018sang-nat-situ-atomistic]]
- [[reaxff-family]]
