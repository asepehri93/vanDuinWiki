---
id: paper:2018mo-zhang-j-phys-chem-modeling-polymerization
type: paper
title: Modeling the Polymerization Process for Geopolymer Synthesis through Reactive
  Molecular Dynamics Simulations
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:cement-mineral
- domain:water-silica-geo
- domain:reactive-md
- material:silicate-glass
- method:dft-static
- method:reactive-md-generic
- task:application
- scale:atomistic
paper_keywords:
- keyword:silica-silicate
- keyword:reactive-md
- keyword:dft-static
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcc.8b00697
year: 2018
authors:
- Mo Zhang
- N. Aaron Deskins
- Guoping Zhang
- Randall T. Cygan
- Mingjiang Tao
venue: J. Phys. Chem. C 2018, 122, 6760–6773
pdf_sha256: 04c51f8306afd8ced0fbcb9dcf569820c1d1b02aefdf711732b5c7a3a6772704
pdf_path: papers/Others/Zhang_Tao_JPCC_2018_Geopolymer_Garofalini.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018mo-zhang-j-phys-chem-modeling-polymerization -->

## Summary

This *Journal of Physical Chemistry C* study simulates **geopolymer gelation**—the solution-mediated formation of **aluminosilicate networks** used in cementitious geopolymer binders—using **reactive molecular dynamics** with the **Feuston–Garofalini** aluminosilicate reactive potential rather than **ReaxFF**. The authors first use **density functional theory** to **prerelax** reactive **silicate and aluminate monomer** motifs that seed the MD, then heat and condense systems at **Si:Al** ratios of **2** and **3** over a **650–1800 K** temperature window to capture **oligomerization**, **aggregation**, and **condensation** stages. The scientific goal is to connect atomistic **network topology** statistics—**Si–O–Al** connectivity and **Si(nAl)** distributions—to **radial distribution functions** and **bulk density** trends that can be compared with **experimental geopolymer** literature benchmarks cited in the paper.

## Methods

The workflow couples **DFT**-relaxed monomer inputs to **large-scale reactive molecular dynamics** using the **Feuston–Garofalini** reactive **aluminosilicate** potential (bond-making/breaking formalism distinct from **ReaxFF**). Simulations sweep **temperature** (**650–1800 K** in the abstract) and compare **Si:Al** ratios of **2** and **3** to interrogate **oligomerization**, **aggregation**, and **condensation** kinetics plus **gel** microstructure. Analysis emphasizes **Si–O–Al** connectivity and **Si(nAl)** distributions alongside **RDFs** and **bulk density** vs experiment-focused literature benchmarks cited in the paper (`papers/Others/Zhang_Tao_JPCC_2018_Geopolymer_Garofalini.pdf`).

### MD application (Garofalini RMD)

**Engine / code:** **Reactive MD** with the **Feuston–Garofalini** potential (**N/A — LAMMPS vs in-house** integrator name not on indexed excerpt—confirm in **Methods**). **System & PBC:** periodic **aluminosilicate** melt/gel **supercells** built from **DFT-prerelaxed** monomers (**atom** totals in article). **Ensemble:** **NVT**/**NPT** staging for the **heating** and **condensation** protocol is defined in **Methods** (exact labels per stage in **PDF**). **Thermostat / barostat / timestep:** **N/A — not transcribed** here beyond the **650–1800 K** **temperature** window quoted in the abstract. **Duration / stages:** **equilibration** and **production** segments with lengths in **ps**/**ns** accompany the three-stage **oligomerization → aggregation → condensation** narrative in **Methods**. **Pressure:** **N/A — not highlighted** in the abstract-level summary used here. **Electric field:** **N/A — not used**. **Enhanced sampling:** **N/A — not indicated** for the geopolymerization protocol summarized in the abstract.
## Findings

The authors report that computationally synthesized **geopolymer-like** gels can reproduce key **Si(nAl)** distribution signatures and **RDF** features relative to selected experimental references. **Higher temperature** accelerates **condensation** kinetics and yields **lower final bulk density** in the modeled gels, while **lower Si/Al** produces **denser** networks under the reported simulation trends. The paper is an important **contrast case** in this corpus because it demonstrates reactive MD for **geopolymer** chemistry using a specialized silicate potential rather than the van Duin-group **ReaxFF** ecosystem.

**Corpus honesty.** This work is **not** a **ReaxFF** parameterization; cite **`reactive-md-generic`** tooling and the **Garofalini** potential sections in the **PDF** for reproducibility details.

## Limitations

Community tooling and transferability for **Feuston–Garofalini**-class potentials are narrower than for ReaxFF; **alkali-ion** chemistry, long-time **curing**, and full **water activity** in real geopolymers may require additional model extensions and validation beyond the published protocol.

## Reproducibility notes

Geopolymer simulations are sensitive to **initial hydroxyl speciation**, **alkali content** (if added in extended models), and the **heating schedule** used to drive condensation. Readers should reproduce the authors’ **temperature ramps** and **composition** endpoints exactly before comparing RDF or Si(nAl) statistics across software ports. When cross-walking to **ReaxFF** cementitious literature, avoid mixing bond-order definitions: the aluminosilicate reactive form differs materially from ReaxFF’s charge equilibration and bond-order formalism. The **DFT** prerelaxation stage is load-bearing: small changes in silanol/aluminol protonation states in the optimized monomers can shift subsequent condensation cascades, so archive the exact quantum settings used to build MD initial states.

## Relevance to group

Important **contrast** case: **reactive MD** for **geopolymers** using **Garofalini-family** potentials rather than **ReaxFF**.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acs.jpcc.8b00697](https://doi.org/10.1021/acs.jpcc.8b00697)

## Related topics

- [[reaxff-family]]

