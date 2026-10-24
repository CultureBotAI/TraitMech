# Evidence and ontology review of aerotolerance (METPO:1000609)

- Review: 20261021T083011Z-aerotolerant
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T08:24:05Z
- Finished UTC: 2026-10-21T08:30:11Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The aerotolerant identity, definition, parent and current ontology/taxon identifiers are sound. One major finding groups five relation-semantic conflicts; two minor findings concern conditional Lactococcus example scope and a bounded missing human-acceptance link. All eleven nodes and eight edges were assessed. Four of six quotations are exact, one is a faithful table composite and one remains unverified because the source body was inaccessible.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Second batch004 target in lexicographic path order after aerobic was validated and saved. Whole target read before native capture. Supplemental owner captures retained all earlier input hashes unchanged; scientific review covers one complete record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000609 | data/traits/environment/aerotolerant.yaml | maintained | aerotolerant |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000609 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000609 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000609 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1000609 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000609 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000609 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000609 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1000609 | The selected record validates. |
| Focused strict validation | passed | True | METPO:1000609 | One file scanned; zero strict errors. |
| Focused snippet verification | passed | True | METPO:1000609 | The DOI/PMID recipe checked five snippets: three VERIFIED and two NOT_IN_ABSTRACT. The URL-based definition excerpt was checked manually. Across all six occurrences, four are exact, one is a faithful ellipsized table composite and one remains unverified. |
| Structured-source runner availability | unavailable | False | METPO:1000609 | Original bounded discovery reused; official catalog fallback inspected. |
| Lactococcus expression-source applicability | not_applicable | False | METPO:1000609 | No matching dataset in the inspected catalog; no substitute organism or negative phenotype inference. |

## Scientific And Domain Assessments

### Native checklist: identifier, definition, synonym and parent

identity: supported. Targets: METPO:1000609.

Active METPO1000609 and parent1000601 match. The definition source and related synonym directly support the nonrespiring oxygen-tolerant class.

### Native checklist: category, class and NONMECHANISTIC context

representation: supported. Targets: METPO:1000609.

ENVIRONMENT/CLASS and contextual NONMECHANISTIC scope fit. Optional protein instances, datasets and universal mechanisms are not missing requirements.

### Native checklist: canonical examples and contextual organism quotation

evidence: concern. Targets: METPO:1000609.

Both canonical taxon identities resolve. Streptococcus introductory phenotype context supports the example. Lactococcus fermentative membership is plausible but needs conditions in light of the cited respiratory-capacity result. The separate C. perfringens quotation remains unverified.

### Native checklist: current term identity and historical corrections

grounding: supported. Targets: METPO:1000609.

Current GO/CHEBI/InterPro terms match intended functional, process, chemical and family meanings. GO activity groundings do not automatically retype described enzyme actors. Historical withdrawn IDs are not current errors.

### Native checklist: eleven nodes and eight grounded or free-text edges

consistency: concern. Targets: METPO:1000609.

Five relations conflate trait facets with whole-part structure, a trait with a process object, or chemical consumption with process regulation. Catalase enabling a detoxification process and provisional mitigates have compatible contextual roles.

### Native checklist: all eight edge claims and source contexts

evidence: supported. Targets: METPO:1000609.

The table and general source passages support the contextual biological descriptions. Correlation, anammox physiology and cell-free enzyme assays retain their limits; they are not universal causal proof. Ontology relation errors are assessed separately from source support.

### Native checklist: all six snippet occurrences

evidence: unknown. Targets: METPO:1000609.

Four excerpts are exact, one is a faithful explicitly ellipsized table composite and one is unverified due to inaccessible body text. No false-quote finding is inferred from source-access failure.

### Native checklist: structure and optional evidence surfaces

completeness: supported. Targets: METPO:1000609.

All nodes and edge endpoints resolve and required identity/evidence surfaces are present. The graph’s contextual disposition does not demand one token accession per enzyme or every possible defense pathway.

### Native checklist: optional Lactococcus dataset coverage

evidence: supported. Targets: METPO:1000609.

Catalog coverage is not applicable for the scoped Lactococcus example. No other organism was substituted and missing coverage is not treated as biological absence.

### Native checklist: AI disclosure, writer recurrence and human acceptance

provenance: concern. Targets: METPO:1000609.

AI assistance is explicit. Wildcard mappings can reproduce semantic mistakes when filling empty IDs; already grounded edges require separate correction. Human acceptance is not linked within the bounded inspected local provenance.

## Findings

### external-relation-semantics: Five relation mappings conflict with the represented endpoint meanings

major / open / confirmed; issue key: aerotolerant-external-relation-semantics.

Edge0 maps a conceptual trait/growth facet to material/process whole-part semantics. Edge2 gives RO contributes-to a trait object despite its inherited process range. Edges5–7 map protein-to-chemical decreases to RO process regulation. Biolink formal endpoints remain named thing; native validation passes and no formal reasoner failure is claimed.

### example-condition-scope: Lactococcus example needs its fermentative condition scope

minor / open / confirmed; issue key: aerotolerant-example-condition-scope.

The note already calls L. lactis a fermenter, but its cited source explicitly demonstrates conditional respiratory capacity. Qualify the canonical example so the definition is not read as a species-wide inability to use oxygen. This does not make the species an impossible example or contradict its fermentative aerotolerance.

### human-acceptance-link: Human scientific acceptance is not linked locally

minor / open / confirmed; issue key: aerotolerant-human-acceptance-link.

Seventeen AI-assisted events and one seed are explicit, but the bounded inspected target and local provenance contain no acceptance link identifying this record revision. Remote/private approval remains unknown.

## Recommended Actions And Acceptance Checks

### repair-relations

In separately authorized curation, reconcile the five predicate meanings with their actual endpoint roles and review the wildcard mapping decisions for recurrence while preserving supported source scope.

- Inspect inherited RO constraints and Biolink textual semantics separately from permissive formal endpoints.
- Keep described enzyme actors distinct from their allowed GO activity-facet groundings.
- Use the maintained ground-predicates dry run to review recurrence; it cannot overwrite the existing nonempty IDs.
- Run focused strict and graph checks plus just qc after authorized correction; append native history and regenerate affected maintained products.

### qualify-example

Retain the Lactococcus fermentative example with explicit condition/evidence scope rather than asserting a species-wide inability to respire.

- The note distinguishes the documented fermentative state from conditional respiration in the same cited study.
- No unsupported phenotype, strain equivalence or new experimental recipe is introduced.
- Run focused record validation after any authorized edit.

### link-acceptance

Locate and link existing human scientific acceptance or obtain it through the established process; preserve AI history and reassess status if acceptance remains unavailable.

