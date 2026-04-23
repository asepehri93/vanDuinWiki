---
id: paper:2015achtyl-nat-aqueous-proton
type: paper
title: "Aqueous proton transfer across single-layer graphene"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:water-silica-geo
  - method:dft-static
  - task:experiment-integrated
  - task:validation
  - scale:atomistic
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
  - "Adri C.T. van Duin"
  - "Matthew Neurock"
  - "Franz M. Geiger"
venue: "Nature Communications 6, 6539 (2015)"
pdf_sha256: "e5a780b4bd544becd590d49cc325be4b0d1053e9300186f01df68379d493dd26"
pdf_path: "papers/Achtyl_NatureComm_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015achtyl-nat-aqueous-proton -->

## Summary

Achtyl *et al.* combine **interface-specific second-harmonic generation (SHG)** on **graphene-on-fused-silica** with **plane-wave DFT (PBE/PAW, NEB)** and **ReaxFF molecular dynamics** to argue that **aqueous protons** can traverse **monolayer graphene** reversibly during bulk **pH cycling**, communicating with **silanol acid–base chemistry** beneath the sheet. After arguing against **macroscopic pinhole** transport via SEM and diffusion-order-of-magnitude estimates, they attribute permeation to **rare atomic defects**. The modeling reports comparatively **low barriers (~0.61–0.75 eV)** for water-mediated **Grotthuss-like** transfer across **hydroxyl-terminated** defect motifs, while **pyrylium-like ether** terminations are predicted to **block** exchange; helium/hydrogen transfer is argued to be disfavored, supporting **proton selectivity**.

## Methods

**Experiments (interface electrochemistry + SHG).** Well-characterized **single-layer graphene** on **fused silica** is exposed to aqueous electrolytes at **room temperature** while the bulk **pH** is cycled between about **3** and **10** at **fixed 1 mM ionic strength**. A dual-pump flow cell (**Fig. 1a**) runs near **0.9 ml s⁻¹** as documented on the opening pages of `papers/Achtyl_NatureComm_2015.pdf`. **Interfacial second-harmonic generation (SHG)** with **~120 fs** pulses (energies below the graphene damage threshold cited in the article) tracks silanol acid–base speciation at the buried silica/water interface. **SEM** and proton-diffusion scaling estimates (developed in the article) are used to argue against macroscopic pinholes as the dominant transport route.

**Static QM / DFT (barriers and defect models).** Plane-wave DFT within the **GGA–PBE** approximation uses **projector-augmented wave (PAW)** potentials. The Methods section of `papers/Achtyl_NatureComm_2015.pdf` specifies a **400 eV** cutoff for calculations on systems **without** explicit water solvation, whereas solvated supercells use **283 eV** cutoffs for **C** and **O** (with other elements treated as stated in the article). The surface Brillouin zone is sampled with a **Monkhorst–Pack** mesh reported as **3×3×1**, and electronic energies are converged to within **1×10⁻⁵ eV** in the same section. **Nudged elastic band (NEB)** calculations map proton-transfer pathways for oxygen- versus hydroxyl-terminated defect motifs referenced in Fig. 2 and Table 1.

**DFT dispersion correction:** **N/A —** the Methods excerpt used for this note does not name an explicit **DFT-D**/**vdW** correction beyond the PBE functional; see the article/SI for any updates.

**MD application (ReaxFF).** Reactive MD uses the **ReaxFF** implementation described in the Methods section of `papers/Achtyl_NatureComm_2015.pdf` on a **(6×6)** periodic graphene sheet solvated on both sides (**~15.01 × 17.83 Å** in-plane, **30 Å** normal). Simulations are run in the **NVT** ensemble with a **0.25 fs** timestep and **Berendsen** thermostat (**100 fs** coupling constant) to control the total system temperature, with longer aggregate sampling windows reported for rare-event statistics (consult the article/SI for exact trajectory lengths).

**Force-field training:** **N/A —** the publication applies an established ReaxFF parameterization for C/H/O/water/graphene rather than reporting a new fit in this manuscript.

**Electric field / bias during MD:** **N/A —** the MD discussion focuses on neutral defect motifs; biased electrochemistry is represented experimentally rather than as constant-potential AIMD here.

## Findings

SHG traces with graphene overlaying silica match control traces on bare silica within experimental uncertainty, yet still track silanol acid–base chemistry expected only if protons communicate through the sheet—supporting permeation without requiring macroscopic tears. After ruling out macroscopic pinholes, the authors attribute transport to rare native defects. DFT/NEB and ReaxFF sampling converge on **0.61–0.75 eV** barriers for water-mediated **Grotthuss-like** proton hops through **hydroxyl-terminated** defects, whereas **pyrylium-like ether** bridges suppress exchange. **Helium** and **H\(_2\)** permeation barriers remain comparatively unfavorable in the models highlighted, supporting **selective aqueous proton** transport. The combined spectroscopy + modeling narrative contrasts defect terminations that enable versus block proton exchange; laser-averaged SHG cannot assign single-defect structures without correlative microscopy or fabrication studies.

## Limitations

- Rare-defect mechanisms require knowledge of **actual defect populations** in CVD graphene, which can vary by synthesis and transfer.
- Extract is early pages; full simulation setup and statistics live later in the PDF/SI.

## Relevance to group

**Adri C. T. van Duin** is among the co-authors; the work pairs **precision interface spectroscopy** with **atomistic modeling** of defect-mediated proton transport (consult the full article for the simulation model details used beyond the p1–2 extract).

## Citations and evidence anchors

- DOI: [https://doi.org/10.1038/ncomms7539](https://doi.org/10.1038/ncomms7539)

## Related topics

- [[reaxff-family]]
