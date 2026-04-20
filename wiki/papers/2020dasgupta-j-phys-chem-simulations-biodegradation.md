---
id: paper:2020dasgupta-j-phys-chem-simulations-biodegradation
type: paper
title: "Simulations of the Biodegradation of Citrate-Based Polymers for Artificial Scaffolds Using Accelerated Reactive Molecular Dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:reaxff
  - task:application
  - task:validation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcb.0c03008"
year: 2020
authors:
  - "Nabankur Dasgupta"
  - "Dundar E. Yilmaz"
  - "Adri van Duin"
venue: "J. Phys. Chem. B 124:5311-5322 (2020)"
pdf_sha256: "d836bd4e827e526cd18607a93907661ed8bf9c5cc7997cea178e3d1aec1ec6b5"
pdf_path: "papers/Dasgupta_Citrate_JPC_2020.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2020dasgupta-j-phys-chem-simulations-biodegradation -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

ReaxFF MD studies poly(1,6-hexanediol-co-citric acid) hydrolysis with an **accelerated (bond-boost style)** scheme after pre-transition-state preparation. Barriers for ester vs ether hydrolysis are checked against literature DFT. At 300 K, chemical degradation shows faster ester cleavage than ether due to lower barriers; lowering boost parameters suppresses ether hydrolysis selectively. Bundles are also strained longitudinally at two rates: modulus rises with strain rate; polyester–ether is stiffer but yields sooner than polyester alone (polyester more ductile in this comparison).

## Methods

ReaxFF; accelerated reactive MD; mechanical tensile tests on partially hydrolyzed bundles.

The article further notes that atomistic-scale simulations have also been carried out using nonreactive interatomic potentials such as CHARMM 26 and OPLSAA27 enabling larger time scale simulations up to microsecond- and nanoscale level sizes are possible using these methods. These nonreactive simulations can describe bond stretching, angle bending, dihedral rotations, and nonbonded interactions but not bond breaking or bond formation. There have been MD studies on the thermal 28,29 and mechanical degradation30,31 of polymers. However, studies on hydrolytic cleavage of di ﬀerent functional groups in order to understand the chemistry of polymer biodegradation in solvents using atomistic MD techniques have been scarce.

## Findings

Ester vs ether selectivity consistent with barrier arguments; strain-rate sensitivity of modulus; qualitative ranking of ductility between polyester and polyester–ether constructs.


From the abstract: ester can be readily hydrolyzed in the presence of water as the activation energy barriers of ester hydrolysis is generally within the range of 20 −30 kcal/mol. 32−36 Ether hydrolysis refers to the substitution reactions that lead to the cleavage of ether bond and resulting in the formation of alcohols. However, in the presence of nucleophiles, ethers can be hydrolyzed by the nucleophilic substitution reaction. 37 The classical energy barrier of acid-catalyzed ether hydrolysis is around. Carboxylic esters are one of the most important functional groups in organic chemistry. Hydrolysis of esters are mainly addition−elimination reactions which can be acid-catalyzed, base-catalyzed, or neutral in nature. 32 The transition state in each of these products di ﬀer; however, the end product is the same. Because of high chemical stability of ethers, they are diﬃ cult to hydrolyze in neutral environment.

## Limitations

Accelerated MD introduces tunable bias; clinical biodegradation involves enzymes and water transport not fully modeled here.

## Relevance to group

Application of ReaxFF to biodegradable biomedical polymers with explicit acceleration methodology—common theme in reactive polymer degradation studies.

## Citations and evidence anchors

`papers/Dasgupta_Citrate_JPC_2020.pdf` — abstract (barrier checks, hydrolysis selectivity, mechanical tests). https://doi.org/10.1021/acs.jpcb.0c03008

## Related topics

- [[reaxff-family]]