- Acceptance identifies the record revision and scientific scope.
- Automated validation and AI provenance are not presented as human approval.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-aerotolerant-validate | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/aerotolerant-validate.log; Executed 2026-10-21T08:24:45Z through 2026-10-21T08:24:46Z; metadata aerotolerant-validate.json | context_only | The selected record validates. |
| check-aerotolerant-strict | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/aerotolerant-strict.log; Executed 2026-10-21T08:24:45Z through 2026-10-21T08:24:47Z; metadata aerotolerant-strict.json | context_only | One file scanned; zero strict errors. |
| check-aerotolerant-snippets | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/aerotolerant-snippets.log; Executed 2026-10-21T08:25:02Z through 2026-10-21T08:25:09Z; metadata aerotolerant-snippets.json | context_only | The DOI/PMID recipe checked five snippets: three VERIFIED and two NOT_IN_ABSTRACT. The URL-based definition excerpt was checked manually. Across all six occurrences, four are exact, one is a faithful ellipsized table composite and one remains unverified. |
| record | data/traits/environment/aerotolerant.yaml; Complete target: identity, definition, synonym, evidence, two canonical examples, eleven nodes, eight edges and eighteen events | partial | The aerotolerant concept is correctly identified. Five grounded relations have endpoint or meaning conflicts; one example needs conditional context and human acceptance is not linked in bounded local provenance. |
| shape | Complete parsed graph/history; All eleven nodes, eight edge endpoints and eighteen events | supports | No unresolved endpoints. Seventeen events disclose AI assistance and one records seeding. No pathway-context link is asserted. |
| identity | data/raw/metpo.owl; data/traits/environment/oxygen_preference.yaml; Active1000609 and broader1000601; complete exact-name/synonym scan | supports | Current identity, definition and parent match the pinned ontology. The related aerotolerant-anaerobe synonym has an independently cited teaching source. Obsolete matches have explicit replacement links only where actually recorded. |
| live-identifiers | QuickGO, InterPro, ChEBI and NCBI Taxonomy; Five current GO terms, IPR052364, CHEBI16240 and taxa1358/1314 | supports | GO0004784,0004096,0016692,0050137 are active activity terms and GO0042744 is active hydrogen-peroxide catabolism. InterPro resolves Rubrerythrin family; peroxide and both taxon labels match. The existing corrected GO term is assessed, not its historical predecessor. |
| reused-chemicals | Official ChEBI responses retained from aerobic review; CHEBI15379 and26523; original08:17:52Z accesses and verified hashes | supports | Dioxygen and reactive oxygen species match the current chemical nodes. Reuse preserves the original actual retrieval times and hashes. |
| ro | Read-only authoritative RO snapshot; Inherited relations for contributes-to, negative regulation and enables | partial | Contributes-to has a process range; negative regulation has process endpoints. The described enzyme actors are material despite allowed activity-facet groundings. Catalase enabling a detoxification process fits the material-actor/process roles. Original RO inspections08:04:46Z and07:58:06Z are retained with matching source hashes. |
| biolink | data/raw/biolink-model.yaml; has-part textual description and inherited slots | partial | Has-part describes material/process wholes and parts. A trait linked to a defining growth facet is not that same relation. Formal inherited endpoints are named thing; no enforced material-domain failure is claimed. |
| ledger | Independent documentary ontology audit; All eleven nodes and eight edges, zero-based indices | partial | Confirmed conflicts at edges0,2,5,6,7. Edge4 fits its described material actor and process object. Provisional mitigates accepts the represented contextual roles. GO activity facets, label-only context and replaced historical identifiers are not extra defects. |
| mapping-owners | mappings/predicate_grounding.tsv; mappings/node_grounding.tsv; proposals/metpo_traitmech_v2; Predicate rows10,39,61,76 and current node decisions | partial | Broad wildcard mappings assign contributes-to, negative-regulation and has-part without guarding the present semantic distinctions. Current protein-function and Rubrerythrin-family decisions follow native policy; mitigates is a documented provisional proposal. |
| writer | scripts/ground_causal_predicates.py; justfile; Writer contract and ground-predicates recipe | supports | The dry-run-by-default writer fills empty predicate identifiers from the mapping; it does not overwrite existing nonempty identifiers. Mapping repair alone therefore would not correct the existing target edges. Guarded record curation and mapping recurrence checks are distinct proposed steps. |
| policy | docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml; Legacy protein function-facet grounding and NONMECHANISTIC scope | supports | GO activity terms are allowed taxon-agnostic functional groundings for described enzyme actors. Broad contextual graphs do not require token protein instances, datasets or a single universally necessary defense mechanism. |
| definition | https://bio.libretexts.org/Courses/Ohio_State_University/Microbiology_Lab_SP25/05%3A_Lab_5/5.05%3A_Bacterial_Oxygen_Requirements; Conceptual oxygen-classification section, aerotolerant-anaerobes bullet | supports | The actual teaching page supports oxygen tolerance without oxygen use for ATP production and the related synonym. The short top-level quotation is exact. Laboratory procedures and unrelated categorical claims on the page were not used as evidence. |
| bibliography | Europe PMC and inspected primary/publisher sources; Nine citation identities, eight edge claims and all six snippets | partial | All nine identities resolve. Four snippets are exact, one is a faithful table composite and one is access-limited. Eighteen acquisition attempts include fourteen hashed responses; two API-error bodies are explicitly excluded. Two reused files retain original hashes/times. |
| lactococcus | https://pubmed.ncbi.nlm.nih.gov/11443085/; DOI10.1128/jb.183.15.4509-4516.2001; complete indexed abstract | partial | The source describes fermentative Lactococcus lactis but also demonstrates conditional respiratory capacity. The existing note already says fermenter; add the applicable context rather than declaring the species incapable of fermentative aerotolerance or treating inability to use oxygen as species-wide. |
| streptococcus | https://journals.asm.org/doi/10.1128/jb.182.19.5290-5299.2000; PMID10986229; actual publisher introductory phenotype paragraphs, browser lines88–90 | supports | Introductory fermentative and aerotolerant physiology supports the canonical example. The source uses facultative-anaerobe terminology for lactic-acid bacteria while describing fermentative metabolism; terminology alone is not a contradiction. Detailed pathogen defense routes and mutant mechanisms were not assessed. |
| perfringens | https://pubmed.ncbi.nlm.nih.gov/38864615/; DOI10.1128/mmbr.00140-23; metadata and publisher summary only | context_only | The reference and species context resolve, but the relative-aerotolerance quotation and its phenotype support remain unverified on the available source surfaces. Full-text failures, API-error response and challenge pages do not establish that the quote is false. No detailed pathogen biology was assessed. |
| classification | https://pmc.ncbi.nlm.nih.gov/articles/PMC3969821/; DOI10.1038/nrmicro2970; BioC Introduction offset1661 and Table1 offset37517 | supports | The introduction and table support aerotolerant anaerobes as oxygen-tolerating nonrespiring organisms with anaerobic growth. The excerpt combines row label and column headings with explicit ellipses; it is a faithful table composite, not continuous prose or proof of a formal part-whole relation. |
| oxygen-context | https://pmc.ncbi.nlm.nih.gov/articles/PMC9191689/; DOI10.1038/s41579-021-00583-y; newly acquired BioC abstract offset86 and Introduction offset4048 | supports | The short phrase is exact. The general introduction supplies oxygen-derived-stress context beyond the quoted phrase about joint toxicity. Only conceptual context was assessed, not detailed pathogen survival routes. |
| sod-association | https://pubmed.ncbi.nlm.nih.gov/326669/; DOI10.1128/iai.16.1.20-25.1977; abstract correlation and qualified conclusion sentences | partial | Both snippets are exact. The comparison covers twenty-two isolates and explicitly reports correlation with a usually-qualified inference. This supports the record’s qualified abundance association, not universal necessity or a reconstructed causal survival mechanism. |
| anammox-context | https://pmc.ncbi.nlm.nih.gov/articles/PMC10156729/; DOI10.1038/s43705-023-00251-7; Discussion Sec19 paragraph2, contextual Sec17 paragraph1 | partial | The general catalase and Rubrerythrin functional descriptions appear in the cited anammox source. Nearby text leaves individual cellular contributions uncertain. This supports contextual biochemical descriptions without proving a class-wide required mechanism. |
| peroxidase-context | https://pmc.ncbi.nlm.nih.gov/articles/PMC10457377/; DOI10.1038/s41598-023-41185-3; Introduction Sec1 equationEqub and paragraph7 | partial | The introductory reaction identity and analogous cofactor statement support generic contextual enzyme chemistry. The study concerns cell-free activities in two intestinal sulfate-reducing strains; it does not establish universal aerotolerance machinery. Experimental/kinetic optimization was not assessed. |
| provenance | Target fields and bounded local provenance; All eighteen events and ignored-inclusive exact identifier/path/slug search | partial | No explicit human scientific acceptance link for this target/revision was found in inspected local provenance. Matching migration histories disclose AI actors and contextual changes. Private or remote approval remains unknown. |
| status-rule | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md; Status/audit and Verification gate | supports | REVIEWED requires human scientific acceptance; AI curation and automated checks have different provenance roles. |
| expression | https://imodulondb.org/api/datasets; Original07:36:12Z catalog; bounded Lactococcus applicability check08:26:53Z | context_only | No Lactococcus lactis dataset matches the complete inspected catalog. Other lactobacilli were not substituted. No gene/module query or negative biological conclusion followed; detailed pathogen stress-defense queries were outside this expression scope. |
| runner | Reused structured-source runner discovery; Original bounded ignored-inclusive search08:17:15Z | context_only | No usable runner was found in the declared original PATH/install/project/B4 scope. The original receipt and catalog fallback are retained; no new or global runner absence is asserted. |

