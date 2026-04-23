---
id: paper:2005chen-venue-paper
type: paper
title: "Mechanical properties of connected carbon nanorings via molecular dynamics simulation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - method:classical-md
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.72.085416"
year: 2005
authors:
  - "Nan Chen"
  - "Mark T. Lusk"
  - "Adri C. T. van Duin"
  - "William A. Goddard III"
venue: "Phys. Rev. B"
pdf_sha256: "526290f66f3b836ea36bc4a29cc6f412eff4ac594e5807c86ba6ff124dbc8300"
pdf_path: "papers/Chen_Lusk_Nanorings_PRB2005.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2005chen-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Molecular dynamics** explores **mechanical** response of **connected carbon nanorings** (“**nanochains**” / “**nanomaile**” idealizations) built from **nanotori**. The study reports **Young’s modulus**, **extensibility**, and **tensile strength** under constraint patterns mimicking **chain** vs **mesh**-like connectivity. **Nanorings** remain stable under large tensile deformation; **modulus** and **strength** depend strongly on **side constraints**, with **Young’s modulus** spanning roughly **tens of GPa** to **TPa**-scale values in the **constrained** cases reported in the abstract, and **large recoverable strains** (on the order of **25–40%** depending on loading mode). The paper predates widespread graphene mechanics literature but anticipates network effects from covalently linked curved carbon motifs. *Phys. Rev. B* **72**, 085416 gives the full interatomic model specification and the tensile-loading ensembles for each nanoring connectivity pattern.

## Methods

### Interatomic model (checklist A)

- **ReaxFF** **hydrocarbon** reactive **FF** for **C** (and implicit **H** where applicable); authors contrast **ReaxFF** with **Brenner**-type models for **bond dissociation** and **long-range** terms (*Phys. Rev. B* **72**, 085416, Sec. II). **Parameter** details are cited to prior **ReaxFF** carbon work.

### Molecular dynamics (checklist B)

- **Engine:** **MD** using **ReaxFF** as stated in Sec. II.
- **Validation case (SWNT):** **(10,10)** tube, length **~35.9 Å**, equilibrated **5 ps** at **30 K**, then **uniaxial** tension at constant loading rate **4.45×10\(^{10}\) s\(^{-1}\)** with **0.25 fs** timestep at **30 K** (Sec. II.A).
- **Nanoring construction / equilibration:** initial **(5,5)** **armchair** toroid from **50** unit cells (**1000** **C** atoms); **annealed** **25 ps** at **500 K** to assess stability; additional ring circumferences with **30**, **40**, **65**, **85**, and **100** unit cells examined (Sec. II.B).
- **Tensile tests on rings (“nanochain” vs “nanomaile” constraints):** **MD** at **100 K**, **0.25 fs** timestep; **end** loading via embedded **(5,5)** pull rods (**Fig. 5**); **displacement rate** **0.002 Å per MD step** (**~2×10\(^{11}\) s\(^{-1}\)** strain rate as stated). Selected **snapshots** re-**annealed** **6.25 ps** at **100 K** to reduce **rate** artifacts for **modulus** extraction. Separate **ultimate strength** protocol uses tension rate **4×10\(^{10}\) s\(^{-1}\)** with **pre-rupture** structures **annealed** **6.25 ps** at **100 K** (Sec. II.C).
- **Stress / modulus definitions:** **Young’s modulus** from **differential** slope **\(E=\partial\sigma/\partial\varepsilon\)**; **cross-section** for rings taken as **twice** a **SWNT** shell area; **shell thickness** **\(h=3.354\) Å** (graphitic interlayer spacing) as discussed in Sec. II.C.

**MD checklist (integrated):** **Engine / code:** **molecular dynamics** with **ReaxFF** as described in Sec. II; **N/A — standalone MD program name** in the excerpt we indexed—confirm in `papers/Chen_Lusk_Nanorings_PRB2005.pdf`. **System:** **(10,10)** **SWNT** benchmark (**~35.9 Å** length); **(5,5)** toroidal **nanorings** with **50** unit cells (**1000** **C** atoms) plus other circumferences (**30**, **40**, **65**, **85**, **100** cells). **Boundaries / periodicity:** **N/A — explicit PBC statement** not recovered from the short extract for every geometry; the **SWNT** validation uses an elongated tube as standard in the field—see Sec. II.A–B in the PDF. **Ensemble:** **N/A — NVE/NVT/NPT** labels are not spelled out for every loading segment in our summary; runs are described by **target temperature** (**30 K**, **100 K**, **500 K**), **timestep**, and **strain rate** per Sec. II. **Timestep:** **0.25 fs** for the protocols quoted here. **Duration / stages:** **5 ps** equilibration (**SWNT**); **25 ps** **500 K** ring annealing; tensile segments with **0.002 Å per MD step** displacement (**~2×10\(^{11}\) s\(^{-1}\)** strain rate) plus **6.25 ps** **100 K** re-anneals for selected modulus snapshots (**Sec. II.C**). **Thermostat:** **N/A — thermostat algorithm** not named in the indexed extract (temperatures are specified). **Barostat:** **N/A — NPT** / barostat not stated for these mechanical tests. **Temperature:** **30 K**, **100 K**, **500 K** as quoted. **Pressure / stress:** uniaxial **tension** / **stress–strain** analysis (**Young’s modulus**, **strength**); **N/A — hydrostatic pressure** control. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**.

## Findings

- **SWNT benchmark:** **ReaxFF** gives **~1.047 TPa** average **Young’s modulus** for the **(10,10)** validation case, consistent with cited **MD**/**experiment** references (Sec. III.A, Fig. 6).
- **Ring stability:** **500 K** **annealing** yields **belt-like** equilibrated **(5,5)** rings **without** **kink** formation in these runs—contrasted with prior **Brenner–Tersoff** results for the same initial construction (Sec. III.B; Figs. 7–9).
- **Reported mechanical metrics (abstract / Sec. I):** **Young’s modulus** ranges **~19.4–122 GPa** (**unconstrained**) and **~125 GPa–1.56 TPa** (**with side constraints**); **tensile strength** **~5.72 GPa** vs **~8.522 GPa**; **maximum strain** **~39%** (**nanochain** mode) vs **~25.2%** (**nanomaile** constraints)—**fully reversible** in the simulations summarized in the abstract.
- **Density convention:** **nanoring** **mass density** quoted as **~1.467×10\(^3\) kg m\(^{-3}\)** under the paper’s **geometric** assumptions (Sec. III / II.C).

## Limitations

- **Idealized** ring **topologies** and **temperature**/**strain-rate** choices affect quantitative **moduli**; experimental **synthesis** of **nanoring** **chains** was not mature at publication.
- The 2005 hydrocarbon potential omits explicit chemistry; oxidation or cross-linking between rings—relevant to realistic carbon networks—is outside the scope of the mechanical survey reported in *Phys. Rev. B* **72**, 085416.

## Relevance to group

Direct **van Duin** / **Goddard** collaboration on **carbon** **nanostructure** **mechanics**—adjacent to **CNT** and **graphene** **materials** threads in the wiki. The emphasis on constraint-dependent modulus provides an early reminder that continuum-scale stiffness estimates from nanoscale motifs require explicit boundary ensembles, a theme that persists in modern 2D heterostructure modeling.

## Citations and evidence anchors

- **DOI:** https://doi.org/10.1103/PhysRevB.72.085416 — *Phys. Rev. B* **72**, 085416 (2005).

## Reader notes (navigation)

- Early **carbon nanostructure mechanics** with Goddard/van Duin lineage; compare later [[graphene-nanocarbon]] corpus entries.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
