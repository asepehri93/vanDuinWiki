---
id: paper:2025askari-chemical-eng-synergistic-electronic
type: paper
title: "Synergistic electronic interplay between CoFe single atom and nitrogen on 2D carbon boosts bifunctional oxygen redox in metal-air batteries"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:catalysis-surfaces
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:dft-static
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.cej.2025.167663"
year: 2025
authors:
  - "Saeed Askari"
  - "Swarit Dwivedi"
  - "Kang Hui Lim"
  - "Masood S. Alivand"
  - "Parisa Biniaz"
  - "Ali Zavabeti"
  - "Sibudjing Kawi"
  - "Matthew R. Hill"
  - "Adri C. T. van Duin"
  - "Akshat Tanksale"
  - "Mainak Majumder"
  - "Parama Chakraborty Banerjee"
venue: "Chem. Eng. J. 522 (2025) 167663"
pdf_sha256: "424d074d4d63892ad130b68b806f83efb2b50a07a4461c35f1deb7e76c0554f9"
pdf_path: "papers/Askari_CoFe_metalair_batteries_ChemEngJournal_2025.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025askari-chemical-eng-synergistic-electronic -->

## Summary

The work reports a dual-metallic single-atom electrocatalyst (CoFe-2DSA) on two-dimensional nitrogen-doped carbon, made by a molten salt–assisted pyrolysis route from a ZIF-type precursor, and evaluates it as a bifunctional oxygen electrocatalyst for metal–air battery cathodes. Density functional theory is used to relate graphitic versus pyridinic nitrogen motifs near Co–Fe dual-atom sites to charge transfer, intermediate binding, and computed oxygen reduction and evolution energetics, alongside electrochemical and zinc–air cell measurements.

## Methods

- **Synthesis and experiments:** CoFe-2DSA is derived from a 3D ZIF framework converted to a 2D bi-metallic single-atom catalyst on N-doped carbon (details in Supporting Information). Electrocatalytic oxygen reduction (ORR) and oxygen evolution (OER) are characterized, and zinc–air battery tests report power density, specific capacity, energy density, and long-term cycling.
- **Atomistic modeling:** The study uses **density functional theory** to probe ORR/OER mechanisms on model Co–FeN\(_6\) ensembles with different combinations of nearby graphitic and pyridinic nitrogen, including cases with hydroxyl species at the bi-metallic bridge as in prior work. **Nørskov-type thermochemical analysis** (free-energy profiles at 0 V vs RHE, overpotentials from rate-limiting steps) is applied to compare configurations. The main text emphasizes trends in \(\Delta G\) for key steps (e.g., water formation step \(\Delta G_4\)) and assigns rate-limiting steps for different N motifs; **exchange–correlation functional**, **plane-wave/PAW** settings, **k-mesh** density, and **DFT–D3**-style **dispersion** (if any) are specified in the **Supporting Information** rather than duplicated in this note—see SI tables/figures for exact **reaction** **pathways** and **energies**/**barriers** used in the free-energy **property** model.
## Findings

- CoFe-2DSA delivers strong bifunctional performance in the experiments quoted in the article: ORR half-wave potential \(E_{1/2} \approx 0.886\) V vs RHE and OER overpotential \(\eta \approx 290\) mV at 10 mA cm\(^{-2}\), with a small overall ORR/OER voltage gap \(\Delta V \approx 0.634\) V relative to a Pt–Ru benchmark discussed in the paper.
- In zinc–air battery testing, the catalyst is reported to reach about **229.6 mW cm\(^{-2}\)** power density, **811.5 mA h g\(^{-1}\)** specific capacity, and **997 W h kg\(^{-1}\)** energy density, with **multi-week cycling** stability (on the order of **74 days** / thousands of cycles as stated).
- DFT indicates that **graphitic nitrogen** can strengthen metal–oxygenate coupling and improve charge transfer to Co–Fe sites, lowering the thermodynamic overpotential for the water-formation step in some models, whereas **pyridinic nitrogen** introduces sp\(^3\)-like defects that accumulate charge and can weaken metal–oxygenate binding and raise overpotentials. The relative amounts of these motifs shift which step is rate-limiting (e.g., \(\Delta G_4\) vs \(\Delta G_1\) for *OOH-related steps).
## Limitations

- Detailed **exchange–correlation functional, basis set, and electronic-structure code** settings are not fully reproduced in the main text reviewed here; quantitative DFT comparisons should use the **Supporting Information** and original tables.
- Experimental catalyst structures are represented by **idealized cluster models**; real distributions of N types and Co/Fe coordination are more heterogeneous than the few configurations shown.

## Relevance to group

Adri C. T. van Duin is a co-author; the study couples **experimental electrochemistry** with **DFT-based interpretation** of N–metal synergy on carbon for oxygen electrocatalysis.

## Citations and evidence anchors

- DOI: [10.1016/j.cej.2025.167663](https://doi.org/10.1016/j.cej.2025.167663)

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]

## Reader notes (navigation)

- Experimental synthesis and additional computational parameters: **Supporting Information** referenced in the article.
