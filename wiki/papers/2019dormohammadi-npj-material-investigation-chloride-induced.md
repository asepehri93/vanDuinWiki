---
id: paper:2019dormohammadi-npj-material-investigation-chloride-induced
type: paper
title: "Investigation of chloride-induced depassivation of iron in alkaline media by reactive force field molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:water-silica-geo
  - material:metal-surface
  - material:cement-mineral
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:oxide-surface
  - keyword:reactive-md
  - keyword:validation-experiment
source_refs: []
doi: "10.1038/s41529-019-0081-6"
year: 2019
authors:
  - "Hossein DorMohammadi"
  - "Qin Pang"
  - "Pratik Murkute"
  - "Liney Arnadottir"
  - "O. Burkan Isgor"
venue: "npj Materials Degradation 3, 19 (2019)"
pdf_sha256: "5d80f62a89c24634700c71389139fe9df803a816eb938262ac001c098756d1ea"
pdf_path: "papers/ReaxFF_others/DorMohammadi_npjMatDeg_FeClNa_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019dormohammadi-npj-material-investigation-chloride-induced -->

## Summary

DorMohammadi *et al.* combine **ReaxFF molecular dynamics**, **electrochemical** measurements, and **X-ray photoelectron spectroscopy** to study **chloride-induced depassivation** of **iron** in strongly **alkaline** media (*npj Materials Degradation*, DOI `10.1038/s41529-019-0081-6`). The scientific target is a longstanding infrastructure and materials question: how **chloride** destabilizes **passive oxide** films that otherwise protect steel in **high-pH** environments such as **cementitious** pore solutions. The authors align simulations with experiments on **pure iron** to reduce compositional ambiguity while preserving the **Fe–oxide–electrolyte** chemistry central to corrosion science. At the narrative level, the integrated story emphasizes **local acidification** near the **oxide/electrolyte** interface, **iron dissolution**, and **cation vacancy** dynamics in the passive film, with **chloride** acting as a **catalyst** for **defect** formation rather than necessarily as a species that must fully **penetrate** a thick barrier—consistent with **point-defect** and **film breakdown** pictures discussed in the corrosion literature.

## Methods

**Experiments (electrochemistry + XPS).** The study reports **electrochemical** measurements and **X-ray photoelectron spectroscopy (XPS)** on **99.95% Fe** specimens prepared/polished as described in the article, exposed to **pH ~13.5 NaOH** electrolytes with controlled **chloride** additions intended to connect to **alkaline corrosion** contexts (details of polishing, chambers, and electrochemical schedules are in the PDF).

**Reactive MD (ReaxFF, LAMMPS, XSEDE).** **Engine / code:** **ReaxFF-MD** is implemented in **LAMMPS** and run on **XSEDE** resources as stated in the article. **Boundaries / periodicity:** the **Fe / passive film / electrolyte** **supercell** uses **3D periodic boundary conditions (PBC)** in the published setup (with **vacuum** spacing and **slab** geometry along the non-metallic direction as detailed in the **PDF**). **Temperature / pressure framing:** simulations are reported at **room temperature (300 K)** with **“standard atmospheric pressure (1 atm)”** noted as part of the simulation framing, while the thermostat/ensemble paragraph is written for **canonical (NVT)** sampling. **Timestep:** **0.1 fs** with **Velocity Verlet** integration. **Thermostat:** **Nosé–Hoover** for **NVT**. **COM constraint:** the **center of mass** of the system is **fixed** to remove rigid-body translation. **Initial state / electrolyte geometry:** initial **solution density** and **vacuum slab** dimensions are set using **solution density at 300 K** as described in the article. **Barostat:** **N/A —** the excerpted protocol emphasizes **NVT** temperature control rather than **NPT** stress control.

**Force-field provenance / validation hooks.** The manuscript cites **ReaxFF** parameter sources for **Fe/Na/O/H/Cl** interactions drawn from prior parameterizations (**Aryanpour**, **Rahaman**, **Psofogiannakis** lines as named in the paper) and reports comparing selected **surface formation energies** and **water adsorption energies** on **Fe(110)** against **DFT** references as a consistency check.

**Electric fields / enhanced sampling.** **N/A —** not summarized as part of the core MD protocol text excerpted for this note.

**Production length / staged sampling.** The article discusses **chloride exposure** trajectories on **multi-nanosecond** scales in the **Results**/**figures** (e.g., **PDF** comparisons shown out to **2000 ps** in the extracted figure caption region); use the **npj Materials Degradation** PDF for exact run lengths and any separate equilibration stages beyond **energy minimization** as stated.
## Findings

The authors argue that **depassivation** begins with **localized** **electrolyte acidification** adjacent to the **passive film**, which promotes **Fe** release and drives **iron vacancy** accumulation within the **oxide** network. **Chloride** is associated with **accelerated vacancy formation** and **migration** toward the **metal/oxide** interface in the simulated mechanisms, supporting a view where **chloride** **catalysis** of **defect chemistry** can precede catastrophic breakdown even when macroscopic **film thickness** appears modestly perturbed. **Experiments** corroborate the broad **electrochemical** trends implied by the mechanistic sequence, though the manuscript also acknowledges simplifications such as **pure Fe** substrates versus **engineering steels** and the intrinsic **time** and **length** limits of **MD** relative to **field** corrosion. For the knowledge base, the paper is a concrete **ReaxFF** application bridging **electrochemistry** and **reactive MD** for **oxide** films in **alkaline** **electrolytes**.

## Limitations

Simplified iron substrates versus industrial carbon steel; scale and time sampling limits of MD.

## Relevance to group

ReaxFF application to corrosion/passivation chemistry in alkaline environments.

## Citations and evidence anchors

https://doi.org/10.1038/s41529-019-0081-6

## Related topics

- [[reaxff-family]]