## Limits And Additional Notes

- The C. perfringens quotation and phenotype claim remain unverified on inspected abstract/summary surfaces; inaccessible body text does not establish falsity.
- Detailed pathogen survival, stress-defense and mutant mechanisms were not assessed or reconstructed. Streptococcus support is confined to introductory phenotype framing.
- The Streptococcus primary introduction was inspected through an actual publisher browser open without a local body hash; a separate BioC error response is excluded.
- Lactococcus and the comparative SOD study were checked from complete indexed abstracts. The former has condition-dependent physiology; the latter supports correlation with a usually qualifier, not universal necessity.
- The table excerpt is a row/header composite with explicit ellipses, not continuous prose. Its classification does not establish formal ontological parthood.
- Anammox and cell-free enzyme studies support contextual functional claims; individual cellular contributions and class-wide causal necessity remain unestablished.
- The teaching source was used only for its cited conceptual classification; laboratory instructions and unrelated generalizations were not adopted.
- GO activity terms are permitted enzyme-function facets. Described protein actors are not silently converted to process nodes, and chemical objects are not silently replaced by concentration-change processes.
- RO/CHEBI cache reuse retains original timestamps/hashes; local inspection does not certify a new ontology release.
- No Lactococcus dataset matches the inspected expression catalog; that is missing coverage, not negative biological evidence.
- Human acceptance outside the bounded local search remains unknown.
- No scientific record, schema, mapping, writer, status, history or generated page was changed.
- Field paths use zero-based indices.
- The initial native capture ran08:24:05Z, followed by supplemental owner capture08:24:17Z and writer/recipe capture08:28:22Z; all previously captured inputs stayed byte-identical.
- Current GO0042744 replaced a historical plant-pathway grounding; the withdrawn ID is not a present defect.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T083011Z-aerotolerant
kind: record
repository: CultureBotAI/TraitMech
title: Evidence and ontology review of aerotolerance (METPO:1000609)
started_at: '2026-10-21T08:24:05Z'
finished_at: '2026-10-21T08:30:11Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Current review session did not author or change the captured
    trait. Supporting agents inspected sources and prepared draft observations; root
    reviewer integrates and validates the final review. Historical Codex/Claude curation
    events are disclosed and are not human sign-off.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The aerotolerant identity, definition, parent and current ontology/taxon
  identifiers are sound. One major finding groups five relation-semantic conflicts;
  two minor findings concern conditional Lactococcus example scope and a bounded missing
  human-acceptance link. All eleven nodes and eight edges were assessed. Four of six
  quotations are exact, one is a faithful table composite and one remains unverified
  because the source body was inaccessible.
