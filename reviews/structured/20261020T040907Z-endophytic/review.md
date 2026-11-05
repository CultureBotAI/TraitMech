# Scientific and source review of endophytic (traitmech:000442)

- Review: 20261020T040907Z-endophytic
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-20T04:05:18Z
- Finished UTC: 2026-10-20T04:09:07Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The proposed ecological trait, local fallback identifier, broader host-associated parent and scoped definition are defensible. All four quotations were verified, and both cited reviews were inspected. Their different definitions of endophyte are preserved as a scope limitation. One major finding concerns the first edge: a habitat statement is grounded as the stronger RO enables relation. All three nodes and both edges were assessed; no universal mechanism or mandatory example is inferred.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: First record in batch 002 and eleventh newly covered record overall, following the validated inventory from batch 001 in lexicographic path order. Exactly one entire TraitRecord.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f25e2af0b38a8303b13f627a9a5c33b36af4b3d2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000442 | data/traits/ecology/endophytic.yaml | maintained | endophytic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000442 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000442 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000442 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | traitmech:000442 | 1276 history records checked, zero invalid links; integrity does not establish scientific correctness or human sign-off. |
| Initial full-product validation | failed | False | traitmech:000442 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000442 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000442 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | traitmech:000442 | The selected record validates. |
| Focused strict validation | passed | True | traitmech:000442 | One file scanned; zero error rows. |
| Focused source snippet verification | passed | True | traitmech:000442 | Four snippets across two references were VERIFIED. Source identity, context and the meaning of the cited relation were assessed separately. |
| Native proposal verification | passed | True | traitmech:000442 | The one-class v319 cohort passes. Scope-C checking was explicitly skipped because this cohort proposes no enum vocabulary; this is not an OWL reasoning result. |
| Expression-module applicability | not_applicable | False | traitmech:000442 | This broad habitat record asserts no gene, protein, strain or transcriptomics dataset. No expression-module match is required or inferred. |

## Scientific And Domain Assessments

### Native checklist: identifier, label, synonyms, polarity and kind

identity: supported. Targets: traitmech:000442.

One ecological trait is identified. The fallback and pending proposal are documented. The endophyte alias is interpreted as conventional trait-bearing terminology, not an organism-class equivalence assertion; the related endophytism alias does not erase broader usage in the literature.

### Native checklist: definition and concept boundary

evidence: supported. Targets: traitmech:000442.

The no-apparent-disease convention has source support. The inspected papers also discuss broader usage; this review preserves that distinction rather than treating both papers as endorsing an identical boundary.

### Native checklist: strictly broader parent and sibling distinction

consistency: supported. Targets: traitmech:000442.

The host-associated parent is broader and the internal/surface distinction from epiphytic is coherent. No requirement for plant growth promotion or nitrogen fixation is added.

### Native checklist: category and graph scope

representation: supported. Targets: traitmech:000442.

The class describes an ecological habitat association. NONMECHANISTIC scope is appropriate, and the generic nodes do not require a fabricated universal molecular mechanism.

### Native checklist: canonical-example disposition

completeness: supported. Targets: traitmech:000442.

Examples are optional and the history explicitly records a first-pass evidence gap. No unsupported strain or species is asserted. This is not an exhaustive claim that no suitable example exists.

### Native checklist: references, quotations and nearest support

evidence: concern. Targets: traitmech:000442.

Both article identities resolve and all four quotations match. Exact wording alone does not establish the first edge’s stronger causal/ontology interpretation. The two sources’ definition scopes remain distinct.

### Native checklist: all three nodes and both edges

graph: concern. Targets: traitmech:000442.

The habitat, colonization process and ecological trait have distinct intended meanings, and all endpoints resolve. Edge0 presents a location definition as RO enables. Edge1 is a conceptual realization statement under the record’s selected endophytic convention and uses a documented proposed predicate.

Zero-based ledger: edge0 internal_plant_tissue/enables/endophytic_colonization is not supported at the semantics of RO:0002327 by the quoted definition; material subject type alone is insufficient. Edge1 endophytic_colonization/confers/endophytic_trait is a nonmechanistic conceptual bridge, not an experimental demonstration of one universal route. Its meaning remains bounded by the no-apparent-disease definition of the target node and cited convention.

