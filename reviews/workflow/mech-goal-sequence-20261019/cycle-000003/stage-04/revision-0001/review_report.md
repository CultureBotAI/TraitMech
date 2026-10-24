# TraitMech Cycle 3 Stage 4 (`record_review`) — Frozen-Inventory Record and Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `3`, Stage `4` (`record_review`), Revision `1`
- **Repository**: `CultureBotAI/TraitMech`
- **Frozen Inventory Git SHA**: `8ee71cf99e270d60a2e08b550728f0cabdd6ce96`
- **Native Structured Review ID**: `20261023T235000Z-cycle3-stage4-corpus-record-and-cohort-review` (`reviews/structured/20261023T235000Z-cycle3-stage4-corpus-record-and-cohort-review/review.yaml`)
- **Skills Executed**: `.claude/skills/review-yaml-record/SKILL.md`, `.claude/skills/review-yaml-category/SKILL.md`
- **Generated At**: `2026-10-23T23:50:00Z`

## 1. Executive Summary & Coverage Accounting

All **1,130** `TraitRecord` YAML files in `data/traits/` were inventoried at frozen commit `8ee71cf99e270d60a2e08b550728f0cabdd6ce96`:
- **Eligible & Reviewed Records**: **1,129 / 1,129** (`100.0%` coverage across all 10 category cohorts: `395` eligible `METPO:` records and `734` eligible `traitmech:NNNNNN` records)
- **Excluded Records**: **1** (`data/traits/physiology/spore_germination.yaml`, `traitmech:000083`, protected by `DO_NOT_WORK.md` `#291`; `735` total `traitmech:NNNNNN` records including excluded `traitmech:000083`)
- **Updated Records in Stage 4**: **0** (Stage 4 is a read-only corpus review; all 17 open findings are preserved for Cycle 3 Stage 5 `resolve_review_findings`)
- **Source-Limited Records**: **366** (eligible mechanistic-domain records lacking multi-step molecular pathways in currently cited open abstracts; reduced from `369` in Cycle 2 after `+3` Cycle 3 Stage 2 graphs: `coagulase_positive.yaml`, `indole_test_positive.yaml`, `pyrazinamidase_activity.yaml`)
- **Non-Mechanistic Vocabulary Records**: **22** (`upper`: 8, `observation`: 1, `quantitative_property`: 7, `morphology` supporting vocabulary: 6)

### Category Cohort Breakdown

| Category Cohort | Total Files | Eligible & Reviewed | Excluded (`DO_NOT_WORK.md`) | With `causal_graphs` | With `canonical_examples` | Open Findings | Boundary Decision |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| `ecology` | 40 | 40 | 0 | 28 | 30 | 1 | `keep` |
| `environment` | 122 | 122 | 0 | 122 | 119 | 0 | `keep` |
| `genomics` | 387 | 387 | 0 | 372 | 102 | 0 | `keep` |
| `metabolism` | 180 | 180 | 0 | 58 | 66 | 10 | `keep` |
| `morphology` | 129 | 129 | 0 | 95 | 124 | 4 | `keep` |
| `observation` | 20 | 20 | 0 | 0 | 0 | 0 | `keep` |
| `other` | 32 | 32 | 0 | 2 | 12 | 0 | `keep` |
| `physiology` | 205 | 204 | 1 | 59 | 125 | 2 | `keep` |
| `quantitative_property` | 7 | 7 | 0 | 0 | 0 | 0 | `keep` |
| `upper` | 8 | 8 | 0 | 5 | 0 | 0 | `keep` |
| **Total** | **1,130** | **1,129** | **1** | **741** (eligible) | **578** (eligible) | **17** | **All 10 cohorts kept** |

## 2. Open Findings Preserved for Cycle 3 Stage 5 (`resolve_review_findings`)

Seventeen concrete, source-backed `minor` findings (`status: open`, `F-C3S4-DEF-SRC-001`..`017`) were identified across the `ecology` (`1`), `metabolism` (`10`), `morphology` (`4`), and `physiology` (`2`) cohorts where a record either omits its primary `definition_source` from record-level `evidence[]` (`1` record) or cites it in record-level `evidence` with `notes:` only and no verbatim `snippet` (`16` records), even though a verified verbatim quote from that exact `definition_source` already exists on the record's own `causal_graphs` or on a parent/sibling `TraitRecord`:

