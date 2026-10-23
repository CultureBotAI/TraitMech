# Cycle 2 Stage 5 Grouped Finding & Issue Map (`mech-goal-sequence-20261019`, Cycle 2, Stage 5)

## Input Review Provenance
- **Source workflow evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml` (`sha256: 1bb1aa12138f8562dcc3f57d321ee35461719215c7e1ca41a4f45ebd1de516d1`)
- **Source native structured review**: `reviews/structured/20261023T140800Z-cycle2-stage4-corpus-record-and-cohort-review/review.yaml` (`sha256: 0c962524454ffdb843da049562315a40a98583159335b775eccd8045616d7c47`)
- **Carried-forward findings**: 11 total (`6` open record-level `definition_source` evidence snippet findings + `5` deferred cohort-level source-limited or upstream-blocked findings)
- **Live GitHub issue deduplication**: Reconciled against all live issues in `CultureBotAI/TraitMech` via `gh issue list --state all --limit 200 --json number,title,state,url,labels`

---

## Cause-and-Ownership Group Summary

| Group ID | Cause & Repair Ownership | GitHub Issue | Issue Disposition | Finding IDs | Target Count | Stage 5 Disposition |
|---|---|---|---|---|---:|---|
| `G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS` | Six `METABOLISM` TraitRecord files cite their `definition_source` (`DOI:`) in `evidence[0]` with `notes` only (`MISSING_SNIPPET` at `evidence[0]` and `UNQUOTED_DEFINITION_SOURCE` under `scripts/audit_evidence_snippets.py --check-definition-sources`), while already carrying a verified verbatim contiguous `snippet` from that exact `definition_source` on a `causal_graphs[0].edges` entry. Owned by `data/traits/metabolism/*.yaml` via guarded writer `scripts/curate_stage5_review_findings.py`. | [#1995](https://github.com/CultureBotAI/TraitMech/issues/1995) | `created` | `F-DEF-SRC-CARBON-FIXATION-010`, `F-DEF-SRC-WOOD-LJUNGDAHL-011`, `F-DEF-SRC-PROPIONIC-FERM-012`, `F-DEF-SRC-MANGANESE-OX-013`, `F-DEF-SRC-CELLULOLYSIS-014`, `F-DEF-SRC-CHITINOLYSIS-015` | 6 | **`resolved`** (`scripts/curate_stage5_review_findings.py --apply`) |
| `G-STAGE4-CAUSAL-GRAPHS-SOURCE-LIMITED` | Source-limited and supporting-vocabulary TraitRecord files lacking `causal_graphs` (369 records where open-access PubMed/PMC/EuropePMC literature lacks a multi-step causal mechanism snippet, reduced from 379 in Cycle 1 after +10 Cycle 2 Stage 2 graphs, plus 22 `SUPPORTING_FIELD_VOCABULARY` non-mechanistic records); requires new primary experimental literature (`deep-research-trait` / `research-causal-graphs`) rather than mechanical backfill. | [#1982](https://github.com/CultureBotAI/TraitMech/issues/1982) | `reused_open` | `F-COHORT-CAUSAL-GRAPHS-SOURCE-LIMITED-005` | 391 | **`deferred`** (external primary literature blocker) |
| `G-STAGE4-CANONICAL-EXAMPLES-SOURCE-LIMITED` | Source-limited TraitRecord files lacking species/strain `canonical_examples` (`POST_444_CANONICAL_EXAMPLE_QUEUE`); 578 eligible records and 579 total records carry verified `canonical_examples` (up from 577 eligible in Cycle 1), while 551 require primary experimental strain/species citations with verified `NCBITaxon` IDs. | [#1983](https://github.com/CultureBotAI/TraitMech/issues/1983) | `reused_open` | `F-COHORT-CANONICAL-EXAMPLES-SOURCE-LIMITED-006` | 551 | **`deferred`** (external primary literature blocker) |
| `G-STAGE4-CAUSAL-GRAPH-BASELINES` | Pre-existing baselined cross-record `node_type` / grounding harmonization warnings (`conf/causal_graph_audit_baseline.tsv`, 85 warnings across 72 files). | [#1984](https://github.com/CultureBotAI/TraitMech/issues/1984) | `reused_open` | `F-COHORT-CAUSAL-GRAPH-BASELINES-007` | 72 | **`deferred`** (multi-record ontology harmonization cohort) |
| `G-STAGE4-DEF-SOURCE-PAYWALLED` | TraitRecord files whose `definition_source` (`PMID:` or `DOI:`) is a paywalled primary discovery paper or textbook chapter lacking open-access full text from which a contiguous verbatim snippet can be extracted without fabrication. | [#1985](https://github.com/CultureBotAI/TraitMech/issues/1985) | `reused_open` | `F-COHORT-DEF-SOURCE-PAYWALLED-008` | 70 | **`deferred`** (paywalled primary literature blocker) |
| `G-STAGE4-METPO-UPSTREAM-MINTING` | Repository-minted `traitmech:NNNNNN` identifiers (734 eligible + 1 excluded in `DO_NOT_WORK.md`, 735 total) backed by validated ROBOT templates in `proposals/metpo_traitmech_v1..v611` awaiting upstream `METPO:` release minting. | [#364](https://github.com/CultureBotAI/TraitMech/issues/364) | `reused_open` | `F-COHORT-METPO-UPSTREAM-MINTING-009` | 734 | **`deferred`** (upstream `berkeleybop/metpo#535` release blocker) |

---

## Per-Finding Disposition Detail

### Resolved Findings (`G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS` -> [#1995](https://github.com/CultureBotAI/TraitMech/issues/1995))

1. **`F-DEF-SRC-CARBON-FIXATION-010`** (`traitmech:000019`, `data/traits/metabolism/carbon_fixation.yaml`)
   - **Defect**: `definition_source: DOI:10.1128/AEM.02473-10` cited in `evidence[0]` with `notes` only, while `causal_graphs[0].edges[11].evidence[0]` already quoted `DOI:10.1128/AEM.02473-10` verbatim.
   - **Fix Applied**: Promoted verified verbatim `snippet` (`"The reductive pentose phosphate cycle is the quantitatively most important mechanism of autotrophic CO2 fixation in nature."`) into `evidence[0]` and appended `ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE` to `curation_history` via `scripts/curate_stage5_review_findings.py --apply`.
   - **Fresh Review Verification**: `reviews/structured/20261023T161000Z-cycle2-stage5-remediated-records-review/review.yaml` (`status: resolved`, `verdict: pass`).

2. **`F-DEF-SRC-WOOD-LJUNGDAHL-011`** (`traitmech:000022`, `data/traits/metabolism/wood_ljungdahl_pathway.yaml`)
   - **Defect**: `definition_source: DOI:10.1016/j.bbapap.2008.08.012` cited in `evidence[0]` with `notes` only, while `causal_graphs[0].edges[0].evidence[0]` already quoted `DOI:10.1016/j.bbapap.2008.08.012` verbatim.
   - **Fix Applied**: Promoted verified verbatim `snippet` (`"use the reductive acetyl-CoA or Wood-Ljungdahl pathway as their main mechanism for energy conservation and for synthesis of acetyl-CoA and cell carbon from CO2"`) into `evidence[0]` and appended `ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE` to `curation_history` via `scripts/curate_stage5_review_findings.py --apply`.
   - **Fresh Review Verification**: `reviews/structured/20261023T161000Z-cycle2-stage5-remediated-records-review/review.yaml` (`status: resolved`, `verdict: pass`).

3. **`F-DEF-SRC-PROPIONIC-FERM-012`** (`traitmech:000029`, `data/traits/metabolism/propionic_acid_fermentation.yaml`)
   - **Defect**: `definition_source: DOI:10.3390/molecules31020333` cited in `evidence[0]` with `notes` only, while `causal_graphs[0].edges[1].evidence[0]` already quoted `DOI:10.3390/molecules31020333` verbatim.
   - **Fix Applied**: Promoted verified verbatim `snippet` (`"substrates such as glucose, glycerol or lactic acid are converted into propionic acid"`) into `evidence[0]` and appended `ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE` to `curation_history` via `scripts/curate_stage5_review_findings.py --apply`.
   - **Fresh Review Verification**: `reviews/structured/20261023T161000Z-cycle2-stage5-remediated-records-review/review.yaml` (`status: resolved`, `verdict: pass`).

4. **`F-DEF-SRC-MANGANESE-OX-013`** (`traitmech:000032`, `data/traits/metabolism/manganese_oxidation.yaml`)
   - **Defect**: `definition_source: DOI:10.1016/j.tim.2005.07.009` cited in `evidence[0]` with `notes` only, while `causal_graphs[0].edges[3].evidence[0]` already quoted `DOI:10.1016/j.tim.2005.07.009` verbatim.
   - **Fix Applied**: Promoted verified verbatim `snippet` (`"the reaction might involve a unique multicopper oxidase system capable of a two-electron oxidation of the substrate"`) into `evidence[0]` and appended `ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE` to `curation_history` via `scripts/curate_stage5_review_findings.py --apply`.
   - **Fresh Review Verification**: `reviews/structured/20261023T161000Z-cycle2-stage5-remediated-records-review/review.yaml` (`status: resolved`, `verdict: pass`).

5. **`F-DEF-SRC-CELLULOLYSIS-014`** (`traitmech:000111`, `data/traits/metabolism/cellulolysis.yaml`)
   - **Defect**: `definition_source: DOI:10.1128/MMBR.66.3.506-577.2002` cited in `evidence[0]` with `notes` only, while `causal_graphs[0].edges[15].evidence[0]` already quoted `DOI:10.1128/MMBR.66.3.506-577.2002` verbatim.
   - **Fix Applied**: Promoted verified verbatim `snippet` (`"complexed cellulase systems"`) into `evidence[0]` and appended `ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE` to `curation_history` via `scripts/curate_stage5_review_findings.py --apply`.
   - **Fresh Review Verification**: `reviews/structured/20261023T161000Z-cycle2-stage5-remediated-records-review/review.yaml` (`status: resolved`, `verdict: pass`).

6. **`F-DEF-SRC-CHITINOLYSIS-015`** (`traitmech:000112`, `data/traits/metabolism/chitinolysis.yaml`)
   - **Defect**: `definition_source: DOI:10.3389/fmicb.2013.00149` cited in `evidence[0]` with `notes` only, while `causal_graphs[0].edges[6].evidence[0]` already quoted `DOI:10.3389/fmicb.2013.00149` verbatim.
   - **Fix Applied**: Promoted verified verbatim `snippet` (`"initial hydrolysis of the (1→4)-β-glycoside bond, as seen for chitinase-catalyzed chitin degradation"`) into `evidence[0]` and appended `ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE` to `curation_history` via `scripts/curate_stage5_review_findings.py --apply`.
   - **Fresh Review Verification**: `reviews/structured/20261023T161000Z-cycle2-stage5-remediated-records-review/review.yaml` (`status: resolved`, `verdict: pass`).
