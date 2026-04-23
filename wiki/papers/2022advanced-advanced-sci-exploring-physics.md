---
id: paper:2022advanced-advanced-sci-exploring-physics
type: paper
title: "Exploring Physics of Ferroelectric Domain Walls in Real Time: Deep Learning Enabled Scanning Probe Microscopy"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:ferroelectrics-polar
  - material:perovskite-oxide
  - domain:ml-atomistic
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1002/advs.202203957"
year: 2022
authors:
  - "Yongtao Liu"
  - "Kyle P. Kelley"
  - "Hiroshi Funakubo"
  - "Sergei V. Kalinin"
  - "Maxim Ziatdinov"
venue: "Advanced Science"
pdf_sha256: "5d5f10eb2a0aeae5c1277e4dc3d203ab341997ab2dba8d1d8adaeae6ab58029d"
pdf_path: "papers/Others/Advanced Science - 2022 - Liu - Exploring Physics of Ferroelectric Domain Walls in Real Time Deep Learning Enabled.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022advanced-advanced-sci-exploring-physics -->

## Summary

The study couples scanning probe microscopy (SPM) on ferroelectric thin films with a deep convolutional network (DCNN) built from a deep residual backbone and holistically nested edge detection, trained as an ensemble to reduce out-of-distribution drift. The network segments ferroelastic domain walls in real time from the SPM stream and supplies uncertainty maps; segmented walls then trigger targeted band-excitation piezoresponse spectroscopy (BEPS) workflows on PbTiO\(_3\) and PZT films.

Real-time segmentation matters because domain walls can move during imaging; offline post-processing can misassign wall pixels when the underlying polarization evolves scan-by-scan.

## Methods

PFM imaging uses band-excitation modes that yield amplitude, phase, and resonance-frequency maps. Semantic segmentation uses ResHedNet-style architectures with residual blocks and multi-scale fusion; deep ensembles with different initializations and training shuffles approximate epistemic uncertainty, augmented on-the-fly to mimic imaging variability. BEPS loops are placed on skeletonized wall locations to extract loop width and related descriptors of out-of-plane polarization dynamics; additional analyses include coercive field, loop area, and nucleation bias histograms for representative wall locations.

The pipeline closes a loop: fast wall detection guides expensive spectroscopy only where microstructure is likely interesting, improving throughput on heterogeneous films.

## Findings

The DCNN is reported to run on the live data stream, producing wall masks and uncertainty consistent with simulated line-by-line acquisition tests. On PbTiO\(_3\), BEPS loop widths mapped onto ferroelastic walls show spatial heterogeneity linked to wall topology; analyses extend to PZT with analogous workflows. The authors highlight alternating high- and low-polarization dynamics at ferroelastic walls in PbTiO\(_3\) and stronger out-of-plane response on short versus long ferroelastic walls in PZT within the imaged fields.

These spatial contrasts motivate future structure–property models where wall segments are not interchangeable despite similar nominal orientation.

Advanced Science includes architecture diagrams for the ensemble, acquisition-rate tests, and extended BEPS statistics across wall classes that retrieval systems should cite for quantitative ML performance claims.

SPM instrument parameters and sample histories in the supplementary sections matter when comparing uncertainty maps across datasets.

## Limitations

Deep models can fail under large domain shift despite ensembles and augmentation; SPM-specific artifacts (e.g., tip convolution) may affect segmentation near scan lines where uncertainty peaks.

## Relevance to group

Demonstrates ML-assisted interpretation of complex ferroelectric microstructures, orthogonal to reactive MD but relevant where polar oxides intersect data-driven characterization.

## Citations and evidence anchors

- DOI: [10.1002/advs.202203957](https://doi.org/10.1002/advs.202203957)

## Related topics

- [[theme-ferroelectrics-polar-oxides]]
- Ferroelectric characterization and SPM-heavy workflows adjacent to atomistic polar-oxide entries in this wiki
