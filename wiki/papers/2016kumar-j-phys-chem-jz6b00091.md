---
id: paper:2016kumar-j-phys-chem-jz6b00091
type: paper
title: "Interface-induced renormalization of electrolyte energy levels in magnesium batteries"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:dft-static
  - task:application
  - material:metal-surface
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.6b00091"
year: 2016
authors:
  - "Nitin Kumar"
  - "Donald J. Siegel"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "42a78b311ad96dfef6f4c5780a74930ffe54559ba8a15c1825335d72bf1cbad4"
pdf_path: "papers/Others/Mg_Kumar.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016kumar-j-phys-chem-jz6b00091 -->

## Summary

High-throughput screening of **liquid electrolytes** for **multivalent batteries** often ranks candidates using **gas-phase** or **continuum-solvated** **HOMO/LUMO** windows, implicitly assuming that **interfacial** electronic structure is a small perturbation. This **J. Phys. Chem. Lett.** communication challenges that assumption for **Mg-battery-relevant** electrodes and **organic solvents** by computing **many-body quasiparticle** corrections (**G₀W₀** on top of **DFT**) for **surface–solvent** configurations. The central claim is that **electrode–electrolyte interactions** can **renormalize** frontier orbital energies enough to **narrow** the **HOMO–LUMO gap**—by up to **~25%** for selected **high-dipole** molecules relative to gas-phase references in the datasets reported—implying faster onset of **reductive** or **oxidative decomposition** than isolated-molecule screening would predict. The letter argues that **interfacial** electronic structure must be folded into screening pipelines alongside transport metrics. **G₀W₀** is used to discuss **quasiparticle** shifts relevant to **reduction** and **oxidation** onsets, not optical spectra.

## Methods

**MD application and force-field training.** **N/A** — not an MD or force-field parametrization paper.

**Static QM / interfacial electronic structure.** The letter builds Mg-battery-relevant electrode models with common organic electrolyte solvents in interfacial geometries. Semilocal DFT relaxes structures; many-body **G₀W₀** then evaluates quasiparticle shifts of HOMO/LUMO-like levels and the HOMO–LUMO gap, isolating how electrode–electrolyte coupling moves frontier states relative to isolated-molecule references. The text argues that semilocal DFT underestimates gaps, that hybrids help isolated molecules but still miss image-charge physics at interfaces, and that **G₀W₀** is needed for the reported interfacial renormalization. The opening pages summarized in `normalized/extracts/2016kumar-j-phys-chem-jz6b00091_p1-2.txt` do not restate full DFT numerical settings (functional beyond this discussion, dispersion treatment, **plane-wave** or **localized basis** choices, **Brillouin**-zone **k**-mesh density or **Γ**-only conventions, cutoffs); use the *J. Phys. Chem. Lett.* PDF for computational tables. **Interfacial geometry** relaxation supplies **structures** for **G₀W₀** post-processing; the letter focuses on frontier **energy** shifts and **HOMO–LUMO gap** narrowing rather than phonons, full DOS, or optical spectra as primary reported observables.

## Findings

For high-dipole molecules, **G₀W₀** calculations indicate HOMO–LUMO gap narrowing by up to **~25%** compared with isolated-molecule references under the interfacial models used (`normalized/extracts/2016kumar-j-phys-chem-jz6b00091_p1-2.txt`), so electrode–electrolyte interactions can renormalize electrolyte stability windows beyond gas-phase or simple continuum-solvation screening. The letter contrasts interfacially embedded molecules with vacuum or simpler solvation pictures in the same Mg-electrolyte context and ties trends to molecular dipole and binding motif at the interface. Static QM omits explicit dynamics, entropy, and full electrolyte plus salt plus SEI complexity; the authors frame the contribution as a screening guardrail rather than a substitute for reactive MD.

**Corpus context.** Not a ReaxFF study—adjacent QM reference for electrolyte stability arguments in battery modeling.

## Limitations

**Idealized surfaces**, **static** electronic structure, and finite sampling omit **explicit dynamics**, **SEI** formation chemistry, and **entropic** contributions. This is **not** a **ReaxFF** study.

## Relevance to group

Provides **QM context** for **electrolyte stability** adjacent to the corpus’s many **battery-interface ReaxFF** efforts.

## Citations and evidence anchors

- Abstract in `papers/Others/Mg_Kumar.pdf`; **DOI:** [10.1021/acs.jpclett.6b00091](https://doi.org/10.1021/acs.jpclett.6b00091).

## Related topics

- [[reaxff-family]]
