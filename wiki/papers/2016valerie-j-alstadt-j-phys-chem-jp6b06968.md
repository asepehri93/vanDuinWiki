---
id: paper:2016valerie-j-alstadt-j-phys-chem-jp6b06968
type: paper
title: "Competitive Adsorption of Acetic Acid and Water on Kaolinite"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - material:silicate-glass
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.6b06968"
year: 2016
authors:
  - "Valerie J. Alstadt"
  - "James D. Kubicki"
  - "Miriam Arak Freedman"
venue: "J. Phys. Chem. A (2016) 120, 8339–8346"
pdf_sha256: "6eb856f18410ab2e187e875fce207a910a5778622fa83b04cb356745f95999af"
pdf_path: "papers/Others/Friedman_Kubicki_acid_kaolinite_JPCA_2016.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:oxide-surface
  - keyword:water-interfaces
  - keyword:validation-experiment
---
<!-- id:paper:2016valerie-j-alstadt-j-phys-chem-jp6b06968 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **J. Phys. Chem. A** article identified by `doi`. **DFT** level and **cluster** choices appear in the **Computational** section of the PDF.

## Summary

**DRIFTS** experiments probe **acetic acid** adsorption on **kaolinite** and subsequent exposure to **gas-phase water** to study **competitive adsorption** without liquid water (heated purged cell protocol described in the article). **Molecular modeling** interprets **chemisorbed acetate** motifs (**mono-/bi-dentate** linkages to **Al** sites) and how **water vapor** displaces or preserves species depending on **adsorption geometry**. **Clay mineral** surfaces are abundant **atmospheric** **ice nuclei**; understanding **organic acid** vs **water** competition at **sub-saturation** humidities informs **aerosol** **chemistry** models where **co-adsorption** sets **surface** **hydrophilicity** (introduction themes).

## Methods

**Experiment (DRIFTS).** **Diffuse reflectance infrared Fourier transform spectroscopy (DRIFTS)** probes **acetic acid** adsorption on **low-defect kaolinite (KGa-1b)** (with documented **anatase** impurity per the **Experimental** section), followed by controlled exposure to **gas-phase water** to study **competitive adsorption** without bulk liquid water.

**Static QM / cluster modeling.** **Program:** **Gaussian 09** geometry optimizations and **harmonic frequency** calculations on **kaolinite cluster** models (six **Si** and two **Al** centers with stoichiometric **O/H** saturations—**Figure S1** family) hosting **acetic acid / acetate** motifs, including **hydrated duplicates** with one or two **H\(_2\)O** molecules for hydrogen-bonding (**Figure S2**). **Functionals / basis set:** **B3LYP/6-31G(d,p)** and **M05-2x/6-31G(d,p)** as stated in **Computational Studies**; computed frequencies are scaled by literature factors (**1.0119** for **B3LYP**, **0.9364** for **M05-2x**) when compared to experiment, following **Merrick *et al.*** as cited in the article. **Dispersion:** the **Computational Studies** paragraph does not add a separate **DFT-D**-style correction on top of these hybrid/meta-hybrid choices; **M05-2x** is used as published in **Gaussian 09** without an extra empirical dispersion term called out there. **k-point sampling:** **N/A —** finite molecular clusters rather than periodic **k**-mesh sampling. **Structures / pathways:** **nine** **gas-phase cluster** geometries enumerating **acetate** binding modes plus **hydrated** duplicates; **optimized minima** only (no **NEB** pathway searches in the methods text summarized here). **Properties computed:** **vibrational frequencies** for assignment to **DRIFTS** bands and **relative energies** of adsorption motifs used to judge stability under water co-adsorption.

**1 — MD application.** **N/A —** not used.

**2 — Force-field training.** **N/A —** not used.

**3 — Additional analyses.** Bulk **DRIFTS** ratios vs **kaolinite** reference spectra remove bulk **kaolinite** modes prior to comparing to modeled **acetate** bands as described in the **Computational Studies** paragraph.
## Findings

**Outcomes.** After **acetic acid** dosing, **four chemisorbed acetate** configurations are inferred—**Al**-bound **monodentate**, **bidentate**, and **bidentate bridging** motifs as summarized in the **abstract**.

**Comparisons.** Computed **frequencies** (after removing modes localized on bare **kaolinite**) are used alongside **DRIFTS** fingerprints to assign **surface** species before vs after **water vapor** co-exposure.

**Sensitivity / levers.** The **abstract** stresses that **water vapor** alters **acetate** populations in a **geometry-dependent** way: **binding motif** controls whether **water** **displaces** or **preserves** a given **acetate** configuration.

**Atmospheric / ice-nucleation framing.** The **Introduction**/**Discussion** connect **competitive adsorption** on **clay** surfaces to **mineral dust** processing and **ice nucleation** implications—read those sections for caveats on **field** vs **laboratory** **kaolinite**.

**Limitations (scope).** Natural **dust** is **poly-mineralic** and **structurally heterogeneous** compared with **KGa-1b** laboratory samples; **anatase** impurities may contribute parallel chemistry noted in the article.
## Limitations

- Natural **dust** is more heterogeneous than **KGa-1b**; **anatase** and other **impurities** can contribute parallel **IR** signatures.
- **DRIFTS** assignments depend on **baseline** handling and **packing**; cluster **frequencies** should be transferred only with the **SI** benchmarks in the article.
- **Cluster models** omit long-range **field effects** of extended **clay** stacks; check the **Discussion** before extrapolating to **tropospheric** **multilayer** coatings.

## Relevance to group

Penn State coauthored **clay–water–organics** interface science adjacent to **silicate** geochemistry and environmental surface chemistry in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.6b06968](https://doi.org/10.1021/acs.jpca.6b06968)
- Text-aligned pointers: `normalized/extracts/2016valerie-j-alstadt-j-phys-chem-jp6b06968_p1-2.txt`

## Related topics

- [[theme-oxides-silica-ceramics]]
