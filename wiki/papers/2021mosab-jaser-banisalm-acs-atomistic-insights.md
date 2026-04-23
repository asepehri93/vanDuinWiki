---
id: paper:2021mosab-jaser-banisalm-acs-atomistic-insights
type: paper
title: 'Atomistic insights into H\(_2\)O\(_2\) direct synthesis of Ni–Pt nanoparticle catalysts under water solvents by reactive molecular dynamics simulations'
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - material:metal-surface
  - method:reaxff
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:catalysis-surface
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.1c01947"
year: 2021
authors:
  - "Mosab Jaser Banisalman"
  - "Hong Woo Lee"
  - "Heeyeun Koh"
  - "Sang Soo Han"
venue: "ACS Appl. Mater. Interfaces (2021); DOI 10.1021/acsami.1c01947"
pdf_sha256: "f3a239d0e20903d5bde4fe48fde5725841d5f928906bd42a0c1cd1775a7e16ef"
pdf_path: "papers/ReaxFF_others/Banisalman_Han_NiPt_H2O2_ACS_AMI_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021mosab-jaser-banisalm-acs-atomistic-insights -->

## Summary

**Direct synthesis** of **hydrogen peroxide** from **H₂** and **O₂** over **bimetallic** catalysts is attractive industrially, but **selectivity** hinges on suppressing **over-reduction** and **O–O** cleavage pathways while keeping **H₂** activation facile. Banisalman *et al.* simulate **Ni–Pt** **nanoparticles** spanning **1.5–3.5 nm** in explicit **water** at compositions **Ni₉₀Pt₁₀**, **Ni₈₀Pt₂₀**, and **Ni₅₀Pt₅₀** using **ReaxFF MD**, augmented by **DFT** for key **elementary** energetics. The study correlates **facet** and **site-type** statistics—especially **NiNiPt-fcc** and **Ni–Ni bridge** ensembles—with **H₂** versus **O₂** **dissociation** propensities and with **H₂O₂** **selectivity** metrics emerging from trajectories.

## Methods

**MD application (ReaxFF, LAMMPS).** The article uses **LAMMPS** with the published **ReaxFF** for **Ni–Pt** / water / **H\(_2\)** / **O\(_2\)** (force-field citation in the paper). **Relaxation** uses **conjugate-gradient** **minimization** plus **MD** in a **microcanonical (NVE)** **ensemble** as written; **production** **MD** extends to **400 ps** with a **1 fs** time step and **Langevin**-type **temperature** **control** (damping **10⁻¹** and **10** **fs** for **Ni/Pt** and **O/H**, respectively, in the text). **Long-range electrostatics:** **PPPM** for the **Coulomb** term. **System class:** **fcc** **Ni\(_x\)Pt\(_{1-x}\)** **nanoparticles** **1.5–3.5 nm** in **diameter** and compositions **Ni\(_{90}\)Pt\(_{10}\)**, **Ni\(_{80}\)Pt\(_{20}\)**, **Ni\(_{50}\)Pt\(_{50}\)**, in **explicit** **water** with **>10⁴–10⁵**-atom **ReaxFF-MD** **cells** (per the article). **3D** **PBC** as in their **non-bulk** **nanoparticle** **setup**. **Barostat — N/A** (no **NPT** **barostat** in the **stated** **protocol**). **Hydrostatic** **pressure** as an **MD** **knob** **— N/A** in the **same** **sense**. **Electric field, impact, umbrella — N/A** in the **documented** **runs**.

**Static / constrained QM.** Complementary **DFT** (see the article) supplies selected **barriers** and **mechanistic** **checks** (e.g. **O\(_2\)** **dissociation** vs **Pd**-type surfaces) that are **difficult** in large **solvated** **NP** **ReaxFF** runs; full **functional**/**basis** lines are in the *ACS AMI* file + **SI**.

**Force-field reparameterization. N/A** (literature ReaxFF).

## Findings

**Catalytic performance and structure.** In the ReaxFF-**MD** **metrics** reported, **3.0 nm** **NPs** show a favorable balance of **activity** and **H\(_2\)O\(_2\)** **selectivity** even though **catalytic** **response** is **not** a simple function of **surface** **area**—**site** **counts** (**NiNiPt-**fcc**, **Ni–Ni bridge** ensembles) co-vary with **H\(_2\)** **dissociation** and **O\(_2\)** **dissociation** propensities. The authors highlight **Ni\(_{80}\)Pt\(_{20}\)** at about **3 nm** as a **compositional** **optimum** in their simulation campaign.

**Mechanism.** **Langmuir–Hinshelwood** routes remain in play, but trajectories and supporting **DFT** also support **water-mediated** H\(_2\)O\(_2\)-forming pathways argued to be more accessible on **Ni–Pt** than on **Pd**-type surfaces.

**Comparisons.** **N/A** — direct **laboratory** kinetics in this **computational** paper; authors compare against prior **DFT** **slab** literature and **ReaxFF**+**MD** use cases. **ReaxFF** is noted as still **parametrization**-sensitive for **oxides**/**hydroxide** edge cases when predicting **TOF**-level quantities.

**Sensitivity.** Performance varies with **NP** **diameter** and **Ni:Pt** **stoichiometry**; **concentration** and **water**-mediated **network** **structure** enter the **interfacial** **selectivity** picture.

## Limitations

ReaxFF remains parametrization-dependent for transition-metal/water interfaces; quantitative turnover frequencies require experimental calibration. **Microkinetic** interpretation should keep **explicit water** structure—**double-layer** fields and **surface hydroxyl** populations—in view when mapping trajectories to **engineering** metrics. **Particle** **faceting** may evolve under **reaction** conditions; the study’s **frozen** **nanoparticle** morphology is a modeling convenience that experiments may violate at long times. **DFT** segments in the paper are used to anchor selected **barriers**; treat **ReaxFF** **selectivity** trends as **qualitative** when extrapolating to **industrial** **pressure** or **electrolyte** **pH** outside the simulated **water** boxes.

## Relevance to group

Reactive MD + DFT for **bimetallic** **H\(_2\)O\(_2\)** catalysis in explicit solvent—parallel themes to other ReaxFF catalysis entries.

## Citations and evidence anchors

- ACS Appl. Mater. Interfaces **13**, 20123–20133 (2021); DOI **10.1021/acsami.1c01947**.

## Related topics

- [[reaxff-family]]
- [[catalysis-surfaces]]
