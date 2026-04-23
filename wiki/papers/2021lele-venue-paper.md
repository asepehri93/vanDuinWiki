---
id: paper:2021lele-venue-paper
type: paper
title: "ReaxFF molecular dynamics study on pyrolysis of bicyclic compounds for aviation fuel (pre-publication PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2021.120724"
year: 2021
authors:
  - "Aditya Lele"
  - "Hyunguk Kwon"
  - "Karthik Ganeshan"
  - "Yuan Xuan"
  - "Adri C. T. van Duin"
venue: "Fuel (pre-publication / placeholder volume PDF in corpus)"
pdf_sha256: "2cf05e3467b965c4d5b91f199c2c3c133ea260cc806afa792d51c9a1e4bc1ded"
pdf_path: "papers/Lele_Fuel_2021_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2021lele-venue-paper -->

## Summary

Aviation fuels must satisfy many engineering constraints (density, volatility, emissions), and there is sustained interest in **high energy density** polycyclic candidates that can be sourced or upgraded from renewable feedstocks. This **Fuel** article uses **ReaxFF molecular dynamics** to study **initial pyrolysis** of **bicyclic** hydrocarbons proposed as **jet fuel** alternatives, grouped by whether rings are linked through a **four-membered ring** or a **single C–C bond**. The authors extract **global Arrhenius** parameters (activation energies and pre-exponential factors) to summarize apparent decomposition kinetics and compare rates against **JP-10** and related references discussed in the paper. Mechanistically, the abstract emphasizes two broad reaction classes: **cleavage of the central linkage** to form **cyclic radicals** versus **ring opening** to small **alkenes**, with the relative importance of these channels shifting strongly with **temperature**. The scientific claim is methodological as well as chemical: **ReaxFF** can help discover **reaction networks** relevant to kinetic model building **without** imposing a fully prespecified mechanism. **Corpus note:** this slug registers the **galley** PDF; the same DOI is curated from the **version-of-record** PDF on **[[2021lele-fuel-297-202-reaxff-molecular]]**. This galley ingest is listed in the maintainer catalog of non-primary article PDFs: [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Methods

### 1 — MD application (atomistic dynamics)

Same peer-reviewed study as [[2021lele-fuel-297-202-reaxff-molecular]]: LAMMPS/ReaxAMS-style CHO-2016 ReaxFF; **NVT**; **0.1 fs** production; **40** molecules at **0.2 kg dm\(^{-3}\)** in a **3D periodic** supercell (order **1500** **atoms** total in the equilibrated cell per the VOR article—confirm exact count in the PDF); equilibration **1500 K** with **Berendsen** (100 fs damping); production **1500–3000 K**; **CVHD** at **1500 K**; **10** seeds per **T**; **E-field** **N/A**; **hyperdynamics** as **CVHD** where applied. **Barostat / pressure:** **N/A** — no **NPT**; **N/A** — **hydrostatic** **pressure** not held (constant-volume **NVT**; initial gas-like pressure from density as in the VOR). For **citation**-stable **locators**, use **[[2021lele-fuel-297-202-reaxff-molecular]]**—this **galley** `pdf_path` is **non**-**primary** per maintainer list.

### 2 — Force-field training

N/A — application of published CHO-2016; see VOR page.

### 3 — Static QM (B3LYP BDE in Jaguar)

As on the VOR page (Section 3, Table 1); not re-summarized from the galley.

### 4 — Review

N/A.

## Findings

The paper reports that the bicyclic fuels exhibit **decomposition rates** that are **competitive with or faster than** **JP-10** on the metrics quoted in their Arrhenius analysis. **Temperature** strongly controls which of the two major reaction classes dominates: central-bond scission toward **cyclic fragments** competes with **ring-opening** channels producing **small alkenes**, and the balance is **nonstatic** across the temperature window explored. The authors argue that this temperature-sensitive branching matters for integrating these molecules into **kinetic models** of pyrolysis and combustion, and that **ReaxFF** can supply **data-driven** networks to support such modeling when detailed mechanisms are unknown. For any quantitative comparison (barriers, product lists, species timelines), use **[[2021lele-fuel-297-202-reaxff-molecular]]** and the publisher PDF. The article also frames **endothermicity** of early steps as a practical figure of merit for **fuel cooling** scenarios, connecting decomposition chemistry to engine thermal-management narratives discussed in the introduction. **Corpus / KB honesty:** quantitative kinetics, barriers, and Arrhenius tables: **[[2021lele-fuel-297-202-reaxff-molecular]]** and DOI-resolved *Fuel* PDF, not this galley path alone.

## Limitations

Galley headers can show **placeholder** volume or page metadata. **ReaxFF** omits explicit **quantum nuclear** effects; absolute barriers should be cross-checked when used for quantitative engineering predictions.

## Relevance to group

Duplicate **galley** ingest alongside the **final Fuel** PDF; **van Duin**-group **aviation fuel** pyrolysis line.

## Citations and evidence anchors

Canonical article: **[[2021lele-fuel-297-202-reaxff-molecular]]**. https://doi.org/10.1016/j.fuel.2021.120724

## Related topics

- [[2021lele-fuel-297-202-reaxff-molecular]]
- [[reaxff-family]]
