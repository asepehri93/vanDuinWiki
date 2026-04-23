---
id: paper:2021sharma-carbon-180-2-coalescence-incipient
type: paper
title: "The coalescence of incipient soot clusters"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:carbon-hydrocarbon
  - method:reactive-md-generic
  - material:graphene-carbon-nano
  - task:application
paper_keywords:
  - keyword:reactive-md
  - keyword:combustion
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2021.04.065"
year: 2021
authors:
  - "Akaash Sharma"
  - "Khaled Mosharraf Mukut"
  - "Somesh P. Roy"
  - "Eirini Goudeli"
venue: "Carbon 180 (2021) 215–225"
pdf_sha256: "9c64c9b046d96656f4881d5b640ec9d6f216e2b111fc267001ec666955617348"
pdf_path: "papers/ReaxFF_others/Sharma et al._soot_growth_2021_Carbon.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021sharma-carbon-180-2-coalescence-incipient -->

!!! abstract "Scope"
    **Reactive MD** of acetylene chemistry up to nascent soot (~3.5 nm), then **isothermal coalescence** of isolated incipient clusters (800–1800 K); **surface-area evolution** used to define a characteristic coalescence time.

## Summary

Reactive molecular dynamics begins from a thousand acetylene molecules that collide, react, and polymerize into linear and branched hydrocarbons and polycyclic aromatics until nascent soot clusters of up to about 3.5 nm diameter form. Packing density and C/H ratio track nucleation. The study then isolates incipient clusters from the reactive bath and simulates pairwise coalescence at 800–1800 K, monitoring surface area to extract a characteristic coalescence time. Smaller clusters (up to roughly 760 atoms) coalesce rapidly (within ~0.1 ns), especially at 800–1000 K, whereas higher temperatures (1200–1600 K) yield more rigid, aromatic-rich particles that coalesce more slowly. Clusters beyond about 1300 atoms do not fully coalesce within the maximum 5 ns trajectories reported. The two-stage workflow separates **gas-phase** **nucleation** from **post-nucleation** **agglomeration**, which is useful when interpreting **soot** growth as a sequence of **chemistry**-limited and **diffusion**-limited steps.

## Methods

**1 — MD application (reactive two-stage workflow).** The authors use **reactive** **molecular dynamics** in **LAMMPS** (per *Carbon* **Methods**) with a **bond-order** **ReaxFF**-class or related **reactive** **force field** for **hydrocarbon**/**soot** growth. **Stage A (nucleation):** a gas-phase cell of **1000** **C\(_2\)H\(_2\)** **molecules** under **3D** **PBC** evolves to **branched** **PAH**-like and **incipient** **soot** clusters of order **3.5 nm** diameter, tracking **C/H** ratio and **packing** **density**. **Stage B (coalescence):** isolated **incipient** **clusters** are **annealed** pairwise at **800–1800** **K**; **NVT** control (see article for **thermostat** and **timestep** in **fs**), with **trajectories** up to **5** **ns** for the largest **clusters**; **surface** **area**–time **analysis** gives a **characteristic** **coalescence** time. **Barostat / isotropic** **pressure** **control:** **N/A** for the excerpted isochoric coalescence runs. **N/A — external** **electric** **field**; **N/A — umbrella** or **metadynamics** in the reported protocol.

**2 — Force-field training. N/A —** application of an existing reactive field, not a new **parameter** **fit** study.

**3 — Static QM. N/A** as the main method.

**4 — Experiments. N/A** — **computational** only.
## Findings

- Incipient soot formation proceeds through rich gas-phase chemistry to branched aromatics and nascent particles with quantified C/H and density evolution.
- Coalescence is fastest for smaller clusters at lower temperatures in the window studied; aromatic content at higher temperatures impedes coalescence within the simulated times.
- Very large clusters (>1300 atoms) remain non-coalesced within 5 ns under the investigated conditions.
- Surface-area tracking provides a first-pass timescale characterization for coalescence as described in the paper.
- The authors relate **coalescence** **time** trends to **practical** **soot** models that must parameterize **collision** efficiencies between **incipient** particles drawn from **flame** samples.

**Comparisons, sensitivity, corpus.** The two-stage design **compares** **nucleation** **chemistry** to post-**nucleation** **agglomeration**; **temperature** strongly controls how fast small **clusters** coalesce. **Limitations (corpus):** local **extract** is abstract-heavy—confirm **timestep** and **ReaxFF** **designation** in the **PDF**.

## Limitations

Force-field fidelity limits quantitative agreement with experiment; long-time agglomeration and oxidation are outside the scope. **Particle** **charge** and **ion** **seeding**, omitted here, can alter **coalescence** in real **soot** **flames**.

## Relevance to group

Corpus combustion/soot paper using reactive MD (methodological neighbor to ReaxFF combustion studies).

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2021.04.065](https://doi.org/10.1016/j.carbon.2021.04.065)

## Related topics

- [[reaxff-family]]
