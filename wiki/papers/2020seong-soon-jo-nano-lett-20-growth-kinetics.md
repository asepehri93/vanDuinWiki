---
id: paper:2020seong-soon-jo-nano-lett-20-growth-kinetics
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
  - keyword:validation-experiment
  - keyword:oxide-surface
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
pdf_sha256: "30d51ec1f2143174b04443598292127de636dda10e585dda181318db7ddb72fd"
pdf_path: "papers/Others/Jo_MoS2_ZrS2_oxidation_acs.nano_2020.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020seong-soon-jo-nano-lett-20-growth-kinetics -->

## Summary

This entry registers an **alternate corpus PDF** path (`papers/Others/Jo_MoS2_ZrS2_oxidation_acs.nano_2020.pdf`) for the **Nano Letters** article **DOI `10.1021/acs.nanolett.0c03263`**. **Spectroscopic ellipsometry** follows **native oxide** growth on cleaved bulk **ZrSₓSe₂₋ₓ** alloys vs **MoS₂**; **ReaxFF reactive MD** (with **first-principles** checks summarized in the **Supporting Information**) interprets **O₂** chemisorption, **Zr–O** network formation, chalcogen **redox**, and late-stage **SO₂** evolution. **Zr**-based alloys oxidize rapidly in air with rate increasing in **Se** content, whereas **MoS₂** basal surfaces stay essentially non-reactive on laboratory timescales under the reported conditions. Canonical full write-up: **`[[2020seong-soon-jo-nano-lett-0-nl0c03263]]`**. The **comparative** **Zr vs Mo** storyline highlights **early-stage** **oxygen** uptake as **metal–chalcogen** **chemistry**-controlled: **Zr** **oxides** **form** readily from **cleaved** **surfaces**, while **MoS₂** **basal** **planes** present **unfavorable** **O₂** **activation** in both **experiment** and **simulation**.

## Methods

**Experiments:** ambient oxidation of cleaved crystals; **ellipsometry** for sub-nm oxide thickness evolution (see article). **Atomistics:** **ReaxFF** for **Mo/Zr/S/O** with development and benchmarks in **SI**; **reactive MD** at representative temperatures (including **800 K** short runs and **1500 K** longer runs for **SO₂** egress in the main text). **Validation:** authors reference **first-principles QMD** comparisons for key **ZrS₂** oxidation steps (**SI**). File-specific note: two PDFs share one DOI—use primary page for figure/table alignment if paths differ.

**Trajectory analysis:** authors monitor **oxide** **thickness** proxies, **gas** **species** counts, and **chalcogen** **oxidation** state evolution to connect **ellipsometry** slopes to **elementary** steps in **MD**.

**MD application (ReaxFF).** **ReaxFF reactive molecular dynamics** on **3D PBC** TMD slabs (full **atom** counts in `pdf_path` and **SI**); **~800** **K** vs **~1500** **K** **stages** with **ps**–**ns** **total** **durations** as on **`[[2020seong-soon-jo-nano-lett-0-nl0c03263]]`**. **Timestep:** **N/A** — femtosecond-scale integrator settings are not duplicated in this duplicate-path note; read `pdf_path`. **Ensemble:** **NVT**-style **thermostated** **ramped**-**T** **windows** in the **published** text. **Pressure in MD: N/A —** **1** **bar**-scale **ambient** **(ellipsometry)** **vs** **O₂** **(MD)**; see **`pdf_path`**. This file is a **duplicate** **corpus** path for the same **DOI**; **reproduce** **all** **settings** from **`pdf_path`**. **Barostat: N/A —** **Electric field: N/A —** **Umbrella** / **replica: N/A —** as on the **primary** **sibling** **page** **above**.


## Findings

**ZrSₓSe₂₋ₓ** oxidation begins with favorable **O₂** adsorption, **Zr–O** bond switching and **vdW** gap collapse, and successive chalcogen **redox**; **SO₂** formation/egress is the **slow** step in the mechanism narrative, with **1500 K** simulations showing **SO₂** escape where **800 K** runs are too short. **MoS₂** shows **unfavorable** basal **O₂** chemisorption in the model, consistent with slow oxidation in experiment. Numbers and trajectory discussion: **`[[2020seong-soon-jo-nano-lett-0-nl0c03263]]`**.

**Alloy trend:** increasing **Se** content in **ZrSₓSe₂₋ₓ** correlates with faster **ambient** oxidation in **ellipsometry**, interpreted via **weaker** **metal–chalcogen** bonding and **favorable** **O** incorporation pathways relative to **sulfide**-rich compositions.

**Corpus honesty:** canonical **protocol** **narrative** and **figure**-**pointed** **repro** **steps** are on **`[[2020seong-soon-jo-nano-lett-0-nl0c03263]]`** with **`papers/ReaxFF_others/Jo_Sungwook_acs.nanolett_2020_ZrSSe_MoS2.pdf`**. This `pdf_path` is an **alternate** **duplicate** of the same **DOI** only.

## Limitations

High-temperature MD accelerates chemistry; mapping to room-temperature kinetics requires care. Two corpus PDFs for one DOI—prefer consistent citation to one file for locators. **Ambient** **ellipsometry** **rates** also depend on **humidity**, **defect** **density**, and **edge** **exposure** not fully encoded in **ideal** **basal** **slab** models. **Plasma** **enhanced** **CVD** **impurities** may introduce **catalytic** **oxidation** pathways beyond those captured in **pristine** **surface** **models**.

## Relevance to group

**ReaxFF_others** corpus reference; **no van Duin authorship**—comparative context for **TMD** oxidation.

## Reader notes (navigation)

- [[2020seong-soon-jo-nano-lett-0-nl0c03263]]
- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
