---
id: paper:2017fa-venue-acam
type: paper
title: "Investigation of N transfer during coal pyrolysis and combustion by using ReaxFF molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:combustion
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: ""
year: 2017
authors:
  - "Mo Zheng"
  - "Xiaoxia Li"
  - "Li Guo"
venue: "2017 International Conference on Coal Science & Technology / 2017 Australia-China Symposium on Energy (Beijing)"
pdf_sha256: "f464c270f65bc3010de03aab5b980f8ff9345bec50287fca5698e38f01693a01"
pdf_path: "papers/ReaxFF_others/Chinese_Coal_Abstracts/Investigation of N Transfer during Coal Pyrolysis and Combustion by Using ReaxFF Molecular Dynamics.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017fa-venue-acam -->

## Summary

**ReaxFF MD** on a **~26k-atom** coal model with **diverse nitrogen functionalities** follows **N partitioning** during **pyrolysis** and **combustion**. The abstract reports that **>65% N** remains in **char** after pyrolysis, **~25%** enters **tar**, and combustion with **10,000 O2** molecules yields trends for **NH3, HCN, HNCO, NO** and radicals (**CN, NH2/NH, COxN, HOxN**), with **pyrrolic-N** highlighted as especially active. The extended abstract ties **fuel-N** tracking to **NOx** control in **clean coal** conversion: because experiments struggle to resolve **radical** populations during **fast** pyrolysis and **combustion**, **ReaxFF** trajectories are presented as a complement for **atomic-scale** **N** migration and **gas-phase** product evolution.

## Methods

**MD application (ReaxFF).** **Reactive MD** uses **GMD-Reax** (GPU-oriented **ReaxFF** implementation named in the conference PDF) with the **Mattsson** **coal/char** **ReaxFF** parameterization referenced there. **Coal supercell:** stoichiometry **C₁₄₁₈₈H₁₁₄₆₁N₁₂₂O₆₅₈S₅₈** (**26,487 atoms**) built from a **Liulin** coal skeleton; **N** is partitioned among **pyrrolic**, **pyridinic**, **quaternary**, and **–NH₂** motifs using **XPS**-motivated fractions quoted in the text. **Equilibration:** both **pyrolysis** and **combustion** geometries are **NPT**-relaxed at **500 K**, **1 atm**. **Combustion setup:** a **~204.6 Å** cubic **PBC** cell containing the coal model plus **10,000 O₂** molecules. **Heating ramps:** **500–2500 K** (**pyrolysis**) and **1000–3000 K** (**combustion**) at **2 K/ps**; **velocity–Verlet** integration with **Δt = 0.25 fs** and a **Berendsen** thermostat (as stated in the PDF). **Reaction mining** uses **VARxMD**.

**Force-field training** and **standalone static QM** are **N/A** for the headline workflow.

**Barostat** details after **500 K** equilibration, **total simulated time** per ramp stage, **post-ramp production** segments, **pyrolysis-only** cell vectors, **electric fields**, and **replica exchange** are **not transcribed numerically** from the indexed conference pages—see the **PDF** for any additional timing tables.

## Findings

**Pyrolysis partitioning:** trajectory analysis reports **>65%** of **N** retained in **char** and **~25%** migrating to **tar**-range fragments (percentages as stated in the abstract). **Temperature trends:** **N** in **C₄₀⁺** fragments changes slowly **500–1300 K**, then **redistributes rapidly ~1300–1900 K** with growth of **N** in **C₅–C₄₀** species (qualitative description in the PDF). **Combustion gases:** tracks **NH₃, HCN, HNCO, NO** and radicals/intermediates (**CN**, **NH₂/NH**, **COₓN**, **HOₓN**) with only minor **N₂**, **NO₂**, **N₂O** generation in the summarized runs. **Mechanism hooks:** **NO** tied to **NH** oxidation and subsequent **HOₓN**/**COₓN** pathways; **HNCO** feeds **COₓN** species that influence **NOₓ** evolution; **pyrrolic-N** highlighted as most **active**, with **O₂** **H-abstraction** on **N–H** promoting combustion chemistry.

## Limitations

**Conference proceedings extended abstract** (no **DOI** in front matter); claims should be checked against any **peer-reviewed** follow-on publication. **Hardware/runtime** remarks in the PDF are **illustrative**, not transferable performance benchmarks.

## Relevance to group

Corpus **coal + ReaxFF** snapshot complementary to **combustion** and **hydrocarbon** ReaxFF applications.

## Citations and evidence anchors

- No DOI in front matter; cite **conference abstract PDF** path above.

## Related topics

- [[reaxff-family]]
