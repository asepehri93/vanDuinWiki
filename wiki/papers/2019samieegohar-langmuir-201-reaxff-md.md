---
id: paper:2019samieegohar-langmuir-201-reaxff-md
type: paper
title: "ReaxFF MD Simulations of Peptide-Grafted Gold Nanoparticles"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:water-silica-geo
  - method:reaxff
  - task:application
  - material:metal-surface
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:charge-equilibration
  - keyword:nvt-simulation
  - keyword:lammps
source_refs: []
doi: "10.1021/acs.langmuir.8b03951"
year: 2019
authors:
  - "Mohammadreza Samieegohar"
  - "Feng Sha"
  - "Andre Z. Clayborne"
  - "Tao Wei"
venue: "Langmuir (2019), 35, 5029-5036"
pdf_sha256: "d46395939a4703a020d82c9d2e41515cc6653638d7c32005f51545b05b8de00a"
pdf_path: "papers/ReaxFF_others/Samieegohar_Langmuir_Peptide_Gold_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019samieegohar-langmuir-201-reaxff-md -->

## Summary

**ReaxFF molecular dynamics** is used to study **~3 nm** gold nanoparticles grafted with short **cysteine/glycine**-containing peptides in **water**, varying **surface grafting density**. The work emphasizes **facet-dependent adsorption**, **charge polarization** on Au, **electrostatic potential** of the functionalized particle, and **thiol (de)protonation / proton transfer** to water and carboxyl groups. The **Langmuir** abstract motivates **peptide-grafted** **AuNP** systems for **biodetection** and **drug delivery**, noting **surface-enhanced** **Raman** uses and **thiol–gold** functionalization as a standard **bioconjugation** handle; **DFT** literature on **small** **Au** clusters is cited for **electronic** **trends**, while this study targets **explicit-solvent** **ReaxFF** **MD** at **nanoparticle** sizes relevant to **colloidal** experiments.

## Methods

**Models / engine.** **ReaxFF** **molecular** **dynamics** in **LAMMPS** (as standard for the cited **reactive**-**FF** **workflow**; **see** *Langmuir* **+** **SI** for the exact **version** and **neighbors**). **Au** **cores** **~3** **nm** **diameter**; peptide ligands **CGCG** and **CGGG** at **low (~1.46 peptides/nm²)** and **high (~2.24 peptides/nm²)** **grafting** **densities**; **solvation** in **cubic** **~8.7**–**8.9** **nm**-**side** **cells** with **3D** **PBC** (**N**-**k**-**class** **atom** **counts** as in **the** **paper**).

**ReaxFF MD.** Initial relaxation in vacuum (**100 ps at 5 K**), then heating to **289.15 K**; **Berendsen** thermostat (**damping 100 fs**); **NVT**; **time step 0.1 fs**; **QEq** charge updates every **10 MD steps**; bond-order and nonbonded cutoffs **0.3 Å** and **10 Å** (hydrogen-bond and neighbor criteria as stated in the article). **Coarse-grained MARTINI** simulations are reported for comparison on the same systems.

**Analysis.** Gyration radius, **normalized facet coverage**, electrostatic potential from Au charges, and reaction chemistry from trajectories.

**Engine / other MD.** **ReaxFF** block above follows the **Langmuir** **protocol**; **MARTINI** **coarse**-**grained** **runs** for **comparison** use the **companion** **setup** in the **article**. **Barostat / NPT:** **N/A** for the **NVT** **stated** **protocol**; **uniaxial** **stress** / **constant**-**p** **segments** are **N/A** unless the **SI** **adds** them. **External** **E**-**field, shear, shock, umbrella** **sampling:** **N/A** for the **stated** **peptide**-**Au** **adsorption** **study**.
## Findings

Peptide adsorption shows **slight facet dependence**, with **Au(111)** favored versus **Au(100)** and **Au(110)**. **Thiol–Au** binding plus **O/N–Au** interactions polarize the surface (**net positive** on exterior Au, **negative** core in charge histograms); the **outer peptide layer** yields **overall negative** electrostatic potential. Simulations report **thiol deprotonation** and **proton transfer** to **water** and **carboxyl** groups. **MARTINI** comparisons show **similar gyration radii**, supporting that short peptides are relaxed within the ReaxFF runs. **Charge histograms** in the article illustrate **facet-dependent** **Au** **oxidation-state**-like patterns as **peptide** **coverage** changes, helping explain **colloidal** **stability** trends tied to **zeta**-potential sign.

## Limitations

Peptide lengths and simulation times are **finite**; the authors note **ReaxPQ+** as a future improvement for **aqueous polarization** accuracy.

**Ion** **strength**, **pH**, and **competitive** **adsorbates** in **serum**-like media are not exhaustively sampled in the **Langmuir** **protocol** excerpted here; extend cautiously to **in vivo** **delivery** **claims** without **orthogonal** **experiments**.

**Peptide** **sequence** **isomers** beyond **CGCG/CGGG** may shift **facet** **preferences** and **charge** **patterns**; repeat **sampling** when **ligand** **libraries** expand.

## Relevance to group

Application of **ReaxFF** to **biomolecular–Au** interfaces in explicit **water**, relevant to **reactive FF** validation for **nanoparticle–ligand** chemistry.

## Citations and evidence anchors

DOI: [10.1021/acs.langmuir.8b03951](https://doi.org/10.1021/acs.langmuir.8b03951)

## Related topics

- [[reaxff-family]]
