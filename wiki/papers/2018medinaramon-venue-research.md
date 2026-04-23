---
id: paper:2018medinaramon-venue-research
type: paper
title: Cathodic Corrosion at the Bismuth–Ionic Liquid Electrolyte Interface under
  Conditions for CO2 Reduction
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:batteries-electrochemistry
- domain:catalysis-surfaces
- domain:reaxff-lineage
- material:metal-surface
- method:dft-static
- method:reaxff
- task:experiment-integrated
- scale:atomistic
paper_keywords:
- keyword:batteries-interfaces
- keyword:reaxff-application
- keyword:dft-static
- keyword:aimd
candidate_tags: []
source_refs: []
doi: 10.1021/acs.chemmater.8b00050
year: 2018
authors:
- Jonnathan Medina-Ramos
- Weiwei Zhang
- Kichul Yoon
- Peng Bai
- Ashwin Chemburkar
- Wenjie Tang
- Abderrahman Atifi
- Sang Soo Lee
- Timothy T. Fister
- Brian J. Ingram
- Joel Rosenthal
- Matthew Neurock
- Adri C. T. van Duin
- Paul Fenter
venue: Chem. Mater.
pdf_sha256: c348e03ccaeeafda40af14874e3518b99d4fc88899430a455d3bf767aebcfa14
pdf_path: papers/MedinaRamon_ChemMat_2018_final.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018medinaramon-venue-research -->

In situ X-ray reflectivity on Bi(001) films in ionic-liquid electrolytes under cathodic bias is interpreted with ReaxFF MD and DFT to connect imidazolium adsorption, surface disorder, and bismuth dissolution pathways.

## Summary

Combines **in situ X-ray reflectivity** on **Bi(001)** thin films in **acetonitrile** with **BMIM**-based **ionic liquid** electrolytes under **cathodic** scans with **ReaxFF MD** and **DFT** to interpret **potential-driven** **thinning**, **roughening**, and **partial dissolution** of **Bi**. The modeling emphasizes stronger **imidazolium** binding vs **TBA⁺** as surfaces become more negative and connects **Bi···IL** motifs to **step-edge** dissolution at **intermediate** potentials. The electrochemical context is CO₂ reduction conditions where cathodic corrosion of Bi can compete with catalytic turnover, motivating interface-sensitive probes beyond cyclic voltammetry alone.

## Methods

- **Experiment:** **XR** tracking **Bi(001)** **Bragg** intensity and **domain** sizes vs **cyclic** potential in **Ar**- and **CO₂**-saturated electrolytes as reported (see **SI** figures referenced in the main text).
- **ReaxFF MD:** **Bi(001)** slabs with **IL cations** to capture **disorder** and **migration** trends at **negative** charge states.
- **DFT:** **Local bonding** and **dissolution** energetics for **Bi···[Im]⁺** motifs and **step** vs **terrace** pathways with **potential** estimates quoted in the article.
- **Integration:** Experimental potentials, electrolyte composition, and Bi film thickness ranges should be taken from Chem. Mater. when comparing XR trends to simulation snapshots.

### MD application (ReaxFF interface sampling)

**Engine / code:** **ReaxFF molecular dynamics** of **Bi(001)** slabs with **BMIM-class imidazolium** vs **TBA⁺** electrolyte motifs as described in the article; **N/A — specific MD engine name** not stated in the indexed abstract/excerpt—confirm in **Chem. Mater.** **Methods**/**SI** (`papers/MedinaRamon_ChemMat_2018_final.pdf`). **System & PBC:** **Bi** **slab supercells** with explicit **ionic-liquid** ions (**atom** counts, vacuum, and **PBC** freeze protocols in **Methods**). **Ensemble:** **NVT** thermal sampling for the **ReaxFF** interfacial runs unless **Methods** specify mixed **NVE**/**NVT** staging. **Timestep / duration / thermostat / barostat:** **N/A — not transcribed** in this excerpt-based note; import from the primary text. **Temperature:** **N/A — explicit MD thermostat K** not in the indexed excerpt—likely room-temperature sampling for the interface exploration, but verify in **PDF**. **Pressure:** **N/A — not used** for the classical MD discussion summarized here. **Electric field / applied bias in MD:** **N/A — classical ReaxFF** trajectories do not embed continuous **Poisson–Boltzmann** electrode models; potentials enter via **DFT** cluster models as quoted below. **Enhanced sampling:** **N/A — not indicated** in the abstract for **ReaxFF** runs.
## Findings

- First **cathodic** sweep reduces native **Bi₂O₃** to **Bi⁰**; subsequent sweeps show **large** **reflectivity** loss attributed to **thinning** and **lateral** **domain** shrinkage partly **recovered** on **anodic** return, with **cycling** increasing **damage**.
- **ReaxFF** predicts **greater disorder** and **Bi** **migration** with **[Im]⁺** vs **TBA⁺** under increasingly negative **surface** conditions.
- **DFT** suggests **step-edge** **dissolution** via **Bi···[Im]⁺** complexes at **−1.65 to −1.95 V** vs **Ag/AgCl**, while **terrace** desorption requires **more negative** potentials (~**−2.25 V**).
- Together, the XR and modeling sections argue that cation-specific adsorption steers where Bi atoms leave the surface during cathodic polarization, informing electrolyte design for stable Bi electrodes.

**Corpus honesty.** XR **percent** thinning/domain loss and **DFT** **potential** windows quoted above follow the **Chem. Mater.** abstract text; any figure-specific **layer electron density** details should be checked against the **PDF**/**SI** rather than this wiki alone.
## Limitations

- **Electrochemical potential** mapping to **classical MD** remains **approximate**; **DFT** provides **local** energetics but not **full** **electrolyte** dynamics at **long** times.
- CO₂ versus Ar saturation changes interfacial pH and buffering; the XR trends should be read with the electrolyte conditions tabulated in Chem. Mater. when extrapolating to other CO₂RR setups.

## Relevance to group

**Adri C. T. van Duin**-coauthored **electrified interface** study pairing **ReaxFF** with **DFT** and **XR**.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acs.chemmater.8b00050](https://doi.org/10.1021/acs.chemmater.8b00050)

## Reader notes (navigation)

- Canonical article note (VOR PDF): [[2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion]]

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
