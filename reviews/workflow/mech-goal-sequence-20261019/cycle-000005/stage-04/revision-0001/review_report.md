# TraitMech Cycle 5 Stage 4 (`record_review`) — Frozen-Inventory Record and Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `5`, Stage `4` (`record_review`), Revision `1`
- **Repository**: `CultureBotAI/TraitMech`
- **Frozen Inventory Git SHA**: `afb7c6f4195120046f2e7ec9d46072998c725505`
- **Native Structured Review ID**: `20261025T200500Z-cycle5-stage4-corpus-record-and-cohort-review` (`reviews/structured/20261025T200500Z-cycle5-stage4-corpus-record-and-cohort-review/review.yaml`)
- **Skills Executed**: `.claude/skills/review-yaml-record/SKILL.md`, `.claude/skills/review-yaml-category/SKILL.md`
- **Generated At**: `2026-10-25T20:05:00Z`

## 1. Executive Summary & Coverage Accounting

All **1,130** `TraitRecord` YAML files in `data/traits/` were inventoried at frozen commit `afb7c6f4195120046f2e7ec9d46072998c725505`:
- **Eligible & Reviewed Records**: **1,129 / 1,129** (`100.0%` coverage across all 10 category cohorts: `395` eligible `METPO:` records and `734` eligible `traitmech:NNNNNN` records)
- **Excluded Records**: **1** (`data/traits/physiology/spore_germination.yaml`, `traitmech:000083`, protected by `DO_NOT_WORK.md` `#291`; `735` total `traitmech:NNNNNN` records including excluded `traitmech:000083`)
- **Updated Records in Stage 4**: **0** (Stage 4 is a read-only corpus review; all 7 open findings are preserved for Cycle 5 Stage 5 `resolve_review_findings`)
- **Source-Limited Records**: **360** (eligible mechanistic-domain records lacking multi-step molecular pathways in currently cited open abstracts; reduced from `363` in Cycle 4 after `+3` Cycle 5 Stage 2 graphs: `acetoin_production_vogues_proskauer_positive.yaml`, `alkaline_phosphatase_activity.yaml`, `arginine_dihydrolase_activity.yaml`)
- **Non-Mechanistic Vocabulary Records**: **22** (`upper`: 8, `observation`: 1, `quantitative_property`: 7, `morphology` supporting vocabulary: 6)

### Category Cohort Breakdown

| Category Cohort | Total Files | Eligible & Reviewed | Excluded (`DO_NOT_WORK.md`) | With `causal_graphs` | With `canonical_examples` | Open Findings | Boundary Decision |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| `ecology` | 40 | 40 | 0 | 28 | 30 | 0 | `keep` |
| `environment` | 122 | 122 | 0 | 122 | 119 | 0 | `keep` |
| `genomics` | 387 | 387 | 0 | 372 | 102 | 3 | `keep` |
| `metabolism` | 180 | 180 | 0 | 59 | 66 | 3 | `keep` |
| `morphology` | 129 | 129 | 0 | 95 | 124 | 0 | `keep` |
| `observation` | 20 | 20 | 0 | 0 | 0 | 0 | `keep` |
| `other` | 32 | 32 | 0 | 2 | 12 | 0 | `keep` |
| `physiology` | 205 | 204 | 1 | 64 | 125 | 1 | `keep` |
| `quantitative_property` | 7 | 7 | 0 | 0 | 0 | 0 | `keep` |
| `upper` | 8 | 8 | 0 | 5 | 0 | 0 | `keep` |
| **Total** | **1,130** | **1,129** | **1** | **747** (eligible) | **578** (eligible) | **7** | **All 10 cohorts kept** |

## 2. Open Findings Preserved for Cycle 5 Stage 5 (`resolve_review_findings`)

Seven concrete, source-backed `minor` findings (`status: open`, `F-C5S4-DEF-SRC-001`..`007`) were identified across the `genomics` (`3`), `metabolism` (`3`), and `physiology` (`1`) cohorts where a `CLASS` record either cites the exact `definition_source` paper in record-level `evidence[0]` under its PMID alias `PMID:32855333` rather than `DOI:10.1126/science.aba0372` (`2` records), or cites its primary `definition_source` in record-level `evidence[0]` without a non-elliptical verbatim `snippet` while a verified verbatim quote from that exact `definition_source` already exists on an ancestor or cross-cohort `TraitRecord` in the corpus (`5` records):

