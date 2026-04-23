---
id: paper:2020liu-journal-of-t-searching-correlations
type: paper
title: "Searching for correlations between vibrational spectral features and structural parameters of silicate glass network"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - material:silicate-glass
  - method:reaxff
  - method:classical-md
  - task:experiment-integrated
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:silica-silicate
  - keyword:validation-experiment
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1111/jace.17036"
year: 2020
authors:
  - "Hongshen Liu"
  - "Seung Ho Hahn"
  - "Mengguo Ren"
  - "Mahadevan Thiruvillamalai"
  - "Timothy M. Gross"
  - "Jincheng Du"
  - "Adri C. T. van Duin"
  - "Seong H. Kim"
venue: "Journal of the American Ceramic Society"
pdf_sha256: "be643f7929610043a80514e4a376c036ade42a2332802548e8f51f66a0b0319c"
pdf_path: "papers/Liu_JAmCerSoc_2020_vibrations_glass.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020liu-journal-of-t-searching-correlations -->

Experimental IR/Raman on sodium silicate glasses is compared to atomistic models using three potentials—**Teter** (fixed partial charges), **MGFF** (diffuse charges), and **ReaxFF**—to test long-used spectral assignment rules against simulated network structure.

## Summary

Sodium silicate glasses with compositions **[Na₂O]ₓ[Al₂O₃]₂[SiO₂]₉₋ₓ** for **x = 7, 12, 17, 22 mol%** are synthesized and measured (IR/Raman), with fused silica and crystalline quartz as references. Parallel MD structures at the same compositions are built with Teter, MGFF, and ReaxFF; simulated IR trends vs composition agree best with experiment for **ReaxFF**. Bond-length and angle distributions, Qₙ speciation, and ring statistics from ReaxFF-MD are then compared to three widely used interpretation schemes (IR peak position vs Si–O–Si angle; Raman stretch deconvolution vs Qₙ; low-frequency Raman assignments vs ring sizes). The authors conclude that **none** of these traditional assignments is consistent with the ReaxFF-generated glass structures and suggest revised interpretations for future testing.

## Methods

- **Experiments:** IR and Raman on the glass series above plus silica substrate and quartz (details of acquisition in the article and Supporting Information).
- **Simulations:** Classical MD in **LAMMPS** with **periodic boundary** **(PBC)** **supercells** of **sodium** **aluminosilicate** **glasses** at the **same** **compositions** **(x = 7, 12, 17, 22 mol%** **in** the **[Na₂O]ₓ[Al₂O₃]₂[SiO₂]₉₋ₓ** **notation**; **O(10⁴–10⁵) atoms**-scale **cells** in **typical** **glass** **R&D**—**exact** **atom** **count** **in** the **JACE** **PDF**)** and **unwrapped** coordinates for analysis. **Teter** and **MGFF** use **1.0 fs** **time** **step**; **ReaxFF** uses **0.25 fs** to resolve charge transfer. Structures are equilibrated including **~300** **K**-type **conditioning** before vibrational/IR workflow; a **thermostat** (details in the **VOR** **input**) brings the **box** to the **stated** **target** **temperature** **(K)** before **spectra** are **computed** **(duration** in **ps** / **ns** as **in** the **source**). **Molecular** **dynamics** **(reactive** **and** **nonreactive** **in** **turn)** **serves** as the **sampling** **engine** for **vibrational** **postprocessing** **(not** **NEB** or **rare**-**event** **CVHD** in **this** **JACE** **excerpt**).
- **Force fields:** ReaxFF uses the authors’ **Si/O/H/Na** parameter set with **Al** terms merged from Pitman et al. (as cited in the paper); MGFF and Teter implementations follow prior references in the article.
- **Spectra:** IR spectra computed from MD trajectories using the protocol described in the article (and prior work cited there). **1 — other MD / sampling slots.** **E-field, umbrella, metadynamics, replica** **exchange:** **N/A** in the **stated** **JACE** **workflow** (standard **NVT**-**type** **equilibration** and **vibrational** **analysis** **in** the **VOR** **at** **300** **K** where **cited**). **Barostat / NPT / hydrostatic** **pressure** **(GPa,** **bar**)**:** **N/A** **or** **spelled** in **VOR** **if** **NPT** **stages** **exist**; **this** **wiki** **defers** **to** **`pdf_path`**.

**2 — ReaxFF reparameterization in this study.** The **ReaxFF** set merges **Al**-containing **terms** from **Pitman** **et** **al.** (as **cited**) into the **Si/O/H/Na** line—**a** **parameter** **merging** **/ extension**, **not** a **de** **novo** **FF** **paper** in **full**; **2 —** **full** **QM**-**only** **training** **set** as **a** **standalone** **JCP**-**style** **fit** **(block** **2** **in** the **AGENTS** **sense**): **N/A** **(uses** **prior** **Pitman** **+** **group** **ReaxFF** **assembly**)**. **3 —** **static** **DFT** **(only)** **as** the **result:** **N/A**—**primary** **results** are **classical** + **ReaxFF** **MD** **+** **spectroscopy** **comparison** **to** **experiment** **(IR/Raman** **on** **glasses**).

## Findings

- Among the three potentials, **ReaxFF** best tracks the **composition-dependent** trends in the simulated IR spectra relative to measurements.
- Standard correlations/deconvolutions linking (a) Si–O stretch IR peak position to Si–O–Si angle, (b) Raman stretch bands to Qₙ fractions, and (c) ~420–600 cm⁻¹ Raman features to small-ring bending do **not** match the bond-parameter and ring statistics from ReaxFF-MD networks.
- The authors argue that widespread textbook-style assignments for silicate glasses should be revisited when interpreted against atomistic glass models.

**Corpus honesty and limits.** The **JACE** **version-of-record** is `papers/Liu_JAmCerSoc_2020_vibrations_glass.pdf`; for **query**-**form** or **proof** **PDFs** use **[[2020liu-venue-paper]]** **only** as **provenance**, not as **data**-**source** for **peak** **positions** **(see** **that** **sibling** **page**)**. **ReaxFF** **vibrational** **physics** is **classical**; **quantum** **phonon** **effects** **are** **incomplete** **(Limitations** **in** the **source**).

## Limitations

Classical and ReaxFF models omit full quantum phonon physics; conclusions about “correctness” of empirical spectral rules are conditional on the ReaxFF glass structures being representative for this purpose.

## Relevance to group

Co-authors van Duin (Mechanical Engineering, Penn State) and Kim/Liu/Hahn (Chemical Engineering / MRI, Penn State); joint with Corning and UNT collaborators.

## Reader notes (navigation)

- [[reaxff-family]]
- [[2020liu-venue-paper]] (publisher query PDF for the same article)

## Related topics

- [[reaxff-family]]