### Native checklist: discussions and datasets

completeness: not_applicable. Targets: traitmech:000442.

The complete target contains no discussion or dataset assertion. Optional fields need not be added simply to populate the model.

### Native checklist: status, history and native checks

provenance: supported. Targets: traitmech:000442.

PROPOSED status and explicitly AI-assisted creation/history are consistent with the documented work. No human scientific sign-off or status promotion is claimed. Focused checks pass; earlier same-base corpus diagnostics retain their limitations.

## Findings

### habitat-enables-overclaim: A habitat statement is assigned the stronger RO enables relation

major / open / confirmed; issue key: endophytic-habitat-enables-overclaim.

The first edge’s description and quotation say where the microbial process takes place. RO:0002327 instead identifies a material entity capable of executing that process. The record describes the plant tissue as habitat, not as the entity performing microbial entry, growth and multiplication. This is an evidence-to-predicate mismatch, not a claim that tissue cannot matter causally and not a formal material-entity domain violation.

## Recommended Actions And Acceptance Checks

### align-habitat-relation

Represent the source-supported habitat relation at its actual semantic strength and reconcile the maintained creation constants.

- Inspect the intended relation’s definition and direction as well as endpoint types; do not select an identifier from its label alone.
- Retain a conceptual ecological graph without inventing a causal mechanism to justify an existing edge.
- The creation script is an owner to update, not a migration to replay over an existing record.
- After separately authorized curation, use guarded writes/history and run focused validation, strict validation, snippet checks, graph/grounding checks and applicable qc.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; metadata validate-history.json | context_only | 1276 history records checked, zero invalid links; integrity does not establish scientific correctness or human sign-off. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-endophytic-validate | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endophytic-validate.log; Executed 2026-10-20T04:05:31Z through 2026-10-20T04:05:32Z; metadata endophytic-validate.json | context_only | The selected record validates. |
| check-endophytic-strict | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endophytic-strict.log; Executed 2026-10-20T04:05:31Z through 2026-10-20T04:05:32Z; metadata endophytic-strict.json | context_only | One file scanned; zero error rows. |
| check-endophytic-snippets-network | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endophytic-snippets-network.log; Executed 2026-10-20T04:05:52Z through 2026-10-20T04:05:56Z; metadata endophytic-snippets-network.json | context_only | Four snippets across two references were VERIFIED. Source identity, context and the meaning of the cited relation were assessed separately. |
| check-endophytic-proposal | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endophytic-proposal.log; Executed 2026-10-20T04:07:22Z through 2026-10-20T04:07:22Z; metadata endophytic-proposal.json | context_only | The one-class v319 cohort passes. Scope-C checking was explicitly skipped because this cohort proposes no enum vocabulary; this is not an OWL reasoning result. |
| record | data/traits/ecology/endophytic.yaml; Entire record; three nodes, two edges, two references and two history events | partial | The record explicitly chooses an internal living-plant habitat without apparent host disease. Its graph is NONMECHANISTIC, its status is PROPOSED, and examples are deliberately deferred. |
| identity | data/raw/metpo.owl; All literal values searched for normalized exact endophytic, endophyte and endophytism, including obsolete-label forms | supports | No exact label or synonym match was found in the complete captured METPO snapshot. The reserved proposal identifier METPO:1039600 is absent there. This is a bounded snapshot conclusion, not a claim about every ontology or later release. |
| ownership | scripts/add_endophytic_trait.py; RECORD constants, build_record and main; v319 class row/proposal and per-record repository history | context_only | The creation writer contains the current definition, synonyms and graph and uses guarded validation/history. It refuses to overwrite an existing target. The proposal and history document the fallback reservation; they are not independent scientific evidence. |
| hierarchy | data/traits/ecology/host_associated.yaml; Parent definition and identity; epiphytic sibling definition; v319/v320 proposal boundaries | supports | Host-associated includes residence on or within plant or animal hosts and is broader than internal plant residence. The surface-residence sibling is distinct. The v319 parent placeholder matches the existing host-associated proposal. |
| bibliography | https://www.ebi.ac.uk/europepmc/webservices/rest/search; Exact DOI lookup for 10.3390/microorganisms5040077 and 10.1128/MMBR.00050-14 | supports | The citations resolve to Kandel, Joubert and Doty 2017, PMID29186821, and Hardoim et al. 2015, PMID26136581. Both are reviews; bibliographic identity does not establish each graph assertion. |
| kandel | https://doi.org/10.3390/microorganisms5040077; Bacterial Endophyte Colonization and Distribution within Plants; abstract and introduction, PMC5748586 full-text XML | partial | The abstract supports internal residence, a non-detrimental association and the process definition used in the record. The introduction acknowledges broader habitat-only usage. The cited process-definition sentence locates colonization within a plant; it does not identify host tissue as the entity executing that process. |
| hardoim | https://pmc.ncbi.nlm.nih.gov/articles/PMC4488371/; The Hidden World within Plants; summary, introduction and History of Endophyte Definitions, especially its concluding definition | partial | The source supports diverse internal microbial residents, reviews the traditional absence-of-apparent-harm convention, and explicitly advocates a broader habitat-based definition independent of host effect. These are different scopes. The record’s narrower convention is defensible but should not be mistaken for consensus between the two reviews. |
| ro | http://purl.obolibrary.org/obo/ro.owl; RO:0002327 enables definition; inherited RO:0002215 and RO:0002595 material-entity/process semantics | refutes | The relation concerns a material entity that can execute the process. A material habitat can be a process location without being its enabler in this sense. This is manual semantic analysis of the record, not an automated domain/range failure. |
| model | src/traitmech/schema/traitmech.yaml; Trait category, term kind and CausalNodeTypeEnum; grounding policy; predicate mapping; v8 confers proposal | supports | ECOLOGY, CLASS and NONMECHANISTIC fit a broad host-habitat trait. Generic habitat/process/trait nodes are permitted. The confers predicate is a documented local proposal, and permissive enables gates do not prove support for this particular assertion. |
| bounded-search | Local repository working tree at f25e2af0b38a8303b13f627a9a5c33b36af4b3d2; Ignored-and-hidden-inclusive identity and ownership searches; full target read | context_only | The target identifier resolves to one maintained record. Searches located its creation writer, proposal and history. No direct DO_NOT_WORK match was found. No additional review target or missing biological mechanism is inferred. |

