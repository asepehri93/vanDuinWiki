---
id: paper:2024kim-nat-growth-based-monolithic
type: paper
title: "Growth-based monolithic 3D integration of single-crystal 2D semiconductors"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:tmd
  - method:dft-static
  - task:experiment-integrated
  - scale:multiscale
paper_keywords:
  - keyword:2d-materials
  - keyword:dft-static
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/s41586-024-08236-9"
year: 2024
authors:
  - "Ki Seok Kim"
  - "Seunghwan Seo"
  - "Junyoung Kwon"
  - "Doyoon Lee"
  - "Changhyun Kim"
  - "Jung-El Ryu"
  - "Jekyung Kim"
  - "Jun Min Suh"
  - "Hang-Gyo Jung"
  - "Youhwan Jo"
  - "June-Chul Shin"
  - "Min-Kyu Song"
  - "Jin Feng"
  - "Hogeun Ahn"
  - "Sangho Lee"
  - "Kyeongjae Cho"
  - "Jongwook Jeon"
  - "Minsu Seol"
  - "Jin-Hong Park"
  - "Sang Won Kim"
  - "Jeehwan Kim"
venue: "Nature 2024, 636, 615–623"
pdf_sha256: "51de7d3a2413bd30dc1520fa11304b8cfa1f045a64312bbefe5b2e13ccfbc71f"
pdf_path: "papers/Others/Kim_Kim_single_crystal_2D_Nature_2024.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024kim-nat-growth-based-monolithic -->

## Summary

The work reports **growth-based monolithic 3D (M3D)** integration of **single-crystal transition metal dichalcogenide (TMD)** channels on **amorphous or polycrystalline** back-end-compatible surfaces at temperatures **below about 400 °C**, enabling **vertically stacked complementary MOS (CMOS)** arrays with **grown** single-crystal channels rather than wafer bonding alone. Confined selective growth is used so that **MoS\(_2\)** and **WSe\(_2\)** nucleate in trenches on insulating layers at **sub-400 °C** (e.g. **MoS\(_2\)** growth at **385 °C** in the vertical stack described in the article), supporting **n-type** and **p-type** FET tiers in a monolithic flow.

## Methods

- **DFT (binding and slabs):** **VASP** self-consistent energy minimization with convergence **10\(^{-5}\) eV**; **IVDW = 11** dispersion correction for van der Waals binding; diverse slab models with **H-passivated** substrates; vertical **WSe\(_2\)**–substrate distances set to **2.0 Å (a-SiO\(_2\))** and **1.0 Å (a-HfO\(_2\), c-HfO\(_2\))** for the largest simulated flake in each case (per the article’s Methods).
- **TMD synthesis (CVD):** Two-zone **CVD** in a **4-inch** quartz tube; **Se** (or **S**) and **WO\(_3\)** (or **MoO\(_3\)**) sources with stated zone temperatures and **showerhead** geometry over trenches; processes such as **385 °C** channel growth for **MoS\(_2\)** in the vertical CMOS stack and **485 °C** for an initial **WSe\(_2\)** channel step in the described fabrication sequence; **Ar/H\(_2\)** carrier flow as specified in Methods.
- **Characterization:** **Raman/PL** (e.g. **532 nm**), **SEM**, **AFM**, **HRTEM**, **EDS** as stated.
- **Device fabrication:** **ALD** gate stacks, **e-beam lithography** and metallization (**Ti/Ni/Pt/Cr** etc.) for contacts and gates; **vertical CMOS** process flow with **MoS\(_2\)** grown at **385 °C** atop a **pMOS** tier in the reported integration.
- **Electrical / scaling analysis:** **I–V** at room temperature in air (**B1500A**); **3D finite-element** device simulation with **V\(_\mathrm{dd}\) = 0.5 V**, **I\(_\mathrm{OFF}\) = 10 pA μm\(^{-1}\)**, and cases comparing **D\(_\mathrm{np}\)** scaling with **EOT** rules (Supplementary discussion referenced in Methods).

**3 — Static QM (DFT binding studies).** **VASP** **GGA** **PBE** **DFT** **self-consistent** **SCF** minimization, **10\(^{-5}\) eV** electronic convergence, **IVDW=11** **vdW**-aware treatment, **H-passivated** **slab** **geometries** with **PAW** **pseudopotentials** / **plane-wave** treatment as in *Nature* *Methods* (exact **eV** **cutoff** and full **k-mesh**/**Brillouin** sampling: **N/A** in this process note); fixed **2.0/1.0 Å** **interlayer** spacings in the **binding** test models. **1 — Full MD** trajectories: **N/A**—not a bulk molecular-dynamics report. **2 — Force-field training:** **N/A**. **4 — Experiments and continuum FEM** supplement **DFT**; see the **Nature** article for the complete protocol table.
## Findings

- **Single-crystal TMD channels** are grown on **amorphous** insulators at temperatures compatible with preserving underlying **BEOL**-like constraints, using **confined selective growth** that promotes a **single nucleation** event in trenches; **heterogeneous nucleation** at trench **edges/corners** is leveraged for **MoS\(_2\)** and **WSe\(_2\)** on amorphous layers at **sub-400 °C** (substantially lower than typical **700–900 °C** TMD growth regimes cited in the paper).
- **Monolithic vertical CMOS** is demonstrated by growing **n-type** **MoS\(_2\)** FET arrays over **p-type** **WSe\(_2\)** FET arrays in an integrated flow.
- **DFT** supports favorable **vdW** binding scenarios used in the slab studies (with **dispersion-corrected** treatment as described).
- **FEM scaling** analysis relates **short-channel** behavior and **n/p balance** in **CFET**-like stacks, including the role of **D\(_\mathrm{np}\)** versus **EOT** scaling for matching **n-type** and **p-type** drive in scaled nodes (per the article and Supplementary Fig. 10). **Comparisons** to **CVD** literature growth temperatures and **I–V** data are in the main paper; this wiki note does not restate the **TEM/EDS** or **EOT** tables in full. **Version-of-record** **Nature** text governs device numbers.
## Limitations

The study is an experimental integration and **DFT/FEM** demonstration on specific **TMD** materials and stacks; generalization to other **2D** semiconductors, defect densities, and manufacturing lines requires separate validation.

## Relevance to group

Not a **ReaxFF** paper; included in the corpus as **2D semiconductor** process science adjacent to broader materials and device simulation interests.

## Citations and evidence anchors

- DOI: [10.1038/s41586-024-08236-9](https://doi.org/10.1038/s41586-024-08236-9)

## Related topics

- [[graphene-nanocarbon]]
