---
id: paper:2010medhekar-venue-paper
type: paper
title: "Hydrogen bond networks in graphene oxide composite paper: Structure and mechanical properties"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:water-interfaces
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:nvt-simulation
canonical_tags:
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - material:polymer-organic
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/nn901934u"
year: 2010
authors:
  - "Nikhil V. Medhekar"
  - "Ashwin Ramasubramaniam"
  - "Rodney S. Ruoff"
  - "Vivek B. Shenoy"
venue: "ACS Nano 4 (4), 2300–2308 (2010)"
pdf_sha256: "e74a46aba73ad282ee30bfbd584c7592038fb4e8b1a778886666080975ca5c71"
pdf_path: "papers/ReaxFF_others/Medhekar_Shenoy_grapheneoxide_ACSNano_2010.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2010medhekar-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Distances (**5.1 Å**, **9.0 Å**), **water weight percents** (**1–26 wt %**), and **76% volume swelling** are taken from the **extract** as printed in the Results discussion.

## Summary

The paper uses **ReaxFF MD** to model **hydrated graphene oxide (GO) paper**—stacked **GO platelets** with **interlamellar water**—and argues that **hydrogen-bond networks** involving **oxygen functional groups** and **water** control morphology and mechanics. The abstract states water content modulates **hydrogen-bond extent/strength**, **interlayer spacing**, and **elastic moduli**, while higher **functional group density** on platelets increases hydrogen bonding and **stiffness**. Simulated structural/mechanical trends are reported to agree with experiments.

## Methods


**ReaxFF** in **LAMMPS**: periodic **supercells** with **four** **~3.4 nm \(\times\) 3.0 nm** GO platelets, initial **7 Å** interlayer gap, **random** **epoxy/hydroxyl** patterns for **C\(_{10}\)O\(^1\)(OH)\(^1\)** and **C\(_{10}\)O\(^2\)(OH)\(^2\)** stoichiometries, and **random** interlayer **water** placement. **Equilibration** uses **NPT** with **Nosé–Hoover** **thermostat** and **barostat**, time step **0.025 fs**, heating **10→1000 K** over **625 fs**, **anneal** at **1000 K** for **625 fs**, **quench** to **300 K** over **625 fs**, then **300 K**, **zero pressure** for **4.25 ps**. **Mechanical** analysis runs **NVT** at **300 K**; atomic displacements sampled every **50** steps feed **fluctuation-based** **elastic** constants via the **displacement-correlation** approach cited in the article (references to **Pratt** and **Meyers** et al. in the PDF). Water content spans **~1–26 wt %**.

## Findings

**Interlayer** **spacing** increases from **~5.1 Å** (low water) to **~9.0 Å** at **~26 wt %** water for the **C\(_{10}\)O\(^1\)(OH)\(^1\)** models, with **~76%** **volume swelling** over that range. **Spacing vs. water** is **approximately linear** and **similar** for both **oxidation** stoichiometries at comparable hydration. **H-bond** counts rise **roughly linearly** with water; **C\(_{10}\)O\(^2\)(OH)\(^2\)** supports **more** H-bonds than **C\(_{10}\)O\(^1\)(OH)\(^1\)** at the same water content. **ReaxFF** **optimal** **O···H** distance **~2.55 Å** with **~320 meV** interaction strength matches typical **H-bond** scales cited for comparison. **Modeled** structural/mechanical trends align with **experimental** **X-ray** gallery heights (**~6–11 Å** cited) and **humidity**-dependent **modulus** changes.

The authors emphasize that **water-mediated** **H-bond networks** couple **swelling** to **mechanical stiffening**, so **GO paper** cannot be treated as a simple **graphite** stack with fixed interlayer spacing.

## Limitations

Reactive MD captures graphene oxide chemistry only approximately; laboratory samples exhibit polydisperse oxidation and defect distributions. `extraction_quality` is **partial**; elastic moduli and stress–strain data are in the PDF figures.

## Relevance to group

Demonstrates **ReaxFF** for **oxide–water–carbon** hydrogen-bonded assemblies relevant to **interfaces**, **nanocarbon**, and **composite** mechanics threads in the corpus.

## Citations and evidence anchors

- DOI: `10.1021/nn901934u`.
- PDF: `papers/ReaxFF_others/Medhekar_Shenoy_grapheneoxide_ACSNano_2010.pdf`.
- Extract: `normalized/extracts/2010medhekar-venue-paper_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
