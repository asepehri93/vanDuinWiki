---
id: paper:2016osti-venue-research
type: paper
title: "Effect of metal ion intercalation on the structure of MXene and water dynamics on its internal surfaces (proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:water-interfaces
  - keyword:validation-experiment
  - keyword:2d-materials
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.6b01490"
year: 2016
authors:
  - "Naresh C. Osti"
  - "Michael Naguib"
  - "Alireza Ostadhossein"
  - "Yu Xie"
  - "Paul R. C. Kent"
  - "Boris Dyatkin"
  - "Gernot Rother"
  - "William T. Heller"
  - "Adri C. T. van Duin"
  - "Yury Gogotsi"
  - "Eugene Mamontov"
venue: "ACS Appl. Mater. Interfaces (author proof PDF)"
pdf_sha256: "94464791710812be54c0909b2f2ba5fc1a9ff01599a95f8ac28e6911dc253f99"
pdf_path: "papers/Osti_ACS_AMI_Water_Mxene_proof_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016osti-venue-research -->

## Summary

MXene electrodes intercalate ions and water between exfoliated transition-metal carbide layers, coupling electrochemical performance to nanoconfined hydration dynamics and interlayer structural coherence. Hydroxyl-, oxygen-, and fluorine-terminated surfaces make MXenes hydrophilic, so interlayer water and cations can strongly affect electrochemical response in realistic humid environments. This ACS Applied Materials & Interfaces letter combines laboratory X-ray diffraction, small-angle neutron scattering, and quasielastic neutron scattering on Ti₃C₂Tₓ MXene with ReaxFF molecular dynamics to interrogate how potassium-ion intercalation alters c-axis stacking, morphological homogeneity, and water mobility inside galleries. After vacuum annealing at 110 °C, the published letter reports layer-to-layer repeat distances near **19.64 Å** for pristine MXene and near **24.35 Å** for K⁺-intercalated material, with a sharper 0001-like diffraction peak for the intercalated case interpreted as larger and/or more ordered stacked domains. Scanning electron microscopy images in the supporting material are cited as consistent with more uniform nanoscale stacking after intercalation. Quasielastic neutron scattering and simulations both indicate orders-of-magnitude reduction in confined water self-diffusion upon K⁺ intercalation, which the authors connect to improved environmental stability under changing humidity. This wiki slug records an author-proof PDF; **`[[2016osti-venue-am6b01490]]`** should be used for version-of-record pagination and figures when both files are available.

## Methods

Author-proof PDF for the MXene + confined-water letter curated on [[2016osti-venue-am6b01490]] (DOI `10.1021/acsami.6b01490`). Experiments match the issue letter (post-anneal \(c\)-axis repeats near **19.64 Å** versus **24.35 Å** after **110 °C** drying, plus SANS/QENS as published). Companion **ReaxFF** **molecular dynamics** in **LAMMPS** uses the **SI**-documented **0.25 fs** **timestep**, **NPT** relaxations (**10 ps**, **300 K**, **0.1 MPa**) between GCMC moves, and **1.5 ns NVT** segments for confined-water **MSD**/diffusivity comparisons—see [[2016osti-venue-microsoft-word]] for the ASCII tables. **Periodic** hydrated **supercells** follow the same construction rules as the issue **PDF**. Do not read **thermostat** coupling constants from this proof layout; use the SI LAMMPS deck. **N/A — new force-field training or standalone static QM** beyond the published parametrization story.
## Findings

**K\(^+\) intercalation** increases **interlayer spacing**, yields **sharper** **000ℓ** diffraction than **pristine** MXene after comparable drying/annealing, and is interpreted as **larger, more homogeneous** stacked domains (**SEM** motifs in **SI** support uniformity narratives in the letter). **SANS** trends align with more homogeneous swelling. **QENS** and **ReaxFF** both report **strongly suppressed** interlayer **water** mobility upon intercalation (authors quote ~**two orders of magnitude** lower **self-diffusion** in MD for the intercalated case relative to pristine in the published comparison). Together, the data argue that **cation** and **water** content tune both **structural coherence** and **nanoconfined hydration** dynamics—use **`[[2016osti-venue-am6b01490]]`** for exact factors and discussion of **humidity** stability.

**Comparisons and sensitivity.** **Compared** to pristine MXene, intercalated samples show sharper diffraction, distinct SANS slopes, and slower QENS relaxation; **temperature** history (**110 °C** vacuum anneal) is a shared experimental knob between batches.

**Limitations and corpus honesty.** Proof PDFs can differ cosmetically from the **version-of-record**; cite [[2016osti-venue-am6b01490]] for authoritative figures. **Future work** implied by the letter—broader humidity cycling and additional cations—is not expanded on this duplicate page.

## Limitations

Proof PDFs may exhibit editorial markup and layout differences; cite the issue PDF for authoritative figure labels. Force-field models of interfacial water cannot capture all quantum tunneling or proton-transfer effects relevant at the lowest temperatures.

## Relevance to group

The entry documents duplicate corpus bytes for a van Duin-coauthored ReaxFF plus neutron-scattering MXene study, routing operators to the canonical slug for DOI `10.1021/acsami.6b01490`.

## MAS / retrieval notes

Prefer **`[[2016osti-venue-am6b01490]]`** for stable figure numbering; when answering about intercalation-induced water slowdown, cite both QENS observables and ReaxFF diffusion metrics from the parent article rather than this proof PDF alone. Keywords `water-interfaces`, `2d-materials`, and `galley-or-proof-pdf` should surface this page only with the duplicate-ingest warning. Automated pipelines should not merge duplicate manifests without reconciling `pdf_sha256` values across proof and issue files.

## Citations and evidence anchors

- DOI: [10.1021/acsami.6b01490](https://doi.org/10.1021/acsami.6b01490)

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
