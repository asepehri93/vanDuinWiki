---
id: paper:2022anushka-bansal-acs-toward-mechanistic
type: paper
title: "Toward a Mechanistic Understanding of the Formation of 2D-GaNx in Epitaxial Graphene"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - material:widegap-semiconductor
  - material:graphene-carbon-nano
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:graphene-carbon
  - keyword:2d-materials
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.2c07091"
year: 2022
authors:
  - "Anushka Bansal"
  - "Nadire Nayir"
  - "Ke Wang"
  - "Patrick Rondomanski"
  - "Shruti Subramanian"
  - "Shalini Kumari"
  - "Joshua A. Robinson"
  - "Adri C. T. van Duin"
  - "Joan M. Redwing"
venue: "ACS Nano"
pdf_sha256: "20a515452f5a1baf43762e98aa2aeb951998c468dfbd751dd700d9e35d496992"
pdf_path: "papers/Bansal_GaNx_ASCNano_2022_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022anushka-bansal-acs-toward-mechanistic -->

## Summary

The work links MOCVD growth, surface analytics (SEM, Auger mapping, STEM/EDS), and DFT to explain how graphene thickness and oxygen functionalization steer gallium intercalation and subsequent nitridation to 2D-GaN\(_x\) under epitaxial graphene on SiC. Oxygen-rich buffer-layer regions near steps adsorb plasma-generated oxygen and block intercalation, whereas thicker, nonfunctionalized terraces intercalate gallium; immediate NH\(_3\) annealing after TMGa exposure is required to avoid gallium loss during heating. **Epitaxial graphene on SiC** is a **platform** for **2D** **nitride** integration because **sp\(^2\)** **carbon** can template **intercalation** chemistry while **SiC** supplies **C**-face vs **Si**-face **step** structure that localizes **oxygen** uptake.

## Methods

**1 — MD application (atomistic dynamics).** **N/A** — the study does not report production reactive or classical MD trajectories; prior ReaxFF work on gallium intercalation is cited in the introduction for context only.

**2 — Force-field training.** **N/A** — no ReaxFF or classical FF reparameterization in this work.

**3 — Static QM / DFT.** The authors use density functional theory to relax and compare adsorption **energy** (and related interaction **energy** targets) for **epoxy-** and **hydroxyl-** functionalized **graphene** with **gallium** and **NH\(_3\)**-related motifs, contrasting **basal (nonoxidized) terraces** with **oxidized** regions. Full **functional** (e.g. **PBE**-class and hybrid or dispersion choices), **PAW**/**plane-wave** or equivalent **basis** settings, a documented **k-mesh** (k-point) grid for the periodic **supercells**, and the list of **relaxed structures** and other computed **property** sets are given in the electronic-structure section of the **PDF** (this wiki does not restate every numerical cut-off from the VOR; the corpus `pdf_path` is a **galley**-style file for this ingest).

**4 — Experiments and correlative analysis.** MOCVD uses **epitaxial graphene on SiC** with **as-grown** and **He/O\(_2\)**-**plasma**-exposed conditions; **Auger** maps (e.g. **C/O** contrast) and **STEM/EDS**-style **cross-section** imaging (per *ACS Nano* Methods) tie **graphene thickness** and **local oxygen** content to **TMGa** exposure, **gallium** **intercalation** vs **droplet** formation, and **NH\(_3\)**-driven **nitridation** to **2D-GaN\(_x\)**. Correlative readouts link **O-rich buffer-layer** areas to **blocked intercalation** and **O-functionalized** thin regions to **2D-GaN\(_x\)** when **ammonia** annealing follows **gallium** immediately.

## Findings

**Outcomes and mechanisms.** Thin **buffer-layer** **graphene** near **SiC** steps attains **oxygen** functionalization under **plasma** or **air**-equivalent exposure more readily than **thicker**, less reactive terraces; that **O**-rich state **inhibits Ga intercalation** and can yield **surface gallium droplets**, whereas **thicker**, **low-oxygen** regions allow **gallium** **under the graphene**. **2D-GaN\(_x\)** after **TMGa** + **NH\(_3\)** is observed preferentially in **O-functionalized** **thin** regions when **ammonia** is applied right after **gallium** exposure, while **intercalated** Ga under **thick, nonfunctionalized** graphene may **not** convert in the same window. **DFT** supports a picture where **hydroxyls** and related **O** groups **weaken** direct **Ga** binding to the **surface** but **enhance** **NH\(_3\)** **reattivity** at the **graphene**, promoting **local nitridation** and **2D-GaN\(_x\)** at **O-rich** **patches**, consistent with the experimental emphasis on **O-functionalized buffer** graphene for **uniform** coverage. Co-authors **Nayir** and **van Duin** place the **theory** in the same Penn State line as **graphene**-related **reactive** modeling, though **ReaxFF** is not the main engine here.

**Comparisons.** The work contrasts **O-rich vs** **low-O** **EG** regions, **thin vs thick** **graphene** on **SiC**, and **sequencing** of **Ga** and **NH\(_3\)** exposure; see the **PDF** (prefer **VOR** over the corpus galley file for pagination) for **SEM/Auger/STEM** correlation and **DFT** **energy** tabulations.

**Sensitivity and levers.** **Graphene** **thickness**, **step**- and **plasma**-driven **oxygen** uptake, and **MOCVD** **timing** (**immediate NH\(_3\)** after **gallium**) are the central process knobs the authors highlight.

**Limitations (as framed on this page).** **Reactive MD** in cited work is not driving this study’s new results. **Kinetics** of full **MOCVD** cycles and **entropic** effects in **ALD**-like **precursor** **coverage** exceed the **0 K**-style **DFT** **sampling** summarized here; **wafer** **nonuniformity** in **graphene** from **sublimation** **growth** can outrun **lab** **coupon** **maps**—see also **`## Limitations`** below and the **VOR** **PDF** for author discussion.
## Limitations

Reactive MD cited from related work is not the primary engine here; kinetics of full MOCVD cycles exceeds the DFT models.

**Wafer-scale** **nonuniformity** in **graphene** **thickness** and **step** **density** from **SiC** **sublimation** growth can amplify **oxygen** **plasma** **heterogeneity** beyond the **lab** **coupons** analyzed—expect **process-window** **sensitivity** when **scaling** **GaN\(_x\)** **coverage**.

## Relevance to group

Co-authored by van Duin; couples epitaxial graphene/III–V chemistry with DFT interpretation relevant to 2D nitride synthesis.

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
