---
id: paper:2019chen-nat-high-resolution-tip-enhanced
type: paper
title: "High-resolution tip-enhanced Raman scattering probes sub-molecular density changes"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - method:dft-static
  - task:method-development
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:method-development
  - keyword:validation-experiment
source_refs: []
doi: "10.1038/s41467-019-10618-x"
year: 2019
authors:
  - "Xing Chen"
  - "Pengchong Liu"
  - "Zhongwei Hu"
  - "Lasse Jensen"
venue: "Nature Communications 10, 2567 (2019)"
pdf_sha256: "051aabce6f1a6033b38a9dd70bcdae4dd9188bd5bf67c207eac71e2cb0aa45a3"
pdf_path: "papers/Others/Xing_Jensen_SERS_NatureComm_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019chen-nat-high-resolution-tip-enhanced -->

## Summary

The paper develops a **linear-response TDDFT**-based framework showing how **tip-enhanced Raman** intensities can track **locally integrated Raman polarizability density (LIRPD)**—i.e., **sub-molecular** changes in **induced electron density** under the **confined plasmonic near field** during the Raman process, not only atomic positions. Applied to **meso-tetrakis(3,5-di-tert-butylphenyl)porphyrin (H₂TBPP)** on a surface, the model explains how **four-fold symmetric** TERS maps can arise from modes localized in **tert-butylphenyl** substituents rather than the **porphyrin core** alone.

## Methods

This is a **static electronic-structure theory** / **spectroscopy modeling** paper (not a production classical MD study).

**Static QM / TDDFT (TERS junction model).** The authors start from **linear-response time-dependent density functional theory (TDDFT)** and relate the **induced density** under a perturbing field to a **density–density response kernel**. The **plasmonic near field** in the **TERS** junction is represented as a **localized envelope** multiplying molecular operators, enabling a **local** reformulation in which **spatially resolved** **LIRPD** maps can be compared to **simulated TERS images** as a function of **tip position**.

**Functional / dispersion / basis / k-sampling.** Specific **XC functional**, **dispersion correction**, **basis set**, and any **periodic k-point** conventions are **N/A — not restated** in the short wiki summary; they are specified in the **Nature Communications** article and **Supplementary Methods** where they control **absolute intensities** and **hotspot widths**.

**Structures / pathways.** The primary molecular exemplar discussed in the curated summary is **H₂TBPP** on a surface under **TERS-relevant** junction geometries; the paper’s figures compare **simulated** and **experimental** high-resolution maps for this system class.

**Properties computed.** **LIRPD** fields, **TERS** **intensity** maps, Raman **polarizability**-linked **response**, and **energy**-based diagnostics of the **linear-response** treatment; supplementary material discusses comparison to **fully nonlocal** response treatments and reports numerical **frequency**-domain checks where applicable.

**MD / force-field training.** **N/A —** not applicable as the primary methodology for this publication.
## Findings

**Outcomes / mechanism attribution.** TERS contrast is interpreted as probing **Raman polarizability density** features that can be **strongly localized** by the **confined electromagnetic hot spot**, motivating **gradient-type** selection rules distinct from simple “atom-by-atom” pictures.

**Comparisons (H₂TBPP).** For **H₂TBPP**, a **four-fold** high-resolution TERS motif can arise from **degenerate** modes localized in **tert-butylphenyl** substituents rather than the **porphyrin core** alone, reconciling cases where the **TERS symmetry** does not mirror the **core** symmetry intuitively.

**Sensitivity / levers.** The narrative depends on **field localization width**, **molecular orientation**, and the validity of the **local** approximation—quantitative sensitivities are in the paper’s **Supplementary Methods** and figures.

**Authored limitations.** The **local** mapping is expected to be most reliable for **sufficiently confined** near fields; transferring the same modeling assumptions to other **plasmon junctions** requires re-validation of the approximation (see **## Limitations**).
## Limitations

Approximations tie validity to sufficiently confined near fields and specific electronic-structure treatments; extension to other plasmon junctions requires re-evaluation of the local approximation.

## Relevance to group

Penn State chemistry (Jensen group); spectroscopy theory rather than ReaxFF MD.

## Citations and evidence anchors

https://doi.org/10.1038/s41467-019-10618-x

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Spectroscopy/theory cluster adjacent to MD-heavy corpus notes; not a ReaxFF application paper.
