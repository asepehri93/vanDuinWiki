---
id: paper:2019liu-j-phys-chem-formation-alfx
type: paper
title: "Formation of AlFx Gaseous Phases during High Temperature Etching: A Reactive Force Field Based Molecular Dynamics Study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:application
  - material:oxide
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.9b03957"
year: 2019
authors:
  - "Yongli Liu"
  - "Yang Qi"
  - "Xianwei Hu"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C 123:16823-16835 (2019)"
pdf_sha256: "bf9a5e02f4dd35b3e74d1360d81465ab696811f32921e1092cbe255e977f654f"
pdf_path: "papers/Liu_AlF_etching_JPCC_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019liu-j-phys-chem-formation-alfx -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The work develops a ReaxFF parameterization for Al–F interactions fitted to QM-derived training data for gaseous AlFx species and Al–F crystal phases, then apply it to reactive MD of high-temperature etching. Simulations scan fluorine source strength (F/Al = 1–6) and temperature (1000–1500 K), resolving how gaseous AlFx products emerge in a multi-step sequence. A critical F/Al ratio near 3 separates regimes where clustered AlFx remains largely nonvolatile from a “fifth step” regime producing isolated gas-phase species such as AlF4, AlF5, and AlF6 with more favorable formation energies.

## Methods

**2 — Force-field training.** The authors develop an **Al–F** extension of **ReaxFF** by fitting **bond/valence** parameters for **Al–F** and **F–F** and angles **Al–F–Al** and **F–Al–F** against a **DFT** training set. **QM reference (bulk and molecules):** **fcc-Al** and **R3̅c-AlF₃** data come from **CASTEP** with **GGA–PBE**, **ultrasoft pseudopotentials**, **plane-wave cutoffs** of **160 eV (Al)** and **370 eV (AlF₃)**, and a **6 × 6 × 6** **k**-point mesh, with **geometry optimization** tolerances as stated in **§2.4** of the article. **Gas-phase AlF\(_x\)** reference data use **Gaussian 09** with **B3LYP** and a **6-311G** **basis** (per **§2.4**). The training set spans **Al metal**, **AlF₃** crystal, and **F₂**, **AlF**, cation/anion **AlF\(_x\)** species up to **AlF₆³⁻** (see **§2.2**). **Optimization** uses the **ReaxFF** parabolic-extrapolation workflow against these QM targets (as described in the *J. Phys. Chem. C* paper).