## Limits And Additional Notes

- The reviewed literature contains both a traditional no-apparent-harm definition and a broader habitat-only definition. The record adopts the former; this review does not establish universal terminology.
- Europe PMC’s Hardoim full-text XML endpoint returned HTTP500, but the full PMC HTML article was subsequently available and inspected. This recovered access is distinguished from the failed endpoint.
- Canonical examples were not newly curated; their absence is an explicit optional first-pass gap rather than negative biological evidence.
- RO evidence retains its actual earlier access time. The semantic finding is manual; no OWL reasoning run is claimed.
- Native proposal verification skipped inapplicable enum coverage and did not compile/reason the proposal. The review changes no proposal or schema.
- The earlier corpus checks are from the same unchanged Git base in the first isolated checkout; their original logs, timestamps, baselines, adapter skips and superseded failures are retained.
- This review does not confer human sign-off or change PROPOSED status.
- Batch002 began from a fresh origin/main fetch at f25e2af0b38a8303b13f627a9a5c33b36af4b3d2. Batch001 reviews remain committed in the first isolated checkout and are included in the sweep’s coverage union.
- Only this new immutable review bundle is written. The target, creation writer, proposal, history and generated products remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T040907Z-endophytic
kind: record
repository: CultureBotAI/TraitMech
title: Scientific and source review of endophytic (traitmech:000442)
started_at: '2026-10-20T04:05:18Z'
finished_at: '2026-10-20T04:09:07Z'
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
summary: 'The proposed ecological trait, local fallback identifier, broader host-associated
  parent and scoped definition are defensible. All four quotations were verified,
  and both cited reviews were inspected. Their different definitions of endophyte
  are preserved as a scope limitation. One major finding concerns the first edge:
  a habitat statement is grounded as the stronger RO enables relation. All three nodes
  and both edges were assessed; no universal mechanism or mandatory example is inferred.'
