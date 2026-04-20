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

## One-paragraph summary

ReaxFF MD studies poly(1,6-hexanediol-co-citric acid) hydrolysis with an **accelerated (bond-boost style)** scheme after pre-transition-state preparation. Barriers for ester vs ether hydrolysis are checked against literature DFT. At 300 K, chemical degradation shows faster ester cleavage than ether due to lower barriers; lowering boost parameters suppresses ether hydrolysis selectively. Bundles are also strained longitudinally at two rates: modulus rises with strain rate; polyester–ether is stiffer but yields sooner than polyester alone (polyester more ductile in this comparison).

## Methods

ReaxFF; accelerated reactive MD; mechanical tensile tests on partially hydrolyzed bundles.

## Findings

Ester vs ether selectivity consistent with barrier arguments; strain-rate sensitivity of modulus; qualitative ranking of ductility between polyester and polyester–ether constructs.

## Limitations

Accelerated MD introduces tunable bias; clinical biodegradation involves enzymes and water transport not fully modeled here.

## Relevance to group

Application of ReaxFF to biodegradable biomedical polymers with explicit acceleration methodology—common theme in reactive polymer degradation studies.

## Citations and evidence anchors

`papers/Dasgupta_Citrate_JPC_2020.pdf` — abstract (barrier checks, hydrolysis selectivity, mechanical tests). https://doi.org/10.1021/acs.jpcb.0c03008

## Related topics

- [[reaxff-family]]
