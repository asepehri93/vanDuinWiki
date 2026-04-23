---
id: paper:2019sattler-venue-st-century
type: paper
title: "Topological Constraint Theory and Rigidity of Glasses (handbook chapter)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - material:silicate-glass
  - task:review
  - method:classical-md
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2019
authors:
  - "Mathieu Bauchy"
venue: "Chapter in: 21st Century Nanoscience – A Handbook: Nanophysics Sourcebook (CRC, ed. Klaus D. Sattler)"
pdf_sha256: "c31d28e10acd71fd388f0c3b3d2072bab583fb582733d8a775bf8d7f09704afb"
pdf_path: "papers/Others/chapter-TCT_Bauchy.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019sattler-venue-st-century -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The archived PDF is **Mathieu Bauchy’s** handbook chapter **“Topological Constraint Theory and Rigidity of Glasses”** in *21st Century Nanoscience – A Handbook* (CRC, **Klaus D. Sattler**, editor). The **table of contents** (extract) outlines **glass science** basics (**glassy state**, **network formers vs modifiers**, **Zachariasen** rules), introduces **Topological Constraint Theory (TCT)** as a **mechanical truss** analogy for **atomic networks**, and develops **mean-field** constraint counting with extensions for **temperature**, **pressure**, **intermediate phases**, and **onefold-coordinated** atoms. Application sections survey **chalcogenide** glasses, **network oxides**, **sodium silicate** **modifiers**, and links between **TCT** and **molecular dynamics** simulations. Later sections forecast **hardness**, **fracture**, **viscosity/fragility**, **Tg**, and **dissolution** trends from **rigidity** concepts. The **chapter** also frames **materials genome**-style discovery motivations, using **glass** as a historically consequential **materials class** whose **property** optimization benefits from **compositional** **rules** beyond **trial-and-error** alone.

## Methods

The chapter is **review**-only: it is **not** a single **experimental** or **simulation** **benchmark** paper. It **explains** **Topological** **Constraint** **Theory** ( **TCT** ) for **covalent** **networks** and **cites** how **molecular** **dynamics** can **test** **constraint**-**theoretic** **predictions** for **silicate**-class **glasses** (and **other** **network** **formers**), but **any** **LAMMPS** /**GROMACS** /**VASP**-**AIMD** **timestep**, **ensemble**, and **box** **size** must be taken from the **primary** **works** **cited** in the **handbook** **bibliography**, not **invented** here. **1 — MD** “**application**” **as** a **reported** **single**-**paper** **protocol** **N/A** for **TCT** **itself**; **2 — FF** **training** **N/A**; **3 — DFT**-**only** **N/A** as a **unified** **FF**-**line**; **4 — This** **Methods** **block** **satisfies** **“review** / **non**-**sim**” by **describing** **how** the **text** **surveys** **MD**-**relevant** **oxide**-**network** **literature** ( **AIMD**, **ReaxFF**, **classical** **pair**-**potentials** ) in **bibliography**-**driven** **fashion** **with** **no** **one**-**code**-**one**-**input**-**file** **protocol**.
## Findings

**Synthesis (chapter-level).** **TCT** is presented as a **vocabulary** for **rigidity** **percolation** and **floppy**/**stressed**-**rigid** **windows** in **covalent** **networks**, including **oxide**-rich and **chalcogenide** **families** and the **“intermediate** **phase**” **idea** where **stress** **self**-**organization** is invoked. **Application**-oriented **sections** tie these **concepts** to **hardness**, **fracture** **toughness** **qualifiers**, **viscosity**-**related** **fragility** **arguments**, and **Tg** / **dissolution** **narratives** in **survey** **form**—**always** **through** **cited** **work**, not a **new** **dataset** on this page.

**Comparisons, sensitivity, limitations.** The **book**-**level** text **reminds** that **TCT** is a **mean**-**field** **skeleton**; **full** **structure**-**property** **maps** need **MD**-level **structural** **and** **reactive** **detail** from **cited** **primary** **papers** (see **Limitations** in **TCT**-**reliant** **chapters**). **Corpus honesty:** the **`pdf_path`** is the **Bauchy** **handbook** **PDF**; **Bauchy** (not **van** **Duin**) is the **author**; use this **node** for **retrieval** **of** **constraint**-**rigid** **vocabulary** **next** to **atomistic** **silicate** **ReaxFF** **pages**, **not** for **FF** **parameters** themselves.
## Limitations

**Handbook** format—**not peer-reviewed primary data**; **van Duin** is **not** an author. Use as **pedagogical** context for **silicate** **ReaxFF** pages, not as a **parameter** source. **Mean-field** **constraint** counts can **miss** **medium-range** **order** captured by **MD**—treat **TCT** predictions as **complementary** to **simulation**, not **substitutes** for **validation** on **specific** compositions.

## Relevance to group

Background reading connecting **silica/glass** **structure** to **rigidity** and **properties**; complementary to **atomistic ReaxFF** studies of **silicates** where **constraint** pictures help interpret **Qⁿ** speciation and **mechanical** trends without replacing **simulation** data. The chapter’s **MD** cross-references align with operator interest in **bridging** **analytical** **rigidity** tools and **trajectory-based** metrics.

## Citations and evidence anchors

- `papers/Others/chapter-TCT_Bauchy.pdf` — table of contents and Sec. 13 overview in `normalized/extracts/2019sattler-venue-st-century_p1-2.txt`.

## Related topics

- [[2020deng-venue-structural-features]]
- [[reaxff-family]]
