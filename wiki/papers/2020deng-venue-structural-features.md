---
id: paper:2020deng-venue-structural-features
type: paper
title: "Structural features of sodium silicate glasses from reactive force field–based molecular dynamics simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:water-silica-geo
  - material:silicate-glass
  - method:reaxff
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1111/jace.16837"
year: 2020
authors:
  - "Lu Deng"
  - "Shingo Urata"
  - "Yasuyuki Takimoto"
  - "Tatsuya Miyajima"
  - "Seung Ho Hahn"
  - "Adri C. T. van Duin"
  - "Jincheng Du"
venue: "J. Am. Ceram. Soc. 103:1600-1614 (2020)"
pdf_sha256: "017a658b425b660f93f5bd87e28e363fcf49a776d90d86921b161f81f9728889"
pdf_path: "papers/Deng_NaSiOx_JaCERS_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020deng-venue-structural-features -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This *Journal of the American Ceramic Society* (*JACS* in the sense of the American Ceramic Society, not the American Chemical Society) article benchmarks reactive molecular dynamics of sodium silicate glasses using ReaxFF against a widely used partial-charge pairwise potential and against experimental structure probes. The motivation is twofold: sodium silicate glass is an industrially important archetype for multicomponent silicates, and reactive potentials are increasingly needed to study corrosion and environmental interactions where bond rearrangement with water matters. Prior work with nonreactive potentials produced detailed short- and medium-range structural comparisons for many compositions, but capturing reaction chemistry with water requires potentials that treat bond breaking and formation self-consistently. Lu Deng, Adri C. T. van Duin, Jincheng Du, and AGC-affiliated coauthors therefore evaluate whether refined ReaxFF parameters can reproduce key glass structural signatures before deploying them in water–glass studies.

## Methods

**1 — MD application (melt, quench, annealing; LAMMPS).** **Engine:** **LAMMPS** runs classical molecular dynamics for **Na\(_2\)O**–**SiO\(_2\)** **supercells** (thousands of **atoms**; **3D** **PBC** / **periodic** **boundaries** in the **bulk** **glass** **setup** as **standard** for these **packings**). **Nosé–Hoover** **thermostat** and **barostat** for **NPT** where applicable; **Ewald** summation; **10 Å** **cutoff**s for **short-range** **pairs** (as stated). **Teter** **(rigid-ion)** **melt–quench** **(initial** **structures):** **minimize** at **0 K**, **relax** at **300 K**, **heat** to **3500 K** and **hold** **100 ps** **(NPT)**, then **cool** to **300 K** at **5 K ps⁻¹** **(NPT)**; **time** **step 1 fs** for this **Teter** **preparation** **block**. **ReaxFF** **(Yu17** / **Hahn18** **families)** **uses** **Teter**-**prepared** **glasses** as **inputs**; **NPT** **anneal** over **Tₐ = 300, 600, …, 3000 K** (**11** **temperatures**), **100 ps** **at** **each** **Tₐ**, then **5 K ps⁻¹** **cool** to **300 K**; **~80 ps** **NPT** **at** **300 K**; **10 ps** **NVT**; **10 ps** **NVE** with **structural** **output** from the **last** **2 ps** **(50 fs** **output** **interval)**. **Barostat:** **NPT** **through** **anneal** **and** **equilibration**; **NVE** **for** **the** **final** **output** **segment**. **Replica** / **umbrella** / **metadynamics: N/A**. **Electric** **field: N/A**. **Discussion** **compares** **cost:** **ReaxFF** **~35×** **slower** than **Teter** for the **same** **simulated** **time** under their **setup**, with **ReaxFF** **using** **0.1 fs** **vs** **1 fs** **(Teter)** **per** **step**. **Pure** **ReaxFF** **melt–quench** is **noted** as **feasible** but **more** **expensive** and **can** **raise** **coordination** **defects** **(SI** **Table** **S3)**.

**2 — Force-field training in this work.** **N/A** — the study **adopts** published **Na–Si–O–H** ReaxFF parameter lines (**Yu17** and **Hahn18** / **Hahn1831** in the text) and does not report a new in-paper CMA/MCFF fit.

**3 — Static DFT in this work.** **N/A** — validation is **ReaxFF** and **Teter** MD against diffraction, NMR motifs, and experiment.

## Findings

- **ReaxFF lines vs Teter.** The **Hahn18**-family ReaxFF sets (including **(OO)**-related treatments, labeled as **Hahn18-OO** in the text) better match **Qₙ**, **PDFs**, and **F(Q)** against the Teter nonreactive baseline in their protocol than the **Yu17** set; a pure ReaxFF melt–quench leaves more coordination defects than a **Teter**-seeded glass followed by the reported **Hahn**-line **re-anneal** (**Table** **S3**).
- **Experiment.** Neutron- and X-ray-broadened **F(Q)**, **PDFs**, and **coordination**/**Qₙ** are compared to experimental and literature data; F(Q) peak positions are largely reproduced, while the Discussion notes amplitudes and some secondary features (shoulder/split peaks) where the rigid-ion or ReaxFF models differ.
- **Practical route.** The authors recommend a mixed workflow: efficient **Teter** **melt–quench** to build initial glasses, then **Hahn**-ReaxFF **re-annealing** near the glassy regime to obtain models suitable for subsequent **water–glass** ReaxFF studies, citing **~35×** **wall**-**time** cost and **0.1** **fs** **vs** **1** **fs** timesteps.
- **Outlook.** Polarizable-ion models and further ReaxFF improvements are mentioned where **F(Q)**, **Qₙ**, and related metrics remain imperfect in their tests (Discussion/Conclusions).

## Limitations

Specific compositions studied; ReaxFF refinements evolve—later parameter sets may supersede details here.

## Relevance to group

Collaboration with UNT/AGC on industrially relevant silicate glasses; van Duin co-authorship on validation-centric ReaxFF for soda–silica networks.

## Citations and evidence anchors

`papers/Deng_NaSiOx_JaCERS_2019.pdf` — abstract and structural comparison sections. https://doi.org/10.1111/jace.16837

## Reader notes (navigation)

- Soda–lime / silicate glass validation: [[theme-oxides-silica-ceramics]], [[reaxff-family]].

## Related topics

- [[2019sattler-venue-st-century]]
- [[reaxff-family]]
