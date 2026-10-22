# TraitMech Cycle 1 Stage 4 (`record_review`) — Frozen-Inventory Record and Cohort Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `1`, Stage `4` (`record_review`), Revision `1`
- **Repository**: `CultureBotAI/TraitMech`
- **Frozen Inventory Git SHA**: `b096d61ed6d2c4a78042c91bd8dc516459c9cd7a`
- **Native Structured Review ID**: `20261022T033000Z-stage4-corpus-record-and-cohort-review` (`reviews/structured/20261022T033000Z-stage4-corpus-record-and-cohort-review/review.yaml`)
- **Skills Executed**: `.claude/skills/review-yaml-record/SKILL.md`, `.claude/skills/review-yaml-category/SKILL.md`
- **Generated At**: `2026-10-22T03:30:00Z`

## 1. Executive Summary & Coverage Accounting

All **1,130** `TraitRecord` YAML files in `data/traits/` were inventoried at frozen commit `b096d61ed6d2c4a78042c91bd8dc516459c9cd7a`:
- **Eligible & Reviewed Records**: **1,129 / 1,129** (`100.0%` coverage across all 10 category cohorts: `395` eligible `METPO:` records and `734` eligible `traitmech:NNNNNN` records)
- **Excluded Records**: **1** (`data/traits/physiology/spore_germination.yaml`, `traitmech:000083`, protected by `DO_NOT_WORK.md` `#291`; `735` total `traitmech:NNNNNN` records including excluded `traitmech:000083`)
- **Updated Records in Stage 4**: **0** (Stage 4 is a read-only corpus review; all 4 open findings are preserved for Stage 5 `resolve_review_findings`)
- **Source-Limited Records**: **379** (eligible mechanistic-domain records lacking multi-step molecular pathways in currently cited open abstracts)
- **Non-Mechanistic Vocabulary Records**: **22** (`upper`: 8, `observation`: 1, `quantitative_property`: 7, `morphology` supporting vocabulary: 6)

### Category Cohort Breakdown

| Category Cohort | Total Files | Eligible & Reviewed | Excluded (`DO_NOT_WORK.md`) | With `causal_graphs` | With `canonical_examples` | Open Findings | Boundary Decision |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| `ecology` | 40 | 40 | 0 | 28 | 30 | 0 | `keep` |
| `environment` | 122 | 122 | 0 | 122 | 119 | 3 | `keep` |
| `genomics` | 387 | 387 | 0 | 372 | 102 | 0 | `keep` |
| `metabolism` | 180 | 180 | 0 | 51 | 65 | 0 | `keep` |
| `morphology` | 129 | 129 | 0 | 95 | 124 | 1 | `keep` |
| `observation` | 20 | 20 | 0 | 0 | 0 | 0 | `keep` |
| `other` | 32 | 32 | 0 | 0 | 12 | 0 | `keep` |
| `physiology` | 205 | 204 | 1 | 55 | 125 | 0 | `keep` |
| `quantitative_property` | 7 | 7 | 0 | 0 | 0 | 0 | `keep` |
| `upper` | 8 | 8 | 0 | 5 | 0 | 0 | `keep` |
| **Total** | **1,130** | **1,129** | **1** | **728** (eligible) | **577** (eligible) | **4** | **All 10 cohorts kept** |

## 2. Open Findings Preserved for Stage 5 (`resolve_review_findings`)

