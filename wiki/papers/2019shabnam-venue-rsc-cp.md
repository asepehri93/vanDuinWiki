---
id: paper:2019shabnam-venue-rsc-cp
type: paper
title: "Evaluation of the effect of nickel clusters on the formation of incipient soot particles from PAHs (RSC proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:nvt-simulation
source_refs: []
doi: "10.1039/C9CP00354A"
year: 2019
authors:
  - "Sharmin Shabnam"
  - "Qian Mao"
  - "Adri C. T. van Duin"
  - "K. H. Luo"
venue: "Phys. Chem. Chem. Phys. (author proof)"
pdf_sha256: "7d359b68327338701d7d61f80fbdca849949433e14bb6ffd9ec6f8594b0c1a0e"
pdf_path: "papers/Shabnam_PCCP_Ni_soot_2019_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019shabnam-venue-rsc-cp -->

??? info "PDF variant"
    Author **proof** PDF (`c9cp00354a`). The local extract is dominated by RSC proofing instructions. Scientific prose and stable pagination are on [[2019shabnam-physical-che-evaluation-effect]] with the issue PDF.

## Summary

The corpus file `papers/Shabnam_PCCP_Ni_soot_2019_galley.pdf` is the Royal Society of Chemistry **author proof** for Phys. Chem. Chem. Phys. article DOI `10.1039/C9CP00354A`. The first pages of the automated extract (`normalized/extracts/2019shabnam-venue-rsc-cp_p1-2.txt`) reproduce RSC proofing instructions, a funding table, and researcher identifiers rather than the continuous article body. Within that proof package, the **graphical abstract** block nevertheless states the study title as “Evaluation of the effect of nickel clusters on the formation of incipient soot from polycyclic aromatic hydrocarbons via ReaxFF molecular dynamics simulations” and lists authors Sharmin Shabnam, Qian Mao, Adri C. T. van Duin, and K. H. Luo, with a one-line caption describing the effect of nickel clusters on incipient soot from PAH precursors via ReaxFF-MD. The peer-reviewed article (read from the version-of-record PDF on [[2019shabnam-physical-che-evaluation-effect]]) uses ReaxFF molecular dynamics in the NVT ensemble to study how a Ni₁₃ cluster influences incipient soot formation from polycyclic aromatic hydrocarbon monomers ranging from naphthalene to circumcoronene over 400–2500 K. That sibling page summarizes that at low temperature PAHs stack and bind around nickel, forming larger clusters earlier than in homogeneous systems; that between roughly 1200 K and 1600 K chemisorption on nickel becomes important for incipient soot; that near 2000 K “chemical nucleation” produces soot-like growth facilitated by nickel-assisted dehydrogenation; and that at 2500 K nickel accelerates ring opening and fullerene-like soot growth relative to nickel-free simulations.

## Methods

**1 — MD (ReaxFF, as in the VOR).** The science **protocol** is the same as on **`[[2019shabnam-physical-che-evaluation-effect]]`**: **reactive** **MD** in the **NVT** **ensemble** with one **Ni₁₃** and one **PAH** ( **naphthalene** to **circumcoronene** ) per **cell**, **temperatures** from **~400** to **~2500** **K**; **3D** **PBC**; **Reaxff**-level **C/H** and **Ni**-containing **chemistry**; **analysis** of **clustering**, **chemisorption**, **D/H** **chemistry**, and **graphitization** toward **fullerene**-like **motifs** as in **PCCP**. **Timestep**, **thermostat**, and **trajectory** **lengths** must be read from the **version-of-record** **PDF**—**N/A** to re-key them from this **galley** (the **automation** **extract** is **mostly** RSC **proofing** text). **Barostat**; **E**-**field**; **shear**; **shock**; **umbrella** or **replica** **sampling: N/A** in the main **NVT** **description** of this work if the **VOR** does not add them.

**2 — Force-field training.** **N/A** ( **cited** **Reaxff** for **C/H** /**Ni**; **not** a **de** **novo** **fit** paper).

**3 — DFT** as **stand-alone** **outcome** **N/A.**

**VOR** **MD** (not the galley): **LAMMPS** **molecular** **dynamics** with **>1000** **atoms** per **supercell**; **0.1**–**0.5** **fs** **timestep**; **Nose**–**Hoover** **thermostat**; **NVT** with **3D** **PBC**; **~ns**-class **production** in *Phys. Chem. Chem. Phys.* **Methods**; **NPT** **Parrinello**–**Rahman** **barostat** and **hydrostatic** **pressure** in **bar** are **N/A** for the main **NVT** **RMD** path **unless** the **VOR** **/ ** **SI** **adds** a **NPT** **block**. **External** **E**-**field**, **shear**, **umbrella**: **N/A** in the main **NVT** **description** on **`[[2019shabnam-physical-che-evaluation-effect]]`**.
## Findings

The qualitative temperature ladder and nickel-assisted pathway distinctions summarized on [[2019shabnam-physical-che-evaluation-effect]] are grounded in the PCCP article text; this galley slug does not duplicate quantitative cluster-size statistics or figure references. The published article frames nickel-assisted growth as accelerating early clustering relative to homogeneous PAH systems, then distinguishes regimes where chemisorption on nickel becomes important, where “chemical nucleation” produces soot-like growth with nickel-assisted dehydrogenation, and where ring-opening toward fullerene-like soot is accelerated relative to nickel-free trajectories. Interpreting those stages requires the full PCCP text and figures on the version-of-record PDF because the galley extract here is dominated by RSC proofing correspondence (for example, instructions to return corrections within 48 hours to pccp@rsc.org and checks on tables, equations, and references) rather than the scientific sections. Operators should treat this slug as a **manifest-aligned proof** duplicate: evidence for combustion and soot chemistry claims should be cited from the issue PDF path on the sibling page, not from workflow text in `normalized/extracts` for this stem.

## Limitations

Proof PDFs may differ in figure quality and line breaks from the issue PDF. For citations and locators, use the final article.

## Relevance to group

Combustion and soot chemistry with metal nanoparticles, co-authored by van Duin (Penn State).

## Reader notes (navigation)

- [[2019shabnam-physical-che-evaluation-effect]]
- [[theme-pyrolysis-combustion-organics]]
- [[reaxff-family]]
