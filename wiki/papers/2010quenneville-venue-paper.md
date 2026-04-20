---
id: paper:2010quenneville-venue-paper
type: paper
title: "Reactive molecular dynamics studies of DMMP adsorption and reactivity on amorphous silica surfaces"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:oxides-ceramics, domain:catalysis-surfaces, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1021/jp104547u"
year: 2010
authors: ["Quenneville, Jason", "Taylor, Ramona S.", "van Duin, Adri C. T."]
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "92ec8b991cdbee2820af8f1e8aaf948a2e9f614fc9936571a2f8ea6b41cf4c78"
pdf_path: "papers/Quenneville_2010_JPC.pdf"
extraction_quality: partial
group_affiliation: true
---

<!-- id:paper:2010quenneville-venue-paper -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study uses **ReaxFF molecular dynamics** to study **dimethyl methylphosphonate (DMMP)** interacting with **amorphous silica** as a function of surface hydroxylation (reported modeled densities 2.0–4.5 OH/nm²). The introduction frames DMMP as a **nerve-agent simulant** relevant to environmental fate on silica-rich materials. Key qualitative results in the excerpt include: at higher OH coverage, binding involves **vdW + hydrogen bonding**; at lower coverages, **covalent** interaction between the phosphonyl oxygen and **3-coordinate Si defects**; at very low coverage, **fragmentation** is observed. A stated binding energy example is **−4.7 kcal/mol** at **4.5 OH/nm²**, and added water can **displace/hydrolyze** adsorbed DMMP. MP2/DFT cluster calculations are reported as supporting selected ReaxFF predictions.

## Methods

- **ReaxFF MD** on amorphous silica surfaces with varying hydroxyl density; structural characterization of the silica model compared to experiment (per text).
- **QM spot checks:** MP2 and DFT on small silica clusters to validate reactions suggested by MD.

The article further notes that reactive Molecular Dynamics Studies of DMMP Adsorption and Reactivity on Amorphous Silica Surfaces Jason Quenneville* and Ramona S. The amorphous silica surface used in the reported simulations is quantiﬁed structurally and compares well to experimental ﬁndings. To validate the ReaxFF/MD ﬁndings, we performed MP2 and DFT quantum chemical studies of reactions predicted by the MD/ReaxFF by using small silica clusters. The quantum chemistry results support the MD/ReaxFF results, providing further veriﬁcation of our ﬁndings and indicating the viability of ReaxFF/MD to study complex surface chemistry. Here, we examine the interaction of DMMP with amorphous silica as a function of the surface hydration via molecular dynamics (MD) computer simulations. The potential model employed in these calcula- tions is the fully reactive ReaxFF empirical potential which was developed by van Duin and Goddard. 21-24 ReaxFF is an empirical force ﬁeld that relates the degree of chemical bonding between two atoms (the bond order) to the distance between them. 25-28 This allows for the efﬁcient treatment of bond formation and breakage (i.e., chemical reactions) in large condensed phase systems. The ReaxFF potential energy function is: where the individual energy terms represent the bond order term (with N-body terms to correct for the possibility of over- or under-coordination of atoms), the bond angle and torsion energies, terms corresponding to the formation/destruction of nonbonding electron pairs and conjugation hydrogen bonding, and van der Waals and Coulombic interactions. In addition, chemical reactions and large geometrical variations can change the charge distribution in the system dramatically; thus, ReaxFF necessarily contains a means for equilibration of atomic charges throughout the course of the simulation. 29 MD investigations of the structure of liquid DMMP 30 and calculations of reaction cross sections for the interaction of DMMP and sarin with O( 3P)31 have been reported in the literature. Taylor* Spectral Sciences, Inc., Burlington, Massachusetts 01803, United States Adri C. Surface hydroxylation densities of 2.0, 3.0, 4.0, and 4.5 hydroxyl/nm 2 were modeled.

## Findings

- Strong dependence of binding mode on OH density: from vdW/H-bonding dominance at high OH, to defect-mediated covalent attachment at lower OH, to fragmentation at the lowest studied OH density.
- Quantitative example binding energy (−4.7 kcal/mol) and qualitative solvent displacement chemistry with an added water layer.


From the abstract: at the higher OH densities, binding of DMMP to the hydroxylated silica was found to occur through a combination of van der Waals interactions and hydrogen bonding. Finally, at extremely low hydroxyl coverages (2.0 nm -2), DMMP fragmentation was found to occur. The binding energy of DMMP on amorphous silica with a hydroxyl density of 4.5 OH/nm 2 was calculated to be -4.7 kcal/mol. Addition of a water layer to the silica-supported DMMP system showed that water can displace and/or hydrolyze the adsorbed DMMP molecules. Structures for DMMP and sarin are shown Figure 1. On the other hand, DMMP was found to undergo a small amount of decomposition if the surface was hydrated prior to the DMMP adsorption. DMMP is a common simulant for the organophosphate nerve agents, sarin and VX. In one of the earliest studies of the interaction of DMMP with a-SiO 2, Henderson and co-workers adsorbed DMMP onto a nonhydrated a-SiO 2 surface at 170 K and monitored its reactivity by using temperature program desorption. 11 The DMMP was completely desorbed from the surface between 200 and 275 K, giving an activation energy for desorption of 16.9 kcal/mol. No decomposition of the DMMP was seen in these experiments. Structures of (a) sarin and (b) dimethyl methylphosphonate (DMMP).

## Limitations

- Extraction is **partial**; barrier heights, full product distributions, and sensitivity analysis may require the full article.
- Classical reactive FF uncertainty for organophosphate/surface chemistry should be tracked against QM benchmarks.

## Relevance to group

Demonstrates **ReaxFF + QM validation** for **oxide surface chemistry** with organics, a template for adsorption/reactivity studies on amorphous silica and related environmental interfaces.

## Citations and evidence anchors

- Abstract and introduction: DMMP/silica coverage effects, binding energy example, water displacement (J. Phys. Chem. C 2010; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]