source:
  git_revision: 8eee04a8c65609fbaff6df7c54597dcaf1b9d282
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
    role: context
  - path: .claude/skills/manage-identifiers/SKILL.md
    sha256: a5c5aaa10943ee6d15423a5878ed2189e4e0b28a5c6e09fda80ba299ab779ebb
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: bb03efa3bbd3748ee1dccf57612a6ce8fcc861f20eb57c33eb16e3ac1dd728bd
    role: context
  - path: CLAUDE.md
    sha256: 4d328127022388e1affe9b71be24bc93944a971636d0d0ea902f6511e0b405c5
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: conf/evidence_snippet_baseline.tsv
    sha256: cbe5c82379e796446366b292f15194d80625b928119b482a67d857a379ab31a7
    role: context
  - path: data/raw/biolink-model.yaml
    sha256: 4955709e1cac1d26fd657f7a0c29d6c8390f42e41f9ebfab859c82b102f2bebb
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/environment/aerotolerant.yaml
    sha256: 4ae40096583868e5ab9b31f8aec3a81a09938faf24391f57a6a34b32b2efb3a8
    role: target
  - path: data/traits/environment/oxygen_preference.yaml
    sha256: 16829173ea947f2fef083f673c51519aad962d6812fcd54826ea86f055c5a40b
    role: context
  - path: docs/CURATION_PLAYBOOK.md
    sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
    role: context
  - path: docs/GROUNDING_POLICY.md
    sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
    role: context
  - path: docs/PATHWAY_LINKS.md
    sha256: 800492750fb3c025dfdf7164813e7a00b3bd72dc8cc6f8e754e2aed5d7bbf414
    role: context
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/infrastructure/disposition-typing-burndown/2026-08-08T030032Z-claude-code-d72d86.yaml
    sha256: efe9fd09e810c5d0d0c447b74bdf1038d2bcf7fd3524f13c3a6b3aa67f0b6ced
    role: context
  - path: history/infrastructure/disposition-typing-burndown/2026-08-08T060908Z-claude-code-f802c8.yaml
    sha256: 8ede4f80f46395efb74643e1f4158975a119ffaec78b5b291f0fc3a520a11c59
    role: context
  - path: history/infrastructure/oxygen-senses/2026-08-17T031421Z-claude-code-76561e.yaml
    sha256: 2a021c768e6db37eed31e3ab73c9714bd85ef31bc5f04e986ac0642c16fbe2a3
    role: context
  - path: history/mappings/name-match-groundings/2026-08-17T042357Z-claude-code-2a9f93.yaml
    sha256: c3f93d5c8c0da5c538af391bfdbad3a8bcbe238a26a8727764c3f0ddc3422ad8
    role: context
  - path: history/other/canonical-examples-environment/2026-08-26T105411Z-codex-29d8602.yaml
    sha256: 6e602707db80e54519a6f46d5bf2b79f5c6b2fc294d75176ba4406cac22fc2c2
    role: context
  - path: justfile
    sha256: 008643042a721e84f647be6beda104ae02fe616361ff9b34fc608643a7526ee2
    role: context
  - path: mappings/node_grounding.tsv
    sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
    role: context
  - path: mappings/predicate_grounding.tsv
    sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
    role: context
  - path: mappings/trait_exact_match_review.tsv
    sha256: 7728593d526d9a723716e5daad64beb7e1ab5c2e4221ae8d43dd9480cd02f62b
    role: context
  - path: mappings/uniprot_regrounding_candidates.tsv
    sha256: c36d8e038886d137d5a1ae609240e59ce74b6aeee17ae24f21b6c4a0d7407391
    role: context
  - path: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
    sha256: 4ab5ca37ff8595210254b1099563b4425ecd737ed375dc5a932b44e2ad5c332e
    role: context
  - path: proposals/metpo_traitmech_v2/proposal.md
    sha256: fe0601356b120ef9babc6f90a417f860bf02aa628c46af661517f168e01bc48f
    role: context
  - path: proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
    sha256: 1a1cc789782cfae195c1fc81ddaf848d06d162c7434d94cceb66838de98ab6fa
    role: context
  - path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
    role: context
  - path: proposals/metpo_traitmech_v5/proposal.md
    sha256: 5d54623dd00ac80a8d67a0eab7b70385f7f57b36daa205c28aa1f9d6f9be6167
    role: context
  - path: proposals/metpo_traitmech_v6/metpo_proposal_properties_robot.tsv
    sha256: ed877efe2d59f43c51898e2dc85440188711455dcc5c882af2dc1384fc38fc19
    role: context
  - path: proposals/metpo_traitmech_v6/proposal.md
    sha256: aecbd48fd73712ccab57619d753b6084a7fa2fbf616f80623f63ce15b65871ae
    role: context
  - path: proposals/metpo_traitmech_v7/metpo_proposal_classes_robot.tsv
    sha256: 99e779afa894363b32966bd15415417035d246970aab02931ce896f37c910a73
    role: context
  - path: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
    role: context
  - path: proposals/metpo_traitmech_v8/proposal.md
    sha256: 119d51e7b7194890514a9e313505212bab92aeba607f7c1b8f9d9d2edeef67e7
    role: context
  - path: proposals/metpo_traitmech_v9/metpo_proposal_properties_robot.tsv
    sha256: 5ae84dd1351a4bec39adf7bcd5b3a8982af2e95fbccd0b53c0efa3efbfc89b0e
    role: context
  - path: proposals/metpo_traitmech_v9/proposal.md
    sha256: 85fde22f4733863188b437cfcf7552a31fea07ad1d32c0400cf493295c1e1156
    role: context
  - path: research/traits/environment/aerotolerant-deep-research-falcon.md
    sha256: 6d95564ab53550b2e9fa6173be208f68ed0f085d4432d5a569931d12695d8a35
    role: context
  - path: scripts/audit_causal_graphs.py
    sha256: e0c26506c9de712700317284f142097e7bf69334806b8010db5d6517e905e834
    role: context
  - path: scripts/backfill_canonical_examples_444.py
    sha256: 18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c
    role: context
  - path: scripts/curate_knowledge_gaps.py
    sha256: 9e0fb7e01a901d84189a28f1912a2552f28d2da8733c113589e4947359d48c73
    role: context
  - path: scripts/ground_causal_predicates.py
    sha256: 5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381
    role: context
  - path: scripts/migrate_disposition_typing.py
    sha256: ebafdd145fc0729d32f3b8a45f570d97a8e001838afadd698e2b246cb8950714
    role: context
  - path: scripts/migrate_enables_trait_edges.py
    sha256: a5e7965ee4f6b6ba5bae3a06bced2a83cbf755f3b9b150ce6acc0cd808cb1d88
    role: context
  - path: scripts/migrate_microbe_domain_edges.py
    sha256: 5187ccfb2897d415b243792a27afd6002c0eea4b167068639ff5be73ed583bb6
    role: context
  - path: scripts/migrate_name_match_groundings.py
    sha256: 9b3ea1153839b9b260638cef95eba2d1ccc6d7b3825e7352c33cceb21bfe4dd4
    role: context
  - path: scripts/migrate_oxygen_senses.py
    sha256: 372e977a58ec6e17cdd45021c5849895142c67187eb29b995b8c39f0e899d2f3
    role: context
  - path: scripts/migrate_pathway_vs_process.py
    sha256: f236de7183048732e9001b7fac4367affff58d8b7a7d5c63286e6b058a4b38c2
    role: context
  - path: scripts/migrate_process_quality_consistency.py
    sha256: 1a83ad3dba79ed0c958b875a6fcc4b9e562259af26da2f248d32d5cf7784f80a
    role: context
  - path: scripts/migrate_protein_vs_activity.py
    sha256: 0b183248ff22d3d8aa66b35aece40c53b516684ca499cf73b7714206031dad49
    role: context
  - path: scripts/seed_from_metpo.py
    sha256: 0fb9c9f7ea6a8f137eecd5c319775b511c398dba6158c81b1fbfb94210f7d851
    role: context
  - path: scripts/verify_metpo_proposal.py
    sha256: f58355151f7d6a807bb50dc8b732184994b0d6145d3c57f54e29fd0bb76268b6
    role: context
  - path: src/traitmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: src/traitmech/validation/write_validated.py
    sha256: 68cfeb876a60d67fd72d5a2800cd29e41b5cf563be5a27b698398a5bb3e67231
    role: context
