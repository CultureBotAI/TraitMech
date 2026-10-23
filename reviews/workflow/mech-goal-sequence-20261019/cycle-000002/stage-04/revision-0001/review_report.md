# TraitMech Cycle 2 Stage 4 (`record_review`) — Frozen-Inventory Record and Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `2`, Stage `4` (`record_review`), Revision `1`
- **Repository**: `CultureBotAI/TraitMech`
- **Frozen Inventory Git SHA**: `a9355a37586d2808d945ffdb292862f7d64c1c67`
- **Native Structured Review ID**: `20261023T140800Z-cycle2-stage4-corpus-record-and-cohort-review` (`reviews/structured/20261023T140800Z-cycle2-stage4-corpus-record-and-cohort-review/review.yaml`)
- **Skills Executed**: `.claude/skills/review-yaml-record/SKILL.md`, `.claude/skills/review-yaml-category/SKILL.md`
- **Generated At**: `2026-10-23T14:08:00Z`

## 1. Executive Summary & Coverage Accounting

All **1,130** `TraitRecord` YAML files in `data/traits/` were inventoried at frozen commit `a9355a37586d2808d945ffdb292862f7d64c1c67`:
- **Eligible & Reviewed Records**: **1,129 / 1,129** (`100.0%` coverage across all 10 category cohorts: `395` eligible `METPO:` records and `734` eligible `traitmech:NNNNNN` records)
- **Excluded Records**: **1** (`data/traits/physiology/spore_germination.yaml`, `traitmech:000083`, protected by `DO_NOT_WORK.md` `#291`; `735` total `traitmech:NNNNNN` records including excluded `traitmech:000083`)
- **Updated Records in Stage 4**: **0** (Stage 4 is a read-only corpus review; all 6 open findings are preserved for Cycle 2 Stage 5 `resolve_review_findings`)
- **Source-Limited Records**: **369** (eligible mechanistic-domain records lacking multi-step molecular pathways in currently cited open abstracts; reduced from `379` in Cycle 1 after `+10` Cycle 2 Stage 2 graphs)
- **Non-Mechanistic Vocabulary Records**: **22** (`upper`: 8, `observation`: 1, `quantitative_property`: 7, `morphology` supporting vocabulary: 6)

### Category Cohort Breakdown

| Category Cohort | Total Files | Eligible & Reviewed | Excluded (`DO_NOT_WORK.md`) | With `causal_graphs` | With `canonical_examples` | Open Findings | Boundary Decision |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| `ecology` | 40 | 40 | 0 | 28 | 30 | 0 | `keep` |
| `environment` | 122 | 122 | 0 | 122 | 119 | 0 | `keep` |
| `genomics` | 387 | 387 | 0 | 372 | 102 | 0 | `keep` |
| `metabolism` | 180 | 180 | 0 | 58 | 66 | 6 | `keep` |
| `morphology` | 129 | 129 | 0 | 95 | 124 | 0 | `keep` |
| `observation` | 20 | 20 | 0 | 0 | 0 | 0 | `keep` |
| `other` | 32 | 32 | 0 | 0 | 12 | 0 | `keep` |
| `physiology` | 205 | 204 | 1 | 58 | 125 | 0 | `keep` |
| `quantitative_property` | 7 | 7 | 0 | 0 | 0 | 0 | `keep` |
| `upper` | 8 | 8 | 0 | 5 | 0 | 0 | `keep` |
| **Total** | **1,130** | **1,129** | **1** | **738** (eligible) | **578** (eligible) | **6** | **All 10 cohorts kept** |

## 2. Open Findings Preserved for Cycle 2 Stage 5 (`resolve_review_findings`)

Using the new `scripts/audit_evidence_snippets.py --check-definition-sources` check (implemented in Cycle 1 Stage 6 under `traitmech-infra-0004`, `#1981`), six concrete, source-backed `minor` findings (`status: open`) were identified in the `metabolism` cohort where a record cites its primary `definition_source` in record-level `evidence[0]` with `notes:` only and no verbatim `snippet` (`UNQUOTED_DEFINITION_SOURCE`), even though the exact same record's `causal_graphs[0].edges` already carries a verified verbatim quote from that `definition_source`:

