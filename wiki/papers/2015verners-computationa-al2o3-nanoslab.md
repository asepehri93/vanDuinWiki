---
id: paper:2015verners-computationa-al2o3-nanoslab
type: paper
title: "α-Al2O3 nanoslab fracture and fatigue behavior"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - method:reaxff
  - material:oxide
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2015.02.048"
year: 2015
authors:
  - "Osvalds Verners"
  - "George Psofogiannakis"
  - "Adri C. T. van Duin"
venue: "Comput. Mater. Sci."
pdf_sha256: "b19713853cce68af6cd13b9dfa8dfa6542b795cf3c0f0e20f0f94a8bc1c7ce12"
pdf_path: "papers/Verners_CompMatSci_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2015verners-computationa-al2o3-nanoslab -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Reactive MD (ReaxFF)** and complementary **ionic relaxation** workflows are applied to **single-crystalline α-Al2O3 nanoslabs** under **monotonic and cyclic** mechanical loading, comparing **finite-temperature dynamic** failure with **incremental static** pathways. The study emphasizes how **strain rate**, **lateral pre-strain**, and **size effects** change **failure strains**, **crack healing vs. branching**, and **amorphization** ahead of cracks, with selected comparisons to **DFT** for bulk-like responses. Conclusions are framed around **low-cycle fatigue** scenarios where **shakedown-like** elastic responses can emerge after repeated loading. The article ties these atomistic trends to how **bond-order reactive** descriptions capture **network rearrangement** near crack tips without predefining failure planes, complementing purely elastic treatments of alumina.

## Methods

**Reactive MD (LAMMPS + ReaxFF)** treats single-crystalline **α-Al₂O₃ nanoslabs** in the **[10̄10]** tensile orientation inside **3D periodic** cells; one box dimension is strained while in-plane response follows the dynamic vs static branches below. Dynamic runs use **NPT**-style control at **300 K** with the tensile direction fixed and lateral normal stresses relaxed toward **0 Pa** using **Nosé–Hoover** thermostat (**100 fs** damping) and barostat (**5000 fs** damping), **0.2 fs** timestep, **0.25%** strain pulses of **0.5 ps** separated by **5 ps** relaxations (**~1.9 ns⁻¹** loading frequency in the article). A parallel **static** branch applies **0.25%** strain increments followed by energy minimization (conjugate-gradient / FIRE-style routines referenced in the text), including multi-cycle tension–compression–reloading protocols. Additional **7% [10̄10]/[11̄20]** pre-strained starts and **volume-minimized** initial states are compared to the **0 atm** relaxed reference. No electric field or enhanced sampling is used.

**Force-field training:** **N/A —** the article **uses** merged published **Al/O**, **Al/H**, **O/H**, and **Al/O/H** ReaxFF subsets and validates elastic response; it does not report a new global ReaxFF refit.

**Static QM / DFT:** **VASP** **PBE**-type calculations on **α-Al₂O₃** provide equation-of-state and bulk **Cᵢⱼ** data summarized in **Table 1** and used to contextualize ReaxFF moduli; dispersion, basis, and **k**-mesh follow the settings tabulated in the Computational section.

## Findings

**Finite-temperature dynamic** loading produces **lower failure strains** than the **incremental static** pathway for the compared nanoslab setups in `papers/Verners_CompMatSci_2015.pdf`. **Amorphous bands** ahead of cracks and **local amorphization** accompany **small-strain plasticity** and **defect healing** channels illustrated in the figures. ReaxFF elastic and fracture-related quantities are compared to **DFT** and experiment in the article’s tables. **Positive [10̄10]/[11̄20] pre-strain** increases **stress triaxiality**, favoring a **single sharp crack** and **less crack healing**, whereas **volume pre-relaxation** promotes **branching** and **amorphous-band** formation that can support **healing** and **elastic shakedown** after cyclic loading (abstract and discussion). The discussion ties **strain rate**, **temperature**, and **preparation path** to **healing vs branching**; use the journal PDF for stress–strain numbers and cycle counts ([[2015verners-venue-paper]] catalogs a non-primary proof sibling).

## Limitations

- **Nanoscale slabs** omit **grain boundaries** and **environmental chemistry** (humidity) present in engineering alumina.
- **ReaxFF** alumina mechanics must stay tied to the **parameterization’s QM training envelope**.

## Relevance to group

Joint **Penn State** effort on **ReaxFF for ceramic fracture and fatigue**, connecting reactive FF capabilities to **mechanical reliability** questions.

## Citations and evidence anchors

- Abstract and article metadata in `papers/Verners_CompMatSci_2015.pdf`; **DOI:** `10.1016/j.commatsci.2015.02.048`.

## Related topics

- [[reaxff-family]]