targets:
- target_id: METPO:1000609
  path: data/traits/environment/aerotolerant.yaml
  label: aerotolerant
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/aerotolerant.yaml
    role: Maintained TraitRecord; scientific changes require guarded curation
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Original METPO import identity/provenance
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Second batch004 target in lexicographic path order after aerobic was
    validated and saved. Whole target read before native capture. Supplemental owner
    captures retained all earlier input hashes unchanged; scientific review covers
    one complete record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000609
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000609
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000609
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000609
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000609
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000609
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000609
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000609
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    004 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: aerotolerant-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1000609
  command: just validate data/traits/environment/aerotolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The selected record validates.
  evidence_ids:
  - check-aerotolerant-validate
- check_id: aerotolerant-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000609
  command: just validate-strict data/traits/environment/aerotolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero strict errors.
  evidence_ids:
  - check-aerotolerant-strict
- check_id: aerotolerant-snippets
  name: Focused snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1000609
  command: just verify-snippets --record data/traits/environment/aerotolerant.yaml
    --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/aerotolerant-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'The DOI/PMID recipe checked five snippets: three VERIFIED and two NOT_IN_ABSTRACT.
    The URL-based definition excerpt was checked manually. Across all six occurrences,
    four are exact, one is a faithful ellipsized table composite and one remains unverified.'
  evidence_ids:
  - check-aerotolerant-snippets
- check_id: structured-source-runner
  name: Structured-source runner availability
  status: unavailable
  required: false
  target_ids:
  - METPO:1000609
  summary: Original bounded discovery reused; official catalog fallback inspected.
  evidence_ids:
  - runner
- check_id: expression-context
  name: Lactococcus expression-source applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000609
  summary: No matching dataset in the inspected catalog; no substitute organism or
    negative phenotype inference.
  evidence_ids:
  - expression
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T08:30:11Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T08:30:11Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T08:30:11Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T08:30:11Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T08:30:11Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T08:30:11Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T08:30:11Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-aerotolerant-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/aerotolerant-validate.log
  locator: Executed 2026-10-21T08:24:45Z through 2026-10-21T08:24:46Z; metadata aerotolerant-validate.json
  accessed_at: '2026-10-21T08:30:11Z'
  support: context_only
  summary: The selected record validates.
  snapshot_sha256: 0b4435bfe76a7c7561ee4139d39f4e5f5d239162f13e8da0793ec24d33a2d287
- evidence_id: check-aerotolerant-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/aerotolerant-strict.log
  locator: Executed 2026-10-21T08:24:45Z through 2026-10-21T08:24:47Z; metadata aerotolerant-strict.json
  accessed_at: '2026-10-21T08:30:11Z'
  support: context_only
  summary: One file scanned; zero strict errors.
  snapshot_sha256: fa0fc4438c74383b52eba93084b47a02c3ee01d0f035d78ebc5bb62a4eae71c7
- evidence_id: check-aerotolerant-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/aerotolerant-snippets.log
  locator: Executed 2026-10-21T08:25:02Z through 2026-10-21T08:25:09Z; metadata aerotolerant-snippets.json
  accessed_at: '2026-10-21T08:30:11Z'
  support: context_only
  summary: 'The DOI/PMID recipe checked five snippets: three VERIFIED and two NOT_IN_ABSTRACT.
    The URL-based definition excerpt was checked manually. Across all six occurrences,
    four are exact, one is a faithful ellipsized table composite and one remains unverified.'
  snapshot_sha256: ea3f9fc92987409139e9ea8f923004bfb85a156c9dad772e5137cca730112579
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/aerotolerant.yaml
  locator: 'Complete target: identity, definition, synonym, evidence, two canonical
    examples, eleven nodes, eight edges and eighteen events'
  accessed_at: '2026-10-21T08:30:11Z'
  support: partial
  summary: The aerotolerant concept is correctly identified. Five grounded relations
    have endpoint or meaning conflicts; one example needs conditional context and
    human acceptance is not linked in bounded local provenance.
  snapshot_sha256: 4ae40096583868e5ab9b31f8aec3a81a09938faf24391f57a6a34b32b2efb3a8
- evidence_id: shape
  kind: validation
  reference: Complete parsed graph/history
  locator: All eleven nodes, eight edge endpoints and eighteen events
  accessed_at: '2026-10-21T08:25:03Z'
  support: supports
  summary: No unresolved endpoints. Seventeen events disclose AI assistance and one
    records seeding. No pathway-context link is asserted.
  snapshot_sha256: e2d99230bdc8daf8982328a7545613e1d2b60a1f7ce289fe505b776ce88fd738
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl; data/traits/environment/oxygen_preference.yaml
  locator: Active1000609 and broader1000601; complete exact-name/synonym scan
  accessed_at: '2026-10-21T08:25:36Z'
  support: supports
  summary: Current identity, definition and parent match the pinned ontology. The
    related aerotolerant-anaerobe synonym has an independently cited teaching source.
    Obsolete matches have explicit replacement links only where actually recorded.
  snapshot_sha256: 5ce5b640b41976f53cd41ac1ea16dc662dcc97afe8eefb696c42f429bb93af18
- evidence_id: live-identifiers
  kind: authority
  reference: QuickGO, InterPro, ChEBI and NCBI Taxonomy
  locator: Five current GO terms, IPR052364, CHEBI16240 and taxa1358/1314
  accessed_at: '2026-10-21T08:25:49Z'
  support: supports
  summary: GO0004784,0004096,0016692,0050137 are active activity terms and GO0042744
    is active hydrogen-peroxide catabolism. InterPro resolves Rubrerythrin family;
    peroxide and both taxon labels match. The existing corrected GO term is assessed,
    not its historical predecessor.
  snapshot_sha256: 5b8315798fe6a58daa0a79c1da2a02b63db66bb4b214b42c7cd9747f3e02f7fb
- evidence_id: reused-chemicals
  kind: authority
  reference: Official ChEBI responses retained from aerobic review
  locator: CHEBI15379 and26523; original08:17:52Z accesses and verified hashes
  accessed_at: '2026-10-21T08:17:52Z'
  support: supports
  summary: Dioxygen and reactive oxygen species match the current chemical nodes.
    Reuse preserves the original actual retrieval times and hashes.
  snapshot_sha256: 2ac0ff147bf5adb475adf995227a2b4688dbad74bf4914f80c5893e1f607d6fd
- evidence_id: ro
  kind: authority
  reference: Read-only authoritative RO snapshot
  locator: Inherited relations for contributes-to, negative regulation and enables
  accessed_at: '2026-10-21T08:25:36Z'
  support: partial
  summary: Contributes-to has a process range; negative regulation has process endpoints.
    The described enzyme actors are material despite allowed activity-facet groundings.
    Catalase enabling a detoxification process fits the material-actor/process roles.
    Original RO inspections08:04:46Z and07:58:06Z are retained with matching source
    hashes.
  snapshot_sha256: 98cdf11c414a6952c650cbeeae56e0b68d19eb443c6ce7cc6779989ae740f485
