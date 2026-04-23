---
id: paper:2024ghorai-chem-mater-0-molecular-precursors
type: paper
title: "From molecular precursors to MoS2 monolayers: nanoscale mechanism of organometallic chemical vapor deposition"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:tmd
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:oxide-surface
  - keyword:2d-materials
  - keyword:catalysis-surface
candidate_tags:
  - "OM-CVD-MoCO6"
source_refs: []
doi: "10.1021/acs.chemmater.3c02675"
year: 2024
authors:
  - "Sagar Ghorai"
  - "Ananth Govind Rajan"
venue: "Chem. Mater."
pdf_sha256: "d3904c08cd06c2825933dca2b1bd3c26ea6302bb014cfd071967dd35cb1ae018"
pdf_path: "papers/Others/ghorai-govind-rajan-2024-from-molecular-precursors-to-mos2-monolayers-nanoscale-mechanism-of-organometallic-chemical.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024ghorai-chem-mater-0-molecular-precursors -->

!!! note "Authorship"
    This **Chem. Mater.** study is authored by **Ghorai** and **Govind Rajan** (IISc); **Adri van Duin** is **not** a co-author. It is included in the corpus as **adjacent** **2D CVD** theory.

## Summary

**IISc** authors **Ghorai** and **Govind Rajan** use **density-functional theory** to propose a **stepwise organometallic CVD (OM-CVD)** mechanism for **monolayer 2H–MoS₂** from **Mo(CO)₆** and **H₂S** on **amorphous SiO₂**. The pathway follows **precursor decomposition** (**decarbonylation** toward **Mo(CO)₃** fragments), **sulfidation**, transient **1T metallic Mo–S clusters**, and eventual **2H semiconducting** **flake** growth. The study contrasts **Mo-zigzag** vs **S-zigzag** edge **propagation** and relates **edge termination** to **triangular** vs **hexagonal** **island** morphologies observed experimentally. The **DFT** narrative is intended as a **mechanistic** **hypothesis generator** for **CVD** practitioners: it connects **gas-phase** **precursor** chemistry to **surface** **cluster** **isomerism** that precedes **extended** **TMD** **lattices**. **Downstream** **ReaxFF** or **kinetic Monte Carlo** projects should treat these **static** **pathways** as **starting points** that may require **refitting** **barriers** when **coverage**, **electric fields**, or **alloying** **impurities** depart from the **idealized** **SiO₂** **substrate** models used here.

## Methods

### Static DFT on amorphous SiO₂ (C)

**DFT** (**functional**/basis per *Chem. Mater.*) for **Mo(CO)\(_6\)** + **H\(_2\)S** **OM-CVD** pathway: **decarbonylation**, **sulfidation**, **Mo–S** cluster **isomerism**, **edge** propagation (**Mo-zigzag** vs **S-zigzag**) on **a-SiO\(_2\)**.

### Thermodynamics and kinetics

**H\(_2\)** **elimination** highlighted as **rate-limiting** for the featured sequence; compare **edge**-mediated growth modes in the article.

**Static QM / DFT (OM-CVD on a-SiO\(_2\)).** **Density functional theory** with **PBE** or the **hybrid**/**meta-GGA** level named in *Chem. Mater.*; **DFT**+**D**-type **vdW** treatment if used. **Plane-wave**+**PAW** (or the paper’s **localized** **basis** description) and **k-point**/**Brillouin** **sampling** for **slab**+**molecule** models. **Structures** follow **NEB**/**climbing-image** (or as stated) **reaction** **pathways** for **decarbonylation**/**sulfidation**; **properties** include **formation** **energies**, **barriers**, and **edge**-mediated **kinetics** arguments. **N/A**—**molecular-dynamics** **production** in this work (this is a **static** **QM** study per **tags**); **N/A**—**ReaxFF** in this **paper**—see **## Limitations**.

## Findings

**Precursor cracking** feeds **1T metallic Mo–S clusters** that convert toward **2H MoS₂**, with **edge kinetics** and **H removal** controlling **shape** and **growth rate** in the model. **Cluster formation energies** on **SiO₂** favor **multi-Mo** **nuclei**, consistent with experimental **nucleation** trends discussed in the paper.

**Comparisons, sensitivity, corpus note.** **Compares** model **nucleation**/**morphology** to **CVD** **experiments** cited in the paper; **sensitivity** to **edge** termination and **H**-transfer **kinetics** is a theme. **IISc** work—**not** a **van Duin**-authored page.

## Limitations

**DFT** provides **0 K** **static** pathways; **ReaxFF** is **not** used here. **Real CVD** involves **gas-phase** transport, **coverage fluctuations**, and **substrate** heterogeneity beyond a **single** **amorphous** **SiO₂** model. **Microkinetic** extrapolation from **few** **elementary** steps can **miss** **surface** **carbon** **contamination** and **chamber**-specific **impurities** highlighted experimentally in **MoS₂** growth literature. **Readers** should cite **Chem. Mater.** **metadata** from the publisher page for **volume/issue/pages** rather than relying on **filename-only** **paths** in **`papers/Others/`**. **Preprint**-style filenames in **`papers/Others/`** are **not** authoritative bibliographic identifiers by themselves; always prefer publisher metadata.

## Relevance to group

Provides **QM** **reference mechanisms** for **MoS₂** **OM-CVD** useful alongside **ReaxFF** **TMD** and **2D growth** reviews (**e.g.**, **`[[2020momeni-npj-computat-multiscale-computational]]`**) even though **Adri van Duin** is **not** an author. The page flags **IISc** authorship explicitly to avoid **incorrect** **group** attribution in **retrieval** snippets.

## Citations and evidence anchors

- DOI: `10.1021/acs.chemmater.3c02675` — *Chem. Mater.*; `papers/Others/ghorai-govind-rajan-2024-from-molecular-precursors-to-mos2-monolayers-nanoscale-mechanism-of-organometallic-chemical.pdf`; extract `normalized/extracts/2024ghorai-chem-mater-0-molecular-precursors_p1-2.txt`.

## Related topics

- [[2020momeni-npj-computat-multiscale-computational]]
- [[theme-2d-epitaxy-growth]]
