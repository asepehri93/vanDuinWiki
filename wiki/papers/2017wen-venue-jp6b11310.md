---
id: paper:2017wen-venue-jp6b11310
type: paper
title: "Surface Orientation and Temperature Effects on the Interaction of Silicon with Water: Molecular Dynamics Simulations Using ReaxFF Reactive Force Field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:water-silica-geo
  - domain:reaxff-lineage
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:tribology
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.6b11310"
year: 2017
authors:
  - "Jialin Wen"
  - "Tianbao Ma"
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
  - "Xinchun Lu"
venue: "The Journal of Physical Chemistry A (2017)"
pdf_sha256: "039b502e023d70961059f9aa09c7a2f9bc9ad453b849f27d05ea355bf214f115"
pdf_path: "papers/Wen_Silicon_water_JPC_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017wen-venue-jp6b11310 -->

## Summary

Silicon wafer processing, MEMS fabrication, and chemical–mechanical polishing rely on understanding how water interacts with low-index silicon surfaces. This study applies ReaxFF molecular dynamics in LAMMPS to compare water adsorption, dissociation, and oxidation on Si(100), Si(110), and Si(111) at 300 K and 500 K, using **periodic** **slab** models with explicit **water** films so **facet**-resolved **speciation** can be compared at matched **thermal** conditions. Periodic slab models expose crystalline surfaces to water layers, sampling molecular versus dissociative adsorption, hydrogen versus hydroxyl termination, and insertion of hydroxyl oxygen into Si–Si backbonds to form Si–O–Si bridges. The work positions results as qualitatively consistent with many experimental termination trends cited in the article.

## Methods

**Molecular dynamics (reactive).** **ReaxFF** **molecular dynamics** simulations study **H₂O** reacting with crystalline **Si(100), Si(110), and Si(111)** slabs at **300 K** and **500 K**, exposing each facet to an explicit water film so **adsorption**, **dissociation**, and **oxidation** can be compared on equal thermal footing. The excerpted **Computational details** section documents the reactive force-field energy decomposition (bond, **vdW**, Coulomb, hydrogen-bond terms) and cites the parent ReaxFF training literature for **Si/O/H** chemistry. **Periodic boundary conditions** are implied by the slab-on-water setup described in the article; exact **supercell** sizes, water column thickness, **timestep** (fs), **thermostat** choice, **NVT**/**NPT** staging, **equilibration** versus production **duration** (ps/ns), and any **barostat** parameters should be taken from the full **J. Phys. Chem. A** **PDF** (`pdf_path`) because the local `normalized/extracts` snippet ends early. **Electric fields** and **metadynamics**/**umbrella** sampling are **not** indicated in the indexed pages.

**Force-field fitting.** **N/A —** this work **consumes** a published **Si/O/H ReaxFF** parameterization trained to **quantum chemical** reference data (cited in-section); it does not report a new fit.

**Static QM / DFT.** **N/A —** trajectories are reactive MD, not **AIMD**.

**Review scope.** **N/A —** primary research article (duplicate **galley** bytes tracked separately as **`[[2017wen-venue-research]]`**).

## Findings

**Outcomes and mechanisms.** Water **adsorbs** molecularly and dissociatively on each facet; **molecular adsorption** dominates on **(100)** and **(110)**, whereas **dissociative adsorption** dominates on **(111)**. **Si(100)** trends toward **H-terminated** regions, while **(111)** becomes more **OH-rich**. **Hydroxyl oxygen** can insert into **Si–Si backbonds**, forming **Si–O–Si** bridges that **oxidize** the surface. Raising **temperature** from **300 K** to **500 K** increases dissociation and overall **oxidation** extent, matching the abstract’s statement of qualitative agreement with many experiments.

**Comparisons.** The discussion ties simulated terminations to **experimental** surface spectroscopy cited in the introduction, positioning ReaxFF as a large-scale complement to static **DFT** studies of isolated water adducts.

**Sensitivity / design levers.** **Facet orientation** and **temperature** are the explicit comparative axes; both shift the balance between molecular water, dangling **H**, and **OH** coverages that control hydrophilicity and friction in MEMS/CMP contexts.

**Limitations / outlook.** Finite cells and nanosecond-scale trajectories limit rare-event sampling; electrolyte chemistry beyond neutral water is out of scope.

**Corpus honesty.** Full numerical protocol beyond the excerpted **Computational details** header lives in the **PDF**; use **`[[2017wen-venue-research]]`** only when you must cite the duplicate **galley** ingest explicitly.

## Limitations

Finite cells and short timescales limit rare-event sampling; electrolyte chemistry beyond neutral water is outside the scope.

## Corpus notes

Pair this page with **`[[2017wen-computationa-atomistic-mechanisms]]`** when building CMP-oriented reading lists: overlapping authorship and topic make them natural siblings for retrieval even though DOIs differ.

For benchmarking, note that ReaxFF water dissociation barriers on silicon are force-field dependent; if a downstream project requires quantitative sticking coefficients, compare against experiment or higher electronic structure theory on small cluster models before scaling to large slabs.

Slab thickness and water column height in the published setups influence field effects and hydrogen-bond networks; reproduce those dimensions when comparing to other silicon oxidation papers in the corpus.

## Relevance to group

Foundational **van Duin**-group **ReaxFF + water + silicon** reference tied to manufacturing contexts.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.6b11310](https://doi.org/10.1021/acs.jpca.6b11310)

## Related topics

- [[reaxff-family]]
- [[2017wen-computationa-atomistic-mechanisms]]