- evidence_id: biolink
  kind: authority
  reference: data/raw/biolink-model.yaml
  locator: has-part textual description and inherited slots
  accessed_at: '2026-10-21T08:25:36Z'
  support: partial
  summary: Has-part describes material/process wholes and parts. A trait linked to
    a defining growth facet is not that same relation. Formal inherited endpoints
    are named thing; no enforced material-domain failure is claimed.
  snapshot_sha256: ba7992fc8aa151ff698e2168e1e1b8ef96c18ca6ea9aa81d3991d88e2b4a32cf
- evidence_id: ledger
  kind: validation
  reference: Independent documentary ontology audit
  locator: All eleven nodes and eight edges, zero-based indices
  accessed_at: '2026-10-21T08:27:29Z'
  support: partial
  summary: Confirmed conflicts at edges0,2,5,6,7. Edge4 fits its described material
    actor and process object. Provisional mitigates accepts the represented contextual
    roles. GO activity facets, label-only context and replaced historical identifiers
    are not extra defects.
  snapshot_sha256: d4bf3ba5af2b6cfdd5a005f3e26bc01bc9591c9967ca982c5b92d06385e33312
- evidence_id: mapping-owners
  kind: record_content
  reference: mappings/predicate_grounding.tsv; mappings/node_grounding.tsv; proposals/metpo_traitmech_v2
  locator: Predicate rows10,39,61,76 and current node decisions
  accessed_at: '2026-10-21T08:30:11Z'
  support: partial
  summary: Broad wildcard mappings assign contributes-to, negative-regulation and
    has-part without guarding the present semantic distinctions. Current protein-function
    and Rubrerythrin-family decisions follow native policy; mitigates is a documented
    provisional proposal.
  snapshot_sha256: f50e5a535e83679e4e3e3a5d837987d71906c230f2a486ffbc50368a63a05e3f
- evidence_id: writer
  kind: record_content
  reference: scripts/ground_causal_predicates.py; justfile
  locator: Writer contract and ground-predicates recipe
  accessed_at: '2026-10-21T08:30:11Z'
  support: supports
  summary: The dry-run-by-default writer fills empty predicate identifiers from the
    mapping; it does not overwrite existing nonempty identifiers. Mapping repair alone
    therefore would not correct the existing target edges. Guarded record curation
    and mapping recurrence checks are distinct proposed steps.
  snapshot_sha256: 5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml
  locator: Legacy protein function-facet grounding and NONMECHANISTIC scope
  accessed_at: '2026-10-21T08:30:11Z'
  support: supports
  summary: GO activity terms are allowed taxon-agnostic functional groundings for
    described enzyme actors. Broad contextual graphs do not require token protein
    instances, datasets or a single universally necessary defense mechanism.
- evidence_id: definition
  kind: primary_source
  reference: https://bio.libretexts.org/Courses/Ohio_State_University/Microbiology_Lab_SP25/05%3A_Lab_5/5.05%3A_Bacterial_Oxygen_Requirements
  locator: Conceptual oxygen-classification section, aerotolerant-anaerobes bullet
  accessed_at: '2026-10-21T08:24:53Z'
  support: supports
  summary: The actual teaching page supports oxygen tolerance without oxygen use for
    ATP production and the related synonym. The short top-level quotation is exact.
    Laboratory procedures and unrelated categorical claims on the page were not used
    as evidence.
  snapshot_sha256: 9dd4b1da2c834d8feb5eefa7800442805cb99eae84a217560cb49deb2ea476a8
- evidence_id: bibliography
  kind: database
  reference: Europe PMC and inspected primary/publisher sources
  locator: Nine citation identities, eight edge claims and all six snippets
  accessed_at: '2026-10-21T08:27:12Z'
  support: partial
  summary: All nine identities resolve. Four snippets are exact, one is a faithful
    table composite and one is access-limited. Eighteen acquisition attempts include
    fourteen hashed responses; two API-error bodies are explicitly excluded. Two reused
    files retain original hashes/times.
  snapshot_sha256: cde5249e7032295c4556cd4f2f3fa73ee95751fb38985412b6a5c934bf4b982e
- evidence_id: lactococcus
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/11443085/
  locator: DOI10.1128/jb.183.15.4509-4516.2001; complete indexed abstract
  accessed_at: '2026-10-21T08:24:52Z'
  support: partial
  summary: The source describes fermentative Lactococcus lactis but also demonstrates
    conditional respiratory capacity. The existing note already says fermenter; add
    the applicable context rather than declaring the species incapable of fermentative
    aerotolerance or treating inability to use oxygen as species-wide.
  snapshot_sha256: d763262ff20a64aade9ec672894ec5b5c799197325f3796ff368deacb0f10ccf
- evidence_id: streptococcus
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/jb.182.19.5290-5299.2000
  locator: PMID10986229; actual publisher introductory phenotype paragraphs, browser
    lines88–90
  accessed_at: '2026-10-21T08:25:37Z'
  support: supports
  summary: Introductory fermentative and aerotolerant physiology supports the canonical
    example. The source uses facultative-anaerobe terminology for lactic-acid bacteria
    while describing fermentative metabolism; terminology alone is not a contradiction.
    Detailed pathogen defense routes and mutant mechanisms were not assessed.
- evidence_id: perfringens
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/38864615/
  locator: DOI10.1128/mmbr.00140-23; metadata and publisher summary only
  accessed_at: '2026-10-21T08:24:52Z'
  support: context_only
  summary: The reference and species context resolve, but the relative-aerotolerance
    quotation and its phenotype support remain unverified on the available source
    surfaces. Full-text failures, API-error response and challenge pages do not establish
    that the quote is false. No detailed pathogen biology was assessed.
  snapshot_sha256: 117cf04cb8a8402df725c6453a55b1e4a49c20138cb812073fe2f855847e8a46
- evidence_id: classification
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3969821/
  locator: DOI10.1038/nrmicro2970; BioC Introduction offset1661 and Table1 offset37517
  accessed_at: '2026-10-21T08:25:23Z'
  support: supports
  summary: The introduction and table support aerotolerant anaerobes as oxygen-tolerating
    nonrespiring organisms with anaerobic growth. The excerpt combines row label and
    column headings with explicit ellipses; it is a faithful table composite, not
    continuous prose or proof of a formal part-whole relation.
  snapshot_sha256: 08f399475a6ff5040a7cf2d442f95d5221cba25190c2b4ee1fb815eee76c30ea
