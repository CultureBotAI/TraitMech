# Cycle 11 Stage 5 post-remediation verification review of the 12 genomics TraitRecord files in group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS

- Review: 20261115T041700Z-cycle11-stage5-remediated-records-review
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-11-15T04:16:00Z
- Finished UTC: 2026-11-15T04:17:00Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass
- Scientific review: true

## Summary

Fresh post-remediation batch review of the 12 genomics TraitRecord YAML files remediated in Cycle 11 Stage 5 under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002. All 12 Cycle 11 Stage 4 open findings (F-C11S4-DEF-SRC-001..012) are verified as resolved with contiguous verbatim snippets for their primary definition_source DOI in record-level evidence[0], removal of all 12 baselined MISSING_SNIPPET rows from conf/evidence_snippet_baseline.tsv (2,349 -&gt; 2,337 total baselined findings), append-only curation_history provenance, and 0 remaining open findings.

## Scope And Provenance

Focused post-remediation review of all 12 genomics TraitRecord YAML files modified in Cycle 11 Stage 5 to resolve group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002).

Selection: All 12 records with open findings carried forward from Cycle 11 Stage 4 review 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review.
Coverage: full; 12 reviewed / 12 in the declared population.
Source: working_tree at Git base 2ccbc22ccfb8bd00c9d9ca70e11e020f818fbc18.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000096 | data/traits/genomics/codon_usage_bias.yaml | maintained | codon usage bias |
| traitmech:000094 | data/traits/genomics/crispr_cas_system.yaml | maintained | CRISPR-Cas system |
| traitmech:000097 | data/traits/genomics/gc_skew.yaml | maintained | GC skew |
| traitmech:000098 | data/traits/genomics/genome_size.yaml | maintained | genome size |
| traitmech:000089 | data/traits/genomics/mobile_genetic_element.yaml | maintained | mobile genetic element |
| traitmech:000102 | data/traits/genomics/pangenome_openness.yaml | maintained | pangenome openness |
| traitmech:000090 | data/traits/genomics/plasmid_carriage.yaml | maintained | plasmid carriage |
| traitmech:000100 | data/traits/genomics/ploidy.yaml | maintained | ploidy |
| traitmech:000091 | data/traits/genomics/prophage.yaml | maintained | prophage |
| traitmech:000095 | data/traits/genomics/restriction_modification_system.yaml | maintained | restriction-modification system |
| traitmech:000101 | data/traits/genomics/rrna_operon_copy_number.yaml | maintained | rRNA operon copy number |
| traitmech:000092 | data/traits/genomics/transposable_element.yaml | maintained | transposable element |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Stage 5 guarded writer idempotency | passed | True | traitmech:000096, traitmech:000094, traitmech:000097, traitmech:000098, traitmech:000089, traitmech:000102, traitmech:000090, traitmech:000100, traitmech:000091, traitmech:000095, traitmech:000101, traitmech:000092 | just curate-stage5-review-findings reported 127 resolved specs, 0 files updated, and 0 baseline rows pruned after apply. |
| Stage 5 writer focused tests | passed | True | traitmech:000096, traitmech:000094, traitmech:000097, traitmech:000098, traitmech:000089, traitmech:000102, traitmech:000090, traitmech:000100, traitmech:000091, traitmech:000095, traitmech:000101, traitmech:000092 | uv run pytest tests/test_curate_stage5_review_findings.py -v passed all 6 tests, including the Cycle 11 baseline-prune guard. |
| Strict LinkML validation | passed | True | traitmech:000096, traitmech:000094, traitmech:000097, traitmech:000098, traitmech:000089, traitmech:000102, traitmech:000090, traitmech:000100, traitmech:000091, traitmech:000095, traitmech:000101, traitmech:000092 | just validate-all validated 1130 TraitRecord YAML files with 0 ERROR rows. |
| Evidence snippet ratchet audit | passed | True | traitmech:000096, traitmech:000094, traitmech:000097, traitmech:000098, traitmech:000089, traitmech:000102, traitmech:000090, traitmech:000100, traitmech:000091, traitmech:000095, traitmech:000101, traitmech:000092 | just audit-snippets reported 2337 findings, all baselined, with new: 0 and blocking: 0 after pruning the 12 resolved rows. |
| Trait page regeneration | passed | True | traitmech:000096, traitmech:000094, traitmech:000097, traitmech:000098, traitmech:000089, traitmech:000102, traitmech:000090, traitmech:000100, traitmech:000091, traitmech:000095, traitmech:000101, traitmech:000092 | just gen-pages rendered 1130 trait pages plus category, index, browse, graph, map, sequence-map, and UMAP pages at 100.0% coverage. |

