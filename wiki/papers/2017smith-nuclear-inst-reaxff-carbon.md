---
id: paper:2017smith-nuclear-inst-reaxff-carbon
type: paper
title: "A ReaXFF carbon potential for radiation damage studies"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:carbon-hydrocarbon
  - method:reaxff
  - material:graphene-carbon-nano
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:graphene-carbon
candidate_tags: []
source_refs: []
doi: "10.1016/j.nimb.2016.11.007"
year: 2017
authors:
  - "Roger Smith"
  - "Kenny Jolley"
  - "Chris Latham"
  - "Malcolm Heggie"
  - "Adri van Duin"
  - "Diana van Duin"
  - "Houzheng Wu"
venue: "Nuclear Instruments and Methods in Physics Research B 393, 49–53 (2017)"
pdf_sha256: "659ebeff5fc21df16f1aa8d1be073a227a7455850d17565b092fc06676f09ce6"
pdf_path: "papers/Smith_NucInstMethPhysicsResB_Carbon_potential_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017smith-nuclear-inst-reaxff-carbon -->

## Summary

Molecular dynamics of collision cascades in graphite has relied for decades on empirical bond-order potentials, but comparisons to density functional theory showed mismatches in predicted defect populations and transition pathways. This article refits a ReaxFF carbon model to reproduce LDA reference formation energies and pathways among interstitial, vacancy, di-interstitial, and divacancy defects in graphite, including the spiro interstitial and Stone–Wales (Dienes) motifs emphasized in prior DFT compilations. Training augments existing hydrocarbon and fullerene datasets used for the broader ReaxFF carbon line. Elastic constants are acknowledged as less accurate than point-defect properties: \(c_{33}\) is too high and \(c_{44}\) too low versus experiment. Preliminary low-energy cascade simulations produce point-defect motifs consistent with ab initio expectations.

## Methods

### 1 — MD application (atomistic dynamics)

**ReaxFF molecular dynamics** is used for **preliminary low-energy collision cascades** in **graphite** to check that **defect populations** after impact trend toward **LDA-consistent** **interstitial** and **vacancy** motifs following the refit (*Nucl. Instrum. Methods Phys. Res. B* **393**, 49–53). The article frames these cascade segments as **scoping** studies rather than exhaustive **high-energy** **damage** statistics.

- **Engine / code:** **ReaxFF** reactive MD as implemented in the article (confirm package and input decks in **`pdf_path`**).
- **System size & composition:** **Graphite** supercells for **cascade** tests; explicit **atom counts** and **PKA energies** are **N/A** on the indexed excerpt.
- **Boundaries / periodicity:** **N/A** — **PBC** vs fixed boundaries for cascades not stated in the indexed excerpt.
- **Ensemble:** **N/A** — **NVE/NVT** staging for cascade segments not stated in the indexed excerpt.
- **Timestep:** **N/A** — **Δt (fs)** not stated in the indexed excerpt.
- **Duration / stages:** **N/A** — thermalization vs cascade segment lengths not stated in the indexed excerpt.
- **Thermostat:** **N/A** — not stated in the indexed excerpt (cascade protocols often use **NVE** + boundary thermostats; confirm in PDF).
- **Barostat:** **N/A** — **NPT** not indicated for cascade checks on indexed pages.
- **Temperature:** **N/A** — initial lattice **T** / thermostat targets not stated in the indexed excerpt.
- **Pressure:** **N/A** — not stated for cascade cells in the indexed excerpt.
- **Electric field:** **N/A** — not used.
- **Replica / enhanced sampling:** **N/A** — direct cascade **MD**.

### 2 — Force-field training

**ReaxFF** parameters for **carbon** are **reoptimized** against **LDA** **formation energies**, **barriers**, and **reaction pathways** for **graphite** defects—including **spiro**, **Stone–Wales (Dienes)**, **di-interstitial**, and **divacancy** sequences—using the **Latham *et al.*** **QM** database cited in the paper, **merged** with the existing **hydrocarbon/fullerene** **ReaxFF** training lineage so radiolytic and **organic** chemistry can coexist in one parameter set.

### 3 — Static QM / DFT-only

**LDA** **QM** supplies **static** **reference energies** and **pathway** data for the fit; **on-the-fly AIMD** is **not** the reported production tool for cascades.

### 4 — Review / non-simulation framing

**N/A** — primary research article.

## Findings

### Outcomes and mechanisms

The refit **ReaxFF** tracks many **defect formation energies** and **migration/barrier** sequences from **LDA** more closely than **empirical bond-order** alternatives highlighted in the introduction, while retaining compatibility with the broader **hydrocarbon** reactive **carbon** line.

### Comparisons

**Elastic constants** remain less accurate than **point-defect** properties: **\(c_{33}\)** is **too high** and **\(c_{44}\)** **too low** versus **experiment** as acknowledged in the article—so the potential should not be used as a high-fidelity **phonon** model without further work.

### Sensitivity / design levers

Because training **extends** rather than **replaces** **hydrocarbon/fullerene** datasets, users can combine **radiation damage** with **chemical** reactivity in one framework—contrasting with potentials fit **only** to **elastic** data.

### Limitations, outlook, and corpus honesty

**High-energy** cascades and **cumulative dose** statistics need broader validation than the **preliminary** runs summarized here. **Numerical** **cascade** settings and **defect** counts should be taken from **`pdf_path`**, not inferred from this short wiki note.

## Limitations

High-energy cascade regimes and cumulative dose effects may require additional validation; elastic property errors may couple into thermal transport if misused.

## Corpus notes

Because this potential extends hydrocarbon datasets, workflows that combine radiolytic chemistry with hydrocarbon adsorption should document which parameter subsets dominate energy errors—especially when migrating from older Tersoff or AIREBO baselines.

The publisher PDF is open access under CC BY, which simplifies redistribution of figures in internal presentations provided attribution is preserved.

## Relevance to group

RxFF Consulting / van Duin co-authorship connects the reactive carbon line to **nuclear materials** and radiation damage applications.

## Citations and evidence anchors

- DOI: [10.1016/j.nimb.2016.11.007](https://doi.org/10.1016/j.nimb.2016.11.007)

## Related topics

- [[reaxff-family]]
