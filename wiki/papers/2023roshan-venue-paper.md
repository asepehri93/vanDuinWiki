---
id: paper:2023roshan-venue-paper
type: paper
title: "Supporting Information: Optimization of ReaxFF Reactive Force Field Parameters for Cu/Si/O Systems via Neural Network Inversion (with application to copper oxide interaction with silicon)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - material:oxide
  - method:reaxff
  - method:ml-potential
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2023
authors:
  - "Kamyar Akbari Roshan"
  - "Mahdi Khajeh Talkhoncheh"
  - "Mert Yigit Sengul"
  - "David Jonathan Miller"
  - "Adri C. T. van Duin"
venue: "Supporting information PDF (corpus: Roshan_JPCC_CuSiO_2023_SI.pdf)"
pdf_sha256: "2143b19e62e9e29cb669413e8af52f5393b41ee8a9139a9319f7f9ed4d20975f"
pdf_path: "papers/Roshan_JPCC_CuSiO_2023_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2023roshan-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **Supporting Information** PDF (`papers/Roshan_JPCC_CuSiO_2023_SI.pdf`) accompanies a **J. Phys. Chem. C** article on **optimizing ReaxFF parameters** for **Cu/Si/O** systems using **neural-network inversion**, with application emphasis on **copper oxide** interactions with **silicon** surfaces relevant to **microelectronics** and **oxidation** chemistry. The SI’s visible content (extract) is dominated by **tabular** disclosures: **parameter indices**, **optimization bounds**, and **sensitivity** metrics for **bond**, **off-diagonal**, and **valence** terms in the **Cu–O** and **O–Cu–O** blocks—material needed to **reproduce** the optimized force field alongside the **main text** loss functions and **QM** training sets. These tables are the **machine-readable** backbone for **auditing** how **NN inversion** redistributes **error** across **interaction** classes when fitting **Cu/Si/O** chemistry relevant to **oxidized** **Cu** on **Si**-bearing **substrates**. **Until** the **parent** article’s **DOI** is mirrored in **front matter**, treat **bibliographic** **anchors** as **provisional** and **follow** the **JPCC** **PDF** **title** in **`papers/`** when it appears.

## Methods

**Document role** ([non-primary / SI catalog](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md)). The corpus ingests the **JPCC Supporting Information** at `papers/Roshan_JPCC_CuSiO_2023_SI.pdf`. All **kinetic/oxide/interface** **science** and **any** **validation** **RMD** belong in the **parent** **JPCC** **VOR** article; **citable** **claims** should be anchored there, not on this **SI-****only** note alone.

### 1 — MD application (not owned by this **SI-****only** **PDF** in this form)

**N/A** in this **SI** for a stand-alone, **repro-****ready** LAMMPS story: the **JPCC** VOR+full **SI** for the same **work** would state **how many** **atoms** sit in the **slab**/**supercell**, which **3D** **PBC**/**periodic** **boundary** **conditions** and **NVT**/**NPT** blocks apply, **0.1–0.5** **fs** **class** **timestep** choices typical for **ReaxFF** **(fs**-resolved **RMD)**, **ps**/**ns** **equilibration**+**production** **duration** targets, and **K**-scale **substrate** **temperature** (plus **Nose**–**Hoover**-class **thermostat** when **NVT** is used). **None of that** is **retyped** on this page—use the **parent** **JPCC** **PDF**/**SI** **bytes**. **N/A** for **E-field** or **rare-****event** **(metadynamics) **on** this** **summary**; **E-field**/**metadynamics** are **out** of scope for the **table-**centric excerpt.

### 2 — Force-field training (NN-****inversion** of **ReaxFF** **for** **Cu**/**Si**/**O;** **this** **SI =** **tables** **)**

- **ReaxFF** reoptimization: **JPCC** work uses a **neural-****network-****inversion** **workflow** to adjust **selected** ReaxFF **classes** in **Cu–O** / **O–Cu–O-****related** **manifolds**; the **local** **SI** **publishes** **parameter** **index** **mappings**, **bound** **constraints**, and **sensitivity** to **reproduce** the **fit**; **objectives** and the **DFT**/**QM** **training** **set** that **drove** the **loss** **landscape** are **in** the **JPCC** main **(not** retyped **here**).

**N/A (block 3) — static DFT** in this file: the **JPCC** VOR+SI list **Jaguar**-class and other **static** **QM** **reference** data used to build the ReaxFF **dataset**—**copy** **k**-points, **functionals**, and **basis** from the **primary** **PDF**/**SI**, not this **wiki** **summary**.

**Maintainer note (DOI/merge)**: add `doi: 10.1021/acs.jpcc.3c03079` and a VOR `paper:` page when the parent article is fully registered in the corpus; the empty `doi` in front matter reflects a legacy stub, not a missing community DOI.

## Findings

### Operational content

The SI’s primary “result” is **reproducibility metadata**—which **ReaxFF** **parameters** moved, by how much, and with what **sensitivity** in the **fit**, **versus** a black-box release without **indices** and **bounds**. **Compared** to a bare **field** file, the tables help an operator **reproduce** the same **inversion** **outcome** when paired with the **JPCC** main-text **objectives** and **QM** **data**.

### Scientific interpretation and corpus routing

**DFT**-referenced **error** **metrics**, **reaction** **barriers**, and **oxide**/**interface** **morphology** are **stated** in the **JPCC** main **figures** and text—**not** in this **SI-****only** **extract** as a **self-contained** **story**. **Limitation** (inherent to **SI-****only** routing): the **laser-****style** or **reactor-****grade** “**experiment**-level” **agreement** claims, if any, are **in** the **VOR** **article**, **not** the **table** list **alone**. **Open** **question** for MAS: whether **future** work will **publish** a **unified** **JPCC**+**SI** **wiki** page here—**until** then, use the **VOR** **PDF** and **this** `papers/` **path** to resolve **provenance** (see **##** **Limitations** for **version-of-record** **caveats**).

**Corpus** **honesty**: **proof** the **JPCC** **PDF**/**SI** if you need **T(K)**, **pressure** **(bar)**, or **NVT** **timestep** **(fs)**—**not** the **summary** line **above**; **this** page tracks **ingested** `Roshan_JPCC_CuSiO_2023_SI.pdf` **for** the **BOM** and **repro** **of** the **ReaxFF** **tables** only.

## Limitations

**SI-only** ingest: **no standalone** narrative results; **DOI** must be taken from the **parent article**. Per `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`, this row may stay **pointer-heavy** by policy. **NN inversion** workflows can be **sensitive** to **training set** coverage—treat **tabulated** **bounds** as **necessary** but **not sufficient** without the **main text** **loss** landscape and **validation** simulations.

## Relevance to group

Documents **group methodology** connecting **ReaxFF fitting** to **neural-network inversion** for **Cu/Si/O** chemistry relevant to **microelectronics** and **oxidation** at **Si** interfaces. Operators should treat this page as **SI provenance** paired with a **main JPCC** article once the **DOI** is registered in front matter during corpus hygiene passes.

## Citations and evidence anchors

- `papers/Roshan_JPCC_CuSiO_2023_SI.pdf`; extract `normalized/extracts/2023roshan-venue-paper_p1-2.txt`. Locate the **primary** **J. Phys. Chem. C** article (filename stem `Roshan_JPCC_CuSiO_2023`) for **DOI** and **pagination**.

## Related topics

- [[reaxff-family]]
- [[2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based]]
