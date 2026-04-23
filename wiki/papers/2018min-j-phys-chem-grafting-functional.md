---
id: paper:2018min-j-phys-chem-grafting-functional
type: paper
title: Grafting Functional Groups in Polymeric Binder toward Enhancing Structural
  Integrity of LixSiO2 Anode during Electrochemical Cycling
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:batteries-electrochemistry
- domain:reactive-md
- domain:reaxff-lineage
- material:polymer-organic
- method:reaxff
- task:application
- scale:atomistic
paper_keywords:
- keyword:batteries-interfaces
- keyword:reaxff-application
- keyword:lammps
- keyword:nvt-simulation
- keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcc.8b03625
year: 2018
authors:
- Kyoungmin Min
- Aravind R. Rammohan
- Sung Hoon Lee
- Sushmit Goyal
- Hyunhang Park
- Ross Stewart
- Xiaoxia He
- Eunseog Cho
venue: J. Phys. Chem. C 2018, 122, 17190–17198
pdf_sha256: b7f9dfda28cbd03d2c5da3199adb19585844c26d016abe5f3ee3e12dfd1861d7
pdf_path: papers/ReaxFF_others/Min_LixSiO2_Polymer_JPCC_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018min-j-phys-chem-grafting-functional -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **J. Phys. Chem. C** (**DOI** in front matter). Stress–strain and adhesion metrics must be taken from **figures**/**tables**.

## Summary

**Atomistic MD** compares **polyethylene** binders **grafted** with **polar** (**COOH**, **OH**) versus **nonpolar** (**CH₃**) groups on **lithiated silica** **LiₓSiO₂** for **x = 0–4**, using **pulling** tests and **uniaxial tensile** tests to relate **interfacial adhesion**, **failure mode**, and **mechanical** response to **lithiation** level. **Polar** functionalities are reported to improve **adhesion** and **suppress volume expansion** during lithiation, while **nonpolar** binders tolerate **larger strain** but fail more **cohesively** at low lithiation.

The study illustrates a practical **multi-force-field** workflow for **battery** interfaces where the **oxide** electrode is treated reactively while the **polymer** binder uses a **fixed-bond** organic force field with tailored **interface** mixing rules.

## Methods

### A — Force fields and cross-terms

- **Polymer binder:** **INTERFACE** **force field** for **grafted polyethylene** with **COOH**, **OH**, or **CH\(_3\)** terminations as built in §2.
- **Electrode:** **ReaxFF** for **lithiated silica** **Li\(_x\)SiO\(_2\)** across **\(x=0\)–\(4\)**.
- **Binder–oxide coupling:** **9–6 Lennard-Jones** + **Coulomb** for **cross-interactions** between subsystems (**12 Å** cutoff) with parameters from the cited **interface** mixing rules.

### B — Equilibration and mechanical tests

- **Engine:** **LAMMPS**.
- **Stages:** **NVT** **relaxation** (**1 ns**, **300 K**) then **NPT** **equilibration** (duration/pressure target in **JPCC** **Methods**), followed by **pulling** (**adhesion**) and **uniaxial tensile** tests reported in **Results**.

### C — Electrostatics / cutoffs

- **Coulomb** summation and **neighbor** conventions follow **INTERFACE**/**ReaxFF** defaults described in §2; verify **PPPM**/**cutoff** choices in the article when porting inputs.

### D — Experiments

- **Not stated in the available wiki summary** as containing new **synthesis**/**cycling** experiments—this is primarily a **computational** **interface** screening study.

### MD application (integrated)

Beyond §A–C: **timestep**, **neighbor list** rebuilds, and any **PPPM** settings for **cross-interface Coulomb** should be copied from §2 of the **JPCC** article (`papers/ReaxFF_others/Min_LixSiO2_Polymer_JPCC_2018.pdf`). **System & composition:** hybrid **Li\(_x\)SiO\(_2\)** **slab** supercells with **grafted polyethylene** binders (**atom** totals and **stoichiometry** in **Methods**). **PBC:** **three-dimensional periodic boundary conditions** for the **slab** cells. **Thermostat:** coupled to the **NVT** **relaxation** stage (**1 ns**, **300 K** in §B); damping/time constant values live in **Methods** (**N/A — numeric damping** not duplicated here). **Barostat:** **NPT** **equilibration** follows the **NVT** stage as described in **Methods** (**target pressure** there). **Electric field / bias:** **N/A — not used** in the mechanical test framing summarized here. **Enhanced sampling:** **N/A — not indicated**.
## Findings

**Polar** groups improve **adhesion** to **LiₓSiO₂** relative to **nonpolar** controls in the reported **pulling** tests. **Failure** shifts from **cohesive** (nonpolar) toward **mixed adhesive/cohesive** behavior for **polar** binders as **lithiation** increases. **Polar** binders reach **higher maximum stress**, while **nonpolar** binders sustain **larger strain** before failure in the **tensile** tests summarized. **Polar** chemistry more effectively **suppresses** **volume expansion** during lithiation in the simulated cells.

**Comparisons / sensitivity.** Trends are organized vs **lithiation level** **\(x=0\)–\(4\)** and **graft chemistry** (**COOH**, **OH**, **CH₃**), i.e., **interface** chemistry and **strain**-to-failure levers tied to the **computational** tests.

**Limitations / outlook.** **Voltage-dependent** electrochemistry and explicit **electrolyte** are outside the summarized **INTERFACE + ReaxFF** mechanical screening (see **## Limitations**).

**Corpus honesty.** Stress–strain numbers live in **figures/tables** of the **PDF**; this page does not restate those scalars.
## Limitations

**INTERFACE + ReaxFF** **electrostatics** across the **interface** is an **engineering** choice; **voltage-dependent** electrochemistry and **explicit** **electrolyte** are not fully captured. **Classical** models may miss **charge transfer** at highly lithiated interfaces.

Practically, the paper is most useful as a **screening** story: **grafting** chemistry shifts **adhesion** vs **cohesion** balance as **LiₓSiO₂** expands, which maps to **binder** design levers (polar **COOH/OH**) even when quantitative **cycle life** requires continuum or **continuum–atomistic** coupling beyond this **MD** setup.

## Relevance to group

Demonstrates **LAMMPS** workflows combining **INTERFACE** + **ReaxFF** for **binder**–**oxide** **LIB** interfaces—adjacent to **`batteries-interfaces-reaxff`** themes.

The **lithiation sweep** (**x = 0–4**) makes the paper a convenient **navigation** target for questions about how **binder** performance should change as **silica** becomes progressively **lithiated** during cycling—an effect that continuum **mechanical** models sometimes treat only implicitly.

## Citations and evidence anchors

- DOI [10.1021/acs.jpcc.8b03625](https://doi.org/10.1021/acs.jpcc.8b03625).
- Excerpt alignment: `normalized/extracts/2018min-j-phys-chem-grafting-functional_p1-2.txt`.

## MAS / retrieval

`paper_keywords` lists **`keyword:lammps`**, **`keyword:nvt-simulation`**, and **`keyword:npt-simulation`** to capture the **multi-stage** equilibration workflow used before **mechanical** tests.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
