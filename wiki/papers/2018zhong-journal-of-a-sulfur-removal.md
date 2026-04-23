---
id: paper:2018zhong-journal-of-a-sulfur-removal
type: paper
title: Sulfur removal from petroleum coke during high-temperature pyrolysis. Analysis
  from TG-MS data and ReaxFF simulations
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:carbon-hydrocarbon
- domain:fuel-combustion
- domain:organics-polymers-pyrolysis
- domain:reaxff-lineage
- method:reaxff
- task:application
- task:experiment-integrated
- scale:atomistic
candidate_tags: []
source_refs: []
doi: 10.1016/j.jaap.2018.03.007
year: 2018
authors:
- Qifan Zhong
- Qiuyun Mao
- Jin Xiao
- Adri C. T. van Duin
- Jonathan P. Mathews
venue: J. Anal. Appl. Pyrolysis
pdf_sha256: 199ace13e1bce743988e34fad7d85b2f1903300ec85f6669fcc63c5eac7f8992
pdf_path: papers/Zhong_PetCoke_JAAP_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018zhong-journal-of-a-sulfur-removal -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Thermogravimetry–mass spectrometry (TG-MS)** on **petroleum coke** samples quantifies **sulfur rejection** versus **temperature**, **particle size**, and **source**, showing that **high temperature (≳1673 K)** drives large **desulfurization** extents (often **~80%**) for fine fractions, with **more variable** behavior for **large particles** in some feeds. **ReaxFF MD** on a **macromolecular coke** model with **thiophene-like** sulfur probes **atomistic** elimination pathways at **3000–4000 K** in **NVT** runs, rationalizing **volatile sulfur** species (e.g. **SO₂**, **CS₂**, **COS**) observed or inferred from **experiment**. **Adri C. T. van Duin** and **Jonathan P. Mathews** are Penn State coauthors with **Zhong** and collaborators in China. The paper frames the combination as a **dual-scale** story: **macro** mass-loss and evolved-gas signatures paired with **microscopic** bond-breaking sequences that would be inaccessible at calcination-relevant timescales without accelerated reactive MD.

## Methods

**Experiment (TG-MS).** **Thermogravimetry–mass spectrometry** tracks mass loss and evolved gases for **petroleum coke** samples across **particle sizes** and **sources** under controlled **heating** programs, with **temperature** windows tied to **H₂O**, **volatiles**, **CO₂**/**H₂**, **CO**/**SO₂**, and trace **CS₂** signals summarized in the abstract.

**ReaxFF MD (§2.2.2, *J. Anal. Appl. Pyrolysis* **132** (2018) 134–142).** **Engine / code:** **ReaxFF** **molecular dynamics** is run in **ADF** with the **ReaxFF–CHONSSi** parameterization cited in the article. **Model / composition:** a **Qingdao petcoke**-inspired **macromolecule** **C₁₉₂H₉₆O₇N₃S₆** sits in a cubic **64 × 64 × 64 Å** **PBC** cell (Fig. 1b). **Ensemble:** **NVT**; **atomic** **valency** and **torsion** cutoffs for bond-order assignment are **0.3 Å** and **0.001** as stated in §2.2.2. **Timestep:** **0.25 fs** (tests at **0.1 fs** gave similar **S** decomposition kinetics; **0.25 fs** preferred for **S** tracking per §2.2.2). **Duration / temperature:** **250 ps** at each **T** in **1000–4000 K**, with an **additional 250 ps** if transformations stall. **Thermostat:** **Berendsen** with **100 fs** damping. **Barostat / pressure:** **N/A —** **NVT** (constant **volume**). **Electric field / enhanced sampling:** **N/A —** not used.

**Analysis alignment.** Simulation **temperature** is an **acceleration** device to populate **elementary** **elimination** and **rearrangement** events, interpreted alongside **qualitative** **TG-MS** product trends rather than as a literal furnace replica.
## Findings

- **Gas evolution** features include **H₂O** (low-T), **volatiles**, then **CO₂/H₂**, **CO/SO₂** at higher **T**, and trace **CS₂**; **COS/H₂S** are **absent or below detection** under the reported conditions.
- **ReaxFF** trajectories suggest a **multi-step** **S removal** sequence from **thiophenic** sulfur toward **small** **S-bearing** intermediates and ultimately **SO₂** / **CS₂**-class products, consistent with the **TG-MS** picture.
- Together, the datasets support the idea that **thiophenic** sulfur can be liberated through routes that pass through **small oxygenated** and **sulfur-bearing** fragments before appearing as stable gas-phase monitors such as **SO₂**.

**Sensitivity and outlook.** **Experiment** emphasizes **temperature** and **particle size** as levers on **desulfurization** extent; **simulation** highlights how ultrahigh **T** changes **reaction** accessibility within **250 ps** windows. **Limitations** as authored include the illustrative single **macromolecular** model vs real **petcoke** **heterogeneity** (see **## Limitations**). **Corpus honesty:** definitive **mechanistic** sequences and any **literature** benchmarks beyond the abstract bullets require the **PDF** at `pdf_path`.
## Limitations

- **ReaxFF** temperatures are **far above** industrial **calcination** to access **reactions** in **nanoseconds**; **mechanistic** insight is **qualitative** for **absolute yields**.
- **Petcoke** structural **heterogeneity** means any **single** **macromolecular** model is **illustrative**, not **sample-specific**.

## Relevance to group

Companion **JAAP** study to **`paper:2018qifan-combustion-a-reaxff-simulations`** on **petcoke desulfurization**, with **van Duin** / **Mathews** **reactive MD** involvement.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.jaap.2018.03.007` (`papers/Zhong_PetCoke_JAAP_2018.pdf`).

## Related topics

- [[reaxff-family]]