source:
  git_revision: f25e2af0b38a8303b13f627a9a5c33b36af4b3d2
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
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/ecology/endophytic.yaml
    sha256: a71d78c4bde350bd7941f5e5e7340207d67ee1d86cfa7ee76bc7236c10221d6a
    role: target
  - path: data/traits/ecology/epiphytic.yaml
    sha256: 98678827caa570a3f00e302059beadbb8b72dc2341c8eb5322621ead264ac4b1
    role: context
  - path: data/traits/ecology/host_associated.yaml
    sha256: 8f39eb631802725d79cec85d1d80e0a2f24b2fb74940473bc39b32a2c57d6384
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
  - path: history/records/endophytic/2026-09-28T193953Z-codex-532a66.yaml
    sha256: 1d7d0bdb6c57b54ef0a8ecb848d8f556f4be2eddf938ddfd963354b6c0f7b96c
    role: context
  - path: mappings/predicate_grounding.tsv
    sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
    role: context
  - path: proposals/metpo_traitmech_v319/metpo_proposal_classes_robot.tsv
    sha256: afcd36950f37d75f6b84660ec36b247a0af5280e9223a2c0d59f3b445fee881c
    role: context
  - path: proposals/metpo_traitmech_v319/proposal.md
    sha256: 469844be8ec8d06cef198ccf9d4526cedb009fe0618cd1fd32265bea83316f36
    role: context
  - path: proposals/metpo_traitmech_v320/metpo_proposal_classes_robot.tsv
    sha256: 05d2e7df3a63c205c600f192236ee6b049d6240fcc0c4777a136aa3cc86fa9dc
    role: context
  - path: proposals/metpo_traitmech_v320/proposal.md
    sha256: 58883053b8d6f5d5158a24d95fdc7c690886cdf1447cb7068512bc4ccdddafa6
    role: context
  - path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
    role: context
  - path: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
    role: context
  - path: scripts/add_endophytic_trait.py
    sha256: 6b97941236c61a8fbc220b923d418b0a0674811636a1a07aae273c09e72f2120
    role: context
  - path: scripts/audit_causal_graphs.py
    sha256: e0c26506c9de712700317284f142097e7bf69334806b8010db5d6517e905e834
    role: context
  - path: scripts/curate_knowledge_gaps.py
    sha256: 9e0fb7e01a901d84189a28f1912a2552f28d2da8733c113589e4947359d48c73
    role: context
  - path: scripts/migrate_microbe_domain_edges.py
    sha256: 5187ccfb2897d415b243792a27afd6002c0eea4b167068639ff5be73ed583bb6
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
- target_id: traitmech:000442
  path: data/traits/ecology/endophytic.yaml
  label: endophytic
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endophytic.yaml
    role: Maintained scientific record; future changes require guarded curation and
      history
  - repository: CultureBotAI/TraitMech
    path: scripts/add_endophytic_trait.py
    role: Maintained trait creation writer and proposal constants
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: First record in batch 002 and eleventh newly covered record overall,
    following the validated inventory from batch 001 in lexicographic path order.
    Exactly one entire TraitRecord.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000442
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000442
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - traitmech:000442
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - traitmech:000442
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - traitmech:000442
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1276 history records checked, zero invalid links; integrity does not establish
    scientific correctness or human sign-off.
  evidence_ids:
  - check-validate-history
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - traitmech:000442
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - traitmech:000442
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - traitmech:000442
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: endophytic-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000442
  command: just validate data/traits/ecology/endophytic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The selected record validates.
  evidence_ids:
  - check-endophytic-validate
- check_id: endophytic-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000442
  command: just validate-strict data/traits/ecology/endophytic.yaml --out /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endophytic-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero error rows.
  evidence_ids:
  - check-endophytic-strict
