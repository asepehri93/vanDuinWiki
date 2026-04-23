---
id: paper:2018yang-j-phys-chem-prediction-glass
type: paper
title: Prediction of the Glass Transition Temperatures of Zeolitic Imidazolate Glasses
  through Topological Constraint Theory
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:reaxff-lineage
- material:zeolite-porous
- method:reaxff
- task:application
- task:method-development
- scale:atomistic
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpclett.8b03348
year: 2018
authors:
- Yongjian Yang
- Collin J. Wilkinson
- Kuo-Hao Lee
- Karan Doss
- Thomas D. Bennett
- Yun Kyung Shin
- Adri C. T. van Duin
- John C. Mauro
venue: J. Phys. Chem. Lett.
pdf_sha256: 8b60ae242d6f9839444651f5816696194c3b0bdf2f21399ff9eccacae714ca01
pdf_path: papers/Yang_ZIF_JPCL_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018yang-j-phys-chem-prediction-glass -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

For **agZIF-62** glasses of composition **Zn(Im₂₋ₓbImₓ)**, the work builds a **topological constraint model** for **glass transition temperature (Tg)** that combines **experimental** data with **ReaxFF molecular dynamics** to define a **hierarchy of bond constraints**. The model reproduces **Tg** versus **benzimidazolate** content with reported **~3.5 K** error and is extended to **5-methylbenzimidazolate**, yielding a **ternary Tg diagram** for a **hypothetical** three-ligand framework. **Yang**, **Shin**, and **van Duin** anchor the **reactive MD** contribution; **Mauro** and collaborators provide the **constraint-theory** framework for **MOF glasses**.

## Methods

### Topological constraint theory (**TCT**) backbone

The letter develops a **constraint hierarchy** for **agZIF-62** compositions **Zn(Im\(_{2-x}\)bIm\(_x\))**, treating **ZnN\(_4\)** tetrahedra and **imidazolate / benzimidazolate** linkers as network formers. **Hydrogen** is excluded from connectivity counting because it is monovalent and does not change the **Im/bIm** backbone graph. **Bond-stretching (BS)** and **bond-bending (BB)** constraints are assigned per **Figure 1**, with **mean coordination ⟨r⟩** feeding the usual **TCT** counting formulas (eq. (1) in the paper). **Temperature-dependent** constraint survival probabilities **\(q_n(T)\)** follow the Mauro **onset-temperature** construction (their eq. (2)), yielding ordered onsets **\(T_\beta < T_\gamma < T_\alpha\)** so the network is **stressed-rigid** at low **\(T\)** and progressively unlocks **floppy** modes as **\(T\)** rises (**Figure 2**).

### ReaxFF **MD** used as a rigidity probe (**SI**)

The main text does **not** reproduce full **LAMMPS** decks on the printed pages; instead it cites **Supporting Information** **ReaxFF MD** of **ZIF-62** to measure **relative standard deviations (RSD)** of **C–C** and **C–N** bonds and of **C–N–C** / **N–C–N** angles (**RSD < 0.04–0.05**) versus **temperature** from **300 K to 1200 K**, while **N–Zn–N** remains comparatively **floppy** (**RSD ~0.12–0.19**). The authors caution that **Zn–N(bIm)** stiffening inferred from **MD** appears near **~500 K** but the **true** onset may be higher because the **ZIF ReaxFF** parameterization was trained on **small Zn/Im clusters** rather than full frameworks (**Gaillac et al.** barrier discussion).

- **Engine / code:** **ReaxFF** **molecular dynamics**; **LAMMPS** is the standard engine for this parameter line in the broader corpus, but operators should copy the exact package callouts from the **SI** PDF bundled with **`papers/Yang_ZIF_JPCL_2018.pdf`**.
- **System / PBC:** **ZIF-62** supercell for the **RSD** study (**atom** totals and **periodic** lattice vectors **N/A — SI-only** in this workspace curation).
- **Ensemble, timestep, barostat, production length:** **N/A — not restated** on the **letter** pages; the article directs readers to the **Supporting Information** for **equilibration**/**production** segment lengths in **ps**, **NVT**/**NPT** labels, and **fs** timesteps.
- **Thermostat:** **N/A — thermostat** brand/damping is **not named** in the **letter** excerpt used here—confirm in the **SI** trajectory description.
- **Pressure:** **N/A — MD barostat targets** for the **RSD** validation runs are **not stated** in the **letter** body (see **SI** if pressure coupling was used).
- **Electric field / replica / metadynamics:** **N/A — not used** for the **RSD** survey described above.
## Findings

- **Outcomes / mechanisms:** The **TCT + ReaxFF** pipeline reproduces **\(T_g\)** vs **benzimidazolate** fraction for **Zn(Im\(_{2-x}\)bIm\(_x\))** glasses with **mean absolute error ~3.5 K** (letter headline; abstract quotes **<4 K** vs **DSC** data). **Constraint onsets** (**\(T_\beta<T_\gamma<T_\alpha\)**) explain how the network moves from **stressed-rigid** to **floppy** as temperature increases (**Figure 2** narrative).
- **Comparisons:** Predicted **\(T_g\)** tracks **experimental DSC** traces for literature **agZIF** compositions; **RSD** metrics from **ReaxFF MD** justify treating **Im/bIm** internal coordinates as **rigid** relative to the **floppy N–Zn–N** hinge at sub-**\(T_g\)** temperatures.
- **Sensitivity / design levers:** Varying **\(x\)** shifts the balance of **Zn–Im** vs **Zn–bIm** constraints, which feeds directly into the **\(T_g\)** curve; extension to **5-methylbenzimidazolate** produces a **ternary** **\(T_g\)** diagram for a hypothetical three-ligand glass.
- **Limitations / outlook (as authored):** The authors flag that **MD-predicted Zn–N(bIm)** stiffening near **~500 K** may underestimate the true onset because **ReaxFF** was trained on **small clusters**; **TCT** itself remains a **coarse** rigidity factorization that may need full cooling **MD** near **borderline** chemistries.
- **Corpus honesty:** Verbatim **abstract** paste and publisher boilerplate were **removed** from this page; operators needing **DSC** scan rates (**10 K/min**), **constraint** tables (**Table 1**), or **SI** **MD** settings should read **`papers/Yang_ZIF_JPCL_2018.pdf`** directly.

## Limitations

- **TCT** assumes a **coarse** decomposition of **rigidity**; **local** chemical detail may require **full MD** cooling curves for **borderline** compositions.
- **ReaxFF** must be **trusted** for each **ligand chemistry** before **constraint** parameters are exported to **theory**.

## Relevance to group

Links **Penn State ReaxFF** on **ZIF** **glasses** to **Mauro-group** **topological constraint** methods for **Tg** design.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpclett.8b03348` (`papers/Yang_ZIF_JPCL_2018.pdf`).

## Related topics

- [[reaxff-family]]