**1 — MD application (etching with the fitted Al–F ReaxFF).** **Reactive MD** places **F** on/into an **Al** **supercell** **slab**-like **etching** **geometry** (see **§3.2** **and** **figures** for **atom** **counts** and **stoichiometry**); **3D** **periodic** **boundary** **conditions** apply to the **cell** as in the **JPCC** **setup**. **Ensemble:** **NVT** at **target** **temperatures** **(1000–1500 K** **sweeps** **in** **§3.2**, **with** **1250 K** **used** **as** a **representative** **etch** **temperature** **in** the **text**)**. **Timestep** **0.25** **fs**; **production** **duration** **250** **ps** **per** the **quoted** **etch** **segment**; **equilibration** **stages** **precede** **production** **in** the **same** **section** **(see** **PDF** **for** **full** **multi-** **stage** **protocol**)**. **Thermostat** **implementation** **(e.g.,** **Berendsen** /**Nosé–Hoover**)**:** **N/A** on this **summary** **page**—the **indexed** **p1–2** **excerpt** **does** **not** **name** the **heat**-**bath** **style**; **read** the **full** **Methods** **in** **VOR** **PDF**/**SI** **before** **reproducing** **\(damping** **constants\)**. **Engine / code name:** **N/A** in the **short** **excerpt**; **treat** as **generic** **ReaxFF** **reactive** **MD** **with** the **numeric** **settings** **above** **anchored** **to** **§3.2**.

**Barostat / mean pressure control in production etch MD:** **N/A** — **NVT** runs at fixed cell volume (no **NPT** servocontrol in the quoted etch segment).

**Electric field / plasma bias:** **N/A** in the MD cells; the abstract mentions **voltage**/**discharge** only as a qualitative external lever, not as an applied **E-field** in the reported trajectories.

**Replica / enhanced sampling:** **N/A**.

**3 — Static QM / DFT-only as primary result:** **N/A** — **DFT** supports the **ReaxFF** fit; the scientific story is **reactive MD** with the new **Al–F** parameters.
## Findings

**1 — Outcomes & mechanisms.** The **Al–F** **ReaxFF** **reproduces** the **QM** **training** **EOS**/**energetics** for **Al–F** **crystals** and **molecules** in the **benchmark** **plots** **(Figs.** **2–5** **class** **comparisons** **in** the **article**). In **reactive** **etching** **MD**, **gaseous** **AlF\(_x\)** **formation** **unfolds** in **five** **conceptual** **steps** **with** **F/Al** **as** the **primary** **stoichiometric** **knob**; **below** **F/Al** **≈** **3** the **chemical** **driving** **force** **is** **too** **weak** to **complete** the **fifth** **step**, **leaving** **clustered** **AlF\(_x\)** **without** **strong** **gas**-**phase** **release**, **whereas** **above** **that** **ratio** **isolated** **higher**-**coordination** **gas**-**like** **species** **(AlF\(_4\)**-**class** **through** **AlF\(_6\)**-**class** **motifs** **as** **named** **in** the **abstract**)** **emerge** **with** **more** **exothermic** **formation** **trends** **in** the **model**. **2 — Comparisons vs** **QM** **and** **literature**-**style** **expectations** are **through** the **EOS**/**reaction**-**energy** **tables** **and** **DFT** **curves** **embedded** **in** **§3.1**; **experimental** **plasma** **comparisons** are **not** **the** **focus** **of** the **atomistic** **cells** **(see** **Limitations**)**. **3 — Sensitivity** **to** **levers:** **F/Al** **(1–6)** **and** **temperature** **(1000–1500 K)** **shift** **which** **AlF\(_x\)** **products** **dominate** **and** **how** **fast** **etch**-**like** **sequences** **run** **in** **the** **model**; the **abstract** **also** **mentions** **(via** **wording** **on** **“voltage** **/”** **discharge”)** **that** **non-** **MD** **external** **energetics** **could** **modulate** **yields** **even** **when** **the** **simulation** **cell** **omits** **a** **bias** **field**. **4 — Authored** **limitations** / **outlook** — **simplified** **radical** **treatments** **of** **AlF\(_4\)^–** / **AlF\(_5\)^2–** / **AlF\(_6\)^3–** **are** **explicit** **in** the **text**; **reactor-** **scale** **plasma** **or** **flow** **phenomena** **are** **outside** the **slab-** **like** **ReaxFF** **protocol** **(see** **##** **Limitations**)**. **5 —** **Corpus** **/ KB** **honesty** — **cluster**-**level** **atom** **counts** **and** **full** **thermostat** **lines** **should** be **pulled** **from** the **VOR** **PDF** **if** **this** **wiki** **line** **is** **insufficient** **for** **reproducibility**.

## Limitations

Specific to Al–F high-temperature etching chemistry; plasma and reactor-level transport are not resolved. Parameter set should be checked before transfer to unrelated Al chemistry. **Reactor** **models** that need **ion** **energy** distributions, **wall** **recombination**, and **flow** **residence** times should combine these **MD** insights with **continuum** **CFD** or **plasma** **kinetics** tools. **Chamber** **wall** **materials** and **substrate** **bias** can shift **F/Al** **ratios** away from **idealized** **bulk** **simulation** **cells**.

## Relevance to group

van Duin co-authorship; demonstrates ReaxFF for halide etching and multicomponent gas-phase speciation relevant to processing and preparative Al–F chemistry.

## Citations and evidence anchors

`papers/Liu_AlF_etching_JPCC_2019.pdf` — abstract (mechanism summary, F/Al = 3 threshold), methods for FF training. https://doi.org/10.1021/acs.jpcc.9b03957

## Related topics

- [[reaxff-family]]
