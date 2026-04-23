---
id: paper:2018dengpan-dong-in-this-stud-multiscale-modeling
type: paper
title: "Multiscale Modeling of Structure, Transport and Reactivity in Alkaline Fuel Cell Membranes: Combined Coarse-Grained, Atomistic and Reactive Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:classical-md
  - method:hybrid-qmmm
  - method:reaxff
  - task:application
  - scale:multiscale
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:polymer
source_refs: []
doi: "10.3390/polym10111289"
year: 2018
authors:
  - "Dengpan Dong"
  - "Weiwei Zhang"
  - "Adam Barnett"
  - "Jibao Lu"
  - "Adri C. T. van Duin"
  - "Valeria Molinero"
  - "Dmitry Bedrov"
venue: "Polymers"
pdf_sha256: "41070f46fe1677dbba14643c0055c2bdd320d8ec57a47b833c89712b43f2f74e"
pdf_path: "papers/Dong_Polymers_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018dengpan-dong-in-this-stud-multiscale-modeling -->

## Summary

This **open-access Polymers** article develops a **three-tier modeling chain** for **hydrated anion-exchange membranes (AEMs)** based on **functionalized poly(phenylene oxide)**: a **high-resolution coarse-grained** model for **morphology**, an **atomistic polarizable (APPLE&P)** model for **local hydration**, **ion–water structure**, and **vehicular transport**, and **ReaxFF** for **reactive** questions such as **hydroxide transport mechanisms** (including **Grotthuss-like** behavior as framed in the paper) and **chemical degradation** pathways. The study argues that **no single model** can span this whole property space, but **sequential mapping** between resolutions enables **practical materials-by-design** guidance for **AEM** chemistry, because morphology sets the water network that both polarizable MD and reactive MD must inherit. From a **fuel-cell** perspective, **hydroxide** mobility and **chemical stability** under **alkaline** stress are coupled: **vehicular** transport baselines from **APPLE&P** help bracket when **explicit bond rearrangement** must be turned on with **ReaxFF**.

## Methods

**Coarse-grained morphology:** A **coarse-grained** representation equilibrates **hydrated anion-exchange membranes** built from **functionalized poly(phenylene oxide)** backbones; equilibrated **CG** structures are **backmapped** to atomistic coordinates for later stages (*Polymers* **Methods**).

**Polarizable atomistic MD (APPLE&P):** **APPLE&P** runs on the backmapped cells supply **morphology**, **hydration structure**, **ion–water** correlations, and **vehicular OH⁻** transport baselines while **bonds remain fixed** (non-reactive mode).

**ReaxFF reactive MD:** **ReaxFF** trajectories—typically on configurations **mapped** from **APPLE&P**—treat **bond-making and bond-breaking**, including **Grotthuss-like OH⁻** shuttling hypotheses and **chemical degradation** channels invisible to the polarizable nonreactive model. **LAMMPS** integration settings (**timestep**, **QEq**, cutoffs) appear in the open-access **PDF** tables.

**Literature scope:** The article is a primary modeling paper, not a methods-free review; background citations frame **AEM** physics for the chosen ionomer chemistry.

**Atomistic protocol spine (CG → APPLE&P → ReaxFF):** **LAMMPS** drives **APPLE&P** and **ReaxFF** on hydrated ionomer cells on the order of **10⁴–10⁵ atoms** after backmapping, with **three-dimensional periodic boundary conditions**. **NVT** sampling uses the thermostat brands and **timestep** values tabulated per stage; **temperature** setpoints near **ambient** (**300 K** class) appear in the article unless a subsection states otherwise. **Equilibration** and **multi-ns** production lengths are reported separately for **CG**, **APPLE&P**, and **ReaxFF** segments. **Barostat / pressure:** **N/A —** the summarized workflow emphasizes constant-volume **NVT** segments; confirm the **PDF** for any optional **NPT** swelling studies. **Electric field:** **N/A —** no applied field in the quoted transport analysis. **Replica / enhanced sampling:** **N/A —** no umbrella sampling or metadynamics in the excerpted multiscale chain.

**2 — Force-field training:** **N/A as a headline contribution** — the article **uses** literature **ReaxFF** and **APPLE&P** parameterizations for the membrane chemistry; any QM training citations belong to the original force-field papers referenced in *Polymers* **Methods**, not a new global refit documented as the core result here.

## Findings

- **Mechanism / outcomes:** **Multiscale coupling** is presented as necessary to capture **morphology**, **ion correlations**, and **bond-breaking chemistry** in the same **material class**; **ReaxFF** resolves **decomposition** and **Grotthuss**-like **OH⁻** events where **APPLE&P** stays nonreactive.
- **Comparisons:** **CG** morphologies are **compared** to backmapped **atomistic** snapshots before reactive segments; **literature** AEM datasets contextualize the chosen **functionalization** level.
- **Sensitivity:** **Hydration** level, **temperature**, and **functionalization** density shift channel connectivity that feeds both **vehicular** and **reactive** transport conclusions.
- **Limitations / outlook:** **Mapping** uncertainty between resolutions remains an authored caveat; **conductivity** targets require cross-checking against **experiment**.
- **Corpus honesty:** Workflow labels follow the open-access **PDF** at `pdf_path`; confirm **QEq** and **cutoff** settings when cloning **LAMMPS** inputs.

## Limitations

- **Mapping fidelity** between CG, polarizable atomistic, and ReaxFF representations introduces **uncertainty**; sensitive observables need **cross-checks**.
- **Parameter sets** and **water models** strongly affect **ionic conductivity** and **mechanistic attribution**.
- AEM morphologies evolve with hydration history; the sequential workflow assumes representative backmapped snapshots capture the ionomer heterogeneity relevant to both vehicular and reactive segments without large hysteresis errors.

## Relevance to group

**Adri C. T. van Duin** coauthorship anchors the **ReaxFF** segment of a **large collaborative** membrane modeling effort.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.3390/polym10111289` (`papers/Dong_Polymers_2018.pdf`).

## Reader notes (navigation)

- AEM / fuel-cell membrane multiscale chain: [[batteries-interfaces-reaxff]]; compare other ionomer work in [[theme-reactive-md-corpus]].

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