1. **`F-C5S4-DEF-SRC-001`** (`data/traits/genomics/gao_her_duf_system.yaml`, `traitmech:000361`):
   - **Defect (`MISSING_DEFINITION_SOURCE_EVIDENCE`)**: Declares `definition_source: DOI:10.1126/science.aba0372` and cites `PMID:32855333` in record-level `evidence[0].reference` rather than `DOI:10.1126/science.aba0372`, while `record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and parent data/traits/genomics/gao_her_system.yaml (traitmech:000409) evidence[0]` carries the verified verbatim quote `"By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages."`.
   - **Planned Stage 5 Remediation (`ACT-C5S4-DEF-SRC-001`)**: Align or populate verified verbatim quote for `DOI:10.1126/science.aba0372` in `data/traits/genomics/gao_her_duf_system.yaml`, append a `CURATE` event, and regenerate trait pages.
2. **`F-C5S4-DEF-SRC-002`** (`data/traits/genomics/gao_her_sir_system.yaml`, `traitmech:000362`):
   - **Defect (`MISSING_DEFINITION_SOURCE_EVIDENCE`)**: Declares `definition_source: DOI:10.1126/science.aba0372` and cites `PMID:32855333` in record-level `evidence[0].reference` rather than `DOI:10.1126/science.aba0372`, while `record-level evidence[0] on the same record (cited under PMID alias PMID:32855333) and parent data/traits/genomics/gao_her_system.yaml (traitmech:000409) evidence[0]` carries the verified verbatim quote `"By systematic defense gene prediction and heterologous reconstitution, here we discover 29 widespread antiviral gene cassettes, collectively present in 32% of all sequenced bacterial and archaeal genomes, that mediate protection against specific bacteriophages."`.
   - **Planned Stage 5 Remediation (`ACT-C5S4-DEF-SRC-002`)**: Align or populate verified verbatim quote for `DOI:10.1126/science.aba0372` in `data/traits/genomics/gao_her_sir_system.yaml`, append a `CURATE` event, and regenerate trait pages.
