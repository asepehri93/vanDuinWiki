---
id: paper:2019liam-s-morrissey-journal-of-s-erosion-spacecraft
type: paper
title: "Erosion of Spacecraft Metals due to Atomic Oxygen: A Molecular Dynamics Simulation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:metal-surface
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.2514/1.A34414"
year: 2019
authors:
  - "Liam S. Morrissey"
  - "Stephen M. Handrigan"
  - "Sam Nakhla"
  - "Ali Rahnamoun"
venue: "Journal of Spacecraft and Rockets"
pdf_sha256: "b9cc1a67a00bc09ca4f4b4fcf37e4ba7fd3cbb534e1edb1594311158c6617fff"
pdf_path: "papers/ReaxFF_others/morrissey_oxidation_spacecraft_rockets_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019liam-s-morrissey-journal-of-s-erosion-spacecraft -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the *Journal of Spacecraft and Rockets* article identified by `doi`, `title`, and `pdf_path`.

## Summary

Low-Earth orbit (LEO) environments contain **atomic oxygen (AO)** that erodes spacecraft materials; flight experiments are expensive, motivating atomistic models. Prior ReaxFF studies emphasized polymers; this paper asks whether **ReaxFF molecular dynamics** can reproduce **high-energy AO impacts** on **silver** and **gold** slabs representing spacecraft metals. The authors report **erosion coefficients** and **surface temperature evolution** as functions of cumulative oxygen impacts (e.g., up to **100** oxygen atoms in the abstract-level protocol) and compare simulation outcomes to **literature erosion data** for LEO-relevant conditions.

The introduction motivates **~4.5 eV** **relative** **collision** energies as representative of **LEO** **AO** encounters for orbiting hardware, explaining why **bond-breaking** reactive frameworks are needed rather than purely elastic scattering models.

## Methods

### 1 — MD application (RMD, sequential AO impacts)

This is **ReaxFF** reactive MD in the same spirit as **Rahnamoun & van Duin** and **Zeng** *et al.*, but applied to **Ag(001)** and **Au(001)** slabs. **Engine / program name:** **N/A** — *Journal of Spacecraft and Rockets* **Sec. II** specifies the **ReaxFF** parameter sets and integration settings but does **not** name a **LAMMPS**-style package. **ReaxFF parameter sets:** **Lloyd** *et al.* for **Ag/Ag/AgO**; **Joshi** *et al.* for **Au**–**O** (citations as in the paper’s **Table 1** footnotes and **Sec. II.A**). **System size and composition:** **(001) FCC** **Ag** and **Au** **slabs** of approximate lateral extent **32×32 Å** and **40 Å** thickness, placed in a **tall** simulation cell (**100** **Å** height, **PBC** in **x** and **y**). **Boundaries:** in-plane **PBC**; **O** is introduced along **+z** toward the **open** **(001)** surface. **Ensemble / stages:** **NVT** equilibration with a **thermostat** at **200** **K** on the **slab**; during **O** **deposition/impact** the run switches to **NVE** and the **thermostat** is **removed** so the collision energy is **not** instantaneously quenched by the **bath** (per **Sec. II.B**). **Time step:** **0.5** **fs** (**Table** **1**). **O** **impact** **energy:** **4.5** **eV** (**7.4** **km/s** in **+z**). **Cadence / duration:** one **O** every **~200** **fs**; **100** **O** impacts over **20** **ps** (**40,000** time steps) as in **Table 1** / text. **Barostat / NPT or mean-stress servocontrol:** **N/A** — **NVE** impact segments at fixed cell volume. **Shear, shock piston, and electric field:** **N/A**. **Erosion accounting:** **atoms** beyond **~10** **Å** from the **pre-impact** **surface** are treated as **eroded** (definition tied to **Ag**–**Ag** / **Ag**–**O** bond lengths, **Sec. II.B** and **Rahnamoun** *et al.*-style **cutoff** **logic**).

### 2 — Force-field training

**N/A** — **uses** published **Lloyd** and **Joshi** **ReaxFF** sets; the article **rehearses** the **ReaxFF** **energy** **partition** (**Sec. II.A**) for readers but does **not** re-fit parameters.

### 3 — Static QM

**N/A** — there is no **Kohn–Sham** / first-principles **DFT** in the manuscript; the **4.5 eV** **AO** reference energy is taken from the **LEO** / **beam**-literature **Introduction** context. The authors compare their **ReaxFF** sputter-style **yields** (mass per **O** atom) to **in-orbit** and **Banks** *et al.* laboratory data (**Sec. III**). A subsidiary **NVT(200 K)**-style run with a **tight** slab thermostat **(Fig. 7)** shows **no** **Ag** erosion, consistent with **Rahnamoun** & **van** **Duin**-style **polymer** **work**.
## Findings

After **100** oxygen impacts, the **silver** **erosion coefficient** aligns closely with literature **LEO** values in the authors’ comparison. **Gold** shows **minimal erosion** relative to silver, consistent with its reputation for AO resistance. The authors argue ReaxFF MD offers a comparatively **low-cost** way to screen AO–metal interaction scenarios for materials selection and lifetime estimation, subject to force-field limitations.

**Interpretation.** The work positions **temperature** evolution as a diagnostic: **hot** **spots** coincide with **reactive** **removal** regimes, echoing themes from earlier **ReaxFF** **AO** studies on **polymers** and **silica** cited in the introduction.

**Materials selection narrative.** Because **Ag** and **Au** bracket **high** vs **low** **erosion** under the same **impact** **protocol**, the study supports using **ReaxFF** **MD** as a **screening** **tool** for **new** **coatings** or **alloys** before **flight** **qualification**, provided **parameter** **scope** includes the **elements** of interest.

**Limits.** The manuscript does not replace **orbital** **environment** models that include **angular** **flux** distributions, **surface** **roughness** at **micrometer** scale, or **synergistic** **UV**/**electron** exposure; those effects require **multiphysics** **extensions** beyond atomistic **MD**.

## Limitations

Reactive metal–oxygen models may not transfer to alloys or oxide-passivated surfaces without reparameterization; impact statistics in MD are not a full orbital environment model.

## Relevance to group

Demonstrates ReaxFF application to **reactive gas–metal collisions** outside hydrocarbon- or silica-centric group studies.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.2514/1.A34414](https://doi.org/10.2514/1.A34414) (`papers/ReaxFF_others/morrissey_oxidation_spacecraft_rockets_2019.pdf`).

## Related topics

- [[reaxff-family]]
