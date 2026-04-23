---
id: paper:2019mvf3-venue-paper
type: paper
title: "Supporting Information: Development of the ReaxFF Methodology for Electrolyte–Water Systems"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:batteries-interfaces
  - keyword:reaxff-parameterization
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: ""
year: 2019
authors:
  - "Mark V. Fedkin"
  - "Yun Kyung Shin"
  - "Nabankur Dasgupta"
  - "Jejoon Yeon"
  - "Weiwei Zhang"
  - "Diana van Duin"
  - "Adri C. T. van Duin"
  - "Kento Mori"
  - "Atsushi Fujiwara"
  - "Masahiko Machida"
  - "Hiroki Nakamura"
  - "Masahiko Okumura"
venue: "Supporting information (J. Phys. Chem. A)"
pdf_sha256: "b6846160d03c622e0a1b922ad1395d45df53376a78108a5f5e1cc148c3c3aceb"
pdf_path: "papers/Fedkin_JPCA_Electrolyte_2019_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2019mvf3-venue-paper -->

## Summary

This PDF (`papers/Fedkin_JPCA_Electrolyte_2019_SI.pdf`) is the **Supporting Information** for **Fedkin et al.**, *J. Phys. Chem. A*, on extending **ReaxFF** to **alkali-hydroxide / oxide** chemistry in **electrolyte–water** environments relevant to **energy storage** and **aqueous electrochemistry**. The extract begins with **Section S1** heading **“ReaxFF force field development”** and shows **Figure S1–S3** captions comparing **QM** and **ReaxFF equations of state** for crystalline **LiOH**, **Li₂O**, **NaOH**, **Na₂O**, **CsOH**, and **Cs₂O**. These plots document how the fitted potential reproduces **pressure–volume** or **energy–volume** behavior for **ionic crystal** phases used as **training and validation** targets during parameter optimization. The extract’s captions name each panel explicitly: crystalline equations of state for LiOH and Li₂O in Figure S1, NaOH and Na₂O in Figure S2, and CsOH and Cs₂O in Figure S3, each juxtaposing QM and ReaxFF curves as benchmarks for the electrolyte–water parameterization effort described in the parent article.

## Methods

**2 — Force-field training (SI: crystalline equation-of-state benchmarks).** **Section S1** documents **ReaxFF** development for **alkali-hydroxide / oxide** chemistry in the **Fedkin** *J. Phys. Chem. A* **electrolyte–water** line. The opening **figures** in the local **SI** **PDF** show **P–V** / **energy–volume**-style **equations of state** comparing **QM** and **ReaxFF** for **LiOH**/**Li₂O** (**Fig. S1**), **NaOH**/**Na₂O** (**Fig. S2**), and **CsOH**/**Cs₂O** (**Fig. S3**), used to anchor **short-range** **ionic** **interactions** in the broader **fit**. **Molecular dynamics**-based **post-fit** **checks** (if any) and **any** **LAMMPS** **input** **decks** are **not** the **focus** of this **S1** **head**; see the **parent** **[[2019fedkin-j-phys-chem-development-reaxff]]** for **whether** **finite-**T **MD** **is** **reported** there. **DFT** settings (functional, **basis set**, **k**-point mesh), **ReaxFF** **optimization** weights, and **ParReaxFF** / **CMA-ES**-style **fitting** workflow are reported in the **parent** article and the full **SI**—not in the short **p1–2** extract in-repo.

**1 — MD application (if ever applied to the trained FF):** **N/A** on this **SI** **ingest**—**no** **production** **NVT**/**NPT** **trajectory** with **stated** **box** **volume** and **ps**-**long** **equilibration** is the **focus** of the **S1** **head**; **a**queous-**MD** **validation** **(if** **any)** is **in** the **VOR** **JPCA** **text** **/** **SI** **[[2019fedkin-j-phys-chem-development-reaxff]]**, **not** on this **slug**. **For** **blueprint** **N/A** **(indexed** **SI** **front** **only):** **System** (atom **count** in **a** **reported** **MD** **box**): **N/A**; **PBC** **/ boundaries** in **a** **simulation** **cell**: **N/A**; **equilibration** or **production** **duration** (**ps**/**ns**): **N/A**; **timestep:** **N/A**; **NVT**/**NPT** **line** in **Figs. S1–S3** **N/A**—**those** are **static** **equation-of-** state **(EOS)** **lattice** **sweeps** **(QM** **vs** **ReaxFF)**, not **a** **trajectory** **log**. **Thermostat / barostat** in time-dependent **MD**:** **N/A** on this page. **Temperature (K):** **N/A** in the **caption** **slices** that **only** **compare** **0** **K** **(or** **static** **T=0** **lattice)–style** **EOS** **(see** **VOR** **for** **finite-**T **MD** **if** **any)**. **P–V** **plots** in **Figs. S1–S3** **document** **bulk** **crystal** **P–V** for **alkali** **oxides**/**hydroxides** **(training** **checks)**. **External electric field:** **N/A**.

**3 — DFT** as a **primary** “**Methods**” **narrative** on this **fragment** page: **N/A** — use the **parent** **article** for **full** **QM** **reproducibility**; this **entry** only **confirms** **which** **crystals** **enter** the **S1–S3** **EOS** **plots**.
## Findings

The SI figures summarized in the extract indicate **qualitative agreement** between **QM** and **ReaxFF** **equations of state** for the listed **alkali hydroxides and oxides**, which underpins confidence in **short-ranged** ionic interactions within the broader **Li/Na/Cs/O/H** parameterization. **Quantitative** RMSE values, **additional phases**, and **liquid-water** benchmarks are in the **full SI** and main text; they are **not** exhaustively listed in `normalized/extracts` for this slug.

## Limitations

**`extraction_quality: partial`** in the manifest: the local extract captures **figure captions** but not the **entire** SI. **`doi`** is empty in front matter here because the SI file is not a standalone DOI’d object; citations must use the **parent article DOI**. This is an **SI package** in the sense of [`NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) category A.

**Confidence rationale:** `med`—grounded on extract; full numerical claims require parent PDF.

## Reader notes (navigation)

- Primary article: [[2019fedkin-j-phys-chem-development-reaxff]]
- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[2019fedkin-j-phys-chem-development-reaxff]]
- [[reaxff-family]]
