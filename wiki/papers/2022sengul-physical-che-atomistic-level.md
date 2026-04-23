---
id: paper:2022sengul-physical-che-atomistic-level
type: paper
title: "Atomistic level aqueous dissolution dynamics of NASICON-type Li1+xAlxTi2−x(PO4)3 (LATP)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:water-silica-geo
  - domain:oxides-ceramics
  - material:ceramic-electrolyte
  - method:reaxff
  - task:application
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/D1CP05360D"
year: 2022
authors:
  - "Mert Y. Sengul"
  - "Arnaud Ndayishimiye"
  - "Wonho Lee"
  - "Joo-Hwan Seo"
  - "Zhongming Fan"
  - "Yun Kyung Shin"
  - "Enrique D. Gomez"
  - "Clive A. Randall"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys. 24, 4125–4130 (2022)"
pdf_sha256: "865dc85389a4fb64fc2eb2b2f310baa4c6f9d17cb7ed33e8931f1557a32ee62f"
pdf_path: "papers/Sengul_NASICON_PCCP_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022sengul-physical-che-atomistic-level -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**NASICON-type Li\(_{1+x}\)Al\(_x\)Ti\(_{2-x}\)(PO\(_4\))\(_3\)** (**LATP**) is a **fast Li-ion conductor**, yet **moisture** during **cold sintering** or **slurry processing** can trigger **incongruent dissolution** that leaves **porosity**, **impurities**, or **interphase layers** that harm **solid electrolyte** cells. **Sengul** et al. combine **ReaxFF molecular dynamics** of the **LATP / liquid water** interface with **experimental** characterization of **cold-sintered** ceramics to follow **ion release**, **framework** degradation, and **secondary-phase** nucleation in sequence. **Adri C. T. van Duin** co-authors the reactive modeling effort alongside **Randall**-group **processing** expertise, situating the study in **PCCP** as a **Communication**-length mechanistic report.

## Methods

### Experiments (cold-sintered LATP + characterization)

- **Samples:** Densified **LATP** ceramics from **cold sintering** at **130 °C** in the presence of **water** (details of powders, binders, and thermal history in the article **Methods**).
- **Microscopy / spectroscopy:** **SEM/EDS** on initial powder; **HAADF-STEM** with **EDS** mapping on cold-sintered ceramics to track **Ti** vs **Al** segregation and homogeneous **P** distribution (figure set referenced in the Communication).
- **Coupling to computation:** Experimental microstructure motivates the **incongruent dissolution** picture compared against trajectories.

### ReaxFF molecular dynamics (B)

- **Interaction model:** **ReaxFF** for **LATP–water** interfaces with **Li–Al–Ti–P–O** chemistry consistent with **NASICON**-family parameterizations cited from prior training literature.
- **Setup:** **Slab** (or equivalent) **LATP** surface in contact with **liquid water**; evolution of the interface is tracked as dissolution proceeds.
- **Analysis:** **Li** release into solution, **phosphate** connectivity changes, **AlO\(_x\)** / **PO\(_4\)**-related **polymerization**, **Ti–Ti** **radial distribution** evolution, and segregation patterns compared to STEM-EDS (simulation snapshots in the paper).
- **Electrostatics / charge:** ReaxFF **charge equilibration** (QEq) conventions follow the standard ReaxFF treatment in the authors’ software setup; exact **cutoffs**, **timestep**, and **thermostat** are specified in the article/SI—not duplicated here.

### Integrated interpretation

Iterative comparison of **experimental** elemental redistribution with **simulation** morphology (e.g. **Ti**/**Al** segregation during dissolution) supports the proposed **sequential** mechanism.

### MD application (LATP / water)

**Engine / code:** **LAMMPS**-style **ReaxFF** integration (as in *PCCP*). **Slab**/**interface** of **LATP** with **liquid water**: **3D PBC** **supercell** size, **T** and **P** (if **NPT**), **timestep**, **ps**/**ns** stages, **thermostat**/**barostat** where used, and **Coulomb** / **QEq** settings for **Li–Al–Ti–P–O** with **H\(_2\)O** are specified in the article; this wiki defers to that text. **N/A** — open-circuit water exposure, no **galvanostatic** **bias** or static **interfacial electric field** in the **MD** protocol as summarized. **N/A** — no **metadynamics** or **replica** **sampling** beyond the reported **MD** unless the **SI** adds them.

## Findings

### Staged dissolution sequence

Dissolution is **sequential** and **incongruent** (dissolved stoichiometry ≠ bulk stoichiometry): rapid **Li** leaching—common for **NASICON**-type materials—is followed by **phosphate**-linked rearrangements that **destabilize** the framework and promote **Ti-rich** **secondary-phase** formation, rather than uniform surface recession.

### Rate control and polymerization

After initial **Li** loss, the **dissolution rate** is tied to **polymerization** of **AlO\(_6\)** and **PO\(_4\)**-derived species (as summarized in the abstract and Fig. 1 schematic), which in turn triggers **secondary phases**.

### Processing implications

Brief **water** contact during **cold sintering** or slurry steps can leave **interfacial** chemical signatures even when **bulk** **X-ray** patterns look unchanged, motivating care in **solution-based** processing of **NASICON** electrolytes.

### Scope relative to devices

Open-circuit **water** exposure omits **applied bias** and **pH** control of real **battery** interfaces; mapping to operating cells requires extending the model (as the authors note directionally).

## Limitations

Specific surface orientation, pH, and electrochemical bias in real devices extend beyond a single interface model; quantitative dissolution rates require careful calibration to experiment and thermodynamic databases.

## Relevance to group

Direct **ReaxFF + ceramic electrolyte** interface work tied to **PSU materials** collaborations and broader **battery processing** themes in the corpus.

## Citations and evidence anchors

https://doi.org/10.1039/D1CP05360D — Communication (~pp. 1–2) states sequential mechanism and Li/PO\(_4\) arguments.

## Related topics

- [[reaxff-family]]
