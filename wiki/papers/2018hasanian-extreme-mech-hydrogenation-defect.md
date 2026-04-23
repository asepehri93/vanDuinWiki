---
id: paper:2018hasanian-extreme-mech-hydrogenation-defect
type: paper
title: 'Hydrogenation and defect formation control the strength and ductility of MoS\(_2\) nanosheets: Reactive molecular dynamics simulation'
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - method:reaxff
  - task:application
  - material:tmd
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:lammps
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1016/j.eml.2018.05.008"
year: 2018
authors:
  - "Mostafa Hasanian"
  - "Bohayra Mortazavi"
  - "Alireza Ostadhossein"
  - "Timon Rabczuk"
  - "Adri C. T. van Duin"
venue: "Extreme Mechanics Letters"
pdf_sha256: "fcca9e36483b94cef88c8419f33d73d098d12249e8cc582f206f932b565d6ab3"
pdf_path: "papers/Hasanian_ExtremeMechLett_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018hasanian-extreme-mech-hydrogenation-defect -->

## Summary

**Reactive MD (ReaxFF)** in **LAMMPS** studies **uniaxial tension** of **single-layer 2H-MoS\(_2\)** with variable **H coverage** and **point defects** (vacancy motifs aligned with experimental CVD defect taxonomy). **Hydrogenation** and **defects** strongly alter **elastic modulus**, **strength**, **ductility**, and **failure mode** (including **S–S dimerization** after yield in pristine sheets, suppressed by full hydrogenation). The work connects **mechanical design** of **TMD** nanosheets to **hydrogen** from processing or environment, where **partial** coverage can **nonmonotonically** tune modulus while **full** hydrogenation tends to **embrittle** by blocking **S–S** bond formation pathways.

## Methods

- **Code / potential:** **LAMMPS**; visualization **OVITO**; **ReaxFF** for **Mo–S–H** from **Ostadhossein et al.** (as cited in the paper).
- **Pristine sheet:** **8280** atoms; box ~**25 nm × 9.5 nm** planar; periodic **in-plane**; **timestep 0.25 fs**; energy minimization (**10⁻⁶** kcal/mol and **10⁻⁶** kcal/mol·Å criteria).
- **Equilibration:** **NPT** at room temperature; **Nosé–Hoover** thermostat and barostat with damping **62.5 fs** (T) and **625 fs** (P).
- **Loading:** **Uniaxial** engineering strain rate **1×10⁹ s⁻¹**; **NPT** on width direction to approximate uniaxial stress; stress from **virial**, averaged **250 fs** intervals; effective thickness **6.1 Å** (pristine), **8.9 Å** (full **MoS\(_2\)H\(_2\)**), interpolated by H% for partial coverage.
- **Defects:** Monovacancy motifs **V\(_S\)**, **V\(_{S2}\)**, **V\(_{MoS3}\)**, **V\(_{MoS6}\)**, **Mo\(_{S2}\)**, **S\(_2\)Mo** per **Zhou et al.** taxonomy.

## Findings

- **Pristine** MoS\(_2\) shows **yield** then **noisy** stress–strain behavior tied to **phase-like transformation** and **S–S** pairing enabled by **ReaxFF** cutoffs.
- **Hydrogenation** reduces the **phase-transformation** window; **fully hydrogenated** sheets lose the yield anomaly and **embrittle** by blocking **S–S** bond formation.
- **Elastic modulus** vs H% shows a **slight initial drop**, then **rise** after ~**5%** H; **tensile strength** drops sharply then **plateaus** near ~**40%** H.
- **Defects** degrade mechanical metrics relative to pristine; trends are interpreted for **nanodevice** mechanical design.
- Comparisons across **V\(_S\)**, **V\(_{S2}\)**, and larger **chalcogen/metal** vacancy motifs illustrate how **local stoichiometry** shifts the **failure pathway** even when **global** strain rate and **system size** are held fixed.

## Limitations

**High strain rates**, **finite defect sampling**, and **ReaxFF** transferability for **mechanical** vs **electronic** applications. The **S–S** **dimerization** pathway after yield is a **force-field-dependent** feature that should be cross-checked when translating **stress–strain** trends to **device** **failure** criteria beyond the **monotonic** tension protocol used here. **Thickness** **assumptions** for **stress** **conversion** follow the **article**’s **effective** **monolayer** **thickness** conventions; adjust consistently when comparing to **experimental** **nanoindentation** or **bulge** tests.

## Relevance to group

Direct **van Duin-group** collaboration on **TMD** **ReaxFF** mechanics.

## Citations and evidence anchors

- DOI: `10.1016/j.eml.2018.05.008`.

## Related topics

- [[reaxff-family]]
- [[2018hasanian-venue-paper]]
