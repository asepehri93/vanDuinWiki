---
id: paper:2015verlackt-new-journal-atomic-scale-insight
type: paper
title: "Atomic-scale insight into the interactions between hydroxyl radicals and DNA in solution using the ReaxFF reactive force field"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - material:polymer-organic
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:water-interfaces
source_refs: []
doi: "10.1088/1367-2630/17/10/103005"
year: 2015
authors:
  - "C. C. W. Verlackt"
  - "E. C. Neyts"
  - "T. Jacob"
  - "D. Fantauzzi"
  - "M. Golkaram"
  - "Y.-K. Shin"
  - "A. C. T. van Duin"
  - "A. Bogaerts"
venue: "New J. Phys."
pdf_sha256: "6ef38a20f390e494e1218c7d79b95f941e2597d3370307c9bfc207cc3351fb35"
pdf_path: "papers/Verlackt_njp_DNA_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2015verlackt-new-journal-atomic-scale-insight -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This *New Journal of Physics* article uses ReaxFF reactive molecular dynamics to follow how reactive oxygen species, especially hydroxyl radicals, attack a short DNA duplex in explicit water at room temperature—chemistry that fixed-bond force fields cannot represent. The motivation is plasma-medicine and oxidative-stress contexts where short-lived radicals reach biomolecules in solution. The work is a collaboration between Antwerp-led groups and Penn State contributors on the reactive force-field side. The abstract emphasizes bond-making and bond-breaking at nucleobases and backbone sites rather than elastic deformation of a frozen topology.

## Methods

Reactive molecular dynamics uses **ReaxFF in LAMMPS** on a **12 base-pair** DNA dodecamer in explicit water in a **33 × 33 × 48 Å** three-dimensionally periodic **supercell** at roughly **~1 g mL⁻¹** liquid density, with reactive oxygen species added for impact trajectories. After minimization, the protocol ramps temperature **0 → 300 K over 100 ps**, holds **300 K for 200 ps**, then continues **NVT** equilibration for **300 ps** total with a **Nosé–Hoover** thermostat (coupling **25 fs**). Production consists of **15** independent **500 ps** impact trajectories at **300 K** with **0.25 fs** timestep. No barostat, controlled pressure, electric field, or enhanced sampling is used; electrostatics follow the ReaxFF formulation (Coulomb plus QEq-style charges) with parameter lineage cited in the article.

**Force-field training:** **N/A —** the work **applies** a published **CH(O/N)**-class ReaxFF parametrization adapted for DNA and cites prior biomolecular parametrizations; it does not report a new global ReaxFF optimization.

**Static QM / DFT:** **N/A —** the centerpiece is ReaxFF dynamics; DFT appears through citations to prior validation of related parametrizations, not as new barrier or pathway production calculations in this study.

## Findings

The trajectories show **·OH**-driven bond-making and bond-breaking at nucleobases and backbone sites, including **8-OH-adduct** radicals on the path to **8-oxoGuanine**- and **8-oxoAdenine**-like motifs, **H-abstraction from amines**, and **partial opening** of loose DNA ends in water, as discussed with figures in `papers/Verlackt_njp_DNA_2015.pdf`. **H₂O₂** and **HO₂** are in the reactive set; the abstract notes **H₂O₂** is largely unreactive on the simulated time scale relative to **·OH**. The paper is simulation-forward: plasma–DNA experiments motivate the problem but are not used as quantitative fits at abstract level. **Fifteen** parallel runs sample stochastic attack; **OH-terminated** terminal bases are excluded from analyzed reaction statistics so end effects do not dominate pathway counts. Population timelines and numerical details should be read from the journal figures; the authors discuss force-field bias in rare channels and the gap to long biological timescales in the Discussion.

## Limitations

- **Force-field bias** in rare reaction channels; statistical sampling over **long biological times** remains approximate.
- **DNA sequence / secondary structure** dependence is only partially explored in any single study.

## Relevance to group

Demonstrates **ReaxFF deployment outside traditional materials catalysis**—here **soft matter + plasma chemistry**—with direct **van Duin group** authorship.

## Citations and evidence anchors

- Title page and abstract in `papers/Verlackt_njp_DNA_2015.pdf`; **DOI:** `10.1088/1367-2630/17/10/103005`.

## Reader notes (navigation)

- Soft-matter / plasma-medicine ReaxFF; compare method surveys under [[theme-reactive-md-corpus]].

## Related topics

- [[reaxff-family]]
- [[theme-reactive-md-corpus]]