1. **`F-DEF-SRC-CARBON-FIXATION-010`** (`data/traits/metabolism/carbon_fixation.yaml`, `traitmech:000019`):
   - **Defect**: Declares `definition_source: DOI:10.1128/AEM.02473-10` (Berg 2011) and cites `DOI:10.1128/AEM.02473-10` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[11].evidence[0]` (`cbb_cycle -> carbon_fixation_process`) already carrying the verified verbatim quote `"The reductive pentose phosphate cycle is the quantitatively most important mechanism of autotrophic CO2 fixation in nature."`.
   - **Planned Stage 5 Remediation (`ACT-DEF-SRC-CARBON-FIXATION-010`)**: Populate `snippet` on `evidence[0]` in `carbon_fixation.yaml` with the verified Berg 2011 verbatim quote, append a `CURATE` event, and regenerate trait pages.
2. **`F-DEF-SRC-WOOD-LJUNGDAHL-011`** (`data/traits/metabolism/wood_ljungdahl_pathway.yaml`, `traitmech:000022`):
   - **Defect**: Declares `definition_source: DOI:10.1016/j.bbapap.2008.08.012` (Ragsdale and Pierce 2008) and cites `DOI:10.1016/j.bbapap.2008.08.012` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[0].evidence[0]` (`wood_ljungdahl_pathway -> wood_ljungdahl_trait`) already carrying the verified verbatim quote `"use the reductive acetyl-CoA or Wood-Ljungdahl pathway as their main mechanism for energy conservation and for synthesis of acetyl-CoA and cell carbon from CO2"`.
   - **Planned Stage 5 Remediation (`ACT-DEF-SRC-WOOD-LJUNGDAHL-011`)**: Populate `snippet` on `evidence[0]` in `wood_ljungdahl_pathway.yaml` with the verified Ragsdale and Pierce 2008 verbatim quote, append a `CURATE` event, and regenerate trait pages.
3. **`F-DEF-SRC-PROPIONIC-FERM-012`** (`data/traits/metabolism/propionic_acid_fermentation.yaml`, `traitmech:000029`):
   - **Defect**: Declares `definition_source: DOI:10.3390/molecules31020333` and cites `DOI:10.3390/molecules31020333` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[1].evidence[0]` (`propionic_acid_fermentation_trait -> propionate`) already carrying the verified verbatim quote `"substrates such as glucose, glycerol or lactic acid are converted into propionic acid"`.
   - **Planned Stage 5 Remediation (`ACT-DEF-SRC-PROPIONIC-FERM-012`)**: Populate `snippet` on `evidence[0]` in `propionic_acid_fermentation.yaml` with the verified verbatim quote, append a `CURATE` event, and regenerate trait pages.
4. **`F-DEF-SRC-MANGANESE-OX-013`** (`data/traits/metabolism/manganese_oxidation.yaml`, `traitmech:000032`):
   - **Defect**: Declares `definition_source: DOI:10.1016/j.tim.2005.07.009` (Tebo et al. 2005) and cites `DOI:10.1016/j.tim.2005.07.009` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[3].evidence[0]` (`multicopper_oxidase -> manganese_oxidation_trait`) already carrying the verified verbatim quote `"the reaction might involve a unique multicopper oxidase system capable of a two-electron oxidation of the substrate"`.
   - **Planned Stage 5 Remediation (`ACT-DEF-SRC-MANGANESE-OX-013`)**: Populate `snippet` on `evidence[0]` in `manganese_oxidation.yaml` with the verified Tebo et al. 2005 verbatim quote, append a `CURATE` event, and regenerate trait pages.
