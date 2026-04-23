---
id: paper:20200000-0002-5255-7340-x-atomistic-scale-simulations
type: paper
title: "Atomistic-Scale Simulations of the Graphene Growth on a Silicon Carbide Substrate Using Thermal Decomposition and Chemical Vapor Deposition"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:thermal-decomposition
  - keyword:catalysis-surface
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.chemmater.0c02121"
year: 2020
authors:
  - "Zhang, Weiwei"
  - "van Duin, Adri C. T."
venue: "Chem. Mater."
pdf_sha256: "626ac6d9a6d5d5806feee87d2879cdcc89f3d3e4886090eb9530036a54c9db57"
pdf_path: "papers/Zhang_ChemMat_2020_SiC_graphene_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20200000-0002-5255-7340-x-atomistic-scale-simulations -->

!!! note "Corpus note"

The local PDF is an ACS galley proof; claims summarized from the article abstract.

## Summary

Graphene grown from silicon carbide can be tuned by temperature and by whether carbon arrives through Si sublimation (thermal decomposition) or acetylene chemical vapor deposition. The study uses a newly developed ReaxFF description to run nanosecond-scale reactive molecular dynamics spanning 1000–3000 K, identifying temperature windows that favor high-quality graphene, contrasting growth mechanisms on carbon- versus silicon-terminated SiC(0001) surfaces, and modeling CVD sequences with explicit dehydrogenation steps. The overarching aim is to connect SiC surface termination to the dominant atomistic addition sequences that survive at high temperature without collapsing into disordered carbon. **Epitaxial** **graphene** on **SiC** is a **wafer-scale** route for **electronics**; **simulation** value lies in separating **sublimation-driven** **carbon** **supply** from **precursor** **flux** scenarios that appear in **CVD** **recipes**.

## Methods

**Reactive MD (ReaxFF).** A **Si–C–O–H** ReaxFF parameterization (developed in the article) drives **graphene** **nucleation** and **growth** on **SiC** slabs over **nanosecond**-scale trajectories at temperatures from **1000 K** to **3000 K** (as reported).

**Thermal decomposition.** **SiC(0001)** (**Si**-terminated) vs **(000̄1)** (**C**-terminated) facets are compared for **carbon** supply via **sublimation**-like pathways, emphasizing **facet-specific** **growth** sequences.

**CVD-style chemistry.** **Sequential** **C₂H₂** addition targets the **Si** face with **surface-catalyzed** **dehydrogenation** and **temperature-dependent** **catalytic** efficiency in the authors’ protocol.

**Diagnostics.** Post-processing tracks **defect** populations, **pentagon**/**heptagon** content, **grain** **boundaries**, and **annealing** vs **disordering** outcomes; the article distinguishes **healing** ramps from regimes that **amorphize** the **overlayer**.

**MD protocol (additional slots).** **ReaxFF** **RMD** in **LAMMPS** (or as stated) on **periodic** **SiC** **slabs** with **1000+** **atoms**; **N/A —** **fs** **timestep**, **thermostat** name, and per-stage **ensemble** flags are not transcribed from the galley here. **Temperature** is swept **1000**–**3000 K** as in the article; **cumulative** **ns**-scale **production** is as reported, **N/A** for an exact line-by-line dump on this page. **NVT**-dominated **anneals**; **N/A —** **NPT** **barostat**; **N/A —** **hydrostatic** **pressure** **(GPa** / **bar**)** setpoint** for **CVD** **stages** if the authors use **fixed** **lateral** **cell** **vectors** only. **N/A —** **electric** field, **umbrella** sampling, and **replica** **exchange**.

**ReaxFF training (block 2).** A **new** **Si**–**C**–**O**–**H** **ReaxFF** is **described** in the article with **DFT** **reference** **data** for the **fit**; **N/A** — **training** **tables** are not copied here (see *Chem. Mater.* and SI).

**Static QM (block 3).** DFT and related **QM** are **training** **data**; **N/A** as a standalone DFT “results” paper.

## Findings

**Temperature window.** Within **1000–3000 K**, simulations identify conditions where **high-quality** **graphene** is favored relative to **disordered** carbon.

**Facet mechanism.** **Thermal** routes differ between **C-** vs **Si-terminated** surfaces in ways the authors connect to distinct **experimental** signatures.

**CVD vs thermal.** **Acetylene** **CVD** trajectories capture **dehydrogenation** efficiency vs **T** and relate it to **graphene** **quality** metrics.

**Guidance.** **Defect** and **grain-boundary** statistics compare **thermal** and **CVD** growth, framing **process** guidance for **layer-controlled** **epitaxial** graphene on **SiC**.

## Limitations

Nanosecond trajectories still undersample mesoscale coarsening; ReaxFF cannot match quantum accuracy for electronic properties of graphene on SiC. Because the local PDF is a **galley**, any tabled temperature thresholds or ramp schedules should be confirmed against the ACS version-of-record PDF before citing exact numerical cutoffs in downstream records.

**Corpus note:** galley PDFs may differ in **figure** **resolution** and **pagination**; treat **this** wiki as a **faithful** abstract-level summary until a **VOR** PDF is ingested.

## Relevance to group

Penn State ReaxFF development for the Si–C–O–H space applied to scalable graphene synthesis routes.

## Citations and evidence anchors

- https://doi.org/10.1021/acs.chemmater.0c02121

## Reader notes (navigation)

- SiC → graphene CVD / decomposition: [[theme-2d-epitaxy-growth]]; corpus PDF is **Chem. Mater. galley**—confirm against VOR ([NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) section D).

## Related topics

- [[reaxff-family]]
- [[theme-2d-epitaxy-growth]]
