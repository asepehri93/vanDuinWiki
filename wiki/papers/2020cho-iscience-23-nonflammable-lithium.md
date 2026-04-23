---
id: paper:2020cho-iscience-23-nonflammable-lithium
type: paper
title: "Nonflammable Lithium Metal Full Cells with Ultra-high Energy Density Based on Coordinated Carbonate Electrolytes"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - material:li-metal-anode
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.isci.2020.100844"
year: 2020
authors:
  - "Sung-Ju Cho"
  - "Dae-Eun Yu"
  - "Travis P. Pollard"
  - "Hyunseok Moon"
  - "Minchul Jang"
  - "Oleg Borodin"
  - "Sang-Young Lee"
venue: "iScience"
pdf_sha256: "c15c7a495be0dfd06eba25a0bfdc795623e3d546a9c9c0124e92783f84de5fcc"
pdf_path: "papers/Others/Noflammable_Li_battery_iScience_2020_Borodin_et_al.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020cho-iscience-23-nonflammable-lithium -->

Highly concentrated **LiFSI** in **PC/FEC** yields coordinated **Li\(^+\)–FSI\(^-\)–solvent** clusters that stabilize **Li-metal** and **NCM811** interfaces in **thin-Li** full cells with **high reported energy density** and **nonflammability**.

## Summary

This iScience study targets a practical lithium-metal full-cell configuration that combines **thin lithium metal** with a **high-capacity/high-voltage NCM811** cathode. The central claim is that electrolyte coordination chemistry, not only electrode architecture, determines whether this combination can be both high-energy and safer than conventional flammable carbonate systems. The authors formulate concentrated **LiFSI in PC/FEC** electrolytes and report that an **optimal 4 M** composition forms a distinctive coordinated cluster environment around Li\(^+\), FSI\(^-\), and carbonate solvent molecules.

At the level exposed in the local extract (title page, highlights, summary, and introduction opening), the paper frames a long-standing tradeoff: ethers can improve Li-metal compatibility but are oxidation-limited and flammable, whereas conventional carbonates are better for high-voltage cathodes but usually unstable against Li metal. The authors position concentrated coordinated carbonates as an attempt to bridge that gap for demanding full-cell conditions rather than idealized half-cell demonstrations.

The reported full-cell setup is explicitly stringent: **35 µm Li metal**, **4.8 mAh cm\(^{-2}\)** NCM811 loading, **4.6 V** charge cutoff, and **0.83** anode excess capacity relative to cathode. Under those conditions, the abstract reports high cell-level energy metrics and nonflammability outcomes. The paper narrative in the extract also emphasizes that this work is meant to move beyond thick-Li/low-loading configurations that can overstate practical promise. Within that framing, interphase stability on **both** electrodes (SEI on Li, CEI on NCM811) is treated as the mechanism linking coordinated electrolyte structure to cycling reliability.

## Methods

### 4 — Experimental electrochemistry study (non-MD / non-DFT primary engine)

- **Scope and design objective:** Build and test nonflammable, high-energy **Li metal full cells** by coupling **thin Li** to **NCM811** and tuning electrolyte coordination via salt concentration in **PC/FEC** (extract summary + highlights).
- **Electrolyte space:** **LiFSI in PC/FEC** mixtures, with **4 M LiFSI** identified as the optimal concentration in the abstract summary.
- **Cell configuration emphasized in the extract:** **35 µm Li**, **4.8 mAh cm\(^{-2}\)** NCM811, **4.6 V** charge cutoff, and **0.83** anode excess capacity.
- **Measured outcomes (as stated in extract):** electrochemical performance in full-cell cycling context, interface-stability conclusions, and flammability behavior.
- **Analytical methods:** The extract indicates coordination/interphase analysis is performed, but instrument-by-instrument procedural details are not fully present on p1-2; see full PDF/SI for exact protocol settings and data-processing choices.

### 1 — MD application

N/A — this paper is not presented as a molecular-dynamics trajectory study in the local extract.

### 2 — Force-field training

N/A — no reactive/classical force-field parameter fitting is reported as the main method in the extract.

### 3 — Static QM / DFT-only

N/A — no standalone DFT workflow is described as the core evidence stream in the extract opening pages.

## Findings

- **Primary outcome:** The **4 M LiFSI** coordinated carbonate electrolyte is reported to provide a coordination structure associated with stable interphases on both Li metal and NCM811, enabling full-cell operation under demanding areal loading and voltage conditions.
- **Energy/safety envelope in reported configuration:** For the highlighted thin-Li/high-loading NCM811 design, the abstract reports **679 Wh kg\(^{-1}\)** and **1024 Wh L\(^{-1}\)** cell-level values together with nonflammability behavior.
- **Cross-system performance note:** The abstract also reports **~85.3% capacity retention after 400 cycles** for a Li||LiCoO\(_2\) full-cell example, supporting the argument that the electrolyte concept is not restricted to a single cathode chemistry.
- **Mechanistic interpretation in article framing:** The proposed mechanism is not just bulk conductivity, but **coordination-controlled interphase chemistry** (SEI/CEI) that suppresses failure modes of dilute carbonate electrolytes in Li-metal full cells.
- **Comparative context:** The introduction framing explicitly contrasts this approach against prior studies that used thicker Li and lower areal capacities, which can reduce practical relevance of quoted energy metrics.
- **Corpus honesty:** Detailed cycle protocols, full flammability test definitions, and complete interface diagnostics are beyond the first two extracted pages and should be read in the full paper/SI before reusing numerical claims in downstream synthesis.

## Limitations

Extreme salt concentration raises viscosity, wetting, and cost considerations; long calendar life and safety under abuse conditions require separate qualification beyond the reported scope.

## Relevance to group

**Battery interface chemistry** adjacent to group interests; **not** a ReaxFF paper, but relevant to **SEI/electrolyte** benchmarking.

## Citations and evidence anchors

- DOI: [10.1016/j.isci.2020.100844](https://doi.org/10.1016/j.isci.2020.100844)

## Related topics

- [[batteries-interfaces-reaxff]]