- check_id: endophytic-snippets-network
  name: Focused source snippet verification
  status: passed
  required: true
  target_ids:
  - traitmech:000442
  command: just verify-snippets --record data/traits/ecology/endophytic.yaml --out
    /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endophytic-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Four snippets across two references were VERIFIED. Source identity, context
    and the meaning of the cited relation were assessed separately.
  evidence_ids:
  - check-endophytic-snippets-network
- check_id: endophytic-proposal
  name: Native proposal verification
  status: passed
  required: true
  target_ids:
  - traitmech:000442
  command: just verify-proposal metpo_traitmech_v319 --skip-scope-c
  exit_code: 0
  expected_exit_code: 0
  summary: The one-class v319 cohort passes. Scope-C checking was explicitly skipped
    because this cohort proposes no enum vocabulary; this is not an OWL reasoning
    result.
  evidence_ids:
  - check-endophytic-proposal
- check_id: expression-applicability
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000442
  summary: This broad habitat record asserts no gene, protein, strain or transcriptomics
    dataset. No expression-module match is required or inferred.
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; metadata validate-history.json
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: 1276 history records checked, zero invalid links; integrity does not establish
    scientific correctness or human sign-off.
  snapshot_sha256: 1fc48f1203fbfcd27b1243e4e147afb367aebfc592b496b352201058c6ee85d2
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-endophytic-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endophytic-validate.log
  locator: Executed 2026-10-20T04:05:31Z through 2026-10-20T04:05:32Z; metadata endophytic-validate.json
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: The selected record validates.
  snapshot_sha256: c5f0fcb88032b187c28f4f3c48bd7c970e05a4801c97fa85653588c53a9f164e
- evidence_id: check-endophytic-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endophytic-strict.log
  locator: Executed 2026-10-20T04:05:31Z through 2026-10-20T04:05:32Z; metadata endophytic-strict.json
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: One file scanned; zero error rows.
  snapshot_sha256: ab08a21986c4b7657c656787e87727f0008d3f0e78579e4f65309a2517b48d5f
- evidence_id: check-endophytic-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endophytic-snippets-network.log
  locator: Executed 2026-10-20T04:05:52Z through 2026-10-20T04:05:56Z; metadata endophytic-snippets-network.json
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: Four snippets across two references were VERIFIED. Source identity, context
    and the meaning of the cited relation were assessed separately.
  snapshot_sha256: 73b812de0afb2c9323d3d792ca3d7191a00a3c8149df3cd6088b2e5f18d38814
- evidence_id: check-endophytic-proposal
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endophytic-proposal.log
  locator: Executed 2026-10-20T04:07:22Z through 2026-10-20T04:07:22Z; metadata endophytic-proposal.json
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: The one-class v319 cohort passes. Scope-C checking was explicitly skipped
    because this cohort proposes no enum vocabulary; this is not an OWL reasoning
    result.
  snapshot_sha256: f45eca9dc20ff762d0c150c7ec4675d3174561d3e259e62b6b00b57fb59244bc
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/endophytic.yaml
  locator: Entire record; three nodes, two edges, two references and two history events
  accessed_at: '2026-10-20T04:09:07Z'
  support: partial
  summary: The record explicitly chooses an internal living-plant habitat without
    apparent host disease. Its graph is NONMECHANISTIC, its status is PROPOSED, and
    examples are deliberately deferred.
  snapshot_sha256: a71d78c4bde350bd7941f5e5e7340207d67ee1d86cfa7ee76bc7236c10221d6a
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl
  locator: All literal values searched for normalized exact endophytic, endophyte
    and endophytism, including obsolete-label forms
  accessed_at: '2026-10-20T04:05:51Z'
  support: supports
  summary: No exact label or synonym match was found in the complete captured METPO
    snapshot. The reserved proposal identifier METPO:1039600 is absent there. This
    is a bounded snapshot conclusion, not a claim about every ontology or later release.
  snapshot_sha256: 83006399e7e9cbe3c5b8713f10b9fd6e9f59e34f9a70bee17b334c268df98a54
- evidence_id: ownership
  kind: record_content
  reference: scripts/add_endophytic_trait.py
  locator: RECORD constants, build_record and main; v319 class row/proposal and per-record
    repository history
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: The creation writer contains the current definition, synonyms and graph
    and uses guarded validation/history. It refuses to overwrite an existing target.
    The proposal and history document the fallback reservation; they are not independent
    scientific evidence.
