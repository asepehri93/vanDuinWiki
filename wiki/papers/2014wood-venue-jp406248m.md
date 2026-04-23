---
id: paper:2014wood-venue-jp406248m
type: paper
title: "Coupled thermal and electromagnetic induced decomposition in the molecular explosive α-HMX: a reactive molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
source_refs: []
doi: "10.1021/jp406248m"
year: 2014
authors:
  - "Mitchell A. Wood"
  - "Adri C. T. van Duin"
  - "Alejandro Strachan"
venue: "Journal of Physical Chemistry A 2014, 118, 885–895"
pdf_sha256: "4e5c3ea0d176293776252e8d2caef7e7009088aa1a7c69555413075ef9a91bc0"
pdf_path: "papers/Wood_HMX_JPCA_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014wood-venue-jp406248m -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Wood, van Duin, and Strachan use **ReaxFF MD** to study **α-HMX** decomposition under **rapid heating** and under **sinusoidal electric fields** at multiple frequencies and strengths, focusing on how **insult type** and **energy input rate** change the **energy thresholds** for initial chemistry and for onset of **exothermic** reaction cascades. The abstract argues both thresholds rise with heating/input rate and plateau toward **athermal** regimes at very fast loading, with **insult-type-dependent** thresholds especially for exothermic onset. The introduction frames the work within **vibrational energy transfer**, **anharmonic coupling**, and **mode-targeted excitation** debates in energetic materials, and the methods section notes a **nitramine ReaxFF** parameterization integrated with broader **C/H/O combustion** training for improved transferability.

The study is motivated by the need to separate **thermal** shock initiation from **electromagnetic** coupling in **HMX**, asking whether field frequency and amplitude can selectively excite modes that change onset timing relative to purely thermal ramps at comparable energy deposition rates.

## Methods

**Force-field training (nitramine + combustion ReaxFF).** The parametrization builds on the **original nitramine ReaxFF** and includes **bond dissociation** curves for **C/O/N/H** single, double, and triple bonds, **angle** distortions for viable **C/O/N/H** angular combinations, **dihedral** barriers, and **charge** distributions; **nitramine** training used **DFT** at **B3LYP/6-311G\*\*** and **6-31G\*\*** for **RDX**, **HMX**, and **PETN** dissociation pathways including **barriers**; **charge equilibration** parameters target **Mulliken** partial charges from **DFT** (extract in `normalized/extracts/2014wood-venue-jp406248m_p1-2.txt`). The **nitramine** set was merged with the broader **C/H/O combustion** training set (**Chenoweth** *et al.*, cited in the extract) to improve **transferability** versus a standalone nitramine parameter file. **Validation metrics quoted in the extract:** **NO\(_2\)** dissociation energy **41.3 kcal/mol** vs **DFT 39.8 kcal/mol**; **HONO** pathway mildly **exothermic** (**−9.1 kcal/mol**) vs **concerted ring-opening** more exothermic (**−19.0 kcal/mol**) but with a **very large barrier**, disfavoring the latter as an initiation channel in this parametrization.

**MD application (α-HMX under thermal vs field insults).** **Reactive MD** with **ReaxFF** treats **α-HMX** in **PBC** supercells under varied **thermal heating rates** and **sinusoidal electric fields** at multiple **frequencies** and **strengths**, with later analysis of **vibrational/IR** and **frequency-resolved** energy absorption (extract-level outline). Atom counts, cell vectors, **NVT**/**NVE**/**NPT** staging (including any **pressure** control), timestep, trajectory lengths, thermostat coupling, and the **field** coupling implementation are in **Section 2** of **`papers/Wood_HMX_JPCA_2014.pdf`** and **SI** (**N/A** for numeric transcription from the short extract).

**Static QM (training references only).** **N/A** for standalone production **AIMD**: **DFT** supports **ReaxFF** training/validation as summarized under force-field training.

## Findings

The abstract reports that both the energy required for **initial decomposition** and that for onset of **exothermic chemistry** **rise** with **increasing energy-input rate**, **plateauing** toward **athermal** behavior at very **high** rates; the **exothermic** threshold (and, more weakly, the **initial chemistry** threshold) also depends on **insult type** (**thermal** versus **field**-driven pathways). Introduction themes emphasize that modest stimuli can initiate chemistry when **modes** are well targeted, while **anharmonic** coupling during heating drives rapid **inter-mode** transfer that limits lasting **mode-specific** discrimination between loading types. At the parametrization level (extract), **NO\(_2\)** dissociation energy matches **DFT** closely, and the authors contrast **HONO** versus **concerted ring-opening** pathways by **exothermicity** and **barrier** height as summarized under **Methods**.

## Limitations

- Classical reactive MD cannot capture **electronic excitations** explicitly; electric-field driving is a **classical energy-delivery** model subject to interpretation.
- Extract is early pages; quantitative thresholds and spectra need full-text review.

## Relevance to group

**Adri C. T. van Duin** as co-author ties the study to **ReaxFF** parametrization for **energetic materials** and coupled **thermal/nonthermal** insult modeling pursued in collaboration with **Purdue**-side HED modeling expertise.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/jp406248m](https://doi.org/10.1021/jp406248m)

## Related topics

- [[reaxff-family]]
