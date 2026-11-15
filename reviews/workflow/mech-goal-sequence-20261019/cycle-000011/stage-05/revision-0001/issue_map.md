# Cycle 11 Stage 5 Grouped Finding & Issue Map

## Input Review Provenance

- **Source workflow evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/evidence.yaml` (`sha256: 498792fbeb04a862b662df0d62635742a9abf511e8ef7808f3bac9379595393a`)
- **Source native structured review**: `reviews/structured/20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review/review.yaml`
- **Carried-forward findings**: 17 total (`12` open record-level `definition_source` missing-snippet findings `F-C11S4-DEF-SRC-001`..`012` + `5` deferred cohort-level source-limited or upstream-blocked findings)
- **Live GitHub issue deduplication**: reused reopened [#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) for `G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS` and retained open issues [#1982](https://github.com/CultureBotAI/TraitMech/issues/1982), [#1983](https://github.com/CultureBotAI/TraitMech/issues/1983), [#1984](https://github.com/CultureBotAI/TraitMech/issues/1984), [#1985](https://github.com/CultureBotAI/TraitMech/issues/1985), and [#364](https://github.com/CultureBotAI/TraitMech/issues/364) for the five deferred cohort groups.

## Resolved Group

| Finding | Target | Path | Definition Source | Stage 5 Status |
|---|---|---|---|---|
| `F-C11S4-DEF-SRC-001` | `traitmech:000096` | `data/traits/genomics/codon_usage_bias.yaml` | `DOI:10.1038/nrg2899` | resolved |
| `F-C11S4-DEF-SRC-002` | `traitmech:000094` | `data/traits/genomics/crispr_cas_system.yaml` | `DOI:10.1038/s41579-019-0299-x` | resolved |
| `F-C11S4-DEF-SRC-003` | `traitmech:000097` | `data/traits/genomics/gc_skew.yaml` | `DOI:10.1093/oxfordjournals.molbev.a025626` | resolved |
| `F-C11S4-DEF-SRC-004` | `traitmech:000098` | `data/traits/genomics/genome_size.yaml` | `DOI:10.1038/nrmicro3331` | resolved |
| `F-C11S4-DEF-SRC-005` | `traitmech:000089` | `data/traits/genomics/mobile_genetic_element.yaml` | `DOI:10.1038/nrmicro1235` | resolved |
| `F-C11S4-DEF-SRC-006` | `traitmech:000102` | `data/traits/genomics/pangenome_openness.yaml` | `DOI:10.1073/pnas.0506758102` | resolved |
| `F-C11S4-DEF-SRC-007` | `traitmech:000090` | `data/traits/genomics/plasmid_carriage.yaml` | `DOI:10.1128/MMBR.00020-10` | resolved |
| `F-C11S4-DEF-SRC-008` | `traitmech:000100` | `data/traits/genomics/ploidy.yaml` | `DOI:10.1159/000368855` | resolved |
| `F-C11S4-DEF-SRC-009` | `traitmech:000091` | `data/traits/genomics/prophage.yaml` | `DOI:10.1128/MMBR.67.2.238-276.2003` | resolved |
| `F-C11S4-DEF-SRC-010` | `traitmech:000095` | `data/traits/genomics/restriction_modification_system.yaml` | `DOI:10.1128/MMBR.00044-12` | resolved |
| `F-C11S4-DEF-SRC-011` | `traitmech:000101` | `data/traits/genomics/rrna_operon_copy_number.yaml` | `DOI:10.1128/AEM.66.4.1328-1333.2000` | resolved |
| `F-C11S4-DEF-SRC-012` | `traitmech:000092` | `data/traits/genomics/transposable_element.yaml` | `DOI:10.1111/1574-6976.12067` | resolved |

All 12 resolved findings share the same cause and repair owner: `GENOMICS` records cited their primary `definition_source` DOI in record-level `evidence[0]` but omitted `evidence[0].snippet`, while the accepted Cycle 11 Stage 4 review had already identified verified Europe PMC abstract quotes. `scripts/curate_stage5_review_findings.py --apply` populated `evidence[0].snippet`, appended `ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE` curation-history events, and removed the 12 exact `evidence[0]` `MISSING_SNIPPET` rows from `conf/evidence_snippet_baseline.tsv`.

## Deferred Cohort Groups

| Group | Finding | Issue | Target Count | Stage 5 Status |
|---|---|---|---:|---|
| `G-STAGE4-CAUSAL-GRAPHS-SOURCE-LIMITED` | `F-COHORT-CAUSAL-GRAPHS-SOURCE-LIMITED-005` | [#1982](https://github.com/CultureBotAI/TraitMech/issues/1982) | 361 | deferred |
| `G-STAGE4-CANONICAL-EXAMPLES-SOURCE-LIMITED` | `F-COHORT-CANONICAL-EXAMPLES-SOURCE-LIMITED-006` | [#1983](https://github.com/CultureBotAI/TraitMech/issues/1983) | 551 | deferred |
| `G-STAGE4-CAUSAL-GRAPH-BASELINES` | `F-COHORT-CAUSAL-GRAPH-BASELINES-007` | [#1984](https://github.com/CultureBotAI/TraitMech/issues/1984) | 72 | deferred |
| `G-STAGE4-DEF-SOURCE-PAYWALLED` | `F-COHORT-DEF-SOURCE-PAYWALLED-008` | [#1985](https://github.com/CultureBotAI/TraitMech/issues/1985) | 29 | deferred |
| `G-STAGE4-METPO-UPSTREAM-MINTING` | `F-COHORT-METPO-UPSTREAM-MINTING-009` | [#364](https://github.com/CultureBotAI/TraitMech/issues/364) | 734 | deferred |

These five groups are unchanged from the Cycle 11 Stage 4 accepted dispositions and remain source-limited or upstream-blocked rather than actionable mechanical snippet fixes.