- evidence_id: hierarchy
  kind: record_content
  reference: data/traits/ecology/host_associated.yaml
  locator: Parent definition and identity; epiphytic sibling definition; v319/v320
    proposal boundaries
  accessed_at: '2026-10-20T04:09:07Z'
  support: supports
  summary: Host-associated includes residence on or within plant or animal hosts and
    is broader than internal plant residence. The surface-residence sibling is distinct.
    The v319 parent placeholder matches the existing host-associated proposal.
- evidence_id: bibliography
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search
  locator: Exact DOI lookup for 10.3390/microorganisms5040077 and 10.1128/MMBR.00050-14
  accessed_at: '2026-10-20T04:06:12Z'
  support: supports
  summary: The citations resolve to Kandel, Joubert and Doty 2017, PMID29186821, and
    Hardoim et al. 2015, PMID26136581. Both are reviews; bibliographic identity does
    not establish each graph assertion.
  snapshot_sha256: cdd6555c33f8d306029ea0d6b950bc2257b07e445fab0453c0f5251726571e2d
- evidence_id: kandel
  kind: primary_source
  reference: https://doi.org/10.3390/microorganisms5040077
  locator: Bacterial Endophyte Colonization and Distribution within Plants; abstract
    and introduction, PMC5748586 full-text XML
  accessed_at: '2026-10-20T04:06:12Z'
  support: partial
  summary: The abstract supports internal residence, a non-detrimental association
    and the process definition used in the record. The introduction acknowledges broader
    habitat-only usage. The cited process-definition sentence locates colonization
    within a plant; it does not identify host tissue as the entity executing that
    process.
  snapshot_sha256: aadab6a5cd1843b956bd758cbf72112db352c4fd6a224248d91224bf99cf9ea5
- evidence_id: hardoim
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4488371/
  locator: The Hidden World within Plants; summary, introduction and History of Endophyte
    Definitions, especially its concluding definition
  accessed_at: '2026-10-20T04:07:23Z'
  support: partial
  summary: The source supports diverse internal microbial residents, reviews the traditional
    absence-of-apparent-harm convention, and explicitly advocates a broader habitat-based
    definition independent of host effect. These are different scopes. The record’s
    narrower convention is defensible but should not be mistaken for consensus between
    the two reviews.
  snapshot_sha256: 3037e04fd8b13024addb9f79f99c1cfcfb9541f0e1bbdbe23e78dca9436afbf9
- evidence_id: ro
  kind: authority
  reference: http://purl.obolibrary.org/obo/ro.owl
  locator: RO:0002327 enables definition; inherited RO:0002215 and RO:0002595 material-entity/process
    semantics
  accessed_at: '2026-10-19T23:34:08Z'
  support: refutes
  summary: The relation concerns a material entity that can execute the process. A
    material habitat can be a process location without being its enabler in this sense.
    This is manual semantic analysis of the record, not an automated domain/range
    failure.
  snapshot_sha256: 3120f8e09fcf819197ecf3b15f27d6633811b297e1f6a88aad8fd86d79b616bb
- evidence_id: model
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Trait category, term kind and CausalNodeTypeEnum; grounding policy; predicate
    mapping; v8 confers proposal
  accessed_at: '2026-10-20T04:09:07Z'
  support: supports
  summary: ECOLOGY, CLASS and NONMECHANISTIC fit a broad host-habitat trait. Generic
    habitat/process/trait nodes are permitted. The confers predicate is a documented
    local proposal, and permissive enables gates do not prove support for this particular
    assertion.
