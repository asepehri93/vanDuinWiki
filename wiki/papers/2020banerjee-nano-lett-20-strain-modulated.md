---
id: paper:2020banerjee-nano-lett-20-strain-modulated
type: paper
title: "Strain Modulated Superlattices in Graphene"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:2d-materials
  - keyword:graphene-carbon
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1021/acs.nanolett.9b05108"
year: 2020
authors:
  - "Riju Banerjee"
  - "Viet-Hung Nguyen"
  - "Tomotaroh Granzier-Nakajima"
  - "Lavish Pabbi"
  - "Aurelien Lherbier"
  - "Anna Ruth Binion"
  - "Jean-Christophe Charlier"
  - "Mauricio Terrones"
  - "Eric William Hudson"
venue: "Nano Lett."
pdf_sha256: "4ca0947fb209bc0af57665f527a2b05830de159819c61be21bdec3c72b32d4c1"
pdf_path: "papers/Others/Banerjee_ACS_Nano_2020_graphene_strain.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020banerjee-nano-lett-20-strain-modulated -->

Scanning tunneling microscopy on rippled graphene under large in-plane strain combined with atomistic electronic-structure modeling shows short-wavelength periodic strain and bond-length modulations that act as an effective electronic superlattice distinct from conventional Landau quantization.

## Summary

The study demonstrates **rippled graphene** under extreme (**>10%**) strain on a substrate, producing **spatially oscillating strain** at a wavelength small compared to typical magnetic length scales. STM imaging resolves modulated local density of states. Tight-binding or continuum modeling (as described in the paper) relates the ripple geometry and bond distortions to **pseudomagnetic-field-like** electronic effects and a **superlattice** within a single graphene sheet, offering a strain-engineering route toward effective lateral heterostructures. The **Nano Lett.** report connects **nanoscale** **corrugation** to **electronic** **modulations** without requiring **multi-layer** **stacking** or **external** **magnetic** **fields**.

## Methods

- **Experiment:** STM/STS on nanoscale rippled graphene prepared to host high, spatially varying strain; displacement-field parameters for matching simulated LDOS are quoted in the article (e.g., simulations using \(\lambda = 20\) nm, \(h_0 = 2.5\) nm, \(u_0 = 3.5\) Å stated in the Nano Lett. text for LDOS comparison).
- **Theory:** Atomistic calculations of electronic structure in strained graphene (tight-binding framework as presented) to interpret periodic LDOS peaks; comparison of peak spacing to experiment (e.g., simulated spacing \(\sim\)80 meV versus experimental \(\sim\)69(3) meV stated in the paper).

**Sample** **fabrication** details, **STM** **tip** **conditions**, and **tight-binding** **parameter** choices appear in `papers/Others/Banerjee_ACS_Nano_2020_graphene_strain.pdf` with **supplementary** **figures** referenced in the main text.

**DFT (not primary here).** The study’s **theory** layer is a **tight-binding** or similar **atomistic** **band** model for **strained** **graphene** **LDOS**; **N/A** — this page does not substitute a full **Kohn–Sham** DFT **Methods** list from the *Nano Lett.* file. If the SI cites **PBE**/**PAW** spot checks, treat them as supporting: **N/A** for a copied **functional**/**k-mesh** table in this **wiki**. **Dispersion / vdW:** **N/A** — the **primary** model is not a **DFT**+**D3** **supercell** **study**; any **Grimme**-style **correction** is **N/A** at the level of the **tight-binding** **LDOS** **workflow** summarized here.

**MD (not used).** **N/A** — not an MD paper.

## Findings

- Short-wavelength periodic strain creates **spatially oscillating pseudogauge fields** and LDOS modulations that differ from familiar large-scale strain or uniform magnetic-field (Landau) pictures.
- Graphene ripples induce **large carbon–carbon bond-length variations**, interpreted as an **effective electronic superlattice** embedded in a single sheet.
- Simulated LDOS peak spacing is **consistent with** experimental STM spectra, supporting the strain-superlattice interpretation.

The **authors** highlight **bond-length** **modulation** maps as **evidence** that **electronic** **superlattice** **periodicity** tracks **mechanical** **ripples** rather than **substrate** **moiré** alone in the **showcased** **geometry**.

**Corpus honesty / PDF.** Use `pdf_path` for any **tight-binding** **mesh** and **λ**, **h₀** **geometry**; **N/A** to re-key every **D**-vector here.

## Limitations

The work focuses on specific rippled geometries and substrate conditions; generality to all growth platforms and quantitative long-range disorder effects may require further study.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

**Peripheral** to the group’s ReaxFF-centric corpus: primarily **STM plus electronic structure theory** on graphene, not reactive MD.

## Citations and evidence anchors

- DOI: [10.1021/acs.nanolett.9b05108](https://doi.org/10.1021/acs.nanolett.9b05108)

## Related topics

- [[graphene-nanocarbon]]
