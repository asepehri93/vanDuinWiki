---
id: paper:2018miron-the-journal-accelerated-molecular
type: paper
title: Accelerated molecular dynamics with the bond-boost method
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:methods-software
- domain:alloys-metallurgy
- method:classical-md
- method:enhanced-sampling
- task:method-development
- scale:atomistic
paper_keywords:
- keyword:method-development
- keyword:eam-potential
- keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: 10.1063/1.1603722
year: 2003
authors:
- Radu A. Miron
- Kristen A. Fichthorn
venue: J. Chem. Phys. 2003, 119, 6210–6216
pdf_sha256: 2eed5dd87bf0d64a14aab8c98dff245685c52bf20f7b9c90ae7425e272253526
pdf_path: papers/Others/Miron_Fichthorn_Bond_Boost_2003.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018miron-the-journal-accelerated-molecular -->

## Summary

Rare events such as surface diffusion hops, vacancy motion, and exchange mechanisms on metals often occur on time scales far longer than brute-force molecular dynamics can sample at experimentally relevant temperatures. This Journal of Chemical Physics article introduces bond-boost accelerated molecular dynamics (AMD), an empirical scheme that increases transition rates near potential-energy minima by applying a boost to the potential energy that depends on how far selected bond lengths deviate from their equilibrium values. The method does not require a predefined catalog of events; instead, it uses local bond distortions to bias dynamics toward escape from basins. The authors motivate the approach as a practical way to reach millisecond-scale phenomena while retaining an atomistic embedded-atom method (EAM) description of copper. The paper positions bond boost within the broader accelerated-dynamics family and focuses validation on copper surface processes where direct MD is prohibitively slow.

## Methods

### Method development (bond-boost accelerated MD)

The paper introduces **bond-boost accelerated molecular dynamics (AMD)**: near **local minima** the **potential energy surface** is **modified** by adding a **boost potential** that grows with **deviations of selected bond lengths** from equilibrium, **increasing transition rates** while aiming to **preserve relative rates** among competing pathways when parameters are chosen appropriately (**J. Chem. Phys.** **119**, **6210–6216** (2003); `papers/Others/Miron_Fichthorn_Bond_Boost_2003.pdf`). The approach needs **no predefined event list** and can pair with **many-body classical potentials**.

### MD application (Cu(100) EAM benchmarks)

**Engine / code:** **Molecular dynamics** on **Cu(100)** using an **embedded-atom method (EAM)** potential (abstract). **System & composition:** **Cu** **slab/supercell** setups for **adatom**, **vacancy**, **exchange**, and **dimer** diffusion processes enumerated in the abstract (**atom** counts and supercell vectors in **Methods**). **PBC:** **three-dimensional PBC** for the **surface** cells as standard for slab MD (**exact slab thickness / fixed layers** in **PDF**). **Ensemble / thermostat / timestep / duration:** **NVE**/**NVT** assignments and **timestep** choices for the boosted **MD** stages are given in §§II–III of the article (**N/A — numeric thermostat damping** not transcribed from the indexed excerpt `normalized/extracts/2018miron-the-journal-accelerated-molecular_p1-2.txt`). **Temperature:** **low-temperature surface diffusion** regime emphasized in the Introduction/abstract framing (**exact K** in **Methods**). **Barostat / pressure:** **N/A — not highlighted** in the excerpted abstract (**constant-volume** surface MD typical; confirm in **PDF**). **Electric field:** **N/A — not used**. **Enhanced sampling:** **bond-boost AMD** is the paper’s enhanced-dynamics method (**not** umbrella/replica exchange).

### Comparisons reported in the article

The authors compare **boosted** trajectories to **brute-force MD** and **transition-state theory** expectations for the same **Cu(100)** processes to assess whether **relative rates** remain faithful under boost.
## Findings

For the **Cu(100)** test cases, **bond-boost AMD** reproduces the **correct relative rates** for **adatom hopping**, **exchange**, **vacancy** and **dimer** diffusion, and related processes summarized in the abstract, with **speedups up to several orders of magnitude** vs **brute-force MD**. The work argues **local bond-length-based boosting** can suffice for **metallic surface diffusion** without prelisting events, while warning that **boost parameters** must be tuned to avoid distorting **relative kinetics** among competing pathways.

**Comparisons / validation.** Validation is against **direct MD** and **TST** expectations for the same **EAM Cu** surface processes as described in the article.

**Corpus honesty.** This page corrects an earlier scaffold typo: the study uses **EAM Cu** **MD**, **not** **ReaxFF**; numerical boost settings live in the **2003 JCP** **PDF**.

## Limitations

Boost shape and strength are empirical knobs; transferability to different materials, reactive chemistry, or strongly anharmonic systems requires separate validation. The method inherits limitations of the underlying classical potential and of the assumption that relative transition rates remain meaningful under boost.

## Relevance to group

Reference algorithm for rare-event atomistic simulation that can complement LAMMPS workflows and reactive studies where enhanced sampling is needed.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1063/1.1603722](https://doi.org/10.1063/1.1603722)

## Related topics

- [[reaxff-family]]
