# Paper wiki slugs that are not “full primary article” entries

**Browse on GitHub:** [https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md)

This list documents `wiki/papers/*.md` notes whose **`pdf_path`** (or ingest state) is **not** the recommended standalone **version-of-record research article** PDF for that DOI/work. Use it when interpreting “thin” pages: some are **intentionally** navigation records for **SI**, **proof/galley duplicates**, or **workflow artifacts**.

Paths are **repo-relative** (PDFs live under `papers/` unless noted). Filenames appear in the second column for quick search.

Maintainers: when the corpus later acquires a clean VOR PDF, update `pdf_path`, `extraction_quality`, and expand the wiki body from the new extract.

## A. Supporting information (SI) packages

These slugs primarily register an **SI PDF**; the narrative article is another file/slug.

| Slug | PDF (`pdf_path`) | Notes |
|------|-------------------|--------|
| `2015kim-venue-paper` | `papers/Yeon_Langmuir_2016_SI.pdf` | Langmuir SI for tribochemistry / silica oxidation |
| `2016yoon-venue-microsoft-word` | `papers/Yoon_ACSNano_SI.pdf` | SI for ion irradiation / graphene defects |
| `2018ho-venue-paper` | `papers/Hahn_NaSiOx_JPCC_2018_SI.pdf` | SI for NaSiOx/water ReaxFF |
| `2019nayir-venue-paper` | `papers/Nayir_JPC_C_SiOx_2019_SI.pdf` | SI for Si/silica defects ReaxFF |
| `2020zhang-venue-si-rev2` | `papers/Zhang_ChemMat_2020_SI.pdf` | Revised SI for graphene-on-SiC growth |
| `2022prenger-venue-paper` | `papers/Prenger_ACS_AEM_2022_SI.pdf` | SI for MXene supercapacitor study |
| `2023roshan-venue-paper` | `papers/Roshan_JPCC_CuSiO_2023_SI.pdf` | SI for Cu/Si/O ReaxFF optimization |
| `2023uene-venue-paper` | `papers/Uene_2024_BN_BCl3_JPC_SI.pdf` | SI tables for BN ALD ReaxFF |
| `2017kumar-venue-paper` | `papers/Kumar_thiol_Pd_Langmuir_2018_SI.pdf` | Langmuir SI for Pd–thiol SAM DFT/ReaxFF; pairs with wiki `2018kumar-langmuir-201-thermodynamics-alkanethiol` |

## B. Publisher workflow / non-article PDFs

| Slug | PDF (`pdf_path`) | Notes |
|------|-------------------|--------|
| `2016page-venue-paper` | `papers/Page proof- TOC.pdf` | ACS **TOC / proof** banner fragment—not an article |
| `2013chapter6-venue-untitled` | `papers/Chapter6_water.pdf` | Book/chapter **placeholder** ingest |
| `2013chapter6-venue-untitled-2` | `papers/Chapter6_water_annotated.pdf` | Duplicate placeholder path |

## C. Ingest without usable article text (operator follow-up)

_(None currently listed; earlier **`2015senftle-venue-paper`** was consolidated into **`2015senftle-venue-cs5b00741`** once extracts landed.)_

## D. Proof / galley / preprint duplicate (full article often exists under another slug)

These corpus PDFs are **proof or galley** variants. The wiki should carry **substantive duplicated summaries** (or pointers) to the **VOR sibling** where one exists.

