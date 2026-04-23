---
id: paper:2022yawei-gao-j-phys-chem-al-reaxff
type: paper
title: "C/H/O/F/Al ReaxFF Force Field Development and Application to Study the Condensed-Phase Poly(vinylidene fluoride) and Reaction Mechanisms with Aluminum"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - material:polymer-organic
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.2c02043"
year: 2022
authors:
  - "Yawei Gao"
  - "Wenbo Zhu"
  - "Tao Wang"
  - "Dundar E. Yilmaz"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C 126, 11058–11074 (2022)"
pdf_sha256: "699d3ae0c158c43c2f4c27d851ccbf42be36c0272168b2a05c96be2bc7751d7b"
pdf_path: "papers/Gao_Zhu_PVDF_Al_JPC_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022yawei-gao-j-phys-chem-al-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Develops a **C/H/O/F/Al ReaxFF** for **poly(vinylidene fluoride) (PVDF)** spanning **nonreactive** (polymorph / phase transformation) and **reactive** (pyrolysis and metal oxide surface chemistry) regimes. The abstract frames PVDF as a **(−CH2−CF2−)\(_n\)** repeat unit with chain packing and alignment governing ferroelectric, pyroelectric, and piezoelectric response, and notes practical pairing of PVDF with **aluminum** in energetic composites. Low-temperature work explores **α → β** transitions under **electric poling** and **mechanical deformation**, reporting orientation-dependent **field thresholds** of about **5.0** and **7.5 GV/m** along **y** and **x**, respectively, in the published MD study. Mechanical deformation can convert the **α** **trans–gauche\(^+\)–trans–gauche\(^-\)** motif toward **all-trans** chains, but the stretched structure’s **antiparallel** packing can yield **zero** net polarity; **combined** poling and deformation can **lower** the poling threshold versus poling alone. High-temperature chemistry treats **surface-oxidized Al nanoparticles**, emphasizing initiation by **H** or **F** abstraction at alumina, **HF** evolution from PVDF pyrolysis, rapid **alumina fluorination** to **AlF\(_x\)**, **OH** chemistry and **H\(_2\)O** release, and **AlC\(_x\)** side products, with **Arrhenius** treatment for **AlF\(_x\)** formation where reported.

## Methods

### ReaxFF parameterization (A)

- **Coverage:** **C/H/O/F/Al** ReaxFF intended for **PVDF** (**(–CH\(_2\)–CF\(_2\)–)\(_n\)**) across **nonreactive** (polymorph, polarization) and **reactive** (pyrolysis, **Al/Al\(_x\)O\(_y\)** surface chemistry) regimes.
- **Training data:** **QM** datasets plus selected **experimental** constraints enumerated in the **J. Phys. Chem. C** article and **Supporting Information** (bond/angle dissociation, condensed-phase benchmarks as listed there).
- **Optimization:** **Weighted** least-squares / **ReaxFF** optimization workflow (software named in the paper—commonly **Fortran/C** **ReaxFF** optimizers paired with **DFT** references).

### Low-temperature molecular dynamics (B)

- **Systems:** **α-PVDF** crystal models.
- **Stimuli:** **Electric poling** along defined directions and **mechanical deformation** to drive **α → β** transitions; abstract reports orientation-dependent **coercive field** thresholds near **5.0** and **7.5 GV m\(^{-1}\)** along **y** vs **x** in the published MD study.
- **Analysis:** **Polarization**, **chain conformation**, and **packing** (including cases where **all-trans** chains can yield **zero** net polarity depending on **antiparallel** packing).

### High-temperature reactive MD (B)

- **Systems:** **PVDF** in contact with **surface-oxidized Al nanoparticle** models.
- **Chemistry tracked:** **HF** release, **alumina fluorination** toward **AlF\(_x\)**, **hydroxylation**, **H\(_2\)O** evolution, **AlC\(_x\)** byproducts; **Arrhenius** analysis is applied where the abstract highlights **AlF\(_x\)** formation kinetics.
- **Integration:** **Reactive** ensemble runs at elevated **T** (exact schedules in the article); **QEq** charge updates per standard **ReaxFF** practice unless otherwise noted.

### MD application (low-T PVDF; high-T Al–PVDF)

**Engine / code:** **LAMMPS** with the **C/H/O/F/Al** **ReaxFF**. **Low-T:** **α-PVDF** **crystal** **PBC** **supercell** **models** (unit-cell / **atom** count as in *J. Phys. Chem. C*); **finite** **electric** **field** or **mechanical** **deformation** **stimuli** and **NVT**-style or equivalent **ensembles** as in the **J. Phys. Chem. C** text; **coercive** **field** **thresholds** (~**5.0** / **7.5 GV m\(^{-1}\)**) are **MD** **outputs**, not a separate **continuum** **control**. **High-T:** **PVDF** on **surface-oxidized** **Al** **nanoparticle** models; **N/A** — no **NPT** **barostat** or **open**-circuit **bias** beyond the **reactive** **T** program unless the **SI** adds it; **N/A** — no **metadynamics**/**replica** **sampling** beyond the reported **RMD**. **Timestep**, **thermostat**, **ps**/**ns** **stages** per **article**/**SI**.

## Findings

### Transferability claim

The authors describe the field as **transferable** from **low-T** **polymorph/polarization** behavior to **high-T** **bond-making/breaking** chemistry for **PVDF**/**Al** systems.

### Poling vs mechanical deformation

**Combined** **poling** and **deformation** can **lower** effective **α → β** thresholds compared with **poling alone**, while **packing** determines whether **β**-like chains yield **net** polarization.

### Reactive Al–PVDF sequence

Reactive trajectories support a **hierarchical** picture: **HF** attacks **alumina**, generating **fluorinated** and **hydroxylated** surface species, releasing **water**, and producing **carbide-containing** **AlC\(_x\)** species among side products in the authors’ analysis.

## Limitations

ReaxFF cannot capture electronic polarization and band-structure effects; predicted field thresholds are classical-model dependent and should be interpreted as comparative trends.

## Relevance to group

Core **PVDF + aluminum combustion/ferroelectric** angle with explicit **parameterization** narrative—fits the group’s **reactive organofluorine + metal oxide** portfolio.

## Citations and evidence anchors

https://doi.org/10.1021/acs.jpcc.2c02043 — Abstract summarizes dual low-/high-T scope; Introduction anchors PVDF polymorphism context.

## Related topics

- [[reaxff-family]]
