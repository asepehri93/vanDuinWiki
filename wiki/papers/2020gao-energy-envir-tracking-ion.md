---
id: paper:2020gao-energy-envir-tracking-ion
type: paper
title: "Tracking ion intercalation into layered Ti3C2 MXene films across length scales"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:2d-layered
  - method:dft-static
  - method:reaxff
  - task:experiment-integrated
  - scale:multiscale
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:water-interfaces
  - keyword:validation-experiment
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1039/D0EE01580F"
year: 2020
authors:
  - "Qiang Gao"
  - "Weiwei Sun"
  - "Poorandokht Ilani-Kashkouli"
  - "Alexander Tselev"
  - "Paul R. C. Kent"
  - "Nadine Kabengi"
  - "Michael Naguib"
  - "Mohamed Alhabeb"
  - "Wan-Yu Tsai"
  - "Arthur P. Baddorf"
  - "Jingsong Huang"
  - "Stephen Jesse"
  - "Yury Gogotsi"
  - "Nina Balke"
venue: "Energy Environ. Sci."
pdf_sha256: "ae13d681c692e0e2509c2086704946b229bf9ebc90b240875bfb76dcfb819d08"
pdf_path: "papers/Others/Gao_FIRST_MXene_films_EES_2020.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020gao-energy-envir-tracking-ion -->

Multimodal **experiments** (**operando calorimetry**, **liquid AFM dissipation mapping**) plus **continuum/DFT/ReaxFF-based modeling** track **aqueous cation intercalation** into **Ti\(_3\)C\(_2\) MXene** films, linking **ion positions**, **heat flow**, **mechanics**, and **capacitance** under confinement.

## Summary

The paper addresses how **Li\(^+\), Na\(^+\), K\(^+\), Cs\(^+\), Mg\(^{2+}\)** intercalate between **MXene** sheets in aqueous environments, emphasizing **nonuniform ion distributions**, **dehydration/rehydration** events, and **double-layer** structure distinct from standard planar Gouy–Chapman pictures. The introduction situates **Ti\(_3\)C\(_2\)** among MXenes with reported **volumetric capacitance** benchmarks in acidic and neutral media and stresses that **neutral aqueous electrolytes** remain attractive for practical deployment despite alternative solvent chemistries. **Theory** includes references to **ReaxFF GCMC**-style approaches for water/cation dynamics in related contexts and **first-principles** or continuum components as cited; **calorimetry** ties **enthalpic signatures** to specific ion rearrangements predicted computationally.

## Methods

- **Samples:** **Ti\(_3\)C\(_2\)** films prepared and tested under electrochemical control (details in Methods).
- **Operando calorimetry:** Heat-flow measurements synchronized with electrochemical polarization to probe **ion insertion** thermodynamics.
- **Operando liquid AFM:** Spatial maps of **dissipation** interpreted as **heterogeneous ion populations** within MXene stacks.
- **Modeling (literature context):** The discussion cites **ReaxFF**/**GCMC**-style prior work on **confined** **water**/**ions**; the **first-principles** **dynamics** **performed** **in** this **paper** are **AIMD** (below), not a full **ReaxFF** **production** **run** summarized here.

**1 — MD application (ab initio MD, VASP).** **Engine:** VASP ab initio molecular dynamics (PAW; optB86b-vdW for interlayer dispersion). **System:** **2×2×1** **orthogonal** **supercell** with **~244** **atoms**, **multilayer** **hydroxyl**-**terminated** **Ti\(_3\)C\(_2\)** and a **bilayer** **water** **fill** **(Ti\(_3\)C\(_2\)(OH)\(_2\)(H\(_2\)O)\(_2\))**; **four** **intercalated** **metal** **cations** (treated **as** **neutral** **atoms** in the **setup** **described**). **Boundaries:** **3D** **PBC** in the **supercell** (standard **slab** **+** **confined** **electrolyte**). **Ensemble:** **NPT** at **ambient** **pressure** and **room** **temperature** (as stated). **Timestep:** **1** **fs**. **Thermostat:** **Langevin**. **Barostat:** **NPT** **(isotropic** **ambient** **conditions** **as** **written**). **Duration:** **18** **ps** **total**; **first** **12** **ps** **discarded** as **equilibration**; **last** **6** **ps** **analysed** (with **longer** **statistics** **in** **SI** **for** **some** **plots**). **Electric field:** **N/A** — **open-circuit**-**like** **AIMD** **for** **ion** **site** **sampling** **(no** **finite** **E**-**field** **MD** **in** the **quoted** **protocol**). **Replica**/**umbrella**/**metadynamics:** **N/A**.

**2 — ReaxFF / classical MD in this study: N/A** as a **reported** **production** **code** **path** (ReaxFF **appears** as **prior** **literature** **and** **method** **context**).

## Findings

- **Cation-specific** intercalation pathways alter **mechanical response** and **capacitive energy storage** concurrently.
- **Calorimetry** and **simulation** agree on **exothermic/endothermic** signatures associated with **dehydration** and **H\(^+\) rehydration** processes during ion insertion.
- **AFM dissipation** heterogeneity supports **partially nonuniform** ion distributions inferred from modeling.
- **Average ion–surface distance** vs **capacitance** follows a **modified two-sided Helmholtz** trend, interpreted as a confined **electrical double layer** mechanism distinct from bulk-like EDL models.
- The authors argue this confined EDL picture is important for **energy and power metrics** that depend on how **interlayer spacing**, **confined water**, and **ion oxidation state** co-evolve during charging—topics they connect to prior **XRD/EQCM/neutron** literature on MXene swelling.

## Limitations

Complex electrolytes (additives, pH, anion effects) extend beyond the primary aqueous cation survey; quantitative ReaxFF transferability depends on parameterization for MXene terminations. Multiscale coupling across **calorimetry**, **AFM**, and **simulation** still depends on consistent **electrochemical** boundary conditions between experiment and models, so quantitative heat-flow agreement should be interpreted with the **protocol** details in the article.

## Relevance to group

Touches **ReaxFF electrolyte/MXene** modeling motifs relevant to **interfacial electrochemistry** even though the study is **multimethod and experiment-heavy**.

## Citations and evidence anchors

- DOI: [10.1039/D0EE01580F](https://doi.org/10.1039/D0EE01580F)

## Related topics

- [[batteries-interfaces-reaxff]]