- evidence_id: oxygen-context
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9191689/
  locator: DOI10.1038/s41579-021-00583-y; newly acquired BioC abstract offset86 and
    Introduction offset4048
  accessed_at: '2026-10-21T08:25:23Z'
  support: supports
  summary: The short phrase is exact. The general introduction supplies oxygen-derived-stress
    context beyond the quoted phrase about joint toxicity. Only conceptual context
    was assessed, not detailed pathogen survival routes.
  snapshot_sha256: 8ce53770e39dc8f72cd5dc03fff9676954ed0f43c0ac36be40e2b78466239430
- evidence_id: sod-association
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/326669/
  locator: DOI10.1128/iai.16.1.20-25.1977; abstract correlation and qualified conclusion
    sentences
  accessed_at: '2026-10-21T08:24:52Z'
  support: partial
  summary: Both snippets are exact. The comparison covers twenty-two isolates and
    explicitly reports correlation with a usually-qualified inference. This supports
    the record’s qualified abundance association, not universal necessity or a reconstructed
    causal survival mechanism.
  snapshot_sha256: 568095bf279f0ad19e574b0824144ff12c66212a9273156dea1cd22788c5d233
- evidence_id: anammox-context
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10156729/
  locator: DOI10.1038/s43705-023-00251-7; Discussion Sec19 paragraph2, contextual
    Sec17 paragraph1
  accessed_at: '2026-10-21T08:24:58Z'
  support: partial
  summary: The general catalase and Rubrerythrin functional descriptions appear in
    the cited anammox source. Nearby text leaves individual cellular contributions
    uncertain. This supports contextual biochemical descriptions without proving a
    class-wide required mechanism.
  snapshot_sha256: 3b77abf7cca79062999afc25a02058a2207f166919f1a6ff49eab543503eaa4b
- evidence_id: peroxidase-context
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10457377/
  locator: DOI10.1038/s41598-023-41185-3; Introduction Sec1 equationEqub and paragraph7
  accessed_at: '2026-10-21T08:24:56Z'
  support: partial
  summary: The introductory reaction identity and analogous cofactor statement support
    generic contextual enzyme chemistry. The study concerns cell-free activities in
    two intestinal sulfate-reducing strains; it does not establish universal aerotolerance
    machinery. Experimental/kinetic optimization was not assessed.
  snapshot_sha256: f466fb1b49554f0c9424f6c47875a6cef67095adaa86fe26f3795396a46f23fd
- evidence_id: provenance
  kind: search
  reference: Target fields and bounded local provenance
  locator: All eighteen events and ignored-inclusive exact identifier/path/slug search
  accessed_at: '2026-10-21T08:25:03Z'
  support: partial
  summary: No explicit human scientific acceptance link for this target/revision was
    found in inspected local provenance. Matching migration histories disclose AI
    actors and contextual changes. Private or remote approval remains unknown.
  snapshot_sha256: b701cee26a81bd7790a40e019e9eacf5afc7e6f01307097afa508c518db2eeee
  search_scope: rg --no-ignore --hidden across history,mappings,scripts,reviews/structured
    for METPO:1000609, exact target path and slug. All target events read; remote/private
    approvals unsearched.
- evidence_id: status-rule
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md
  locator: Status/audit and Verification gate
  accessed_at: '2026-10-21T08:30:11Z'
  support: supports
  summary: REVIEWED requires human scientific acceptance; AI curation and automated
    checks have different provenance roles.
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Original07:36:12Z catalog; bounded Lactococcus applicability check08:26:53Z
  accessed_at: '2026-10-21T08:26:53Z'
  support: context_only
  summary: No Lactococcus lactis dataset matches the complete inspected catalog. Other
    lactobacilli were not substituted. No gene/module query or negative biological
    conclusion followed; detailed pathogen stress-defense queries were outside this
    expression scope.
  snapshot_sha256: 1b4a192451ceb8b6361285451668ad245e1a65bffafbbe38319bbb93cb02d4d0
- evidence_id: runner
  kind: search
  reference: Reused structured-source runner discovery
  locator: Original bounded ignored-inclusive search08:17:15Z
  accessed_at: '2026-10-21T08:17:15Z'
  support: context_only
  summary: No usable runner was found in the declared original PATH/install/project/B4
    scope. The original receipt and catalog fallback are retained; no new or global
    runner absence is asserted.
  snapshot_sha256: 39b52930f52e898f85ac3bbb88f11ac674a355967b5704e2b62f0bda259d404f
  search_scope: Original exact bounds are preserved in runner-discovery.json; ignored
    files were included and unsearched directories remain unknown.
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, definition, synonym and parent'
  outcome: supported
  target_ids:
  - METPO:1000609
  summary: Active METPO1000609 and parent1000601 match. The definition source and
    related synonym directly support the nonrespiring oxygen-tolerant class.
  evidence_ids:
  - identity
  - definition
  - record
- assessment_id: model
  area: representation
  topic: 'Native checklist: category, class and NONMECHANISTIC context'
  outcome: supported
  target_ids:
  - METPO:1000609
  summary: ENVIRONMENT/CLASS and contextual NONMECHANISTIC scope fit. Optional protein
    instances, datasets and universal mechanisms are not missing requirements.
  evidence_ids:
  - record
  - policy
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: canonical examples and contextual organism quotation'
  outcome: concern
  target_ids:
  - METPO:1000609
  summary: Both canonical taxon identities resolve. Streptococcus introductory phenotype
    context supports the example. Lactococcus fermentative membership is plausible
    but needs conditions in light of the cited respiratory-capacity result. The separate
    C. perfringens quotation remains unverified.
  evidence_ids:
  - live-identifiers
  - lactococcus
  - streptococcus
  - perfringens
- assessment_id: grounding
  area: grounding
  topic: 'Native checklist: current term identity and historical corrections'
  outcome: supported
  target_ids:
  - METPO:1000609
  summary: Current GO/CHEBI/InterPro terms match intended functional, process, chemical
    and family meanings. GO activity groundings do not automatically retype described
    enzyme actors. Historical withdrawn IDs are not current errors.
  evidence_ids:
  - live-identifiers
  - reused-chemicals
  - ledger
  - policy
- assessment_id: graph
  area: consistency
  topic: 'Native checklist: eleven nodes and eight grounded or free-text edges'
  outcome: concern
  target_ids:
  - METPO:1000609
  summary: Five relations conflate trait facets with whole-part structure, a trait
    with a process object, or chemical consumption with process regulation. Catalase
    enabling a detoxification process and provisional mitigates have compatible contextual
    roles.
  evidence_ids:
  - shape
  - ledger
  - ro
  - biolink
  - mapping-owners
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: all eight edge claims and source contexts'
  outcome: supported
  target_ids:
  - METPO:1000609
  summary: The table and general source passages support the contextual biological
    descriptions. Correlation, anammox physiology and cell-free enzyme assays retain
    their limits; they are not universal causal proof. Ontology relation errors are
    assessed separately from source support.
  evidence_ids:
  - classification
  - oxygen-context
  - sod-association
  - anammox-context
  - peroxidase-context
  - bibliography
