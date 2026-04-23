---
id: paper:2021qiang-liu-acs-gamma-radiation
type: paper
title: "Gamma Radiation Chemistry of Polydimethylsiloxane Foam in Radiation-Thermal Environments: Experiments and Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - material:polymer-organic
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.1c10765"
year: 2021
authors:
  - "Qiang Liu"
  - "Wei Huang"
  - "Bo Liu"
  - "Pu-Cheng Wang"
  - "Hong-Bing Chen"
venue: "ACS Appl. Mater. Interfaces 2021, 13, 41287–41302"
pdf_sha256: "0fe019e9a57ca23d33bb9746ad481c06bdac51e05eb94aee832c434a3cc15ebc"
pdf_path: "papers/ReaxFF_others/liu-et-al-2021-gamma-radiation-chemistry-of-polydimethylsiloxane-foam-in-radiation-thermal-environments-experiments-and-1.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021qiang-liu-acs-gamma-radiation -->


!!! abstract "Scope"
    Combined **γ radiolysis experiments** (0.2 Gy/s, 20–70 °C) and **ReaxFF MD** plus **M06-2X/6-311G(d,p)** thermochemistry for PDMS foam with silica filler—radical-driven gas release and cross-linking.

## Summary

The study examines how temperature modulates γ-radiolysis of polydimethylsiloxane (PDMS) foam in radiation–thermal environments, measuring gas products, paramagnetic species in silica, and cross-linking density. Reactive molecular dynamics with a ReaxFF description reproduces dominant gas evolution and cross-linking trends inferred from experiment and provides atomistic views of interactions among PDMS chains, gas species, radicals, and silica fillers. Complementary quantum calculations at the M06-2X/6-311G(d,p) level characterize barrierless radical coupling (exothermic by 321–618 kJ/mol as reported) and higher-barrier channels (37–229 kJ/mol barriers), underscoring the role of radiation-generated radicals in subsequent chemistry.

## Methods

**1 — MD application (ReaxFF).** Reactive **molecular dynamics** is run in **LAMMPS** with the **Si/C/H/O** ReaxFF description and charge equilibration cited in the article for **PDMS** foam with **silica** filler, using **periodic** (**PBC**) cells large enough to treat the foam composite; atom counts, stoichiometry, and supercell shape are given in the published **Methods** (the short repository extract does not copy every table). The protocol specifies **NVT** control with a **thermostat** (type and damping in the article), a **timestep** in **fs** suitable for ReaxFF, and equilibration plus **production** segments whose lengths are quoted in **ps**/**ns** there. **Barostat / pressure:** **N/A —** not used for the summarized constant-volume ReaxFF runs; **N/A — electric field** in production MD. **N/A — umbrella** sampling, **metadynamics**, and related **rare event** / **replica** schemes are not part of the reported radiolysis MD. ReaxFF **Coulomb** and **QEq** update choices (cutoffs, charge model) are as stated in the primary text and **SI**.

**2 — Force-field training.** **N/A —** this is an application of an existing ReaxFF parameter file to PDMS/silica radiolysis, not a new ReaxFF fit in the sense of a fresh optimization study.

**3 — Static QM.** **M06-2X/6-311G(d,p)** in **Gaussian** (or the program named in the paper) is used for radical **reaction** thermochemistry: barrierless couplings with reported exothermicities **321–618 kJ mol⁻¹** and activated routes with **37–229 kJ mol⁻¹** barriers (abstract-level summary; full set in the paper).

**4 — Experiments.** **γ** irradiation at **0.2 Gy s⁻¹** with **temperature** **20–70 °C**; analysis of gaseous products, **paramagnetic** species in **silica**, and **cross-linking** density as in the **Experimental** section.
## Findings

- Temperature exerts non-monotonic effects on gas formation, radical signatures, and cross-linking, interpreted through competing reaction channels in the proposed mechanism.
- ReaxFF MD reproduces primary gas products and dominant cross-linking phenomenology relative to the experimental observations summarized in the paper.
- Radical coupling and related channels are thermochemically favorable in the barrierless cases computed; higher-barrier routes span 37–229 kJ/mol in the authors’ M06-2X data.
- Radiation-induced radicals are identified as central to gas evolution and network formation in both experiment and simulation.
- The composite **PDMS + silica filler** setting is used to connect **interface chemistry** (radical signatures associated with silica) to **bulk foam** response, so the paper’s value for the KB is both **radiation aging phenomenology** and an example of **ReaxFF** used where **polymer degradation** and **inorganic filler** feedback coexist.

**Comparisons.** ReaxFF **molecular dynamics** **reproduces** the primary **gas** products and **cross-linking** phenomenology **versus** the **experimental** trends discussed; quantum barriers are **compared** within the M06-2X model only.

**Sensitivity.** **Temperature** in the **20–70 °C** window modulates **gas** formation, radical signatures, and **cross-linking** in a **non-monotonic** way tied to competing channels in the proposed **mechanism**.

**Limitations (as framed).** Scope is tied to the reported dose rate, foam formulation, and temperature window; broader radiation fields or matrices are not established here. **Corpus / KB:** numerical MD controls and any **SI** tables should be read from the **version-of-record** **PDF**—not only the short local **extract**.

## Limitations

Modeling is tied to the foam formulation, dose rate, and temperature window studied; scaling to other fillers or atmospheres is not established here. Gamma dose rate and thermal history are specific to the reported protocol; extending conclusions to mixed radiation fields or different polymer matrices requires additional evidence.

## Relevance to group

Demonstrates ReaxFF for radiation–polymer composite aging alongside targeted quantum benchmarks.

## Citations and evidence anchors

- DOI: [10.1021/acsami.1c10765](https://doi.org/10.1021/acsami.1c10765)

## Related topics

- [[reaxff-family]]
