---
id: paper:2015achtyl-venue-untitled
type: paper
title: "Aqueous proton transfer across single-layer graphene"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - method:dft-static
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:aimd
  - keyword:graphene-carbon
  - keyword:water-interfaces
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1038/ncomms7539"
year: 2015
authors:
  - "Jennifer L. Achtyl"
  - "Raymond R. Unocic"
  - "Lijun Xu"
  - "Yu Cai"
  - "Muralikrishna Raju"
  - "Weiwei Zhang"
  - "Robert L. Sacci"
  - "Ivan V. Vlassiouk"
  - "Pasquale F. Fulvio"
  - "Panchapakesan Ganesh"
  - "David J. Wesolowski"
  - "Sheng Dai"
  - "Adri C. T. van Duin"
  - "Matthew Neurock"
  - "Franz M. Geiger"
venue: "Nat. Commun."
pdf_sha256: "2dc2bc3ba04e3b4c788a8c97421828bfc074bdb6977738d60f42d9dbb023e4a7"
pdf_path: "papers/Achtyl_NatureComm_2015_proof.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015achtyl-venue-untitled -->

## Summary

Proton-selective transport through nominally impermeable graphene would reconcile disparate observations from electrochemistry and membrane physics if rare defects enable Grotthuss-like hopping while blocking larger penetrants. This *Nature Communications* article combines electrochemical cells that cycle bulk pH across single-layer graphene on fused silica with second-harmonic generation probes of the buried interface, density functional theory barrier estimates for model defects, and ReaxFF molecular dynamics sampling of reactive pathways. Weiwei Zhang and Adri C. T. van Duin contribute Penn State simulation support alongside experimental collaborators at Northwestern and national laboratories. The central claim is that aqueous protons traverse native nanoscale defects with hydroxyl-rich terminations at substantially lower barriers than helium or dihydrogen, yielding selective interfacial acid–base communication without macroscopic pinholes.

## Methods

This slug registers the **Nature Communications author proof** PDF (`papers/Achtyl_NatureComm_2015_proof.pdf`) for the same article summarized on [[2015achtyl-nat-aqueous-proton]] (**DOI `10.1038/ncomms7539`**); prefer the **version-of-record** PDF for citations when available.

**Experiments** use dual-pump flow cells to cycle bulk **pH** (~**3–10**) at **fixed 1 mM ionic strength** while **interfacial SHG** tracks silanol chemistry beneath monolayer graphene on fused silica; **SEM** and diffusion-order arguments exclude macroscopic pinholes as the dominant route (proof PDF).

**Static QM / DFT** employs **GGA–PBE** with **PAW** potentials, **400 eV** plane-wave cutoff for dry cells versus **283 eV** for **C/O** in solvated cells, **3×3×1** **k** sampling, and **NEB** pathways for hydroxyl- versus oxygen-terminated defects as tabulated in the article.

**Molecular dynamics** with **ReaxFF** runs **NVT** dynamics with a **0.25 fs** timestep and **Berendsen** thermostat (**100 fs** coupling) on a **(6×6)** graphene supercell (**~15.01 × 17.83 Å** in-plane, **~30 Å** vacuum normal) with explicit water placement from Methods. **In-plane PBC** applies with finite vacuum normal separation between images. **Temperature** is **300 K** for the reactive segments quoted; cumulative sampling **duration** for rare permeation events is given in **ps** in the article/SI—read `papers/Achtyl_NatureComm_2015_proof.pdf` rather than inferring totals here. **Force-field training** and **NPT barostat** stages are **not** reported as new fits for this manuscript; the ReaxFF block is constant-volume **NVT** without hydrostatic barostat control in the excerpted protocol.

## Findings

Reversible bulk pH cycles still produce silica-surface acid–base responses equivalent (within uncertainty) to bare silica controls, implying proton permeation through nominally intact graphene. DFT/ReaxFF defect models associate permeation with **0.61–0.75 eV** barriers for hydroxyl-terminated pathways participating in **Grotthuss-like** relays, while **pyrylium-like ether** bridges shut down exchange; **He** and **H\(_2\)** barriers remain unfavorable in the motifs highlighted, supporting proton selectivity. Prefer **[[2015achtyl-nat-aqueous-proton]]** for long-term citations; keep this slug for proof-PDF provenance.

## Limitations

Second-harmonic probes interfacial populations averaged over the laser footprint; rare-defect transport inferred indirectly may not resolve single-defect structural assignments without complementary microscopy or atom-by-atom fabrication. DFT barrier estimates and ReaxFF trajectories simplify solvent polarization, image-charge effects, and full electrochemical potential control relative to biased electrochemical cells.

## Relevance to group

Weiwei Zhang and Adri C. T. van Duin contributed Penn State simulation support alongside Northwestern and national-laboratory experimental partners, making the paper a cross-linked reference for graphene–electrolyte selectivity and charge-assisted reactive modeling in the corpus.

## Citations and evidence anchors

- DOI: [10.1038/ncomms7539](https://doi.org/10.1038/ncomms7539) — *Nat. Commun.* **6**, 6539 (2015); proof PDF `papers/Achtyl_NatureComm_2015_proof.pdf`.

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