- evidence_id: bounded-search
  kind: search
  reference: Local repository working tree at f25e2af0b38a8303b13f627a9a5c33b36af4b3d2
  locator: Ignored-and-hidden-inclusive identity and ownership searches; full target
    read
  accessed_at: '2026-10-20T04:09:07Z'
  support: context_only
  summary: The target identifier resolves to one maintained record. Searches located
    its creation writer, proposal and history. No direct DO_NOT_WORK match was found.
    No additional review target or missing biological mechanism is inferred.
  search_scope: rg --no-ignore --hidden for endophytic, endophyte, endophytism, traitmech:000442
    and METPO:1039600 over data/traits, scripts, history, mappings, proposals, conf
    and DO_NOT_WORK.md; complete captured METPO literal search separately recorded.
    Results are bounded to these local surfaces, with ignored files included.
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, label, synonyms, polarity and kind'
  outcome: supported
  target_ids:
  - traitmech:000442
  summary: One ecological trait is identified. The fallback and pending proposal are
    documented. The endophyte alias is interpreted as conventional trait-bearing terminology,
    not an organism-class equivalence assertion; the related endophytism alias does
    not erase broader usage in the literature.
  evidence_ids:
  - record
  - identity
  - ownership
  - kandel
  - hardoim
  - bounded-search
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: definition and concept boundary'
  outcome: supported
  target_ids:
  - traitmech:000442
  summary: The no-apparent-disease convention has source support. The inspected papers
    also discuss broader usage; this review preserves that distinction rather than
    treating both papers as endorsing an identical boundary.
  evidence_ids:
  - record
  - kandel
  - hardoim
  dimensions:
  - name: definition_convention
    value: Internal living-plant residence without apparent host disease
    definition: The record’s selected ecological scope; not a claim that all endophyte
      literature excludes harmful associations.
    evidence_ids:
    - record
    - kandel
    - hardoim
  - name: source_category
    value: Two scholarly reviews
    definition: Conceptual synthesis and ecological background, not two independent
      experiments establishing the graph relation.
    evidence_ids:
    - bibliography
- assessment_id: hierarchy
  area: consistency
  topic: 'Native checklist: strictly broader parent and sibling distinction'
  outcome: supported
  target_ids:
  - traitmech:000442
  summary: The host-associated parent is broader and the internal/surface distinction
    from epiphytic is coherent. No requirement for plant growth promotion or nitrogen
    fixation is added.
  evidence_ids:
  - record
  - hierarchy
  - kandel
  - hardoim
- assessment_id: category
  area: representation
  topic: 'Native checklist: category and graph scope'
  outcome: supported
  target_ids:
  - traitmech:000442
  summary: The class describes an ecological habitat association. NONMECHANISTIC scope
    is appropriate, and the generic nodes do not require a fabricated universal molecular
    mechanism.
  evidence_ids:
  - record
  - model
- assessment_id: examples
  area: completeness
  topic: 'Native checklist: canonical-example disposition'
  outcome: supported
  target_ids:
  - traitmech:000442
  summary: Examples are optional and the history explicitly records a first-pass evidence
    gap. No unsupported strain or species is asserted. This is not an exhaustive claim
    that no suitable example exists.
  evidence_ids:
  - record
  - ownership
- assessment_id: evidence
  area: evidence
  topic: 'Native checklist: references, quotations and nearest support'
  outcome: concern
  target_ids:
  - traitmech:000442
  summary: Both article identities resolve and all four quotations match. Exact wording
    alone does not establish the first edge’s stronger causal/ontology interpretation.
    The two sources’ definition scopes remain distinct.
  evidence_ids:
  - bibliography
  - kandel
  - hardoim
  - check-endophytic-snippets-network
  - ro
- assessment_id: graph
  area: graph
  topic: 'Native checklist: all three nodes and both edges'
  outcome: concern
  target_ids:
  - traitmech:000442
  summary: The habitat, colonization process and ecological trait have distinct intended
    meanings, and all endpoints resolve. Edge0 presents a location definition as RO
    enables. Edge1 is a conceptual realization statement under the record’s selected
    endophytic convention and uses a documented proposed predicate.
  evidence_ids:
  - record
  - kandel
  - hardoim
  - ro
  - model
  details: 'Zero-based ledger: edge0 internal_plant_tissue/enables/endophytic_colonization
    is not supported at the semantics of RO:0002327 by the quoted definition; material
    subject type alone is insufficient. Edge1 endophytic_colonization/confers/endophytic_trait
    is a nonmechanistic conceptual bridge, not an experimental demonstration of one
    universal route. Its meaning remains bounded by the no-apparent-disease definition
    of the target node and cited convention.'
