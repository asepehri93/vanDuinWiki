---
id: paper:2014muser-venue-paper
type: paper
title: "Redox reactions with empirical potentials: Atomistic battery discharge simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - method:classical-md
  - task:method-development
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:charge-equilibration
  - keyword:method-development
  - keyword:batteries-interfaces
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.1063/1.4817772"
year: 2013
authors:
  - "Wolf B. Dapp"
  - "Martin H. Müser"
venue: "J. Chem. Phys. 139, 064106 (2013)"
pdf_sha256: "9849d2d0b8132f06d93378f84a8f6753c75c24942ecf50aec1d2eac5c685ed3b"
pdf_path: "papers/Others/Muser_JCP_2013_Redox_EFF.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2014muser-venue-paper -->

## Summary

Empirical potentials with fixed integer oxidation states cannot describe redox reactions where electrons transfer between atoms or between electrodes and electrolyte. This Journal of Chemical Physics article introduces **redox split-charge equilibration (redoxSQE)**, extending split-charge electrostatic models so atoms carry **discrete ionization states** alongside **bonded partial charges**, enabling redox chemistry within a classical Hamiltonian suitable for large-scale molecular dynamics. The wiki filename uses a `2014…` stem while the publication year in the journal is **2013**; front matter follows the **published** year. The authors demonstrate **nano-battery discharge** trajectories that qualitatively reproduce macroscopic behaviors—capacity versus temperature, capacity versus discharge rate, and performance fade on recharge—in minimalist atomistic cells meant as proof-of-concept rather than commercial cell models. The Dapp–Müser framework predates modern machine-learning interatomic potentials yet remains a conceptual bridge between fixed-charge electrolyte models and explicit electron transfer.

## Methods

Grounding: **`papers/Others/Muser_JCP_2013_Redox_EFF.pdf`** (J. Chem. Phys. **139**, 064106, **2013**; DOI in front matter) and the partial header/abstract in `normalized/extracts/2014muser-venue-paper_p1-2.txt`.

### Method development (redoxSQE + atomistic “nano-battery”)

- **Redox split-charge equilibration (redoxSQE):** assigns a **discrete ionization state** to each atom while still exchanging **partial charges** across bonds; **integer charge** swaps implement **redox** moves within an **empirical** Hamiltonian suitable for **large-scale molecular dynamics** (abstract in extract).

### 1 — MD application (atomistic dynamics)

The abstract emphasizes **proof-of-concept** **nano-battery** **discharge** trajectories rather than tabulating a full production **MD** protocol in the indexed pages.

- **Engine / code:** **Molecular dynamics** is the stated vehicle for **nano-battery** studies (abstract); **N/A — specific software** not in `2014muser-venue-paper_p1-2.txt`.
- **System size & composition:** **Nano-battery** cells partition **electrode**/**electrolyte** regions (abstract); **N/A — atom counts** not in the indexed excerpt.
- **Boundaries / periodicity:** **N/A — not stated** in the indexed excerpt.
- **Ensemble:** Canonical MD ensembles (NVE, NVT, NPT) are not identified in the indexed excerpt; read JCP 139, 064106 for the actual choice.
- **Timestep / duration / thermostat / barostat:** **N/A — not stated** in the indexed excerpt.
- **Temperature:** **Abstract** reports **capacity** depends on **temperature** (qualitative trend); numerical thermostat targets **N/A — not in excerpt**.
- **Pressure:** **N/A — not stated.**
- **Electric field:** **N/A — not stated** as an applied bias in the indexed abstract layer.
- **Replica / enhanced sampling:** **N/A — not stated.**

### Implementation detail pointer

Functional forms, constraints, integrators, and parameter tables are in **JCP** **139**, 064106—this wiki does not duplicate those equations.

### 2 — Force-field training

**N/A —** this article introduces an **electrostatic/redox** **model**, not a **bonded force-field** reparameterization in the **ReaxFF** sense.

## Findings

### Outcomes and mechanisms

With **redoxSQE**, the authors study **discharge** of a **nano-battery** and report it **qualitatively reproduces** generic macroscopic behaviors: **capacity** depends on **temperature** and **discharge rate**, and **performance** degrades on **recharge** (abstract).

### Comparisons

The framing contrasts a **self-consistent atomistic battery** picture with traditional **mesoscale** battery models and with standard **MD** approaches that cannot maintain electrode **chemical potential** differences (introduction themes in extract).

### Sensitivity

**Temperature** and **discharge rate** appear as explicit levers affecting **capacity** in the abstract’s qualitative claims.

### Limitations and corpus honesty

The abstract positions the work as **first steps** toward whole-cell atomistic modeling, not quantitative reproduction of commercial cells. Indexed text is **partial** relative to full **Methods**; cite **`papers/Others/Muser_JCP_2013_Redox_EFF.pdf`** for reproducible numerical protocols.

## Limitations

Not a ReaxFF paper; highly stylized geometry and parameter set. Transferability to specific chemistries requires reparameterization and validation against experiment or electronic-structure benchmarks. RedoxSQE parameter sets must be reconstructed from the original article before reuse in new electrolyte chemistries.

## Relevance to group

Electrode–electrolyte modeling context alongside ReaxFF battery entries in the corpus.

## Citations and evidence anchors

- https://doi.org/10.1063/1.4817772 — J. Chem. Phys. **139**, 064106 (2013).

## Related topics

- [[batteries-interfaces-reaxff]]
