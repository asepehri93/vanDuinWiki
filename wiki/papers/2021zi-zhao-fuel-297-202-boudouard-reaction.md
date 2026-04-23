---
id: paper:2021zi-zhao-fuel-297-202-boudouard-reaction
type: paper
title: "Boudouard reaction accompanied by graphitization of wrinkled carbon layers in coke gasification: A theoretical insight into the classical understanding"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:carbon-hydrocarbon
  - method:reaxff
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:thermal-decomposition
  - keyword:combustion
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2021.120747"
year: 2021
authors:
  - "Ding Zi-Zhao"
  - "Sun Zhang"
  - "Lu Qiang"
  - "Dou Ming-Hui"
  - "Guo Rui"
  - "Wang Jie-Ping"
  - "Li Guang-Yue"
  - "Liang Ying-Hua"
venue: "Fuel"
pdf_sha256: "4a5e7cedb87f41e3c3bf1381b244d8abd2d997e3b2e253f4b6c6e8dcc9d5e3fc"
pdf_path: "papers/ReaxFF_others/ZiZhao_Fuel_2021_graphene_wrinkles_Bouduard.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2021zi-zhao-fuel-297-202-boudouard-reaction -->

## Summary

Zi-Zhao et al. study coke gasification by CO2 as a coupled chemical-structural process rather than only a bulk kinetic fit. The article combines particulate coke reaction experiments with X-ray diffraction (XRD) and X-ray photoelectron spectroscopy (XPS), reactive molecular dynamics (ReaxFF), and static DFT reaction-path energetics. In the abstract and early introduction, the central claim is that Boudouard chemistry is accompanied by reconstruction of wrinkled carbon layers in coke, and this reconstruction is linked to both carbon monoxide formation and strength degradation of the coke residue.

The experimental characterization trend emphasized in the paper is an increase of graphitic carbon fraction during reaction together with lower residue strength. The modeling side is used to interpret that trend: defects on wrinkled layers are treated as key intermediates in reconstruction and flattening, and carbon atoms at highly wrinkled sites are described as more reactive toward CO2 than less distorted sites. The DFT component then provides elementary-step energies and barriers to identify which oxidation step most strongly controls rate.

A key motivation in the introduction is inconsistency among published activation energies for coke gasification (the extract cites a broad spread). The paper frames this inconsistency as a sign that classical kinetic summaries can miss microstructural state effects, especially when wrinkled stacking-fault carbon layers are represented poorly. The overall contribution is therefore mechanistic: explain why different coke structures can show different apparent activation behavior, while tying that explanation to observable graphitization and strength changes.

## Methods

### 1 — MD application (reactive MD)

- Engine / code: Reactive MD with ReaxFF is stated; specific executable package name is not present in the local p1-2 extract (`N/A — not stated in extract`).
- System size and composition: The introduction describes a coke model based on wrinkled stacking-fault carbon layers and discusses comparison to earlier polycyclic/edge-rich representations.
- Boundaries / periodicity: `N/A — not stated in extract`.
- Ensemble: N/A — the MD ensemble (for example NVE, NVT, or NPT) is not reported in the local extract text.
- Timestep: `N/A — not stated in extract`.
- Duration / stages: `N/A — production or equilibration duration not reported in extract`.
- Thermostat: `N/A — not stated in extract`.
- Barostat: `N/A — not stated in extract`.
- Temperature: `N/A — no explicit simulation temperature values in extract; introduction refers only to high-temperature gasification context`.
- Pressure: `N/A — no simulation pressure value in extract`.
- Electric field: `N/A — not used/reported in extract context`.
- Replica or enhanced sampling: `N/A — not reported in extract`.

### 2 — Force-field training

- Parent FF / elements: ReaxFF is used for reactive carbon/oxygen gasification chemistry; this page does not assert a new parameterization from the local extract.
- QM reference for fitting: `N/A — no force-field fitting workflow is described in the extract`.
- Training set and targets: `N/A — not a training-focused report in the extract text`.
- Optimization algorithm/software: `N/A — not reported`.
- Reference data used in fitting: `N/A — not reported`.

### 3 — Static QM / DFT

- Functional: `N/A — not specified in the local extract`.
- Dispersion treatment: `N/A — not specified in the local extract`.
- Basis: `N/A — not specified in the local extract`.
- k-sampling: `N/A — not specified in the local extract`.
- Structures / pathways: DFT is used to evaluate elementary oxidation reactions relevant to CO2 attack on the carbon layer and to compute associated barriers.
- Properties computed: Reaction energies and potential barriers are reported, with the highest barrier used to identify the rate-controlling step in the proposed mechanism.

### 4 — Experiments and characterization

Particulate coke gasification experiments are paired with XRD and XPS characterization. The abstract-level observation is that graphitic-carbon proportion increases during reaction while coke residue strength decreases. This experimental trend is the anchor used to compare and interpret the reactive-MD reconstruction picture.

## Findings

The article’s main outcome is a mechanistic bridge between observed coke-strength loss and atomistic carbon-layer evolution during CO2 gasification. Instead of treating graphitization as a passive byproduct, the authors present it as part of the reaction pathway: wrinkled-layer defects participate in reconstruction, and flattening accompanies gasification progress.

The abstract reports that ReaxFF MD trends correspond well with XRD/XPS observations, and that a principal CO formation path is coupled to reconstruction of the carbon matrix. This supports a model where local topology of carbon sites matters for reactivity. In particular, more strongly wrinkled carbon sites are described as reacting more readily with CO2 and evolving toward flatter post-reaction structures.

From DFT energetics, one oxidation step shows the highest potential barrier and is interpreted as the rate-controlling step. That placement is important for reconciling sample-dependent gasification behavior: if structurally distinct coke samples expose different populations of reactive wrinkles/defects, they can exhibit different apparent activation energies in bulk measurements.

The introduction further situates this against prior kinetic literature, noting a wide range of reported activation energies in coke-CO2 gasification and arguing that purely classical models may miss key structural state variables. The paper’s evidence-backed claim is not that classical kinetics are useless, but that microstructure-sensitive mechanistic detail is needed for consistent interpretation.

Comparisons to experiment are qualitative in the local extract (graphitic fraction and strength trend alignment), while quantitative protocol details and full numerical tables require the complete article and supporting information. Accordingly, this page keeps conclusions at the confidence level supported by the available local text: coupling between Boudouard chemistry, wrinkled-layer reconstruction/flattening, and strength-relevant graphitization.

## Limitations

This local curation is grounded in the p1-2 extract and metadata; explicit MD control parameters (ensemble, duration, thermostat, and temperature values) are not available in that extract and are therefore marked `N/A` rather than inferred. For quantitative reuse (rate prediction, transfer to other coke chemistries, or benchmark reproduction), consult the full *Fuel* paper and SI to retrieve complete simulation settings and DFT setup details.

## Reader notes (navigation)

- [[reaxff-family]]
