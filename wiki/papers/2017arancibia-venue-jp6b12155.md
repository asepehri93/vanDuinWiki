---
id: paper:2017arancibia-venue-jp6b12155
type: paper
title: "Advancements in the Synthesis of Building Block Materials: Experimental Evidence and Modeled Interpretations of the Effect of Na and K on Imogolite Synthesis"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:oxides-ceramics
  - method:reaxff
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:silica-silicate
  - keyword:oxide-surface
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b12155"
year: 2017
authors:
  - "Nicolás Arancibia-Miranda"
  - "Mauricio Escudey"
  - "Ricardo Ramírez"
  - "Rafael I. González"
  - "Adri C. T. van Duin"
  - "Miguel Kiwi"
venue: "J. Phys. Chem. C"
pdf_sha256: "5f6d6c1ac1be6348274f063fb1e8b9b593105a0c17f83e2296ef755cdf73a1b8"
pdf_path: "papers/Arancibia_Miranda_JPCC_Imogolite_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017arancibia-venue-jp6b12155 -->

## Summary

Imogolite is a hollow aluminosilicate nanotube studied as a tunable oxide nanostructure for catalysis, adsorption, and encapsulation; its dimensions and purity depend sensitively on synthesis chemistry. This Journal of Physical Chemistry C article investigates how substituting sodium with potassium during hydrolysis of tetraethyl orthosilicate (TEOS) affects imogolite formation, combining experimental characterization with molecular dynamics and density functional theory models. The abstract reports strong experimental evidence—using Fourier-transform infrared spectroscopy, powder X-ray diffraction, isoelectric point measurements, charge measurements, and high-resolution transmission electron microscopy—that potassium alters nanotube morphology relative to sodium-dominated syntheses. Specifically, potassium is associated with shorter nanotubes, larger diameters, and increased amounts of amorphous material related to allophane even at low potassium concentrations. Adri C. T. van Duin’s co-authorship links the study to atomistic modeling expertise applied to aluminosilicate surface chemistry and nanotube elasticity questions raised in the paper.

## Methods

**Experiment.** Imogolite is grown from **TEOS** hydrolysis under acidic water at **temperature** conditions typical of bench imogolite recipes (often **≤ 95 °C** in the cited literature), swapping **NaOH** for **KOH** to probe **Na/K** effects while holding other recipe elements comparable. Products are characterized by **FT-IR**, **XRD**, **IEP**, **charge measurements**, and **HR-TEM** to capture **nanotube** dimensions, **allophane**-like side phases, and **surface** chemistry trends.

**Atomistic modeling.** The article pairs **MD** and **DFT** with the experiments to interpret **interface** motifs (**silanol** *vs.* **aluminol**) and **elastic** / **structural** responses. **Figure 1** in the PDF illustrates a **DFT** comparison for a **28-atom** imogolite sector when **H** is replaced by **Na** *vs.* **K**, with **periodic** repetition along the tube axis (**L_z** reported in the figure). The short **p1–2** extract does **not** reproduce **LAMMPS** settings, **supercell** sizes for **MD**, **timestep**, **ensemble**, **thermostat/barostat**, **production length**, or full **DFT functional/basis/k-mesh** tables—those protocol lines live in **`papers/Arancibia_Miranda_JPCC_Imogolite_2017.pdf`** and the **SI**.

**Force-field training:** **N/A —** not a **ReaxFF** reparameterization paper; **ReaxFF** appears as an applied **MD** tool alongside **DFT** in the full article.

**Static QM / DFT:** **DFT** is used for **sector** models as previewed by **Figure 1**; **functional**, **basis**, **dispersion**, and **k-sampling** details are **not** in the indexed excerpt—read the **PDF/SI** for the complete **QM** protocol.

**MD application (ReaxFF, excerpt-thin).** The article also reports **ReaxFF** **MD** alongside **DFT** to interpret **interfacial** behavior. **Ensemble** (**NVT**/**NPT**), **timestep**, **thermostat/barostat**, **production duration** (*ps*/*ns*), and **pressure** coupling for those trajectories are **not** reproduced from the **p1–2** excerpt—**N/A —** read **`papers/Arancibia_Miranda_JPCC_Imogolite_2017.pdf`** and **SI** for executable **MD** settings.

## Findings

**K**-containing syntheses yield **shorter**, **wider** nanotubes than **Na**-dominated controls in the abstract’s summary, with more **allophane**-like amorphous material even at **low K** loading—highlighting **alkali sensitivity** for **nanoengineering**. **KOH** substitution shifts both **morphology** and **side-phase** content relative to classic **NaOH** recipes. **DFT/MD** are used to connect **cation identity** to **curvature** and **silanol** *vs.* **aluminol** terminations; tabulated **energies** and **barriers** are **not** in the **p1–2** excerpt—use the **full PDF/SI** and figure panels when quoting **tube lengths**, **diameters**, or **model** numbers.

## Limitations

Full numerical tables for every synthesis batch and all **DFT** convergence settings reside in the **PDF** and **SI** rather than in short extracts. **Force-field** and **DFT** models of complex aqueous aluminosilicate formation are approximate; extrapolation to industrial scale-up requires additional validation.

## Relevance to group

van Duin co-authorship on aluminosilicate nanotube synthesis interpreted with atomistic modeling; connects to oxide and clay-adjacent themes in the wiki.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpcc.6b12155`

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
