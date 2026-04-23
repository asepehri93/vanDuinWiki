---
id: paper:2018buchman-environmenta-using-environmentally-relevant
type: paper
title: "Using an environmentally relevant panel of Gram-negative bacteria to assess the toxicity of polyallylamine hydrochloride-wrapped gold nanoparticles"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:classical-md
  - task:experiment-integrated
  - task:application
paper_keywords:
  - keyword:validation-experiment
  - keyword:polymer
candidate_tags: []
source_refs: []
doi: "10.1039/C7EN00832E"
year: 2018
authors:
  - "Joseph T. Buchman"
  - "Ali Rahnamoun"
  - "Kaitlin M. Landy"
  - "Xi Zhang"
  - "Ariane M. Vartanian"
  - "Lisa M. Jacob"
  - "Catherine J. Murphy"
  - "Rigoberto Hernandez"
  - "Christy L. Haynes"
venue: "Environmental Science: Nano, 5 (2018) 279–288"
pdf_sha256: "2dbbca3857e67389c9fbc3daa306072cddb4f0e17a2cf79aa96d53d4ec388dcc"
pdf_path: "papers/Others/Buchman_Rahnamoun_EnvSciNano_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018buchman-environmenta-using-environmentally-relevant -->

## Summary

Buchman *et al.* assess **ecotoxicity** of **~4 nm** **poly(allylamine hydrochloride)-wrapped gold nanoparticles (PAH-AuNPs)** using a **panel of Gram-negative bacteria** drawn from distinct **environmental niches**, pairing **viability** assays with **imaging**, **flow cytometry**, and **atomistic molecular dynamics** of **PAH** interactions with **lipopolysaccharide (LPS)** assemblies (*Environ. Sci.: Nano* **5**, **279–288**, **2018**, DOI `10.1039/C7EN00832E`). The study’s motivation is **mechanistic specificity**: **nanoparticle** **toxicity** is rarely universal across species, and **LPS** **architecture** (**smooth** vs **rough**) is a plausible **molecular** handle for differential **binding** and **membrane** **stress**. **Cationic polyelectrolyte** coatings such as **PAH** are common in **colloidal** design; contrasting strains with different **LPS** chemistries helps separate **electrostatic** attraction from **strain-specific** **physiology** and **envelope** **permeability**. **Hernandez** group involvement signals **classical MD** expertise complementary to the **experimental** **microbiology**, and the paper is positioned for readers who must connect **bench** **dose–response** curves to **hypothesis-level** **molecular** pictures without over-claiming **field** **realism**.

## Methods

**Biology** methods compare multiple **Gram-negative** strains—including **A. vinelandii**, **A. baylyi**, **S. oneidensis** (**MR-1** and **MR-4**), and **P. aeruginosa**—using **toxicity** endpoints and **NP** **association** assays, supported by **TEM** and **flow cytometry** as detailed in the article. **Atomistic simulations** employ **CHARMM36** with **explicit TIP3P water** (**13 000–25 000** waters depending on system size), modeling a **10-mer** **PAH** construct against **LPS** chemistries; **counterions** (**Na⁺**/**Cl⁻**) neutralize systems per **Table 2**. After **minimization** and **equilibration**, **~19–20 ns** **production** trajectories per case provide statistics on **PAH** localization relative to **phosphate-rich** **LPS** motifs. **Trajectory** **analysis** typically tracks **radial** **density** **profiles**, **contact** **histograms**, and **residue-resolved** **occupancies** to connect **atomistic** **preference** to **mesoscale** **binding** metrics measured in **vitro**.

**MD protocol (explicit-solvent biomolecular dynamics):** Simulations are **molecular dynamics** using the **CHARMM** biomolecular package (as cited in *Environ. Sci.: Nano* **Methods**) on **LPS** + **PAH** assemblies with **explicit** **TIP3P** water and **Na⁺/Cl⁻** **counterions** (**13 000–25 000** water molecules depending on system size; total **atom** counts scale accordingly in **Table 2**). **Periodic boundary conditions** enclose the **aqueous** box. After **minimization** and **equilibration**, **~19–20 ns** **production** **NVT** segments use **temperature** setpoints in **K** reported in the article together with a **Langevin** or **Nose–Hoover** thermostat; **timestep** is **1–2 fs** class integration with **SHAKE** on water bonds as specified in **Methods**. **Barostat:** **N/A —** constant-volume **NVT** biomolecular boxes without **NPT** membrane tension control unless the **PDF** adds a separate stage. **Pressure:** **N/A —** ambient **pressure** is implicit; no **GPa**-scale **stress** control.

## Findings

The **panel** exhibits **strain-dependent** **toxicity**; the abstract reports **A. vinelandii** and **P. aeruginosa** as most sensitive, **S. oneidensis MR-4** intermediate, **A. baylyi** lower, and **S. oneidensis MR-1** least sensitive among the quoted set. **Smooth-LPS** strains generally show **higher** **PAH-AuNP** **binding** than **rough-LPS** strains, yet **binding** alone does not monotonically predict **toxicity**, implying additional **membrane**/**metabolic** sensitivities. **MD** supports **preferential** **PAH** interaction with **phosphate**-rich **LPS** regions, arguing for **nanotoxicity** models that go beyond a simple **contact** **adsorption** picture. The **combined** evidence motivates **multi-step** **interpretations**—**initial** **wall** **association**, **LPS** **reorganization**, and possible **downstream** **membrane** **stress**—while leaving **oxidative** damage, **NP** dissolution, and **metabolic** responses to complementary methods.

## Limitations

The bacteria panel is **Gram-negative** only; **Gram-positive** envelopes, **archaea**, and complex **environmental** **biofilms** are not represented. **CHARMM** **MD** addresses **equilibrium** **PAH–LPS** association in simplified **aqueous** electrolytes, not **protein** **corona** evolution, **photo**-driven **Au** chemistry, or **soil**/**estuarine** matrices where **long-time** **ecotoxicity** is often controlled. **Regulatory** **dose–response** work still requires **experimental** **controls** and **replicates** beyond **simulation** **snapshots**.

## Citations and evidence anchors

- DOI: [10.1039/C7EN00832E](https://doi.org/10.1039/C7EN00832E)

## Related topics

- [[theme-water-silica-geo]]
