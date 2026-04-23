---
id: paper:2018zhang-venue-untitled
type: paper
title: 'Supporting Information: Isotope Effects in Water (ReaxFF) — heavy vs light
  water'
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:reaxff-lineage
- method:reaxff
- task:validation
- scale:atomistic
paper_keywords:
- keyword:supporting-information
- keyword:water-interfaces
- keyword:reaxff-parameterization
candidate_tags: []
source_refs: []
doi: ''
year: 2018
authors:
- Weiwei Zhang
- Xing Chen
- Adri C. T. van Duin
venue: Supporting information PDF (J. Phys. Chem. Lett. family; see canonical article
  page)
pdf_sha256: fd23cfd6b0a91f50f076b52c99fa299c9c4a1173429c7fa0e5bea447c7ac4598
pdf_path: papers/Zhang_HeavyWater_JPC_Letters_2018_SI.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018zhang-venue-untitled -->

## Summary

This corpus PDF is Supporting Information for a *Journal of Physical Chemistry Letters* family article on isotope effects in water modeled with ReaxFF, pairing light water (H₂O) against heavy water (D₂O). The opening SI paragraph anchors the discussion to the published ReaxFF energy expression and cites the CHO_2008 and CHON-2017_weak parameter lineage before documenting which bonded, van der Waals, and hydrogen-bond terms were retuned for heavy water. The SI’s role in the knowledge base is documentary: it records how the CHON-2017_weak parameter set is used as the baseline for H₂O, and how a subset of terms is reoptimized to capture the shorter O–D bond length and adjusted hydrogen-bonding balance needed for D₂O structural and dynamical observables within the same overall functional form. Dynamics for D₂O explicitly substitute deuterium mass for hydrogen in the nuclear equations of motion while using the heavy-water-tuned interaction terms. Scientific conclusions, figures, and quantitative performance metrics belong to the primary article page linked below; this entry should not be treated as a standalone publication abstract.

## Methods

**1 — MD application (SI “Simulation details”).** **ReaxFF** **molecular dynamics** is executed in **ADF-2017** (Amsterdam Modeling Suite). Cubic cells with **500** **H₂O** or **D₂O** molecules (**~1500** **oxygen**/**hydrogen** **atoms** per cell, isotope-dependent): **Monte Carlo** pack at **low density** (~**0.2 g/cm³**), minimize, compress toward **~1.00 g/cm³**, then **200 ps NPT** **MD** at **room temperature**; **NPT**-equilibrated cells seed **500 ps NVT** production (**last 250 ps** used for bulk property statistics). **H₃O⁺/D₃O⁺** inserts follow **500 ps NVT** blocks (**last 250 ps** analyzed). **Engine / code:** **ADF-2017** (the SI states all **ReaxFF** runs used the **Amsterdam Modeling Suite** **ADF-2017** package). **Timestep:** **0.25 fs**. **Thermostat / barostat:** **Berendsen** with **pressure** and **temperature** damping **2500 fs** and **100 fs** for **NPT** and **NVT** segments, respectively. **PBC** cubic boxes. **Temperature:** **room temperature** for the equilibration/property blocks tabulated in the SI. **Electric field:** **N/A —** not part of the bulk isotope protocol. **Enhanced sampling:** **N/A —** standard **NVT**/**NPT** **MD** only. **MSD** for **H₃O⁺/D₃O⁺** averages **50** independent trajectories (SI).

**2 — Force-field training (SI).** **CHON-2017_weak** is the **H₂O** baseline; **D₂O** uses successive one-parameter **ReaxFF** **reoptimization** of **O–H** bonded, **van der Waals**, and **hydrogen-bond** terms (shorter **O–D** bond, adjusted **H-bond** balance) while many angular terms track the light-water **training** unless the SI lists an exception. **Nuclear** dynamics use **deuterium** **mass**. **QM**/**DFT** targets and **validation** tables live in the SI and main letter; copy numeric **parameter** values from the SI tables.
## Findings

**Mechanism and isotope treatment.** The SI argues that **CHON-2017_weak** already captures the targeted **H₂O** **density**, **structure**, and **dynamics** observables in their benchmark set, whereas reproducing **D₂O** requires retuning bonded, **van der Waals**, and **hydrogen-bond** contributions—not merely swapping **hydrogen** for **deuterium** mass in the **equations of motion**. That **reparameterization** narrative ties **O–D** bond shortening and shifted **hydrogen-bond** balance to the measured isotope splitting in **liquid** **properties**.

**Comparisons.** **Experimental** **density** and related **liquid** metrics for **H₂O** vs **D₂O** are the primary **validation** anchors; the SI tables should be read beside the main-letter figures on **`[[20180000-0002-5255-7340-j-phys-chem-isotope-effects]]`** rather than trusting this wiki alone.

**Sensitivity.** **Temperature** and **pressure** (when **NPT** blocks appear) enter through the same **MD** protocols as the parent article; extending the fit to other **thermodynamic** states requires re-checking **diffusion** and **structure** against **experiment**.

**Limitations and corpus honesty.** This file is **Supporting Information**, not the peer-reviewed letter body; **pagination** and figure numbering follow the SI bundle, and **`normalized/extracts`** may remain shorter than the full **PDF**. **Future work** implied by the SI—broader state points or additional isotopic species—must be verified against any post-publication corrections on the **version-of-record** **PDF**.
## Limitations

As a supporting-information file, this PDF lacks the full narrative context, peer-reviewed pagination of the main letter, and editorial summary statistics presented in the primary article. The `doi` field is empty in this wiki stub; operators should align metadata with the version-of-record DOI recorded on **`[[20180000-0002-5255-7340-j-phys-chem-isotope-effects]]`**.

## Relevance to group

The document supports reproducibility for isotope-specific water modeling with CHON-family ReaxFF parameters and is linked from the canonical isotope-effects article page for van Duin-group water/electrolyte workflows.

## Citations and evidence anchors

- Primary article: `[[20180000-0002-5255-7340-j-phys-chem-isotope-effects]]`

## Related topics

- [[reaxff-family]]
- [[20180000-0002-5255-7340-j-phys-chem-isotope-effects]]
