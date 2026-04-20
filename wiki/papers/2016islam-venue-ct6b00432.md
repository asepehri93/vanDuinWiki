---
id: paper:2016islam-venue-ct6b00432
type: paper
title: "eReaxFF: a pseudoclassical treatment of explicit electrons within reactive force field simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:ereaxff
  - method:reaxff
  - task:method-development
  - domain:methods-software
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.6b00432"
year: 2016
authors:
  - "Md Mahbubul Islam"
  - "Grigory Kolesov"
  - "Toon Verstraelen"
  - "Efthimios Kaxiras"
  - "Adri C. T. van Duin"
venue: "J. Chem. Theory Comput."
pdf_sha256: "785eb9c8dcbbf11351c7d9a2752ab2578ebc90aafd32285836069df87d45b0c8"
pdf_path: "papers/Islam_JCTC_eReaxFF_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016islam-venue-ct6b00432 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The article introduces **eReaxFF**, an extension of **ReaxFF** that treats **electrons explicitly** in a **pseudoclassical** formulation integrated with **ACKS2-derived** charge/electronic-structure approximations, targeting **orders-of-magnitude** speedups over conventional **quantum chemistry dynamics**. Training emphasizes **electron affinities** for representative **hydrocarbon radicals**, with **MD demonstrations** comparing **eReaxFF** to **Ehrenfest**-style references for selected cases. The study argue that **literature ReaxFF parameters** remain largely **transferable** into the new framework, lowering adoption friction.

## Methods

- **Formulation + integration** of explicit electronic degrees of freedom with **ReaxFF** energy expressions.
- **ACKS2** coupling for charge-related quantities as described in the paper.
- **Proof-of-principle MD** on radical systems with **EA benchmarks**.

<!-- enrich-from-extract:v2 -->

- We present a computational tool, eReaxFF, for simulating explicit electrons within the framework of the standard ReaxFF reactive force ﬁeld method.
- We treat electrons explicitly in a pseudoclassical manner that enables simulation several orders of magnitude faster than quantum chemistry (QC) methods, while retaining the ReaxFF transferability.
- We delineate here the fundamental concepts of the eReaxFF method and the integration of the Atom- condensed Kohn −Sham DFT approximated to second order (ACKS2) charge calculation scheme into the eReaxFF.
- As a proof-of-principle, we performed a set of molecular dynamics (MD) simulations with an explicit electron model for representative hydrocarbon radicals.
- We establish a good qualitative agreement of EAs of various species with experimental data, and MD simulations with eReaxFF agree well with the corresponding Ehrenfest dynamics simulations.
- The standard ReaxFF parameters available in the literature are transferrable to the eReaxFF method.
- The computationally economic eReaxFF method will be a useful tool for studying large-scale chemical and physical systems with explicit electrons as an alternative to computationally demanding QC methods.
- Approximate QC based methodsfor example, density functional theory (DFT) or Tight-Binding (TB) schemes have been developed as computationally advantageous alternatives to truly ab initio methods.
- Even with such appr oximations, nonadiabatic dynamics using time-dependent DFT are quite expensive and are limited to a relatively small number of atoms ( ∼1000) and short time scales ( ∼1 ps). 1,2 Force ﬁeld (FF) based methods have also been developed as an alternative to QC methods.
- FF methods use simpli ﬁed functional forms and provide much better computational performance, enabling simulations to access much larger scales, of order nanometers in length and nanoseconds in time.


## Findings

- **Qualitative EA trends** align with **experiment** for multiple species in the benchmark suite presented.
- **eReaxFF MD** tracks **Ehrenfest** references more closely than naïve classical alternatives in the tests highlighted in the abstract.
- Positions the method as a bridge toward **large-scale redox, polarization, and battery-interface** problems that strain implicit-charge reactive models.

### Additional results (article abstract)

- The eFF has been parametrized only for a limited number of elements in the periodic table, and the primary application areas are materials that are subjected to extreme pressure and temperature apart from the complexity of the reactive systems. 7,8 The ability of the LEWIS method to describe atomic electron a ﬃ nities (EA) and ionization potentials (IP) of the ﬁrst three row elements is encouraging, still such description for molecules is not available. 12,13 The low- temperature dynamics of liquid water 9,11 and prediction of ground state con ﬁgurations of some chemical species 14 indicate the promising capabilities of the LEWIS method, but, the challenge of describing complex reactions or high-temperature dynamics with an acceptable level of accuracy is yet to be demonstrated.
- However, most of the available force ﬁeld methods provide a substitute for the electronic structure and are typically nonreactive in nature, implying the absence of explicit electrons and their impact on system geometry and energy, as well as the inability to simulate bond breaking and formation.
- An accurate description of these phenomena requires an explicit treatment of electron degrees of freedom, which must be within the classical framework of the classical potentials.
- Recently, a number of force ﬁeld methods have been developed that include aspects of explicit valence electrons, like the electron force ﬁeld (eFF) 7,8 and LEWIS9−11 force ﬁeld.
- There also exists alternate methods to couple covalent and electrostatic interactions through split-charge equilibration (SQE) 15,16 for describing charge transfer in reactive dynamics, 17 without an explicit electron treatment.
- To the best of our knowledge, no classical force ﬁeld method with access to explicit electrons has been employed to simulate complex reactive events.
- The treatment of an explicit electron within the classical framework can only capture the “particle” nature of the “wave- particle dual ” nature of the electron


## Limitations

- **Pseudoclassical electrons** are not a full **quantum electronic** solution; accuracy limits near **conical intersections** and **strongly correlated** states must be monitored.
- **Parameter portability** still requires systematic validation per **chemically distinct** subsystem.

## Relevance to group

Landmark **method paper** from the **van Duin + Harvard + Ghent** collaboration defining **eReaxFF**, a cornerstone of the group’s **next-generation reactive FF** roadmap.

## Citations and evidence anchors

- Abstract and Sec. I in `papers/Islam_JCTC_eReaxFF_2016.pdf`; **DOI:** `10.1021/acs.jctc.6b00432`.

## Related topics

- [[reaxff-family]]
