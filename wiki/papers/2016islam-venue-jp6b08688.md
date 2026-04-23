---
id: paper:2016islam-venue-jp6b08688
type: paper
title: "Reductive decomposition reactions of ethylene carbonate by explicit electron transfer from lithium: an eReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:ereaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b08688"
year: 2016
authors:
  - "Md Mahbubul Islam"
  - "Adri C. T. van Duin"
venue: "Journal of Physical Chemistry C"
pdf_sha256: "66c90077f9dcaaeeea43959d07f796c667bd829872c6b85388eac88f3a8235eb"
pdf_path: "papers/Islam_eReaxFF_LiEC_JPC_C_2016.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
---
<!-- id:paper:2016islam-venue-jp6b08688 -->

## Summary

**eReaxFF** molecular dynamics treats electrons as explicit pseudoclassical carriers on top of the ReaxFF reactive framework. The authors apply it to ethylene carbonate (EC) reduction initiated by electron transfer from lithium, following ring opening toward EC⁻/Li⁺-type radicals and subsequent radical termination without predefining a reaction network—chemistry relevant to solid-electrolyte interphase formation in Li-ion cells. The abstract argues that **eReaxFF** tracks literature quantum-chemistry energetics for EC decomposition better than standard ReaxFF, which mishandles electron-affinity-sensitive steps, positioning the method for large-scale redox modeling where ab initio MD is too costly.

## Methods

**MD application.** **eReaxFF** molecular dynamics simulations of ethylene carbonate (EC) with lithium follow the augmented energy expression in **Section 2** (standard ReaxFF bonded terms plus explicit Gaussian electrons, electron–nuclear interactions, and extended nonbonded tapers). The cell contains **60 EC** and **40 Li** atoms, packed with an in-house placement code, relaxed with **NVT** dynamics at **1 K**, then run at **300 K** and **600 K** (heating toward **600 K** at **0.005 K per MD step**). A **Berendsen** thermostat (**100 fs** damping), **velocity Verlet** integration with **Δt = 0.10 fs**, and Newtonian nuclear motion are used throughout; **Section 3.2** assigns a **1 amu** fictitious mass to each explicit electron carrier. **Three-dimensional periodic** boundaries apply. **Section 3** and figure captions cite multi‑ps segments—for example **~120 ps** tracking of o‑EC⁻/Li⁺ radical formation, **25 ps** snapshots, and **600 ps** boxes for termination products. Production segments are **NVT**; hydrostatic **NPT** barostat control, static external electric fields, and umbrella or replica metadynamics are not part of the primary **60 EC / 40 Li** protocol (aside from brief biased restarts mentioned for selected radical configurations in the discussion). The indexed article text does not name a commercial MD engine.

**Force-field training.** **N/A** — the paper applies the published **eReaxFF** parametrization (C/H/O/Li scope motivated against prior ReaxFF battery work) rather than reporting a new fit here.

**Static QM / DFT production.** **N/A** — energetics are compared to **literature quantum-chemistry** data for EC reduction pathways as cited in the article.

## Findings

Molecular dynamics with explicit electron dynamics captures electron transfer from lithium into EC, ring opening toward EC⁻/Li⁺-type radical intermediates, and subsequent radical termination channels consistent with SEI precursor chemistry, without pre-encoding a fixed reaction network. The authors report that **eReaxFF** reaction energetics for EC reduction align with literature quantum-chemistry references better than prior ReaxFF treatments that misestimated the EC electron affinity and gave overly fast dissociation kinetics. **300 K** and **600 K** **NVT** runs show how temperature changes which termination channels appear on the reported timescales. The introduction notes that salt, cosolvent, and additive chemistry at real electrode–electrolyte interfaces remains only partly captured and that quantum-chemistry-based ab initio MD remains too expensive for large interfacial cells—motivating reactive force fields with explicit electrons.

**Corpus note.** Alternate registered PDFs for this DOI: [[2016islam-venue-research-2]], [[2016islam-venue-research-3]].

## Limitations

- Simplified **EC + Li** model does not include full **salt/solvent mixtures** or **electrode surface** complexity of real cells.
- **Pseudoclassical electrons** are approximate; quantitative barriers must be cross-checked for new chemistries.
- Multi-solvent electrolytes, **SEI** **additives**, and **grain-boundary** **Li** **microstructure** can steer reduction pathways beyond the **EC + Li** **cluster** focus summarized on this page—treat the simulations as **mechanistic** **probes**, not full **cell** **digital twins**.

## Relevance to group

Core **van Duin-group eReaxFF** application to **LIB electrolyte reduction** and **SEI formation** narrative.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.6b08688](https://doi.org/10.1021/acs.jpcc.6b08688) — *J. Phys. Chem. C* **120**, 27128–27134 (2016).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- [[2016islam-venue-ct6b00432]]

## Reader notes (navigation)

- Same article, alternate corpus PDFs: [[2016islam-venue-research-2]], [[2016islam-venue-research-3]].