- assessment_id: discussion
  area: completeness
  topic: 'Native checklist: discussions and datasets'
  outcome: not_applicable
  target_ids:
  - traitmech:000442
  summary: The complete target contains no discussion or dataset assertion. Optional
    fields need not be added simply to populate the model.
  evidence_ids:
  - record
- assessment_id: status
  area: provenance
  topic: 'Native checklist: status, history and native checks'
  outcome: supported
  target_ids:
  - traitmech:000442
  summary: PROPOSED status and explicitly AI-assisted creation/history are consistent
    with the documented work. No human scientific sign-off or status promotion is
    claimed. Focused checks pass; earlier same-base corpus diagnostics retain their
    limitations.
  evidence_ids:
  - record
  - ownership
  - check-endophytic-validate
  - check-endophytic-strict
  - check-endophytic-proposal
  - check-validate-history
findings:
- finding_id: habitat-enables-overclaim
  issue_key: endophytic-habitat-enables-overclaim
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: A habitat statement is assigned the stronger RO enables relation
  description: The first edge’s description and quotation say where the microbial
    process takes place. RO:0002327 instead identifies a material entity capable of
    executing that process. The record describes the plant tissue as habitat, not
    as the entity performing microbial entry, growth and multiplication. This is an
    evidence-to-predicate mismatch, not a claim that tissue cannot matter causally
    and not a formal material-entity domain violation.
  target_ids:
  - traitmech:000442
  field_paths:
  - causal_graphs[0].edges[0].predicate_id
  - causal_graphs[0].edges[0].description
  - causal_graphs[0].edges[0].evidence
  evidence_ids:
  - record
  - kandel
  - ro
  - model
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endophytic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/add_endophytic_trait.py
    role: Maintained creation constants; writer refuses to overwrite an existing target
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: align-habitat-relation
  description: Represent the source-supported habitat relation at its actual semantic
    strength and reconcile the maintained creation constants.
  finding_ids:
  - habitat-enables-overclaim
  target_ids:
  - traitmech:000442
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endophytic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/add_endophytic_trait.py
    role: Maintained creation constants; writer refuses to overwrite an existing target
  acceptance_checks:
  - Inspect the intended relation’s definition and direction as well as endpoint types;
    do not select an identifier from its label alone.
  - Retain a conceptual ecological graph without inventing a causal mechanism to justify
    an existing edge.
  - The creation script is an owner to update, not a migration to replay over an existing
    record.
  - After separately authorized curation, use guarded writes/history and run focused
    validation, strict validation, snippet checks, graph/grounding checks and applicable
    qc.
limitations:
- The reviewed literature contains both a traditional no-apparent-harm definition
  and a broader habitat-only definition. The record adopts the former; this review
  does not establish universal terminology.
- Europe PMC’s Hardoim full-text XML endpoint returned HTTP500, but the full PMC HTML
  article was subsequently available and inspected. This recovered access is distinguished
  from the failed endpoint.
- Canonical examples were not newly curated; their absence is an explicit optional
  first-pass gap rather than negative biological evidence.
- RO evidence retains its actual earlier access time. The semantic finding is manual;
  no OWL reasoning run is claimed.
- Native proposal verification skipped inapplicable enum coverage and did not compile/reason
  the proposal. The review changes no proposal or schema.
- The earlier corpus checks are from the same unchanged Git base in the first isolated
  checkout; their original logs, timestamps, baselines, adapter skips and superseded
  failures are retained.
- This review does not confer human sign-off or change PROPOSED status.
notes:
- Batch002 began from a fresh origin/main fetch at f25e2af0b38a8303b13f627a9a5c33b36af4b3d2.
  Batch001 reviews remain committed in the first isolated checkout and are included
  in the sweep’s coverage union.
- Only this new immutable review bundle is written. The target, creation writer, proposal,
  history and generated products remain unchanged.
tags:
- record-review
- endophytic
- ecology
- needs-curation
```
