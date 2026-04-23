---
id: paper:2015cano-marquez-srep-2015-do-enhanced-mechanical
type: paper
title: "Enhanced Mechanical Stability of Gold Nanotips through Carbon Nanocone Encapsulation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:2d-layered
  - method:classical-md
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:graphene-carbon
  - keyword:metallic-systems
  - keyword:validation-experiment
  - keyword:2d-materials
source_refs: []
doi: "10.1038/srep10408"
year: 2015
authors:
  - "Abraham G. Cano-Marquez"
  - "Wesller G. Schmidt"
  - "Jenaina Ribeiro-Soares"
  - "Luiz Gustavo Cançado"
  - "Wagner N. Rodrigues"
  - "Adelina P. Santos"
  - "Clascidia A. Furtado"
  - "Pedro A. S. Autreto"
  - "Ricardo Paupitz"
  - "Douglas S. Galvão"
  - "Ado Jorio"
venue: "Scientific Reports 5, 10408 (2015)"
pdf_sha256: "555a5e67861b9499a49f894dc4d750cca5472528ff7eb5f208649bfab2d247bb"
pdf_path: "papers/ReaxFF_others/Cano_Marquez_Au_CNT_SciRep2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015cano-marquez-srep-2015-do-enhanced-mechanical -->

## Summary

Gold combines corrosion resistance with high electrical conductivity and favorable optical response, yet its pronounced plasticity makes freestanding gold nanotips unreliable for scanning-probe and nano-optics workflows where tip shape must remain stable under feedback forces. This *Scientific Reports* article reports a hybrid design in which electrochemically etched gold tips are encapsulated by multi-walled carbon nanocones and then tested as AFM probes. The experimental narrative emphasizes that bare gold tips deform irreversibly under compression with stress concentrated near the tip–substrate contact, whereas the encapsulated architecture changes how strain is distributed through the composite. Fully atomistic reactive molecular dynamics simulations are used to rationalize the contrast in mechanical response, linking the experimental observation of improved robustness to blocked atomic sliding and redistribution of mechanical load along the gold–carbon assembly. The paper also notes that sp² carbon nanostructures remain conducting and can carry magnetism associated with apex defects, framing the hybrid tip as a platform where transport, mechanics, and magnetism may be co-designed at the nanoscale.

## Methods

### Experiment (fabrication + AFM)

- **Tip synthesis / integration:** electrochemically etched **gold** tips are inserted into a purchased **multi-walled carbon nanocone (MWCNC)** bore on a **Si** substrate and **Pt-soldered** in a **dual-beam** instrument (imaging/acquisition parameters listed in *Sci. Rep.* Methods).
- **AFM testing:** the **Au@CNC** assembly is mounted on a **tuning-fork** scanner; the article compares **durability** and **imaging stability** against **bare gold** tips under feedback conditions that rapidly damage unmodified gold.

### MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** with **ReaxFF** (bond-order reactive model; **EEM** charges updated each step, as stated in *Sci. Rep.* Computational Methods).
- **Ensemble / thermostat:** **NVT** with a **Nose–Hoover thermostat** for all MD segments described in the main text.
- **Observables:** per-step **virial stress tensor** and **von Mises** stress fields are computed to visualize how stress localizes during **compression** sequences.
- **Timestep / run lengths / thermostat damping:** the main text directs readers to **Supplementary Materials** for integrator timestep, damping, and **multi-ps** trajectory lengths tied to the **compression** protocol (**N/A —** not extracted into this note from the main-text paragraph alone). Simulations use **Au** nanotip models with **multi-wall carbon nanocone** segments at atomistic resolution, **PBC** as appropriate for the supercell geometry, and **300 K NVT** control during compression; **N/A —** **NPT** barostat control is not the primary reported knob.

### Force-field training

**N/A —** the publication uses a **ReaxFF** parameterization described as trained against **DFT (PBE)** data for **Au-containing** systems (see *Sci. Rep.* references), but this is not a new parameterization paper.

### Static QM / DFT

**N/A —** DFT enters through the **ReaxFF** training narrative/citations rather than as on-the-fly QM in this study.

## Findings

- **AFM:** the **Au@CNC** tip can image **single-walled carbon nanotubes** on glass under comparatively **aggressive feedback** where **bare gold** tips fail quickly; catastrophic damage for the hybrid tip is reported to require **extreme compression** with feedback disabled.
- **MD interpretation:** compression of **bare** tips shows **localized plasticity** and **atomic-plane sliding** consistent with soft gold nanotips; the **encapsulated** tip shows **multi-stage** mechanical response with **redistributed** stress pathways attributed to the **carbon nanocone** sheath.
- **Outlook (as discussed):** authors connect **sp² carbon** conductivity and possible **magnetic** signatures tied to apex topology to broader probe applications beyond mechanical stiffening alone.
- **Comparisons:** the narrative is explicitly **experiment vs simulation** side-by-side for the same **compression** motifs (see *Sci. Rep.* figures).
- **Sensitivity:** response depends on **strain** stage, **tip–cone** integration quality, and **temperature** / dissipative details carried by the **NVT** thermostat choice (see **SI**).
- **Limitations / corpus honesty:** quantitative **stress** matching should be taken from the **PDF/SI** figures rather than this summary; the main text omits some integrator settings (**version-of-record** + **SI**).

## Limitations

Real tips vary in **cone quality**, **wall thickness**, and **interface adhesion**; the MD side omits full **instrument dynamics** and may use **idealized** boundary conditions—treat numerical stress–strain values as **illustrative** unless reproduced from the paper/SI figures.

## Relevance to group

The study is not a ReaxFF parameterization paper, but it is a clear example of how reactive atomistic models can interpret metal–sp²-carbon composite mechanics alongside microscopy, a motif that recurs in nanoelectromechanics and hybrid nanomaterials discussions relevant to broader simulation portfolios.

## Related topics

- [[graphene-nanocarbon]]