1. **`F-C3S4-DEF-SRC-001`** (`data/traits/physiology/photoorganoheterotrophic.yaml`, `METPO:1000659`):
   - **Defect (`MISSING_DEFINITION_SOURCE_EVIDENCE`)**: Declares `definition_source: DOI:10.1016/B978-012373944-5.00083-3` and omits `DOI:10.1016/B978-012373944-5.00083-3` from record-level `evidence[]`, despite `causal_graphs[0].edges[0].evidence[0] on the same record (photoorganoheterotrophic_trait -> light)` already carrying the verified verbatim quote `"use of light"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-001`)**: Populate verified verbatim quote for `DOI:10.1016/B978-012373944-5.00083-3` in `data/traits/physiology/photoorganoheterotrophic.yaml`, append a `CURATE` event, and regenerate trait pages.
2. **`F-C3S4-DEF-SRC-002`** (`data/traits/physiology/oxidase_activity.yaml`, `traitmech:000076`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.3390/microorganisms10050926` and cites `DOI:10.3390/microorganisms10050926` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[9].evidence[0] on the same record (family_a_cytochrome_c_oxidase -> cytochrome_c_oxidase)` already carrying the verified verbatim quote `"Cytochrome c oxidases of the heme–copper oxygen reductase family A"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-002`)**: Populate verified verbatim quote for `DOI:10.3390/microorganisms10050926` in `data/traits/physiology/oxidase_activity.yaml`, append a `CURATE` event, and regenerate trait pages.
3. **`F-C3S4-DEF-SRC-003`** (`data/traits/morphology/peritrichous.yaml`, `traitmech:000060`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1093/femsre/fuv034` and cites `DOI:10.1093/femsre/fuv034` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[2].evidence[0] on the same record (surface_placement -> flagellar_filament_number)` already carrying the verified verbatim quote `"five to six flagellar filaments distributed over the cell body"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-003`)**: Populate verified verbatim quote for `DOI:10.1093/femsre/fuv034` in `data/traits/morphology/peritrichous.yaml`, append a `CURATE` event, and regenerate trait pages.
4. **`F-C3S4-DEF-SRC-004`** (`data/traits/metabolism/proteorhodopsin_phototrophy.yaml`, `traitmech:000036`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1126/science.289.5486.1902` and cites `DOI:10.1126/science.289.5486.1902` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[0].evidence[0] on the same record (proteorhodopsin -> proteorhodopsin_trait)` already carrying the verified verbatim quote `"bound retinal to form an active, light-driven proton pump"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-004`)**: Populate verified verbatim quote for `DOI:10.1126/science.289.5486.1902` in `data/traits/metabolism/proteorhodopsin_phototrophy.yaml`, append a `CURATE` event, and regenerate trait pages.
5. **`F-C3S4-DEF-SRC-005`** (`data/traits/metabolism/starch_degradation.yaml`, `traitmech:000115`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1016/S0168-1656(01)00407-2` and cites `DOI:10.1016/S0168-1656(01)00407-2` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[0].evidence[0] on the same record (amylase -> starch_degradation_trait)` already carrying the verified verbatim quote `"the use of starch-converting enzymes in the production of maltodextrin, modified starches, or glucose and fructose syrups"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-005`)**: Populate verified verbatim quote for `DOI:10.1016/S0168-1656(01)00407-2` in `data/traits/metabolism/starch_degradation.yaml`, append a `CURATE` event, and regenerate trait pages.
6. **`F-C3S4-DEF-SRC-006`** (`data/traits/metabolism/three_hydroxypropionate_bicycle.yaml`, `traitmech:000023`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1128/AEM.02473-10` and cites `DOI:10.1128/AEM.02473-10` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[9].evidence[0] on the same record (acetyl_coa_carboxylase -> three_hp_bicycle_trait)` already carrying the verified verbatim quote `"The 3-hydroxypropionate (Fuchs-Holo) bi-cycle. Enzymes: 1, acetyl-CoA carboxylase"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-006`)**: Populate verified verbatim quote for `DOI:10.1128/AEM.02473-10` in `data/traits/metabolism/three_hydroxypropionate_bicycle.yaml`, append a `CURATE` event, and regenerate trait pages.
7. **`F-C3S4-DEF-SRC-007`** (`data/traits/metabolism/ethanol_fermentation.yaml`, `traitmech:000028`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.3389/fmicb.2021.703525` and cites `DOI:10.3389/fmicb.2021.703525` in record-level `evidence[1]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[0].evidence[0] on the same record (ethanol_fermentation_trait -> fermentation_process)` already carrying the verified verbatim quote `"fermentation is defined as an anaerobic bacterial redox process of an organic substrate leading to different products"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-007`)**: Populate verified verbatim quote for `DOI:10.3389/fmicb.2021.703525` in `data/traits/metabolism/ethanol_fermentation.yaml`, append a `CURATE` event, and regenerate trait pages.
8. **`F-C3S4-DEF-SRC-008`** (`data/traits/metabolism/lactic_acid_fermentation.yaml`, `traitmech:000026`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.3389/fmicb.2021.703525` and cites `DOI:10.3389/fmicb.2021.703525` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[0].evidence[0] on the same record (lactic_acid_fermentation_trait -> fermentation_process)` already carrying the verified verbatim quote `"fermentation is defined as an anaerobic bacterial redox process of an organic substrate leading to different products"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-008`)**: Populate verified verbatim quote for `DOI:10.3389/fmicb.2021.703525` in `data/traits/metabolism/lactic_acid_fermentation.yaml`, append a `CURATE` event, and regenerate trait pages.
9. **`F-C3S4-DEF-SRC-009`** (`data/traits/metabolism/mixed_acid_fermentation.yaml`, `traitmech:000027`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.3389/fmicb.2021.703525` and cites `DOI:10.3389/fmicb.2021.703525` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `sibling data/traits/metabolism/ethanol_fermentation.yaml and lactic_acid_fermentation.yaml causal_graphs[0].edges[0].evidence[0]` already carrying the verified verbatim quote `"fermentation is defined as an anaerobic bacterial redox process of an organic substrate leading to different products"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-009`)**: Populate verified verbatim quote for `DOI:10.3389/fmicb.2021.703525` in `data/traits/metabolism/mixed_acid_fermentation.yaml`, append a `CURATE` event, and regenerate trait pages.
10. **`F-C3S4-DEF-SRC-010`** (`data/traits/metabolism/fermentative_hydrogen_production.yaml`, `traitmech:000109`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.3389/fmicb.2021.703525` and cites `DOI:10.3389/fmicb.2021.703525` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `sibling data/traits/metabolism/ethanol_fermentation.yaml and lactic_acid_fermentation.yaml causal_graphs[0].edges[0].evidence[0]` already carrying the verified verbatim quote `"fermentation is defined as an anaerobic bacterial redox process of an organic substrate leading to different products"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-010`)**: Populate verified verbatim quote for `DOI:10.3389/fmicb.2021.703525` in `data/traits/metabolism/fermentative_hydrogen_production.yaml`, append a `CURATE` event, and regenerate trait pages.
11. **`F-C3S4-DEF-SRC-011`** (`data/traits/metabolism/calvin_benson_bassham_cycle.yaml`, `traitmech:000020`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1128/AEM.02473-10` and cites `DOI:10.1128/AEM.02473-10` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `parent data/traits/metabolism/carbon_fixation.yaml (traitmech:000019) evidence[0] and causal_graphs[0].edges[11].evidence[0]` already carrying the verified verbatim quote `"The reductive pentose phosphate cycle is the quantitatively most important mechanism of autotrophic CO2 fixation in nature."`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-011`)**: Populate verified verbatim quote for `DOI:10.1128/AEM.02473-10` in `data/traits/metabolism/calvin_benson_bassham_cycle.yaml`, append a `CURATE` event, and regenerate trait pages.
12. **`F-C3S4-DEF-SRC-012`** (`data/traits/metabolism/dissimilatory_manganese_reduction.yaml`, `traitmech:000108`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1128/mr.55.2.259-287.1991` and cites `DOI:10.1128/mr.55.2.259-287.1991` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `parent data/traits/metabolism/dissimilatory_metal_reduction.yaml (traitmech:000039) and sibling dissimilatory_iron_reduction.yaml (traitmech:000024) evidence[0]` already carrying the verified verbatim quote `"The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-012`)**: Populate verified verbatim quote for `DOI:10.1128/mr.55.2.259-287.1991` in `data/traits/metabolism/dissimilatory_manganese_reduction.yaml`, append a `CURATE` event, and regenerate trait pages.
13. **`F-C3S4-DEF-SRC-013`** (`data/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.yaml`, `traitmech:000030`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1126/science.1254070` and cites `DOI:10.1126/science.1254070` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `parent data/traits/metabolism/nitrate_respiration.yaml (traitmech:000122) evidence[0]` already carrying the verified verbatim quote `"Denitrification converts nitrate into nitrogenous gas and thus removes fixed nitrogen from the biosphere, whereas ammonification converts nitrate into ammonium"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-013`)**: Populate verified verbatim quote for `DOI:10.1126/science.1254070` in `data/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.yaml`, append a `CURATE` event, and regenerate trait pages.
14. **`F-C3S4-DEF-SRC-014`** (`data/traits/ecology/free_living.yaml`, `traitmech:000048`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1038/nrmicro1341` and cites `DOI:10.1038/nrmicro1341` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `sibling data/traits/ecology/soil_dwelling.yaml (traitmech:000050) evidence[0]` already carrying the verified verbatim quote `"free-living microbial taxa exhibit biogeographic patterns"`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-014`)**: Populate verified verbatim quote for `DOI:10.1038/nrmicro1341` in `data/traits/ecology/free_living.yaml`, append a `CURATE` event, and regenerate trait pages.
15. **`F-C3S4-DEF-SRC-015`** (`data/traits/morphology/amphitrichous.yaml`, `traitmech:000059`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1093/femsre/fuv034` and cites `DOI:10.1093/femsre/fuv034` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `sibling data/traits/morphology/polar_flagellation.yaml (METPO:1005032) evidence[0]` already carrying the verified verbatim quote `"Bacteria differ in number and location of their flagella that appear in regular patterns at the cell surface (flagellation pattern)."`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-015`)**: Populate verified verbatim quote for `DOI:10.1093/femsre/fuv034` in `data/traits/morphology/amphitrichous.yaml`, append a `CURATE` event, and regenerate trait pages.
16. **`F-C3S4-DEF-SRC-016`** (`data/traits/morphology/lophotrichous.yaml`, `traitmech:000058`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1093/femsre/fuv034` and cites `DOI:10.1093/femsre/fuv034` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `sibling data/traits/morphology/polar_flagellation.yaml (METPO:1005032) evidence[0]` already carrying the verified verbatim quote `"Bacteria differ in number and location of their flagella that appear in regular patterns at the cell surface (flagellation pattern)."`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-016`)**: Populate verified verbatim quote for `DOI:10.1093/femsre/fuv034` in `data/traits/morphology/lophotrichous.yaml`, append a `CURATE` event, and regenerate trait pages.
17. **`F-C3S4-DEF-SRC-017`** (`data/traits/morphology/monotrichous.yaml`, `traitmech:000057`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1093/femsre/fuv034` and cites `DOI:10.1093/femsre/fuv034` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `sibling data/traits/morphology/polar_flagellation.yaml (METPO:1005032) evidence[0]` already carrying the verified verbatim quote `"Bacteria differ in number and location of their flagella that appear in regular patterns at the cell surface (flagellation pattern)."`.
   - **Planned Stage 5 Remediation (`ACT-C3S4-DEF-SRC-017`)**: Populate verified verbatim quote for `DOI:10.1093/femsre/fuv034` in `data/traits/morphology/monotrichous.yaml`, append a `CURATE` event, and regenerate trait pages.

## 3. Carried-Forward Deferred Cohort-Level Findings (`status: deferred`)

Five cohort-level source-limited or upstream-blocked findings carried forward from Cycle 2 Stage 5 are documented with updated Cycle 3 counts and explicit dispositions:

1. **`F-COHORT-CAUSAL-GRAPHS-SOURCE-LIMITED-005`** (`388` eligible records; issue `#1982`): `366` records lack multi-step molecular pathways in currently cited open abstracts (reduced from `369` in Cycle 2 after `+3` Cycle 3 Stage 2 causal graphs) and `22` belong to non-mechanistic vocabulary cohorts (`upper`, `observation`, `quantitative_property`, `morphology` supporting vocabulary).
2. **`F-COHORT-CANONICAL-EXAMPLES-SOURCE-LIMITED-006`** (`551` eligible records; issue `#1983`): `578` eligible records (`579` total including excluded `spore_germination.yaml`) carry verified `canonical_examples`, while `551` eligible records have taxon-general or upper-level definitions lacking strain/species-explicit phenotype values in currently cited open abstracts.
3. **`F-COHORT-CAUSAL-GRAPH-BASELINES-007`** (`72` unique eligible records, `85` baseline warning rows in `conf/causal_graph_audit_baseline.tsv`; issue `#1984`): Cross-record `INCONSISTENT_NODE_TYPE` (`83`) and `DUPLICATE_GROUNDING` (`2`) warnings tracked under `#1984` (follow-up to `#356`).
4. **`F-COHORT-DEF-SOURCE-PAYWALLED-008`** (`69` eligible records; issue `#1985`): `69` eligible records (after excluding `photoorganoheterotrophic.yaml` as open finding `F-C3S4-DEF-SRC-001`; plus `72` remaining `UNQUOTED_DEFINITION_SOURCE` records without an intra-record or parent/sibling verbatim quote and `50` records omitting `definition_source`) have a primary discovery `definition_source` whose full text is paywalled or lacks a contiguous `>=12`-char definition quote in local sources, while record-level `evidence` is backed by open DefenseFinder wiki/catalog or companion sources.
5. **`F-COHORT-METPO-UPSTREAM-MINTING-009`** (`734` eligible `traitmech:NNNNNN` records; `735` total including excluded `traitmech:000083`; issue `#364`): Backed by validated ROBOT templates in `proposals/metpo_traitmech_v1..v611` awaiting upstream incorporation in `berkeleybop/metpo#535` (issue `#364`).