| Slug | Non-primary PDF (`pdf_path`) | Canonical sibling | VOR / main article PDF (sibling `pdf_path`) |
|------|------------------------------|-------------------|---------------------------------------------|
| `2012jeon-venue-rsc-cp` | `papers/Jeon_PCCP_2012_galley.pdf` | `2012jeon-venue-rsc-cp-2` | `papers/Jeon_PCCP_Iron_Efield_2013.pdf` |
| `2014islam-venue-rsc-cp` | `papers/Islam_PCCP_LiS_proof.pdf` | `2014islam-physical-che-reaxff-molecular` | `papers/Islam_PCCP_LiS_2014.pdf` |
| `2014sen-venue-untitled` | `papers/Sen_Nature_Comm_2014_proof.pdf` | `2014sen-nat-oxidation-assisted-ductility` | `papers/Sen_Nature_Comm_2014.pdf` |
| `2014senftle-venue-research` | `papers/Senftle_PdH_JPCCproof_2014.pdf` | Related Senftle PCCP entries | e.g. `papers/Senftle_PdH_JPCC_2014.pdf` (`2014senftle-venue-jp411015a`) |
| `2014zou-venue-paper` | `papers/Zou_ActaMater_2014_proof.pdf` | `2014zou-acta-materia-molecular-dynamics` | `papers/Zou_ActaMater_2014.pdf` |
| `2015hong-venue-research-2` | `papers/Hong_AlOx_JPCC_2015_proof.pdf` | `2015hong-venue-research` | `papers/Hong_AlOx_JPCA_2015_ASAP.pdf` |
| `2017mao-carbon-121-2-formation-incipient-2` | `papers/QianMao_Carbon_Soot_2017.pdf` | `2017mao-carbon-121-2-formation-incipient` | `papers/Mao_Qian_Carbon_soot_2017.pdf` |
| `2016yoon-venue-research` | `papers/Yoon_ACSNano_galley_proof.pdf` | `2016yoon-venue-nn6b03036` | `papers/Yoon_ACSNano_2016.pdf` |
| `2017liu-venue-proof-2-pdf` | `papers/Liu_ACS_Nano_BN_Nickel_2017_galley.pdf` | `2017liu-venue-research` | `papers/Liu_ACS_Nano_BN_Nickel_2017_ASAP.pdf` |
| `2019kwon-venue-paper` | `papers/Kwon_Fuel_2019_proof.pdf` | `2019kwon-fuel-correct-numerical-simulations` | `papers/Kwon_Fuel_2019_online.pdf` |
| `2021lele-venue-paper` | `papers/Lele_Fuel_2021_galley.pdf` | `2021lele-fuel-297-202-reaxff-molecular` | `papers/Lele_Fuel_2021.pdf` |
| `2021leven-x-recent-advances` | `papers/Leven_JCTC_2021_proof.pdf` | `2021itai-leven-j-chem-theor-recent-advances` | `papers/Leven_JCTC_2021.pdf` |
| `2014ong-venue-research` | `papers/Ong_JPCB_IL_DFT_ReaxFF_2014_proof.pdf` | — | VOR via DOI `10.1021/jp508184f` (J. Phys. Chem. B) |
| `2014ostadhossein-venue-rsc-cp` | `papers/Ostadhossein_PCCP_LiSi_proof.pdf` | `2015ostadhossein-physical-che-stress-effects` | `papers/Ostadhossein_PCCP_LiSi_2014.pdf` |
| `2014parsons-venue-paper-2` | `papers/Parsons_N2_N2_JCP_2014_proof.PDF` | — | Final article DOI `10.1063/1.4903782` |
| `2014paupitz-venue-rsc-cp` | `papers/Paupitz_PCCP_2014_Fullerenes_proof.pdf` | `2014paupitz-physical-che-fullerenes-generated` | `papers/Paupitz_PCCP_2014_Fullerenes.pdf` |
| `2014raju-venue-nl-2013-04533k` | `papers/Raju_NanoLetters_2014_proof.pdf` | `2014raju-venue-nl404533k-2` | alternate PDF for DOI `10.1021/nl404533k` |
| `2014raju-venue-nl404533k-2` | `papers/Raju_Nano_Letters_2014_reduced.pdf` | `2014raju-venue-nl-2013-04533k` | duplicate PDF for DOI `10.1021/nl404533k` |
| `2014reaxff-venue-paper` | `papers/ReaxFF_others/ReaxFF_nanobomb.pdf` | — | Published JPCL DOI `10.1021/acs.jpclett.5b00120` (ingest may be preprint-era) |
| `2014rahnamoun-venue-research` | `papers/Rahnamoun_Kapton_JPCA_2014_proof.pdf` | — | VOR via DOI `10.1021/jp4121029` |
| `2013poovathingal-venue-research` | `papers/Poovathingal_Srinivasan_etal_HOPG_oxidation_JPCA_2013_galley.pdf` | `2013poovathingal-venue-jp3125999` | `papers/Poovathingal_Srinivasan_etal_HOPG_oxidation_JPCA_2013.pdf` |
| `2013raju-venue-research` | `papers/Raju_TiO2_water_JPC_C_2013_galley.pdf` | `2013raju-venue-jp402139h-2` | `papers/Raju_TiO2_water_JPC_C_2013_reduced.pdf` |
| `2013russo-venue-research` | `papers/Russo_DNB_HNO3_JPCA_2013_galley.pdf` | `2013russo-venue-jp403511q` | `papers/Russo_DNB_HNO3_JPCA_2013.pdf` |
| `2017li-venue-cr-2016-00440p` | `papers/ReaxFF_others/Li_Merz_ChemReview_Metal_Ions.pdf` | `2017li-chem-rev-201-cr6b00440` | `papers/ReaxFF_others/Li_Merz_ChemReview_2017_Metal_Ions.pdf` |
| `2018yang-j-phys-chem-enabling-computational-2` | `papers/Yang_ZIF_JPC_B_2018_proof.pdf` | — | Version-of-record via DOI `10.1021/acs.jpcb.8b08094` |
| `2019akbarian-venue-paper` | `papers/Akbarian_Polymer_2019_proof.pdf` | `2019akbarian-polymer-183-atomistic-scale-insights` | Uncorrected proof; prefer VOR PDF when ingested |
| `2019dasgupta-computationa-reaxff-molecular-2` | `papers/Nabankur_2019_CompMatSci_electrolyte_in_press.pdf` | `2019dasgupta-computationa-reaxff-molecular` | Elsevier corrected proof duplicate |
| `2020dasgupta-venue-total-number` | `papers/Dasgupta_JCP_2020_supercritical_electrolyte_galley.pdf` | `2020dasgupta-j-chem-phys-reaxff-molecular` | AIP author proof / query PDF |
| `2020hu-npj-computat-predicting-synthesizable` | `papers/ReaxFF_others/Hu_Unocic_Ganesh_npj_CompMat_2020_galley.pdf` | — | Publisher galley; VOR via DOI `10.1038/s41524-020-0327-4` |
| `2021verma-venue-paper` | `papers/Verma_PCCP_BN_water_2021_galley.pdf` | — | Galley/proof; VOR via DOI `10.1039/d1cp00546d` |
| `2022lee-npj-computat-dynamic-observation` | `papers/ReaxFF_others/Lee_NJP_2022_dendrite.pdf` | `2022lee-npj-computat-dynamic-observation-2` | Same SHA-256 and DOI; alternate `pdf_path` filename |
| `2022lee-npj-computat-dynamic-observation-2` | `papers/ReaxFF_others/Lee_npjCompMat_Li_dendrite.pdf` | `2022lee-npj-computat-dynamic-observation` | Same SHA-256 and DOI; alternate `pdf_path` filename |
| `2013odegard-chemical-phy-predicting-mechanical-2` | `papers/ReaxFF_others/ZZ-J092-2014-Chem_Phys_Lett_Predicting mechanical response of crosslinked epoxy using ReaxFF.pdf` | `2013odegard-chemical-phy-predicting-mechanical` | Second corpus PDF for DOI `10.1016/j.cplett.2013.11.036` |

