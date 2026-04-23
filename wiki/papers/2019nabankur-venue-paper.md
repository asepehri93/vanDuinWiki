---
id: paper:2019nabankur-venue-paper
type: paper
title: "ReaxFF molecular dynamics simulations on the structure and dynamics of electrolyte water systems at ambient temperature (uncorrected proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:batteries-interfaces
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2019.109349"
year: 2019
authors:
  - "Nabankur Dasgupta"
  - "Yun Kyung Shin"
  - "Mark V. Fedkin"
  - "Adri C. T. van Duin"
venue: "Computational Materials Science"
pdf_sha256: "12426c9332f2b75babdac258327fca802000f98591436dfc67e46729b803aeee"
pdf_path: "papers/Nabankur_CompMatSci_electrolyte_ambient_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2019nabankur-venue-paper -->

## Summary

This slug registers an **uncorrected proof** PDF (`papers/Nabankur_CompMatSci_electrolyte_ambient_proof.pdf`) for the *Computational Materials Science* article (DOI `10.1016/j.commatsci.2019.109349`) reporting **ambient-temperature ReaxFF molecular dynamics** of **aqueous alkali halides**—**LiCl**, **NaCl**, and **KCl** at **1–5 M**—together with **pure water** baselines, using the **Fedkin** **electrolyte–water** parameterization line developed in the group’s broader **ReaxFF** ecosystem. **Adri C. T. van Duin** co-authorship connects the study to PSU **reactive electrolyte** practice and to downstream wiki links such as [[2019fedkin-j-phys-chem-development-reaxff]] and [[batteries-interfaces-reaxff]]. Scientifically, the work interrogates **structure** and **dynamics** signatures—**radial distribution functions**, **hydrogen-bond** statistics, **reorientational** correlation functions, **ion–water residence** behavior, and **diffusion** trends—as functions of **salt** identity and **concentration**, comparing selectively to **ab initio** and **non-reactive** references cited in the paper. Because **proof** PDFs can differ in **pagination**, **typesetting**, and **watermarking**, the **authoritative** narrative for this knowledge base is maintained on [[2019dasgupta-computationa-reaxff-molecular]], which tracks the **version-of-record** PDF bytes.

## Methods

This **page** tracks the **uncorrected** **proof** `papers/Nabankur_CompMatSci_electrolyte_ambient_proof.pdf` for the same **DOI** as [[2019dasgupta-computationa-reaxff-molecular]]. The **VOR** **MD** **protocol** on the **sibling** **page** uses **LAMMPS** with the **Fedkin-line** **ReaxFF** for **1–5 M** **LiCl/NaCl/KCl** in **3D** **periodic** **simulation** **cells**. **System / composition (VOR):** **~700** **H₂O** **molecules** **plus** **salt** **(order** **10³** **atoms** **in** **the** **electrolyte** **box**)** or** **~1000** **H₂O** **(pure** **water** **baseline**)**; **exact** **atom** **totals** **and** **ion** **counts** **per** **concentration** **are** **tabulated** on **[[2019dasgupta-computationa-reaxff-molecular]]**. **Sampling** **temperature** is **300 K** **(ambient** **NVT**)** after **minimization**/**heating**/**equilibration**, with **0.25** **fs** **timestep** and **0.5** **ns** **trajectories** and **analysis** on the **last** **200** **ps** (see **VOR** for **thermostat**/**damping** and full **RDF**/**H-bond**/**diffusivity** work-up). **Reproduce** all **settings** from **[[2019dasgupta-computationa-reaxff-molecular]]**, **not** from the **proof** **PDF** **alone**. **Mean** **isotropic** **pressure** **control** in **NPT**:** **N/A** on the **quoted** **ambient** **NVT** **protocol**; **Hydrostatic** **stress** **as** a **lumped** **control** is **N/A** **unless** the **VOR** **NPT** **stages** **exist** **(they** **do** **not** **in** **the** **NVT** **line** we mirror). **Barostat** during the **NVT** **hold**:** **N/A**. **External** **electric** **field**:** **N/A**. **Umbrella** / **metadynamics**:** **N/A** — **unbiased** **NVT** in the **parent** **work**.
## Findings

The published conclusions—fully summarized on [[2019dasgupta-computationa-reaxff-molecular]]—emphasize that **ReaxFF** reproduces key **structural** features of **alkali** **chloride** solutions in the modeled concentration window and rationalizes **transport** trends using **time-series** chemistry not accessible to fixed-charge models. The authors relate **species** fluctuations—including **metal–hydroxide**/**chloride** motifs—to **diffusivity** changes and argue that **increasing salt concentration** reduces **water** **self-diffusivity** without the strongest **ion-specific** splitting suggested by some simplified pictures. For this **proof-ingest** page, the wiki does not duplicate every **table** entry; readers should use the **VOR** PDF for **final** **edited** text, **pagination**, and **SI** cross-links. Battery- and interface-themed retrieval should still prefer [[2019dasgupta-computationa-reaxff-molecular]] for **stable** **locators** tying **transport** numbers to **Fedkin** **parameter** **choices** and **simulation** **protocol** details.

## Limitations

**Uncorrected proofs** are **non-authoritative** for **exact** **page** locators and may include **publisher** boilerplate; **hashes** and paths remain useful for **manifest** provenance but should not replace the **VOR** record for citations. **Sub-nanosecond** segments and **finite-size** effects inherit limitations discussed on the primary page.

## Relevance to group

**van Duin**-group electrolyte–water **ReaxFF** application built on **Fedkin** parameterization; duplicate ingest for proof provenance.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2019.109349](https://doi.org/10.1016/j.commatsci.2019.109349)
- Primary wiki: [[2019dasgupta-computationa-reaxff-molecular]]

## Reader notes (navigation)

- Batteries / interfaces context: [[batteries-interfaces-reaxff]], [[reaxff-family]]

## Related topics

- [[reaxff-family]]
- [[2019dasgupta-computationa-reaxff-molecular]]