## Scientific And Domain Assessments

### Cycle 11 definition_source snippet remediation

evidence: supported. Targets: traitmech:000096, traitmech:000094, traitmech:000097, traitmech:000098, traitmech:000089, traitmech:000102, traitmech:000090, traitmech:000100, traitmech:000091, traitmech:000095, traitmech:000101, traitmech:000092.

All 12 Cycle 11 open definition_source MISSING_SNIPPET findings are resolved on the reviewed target records.

### Closed-schema validation after writer application

schema: supported. Targets: traitmech:000096, traitmech:000094, traitmech:000097, traitmech:000098, traitmech:000089, traitmech:000102, traitmech:000090, traitmech:000100, traitmech:000091, traitmech:000095, traitmech:000101, traitmech:000092.

The 12 edited TraitRecord files validate under strict LinkML validation as part of the 1130-file corpus.

## Findings

### F-C11S4-DEF-SRC-001: codon_usage_bias.yaml record-level definition_source DOI:10.1038/nrg2899 now carries a verified snippet

minor / resolved / confirmed; issue key: codon-usage-bias-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1038/nrg2899 on data/traits/genomics/codon_usage_bias.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/codon_usage_bias.yaml.

### F-C11S4-DEF-SRC-002: crispr_cas_system.yaml record-level definition_source DOI:10.1038/s41579-019-0299-x now carries a verified snippet

minor / resolved / confirmed; issue key: crispr-cas-system-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1038/s41579-019-0299-x on data/traits/genomics/crispr_cas_system.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/crispr_cas_system.yaml.

### F-C11S4-DEF-SRC-003: gc_skew.yaml record-level definition_source DOI:10.1093/oxfordjournals.molbev.a025626 now carries a verified snippet

minor / resolved / confirmed; issue key: gc-skew-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1093/oxfordjournals.molbev.a025626 on data/traits/genomics/gc_skew.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/gc_skew.yaml.

### F-C11S4-DEF-SRC-004: genome_size.yaml record-level definition_source DOI:10.1038/nrmicro3331 now carries a verified snippet

minor / resolved / confirmed; issue key: genome-size-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1038/nrmicro3331 on data/traits/genomics/genome_size.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/genome_size.yaml.

### F-C11S4-DEF-SRC-005: mobile_genetic_element.yaml record-level definition_source DOI:10.1038/nrmicro1235 now carries a verified snippet

minor / resolved / confirmed; issue key: mobile-genetic-element-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1038/nrmicro1235 on data/traits/genomics/mobile_genetic_element.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/mobile_genetic_element.yaml.

### F-C11S4-DEF-SRC-006: pangenome_openness.yaml record-level definition_source DOI:10.1073/pnas.0506758102 now carries a verified snippet

minor / resolved / confirmed; issue key: pangenome-openness-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1073/pnas.0506758102 on data/traits/genomics/pangenome_openness.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/pangenome_openness.yaml.

### F-C11S4-DEF-SRC-007: plasmid_carriage.yaml record-level definition_source DOI:10.1128/MMBR.00020-10 now carries a verified snippet

minor / resolved / confirmed; issue key: plasmid-carriage-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1128/MMBR.00020-10 on data/traits/genomics/plasmid_carriage.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/plasmid_carriage.yaml.

### F-C11S4-DEF-SRC-008: ploidy.yaml record-level definition_source DOI:10.1159/000368855 now carries a verified snippet

minor / resolved / confirmed; issue key: ploidy-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1159/000368855 on data/traits/genomics/ploidy.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/ploidy.yaml.

### F-C11S4-DEF-SRC-009: prophage.yaml record-level definition_source DOI:10.1128/MMBR.67.2.238-276.2003 now carries a verified snippet

minor / resolved / confirmed; issue key: prophage-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1128/MMBR.67.2.238-276.2003 on data/traits/genomics/prophage.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/prophage.yaml.

### F-C11S4-DEF-SRC-010: restriction_modification_system.yaml record-level definition_source DOI:10.1128/MMBR.00044-12 now carries a verified snippet

minor / resolved / confirmed; issue key: restriction-modification-system-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1128/MMBR.00044-12 on data/traits/genomics/restriction_modification_system.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/restriction_modification_system.yaml.

### F-C11S4-DEF-SRC-011: rrna_operon_copy_number.yaml record-level definition_source DOI:10.1128/AEM.66.4.1328-1333.2000 now carries a verified snippet

