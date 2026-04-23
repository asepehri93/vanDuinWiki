---
id: paper:2025rush-geochimica-e-towards-stable
type: paper
title: "Towards stable chemical fossils for anaerobic ammonium-oxidizing bacteria in palaeoenvironmental studies: novel cyclic aliphatic hydrocarbons as potential dia- and catagenetic products of ladderane lipids"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:water-silica-geo
  - method:reaxff
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:dft-static
  - keyword:reaxff-application
  - keyword:validation-experiment
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1016/j.gca.2025.12.040"
year: 2025
authors:
  - "Darci Rush"
  - "Jan H. van Maarseveen"
  - "Jan A. J. Geenevasen"
  - "Erik Tegelaar"
  - "Jos Pureveen"
  - "Roel Klein Nijenhuis"
  - "Nick Westerveld"
  - "Md Mahbubul Islam"
  - "Adri C. T. van Duin"
  - "Stefan Schouten"
  - "Jaap S. Sinninghe Damsté"
venue: "Geochimica et Cosmochimica Acta (Journal Pre-proof)"
pdf_sha256: "bbf537068190c3ac245331d6158d1a4fb3448891654b85e3c06af1e950033b67"
pdf_path: "papers/Rush_Islam_GCA_2025_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025rush-geochimica-e-towards-stable -->

!!! abstract

Hydrous-pyrolysis oils from anammox-enriched biomass (Jaeschke et al., 2008 conditions) are screened for thermally robust cyclic hydrocarbons beyond labile ladderane lipids; two-dimensional GC–MS, preparative isolation, 2D NMR, synthesis of model compounds, and δ¹³C signatures motivate tricyclic products possibly derived from C₂₀ ladderane ethers, while ReaxFF conformer screening plus B3LYP/6-311++G** in Jaguar refine stereochemistry and relative stabilities.

## Summary

**Anammox** bacteria carry diagnostic **ladderane** lipids that do not survive deep **thermal maturity**, limiting paleoredox proxies. This study re-examines **pyrolysate oils** from prior **hydrous pyrolysis** of **anammox-rich sludge** (temperatures **>200 °C**) and identifies **novel cyclic aliphatic hydrocarbons** as candidate **long-lived** fingerprints. Analytical chemistry (**2D GC–MS**, **GC–MS**, preparative isolation, **2D NMR**, δ¹³C) constrains structures; **ReaxFF** relaxations screen many stereoisomers before **DFT** refinements and Boltzmann-style mixture estimates.

## Methods

### Hydrous pyrolysis and fractionation (Jaeschke et al. protocol)

- **Feedstock:** Dried **wastewater sludge** (~**70%** *Candidatus Kuenenia stuttgartiensis* biomass) from **Dokhaven** (**Paques B.V.**).
- **Reactors:** **75 g** solids + **500 g** distilled water in **1 L Hastelloy-C276** reactors; **14** temperature steps (**120–365 °C**), **72 h** each.
- **Oils:** Recovered for **200–365 °C** runs from water surface and reactor walls (**benzene** rinse). **Al₂O₃** column fractions (**hexane**, **hexane/DCM 9:1**, **DCM/MeOH 1:1**); **AgNO₃–silica** cleanup of saturates; **anteiso-C₂₂** internal standard for quantification (as described).

### Organic analysis

- **Chromatography / MS:** GC, GC–MS, GC-SMB-MS, and **comprehensive 2D GC–MS** per prior instrumental articles cited in the paper.
- **Isotopes:** **δ¹³C** on appropriate fractions (instrumentation referenced).
- **Structure:** **Preparative GC** isolation of a representative product (two co-eluting components), **2D NMR** assignment, comparison to **synthesized model compounds**, **mass spectral** matching.

### Computational chemistry (ReaxFF and DFT)

- **ReaxFF:** **Chenoweth et al. CHO** parameter set for **geometry optimizations** (**conjugate gradient**) of **32** starting stereoisomers of a key intermediate (**IV**); gradient threshold **0.25 (kcal/mol)/Å**; **annealing** **10–1000 K** on **16** survivors within **10 kcal/mol** of the lowest ReaxFF structure.
- **DFT:** **Jaguar 7.5**, **B3LYP**, **6-311++G(d,p)** on **down-selected** isomers; **equilibrium mixture** fractions from relative free energies (entropy neglected at **298 K** in the stated approximation).

**ReaxFF** in this work is used for **conjugate**-**gradient** **geometry** **optimization** and **short** **annealing** **temperature** **ramps** (10–1000 K) in gas-phase **cluster** **models** (**non-periodic** **boundary** **conditions**; **atom** **lists** and **stoichiometry** for intermediate **IV** isomers are defined in the **GCA** **Computational** section rather than **PBC** **slab** **supercells**)—**N/A** for a **Langevin**/**Nosé–Hoover** **thermostat**-controlled **NVT** **production** run in the same sense as long **molecular dynamics**; full **NVE**/**NVT** **Molecular** **dynamics** with **time** **step** in **fs** is **N/A** as the headline **result** (see **Jaguar** **B3LYP** block for high-accuracy **energies**). **N/A** — **ps**/**ns** **NPT** **melt** **trajectories**; **N/A** — **barostat**-controlled **GPa** **pressure**; **N/A** — **electric** **field**; **N/A** — **replica** **exchange**-style **sampling** in **ReaxFF** (the **DFT** **section** instead reports **formation** **energy**-driven **mixture** **estimates**).

## Findings

- **Pyrolysates** at **>200 °C** contain **alkyl-branched tricyclic hydrocarbons** interpreted as **4-octyl-tricyclo[7.3.0.0²,⁸]dodecane**-type frameworks (**7-4-5** ring counts) from **2D NMR**, with **mass-spectral** support via **synthetic** references.
- **δ¹³C** of isolated material matches the **strong ¹³C depletion** of **ladderane fatty acids** from the parent biomass, supporting a **biogenic ladderane** origin.
- A **mechanistic** proposal links products to **ether cleavage** and **cyclobutane rearrangement** from **C₂₀ [5]- or [3]-ladderane glycerol ethers**; **ReaxFF/DFT** rank **stereoisomer** stabilities and outline **reaction** **pathway**-style interconversion among **congeners** (see **B3LYP** **barriers** in the **article** for quantitative **ranking**). **Comparisons** to **synthesized** **standards** and **literature** **retention** times anchor the **MS** and **2D** **NMR** **identifications**; **δ¹³C** match to **source** **ladderane** **lipid** **signatures** is the key **biogenic** **line** of **evidence** (authors note **caveat**s where **laboratory** **pyrolysis** overestimates field **maturity**). **Sensitivity** to **hydrous** **pyrolysis** **temperature** **step**s (**120–365** **°C** **ladder** in the **reactor** **series**) is central to which **oil** **cuts** are examined, although this **summary** does not reproduce every **T**-bin. For **corpus** use: treat the **GCA** **pre-proof** **PDF** in `pdf_path` as possibly non-final **page** **layout**; **version-of-record** is authoritative.

## Limitations

Elsevier **journal pre-proof** PDF: layout and pagination may change. Hydrous pyrolysis is a **laboratory** maturation mimic, not a field **diagenesis** reactor.

## Relevance to group

**Adri C. T. van Duin** co-authored the **ReaxFF / computational chemistry** thread on **stereoisomer** stability and pathways.

## Citations and evidence anchors

- DOI: `10.1016/j.gca.2025.12.040` — *Geochimica et Cosmochimica Acta* (pre-proof PDF in corpus).

## Related topics

- [[reaxff-family]]