## E. Legacy manifest slug vs ingested article (PDF is primary; rename only via migration)

Some `paper_id`s still carry an old **Kowalik** / placeholder stem from ingest, while the **`pdf_path`** points at a different published article. The wiki **YAML + body** should follow the **actual PDF**; `normalized/papers/*.json` **bibliography** may still show placeholder strings until re-profiled.

| Slug | PDF (`pdf_path`) | Actual work (for curation) |
|------|------------------|----------------------------|
| `2017kowalik-venue-bez-tytu` | `papers/ReaxFF_others/Saha_Carbon_PAN_2015.pdf` | **Saha et al., *Carbon* 2015** (DOI `10.1016/j.carbon.2015.07.048`); legacy manifest slug—not authored by Kowalik. |
| `2019kowalik-venue-bez-tytu` | `papers/ReaxFF_others/Study of high density polyethylene (HDPE) pyrolysis with reactive molecular dynamics.pdf` | **Liu et al., *Fuel*** HDPE pyrolysis ReaxFF (not authored by Kowalik). |
| `2020kowalik-venue-bez-tytu` | `papers/ReaxFF_others/Gonzalez_Bending energy of 2D materials- graphene, MoS2 and imogolite_PCCP_2018.pdf` | **González et al., *RSC Adv.* 2018** (DOI `10.1039/C7RA10983K`); filename says PCCP but venue is **RSC Advances**. |

## F. Special cases

| Slug | PDF (`pdf_path`) | Notes |
|------|-------------------|--------|
| `2013yang-chemical-phy-self-weakening-lithiated` | `papers/CP_Letter_LiC_galley.pdf` | Local **`normalized/extracts`** is **proof query + highlights only**; the **published article** is a full CPL letter (DOI `10.1016/j.cplett.2013.01.048`). Wiki prose should follow the published work, not only the p1–2 extract. |
| `2013jacobs-venue-rsc-cy` | `papers/Jacobs_CST_2013_proofs.pdf` | Proof query extract—prefer final RSC Advances PDF when ingested |
| `2013vanduin-venue-paper` | `papers/vanDuin_IJEMCP_2013_galley.pdf` | Editorial correspondence—not a research article |

---

**Not listed:** Slugs whose `pdf_path` is a normal journal article PDF but whose wiki was briefly “thin” should receive **expanded summaries** in `wiki/papers/`; they are **not** exempt from full curation.

## Retired slugs (after manifest re-key or duplicate merge)

| Retired slug | Canonical page |
|--------------|----------------|
| `2015senftle-venue-paper` | [`2015senftle-venue-cs5b00741`](../../wiki/papers/2015senftle-venue-cs5b00741.md) |
| `2019shchygol-j-chem-theor-reaxff-parameter` | [`2019ganna-shchygol-j-chem-theor-reaxff-parameter`](../../wiki/papers/2019ganna-shchygol-j-chem-theor-reaxff-parameter.md) |
| `2023krstic-venue-paper` | [`2025krstic-venue-paper`](../../wiki/papers/2025krstic-venue-paper.md) |
