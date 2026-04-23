---
id: paper:2020kowalik-venue-bez-tytu
type: paper
title: "Bending energy of 2D materials: graphene, MoS2 and imogolite"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:water-silica-geo
  - method:dft-static
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:2d-materials
  - keyword:graphene-carbon
  - keyword:dft-static
source_refs: []
doi: "10.1039/C7RA10983K"
year: 2018
authors:
  - "Rafael I. González"
  - "Felipe J. Valencia"
  - "José Rogan"
  - "Juan Alejandro Valdivia"
  - "Jorge Sofo"
  - "Miguel Kiwi"
  - "Francisco Munoz"
venue: "RSC Adv. 8, 4577–4583 (2018)"
pdf_sha256: "781c4bfb3cd731d13078fc4090b953c49cf7df5989de5e8fc4da5bc6dedc2fef"
pdf_path: "papers/ReaxFF_others/Gonzalez_Bending energy of 2D materials- graphene, MoS2 and imogolite_PCCP_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020kowalik-venue-bez-tytu -->

!!! note "Legacy slug (manifest)"

    The **`paper_id` slug** `2020kowalik-venue-bez-tytu` is a **legacy ingest label** and does **not** reflect authorship. The **`pdf_path`** is **González *et al.*, *RSC Advances* (2018)**, DOI **`10.1039/C7RA10983K`**. See [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) section **E**.

## Summary

Despite the **legacy wiki slug**, the ingested PDF is the **RSC Advances** article **“Bending energy of 2D materials: graphene, MoS\(_2\) and imogolite”** (**2018**), which develops a **harmonic-restraint** bending protocol to extract **bending moduli** and to track **curvature-dependent electronic** responses for **graphene**, **single-layer MoS\(_2\)**, and **aluminosilicate imogolite** nanostructures. The authors position the work as connecting **mechanical bending** metrics to **electronic structure** changes that become important when layered materials are **flexed** or **wrapped** in nanodevice geometries. The study is a **DFT-focused** materials-physics contribution; it is **not** a **ReaxFF** paper even though the corpus stores the PDF under a **`ReaxFF_others/`** folder name. Automation and human readers should key off the **DOI** and **bibliography**, not the **Kowalik** token in the slug.

## Methods

**3 — Static QM / DFT (VASP, bending protocol).** **DFT** calculations (implemented in **VASP**, per the **RSC Advances** text) are reported for **graphene** and **MoS\(_2\)** using the authors’ **harmonic** **bending** **restraint** that drives **cylindrical** curvature in **steps** while **fully** **relaxing** **internal** **coordinates** between **curvature** **increments**; **PBC** are used **along** the **long** **ribbon** **edge** to model an **infinite** **strip** (see *Methods* in the **PDF**). The **RSC** paper states **LDA/PAW**-style or **(PBE+PAW)…**-level **settings** in **Sec. 2.1**—**this** page does **not** recopy every **k-mesh**/**cutoff** line; use **10.1039/C7RA10983K** for the **definitive** table. **Dispersion:** **N/A to transcribe in full** here; the **2018** **González** **et al.** work discusses **2D** **bending** **models**; **if** a **D3**-style **correction** is **stated** in the **VASP** **block**, it **lives** in the **version-of-record**. **Structures and pathways:** **bending** **reaction** **path** in **R**-**space** of **curvature** **(not** an **NEB** **chemical** **reaction** **path**); **graphene** and **MoS\(_2\)** **sheets** plus **aluminosilicate** **imogolite**-like **sheets** as **treated** in the **manuscript** (see **RSC** **for** **atomic** **counts**). **Properties:** **bending** **modulus** **(eV** **Å²** per **atom** **for** **graphene**), **band** **shifts** **(eV)** with **curvature** for **MoS\(_2\)** as **in** the **abstract**, and **stability** **us** **curvature** for **imogolite**-type **nanotube** **precursors** (**energy** **minimum** at **finite** **R** in their **data**).

**1 — MD / 2 — ReaxFF training.** **N/A —** **this** is a **VASP/DFT**-based **2D** **bending** **and** **electronic**-**structure** **study** (with **imogolite**-related **conclusions**), not **classical** **reactive** **FF** work.

**4 — Reviews.** **N/A** — **primary** **article**, not a **summary** **review**.

## Findings

For **graphene**, the authors report a **bending modulus** on the order of **~3.43 eV Å² per atom**, described as consistent with prior literature benchmarks cited in the paper. **MoS\(_2\)** emerges as much **stiffer** under bending than **graphene** in their modeling (**~11×** in the stated comparison), and **curvature** induces a **bandgap** change on the order of **~1 eV** in the results summarized in the abstract-level description. **Imogolite** shows an **energy minimum** at **finite curvature**, supporting a picture in which **curved** precursors are **thermodynamically** plausible and connecting to **self-assembly** narratives for **aluminosilicate** nanotubes. These statements follow the publication’s own summaries; any figure-extracted numbers should be checked against the **RSC Advances** PDF.

## Limitations

The corpus filename mentions **“PCCP_2018”**, but the **journal** is **RSC Advances**; keep **`pdf_path`** stable for manifest integrity. The **legacy slug** should not be renamed casually because **stable `paper_id`s** anchor links and manifests.

## Relevance to group

Useful **2D mechanics** and **oxide nanotube** context alongside **TMD** and **silica**-related work in the knowledge base; not a **reactive FF** study.

## Citations and evidence anchors

- DOI: [10.1039/C7RA10983K](https://doi.org/10.1039/C7RA10983K)

## Related topics

- [[2020hu-npj-computat-predicting-synthesizable]]
- [[graphene-nanocarbon]]
