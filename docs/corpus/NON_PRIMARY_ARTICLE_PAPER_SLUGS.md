# Paper wiki slugs that are not “full primary article” entries

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

## B. Publisher workflow / non-article PDFs

| Slug | PDF (`pdf_path`) | Notes |
|------|-------------------|--------|
| `2016page-venue-paper` | `papers/Page proof- TOC.pdf` | ACS **TOC / proof** banner fragment—not an article |
| `2013chapter6-venue-untitled` | `papers/Chapter6_water.pdf` | Book/chapter **placeholder** ingest |
| `2013chapter6-venue-untitled-2` | `papers/Chapter6_water_annotated.pdf` | Duplicate placeholder path |

## C. Ingest without usable article text (operator follow-up)

| Slug | PDF (`pdf_path`) | Notes |
|------|-------------------|--------|
| `2015senftle-venue-paper` | `papers/Senftle_ACS Catalysis_2015.pdf` | PDF registered; **normalized extract empty / poor**—curate from PDF when possible |

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
| `2019kwon-venue-paper` | `papers/Kwon_Fuel_2019_proof.pdf` | `2019kwon-fuel-correct-numerical-simulations` | `papers/Kwon_Fuel_2019_online.pdf` |
| `2021lele-venue-paper` | `papers/Lele_Fuel_2021_galley.pdf` | `2021lele-fuel-297-202-reaxff-molecular` | `papers/Lele_Fuel_2021.pdf` |
| `2021leven-x-recent-advances` | `papers/Leven_JCTC_2021_proof.pdf` | `2021itai-leven-j-chem-theor-recent-advances` | `papers/Leven_JCTC_2021.pdf` |

## E. Special cases

| Slug | PDF (`pdf_path`) | Notes |
|------|-------------------|--------|
| `2013yang-chemical-phy-self-weakening-lithiated` | `papers/CP_Letter_LiC_galley.pdf` | Local **`normalized/extracts`** is **proof query + highlights only**; the **published article** is a full CPL letter (DOI `10.1016/j.cplett.2013.01.048`). Wiki prose should follow the published work, not only the p1–2 extract. |
| `2013jacobs-venue-rsc-cy` | `papers/Jacobs_CST_2013_proofs.pdf` | Proof query extract—prefer final RSC Advances PDF when ingested |
| `2013vanduin-venue-paper` | `papers/vanDuin_IJEMCP_2013_galley.pdf` | Editorial correspondence—not a research article |

---

**Not listed:** Slugs whose `pdf_path` is a normal journal article PDF but whose wiki was briefly “thin” should receive **expanded summaries** in `wiki/papers/`; they are **not** exempt from full curation.
