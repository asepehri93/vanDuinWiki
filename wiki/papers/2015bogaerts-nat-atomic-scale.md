---
id: paper:2015bogaerts-nat-atomic-scale
type: paper
title: "Atomic scale simulation of carbon nanotube nucleation from hydrocarbon precursors"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:catalysis-surfaces
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:graphene-carbon
  - keyword:catalysis-surface
  - keyword:monte-carlo-sampling
source_refs: []
doi: "10.1038/ncomms10306"
year: 2015
authors:
  - "Umedjon Khalilov"
  - "Annemie Bogaerts"
  - "Erik C. Neyts"
venue: "Nature Communications 6, 10306 (2015)"
pdf_sha256: "611abb741f2b128c29763c016988ee05f7dec6f360ac4f70ebedcafddf99c644"
pdf_path: "papers/ReaxFF_others/Khalilov_NatCommun_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015bogaerts-nat-atomic-scale -->

## Summary

The work studies **cap nucleation** of **single-walled carbon nanotubes** from **hydrocarbon** precursors on a **Ni** nanocatalyst using **combined reactive molecular dynamics and time-stamped force-bias Monte Carlo (tfMC)** with **ReaxFF**. The analysis emphasizes the role of **hydrogen** (rehydrogenation vs dehydrogenation) and introduces a **dehydrogenation metric (k-coefficient)** to distinguish **incubation**, **cap formation**, and **growth** stages. Against prior simulation literature that had made limited progress on how the **hydrocarbon precursor** steers nucleation, the authors argue for an atomic-scale mechanism in which hydrogen mediates rearrangements that produce **labile carbon motifs**—including structures discussed as consistent with transient experimental signatures and with early-stage multi-walled CNT growth in the article. Results are reported to align with available experimental and quantum-mechanical references while giving an incubation–nucleation picture at the atomistic level.

## Methods

### MD application (atomistic dynamics)

The workflow alternates **gas impingement**, short **reactive MD** segments, and **time-stamped force-bias Monte Carlo (tfMC)** to access **CNT cap nucleation** on a **Ni₅₅** nanocatalyst at **1000–2000 K** (**Nature Communications** Methods). **ReaxFF** treats **Ni/C/H** bond making and breaking during adsorption, relaxation, and cap reorganization (parameter lineage cited in the PDF). **tfMC** moves **all atoms** each attempt with stochastic displacements of order **~0.1 Å**, much larger than typical MD steps, to cross bottlenecks faster than brute-force MD; **canonical Bussi** thermostatting equilibrates the cluster, which sits on a **virtual Al or Si** support modeled with a **z-integrated Lennard–Jones** interaction. Precursors (**CH₄**, **C₂H₂**, **C₆H₆**) impinge while the **total gas-phase molecule count** is held fixed; after adsorption, **tfMC** relaxation runs **without** further impingement. Simulations use a **3D periodic** cell with **Ni₅₅** plus variable adsorbate loadings (intermediate geometries in figures/Methods). **Barostat, applied electric fields, and replica-exchange sampling:** **N/A —** not used; effective gas environment is set by the impingement protocol rather than **NPT** reactor control. **MD integration timestep (ReaxFF segments between tfMC):** **N/A —** not restated in the short extract used for this note; the article Methods/SI give segment lengths and integrator settings for the reactive **MD** windows that bracket **gas impingement** and **tfMC** relaxation (`papers/ReaxFF_others/Khalilov_NatCommun_2015.pdf`).

### Force-field training

**N/A —** the publication applies an established **ReaxFF** parameterization for **Ni/C/H** chemistry (see references in the PDF) rather than reporting a new QM fit in this article.

### Static QM / DFT

**N/A —** primary mechanistic evidence is from reactive MD + tfMC sampling (with comparisons to cited QM/experiment in discussion).

## Findings

Cap nucleation from hydrocarbons is organized as **incubation → cap formation → continued growth**, with **hydrogen** mediating pathways between adsorbed precursors and labile carbon networks at the catalyst edge—i.e., **hydrogen** steers **rearrangement** and **decomposition** of transient carbon motifs seen in **growth** simulations. **(Re)hydrogenation** versus **dehydrogenation** competition modulates under-coordinated carbon; a **dehydrogenation metric (k-coefficient)** resolves substages within incubation. The authors compare trajectories to selected **experimental** micrographs/trends and **QM** references for key bond-making and bond-breaking events, while noting **limitations** of the impingement protocol versus real **CVD** **temperature** and **flux** control. **Sensitivity** to precursor identity (**CH₄**, **C₂H₂**, **C₆H₆**) enters through the staged **adsorption** chemistry.

## Limitations

tfMC accelerates configuration sampling but **does not reproduce exact dynamical paths**; mapping to a specific CVD reactor requires matching **temperature**, **hydrocarbon identity**, and **effective flux/coverage** beyond the idealized impingement protocol.

## Relevance to group

Demonstrates **ReaxFF** + **accelerated dynamics** for **catalytic CNT nucleation** with explicit **hydrocarbon** feedstocks—adjacent to **van Duin**-line reactive carbon/metal parameterization literature cited in the article.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