3. **`F-C5S4-DEF-SRC-003`** (`data/traits/genomics/genome_streamlining.yaml`, `traitmech:000099`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1038/ismej.2014.60` and cites `DOI:10.1038/ismej.2014.60` in record-level `evidence[0].snippet` without a non-elliptical verbatim `snippet`, despite `data/traits/physiology/oligotrophic.yaml (METPO:1000675) causal_graphs[0].edges[1].evidence[0] (streamlined_genome -> efficient_nutrient_use)` already carrying the verified verbatim quote `"minimizes resources required for replication"`.
   - **Planned Stage 5 Remediation (`ACT-C5S4-DEF-SRC-003`)**: Align or populate verified verbatim quote for `DOI:10.1038/ismej.2014.60` in `data/traits/genomics/genome_streamlining.yaml`, append a `CURATE` event, and regenerate trait pages.
4. **`F-C5S4-DEF-SRC-004`** (`data/traits/metabolism/biopolymer_degradation.yaml`, `traitmech:000110`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1016/j.cbpa.2015.10.018` and cites `DOI:10.1016/j.cbpa.2015.10.018` in record-level `evidence[0].snippet` without a non-elliptical verbatim `snippet`, despite `data/traits/ecology/saprotrophy.yaml (traitmech:000042) causal_graphs[0].edges[2].evidence[0] (cazymes -> hemicellulose)` already carrying the verified verbatim quote `"The enzymatic degradation of cellulose and hemicellulose is accomplished in Nature via the collective action of multiple carbohydrate-active enzymes"`.
   - **Planned Stage 5 Remediation (`ACT-C5S4-DEF-SRC-004`)**: Align or populate verified verbatim quote for `DOI:10.1016/j.cbpa.2015.10.018` in `data/traits/metabolism/biopolymer_degradation.yaml`, append a `CURATE` event, and regenerate trait pages.
5. **`F-C5S4-DEF-SRC-005`** (`data/traits/metabolism/denitrification.yaml`, `traitmech:000104`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1128/mmbr.61.4.533-616.1997` and cites `DOI:10.1128/mmbr.61.4.533-616.1997` in record-level `evidence[0].snippet` without a non-elliptical verbatim `snippet`, despite `ancestor data/traits/metabolism/nitrogen_respiration.yaml (traitmech:000126) evidence[0] and data/traits/metabolism/anaerobic_respiration.yaml (traitmech:000013) evidence[0]` already carrying the verified verbatim quote `"N oxides as terminal electron acceptors"`.
   - **Planned Stage 5 Remediation (`ACT-C5S4-DEF-SRC-005`)**: Align or populate verified verbatim quote for `DOI:10.1128/mmbr.61.4.533-616.1997` in `data/traits/metabolism/denitrification.yaml`, append a `CURATE` event, and regenerate trait pages.
6. **`F-C5S4-DEF-SRC-006`** (`data/traits/metabolism/sulfur_oxidation.yaml`, `traitmech:000106`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1111/j.1574-6976.2009.00187.x` and cites `DOI:10.1111/j.1574-6976.2009.00187.x` in record-level `evidence[0].snippet` without a non-elliptical verbatim `snippet`, despite `data/traits/physiology/lithotrophic.yaml (METPO:1000629) causal_graphs[0].edges[0].evidence[0] (reduced_sulfur_compound -> inorganic_electron_donor)` already carrying the verified verbatim quote `"lithotrophic sulfur oxidation"`.
   - **Planned Stage 5 Remediation (`ACT-C5S4-DEF-SRC-006`)**: Align or populate verified verbatim quote for `DOI:10.1111/j.1574-6976.2009.00187.x` in `data/traits/metabolism/sulfur_oxidation.yaml`, append a `CURATE` event, and regenerate trait pages.
7. **`F-C5S4-DEF-SRC-007`** (`data/traits/physiology/catalase_activity.yaml`, `traitmech:000075`):
   - **Defect (`UNQUOTED_DEFINITION_SOURCE`)**: Declares `definition_source: DOI:10.1007/s00018-003-3206-5` and cites `DOI:10.1007/s00018-003-3206-5` in record-level `evidence[0].snippet` without a non-elliptical verbatim `snippet`, despite `data/traits/physiology/oxidative_stress_response.yaml (traitmech:000037) evidence[1]` already carrying the verified verbatim quote `"hydrogen peroxide to water and molecular oxygen, serving to protect cells"`.
   - **Planned Stage 5 Remediation (`ACT-C5S4-DEF-SRC-007`)**: Align or populate verified verbatim quote for `DOI:10.1007/s00018-003-3206-5` in `data/traits/physiology/catalase_activity.yaml`, append a `CURATE` event, and regenerate trait pages.

## 3. Carried-Forward Deferred Cohort-Level Findings (`status: deferred`)

Five cohort-level source-limited or upstream-blocked findings carried forward from Cycle 4 Stage 5 are documented with updated Cycle 5 counts and explicit dispositions:

1. **`F-COHORT-CAUSAL-GRAPHS-SOURCE-LIMITED-005`** (`382` eligible records; issue `#1982`): `360` records lack multi-step molecular pathways in currently cited open abstracts (reduced from `363` in Cycle 4 after `+3` Cycle 5 Stage 2 causal graphs) and `22` belong to non-mechanistic vocabulary cohorts (`upper`, `observation`, `quantitative_property`, `morphology` supporting vocabulary).
2. **`F-COHORT-CANONICAL-EXAMPLES-SOURCE-LIMITED-006`** (`551` eligible records; issue `#1983`): `578` eligible records (`579` total including excluded `spore_germination.yaml`) carry verified `canonical_examples`, while `551` eligible records have taxon-general or upper-level definitions lacking strain/species-explicit phenotype values in currently cited open abstracts.
3. **`F-COHORT-CAUSAL-GRAPH-BASELINES-007`** (`72` unique eligible records, `85` baseline warning rows in `conf/causal_graph_audit_baseline.tsv`; issue `#1984`): Cross-record `INCONSISTENT_NODE_TYPE` (`83`) and `DUPLICATE_GROUNDING` (`2`) warnings tracked under `#1984` (follow-up to `#356`).
4. **`F-COHORT-DEF-SOURCE-PAYWALLED-008`** (`57` eligible records; issue `#1985`): `57` eligible records (after excluding the `2` Gao-Her-* defense system records promoted to open findings `F-C5S4-DEF-SRC-001`..`002`; plus `58` remaining unquoted `CLASS` `definition_source` records without an in-corpus verbatim quote after promoting `F-C5S4-DEF-SRC-003`..`007`, `31` `OBJECT_PROPERTY` records with predicate-stem snippets resolved under `traitmech-infra-0006`, and `50` records omitting `definition_source`) have a primary discovery `definition_source` whose full text is paywalled or lacks a contiguous `>=12`-char definition quote in local sources, while record-level `evidence` is backed by open DefenseFinder wiki/catalog or companion sources.
5. **`F-COHORT-METPO-UPSTREAM-MINTING-009`** (`734` eligible `traitmech:NNNNNN` records; `735` total including excluded `traitmech:000083`; issue `#364`): Backed by validated ROBOT templates in `proposals/metpo_traitmech_v1..v611` awaiting upstream incorporation in `berkeleybop/metpo#535` (issue `#364`).
