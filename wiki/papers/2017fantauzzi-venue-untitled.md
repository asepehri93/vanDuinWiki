---
id: paper:2017fantauzzi-venue-untitled
type: paper
title: "Growth of stable surface oxides on Pt(111) at near-ambient pressures"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - method:reaxff
  - method:monte-carlo
  - material:metal-surface
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:monte-carlo-sampling
  - keyword:catalysis-surface
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1002/anie.201609317"
year: 2017
authors:
  - "Donato Fantauzzi"
  - "Sandra Krick Calderón"
  - "Jonathan E. Mueller"
  - "Mathias Grabau"
  - "Christian Papp"
  - "Hans-Peter Steinrück"
  - "Thomas P. Senftle"
  - "Adri C. T. van Duin"
  - "Timo Jacob"
venue: "Angew. Chem. Int. Ed."
pdf_sha256: "ae0965e42478014e55fd879661d274ecff31a7dafd219d0a0bf0f3a3acc981e2"
pdf_path: "papers/Fantauzzi_Angewandte_PtO_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017fantauzzi-venue-untitled -->

## Summary

Fantauzzi *et al.* combine **near-ambient pressure X-ray photoelectron spectroscopy (NAP-XPS)** with **ReaxFF grand-canonical Monte Carlo (ReaxFF-GCMC)** to study **oxidation** of **Pt(111)** under **oxygen** at pressures and temperatures representative of **catalytic** environments, rather than ultra-high vacuum (UHV) reference states alone. Experiments show that **oxide formation** can require **hours** even when **thermodynamics** would suggest facile oxidation, underscoring a **kinetic** bottleneck that UHV-focused narratives may underemphasize. **ReaxFF-GCMC** samples **oxygen chemical potential**-driven insertion/deletion moves using **ReaxFF** energies to explore **disordered** **surface oxide** films that are difficult to treat with **DFT** for large **amorphous** supercells. **Adri C. T. van Duin** appears among authors, linking the study to the group’s **Pt–O** reactive parameterization line and **operando**-adjacent modeling culture.

## Methods

**A — Force-field training / fitting:** **ReaxFF** for **Pt–O** surface chemistry is used as an **existing** parametrization suitable for **oxygen insertion** energetics in **GCMC**; the article does **not** center on refitting bond parameters in this work.

**B — Molecular dynamics / sampling:** **ReaxFF grand-canonical Monte Carlo (ReaxFF-GCMC)** samples **oxygen** **insertion/deletion** at fixed **temperature** and **oxygen chemical potential**, evaluating **configurations** with **ReaxFF** to explore **disordered/amorphous** **surface oxide** films (**T = 430–680 K**, **\(p(\mathrm{O}_2)=1\ \mathrm{mbar}\)** per abstract-level summary). This is **thermodynamic** sampling rather than **long-time MD** growth kinetics.

**C — DFT / static QM:** **Not used** as the primary large-cell enumerator—**DFT** cost for **disordered** oxides motivates **ReaxFF-GCMC**; any **DFT** in the paper is supporting comparison (see full PDF).

**D — Review / non-simulation framing:** **Experiment:** **near-ambient pressure XPS (NAP-XPS)** follows **Pt(111)** **oxidation** over **hour** timescales under **O\(_2\)** above UHV—paired with simulation for **coverage**/**trend** interpretation.

**Atomistic sampling note (vs production MD).** The simulation layer is **ReaxFF grand-canonical Monte Carlo (ReaxFF-GCMC)**, i.e. **Monte Carlo** moves in **oxygen chemical potential** space evaluated with **ReaxFF**, not a long **MD** trajectory. **Engine / code:** **ReaxFF-GCMC** as reported in the article (implementation details in **SI/PDF**). **System:** **Pt(111)** surface **oxide** motifs; **supercell sizes** and **O coverage** grids are in the **full text**. **Boundaries / periodicity:** **N/A —** explicit **PBC** statements are not copied into this short wiki summary (see **PDF**). **Ensemble / timestep / thermostat / barostat:** **N/A —** **GCMC** has **no** **fs** integration **timestep** or **NVT/NPT** **thermostat** in the sense of **MD**; treat **equilibration** of the **GCMC** chain as described in-source. **Duration / staging:** **NAP-XPS** tracks **hour**-scale **oxidation** transients; **GCMC** sampling **duration** is reported in **MC statistics** in the **article**, not as **ps/ns** **MD**. **Temperature:** **430–680 K** window quoted in the abstract for the **GCMC** conditions paired with experiment. **Pressure / gas:** **\(p(\mathrm{O}_2)=1\ \mathrm{mbar}\)** in the abstract-level summary. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** **GCMC** is already a **statistical** sampling method rather than **umbrella/metadynamics**.

## Findings

**Kinetics:** **Surface oxides** develop on **hour** timescales under the experimental conditions, slower than naive extrapolation from many **UHV** experiments would suggest. **Structure:** **GCMC** with **ReaxFF** identifies **stable amorphous surface oxides** in the targeted **temperature/pressure** window, a regime where **DFT** faces **cell-size** limits for **disordered** phases. **Consistency:** Simulated **coverages** and qualitative **trends** align with **NAP-XPS** observations, supporting the joint **experiment + reactive simulation** interpretation.

## Limitations

**GCMC** emphasizes **equilibrium** sampling; **full growth kinetics** may require **MD** or **kinetic Monte Carlo** extensions. Language/edition differences between **Angew.** PDFs should be checked at the **DOI**. **NAP-XPS** timescales are experimental observables; mapping them to **GCMC** equilibria is interpretive and should cite both methods’ assumptions.

## Reader notes (navigation)

- Galley duplicate: [[2017fantauzzi-venue-untitled-2]].
- For **retrieval**, pair this entry with **operando** catalysis hubs and with **Pt** surface pages; avoid conflating **oxide** **thermodynamics** with **electrochemical** **polarization** unless the source text supports it.

## Relevance to group

**van Duin-parameter** **ReaxFF** coupled to **GCMC** for **Pt oxidation** under **realistic gas pressures**—strong **catalysis** link.

## Citations and evidence anchors

- DOI: [10.1002/anie.201609317](https://doi.org/10.1002/anie.201609317)

## Related topics

- [[reaxff-family]]