5. **`F-DEF-SRC-CELLULOLYSIS-014`** (`data/traits/metabolism/cellulolysis.yaml`, `traitmech:000111`):
   - **Defect**: Declares `definition_source: DOI:10.1128/MMBR.66.3.506-577.2002` (Lynd et al. 2002) and cites `DOI:10.1128/MMBR.66.3.506-577.2002` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[15].evidence[0]` (`cellulosome -> cellulolysis_trait`) already carrying the verified verbatim quote `"complexed cellulase systems"`.
   - **Planned Stage 5 Remediation (`ACT-DEF-SRC-CELLULOLYSIS-014`)**: Populate `snippet` on `evidence[0]` in `cellulolysis.yaml` with the verified Lynd et al. 2002 verbatim quote, append a `CURATE` event, and regenerate trait pages.
6. **`F-DEF-SRC-CHITINOLYSIS-015`** (`data/traits/metabolism/chitinolysis.yaml`, `traitmech:000112`):
   - **Defect**: Declares `definition_source: DOI:10.3389/fmicb.2013.00149` (Beier and Bertilsson 2013) and cites `DOI:10.3389/fmicb.2013.00149` in record-level `evidence[0]` with `notes:` only and no `snippet`, despite `causal_graphs[0].edges[6].evidence[0]` (`chitinase -> chitin`) already carrying the verified verbatim quote `"initial hydrolysis of the (1→4)-β-glycoside bond, as seen for chitinase-catalyzed chitin degradation"`.
   - **Planned Stage 5 Remediation (`ACT-DEF-SRC-CHITINOLYSIS-015`)**: Populate `snippet` on `evidence[0]` in `chitinolysis.yaml` with the verified Beier and Bertilsson 2013 verbatim quote, append a `CURATE` event, and regenerate trait pages.

## 3. Carried-Forward Deferred Cohort-Level Findings (`status: deferred`)

Five cohort-level source-limited or upstream-blocked findings carried forward from Cycle 1 Stage 5 are documented with updated Cycle 2 counts and explicit dispositions:

1. **`F-COHORT-CAUSAL-GRAPHS-SOURCE-LIMITED-005`** (`391` eligible records; issue `#1982`): `369` records lack multi-step molecular pathways in currently cited open abstracts (reduced from `379` in Cycle 1 after `+10` Cycle 2 Stage 2 causal graphs) and `22` belong to non-mechanistic vocabulary cohorts (`upper`, `observation`, `quantitative_property`, `morphology` supporting vocabulary).
2. **`F-COHORT-CANONICAL-EXAMPLES-SOURCE-LIMITED-006`** (`551` eligible records; issue `#1983`): `578` eligible records (`579` total including excluded `spore_germination.yaml`; up from `577` eligible in Cycle 1) carry verified `canonical_examples`, while `551` eligible records have taxon-general or upper-level definitions lacking strain/species-explicit phenotype values in currently cited open abstracts.
3. **`F-COHORT-CAUSAL-GRAPH-BASELINES-007`** (`72` unique eligible records, `85` baseline warning rows in `conf/causal_graph_audit_baseline.tsv`; issue `#1984`): Cross-record `INCONSISTENT_NODE_TYPE` (`83`) and `DUPLICATE_GROUNDING` (`2`) warnings tracked under `#1984` (follow-up to `#356`).
4. **`F-COHORT-DEF-SOURCE-PAYWALLED-008`** (`70` eligible records; issue `#1985`): `70` eligible records (after Cycle 1 Stage 5 resolved the 4 open `definition_source` findings; plus `88` remaining `UNQUOTED_DEFINITION_SOURCE` records without an intra-record verbatim quote and `50` records omitting `definition_source`) have a primary discovery `definition_source` whose full text is paywalled or lacks a contiguous `>=12`-char definition quote in local sources, while record-level `evidence` is backed by open DefenseFinder wiki/catalog or companion sources.
5. **`F-COHORT-METPO-UPSTREAM-MINTING-009`** (`734` eligible `traitmech:NNNNNN` records; `735` total including excluded `traitmech:000083`; issue `#364`): Backed by validated ROBOT templates in `proposals/metpo_traitmech_v1..v611` awaiting upstream incorporation in `berkeleybop/metpo#535` (issue `#364`).
