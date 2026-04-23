---
id: paper:2017liu-venue-research
type: paper
title: "Atomistic Insights into Nucleation and Formation of Hexagonal Boron Nitride on Nickel from First-Principles-Based Reactive Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:hexagonal-boron-nitride
  - material:metal-surface
  - method:reaxff
  - method:dft-static
  - task:application
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:2d-materials
  - keyword:lammps
  - keyword:nose-hoover
  - keyword:catalysis-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.6b06736"
year: 2017
authors:
  - "Song Liu"
  - "Adri C. T. van Duin"
  - "Diana M. van Duin"
  - "Bin Liu"
  - "James H. Edgar"
venue: "ACS Nano"
pdf_sha256: "faab6fdbfa612cc97964419d85dea67a603c1506ee7caff79fe1536518d9e26d"
pdf_path: "papers/Liu_ACS_Nano_BN_Nickel_2017_ASAP.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017liu-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For **exact** barriers, supercell dimensions, and run schedules, use the **peer-reviewed article** (and Supporting Information where cited).

## Summary

**Multiscale modeling** combines **periodic DFT** and **ReaxFF-based reactive MD** to study how a continuous **atomically thin hBN** lattice forms from **elemental B and N** on **Ni** substrates. **DFT** targets **adsorption and reaction energetics** for **B**, **N**, and small **B\(_x\)N\(_y\)** (x, y = 1, 2) on **Ni(111)** and **Ni(211)**, and **diffusion** paths for **B** and **N** on terraces and in the **Ni sublayer**. The work reports that **B** can diffuse competitively on the **surface** and in the **sublayer**, whereas **N** diffuses on the **surface** only. Those **QM** data inform **Ni–B** and **Ni–N** terms within **ReaxFF**. **Reactive MD** then resolves **elementary nucleation and growth** of an **hBN monolayer** from deposited **B** and **N**; nucleation proceeds from **linear BN chains** toward **branched** and **hexagonal** motifs, with **additional DFT** used in the paper to check **intermediate structures** and the consistency of the **DFT + ReaxFF** workflow. The framing ties this picture to **crystal quality**, **temperature**, and **substrate** effects in **CVD**-relevant growth.

## Methods

**1 — MD application (LAMMPS rMD on Ni slabs).** **Reactive molecular dynamics** of **hBN** growth from **elemental B and N** uses **LAMMPS**. The **Ni(111)** substrate is a **rectangular five-layer slab** with **12×12** surface atoms (**720 Ni atoms**). **Periodic boundary conditions** apply in **all directions**; **~90 Å vacuum** separates periodic images along the surface normal. The **bottom (fifth) Ni layer is fixed** to mimic bulk, while the **top four layers** relax vertically to represent **surface + sublayer**. **Equal numbers of B and N atoms (200 each)** are **deposited sequentially in pairs** from the gas phase at **random (x,y)** positions **every 0.25 ps**, with a **minimum initial B–N separation ≥1.90 Å** to suppress premature bond formation; deposition targets the **relaxed top side** only. Production runs explore **900, 1100, 1300, and 1500 K** using a **Nosé–Hoover thermostat** (cited thermostat reference in the article). Each reported trajectory is **≥6 ns** with **Δt = 0.25 fs** and **velocity Verlet** integration. **N/A — barostat / NPT during growth**: the published setup describes **thermostatted rMD** on a **slab + vacuum** geometry without an explicit **NPT** barostat for the growth segment summarized here. **N/A — external electric field** in the rMD protocol description.

**2 — Force-field training / fitting.** **Periodic DFT** on **Ni(111)** and **Ni(211)** supplies **adsorption**, **diffusion**, and **small B\(_x\)N\(_y\)** reaction data used to develop **Ni–B** and **Ni–N** terms within **ReaxFF**; the **full parameter table** is pointed to **Supporting Information** in the article.

**3 — Static QM / DFT.** **Follow-up DFT** checks **selected intermediates** along the **rMD** growth pathway for **energetic consistency** (multiscale validation described in the **Abstract** and **Results**).

**4 — Review / non-simulation framing.** **N/A**: primary **ACS Nano** study. **Galley duplicate PDF:** **`[[2017liu-venue-proof-2-pdf]]`**.

## Findings

**Outcomes and mechanisms.** **DFT** shows **B** can **diffuse** on the **surface** and in the **Ni sublayer**, whereas **N** diffuses on the **surface** only—this **asymmetry** motivates different **transport** roles during **growth**. **rMD** shows **nucleation** beginning from **linear BN chains**, progressing to **branched** motifs and ultimately **hexagonal** **hBN** patches; **subsequent DFT** on **intermediate structures** supports the **energetic plausibility** of the **ReaxFF** trajectory class and the authors’ **self-consistency** argument.

**Comparisons.** The work is positioned relative to prior **DFT** studies of **hBN**/**precursor** chemistry on **transition metals** and the need for **larger-scale dynamics** than **QM alone** allows.

**Sensitivity and design levers.** **Temperature** (**900–1500 K** in the rMD campaign), **deposition cadence**, and **substrate facet** (**(111)** slab focus in the excerpted setup) are the main **knobs** discussed for **crystal quality** and **growth morphology**.

**Limitations and outlook (as authored).** The **ASAP** PDF may differ slightly from the **final paginated** issue; use the **version-of-record** for **pagination** when citing figures.

**Corpus / PDF honesty.** Protocol details above are taken from the **ingested ASAP PDF** text; the short local extract alone is insufficient for reproduction—prefer **`pdf_path`**.


## Limitations

**ASAP** PDFs can differ slightly from the **final paginated** **ACS Nano** issue; for **pagination** and **figure** numbering in citations, prefer the **journal** **version of record** once available in your library. **Hydrogen** and **realistic precursor chemistry** in **CVD** are not the main focus of the abstract-level summary—see the full text for scope.

## Relevance to group

**Adri C. T. van Duin** and **Diana M. van Duin** (**RxFF Consulting**) co-authored the **Ni/B/N ReaxFF** development and **hBN-on-Ni** **rMD** study with **Kansas State** collaborators; this is a **core** corpus bridge between **2D hBN** **growth** and **ReaxFF** **lineage** work (see also **`[[2019song-liu-nanoscale-20-predicting-preferred]]`**).

## Citations and evidence anchors

- **DOI:** [10.1021/acsnano.6b06736](https://doi.org/10.1021/acsnano.6b06736) — PDF: `papers/Liu_ACS_Nano_BN_Nickel_2017_ASAP.pdf`.
- Duplicate **galley** PDF: **`[[2017liu-venue-proof-2-pdf]]`**.

## Reader notes (navigation)

- **Non-primary sibling:** **`[[2017liu-venue-proof-2-pdf]]`** registers the **galley** PDF for the **same** DOI.

## Related topics

- [[reaxff-family]]
- [[2019song-liu-nanoscale-20-predicting-preferred]]
- [[graphene-nanocarbon]]
