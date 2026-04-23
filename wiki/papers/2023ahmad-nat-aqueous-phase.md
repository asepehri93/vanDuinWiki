---
id: paper:2023ahmad-nat-aqueous-phase
type: paper
title: "Aqueous phase conversion of CO2 into acetic acid over thermally transformed MIL-88B catalyst"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - method:reaxff
  - task:experiment-integrated
  - material:zeolite-porous
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:validation-experiment
  - keyword:water-interfaces
candidate_tags:
  - "MOF-MIL-88B"
source_refs: []
doi: "10.1038/s41467-023-38506-5"
year: 2023
authors:
  - "Waqar Ahmad"
  - "Paramita Koley"
  - "Swarit Dwivedi"
  - "Rajan Lakshman"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "Abhijit Shrotri"
  - "Akshat Tanksale"
venue: "Nature Communications"
pdf_sha256: "d56c366a6d82ed8a2ba0c8280e2ac05c81fa3b1b260b52c907ea16ad7af9d4af"
pdf_path: "papers/Ahmad_Swarit_Yun-CO2_MIL_88B_2023-Nature_Communications.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023ahmad-nat-aqueous-phase -->

## Summary

**CO\(_2\)** hydrogenation and **C–C coupling** in **aqueous** media are attractive routes to **C\(_2\)+** chemicals, but efficient catalysts that operate in water with high **selectivity** to a single liquid product remain challenging. This **Nature Communications** article reports a **thermally transformed MIL-88B** catalyst in which **Fe\(^0\)** and **iron-oxide** motifs are embedded in a **carbonaceous matrix**, evaluated for **aqueous-phase methanol hydrocarboxylation** of **CO\(_2\)** toward **acetic acid** at **150 °C** with **LiI** as a **co-catalyst**. The experimental program reports **yield**, **selectivity**, and **recycling** performance, while **X-ray** characterization supports a nanoscale picture of the active material after transformation. **ReaxFF molecular simulations** are used alongside experiments to propose **plausible** **reaction pathways**—including involvement of **formic acid**-class intermediates—in a way that connects atomistic bond-making and bond-breaking hypotheses to the observed macroscopic performance.

## Methods

### Catalyst synthesis and characterization

- **Precursor:** **MIL-88B** subjected to **thermal transformation** (temperature/atmosphere program in the article) yielding **Fe\(^0\)** / **iron-oxide** species embedded in a **carbonaceous** matrix.
- **Characterization:** **X-ray** and **microscopy** modalities listed in *Nature Communications* **Methods** track **phase** and **Fe** dispersion.

### Catalytic experiments (aqueous CO₂ conversion)

- **Conditions:** **Aqueous** **CO\(_2\)** **hydrocarboxylation** with **methanol** and **LiI** **co-catalyst** at **150 °C** (stirring, pressure, and stoichiometries per paper).
- **Recycling:** Up to **five** cycles reported in the abstract with **yield**/**selectivity** tracking.

### ReaxFF molecular dynamics (B)

- **Purpose:** Explore **plausible** **bond-making/breaking** sequences consistent with **acetic acid** formation, including **water-mediated** chemistry and **C–O** rearrangements.
- **Protocol:** **ReaxFF** trajectories with **cell**, **thermostat**, and **analysis** choices documented in the **computational** section—**not** a substitute for measured **kinetics**.

### MD application (integrated)

**Engine / code:** **LAMMPS**-class **reactive MD** with **ReaxFF** (as in the article). **System & composition, slab vs cluster:** **Catalyst**/**aqueous**/**CO\(_2\)**-related interfacial models; **supercell** sizes and **stoichiometry** in **Nature Communications** *Methods* and figures—**N/A — not duplicated on this stub.** **PBC** for bulk/solution cells unless the article specifies a cluster; **N/A — frozen layers** if not used. **Ensemble:** follow the article’s **NVT** or **NPT** stages; **N/A here — thermostat/barostat types, damping, timestep (fs), and total trajectory length (ps/ns).** **Temperature:** catalytic tests at **150 °C**; MD **setpoints (K)** in the computational section. **N/A — applied electric field; N/A — umbrella/metadynamics/REX.** **Pressure** for autoclave/HP conditions: **N/A in wiki copy—see full text.**

## Findings

### Catalytic performance (abstract-reported)

**High acetic acid yield** on a **per-catalyst mass** basis with **selectivity** ~**81.7%** under the stated **aqueous** conditions (exact numbers in the article text/tables).

### Catalyst structure

Characterization supports **highly dispersed Fe\(^0\)** and **Fe(II)-oxide**-related motifs in the **transformed** catalyst compared with the parent **MOF**.

### Stability

**Recycling** shows **no major loss** of **yield** or **selectivity** over **five** cycles in the authors’ experiments.

### Mechanistic modeling role

**ReaxFF** provides **hypothesis-level** support for pathways involving **formic acid**-class intermediates and related **proton**/**C–O** events—presented as **qualitative** insight, not fitted **barriers** or **rates**.

## Limitations

**ReaxFF** provides qualitative mechanistic insight; **absolute rates**, **barriers**, and **electrochemical** effects in more complex electrolytes are not claimed to be fully captured by the force field. Operators should treat DFT or higher-level benchmarks as orthogonal validation if quantitative energetics are required.

## Relevance to group

Demonstrates **van Duin-group ReaxFF** integrated with **heterogeneous catalysis** experiments for **CO\(_2\)** valorization in **water**.

## Citations and evidence anchors

- DOI: [10.1038/s41467-023-38506-5](https://doi.org/10.1038/s41467-023-38506-5)

## Related topics

- [[reaxff-family]]
- [[theme-porous-mof-zeolite]]