Four concrete, source-backed `minor` findings (`status: open`) were identified where a record declares a primary `definition_source` that already has a verified verbatim quote in the repository (either on the same record's `causal_graphs` edges or on parent/sibling records) but omits that `definition_source` from the record-level `evidence` block:

1. **`F-DEF-SRC-CYANOPHYCIN-001`** (`data/traits/morphology/cyanophycin_granule.yaml`, `traitmech:000673`):
   - **Defect**: Declares `definition_source: DOI:10.1128/AEM.01298-18` (Watzer and Forchhammer 2018) and already cites `DOI:10.1128/AEM.01298-18` with verbatim snippets on `causal_graphs[0].edges[2].evidence[0]` (`"Cyanophycin accumulates in the form of opaque and light-scattering granules in the cell"`) and `causal_graphs[0].edges[3].evidence[0]`, but omits `DOI:10.1128/AEM.01298-18` from record-level `evidence`.
   - **Planned Stage 5 Remediation (`ACT-DEF-SRC-CYANOPHYCIN-001`)**: Add `DOI:10.1128/AEM.01298-18` with its verified verbatim snippet to `evidence` on `cyanophycin_granule.yaml`, record a `CURATE` event, and regenerate trait pages.
2. **`F-DEF-SRC-CADMIUM-002`** (`data/traits/environment/cadmium_tolerant.yaml`, `traitmech:000013`):
   - **Defect**: Declares `definition_source: PMID:12829273` (Nies 2003, *Efflux-mediated heavy metal resistance in prokaryotes*) for its cation-efflux definition, but omits `PMID:12829273` from record-level `evidence` (unlike parent `metal_tolerant.yaml` and sibling `mercury_tolerant.yaml`, which cite `PMID:12829273` with verbatim snippet `"CBA efflux pumps driven by proteins of the resistance-nodulation-cell division superfamily, P-type ATPases, cation diffusion facilitator and chromate proteins"`).
   - **Planned Stage 5 Remediation (`ACT-DEF-SRC-CADMIUM-002`)**: Add `PMID:12829273` with the verified Nies 2003 verbatim snippet to `evidence` on `cadmium_tolerant.yaml`, record a `CURATE` event, and regenerate trait pages.
3. **`F-DEF-SRC-COBALT-003`** (`data/traits/environment/cobalt_tolerant.yaml`, `traitmech:000015`):
   - **Defect**: Declares `definition_source: PMID:12829273` (Nies 2003) for its divalent cobalt efflux definition, but omits `PMID:12829273` from record-level `evidence`.
   - **Planned Stage 5 Remediation (`ACT-DEF-SRC-COBALT-003`)**: Add `PMID:12829273` with the verified Nies 2003 verbatim snippet to `evidence` on `cobalt_tolerant.yaml`, record a `CURATE` event, and regenerate trait pages.
4. **`F-DEF-SRC-ZINC-004`** (`data/traits/environment/zinc_tolerant.yaml`, `traitmech:000014`):
   - **Defect**: Declares `definition_source: PMID:12829273` (Nies 2003) for its zinc resistance efflux definition, but omits `PMID:12829273` from record-level `evidence`.
   - **Planned Stage 5 Remediation (`ACT-DEF-SRC-ZINC-004`)**: Add `PMID:12829273` with the verified Nies 2003 verbatim snippet to `evidence` on `zinc_tolerant.yaml`, record a `CURATE` event, and regenerate trait pages.

## 3. Deferred Cohort-Level Findings (`status: deferred`)

Five cohort-level source-limited or upstream-blocked findings are documented with explicit dispositions:

1. **`F-COHORT-CAUSAL-GRAPHS-SOURCE-LIMITED-005`** (`401` eligible records): `379` records lack multi-step molecular pathways in currently cited open abstracts and `22` belong to non-mechanistic vocabulary cohorts (`upper`, `observation`, `quantitative_property`, `morphology` supporting vocabulary).
2. **`F-COHORT-CANONICAL-EXAMPLES-SOURCE-LIMITED-006`** (`552` eligible records): `577` eligible records (`578` total including excluded `spore_germination.yaml`) carry verified `canonical_examples`, while `552` eligible records (tracked in `POST_444_CANONICAL_EXAMPLE_QUEUE` in `scripts/backfill_canonical_examples_444.py` and record-level `CURATION_TODO` items) have taxon-general or upper-level definitions lacking strain/species-explicit phenotype values in currently cited open abstracts.
3. **`F-COHORT-CAUSAL-GRAPH-BASELINES-007`** (`72` unique eligible records, `85` baseline warning rows in `conf/causal_graph_audit_baseline.tsv`): Cross-record `INCONSISTENT_NODE_TYPE` (`83`) and `DUPLICATE_GROUNDING` (`2`) warnings tracked under issue `#356`.
4. **`F-COHORT-DEF-SOURCE-PAYWALLED-008`** (`70` eligible records): `70` eligible records (beyond the `4` open actionable findings, out of `74` total declaring a `definition_source` not repeated in record-level `evidence`; plus `50` records omitting `definition_source`) have a primary discovery `definition_source` whose full text is paywalled or lacks a contiguous `>=12`-char definition quote in local sources, while record-level `evidence` is backed by open DefenseFinder wiki/catalog or companion sources.
5. **`F-COHORT-METPO-UPSTREAM-MINTING-009`** (`734` eligible `traitmech:NNNNNN` records; `735` total including excluded `traitmech:000083`): Backed by validated ROBOT templates in `proposals/metpo_traitmech_v1..v611` awaiting upstream incorporation in `berkeleybop/metpo#535` (issue `#364`).
