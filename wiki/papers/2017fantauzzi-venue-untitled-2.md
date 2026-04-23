---
id: paper:2017fantauzzi-venue-untitled-2
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
  - keyword:galley-or-proof-pdf
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
pdf_sha256: "0e1157e9001c86bbb4fb8ca5eda442d4ddf8190254220ca35460411a99648f82"
pdf_path: "papers/Fantauzzi_Angewandte_PtO_2017_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017fantauzzi-venue-untitled-2 -->

## Summary

Oxidation of **Pt(111)** under **oxygen** is a classic surface-science benchmark, but many prior mechanistic pictures lean heavily on **ultrahigh-vacuum** experiments that may miss kinetics accessible under more **technologically relevant** gas pressures. This *Angew. Chem. Int. Ed.* study combines **near-ambient pressure XPS** with **ReaxFF grand-canonical Monte Carlo (ReaxFF-GCMC)** to argue that **stable, largely amorphous** surface oxides can form on **hour-long** time scales at **near-ambient** \(p(\mathrm{O}_2)\), reconciling apparent contradictions between UHV expectations and catalytic/real-gas environments. The theoretical side seeks structures and coverages consistent with experiment for **430–680 K** at **1 mbar** \(p(\mathrm{O}_2)\), where brute-force **DFT** sampling of large disordered oxide motifs is expensive. The local corpus PDF is a **galley/proof** variant; for final pagination and figure quality, prefer the version-of-record sibling page **[[2017fantauzzi-venue-untitled]]** when available in-tree.

## Methods

**A — Force-field training / fitting:** Uses a **published Pt–O ReaxFF** suitable for **surface oxide** energetics in **GCMC**; **no** new parameter optimization summarized here.

**B — Molecular dynamics / sampling:** **ReaxFF-GCMC** with **grand-canonical** **O** moves evaluates **amorphous** **oxide** motifs on **Pt(111)** at **T = 430–680 K** and **\(p(\mathrm{O}_2)=1\ \mathrm{mbar}\)** (abstract-level summary). **Equilibrium** sampling; **kinetic** pathways may require **dynamics** beyond GCMC.

**C — DFT / static QM:** **Not** the main engine for large **disordered** cells—**DFT** cited where **small-cluster** or **benchmark** comparisons apply (full article).

**D — Review / non-simulation framing:** **NAP-XPS** tracks **oxidation** vs **time** under **near-ambient** **O\(_2\)**; **galley** PDF—prefer **[[2017fantauzzi-venue-untitled]]** for **version-of-record** alignment.

**Atomistic sampling note.** Same **ReaxFF-GCMC** protocol family as **[[2017fantauzzi-venue-untitled]]**: **Monte Carlo** **O** insertion/deletion at fixed **\(T\)** and **\(\mu_\mathrm{O}\)** evaluated with **ReaxFF**, not **production MD**. **Engine:** **ReaxFF-GCMC** (see **DOI** PDF/SI). **System / boundary / MD timestep / MD thermostat / barostat:** **N/A —** **GCMC** replaces **MD** integration; **PBC** and **slab sizes** are documented in the **article** rather than duplicated here. **Duration / staging:** **NAP-XPS** tracks **oxide** growth over **multi-hour** laboratory exposures (abstract excerpt); **GCMC** sampling **length** in **MC steps**/**cycles** is defined in the **article/SI**, not as **ps/ns MD** trajectories. **Temperature:** **430–680 K** (abstract-level pairing with **NAP-XPS**). **Pressure:** **\(p(\mathrm{O}_2)=1\ \mathrm{mbar}\)** in the abstract summary. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not **metadynamics/umbrella** in the sense of **MD** enhanced sampling.

## Findings

The combined dataset supports **slow** oxide development on **laboratory** hour scales, implying that **equilibration-limited** kinetics can matter when extrapolating from fast UHV protocols. **ReaxFF-GCMC** predicts **stable amorphous** oxide films whose **coverage** and **trends** align with **NAP-XPS** under the stated **temperature** and **pressure** window, extending prior UHV-focused interpretations toward **near-ambient** realism. The work positions **GCMC** as a practical complement to DFT for **large-cell** oxide disorder on metals, while acknowledging that **kinetic** growth pathways may require dynamics beyond pure **thermodynamic** sampling. For practitioners, the paper’s significance is methodological as much as material-specific: it demonstrates a tractable route to **oxygen chemical potential–dependent** oxide films on a **close-packed** metal surface where both **experiment** and **simulation** can be compared under identical **T** and **p(O₂)** statements, reducing the risk of comparing models calibrated in vacuum to measurements taken in reactive gases. The combined NAP-XPS plus ReaxFF-GCMC workflow is also a template for other **noble metal** oxidation problems where **disorder** and **slow kinetics** frustrate brute-force **DFT** enumeration. Practitioners should still treat **GCMC** snapshots as **thermodynamic** baselines: if **oxidation** is limited by **O\(_2\)** **dissociation** or **place-exchange** kinetics, pure **grand-canonical** oxygen sampling may need to be complemented by **dynamics** for fully predictive **growth** rates.

## Limitations

GCMC emphasizes **equilibrium** sampling; full growth kinetics may require **MD** or **kinetic Monte Carlo** extensions. Galley PDFs can differ cosmetically from the **version of record**.

## Relevance to group

**van Duin**-parameter **ReaxFF** with **GCMC** for **Pt** oxidation under realistic gas pressures; integrated surface catalysis line.

## Citations and evidence anchors

- DOI: [10.1002/anie.201609317](https://doi.org/10.1002/anie.201609317)

## Reader notes (navigation)

- Version-of-record PDF: [[2017fantauzzi-venue-untitled]].

## Related topics

- [[reaxff-family]]
- [[2017fantauzzi-venue-untitled]]
