---
id: paper:2021amiri-applied-surf-atomistic-insights
type: paper
title: "Atomistic insights into the protection failure of the graphene coating under hyperthermal impacts of reactive oxygen species"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - material:graphene-carbon-nano
  - material:metal-surface
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:metallic-systems
  - keyword:reactive-md
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1016/j.apsusc.2021.149606"
year: 2021
authors:
  - "Negar Amiri"
  - "Jahan B. Ghasemi"
  - "Hassan Behnejad"
venue: "Appl. Surf. Sci."
pdf_sha256: "c7662545e036694e75a673b84501987ff585e35151111d8f5caa72f310635ec1"
pdf_path: "papers/ReaxFF_others/Amiri_hyperthermal_graphene_AppliedSuSci_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021amiri-applied-surf-atomistic-insights -->

## Summary

Amiri *et al.* use **ReaxFF molecular dynamics** to study **hyperthermal** impacts of **atomic oxygen**, **O\(_2\)**, and **O\(_3\)** on **graphene-covered Ni(111)**, quantifying how effectively **graphene** protects the **metal** from oxidation when incident energies reach **10–30 eV**. The scenario is intentionally **nonthermal**: it resembles **beam**-like delivery of **ROS** rather than ambient **oxidation**, making it relevant to **plasma** and **space**-environment damage questions as well as to conceptual limits of **2D coatings**. The authors define **protection degree** metrics and interpret outcomes with **Wigner–Seitz**-style diagnostics on **Ni** to track **substrate damage**, alongside structural indicators for **graphene disorder** and **NiO** formation. The narrative advances a **three-stage** mechanism—**defect** formation in **graphene**, **Ni** transport across the **interface**, and **NiO** growth over **disordered carbon**—to explain how **protection** fails as energy rises.

## Methods

### A — Force-field training / fitting (ReaxFF and related)

- **N/A** as a new **parametrization** in this work: the study **applies** a **published** **ReaxFF** for **C**/**H**/**O**/**Ni**-class **chemistry** as described in *Appl. Surf. Sci.* (see **pdf_path** for the exact **force-field** **lineage** and any **QM** **benchmarks** cited for **Ni**/**graphene** **oxidation**).

### B — Molecular dynamics, experiments, protocols, and sampling

**ReaxFF** **MD** in **LAMMPS**-class **workflows** compares **bare** and **graphene**-covered **Ni(111)** under **normal** **hyperthermal** incidence of **O**, **O\(_2\)**, and **O\(_3\)** at **10, 20, and 30 eV** (nonthermal **beam**-like **energy** **deposition**). **3D** **PBC** **slab** **supercells**; sub-1 **fs** **timestep**; **ps**-scale (or as stated) **trajectory** **stages** after any **preequilibration**; **NVE**/**NVT** per the **Appl. Surf. Sci.** **Methods**; **thermostat** and **K**-scale **substrate** **temperature** (if a thermal **bath** is used)—see **pdf_path** for the precise recipe. **Barostat** and **isotropic** **1 bar** **pressure**—**N/A** in the **open** **impact** **regime** if the cell is not **NPT**-relaxed. **Shear** and **piston** **shock**—**N/A** in the baseline **normal**-**incidence** **impacts** described. **External** **DC** **electric** **field** in the **impact** protocol—**N/A** in the **abstract**-level summary. **Umbrella** / **replica**—**N/A**. **Analysis** includes **Wigner–Seitz** defect counting for **Ni** to quantify **substrate** **oxidation**/**reordering**, **protection** **degree** metrics, and **sp²** vs **disordered** **carbon** and **NiO** signatures.

### C — Electronic structure / static QM (when reported separately from MD)

- **Not applicable / not separated here:** **QM** used only as **ReaxFF** training data may be documented under **§A** in the article rather than as standalone **§C**.

### D — Review scope, SI/galley notes, and non-primary corpus roles

- **Not applicable:** primary research article unless the **Summary** flags a **review**, **SI-only** register, or **duplicate** PDF (see **Reader notes** / **Limitations**).

## Findings

**Pristine graphene** on **Ni(111)** can block **O\(_2\)** and **O\(_3\)** at **10 eV**, but **fails partially** at **20–30 eV**, with reported **protection degrees** around **53–55%** for **O\(_2\)** and **41–48%** for **O\(_3\)** depending on energy. **Atomic O** at **10 eV** yields about **59%** protection, falling to **~22%** at **20 eV** and **~6%** at **30 eV**, including regimes described as **anti-protective** when oxidation is **catalyzed** through **damaged graphene**. **Graphene** can evolve from **crystalline** **sp²** networks toward **disordered carbon** coexisting with **amorphous NiO** after sustained **hyperthermal** exposure in the authors’ trajectories. **Comparisons** of **bare** versus **coated** **Ni(111)** and of **O** versus **O₂**/**O₃** at the same **incident** **energy** isolate when the **coating** is **protective** versus **anti-protective**. **Sensitivity** to **energy** (**10–30 eV**) and **ROS** **identity** controls the **degree** of **Ni** **oxidation** and **graphene** **disorder**. **Limitations** of the **classical** model and **future** **work** toward **experiment**-anchored **flux** **scenarios** are discussed in the **article** and in **## Limitations** below. **Corpus** honesty: quote **numerical** **protection** **percentages** from the **version-of-record** **PDF** at `pdf_path`, not from this wiki alone.

## Limitations

**Hyperthermal** conditions differ from **thermal** oxidation; **ReaxFF** limits quantitative **sputter** and **electronic** excitation details. Readers comparing to **plasma** diagnostics should remember that **beam-energy** inputs here are **not** a substitute for **flux-weighted** thermal oxidation models.

## Reader notes (navigation)

This entry pairs with **graphene–metal** oxidation pages and with **tribology** notes that emphasize **shear** rather than **impact** loading; keep **`canonical_tags`** distinct to reduce **retrieval** collisions in **theme** hubs.

## Relevance to group

External **ReaxFF** application to **graphene–metal** **oxidation** under extreme **ROS** impact conditions.

## Citations and evidence anchors

- DOI: [10.1016/j.apsusc.2021.149606](https://doi.org/10.1016/j.apsusc.2021.149606)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]

