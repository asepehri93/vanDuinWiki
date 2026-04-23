---
id: paper:2022luis-e-paniagua-guer-acs-effects-moisture
type: paper
title: "Effects of Moisture and Synthesis-Derived Contaminants on the Mechanical Properties of Graphene Oxide: A Molecular Dynamics Investigation"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:graphene-carbon-nano
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:water-interfaces
  - keyword:lammps
source_refs: []
doi: "10.1021/acsami.2c16161"
year: 2022
authors:
  - "Luis E. Paniagua-Guerra"
  - "Mauricio Terrones"
  - "Bladimir Ramos-Alvarado"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "dd68526c751b880837bbca48d69c7c195d782d34d9db2d327d73a9963325eed2"
pdf_path: "papers/ReaxFF_others/Paniagua_Guerra_GO_water_acsami_2022.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022luis-e-paniagua-guer-acs-effects-moisture -->

## Summary

Paniagua-Guerra, Terrones, and Ramos-Alvarado use **ReaxFF molecular dynamics** in **LAMMPS** to connect **graphene oxide (GO)** **microstructure**—oxygen functionalization, **interlayer water**, and **sulfate** residues from **wet** **synthesis**—to **mechanical** responses in **tension**, **nanoindentation**, and **shear** (*ACS Appl. Mater. Interfaces*, DOI `10.1021/acsami.2c16161`). The study targets a persistent modeling gap: **continuum** **mechanics** of **GO** often omits **explicit** **water** and **ions**, even though **galleries** are **hydrated** and **charged** in practice. By sampling **oxidation** levels, **moisture**, and **sulfate** concentration, the authors test how **defect** loadings in the **basal plane** control **stiffness** and **strength**, while **H-bond** networks can **delay** **fracture** when **strong** **hydrogen bonds** bridge **sheets**.

## Methods

Simulations build **oxidized graphene** **slabs** with variable **oxygen** **group** densities, add **intercalated** **water** at controlled **humidity-like** loadings, and introduce **sulfate** ions at concentrations meant to mimic **residual** **synthesis** **contaminants**. **Mechanical** protocols include **uniaxial tension** to extract **stress–strain** behavior and failure strain, **nanoindentation**-style loading normal to the stack, and **interlayer shear** tests to probe **sliding** resistance. **ReaxFF** enables **bond** **cleavage** and **reformation** in **oxygenated** **carbon** frameworks, which is essential when **sp³** **defects** concentrate **stress**. **Post-processing** typically extracts **Young’s** **modulus**-like **slopes**, **peak** **stress**, and **work**-to-**fracture** metrics from **stress–strain** curves, comparing across **oxidation** and **intercalant** **conditions** at matched **strain** **rates**.

**MD setup (ReaxFF).** **Engine: LAMMPS** `reax/c` **reactive** **molecular dynamics**; **GO** **slab** **supercells** (oxidation, **H₂O**, **sulfate** loadings) with **3D PBC**; **NVT**-class **thermostat**-controlled **mechanical** **deformation** at **temperature 300 K** (or the **T** in the **PDF**). **Timestep (fs)**, **equilibration**/**production** **stages** (ps–ns), and **in-plane**/**out-of-plane** **loading** **boundary** **conditions** are in *ACS Appl. Mater. Interfaces* **Methods**—**N/A** here to list every value from the short **extract**. **Barostat: N/A** for the **uniaxial**/**shear** **tests** as summarized. **Pressure: N/A** as a **thermodynamic** **control** in the mechanical protocol narrative. **Electric field: N/A**. **Replica / enhanced sampling: N/A**.

## Findings

**Mechanical** performance is dominated by **basal-plane** **integrity**: higher **sp³**/**defect** loadings reduce **moduli** and **tensile** **strength** as expected from **oxidative** **damage** to the **graphitic** backbone. **Water** and **H-bond** **percolation** in **galleries** modulate **ductility** and **failure** **timing**, sometimes **stabilizing** **strain** **accommodation** relative to dry models. **Sulfate** produces **nonmonotonic** effects: modest **sulfur** loadings can **improve** **fracture** **resistance** relative to selected references, while higher **sulfate** **levels** **reduce** **stiffness**, **strength**, and **toughness**—mirroring **sensitivity** of **experimental** **GO** **films** to **processing** **salts**. Taken together, the results argue that **multilayer** **GO** **mechanics** is not a single **oxidation** **fraction** problem: **electrolyte** **identity**, **gallery** **spacing**, and **ion** **correlations** must be modeled **explicitly** when comparing to **films** precipitated from **wet** routes. Remaining **limitations** include **high** **strain rates**, finite **slab** sizes, and **ReaxFF** uncertainties for **oxidized** **carbon** chemistry compared to **DFT** at large **strains**. **Experimental** **comparisons** should align **simulation** **oxidation** **fractions** and **interlayer** **spacing** with **XRD**/**TGA**-informed **estimates** where possible, because **GO** **samples** are rarely **single**-**oxidation**-**state** **slabs**. **Interlayer** **shear** outcomes can be **sensitive** to **boundary** **conditions** (**fixed** vs **free** edges), so **reproducibility** **notes** in the primary article deserve **priority** over **wiki** paraphrases when **porting** **protocols**. **Corpus / KB:** full **numerical** **MD** **settings** and **stress**–**strain** **protocols** belong in the **PDF**; this page does not add **mechanisms** beyond those **sources**.

## Relevance to group

**ReaxFF** **mechanics** of **hydrated GO** with **electrolyte-like** intercalants—useful for **carbon oxide** **interfaces**.

## Citations and evidence anchors

- DOI: [10.1021/acsami.2c16161](https://doi.org/10.1021/acsami.2c16161)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
