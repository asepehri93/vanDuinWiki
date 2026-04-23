---
id: paper:2015huang-venue-jp5b08286
type: paper
title: "Electronic Origin of Doping-Induced Enhancements of Reactivity: Case Study of Tricalcium Silicate"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:dft-static
  - method:reaxff
  - material:cement-mineral
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:dft-static
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:oxide-surface
source_refs: []
doi: "10.1021/acs.jpcc.5b08286"
year: 2015
authors:
  - "Jian Huang"
  - "Bu Wang"
  - "Yingtian Yu"
  - "Loredana Valenzano"
  - "Mathieu Bauchy"
  - "Gaurav Sant"
venue: "J. Phys. Chem. C"
pdf_sha256: "0178ada9a4820bc7d238d05bab9b2d92a41081bdde3f271ed8567de2351ac771"
pdf_path: "papers/ReaxFF_others/Huang_Bauchy_tricalcium_siliacate_JPCC_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015huang-venue-jp5b08286 -->

## Summary

Manipulating hydration reactivity of silicates in water remains challenging because surface initiation and bulk transport both matter. This study combines density functional theory with reactive molecular dynamics on triclinic T1 tricalcium silicate (C₃S), the most reactive Portland cement clinker phase. Stoichiometric and doped variants with Mg²⁺, Al³⁺, and Fe³⁺ substitutions are constructed to isolate dopant effects at fixed polymorph. DFT evaluates water sorption energetics on low-index surfaces, while ReaxFF MD extends trajectories to capture longer-term proton transport through the bulk. The abstract argues that initial hydration follows surface chemistry, whereas longer-term hydration is controlled by bulk proton transport, and that both stages correlate with dopant-induced electronic-structure changes.

## Methods

**Static QM (DFT).** Bulk and slab models use **VASP** with **PAW** pseudopotentials and the **PBE GGA** functional (**600 eV** plane-wave cutoff, **Γ-only** **k** sampling, **0.02 eV/Å** force tolerance, **10⁻⁶ eV** energy tolerance as stated). **T1–C\(_3\)S** is used for both **pure** and **doped** crystals to isolate **dopant chemistry** from polymorph variability: **Mg\(^{2+}\)** substitutes on **Ca\(^{2+}\)** sites; **Al\(^{3+}\)** and **Fe\(^{3+}\)** are inserted **pairwise** on **Ca** and **Si** sites with overall **charge neutrality**; **Fe** cases use the preferred **antiferromagnetic** solution described in the article. **(100)** surfaces are cleaved preserving **[SiO\(_4\)]** tetrahedra; slabs use a **14 Å** vacuum gap, and a **two-unit-cell** slab (**2 × 162** atoms) is adopted after a thickness convergence check. **Single water molecule** adsorption is evaluated on symmetrically distinct surface sites with orientational variants (**H-up / H-down**) and results averaged to mitigate artificial **dipole** effects from the low-symmetry **triclinic** cleavage.

**MD application (ReaxFF hydration).** After **DFT** cleavage and relaxation, the paper drives **reactive molecular dynamics** (**ReaxFF**) on the same **pure and doped T1–C\(_3\)S** surface motifs. Bulk water is built by relaxing **405** **H\(_2\)O** molecules at **~0.99 g cm\(^{-3}\)** in a **triclinic** box shaped to each crystal, first at **300 K** under **NVT**-style **thermostat** control as stated. Those relaxed water cells are **stacked along \(z\)** onto the **DFT** surface cells (**3D periodic** supercells throughout). During hydration, a **barostat** drives the **stress tensor** normal component toward **~0 GPa** along **\(z\)** while the **in-plane lattice vectors stay fixed**; production segments run **5 ns** followed by **1 ns** for statistics, all with **Δt = 0.25 fs**. The authors explicitly bound interpretation to **nanosecond-scale** hydration and omit slower processes such as **dissolution/reprecipitation** at **microsecond** horizons. **MD engine (software name):** **N/A —** the **JPCC** text extracted from the publisher PDF does **not** name an integration package (only **ReaxFF** as the reactive model). **Replica exchange, applied electric fields:** **N/A —** not used.

**Force-field training.** **N/A —** this paper **applies** an established **ReaxFF** parameterization for reactive **Ca–Si–O–H** chemistry (cited lineage in the article) rather than reporting a new fit.

## Findings

**Outcomes / mechanism.** The **abstract** argues that **early hydration** tracks **surface electronic/chemical** features accessible to **DFT**, whereas **longer-term hydration** is dominated by **proton transport** into the bulk seen only after **multi-nanosecond ReaxFF** sampling—both stages correlated with **dopant-induced** electronic descriptors discussed in the paper.

**Comparisons / levers.** **Mg / Al / Fe** substitutions are used as controlled **electronic-structure** perturbations at fixed **T1** structure; numerical **adsorption** trends, **surface resonance** correlations, and **transport** metrics are plotted in the **JPCC** article and should be quoted from there.

**Limitations (authored).** The manuscript notes **PBE** limitations, **Γ-only** sampling choices, and that **nanosecond** reactive MD still undershoots many **curing-time** phenomena (e.g., late-stage **dissolution/reprecipitation**) that may matter for engineering cements.

## Limitations

DFT and ReaxFF each carry systematic errors; dopant space is limited to the constructed substitutions; nanosecond MD still undershoots laboratory hydration times.

## Corpus notes

Cross-link this entry with **`[[2015hegoi-manzano-acs-am5b02505]]`** when reasoning about C₃S hydration: the Manzano study emphasizes dynamic disorder whereas Huang et al. emphasize dopant electronics—together they bracket composition and mechanism controls.

Downstream MAS prompts about “doped C₃S” should cite both papers when users ask for electronic-structure versus long-timescale reactive pathways, because each answers a different failure mode in simplified reactivity models.

## Relevance to group

Template for **paired QM + ReaxFF** arguments on **cement** clinker phases.

## Related topics

- [[reaxff-family]]
