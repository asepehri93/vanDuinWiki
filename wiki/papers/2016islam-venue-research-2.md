---
id: paper:2016islam-venue-research-2
type: paper
title: "Reductive decomposition reactions of ethylene carbonate by explicit electron transfer from lithium: an eReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
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
pdf_sha256: "bd938ff2fb9cccb131987eac797b4de6bdd615b17432d59bb2ec6f35633ad047"
pdf_path: "papers/Islam_eReaxFF_LiEC_JPC_2016_online.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:batteries-interfaces
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
---
<!-- id:paper:2016islam-venue-research-2 -->

Alternate **online-layout** PDF export for the Islam and van Duin *J. Phys. Chem. C* article on **eReaxFF** simulations of **ethylene carbonate** reduction by **electron transfer from lithium**; same DOI as [[2016islam-venue-jp6b08688]].

## Summary

Same *J. Phys. Chem. C* article as [[2016islam-venue-jp6b08688]] (DOI `10.1021/acs.jpcc.6b08688`). **eReaxFF** molecular dynamics follows ethylene carbonate reduction initiated by electron transfer from lithium—ring opening toward EC⁻/Li⁺-type radicals and subsequent radical termination—without a predefined reaction list, in the SEI-formation context summarized in the abstract. This slug registers an alternate PDF export (`papers/Islam_eReaxFF_LiEC_JPC_2016_online.pdf`); use [[2016islam-venue-jp6b08688]] for stable figure and page locators when the files differ cosmetically.

## Methods

Protocol matches [[2016islam-venue-jp6b08688]] (Section 2 energy expression: ReaxFF bonded framework plus explicit Gaussian electrons, electron–nuclear coupling, and extended nonbonded tapers). The condensed cell contains **60 EC** and **40 Li** atoms with **three-dimensional periodic** boundaries. After structural relaxation at **1 K**, production trajectories are reported at **300 K** and **600 K** (the latter reached by gradual heating), using **NVT** integration, a **Berendsen** thermostat with **100 fs** damping, **velocity Verlet** with **Δt = 0.1 fs**, and **Newtonian** nuclei; each explicit electron carrier uses a **1 amu** fictitious mass as stated in Section 3.2 of the article. Section 3 and figure captions discuss **multi‑ps** segments (e.g. **~120 ps** tracking of o‑EC⁻/Li⁺ radical formation, **25 ps** snapshots, and **600 ps** validation boxes for termination products). The manuscript text indexed for this corpus entry does not name a commercial MD package. **NPT** barostats, static external electric fields, and umbrella or replica enhanced sampling are not part of the primary **60 EC / 40 Li** workflow. This communication applies the published **eReaxFF** parametrization and benchmarks against **literature quantum chemistry** rather than reporting a new force-field fit or a standalone DFT production study.

## Findings

Trajectories show electron transfer from lithium into EC, ring opening toward EC⁻/Li⁺-type radicals, and radical termination channels consistent with SEI precursor chemistry, without encoding reactions in advance. The authors report that **eReaxFF** reaction energetics for EC reduction align better with cited quantum-chemistry references than prior ReaxFF treatments that misestimated the EC electron affinity and gave overly fast dissociation kinetics. Side-by-side **300 K** and **600 K** runs illustrate how temperature changes which termination channels appear within the simulated time windows. The introduction stresses that salt, cosolvent, and additive chemistry at real electrode–electrolyte interfaces remains only partially explored and that ab initio MD remains too costly for large interfacial cells—motivating reactive force-field approaches with explicit electrons.

**Corpus note.** Duplicate PDF bytes relative to other registered paths for this DOI; cite [[2016islam-venue-jp6b08688]] for figure and page locators.

## Limitations

The simplified EC plus Li model omits full salt and solvent mixtures and realistic electrode surface complexity. Pseudoclassical electrons are approximate. Reconcile pagination with **`Islam_eReaxFF_LiEC_JPC_C_2016.pdf`** versus other exports.

## Relevance to group

Bibliography disambiguation entry for multiple PDF bytes of one van Duin-group eReaxFF SEI paper.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.6b08688](https://doi.org/10.1021/acs.jpcc.6b08688) — *J. Phys. Chem. C* **120**, 27128–27134 (2016).

## Reader notes (navigation)

- Primary curated page: [[2016islam-venue-jp6b08688]]. Alternate-PDF export policy: [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (duplicate registration guidance).

## Related topics

- [[2016islam-venue-jp6b08688]]
- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
