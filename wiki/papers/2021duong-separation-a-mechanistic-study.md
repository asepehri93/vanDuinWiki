---
id: paper:2021duong-separation-a-mechanistic-study
type: paper
title: "Mechanistic study of pH effect on organic solvent nanofiltration using carboxylated covalent organic framework as a modeling and experimental platform"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - material:zeolite-porous
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:water-interfaces
  - keyword:berendsen-thermostat
  - keyword:npt-simulation
source_refs: []
doi: "10.1016/j.seppur.2021.120028"
year: 2021
authors:
  - "Phuoc H.H. Duong, Yun Kyung Shin, Valerie A. Kuehl, Mohammad M. Afroz, John O. Hoberg, Bruce Parkinson, Adri C.T. van Duin, Katie D. Li-Oakey"
venue: "Sep. Purif. Technol. 282 (2022) 120028"
pdf_sha256: "b018be409f491c53963c8d149d6997994856f4991483d66392dc59b17ba9979f"
pdf_path: "papers/Phuoc_Sep_Purif_Tech_COF_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021duong-separation-a-mechanistic-study -->

## Summary

This wiki entry documents the **same DOI** and science as **`[[2022duong-separation-a-mechanistic-study]]`** but points at an alternate corpus PDF (`papers/Phuoc_Sep_Purif_Tech_COF_2022.pdf`). The publication investigates **pH-dependent organic solvent nanofiltration** through a **carboxylated COF** selective layer using **methanol** feeds with **HCl**, **neutral**, and **NaOH** conditions. **ReaxFF MD** supplies molecular interpretations for **methanol self-diffusion**, **ion pairing**, **pore metrics**, and **electrostatic** shifts of **carboxylate** groups, while bench experiments report **permeance** and **dye rejection** for **Alcian Blue** and related probes.

## Methods

### MD application (ReaxFF)

- **Engine / code:** ReaxFF **molecular dynamics** on periodic **C-COF** slab supercells in **methanol** electrolytes with **HCl** / **NaOH** concentration sweeps (Section 2.3 in `pdf_path`).
- **System & composition:** **C-COF** + **methanol** + electrolyte **ions** with **HCl**/**NaOH** pH sweeps; full **atom** counts in `pdf_path`.
- **PBC / boundaries:** **Periodic** in-plane **PBC** slab supercells as in `pdf_path`.
- **Ensemble, timestep, duration, thermostat, barostat:** **0.25 fs** integration; **NPT** equilibration at **300 K** and **0 atm** reference **pressure** with **Berendsen** thermostat and barostat (**100 fs** / **1000 fs** damping per the protocol); **NVT** production **RMD** **200 ps** in the documented protocol. Self-diffusion and **pore**/**dye** solvation analyses: `pdf_path`.
- **Shear, electric field, MSST, umbrella:** **N/A** unless the **PDF**/SI states otherwise. ReaxFF **Coulomb** and **QEq** schedules: `pdf_path`.

### Experiments (OSN, rejection, permeance)

Membranes pair a **carboxylated COF** selective layer with an **anodized aluminum oxide** support (**~800 nm** selective thickness, **~20 nm** support pores) following prior synthesis routes cited in the paper. **Dead-end** filtration at **1 bar** transmembrane **pressure** and **25 °C** on **2.5 cm** discs, discarding initial permeate volumes (**10–15 mL**) before sampling. **Permeance** per the article; **rejection** via **UV–visible** dye assays. For figure-stable protocol locators, prefer **`[[2022duong-separation-a-mechanistic-study]]`** (same **DOI**, alternate **PDF** path on this page).

### Force-field training in this work

- **N/A** for a de novo ReaxFF training paper: the work applies a published ReaxFF for the COF/methanol/ion chemistry, as cited in `pdf_path`.

## Findings

**Methanol permeance** decreases when either acid or base is added relative to less perturbed feeds, while **Alcian Blue rejection** increases from about **23% at pH 2.2** to about **98% at pH 10.1**. Atomistic models show **only modest** changes in average **pore dimensions**, implicating **solvated ion** structures and **membrane charge** as dominant knobs: larger **methanol–ion** clusters retard diffusion, and **deprotonated carboxylates** strengthen **dye–framework** interactions that boost **selectivity**. For stable locators and figure alignment, prefer the primary curation on **`[[2022duong-separation-a-mechanistic-study]]`** unless this PDF path is required for manifest provenance. Side-by-side comparison of the two PDFs is recommended after major corpus updates because OCR or compression differences can shift pagination even when scientific content matches. When citing **transport** coefficients derived from **MD**, note that **finite** **system** **sizes** and **short** **production** windows affect **error bars** on **diffusivity**, so the paper’s **experimental** **permeance** remains the **ground-truth** check for **engineering** **predictions**.

## Limitations

ReaxFF charges and sampling length constrain quantitative pH behavior in organic media; experiments use simplified dye cocktails versus industrial feeds.

## Relevance to group

Adri C. T. van Duin is co-author; ReaxFF MD supplies molecular interpretation for COF OSN pH effects.

## Citations and evidence anchors

## Related topics

- [[reaxff-family]]