- assessment_id: quotes
  area: evidence
  topic: 'Native checklist: all six snippet occurrences'
  outcome: unknown
  target_ids:
  - METPO:1000609
  summary: Four excerpts are exact, one is a faithful explicitly ellipsized table
    composite and one is unverified due to inaccessible body text. No false-quote
    finding is inferred from source-access failure.
  evidence_ids:
  - definition
  - classification
  - oxygen-context
  - sod-association
  - perfringens
  - bibliography
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: structure and optional evidence surfaces'
  outcome: supported
  target_ids:
  - METPO:1000609
  summary: All nodes and edge endpoints resolve and required identity/evidence surfaces
    are present. The graph’s contextual disposition does not demand one token accession
    per enzyme or every possible defense pathway.
  evidence_ids:
  - shape
  - record
  - policy
- assessment_id: expression-context
  area: evidence
  topic: 'Native checklist: optional Lactococcus dataset coverage'
  outcome: supported
  target_ids:
  - METPO:1000609
  summary: Catalog coverage is not applicable for the scoped Lactococcus example.
    No other organism was substituted and missing coverage is not treated as biological
    absence.
  evidence_ids:
  - expression
  - runner
- assessment_id: audit
  area: provenance
  topic: 'Native checklist: AI disclosure, writer recurrence and human acceptance'
  outcome: concern
  target_ids:
  - METPO:1000609
  summary: AI assistance is explicit. Wildcard mappings can reproduce semantic mistakes
    when filling empty IDs; already grounded edges require separate correction. Human
    acceptance is not linked within the bounded inspected local provenance.
  evidence_ids:
  - provenance
  - status-rule
  - writer
  - mapping-owners
findings:
- finding_id: external-relation-semantics
  issue_key: aerotolerant-external-relation-semantics
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Five relation mappings conflict with the represented endpoint meanings
  description: Edge0 maps a conceptual trait/growth facet to material/process whole-part
    semantics. Edge2 gives RO contributes-to a trait object despite its inherited
    process range. Edges5–7 map protein-to-chemical decreases to RO process regulation.
    Biolink formal endpoints remain named thing; native validation passes and no formal
    reasoner failure is claimed.
  target_ids:
  - METPO:1000609
  field_paths:
  - causal_graphs[0].edges[0]
  - causal_graphs[0].edges[2]
  - causal_graphs[0].edges[5]
  - causal_graphs[0].edges[6]
  - causal_graphs[0].edges[7]
  evidence_ids:
  - record
  - ledger
  - ro
  - biolink
  - mapping-owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/aerotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: example-condition-scope
  issue_key: aerotolerant-example-condition-scope
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Lactococcus example needs its fermentative condition scope
  description: The note already calls L. lactis a fermenter, but its cited source
    explicitly demonstrates conditional respiratory capacity. Qualify the canonical
    example so the definition is not read as a species-wide inability to use oxygen.
    This does not make the species an impossible example or contradict its fermentative
    aerotolerance.
  target_ids:
  - METPO:1000609
  field_paths:
  - canonical_examples[0].note
  evidence_ids:
  - lactococcus
  - record
  - definition
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/aerotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: aerotolerant-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human scientific acceptance is not linked locally
  description: Seventeen AI-assisted events and one seed are explicit, but the bounded
    inspected target and local provenance contain no acceptance link identifying this
    record revision. Remote/private approval remains unknown.
  target_ids:
  - METPO:1000609
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - status-rule
  - shape
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/aerotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: repair-relations
  description: In separately authorized curation, reconcile the five predicate meanings
    with their actual endpoint roles and review the wildcard mapping decisions for
    recurrence while preserving supported source scope.
  finding_ids:
  - external-relation-semantics
  target_ids:
  - METPO:1000609
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/aerotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Inspect inherited RO constraints and Biolink textual semantics separately from
    permissive formal endpoints.
  - Keep described enzyme actors distinct from their allowed GO activity-facet groundings.
  - Use the maintained ground-predicates dry run to review recurrence; it cannot overwrite
    the existing nonempty IDs.
  - Run focused strict and graph checks plus just qc after authorized correction;
    append native history and regenerate affected maintained products.
- action_id: qualify-example
  description: Retain the Lactococcus fermentative example with explicit condition/evidence
    scope rather than asserting a species-wide inability to respire.
  finding_ids:
  - example-condition-scope
  target_ids:
  - METPO:1000609
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/aerotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The note distinguishes the documented fermentative state from conditional respiration
    in the same cited study.
  - No unsupported phenotype, strain equivalence or new experimental recipe is introduced.
  - Run focused record validation after any authorized edit.
- action_id: link-acceptance
  description: Locate and link existing human scientific acceptance or obtain it through
    the established process; preserve AI history and reassess status if acceptance
    remains unavailable.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000609
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/aerotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies the record revision and scientific scope.
  - Automated validation and AI provenance are not presented as human approval.
limitations:
- The C. perfringens quotation and phenotype claim remain unverified on inspected
  abstract/summary surfaces; inaccessible body text does not establish falsity.
- Detailed pathogen survival, stress-defense and mutant mechanisms were not assessed
  or reconstructed. Streptococcus support is confined to introductory phenotype framing.
- The Streptococcus primary introduction was inspected through an actual publisher
  browser open without a local body hash; a separate BioC error response is excluded.
- Lactococcus and the comparative SOD study were checked from complete indexed abstracts.
  The former has condition-dependent physiology; the latter supports correlation with
  a usually qualifier, not universal necessity.
- The table excerpt is a row/header composite with explicit ellipses, not continuous
  prose. Its classification does not establish formal ontological parthood.
- Anammox and cell-free enzyme studies support contextual functional claims; individual
  cellular contributions and class-wide causal necessity remain unestablished.
- The teaching source was used only for its cited conceptual classification; laboratory
  instructions and unrelated generalizations were not adopted.
- GO activity terms are permitted enzyme-function facets. Described protein actors
  are not silently converted to process nodes, and chemical objects are not silently
  replaced by concentration-change processes.
- RO/CHEBI cache reuse retains original timestamps/hashes; local inspection does not
  certify a new ontology release.
- No Lactococcus dataset matches the inspected expression catalog; that is missing
  coverage, not negative biological evidence.
- Human acceptance outside the bounded local search remains unknown.
- No scientific record, schema, mapping, writer, status, history or generated page
  was changed.
notes:
- Field paths use zero-based indices.
- The initial native capture ran08:24:05Z, followed by supplemental owner capture08:24:17Z
  and writer/recipe capture08:28:22Z; all previously captured inputs stayed byte-identical.
- Current GO0042744 replaced a historical plant-pathway grounding; the withdrawn ID
  is not a present defect.
tags:
- record-review
- aerotolerant
- environment
- needs-curation
```