minor / resolved / confirmed; issue key: rrna-operon-copy-number-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1128/AEM.66.4.1328-1333.2000 on data/traits/genomics/rrna_operon_copy_number.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/rrna_operon_copy_number.yaml.

### F-C11S4-DEF-SRC-012: transposable_element.yaml record-level definition_source DOI:10.1111/1574-6976.12067 now carries a verified snippet

minor / resolved / confirmed; issue key: transposable-element-definition-source-snippet.

Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1111/1574-6976.12067 on data/traits/genomics/transposable_element.yaml, pruned the exact record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history event via scripts/curate_stage5_review_findings.py.

Disposition: Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/transposable_element.yaml.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-stage4 | reviews/structured/20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review/review.yaml; F-C11S4-DEF-SRC-001..F-C11S4-DEF-SRC-012 | supports | Cycle 11 Stage 4 accepted the 12 genomics definition_source missing-snippet findings and their planned Stage 5 remediations. |
| ev-stage5-writer | scripts/curate_stage5_review_findings.py; CYCLE11_TIMESTAMP and F-C11S4-DEF-SRC-001..F-C11S4-DEF-SRC-012 | supports | The guarded Stage 5 writer contains exact Cycle 11 specs for all 12 findings, appends ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history events, and prunes only exact evidence[0] MISSING_SNIPPET rows from conf/evidence_snippet_baseline.tsv. |
| ev-target-records | data/traits/genomics/codon_usage_bias.yaml, data/traits/genomics/crispr_cas_system.yaml, data/traits/genomics/gc_skew.yaml, data/traits/genomics/genome_size.yaml, data/traits/genomics/mobile_genetic_element.yaml, data/traits/genomics/pangenome_openness.yaml, data/traits/genomics/plasmid_carriage.yaml, data/traits/genomics/ploidy.yaml, data/traits/genomics/prophage.yaml, data/traits/genomics/restriction_modification_system.yaml, data/traits/genomics/rrna_operon_copy_number.yaml, data/traits/genomics/transposable_element.yaml; evidence[0].snippet; curation_history[-1] | supports | Every remediated genomics record now carries a record-level definition_source evidence snippet matching the accepted Stage 4 Europe PMC quote and a Cycle 11 Stage 5 curation_history event. |
| ev-baseline | conf/evidence_snippet_baseline.tsv; evidence[0] MISSING_SNIPPET rows for the 12 Cycle 11 genomics targets | supports | The 12 resolved record-level evidence[0] MISSING_SNIPPET rows for the Cycle 11 genomics targets are absent while edge-level baselined rows for the same files remain in place. |
| ev-strict-validation | just validate-all | supports | Strict closed-schema validation passed across all 1130 trait YAML files. |
| ev-snippet-audit | just audit-snippets | supports | Evidence snippet audit passed with 0 new and 0 blocking rows against the updated baseline. |

## Limits And Additional Notes


## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T041700Z-cycle11-stage5-remediated-records-review
kind: batch
repository: CultureBotAI/TraitMech
title: Cycle 11 Stage 5 post-remediation verification review of the 12 genomics TraitRecord
  files in group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
