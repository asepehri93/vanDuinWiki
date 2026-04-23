---
id: paper:2020seong-soon-jo-nano-lett-0-nl0c03263
type: paper
title: "Growth kinetics and atomistic mechanisms of native oxidation of ZrSₓSe₂₋ₓ and MoS₂ crystals"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - material:tmd
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:oxide-surface
  - keyword:validation-experiment
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1021/acs.nanolett.0c03263"
year: 2020
authors:
  - "Seong Soon Jo"
  - "Akshay Singh"
  - "Liqiu Yang"
  - "Subodh C. Tiwari"
  - "Sungwook Hong"
  - "Aravind Krishnamoorthy"
  - "Maria Gabriela Sales"
  - "Sean M. Oliver"
  - "Joshua Fox"
  - "Randal L. Cavalero"
  - "David W. Snyder"
  - "Patrick M. Vora"
  - "Stephen J. McDonnell"
  - "Priya Vashishta"
  - "Rajiv K. Kalia"
  - "Aiichiro Nakano"
  - "R. Jaramillo"
venue: "Nano Letters"
pdf_sha256: "f7d6ecdaab64ceb28935c3252cc4cadb0adea1dae20580fe7cfa6b9e5b4409ed"
pdf_path: "papers/ReaxFF_others/Jo_Sungwook_acs.nanolett_2020_ZrSSe_MoS2.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020seong-soon-jo-nano-lett-0-nl0c03263 -->

## Summary

**Spectroscopic ellipsometry** on cleaved bulk **ZrSₓSe₂₋ₓ** alloys vs **MoS₂** tracks **native oxide** growth; **ReaxFF reactive MD** (with **first-principles** checks in the **Supporting Information**) interprets **O₂** chemisorption, **Zr–O** network formation, chalcogen **redox**, and **SO₂** formation. **Zr**-based alloys oxidize rapidly in air with rate increasing in **Se** content; **MoS₂** basal surfaces remain essentially non-reactive on laboratory timescales under the reported conditions. The paper couples **ellipsometry kinetics** with **atomistic** **Zr** vs **Mo** contrasts in the MD narrative.

## Methods

- **Experiments:** Ambient oxidation of cleaved bulk crystals; **spectroscopic ellipsometry** for sub-nm oxide thickness evolution (see article).
- **Atomistics:** **ReaxFF** parameterization for **Mo/Zr/S/O** (development and benchmarks summarized in **SI**); **reactive MD** trajectories at representative temperatures (including **800 K** short runs and **1500 K** longer runs discussed for **SO₂** evolution in the main text).
- **Validation:** Authors reference **first-principles quantum molecular dynamics** comparisons for key **ZrS₂** oxidation steps (figures cited in **SI**).

**Cell** **sizes**, **ReaxFF** **parameter** **tables**, **thermostat**/**barostat** choices, and **analysis** scripts for **oxide** **thickness** **trends** are detailed in `papers/ReaxFF_others/Jo_Sungwook_acs.nanolett_2020_ZrSSe_MoS2.pdf` and the article **Supporting Information**.

**MD application (ReaxFF).** **ReaxFF reactive molecular dynamics** of **O₂** with **ZrSₓSe₂₋ₓ** and **MoS₂** basal slabs in **3D PBC** (atom counts in `pdf_path` and **SI**). The main text contrasts **~800 K** short **trajectories** (order **~tens of ps** in the article) and **~1500 K** longer **runs** (order **~hundreds of ps to ns**—confirm in `pdf_path`) for **SO₂** formation and egress. **N/A —** exact **fs** timestep in this wiki; see **SI**. **Ensemble:** **NVT**-like **thermostated** **ramped**-**T** **oxidation** (see article). **Barostat: N/A —** not a high-pressure shock cell in the **quoted** protocol summary. **Pressure (MD):** **1** **bar**-scale **laboratory** **ambient** **(ellipsometry)** is **separate** from the **O₂** **/ thermostats** in **ramped** **ReaxFF**; **N/A** **—** see **`pdf_path`** for **O₂** **chemical** **environment** **details**. **Electric field: N/A —** not used. **Umbrella / metadynamics / replica exchange: N/A —** not in the summarized **ramped**-**T** **protocols** here.


## Findings

- **ZrSₓSe₂₋ₓ** basal oxidation initiates with favorable **O₂** adsorption followed by **Zr–O** bond switching and gap collapse; chalcogen sites undergo successive **redox** transitions during oxygen ingress.
- **SO₂** formation and egress appear as the slow step in the mechanism narrative; **1500 K** simulations observe **SO₂** escape whereas **800 K** runs are too short to capture full egress in the showcased trajectory.
- **MoS₂** shows **unfavorable** oxygen chemisorption on basal planes under the model, consistent with slow oxidation in experiment.

The **authors** emphasize interpreting **accelerated** **MD** **temperatures** as **qualitative** **mechanistic** **guides** paired with **room-temperature** **experimental** **oxidation** **rates**. **Corpus honesty:** pull **reproducible** **MD** **settings** from `pdf_path` and **SI**; an **alternate** **PDF** **path** is **`[[2020seong-soon-jo-nano-lett-20-growth-kinetics]]`**.

## Limitations

High-temperature MD used to accelerate chemistry; direct mapping to room-temperature kinetics requires care. Force-field accuracy for Zr–S–Se–O chemistry is benchmarked but remains empirical.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

Included as **ReaxFF_others** corpus reference; **no van Duin authorship**—useful comparative context for TMD oxidation and ReaxFF validation practices.

## Reader notes (navigation)

- [[2020seong-soon-jo-nano-lett-20-growth-kinetics]] (alternate PDF path for the same article)
- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
