---
id: paper:2019xin-qi-acs-nn9b00820
type: paper
title: "Growth mechanism of five-fold twinned Ag nanowires from multiscale theory and simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:2d-layered
  - method:dft-static
  - method:classical-md
  - method:continuum-or-mesoscale
  - task:application
  - material:metal-surface
  - scale:multiscale
candidate_tags: []
paper_keywords:
  - keyword:metallic-systems
  - keyword:dft-static
  - keyword:aimd
  - keyword:validation-experiment
source_refs: []
doi: "10.1021/acsnano.9b00820"
year: 2019
authors:
  - "Xin Qi"
  - "Zihao Chen"
  - "Tianyu Yan"
  - "Kristen A. Fichthorn"
venue: "ACS Nano (2019), 13, 4647-4656"
pdf_sha256: "cab7b645b4d80ae0d5167400a436040d10e266df022a22acfbd102b09181b4cd"
pdf_path: "papers/Others/Xin_Fichthorn_ACS_Nano_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2019xin-qi-acs-nn9b00820 -->

## Summary

Five-fold twinned silver nanowires are grown in experiments with very high aspect ratios, but the kinetic mechanisms behind anisotropic elongation remain debated. The paper combines atomic-scale modeling, mesoscale reasoning, and continuum-style growth arguments to show how strain and seed architecture on decahedral precursors can produce one-dimensional growth without requiring the extreme facet flux ratios that a purely deposition-limited picture would need when capping molecules such as PVP are the only asymmetry. The abstract frames the work as demonstrating that anisotropic surface diffusion driven by the strained wire structure, together with Marks-type {111} “notches” on decahedral seeds, accelerates diffusion along the nanowire axis and leads to heterogeneous aggregation and end trapping of atoms. The authors report that their multiscale treatment predicts decahedral Ag seeds can evolve toward nanowires with aspect ratios in the experimental range, and they emphasize coupling among deposition, diffusion, seed shape, and final aspect ratio as levers for controlled synthesis.

## Methods

The study builds on prior density functional theory work from the same group on Ag {100} versus {111} kinetics and on PVP binding, using those inputs in kinetic Wulff constructions to relate linear facet growth rates on {111} ends and {100} sides to nanowire shapes. Molecular dynamics and energy minimization probe five-fold twinned seed structures in a size range comparable to experiments. The article describes starting from an Ino decahedron with specified in-plane dimensions (on the order of **2.6×10⁵** atoms and **~28 nm** **diameter** in one construction cited in the p1–2 text), performing **MD** annealing that transforms the seed toward a **Marks**-type decahedron with {111} **notches** and stepped corners. The text compares **DFT**-based flux ratios **G₁₁₁/G₁₀₀** near **1.7–2.0** for **PVP**-capped **Ag** (insufficient alone for **aspect ratios** **~100** in a simple flux picture) with mechanisms involving **diffusion** and **seed** geometry. **Continuum** and **kinetic-Wulff** arguments appear alongside the **atomistic** **seed** survey.

**Classical/MD block (atomistic component).** **N/A —** interatomic **potential** label, **timestep**, **thermostat**/**ensemble** tags, and **PBC** details: *not restated* on this wiki; copy from *ACS Nano* **Methods**/**SI** so **repro** is faithful. **Barostat / pressure** for seed relaxation: **N/A** on this page unless the article uses **NPT** for those stages—see PDF. **Electric field:** **N/A**. **Enhanced sampling (umbrella, metadynamics, replica):** **N/A** in the p1–2 **extract**.

**DFT (referenced inputs to flux ratios and binding).** The article cites prior **DFT** work on **Ag** facets and **PVP**; **N/A** here for full **functional**/**basis** tables—use the *ACS Nano* text and cited **prior** **PRL**/group papers.

## Findings

The kinetic Wulff construction in the article illustrates that achieving aspect ratios around 100 in some experiments would require the flux to {111} facets to be nearly two orders of magnitude larger than that to {100} facets, whereas the authors’ DFT-based estimates for Ag nanowires capped only with PVP yield G₁₁₁/G₁₀₀ of roughly 1.7–2.0, a range consistent with {100}-faceted nanocubes rather than extreme wire growth. The MD-based seed survey supports a transition from an Ino decahedron to a Marks-type structure with {111} notches and irregular stepped corners, with {110} facets giving the lowest-energy corner reconstruction among those tested. The central narrative is that strain on {111} facets and the notch-bearing seed morphology funnel diffusion along the wire axis and produce end trapping, enabling high aspect ratios under less extreme flux anisotropy than a deposition-only mechanism would demand. The abstract states that decahedral Ag seeds in their model can grow into nanowires whose aspect ratios fall in the experimental range.

## Limitations

The study focuses on silver and on model kinetic inputs; solution chemistry beyond effective fluxes (halides, micelles, and other electrolyte effects) is treated indirectly through cited mechanisms from other metals rather than fully resolved for Ag in every case. Multiscale coupling simplifies real nucleation and surfactant dynamics at the electrolyte interface.

## Relevance to group

This entry is not a ReaxFF paper; it is retained as multiscale metallic nanowire growth context adjacent to reactive and classical MD threads in the knowledge base.

## Reader notes (navigation)

- [[theme-2d-epitaxy-growth]] (broader growth and 2D/nanostructure themes)
- [[reaxff-family]] (contrasts reactive FF work elsewhere in the corpus)

## Citations and evidence anchors

DOI: [10.1021/acsnano.9b00820](https://doi.org/10.1021/acsnano.9b00820)