started_at: '2026-11-15T04:16:00Z'
finished_at: '2026-11-15T04:17:00Z'
reviewer:
  identity: codex
  kind: agent
  model: gpt-5-codex
  independence: self_review
  independence_basis: Repository-local post-remediation record review verifying resolution
    of the 12 Cycle 11 Stage 4 open findings (F-C11S4-DEF-SRC-001..F-C11S4-DEF-SRC-012)
    under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS (#2002); separate
    from independent PR adversarial review.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass
scientific_review: true
summary: 'Fresh post-remediation batch review of the 12 genomics TraitRecord YAML
  files remediated in Cycle 11 Stage 5 under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
  and GitHub issue #2002. All 12 Cycle 11 Stage 4 open findings (F-C11S4-DEF-SRC-001..012)
  are verified as resolved with contiguous verbatim snippets for their primary definition_source
  DOI in record-level evidence[0], removal of all 12 baselined MISSING_SNIPPET rows
  from conf/evidence_snippet_baseline.tsv (2,349 -> 2,337 total baselined findings),
  append-only curation_history provenance, and 0 remaining open findings.'
source:
  git_revision: 2ccbc22ccfb8bd00c9d9ca70e11e020f818fbc18
  state: working_tree
  inputs:
  - path: data/traits/genomics/codon_usage_bias.yaml
    sha256: 644676f3577290b5b4910c38d0472abf2ea68ae63b6670e8ea82c34f0b6b2067
    role: target
  - path: data/traits/genomics/crispr_cas_system.yaml
    sha256: 194a825c6914a168046f45e10617a3fff30c3364f8c2ad9db7b60ea3d101ea6f
    role: target
  - path: data/traits/genomics/gc_skew.yaml
    sha256: 4ef5e1a58a3594501a2c027b958ff59c39bc66152150963f8447bb6df812426e
    role: target
  - path: data/traits/genomics/genome_size.yaml
    sha256: d61b763cdcb7fd7dd87fbac9a4cde882264c6d313cdf24e8440e54a56357ae90
    role: target
  - path: data/traits/genomics/mobile_genetic_element.yaml
    sha256: 7a402cde3b660bdf768bc87d548349c415593e09fed35d5f57e528067d722d2c
    role: target
  - path: data/traits/genomics/pangenome_openness.yaml
    sha256: f887f38359ab836831c2fddb5782d0bea04046eb8fe59f233608f4955e08b879
    role: target
  - path: data/traits/genomics/plasmid_carriage.yaml
    sha256: c0f2d1143a858271fb01cd9506c9124986ba2bac57c70d72c1a661a76509e59a
    role: target
  - path: data/traits/genomics/ploidy.yaml
    sha256: 9caef72a19f21ea8b73984293cf0fbee144ebc03b13a6aa9abac7fb622c13b2f
    role: target
  - path: data/traits/genomics/prophage.yaml
    sha256: dfac359abec5533a3ca44f8750937e2b1d1d4bef99630d6b1483cc1d0270ea3c
    role: target
  - path: data/traits/genomics/restriction_modification_system.yaml
    sha256: 1476898fbd66d75f1c4583cc01a5937a5dc3c910225939dcd5810ece29f73fcc
    role: target
  - path: data/traits/genomics/rrna_operon_copy_number.yaml
    sha256: 5394fc28d8d9e9767021067b94d22f8f7986ed8d5c8303a2f8220c84b6a1f34d
    role: target
  - path: data/traits/genomics/transposable_element.yaml
    sha256: 1415bfaa74ec90821eae6e1ea0132adafe351802d410db0d34cc263cbec18306
    role: target
  - path: .claude/skills/curate-yaml-record/SKILL.md
    sha256: 27f535d3f057d321c8b87c6506f2f35dd2d37fd005bcd5040b3e17269285075b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: bb03efa3bbd3748ee1dccf57612a6ce8fcc861f20eb57c33eb16e3ac1dd728bd
    role: context
  - path: AGENTS.md
    sha256: 6771ed07ef5ae68deecbf50ae6123e2e3a4834e05b2dbc13faa96ec2329a6f93
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: conf/evidence_snippet_baseline.tsv
    sha256: 20fbe6e481ddd78c18cf23443a21e36cf34a8a35ae1e7e2081e5a7e6b767039c
    role: context
  - path: conf/record_review.yaml
    sha256: 5adc6244761fb2baf8a059d81f23b0c9b32a33f9426ab84094234c3ec417269d
    role: context
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: reviews/structured/20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review/review.yaml
    sha256: 49062de9bd3998348e20ccdefbdeadb1ef749359d2d8340b02f48740f960a840
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/evidence.yaml
    sha256: 498792fbeb04a862b662df0d62635742a9abf511e8ef7808f3bac9379595393a
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/curate_stage5_review_findings.py
    sha256: 531d7d67ee8bdf1f5ffc0984751755420d1f885518dae056229c07487885eb8a
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: tests/test_curate_stage5_review_findings.py
    sha256: 1286797a72d605489f1e6465f7f0a9883f47969b7e5a993619b717777dd0d863
    role: context
scope:
  description: Focused post-remediation review of all 12 genomics TraitRecord YAML
    files modified in Cycle 11 Stage 5 to resolve group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    (#2002).
  selection: All 12 records with open findings carried forward from Cycle 11 Stage
    4 review 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review.
  coverage: full
  population_size: 12
  reviewed_target_ids:
  - traitmech:000096
  - traitmech:000094
  - traitmech:000097
  - traitmech:000098
  - traitmech:000089
  - traitmech:000102
  - traitmech:000090
  - traitmech:000100
  - traitmech:000091
  - traitmech:000095
  - traitmech:000101
  - traitmech:000092
  sampling_method: Exhaustive review of every remediated Cycle 11 Stage 5 target.
targets:
- target_id: traitmech:000096
  path: data/traits/genomics/codon_usage_bias.yaml
  label: codon usage bias
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 644676f3577290b5b4910c38d0472abf2ea68ae63b6670e8ea82c34f0b6b2067
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/codon_usage_bias.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
- target_id: traitmech:000094
  path: data/traits/genomics/crispr_cas_system.yaml
  label: CRISPR-Cas system
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 194a825c6914a168046f45e10617a3fff30c3364f8c2ad9db7b60ea3d101ea6f
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/crispr_cas_system.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
- target_id: traitmech:000097
  path: data/traits/genomics/gc_skew.yaml
  label: GC skew
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 4ef5e1a58a3594501a2c027b958ff59c39bc66152150963f8447bb6df812426e
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gc_skew.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
- target_id: traitmech:000098
  path: data/traits/genomics/genome_size.yaml
  label: genome size
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: d61b763cdcb7fd7dd87fbac9a4cde882264c6d313cdf24e8440e54a56357ae90
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/genome_size.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
- target_id: traitmech:000089
  path: data/traits/genomics/mobile_genetic_element.yaml
  label: mobile genetic element
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 7a402cde3b660bdf768bc87d548349c415593e09fed35d5f57e528067d722d2c
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/mobile_genetic_element.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
- target_id: traitmech:000102
  path: data/traits/genomics/pangenome_openness.yaml
  label: pangenome openness
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: f887f38359ab836831c2fddb5782d0bea04046eb8fe59f233608f4955e08b879
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/pangenome_openness.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
- target_id: traitmech:000090
  path: data/traits/genomics/plasmid_carriage.yaml
  label: plasmid carriage
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: c0f2d1143a858271fb01cd9506c9124986ba2bac57c70d72c1a661a76509e59a
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/plasmid_carriage.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
- target_id: traitmech:000100
  path: data/traits/genomics/ploidy.yaml
  label: ploidy
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 9caef72a19f21ea8b73984293cf0fbee144ebc03b13a6aa9abac7fb622c13b2f
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/ploidy.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
- target_id: traitmech:000091
  path: data/traits/genomics/prophage.yaml
  label: prophage
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: dfac359abec5533a3ca44f8750937e2b1d1d4bef99630d6b1483cc1d0270ea3c
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/prophage.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
- target_id: traitmech:000095
  path: data/traits/genomics/restriction_modification_system.yaml
  label: restriction-modification system
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1476898fbd66d75f1c4583cc01a5937a5dc3c910225939dcd5810ece29f73fcc
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/restriction_modification_system.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
- target_id: traitmech:000101
  path: data/traits/genomics/rrna_operon_copy_number.yaml
  label: rRNA operon copy number
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 5394fc28d8d9e9767021067b94d22f8f7986ed8d5c8303a2f8220c84b6a1f34d
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/rrna_operon_copy_number.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
- target_id: traitmech:000092
  path: data/traits/genomics/transposable_element.yaml
  label: transposable element
  record_class: TraitRecord
  kind: maintained
  semantic_digest:
    algorithm: sha256
    sha256: 1415bfaa74ec90821eae6e1ea0132adafe351802d410db0d34cc263cbec18306
    description: SHA256 of the post-remediation TraitRecord YAML reviewed after scripts/curate_stage5_review_findings.py
      --apply.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/transposable_element.yaml
    role: Curated TraitRecord updated by the guarded Stage 5 writer.
checks:
- check_id: stage5-writer-idempotent
  name: Stage 5 guarded writer idempotency
  status: passed
  required: true
  summary: just curate-stage5-review-findings reported 127 resolved specs, 0 files
    updated, and 0 baseline rows pruned after apply.
  target_ids:
  - traitmech:000096
  - traitmech:000094
  - traitmech:000097
  - traitmech:000098
  - traitmech:000089
  - traitmech:000102
  - traitmech:000090
  - traitmech:000100
  - traitmech:000091
  - traitmech:000095
  - traitmech:000101
  - traitmech:000092
  command: just curate-stage5-review-findings
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-stage5-writer
- check_id: stage5-writer-tests
  name: Stage 5 writer focused tests
  status: passed
  required: true
  summary: uv run pytest tests/test_curate_stage5_review_findings.py -v passed all
    6 tests, including the Cycle 11 baseline-prune guard.
  target_ids:
  - traitmech:000096
  - traitmech:000094
  - traitmech:000097
  - traitmech:000098
  - traitmech:000089
  - traitmech:000102
  - traitmech:000090
  - traitmech:000100
  - traitmech:000091
  - traitmech:000095
  - traitmech:000101
  - traitmech:000092
  command: uv run pytest tests/test_curate_stage5_review_findings.py -v
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-stage5-writer
- check_id: strict-validation
  name: Strict LinkML validation
  status: passed
  required: true
  summary: just validate-all validated 1130 TraitRecord YAML files with 0 ERROR rows.
  target_ids:
  - traitmech:000096
  - traitmech:000094
  - traitmech:000097
  - traitmech:000098
  - traitmech:000089
  - traitmech:000102
  - traitmech:000090
  - traitmech:000100
  - traitmech:000091
  - traitmech:000095
  - traitmech:000101
  - traitmech:000092
  command: just validate-all
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-strict-validation
- check_id: evidence-snippet-audit
  name: Evidence snippet ratchet audit
  status: passed
  required: true
  summary: 'just audit-snippets reported 2337 findings, all baselined, with new: 0
    and blocking: 0 after pruning the 12 resolved rows.'
  target_ids:
  - traitmech:000096
  - traitmech:000094
  - traitmech:000097
  - traitmech:000098
  - traitmech:000089
  - traitmech:000102
  - traitmech:000090
  - traitmech:000100
  - traitmech:000091
  - traitmech:000095
  - traitmech:000101
  - traitmech:000092
  command: just audit-snippets
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-baseline
  - ev-snippet-audit
- check_id: rendered-pages
  name: Trait page regeneration
  status: passed
  required: true
  summary: just gen-pages rendered 1130 trait pages plus category, index, browse,
    graph, map, sequence-map, and UMAP pages at 100.0% coverage.
  target_ids:
  - traitmech:000096
  - traitmech:000094
  - traitmech:000097
  - traitmech:000098
  - traitmech:000089
  - traitmech:000102
  - traitmech:000090
  - traitmech:000100
  - traitmech:000091
  - traitmech:000095
  - traitmech:000101
  - traitmech:000092
  command: just gen-pages
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-target-records
evidence:
- evidence_id: ev-stage4
  kind: prior_review
  reference: reviews/structured/20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review/review.yaml
  locator: F-C11S4-DEF-SRC-001..F-C11S4-DEF-SRC-012
  accessed_at: '2026-11-15T04:17:00Z'
  support: supports
  summary: Cycle 11 Stage 4 accepted the 12 genomics definition_source missing-snippet
    findings and their planned Stage 5 remediations.
  snapshot_sha256: 49062de9bd3998348e20ccdefbdeadb1ef749359d2d8340b02f48740f960a840
- evidence_id: ev-stage5-writer
  kind: record_content
  reference: scripts/curate_stage5_review_findings.py
  locator: CYCLE11_TIMESTAMP and F-C11S4-DEF-SRC-001..F-C11S4-DEF-SRC-012
  accessed_at: '2026-11-15T04:17:00Z'
  support: supports
  summary: The guarded Stage 5 writer contains exact Cycle 11 specs for all 12 findings,
    appends ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history events, and
    prunes only exact evidence[0] MISSING_SNIPPET rows from conf/evidence_snippet_baseline.tsv.
  snapshot_sha256: 531d7d67ee8bdf1f5ffc0984751755420d1f885518dae056229c07487885eb8a
- evidence_id: ev-target-records
  kind: record_content
  reference: data/traits/genomics/codon_usage_bias.yaml, data/traits/genomics/crispr_cas_system.yaml,
    data/traits/genomics/gc_skew.yaml, data/traits/genomics/genome_size.yaml, data/traits/genomics/mobile_genetic_element.yaml,
    data/traits/genomics/pangenome_openness.yaml, data/traits/genomics/plasmid_carriage.yaml,
    data/traits/genomics/ploidy.yaml, data/traits/genomics/prophage.yaml, data/traits/genomics/restriction_modification_system.yaml,
    data/traits/genomics/rrna_operon_copy_number.yaml, data/traits/genomics/transposable_element.yaml
  locator: evidence[0].snippet; curation_history[-1]
  accessed_at: '2026-11-15T04:17:00Z'
  support: supports
  summary: Every remediated genomics record now carries a record-level definition_source
    evidence snippet matching the accepted Stage 4 Europe PMC quote and a Cycle 11
    Stage 5 curation_history event.
- evidence_id: ev-baseline
  kind: record_content
  reference: conf/evidence_snippet_baseline.tsv
  locator: evidence[0] MISSING_SNIPPET rows for the 12 Cycle 11 genomics targets
  accessed_at: '2026-11-15T04:17:00Z'
  support: supports
  summary: The 12 resolved record-level evidence[0] MISSING_SNIPPET rows for the Cycle
    11 genomics targets are absent while edge-level baselined rows for the same files
    remain in place.
  snapshot_sha256: 20fbe6e481ddd78c18cf23443a21e36cf34a8a35ae1e7e2081e5a7e6b767039c
- evidence_id: ev-strict-validation
  kind: validation
  reference: just validate-all
  accessed_at: '2026-11-15T04:17:00Z'
  support: supports
  summary: Strict closed-schema validation passed across all 1130 trait YAML files.
- evidence_id: ev-snippet-audit
  kind: validation
  reference: just audit-snippets
  accessed_at: '2026-11-15T04:17:00Z'
  support: supports
  summary: Evidence snippet audit passed with 0 new and 0 blocking rows against the
    updated baseline.
assessments:
- assessment_id: all-c11-findings-resolved
  area: evidence
  topic: Cycle 11 definition_source snippet remediation
  outcome: supported
  summary: All 12 Cycle 11 open definition_source MISSING_SNIPPET findings are resolved
    on the reviewed target records.
  target_ids:
  - traitmech:000096
  - traitmech:000094
  - traitmech:000097
  - traitmech:000098
  - traitmech:000089
  - traitmech:000102
  - traitmech:000090
  - traitmech:000100
  - traitmech:000091
  - traitmech:000095
  - traitmech:000101
  - traitmech:000092
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  - ev-snippet-audit
  metrics:
  - name: resolved_findings
    value: 12
    unit: findings
    definition: Cycle 11 Stage 4 open findings resolved in Stage 5.
    denominator: 12
    minimum: 0
    maximum: 12
- assessment_id: post-remediation-validation
  area: schema
  topic: Closed-schema validation after writer application
  outcome: supported
  summary: The 12 edited TraitRecord files validate under strict LinkML validation
    as part of the 1130-file corpus.
  target_ids:
  - traitmech:000096
  - traitmech:000094
  - traitmech:000097
  - traitmech:000098
  - traitmech:000089
  - traitmech:000102
  - traitmech:000090
  - traitmech:000100
  - traitmech:000091
  - traitmech:000095
  - traitmech:000101
  - traitmech:000092
  evidence_ids:
  - ev-strict-validation
findings:
- finding_id: F-C11S4-DEF-SRC-001
  issue_key: codon-usage-bias-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: codon_usage_bias.yaml record-level definition_source DOI:10.1038/nrg2899
    now carries a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1038/nrg2899
    on data/traits/genomics/codon_usage_bias.yaml, pruned the exact record-level MISSING_SNIPPET
    baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history
    event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000096
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/codon_usage_bias.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/codon_usage_bias.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-001
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
- finding_id: F-C11S4-DEF-SRC-002
  issue_key: crispr-cas-system-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: crispr_cas_system.yaml record-level definition_source DOI:10.1038/s41579-019-0299-x
    now carries a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1038/s41579-019-0299-x
    on data/traits/genomics/crispr_cas_system.yaml, pruned the exact record-level
    MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE
    curation_history event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000094
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/crispr_cas_system.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/crispr_cas_system.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-002
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
- finding_id: F-C11S4-DEF-SRC-003
  issue_key: gc-skew-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: gc_skew.yaml record-level definition_source DOI:10.1093/oxfordjournals.molbev.a025626
    now carries a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1093/oxfordjournals.molbev.a025626
    on data/traits/genomics/gc_skew.yaml, pruned the exact record-level MISSING_SNIPPET
    baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history
    event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000097
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/gc_skew.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/gc_skew.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-003
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
- finding_id: F-C11S4-DEF-SRC-004
  issue_key: genome-size-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: genome_size.yaml record-level definition_source DOI:10.1038/nrmicro3331 now
    carries a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1038/nrmicro3331
    on data/traits/genomics/genome_size.yaml, pruned the exact record-level MISSING_SNIPPET
    baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history
    event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000098
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/genome_size.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/genome_size.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-004
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
- finding_id: F-C11S4-DEF-SRC-005
  issue_key: mobile-genetic-element-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: mobile_genetic_element.yaml record-level definition_source DOI:10.1038/nrmicro1235
    now carries a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1038/nrmicro1235
    on data/traits/genomics/mobile_genetic_element.yaml, pruned the exact record-level
    MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE
    curation_history event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000089
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/mobile_genetic_element.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/mobile_genetic_element.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-005
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
- finding_id: F-C11S4-DEF-SRC-006
  issue_key: pangenome-openness-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: pangenome_openness.yaml record-level definition_source DOI:10.1073/pnas.0506758102
    now carries a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1073/pnas.0506758102
    on data/traits/genomics/pangenome_openness.yaml, pruned the exact record-level
    MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE
    curation_history event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000102
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/pangenome_openness.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/pangenome_openness.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-006
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
- finding_id: F-C11S4-DEF-SRC-007
  issue_key: plasmid-carriage-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: plasmid_carriage.yaml record-level definition_source DOI:10.1128/MMBR.00020-10
    now carries a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1128/MMBR.00020-10
    on data/traits/genomics/plasmid_carriage.yaml, pruned the exact record-level MISSING_SNIPPET
    baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history
    event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000090
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/plasmid_carriage.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/plasmid_carriage.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-007
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
- finding_id: F-C11S4-DEF-SRC-008
  issue_key: ploidy-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: ploidy.yaml record-level definition_source DOI:10.1159/000368855 now carries
    a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1159/000368855
    on data/traits/genomics/ploidy.yaml, pruned the exact record-level MISSING_SNIPPET
    baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history
    event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000100
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/ploidy.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/ploidy.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-008
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
- finding_id: F-C11S4-DEF-SRC-009
  issue_key: prophage-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: prophage.yaml record-level definition_source DOI:10.1128/MMBR.67.2.238-276.2003
    now carries a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1128/MMBR.67.2.238-276.2003
    on data/traits/genomics/prophage.yaml, pruned the exact record-level MISSING_SNIPPET
    baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE curation_history
    event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000091
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/prophage.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/prophage.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-009
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
- finding_id: F-C11S4-DEF-SRC-010
  issue_key: restriction-modification-system-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: restriction_modification_system.yaml record-level definition_source DOI:10.1128/MMBR.00044-12
    now carries a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1128/MMBR.00044-12
    on data/traits/genomics/restriction_modification_system.yaml, pruned the exact
    record-level MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE
    curation_history event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000095
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/restriction_modification_system.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/restriction_modification_system.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-010
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
- finding_id: F-C11S4-DEF-SRC-011
  issue_key: rrna-operon-copy-number-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: rrna_operon_copy_number.yaml record-level definition_source DOI:10.1128/AEM.66.4.1328-1333.2000
    now carries a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1128/AEM.66.4.1328-1333.2000
    on data/traits/genomics/rrna_operon_copy_number.yaml, pruned the exact record-level
    MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE
    curation_history event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000101
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/rrna_operon_copy_number.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/rrna_operon_copy_number.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-011
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
- finding_id: F-C11S4-DEF-SRC-012
  issue_key: transposable-element-definition-source-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: transposable_element.yaml record-level definition_source DOI:10.1111/1574-6976.12067
    now carries a verified snippet
  description: Cycle 11 Stage 5 populated evidence[0].snippet for DOI:10.1111/1574-6976.12067
    on data/traits/genomics/transposable_element.yaml, pruned the exact record-level
    MISSING_SNIPPET baseline row, and appended an ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE
    curation_history event via scripts/curate_stage5_review_findings.py.
  target_ids:
  - traitmech:000092
  field_paths:
  - evidence[0].snippet
  - curation_history[-1]
  evidence_ids:
  - ev-stage4
  - ev-stage5-writer
  - ev-target-records
  - ev-baseline
  rule_id: MISSING_SNIPPET
  native_severity: minor
  normalization_reason: Cycle 11 Stage 4 normalized record-level missing definition_source
    snippets to minor evidence findings.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/genomics/transposable_element.yaml
    role: Post-remediation TraitRecord evidence[0] owner.
  - repository: CultureBotAI/TraitMech
    path: conf/evidence_snippet_baseline.tsv
    role: Baseline row owner for the resolved audit finding.
  disposition_reason: 'Resolved under group G-C11S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS
    and GitHub issue #2002 by adding the verified snippet to data/traits/genomics/transposable_element.yaml.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
    finding_id: F-C11S4-DEF-SRC-012
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/2002
  tags:
  - cycle11
  - stage5
  - definition_source
actions: []
limitations: []
related_reviews:
- repository: CultureBotAI/TraitMech
  review_id: 20261105T102500Z-cycle11-stage4-corpus-record-and-cohort-review
  relationship: resolves open findings from
links:
- https://github.com/CultureBotAI/TraitMech/issues/2002
tags:
- cycle11
- stage5
- post_remediation
```
