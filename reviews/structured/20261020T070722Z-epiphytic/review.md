# Scientific and source review of epiphytic (traitmech:000443)

- Review: 20261020T070722Z-epiphytic
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-20T07:02:01Z
- Finished UTC: 2026-10-20T07:07:22Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The fallback identity, broader parent, surface-residence definition and NONMECHANISTIC scope are defensible. Both cited papers were inspected and all four quotation occurrences were accounted for, including two unresolved by the automated fetcher. One major finding concerns a habitat statement grounded as RO enables. One minor finding concerns inconsistent boundary prose in the companion proposal. All three nodes and both edges were assessed; optional examples were explicitly deferred in the record history.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Third record in batch002, selected by the union of validated native inventories from the two isolated sweep checkouts. One entire previously uncovered TraitRecord in lexicographic path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f25e2af0b38a8303b13f627a9a5c33b36af4b3d2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000443 | data/traits/ecology/epiphytic.yaml | maintained | epiphytic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000443 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000443 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000443 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | traitmech:000443 | 1276 history records checked, zero invalid links; integrity does not establish scientific correctness or human sign-off. |
| Initial full-product validation | failed | False | traitmech:000443 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000443 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000443 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | traitmech:000443 | The selected record validates. |
| Focused strict validation | passed | True | traitmech:000443 | One file scanned; zero error rows. |
| Focused source snippet verification | passed | True | traitmech:000443 | Four occurrences across two references: two VERIFIED and two UNRESOLVED. Manual inspection recovered the older article and confirmed its repeated quotation; the automated statuses are retained. |
| Native proposal verification | passed | True | traitmech:000443 | The one-class v320 cohort passes with inapplicable enum scope explicitly skipped. This does not constitute an OWL reasoning run. |
| Expression-module applicability | not_applicable | False | traitmech:000443 | No gene, protein, strain or transcriptomics dataset is asserted. Expression-module evidence is not applicable to this broad habitat concept. |

## Scientific And Domain Assessments

### Native checklist: identifier, label, aliases, polarity and kind

identity: supported. Targets: traitmech:000443.

One ecological class with a documented fallback and reservation is identified. Epiphyte is conventional trait-bearing terminology; no equivalence to an organism class is asserted. Phyllosphere association is appropriately related rather than exact.

### Native checklist: definition and source boundary

evidence: supported. Targets: traitmech:000443.

The cited conceptual scope supports the maintained definition. The broader aerial-surface wording is supported by the older article as well as the introductory context of the definition source.

### Native checklist: broader parent and proposal consistency

consistency: concern. Targets: traitmech:000443.

The local parent is broader and the internal/surface distinction is coherent. The proposal introduces an extra disease exclusion; its prose should be reconciled with the record and cited concept.

### Native checklist: category, term kind and graph scope

representation: supported. Targets: traitmech:000443.

ECOLOGY and CLASS fit this habitat trait. NONMECHANISTIC explicitly avoids claiming one molecular route. Generic nodes are permitted.

### Native checklist: canonical-example disposition

completeness: supported. Targets: traitmech:000443.

The record history explicitly defers examples. Examples are optional; no unsupported strain claim needs removal, and this review makes no claim that suitable examples do not exist.

### Native checklist: all citations and nearest support

evidence: concern. Targets: traitmech:000443.

Both DOI identities and all four quotation occurrences were verified through the combined automated and manual checks. Exact wording does not resolve the first edge’s stronger predicate interpretation.

### Native checklist: all nodes, edges and anchors

graph: concern. Targets: traitmech:000443.

Three unique nodes and both endpoint pairs resolve. The local trait grounding is exact. Edge0 overinterprets a habitat statement; edge1 is a conceptual realization bridge under a documented proposed predicate.

Zero-based ledger: node0 is an environmental habitat, node1 describes continuing microbial colonization/residence, and node2 is the ecological trait. Edge0 external_plant_surface/enables/epiphytic_colonization has a source-to-predicate mismatch. Edge1 epiphytic_colonization/confers/epiphytic_trait is appropriate only as the declared nonmechanistic conceptual bridge. No universal causal mechanism or experimental establishment of that relation is claimed.

### Native checklist: discussion and dataset fields

completeness: not_applicable. Targets: traitmech:000443.

The complete target has no discussion or dataset assertion. Optional fields need not be populated.

### Native checklist: status, curation history and checks

provenance: supported. Targets: traitmech:000443.

PROPOSED and explicitly AI-assisted history are coherent. Checks establish their stated technical scopes only; neither review nor green validation promotes scientific status or supplies human sign-off.

## Findings

### habitat-enables-overclaim: Habitat evidence does not establish RO enables

major / open / confirmed; issue key: epiphytic-habitat-enables-overclaim.

The first edge describes the plant surface as the place where the population occurs. Its RO identifier requires an actor that can execute the process. The citation does not establish that stronger relation. This is a semantic evidence mismatch, not a formal claim that a material surface violates the domain.

### proposal-disease-exclusion: Companion proposal adds an unsupported disease exclusion

minor / open / confirmed; issue key: epiphytic-proposal-disease-exclusion.

The proposal’s Proposed Classes paragraph excludes plant pathogenicity with apparent disease; its hierarchy prose and template comment reinforce that separation. The record definition has no such restriction. The definition source treats habitat and host effect as overlapping classifications. This is a bounded proposal-prose inconsistency, not a claim that the current target definition excludes disease.

## Recommended Actions And Acceptance Checks

### align-habitat-relation

Align the first relation and creation constants with the actual meaning supported by the habitat evidence.

- Inspect relation definitions, direction and endpoint types; label similarity alone is insufficient.
- Retain the declared ecological scope without inventing a mechanism to justify an existing edge.
- After separately authorized curation, use guarded writes/history and run focused validation, strict validation, source snippets, grounding/graph checks and applicable qc. Do not replay the creation-only writer as a migration.

### reconcile-proposal-boundary

Reconcile the maintained proposal boundary prose and class-template comment with the target and its definition source.

- Distinguish different traits from mutually exclusive organisms or life-cycle phases.
- Verify agreement among the proposal prose, class row and maintained definition; retain the documented fallback reservation.
- Run native proposal verification and applicable validation after any separately authorized edit. No remote submission is authorized by this review.

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
| check-epiphytic-validate | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/epiphytic-validate.log; Executed 2026-10-20T07:02:09Z through 2026-10-20T07:02:10Z; metadata epiphytic-validate.json | context_only | The selected record validates. |
| check-epiphytic-strict | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/epiphytic-strict.log; Executed 2026-10-20T07:02:09Z through 2026-10-20T07:02:11Z; metadata epiphytic-strict.json | context_only | One file scanned; zero error rows. |
| check-epiphytic-snippets-network | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/epiphytic-snippets-network.log; Executed 2026-10-20T07:02:40Z through 2026-10-20T07:02:47Z; metadata epiphytic-snippets-network.json | context_only | Four occurrences across two references: two VERIFIED and two UNRESOLVED. Manual inspection recovered the older article and confirmed its repeated quotation; the automated statuses are retained. |
| check-epiphytic-proposal | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/epiphytic-proposal.log; Executed 2026-10-20T07:02:39Z through 2026-10-20T07:02:39Z; metadata epiphytic-proposal.json | context_only | The one-class v320 cohort passes with inapplicable enum scope explicitly skipped. This does not constitute an OWL reasoning run. |
| record | data/traits/ecology/epiphytic.yaml; Entire record, including three nodes, two edges, two references and both history entries | partial | The record describes residence on living aerial plant surfaces, uses PROPOSED status and explicitly defers optional canonical examples. |
| identity | data/raw/metpo.owl; Complete captured METPO literals; exact normalized epiphytic, epiphyte, epiphytism and phyllosphere association, including obsolete-label forms | supports | No exact match was found in that complete snapshot; reserved METPO:1039700 is absent there. The local fallback is documented by v320. This bounded result is not a claim about later releases. |
| ownership | scripts/add_epiphytic_trait.py; Entire writer; per-record history; v320 class row and proposal | context_only | The creation constants reproduce the current record and the writer refuses to overwrite an existing target. The local reservation and AI-assisted provenance are explicit. Proposal prose additionally excludes plant pathogenicity with apparent disease, a restriction absent from the maintained definition. |
| hierarchy | data/traits/ecology/host_associated.yaml; Parent definition; endophytic sibling; v319/v320 proposal boundaries | supports | The parent includes host-surface and internal residence. The selected surface location is narrower; internal plant residence is a distinguishable sibling concept, without requiring organism-level disjointness. |
| bibliography | https://www.ebi.ac.uk/europepmc/webservices/rest/search; Exact DOI queries, recorded separately in epiphytic-sources/access.json | supports | Fones et al. 2024 resolves to PMID39113027/PMC11304629; Lindow and Brandl 2003 resolves to PMID12676659/PMC154815. Both are scholarly reviews, not independent experiments for each graph edge. |
| fones | https://doi.org/10.1186/s12915-024-01967-1; Abstract and introductory habitat definitions; PMC11304629 full-text XML | partial | The abstract confirms leaf-surface residence. The introduction distinguishes internal and external above-ground compartments and allows several host-effect categories in those niches. Thus habitat identity does not imply exclusion of disease-associated microbes. |
| lindow | https://pmc.ncbi.nlm.nih.gov/articles/PMC154815/; Opening habitat-definition paragraph and introductory scope; full PMC HTML | partial | The record’s repeated sentence is exact in the opening paragraph. That context includes aerial surfaces beyond leaves and several microbial groups. It describes a habitat, without establishing the surface as the actor executing microbial colonization. |
| ro | http://purl.obolibrary.org/obo/ro.owl; RO:0002327 definition and inherited capability/material-entity-to-process semantics | refutes | Enables identifies an entity capable of and acting to execute a process. A habitat location alone does not establish this meaning. This semantic assessment is distinct from a formal endpoint-type violation. |
| model | src/traitmech/schema/traitmech.yaml; ECOLOGY, CLASS, NONMECHANISTIC; node types; grounding policy; predicate mapping and v8 confers row | supports | The broad ecological representation is permitted. Confers is a documented local proposal, not an active upstream identifier. Permissive predicate gates do not establish source support. |
| search | Local repository working tree at f25e2af0b38a8303b13f627a9a5c33b36af4b3d2; Ignored-and-hidden-inclusive identity, owner and exclusion search | context_only | The identifier identifies one maintained record. Its writer, proposal and history were located; no direct exclusion match was found. |

## Limits And Additional Notes

- The automated source check returned two UNRESOLVED occurrences for Lindow and Brandl. Its XML endpoint returned HTTP500; full PMC HTML was subsequently retrieved and the quoted sentence manually confirmed. These outcomes are not silently relabeled.
- This review inspected concept and habitat passages in the cited reviews, not every downstream reference or a comprehensive experimental literature set.
- No canonical examples, new causal steps or assay procedures were curated.
- RO evidence retains its actual earlier access time. No automated OWL entailment check is claimed.
- Native proposal verification skipped inapplicable enum coverage and did not compile or reason the proposal.
- Earlier full-corpus diagnostics are retained with actual same-base logs, baselines, superseded network failures and 123 no-adapter product skips; they do not certify every identifier.
- The review supplies no human sign-off and changes no scientific status.
- Batch002 is based on fresh origin/main f25e2af0b38a8303b13f627a9a5c33b36af4b3d2. Coverage includes locally committed batch001 through the native inventory union.
- Only this immutable review bundle is written; the scientific record, proposal, writer, history and generated products remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T070722Z-epiphytic
kind: record
repository: CultureBotAI/TraitMech
title: Scientific and source review of epiphytic (traitmech:000443)
started_at: '2026-10-20T07:02:01Z'
finished_at: '2026-10-20T07:07:22Z'
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
summary: The fallback identity, broader parent, surface-residence definition and NONMECHANISTIC
  scope are defensible. Both cited papers were inspected and all four quotation occurrences
  were accounted for, including two unresolved by the automated fetcher. One major
  finding concerns a habitat statement grounded as RO enables. One minor finding concerns
  inconsistent boundary prose in the companion proposal. All three nodes and both
  edges were assessed; optional examples were explicitly deferred in the record history.
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
    role: context
  - path: data/traits/ecology/epiphytic.yaml
    sha256: 98678827caa570a3f00e302059beadbb8b72dc2341c8eb5322621ead264ac4b1
    role: target
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
  - path: history/records/epiphytic/2026-09-28T202112Z-codex-eeb2ca.yaml
    sha256: 768e11780063a6053107d8a14835fe41c49c083e5f0baeb116fc2eae46b1bc91
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
  - path: scripts/add_epiphytic_trait.py
    sha256: edb4967b83e7b71cc7f83e1296bf9361d9bfc11b0c86078a252a66bac7aa05e5
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
- target_id: traitmech:000443
  path: data/traits/ecology/epiphytic.yaml
  label: epiphytic
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/epiphytic.yaml
    role: Maintained scientific record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_epiphytic_trait.py
    role: Maintained creation writer and proposal constants
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Third record in batch002, selected by the union of validated native inventories
    from the two isolated sweep checkouts. One entire previously uncovered TraitRecord
    in lexicographic path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000443
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000443
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
  - traitmech:000443
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
  - traitmech:000443
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
  - traitmech:000443
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
  - traitmech:000443
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
  - traitmech:000443
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
  - traitmech:000443
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: epiphytic-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000443
  command: just validate data/traits/ecology/epiphytic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The selected record validates.
  evidence_ids:
  - check-epiphytic-validate
- check_id: epiphytic-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000443
  command: just validate-strict data/traits/ecology/epiphytic.yaml --out /private/tmp/traitmech-record-sweep-002.mdt7dqwk/epiphytic-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero error rows.
  evidence_ids:
  - check-epiphytic-strict
- check_id: epiphytic-snippets-network
  name: Focused source snippet verification
  status: passed
  required: true
  target_ids:
  - traitmech:000443
  command: just verify-snippets --record data/traits/ecology/epiphytic.yaml --out
    /private/tmp/traitmech-record-sweep-002.mdt7dqwk/epiphytic-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Four occurrences across two references: two VERIFIED and two UNRESOLVED.
    Manual inspection recovered the older article and confirmed its repeated quotation;
    the automated statuses are retained.'
  evidence_ids:
  - check-epiphytic-snippets-network
- check_id: epiphytic-proposal
  name: Native proposal verification
  status: passed
  required: true
  target_ids:
  - traitmech:000443
  command: just verify-proposal metpo_traitmech_v320 --skip-scope-c
  exit_code: 0
  expected_exit_code: 0
  summary: The one-class v320 cohort passes with inapplicable enum scope explicitly
    skipped. This does not constitute an OWL reasoning run.
  evidence_ids:
  - check-epiphytic-proposal
- check_id: expression-applicability
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000443
  summary: No gene, protein, strain or transcriptomics dataset is asserted. Expression-module
    evidence is not applicable to this broad habitat concept.
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; metadata validate-history.json
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: 1276 history records checked, zero invalid links; integrity does not establish
    scientific correctness or human sign-off.
  snapshot_sha256: 1fc48f1203fbfcd27b1243e4e147afb367aebfc592b496b352201058c6ee85d2
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-epiphytic-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/epiphytic-validate.log
  locator: Executed 2026-10-20T07:02:09Z through 2026-10-20T07:02:10Z; metadata epiphytic-validate.json
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: The selected record validates.
  snapshot_sha256: 114a3f86530167eb249cd0712bdfbf0ed18f5b167124e7db435b180a5958cb56
- evidence_id: check-epiphytic-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/epiphytic-strict.log
  locator: Executed 2026-10-20T07:02:09Z through 2026-10-20T07:02:11Z; metadata epiphytic-strict.json
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: One file scanned; zero error rows.
  snapshot_sha256: 6a6340b7f370cb94da0c8f5b5de6da0a1626a71435bd2f6310ca7ee2a9755700
- evidence_id: check-epiphytic-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/epiphytic-snippets-network.log
  locator: Executed 2026-10-20T07:02:40Z through 2026-10-20T07:02:47Z; metadata epiphytic-snippets-network.json
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: 'Four occurrences across two references: two VERIFIED and two UNRESOLVED.
    Manual inspection recovered the older article and confirmed its repeated quotation;
    the automated statuses are retained.'
  snapshot_sha256: 3ab810c28618822d063f37c5eba59fcd7350eef2b0245f70a9b22c052f6d0df8
- evidence_id: check-epiphytic-proposal
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/epiphytic-proposal.log
  locator: Executed 2026-10-20T07:02:39Z through 2026-10-20T07:02:39Z; metadata epiphytic-proposal.json
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: The one-class v320 cohort passes with inapplicable enum scope explicitly
    skipped. This does not constitute an OWL reasoning run.
  snapshot_sha256: bf89184bf6c5301328b5173b462abbd81f93687cd1e148770012794c20e3e7f8
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/epiphytic.yaml
  locator: Entire record, including three nodes, two edges, two references and both
    history entries
  accessed_at: '2026-10-20T07:07:22Z'
  support: partial
  summary: The record describes residence on living aerial plant surfaces, uses PROPOSED
    status and explicitly defers optional canonical examples.
  snapshot_sha256: 98678827caa570a3f00e302059beadbb8b72dc2341c8eb5322621ead264ac4b1
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl
  locator: Complete captured METPO literals; exact normalized epiphytic, epiphyte,
    epiphytism and phyllosphere association, including obsolete-label forms
  accessed_at: '2026-10-20T07:02:39Z'
  support: supports
  summary: No exact match was found in that complete snapshot; reserved METPO:1039700
    is absent there. The local fallback is documented by v320. This bounded result
    is not a claim about later releases.
  snapshot_sha256: ce27c3d875d28cfeb1d12d2032ecbef0637c5861ba2bf450d429269a86a3e779
- evidence_id: ownership
  kind: record_content
  reference: scripts/add_epiphytic_trait.py
  locator: Entire writer; per-record history; v320 class row and proposal
  accessed_at: '2026-10-20T07:07:22Z'
  support: context_only
  summary: The creation constants reproduce the current record and the writer refuses
    to overwrite an existing target. The local reservation and AI-assisted provenance
    are explicit. Proposal prose additionally excludes plant pathogenicity with apparent
    disease, a restriction absent from the maintained definition.
- evidence_id: hierarchy
  kind: record_content
  reference: data/traits/ecology/host_associated.yaml
  locator: Parent definition; endophytic sibling; v319/v320 proposal boundaries
  accessed_at: '2026-10-20T07:07:22Z'
  support: supports
  summary: The parent includes host-surface and internal residence. The selected surface
    location is narrower; internal plant residence is a distinguishable sibling concept,
    without requiring organism-level disjointness.
- evidence_id: bibliography
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search
  locator: Exact DOI queries, recorded separately in epiphytic-sources/access.json
  accessed_at: '2026-10-20T07:05:38Z'
  support: supports
  summary: Fones et al. 2024 resolves to PMID39113027/PMC11304629; Lindow and Brandl
    2003 resolves to PMID12676659/PMC154815. Both are scholarly reviews, not independent
    experiments for each graph edge.
  snapshot_sha256: 43774f08d96ef5d29306338e4d8044ec34f5a299ec498fe2995dbf94b354b8ef
- evidence_id: fones
  kind: primary_source
  reference: https://doi.org/10.1186/s12915-024-01967-1
  locator: Abstract and introductory habitat definitions; PMC11304629 full-text XML
  accessed_at: '2026-10-20T07:05:35Z'
  support: partial
  summary: The abstract confirms leaf-surface residence. The introduction distinguishes
    internal and external above-ground compartments and allows several host-effect
    categories in those niches. Thus habitat identity does not imply exclusion of
    disease-associated microbes.
  snapshot_sha256: 1a0957aa679e0686f61a44a3107e1a0a6816159a77f755d4f8670673b77d4d86
- evidence_id: lindow
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC154815/
  locator: Opening habitat-definition paragraph and introductory scope; full PMC HTML
  accessed_at: '2026-10-20T07:05:40Z'
  support: partial
  summary: The record’s repeated sentence is exact in the opening paragraph. That
    context includes aerial surfaces beyond leaves and several microbial groups. It
    describes a habitat, without establishing the surface as the actor executing microbial
    colonization.
  snapshot_sha256: ad0a984a5519e1403c4fc31140bcfbbdc9261b419fb80fc4a61ea2cb4326f6a4
- evidence_id: ro
  kind: authority
  reference: http://purl.obolibrary.org/obo/ro.owl
  locator: RO:0002327 definition and inherited capability/material-entity-to-process
    semantics
  accessed_at: '2026-10-19T23:34:08Z'
  support: refutes
  summary: Enables identifies an entity capable of and acting to execute a process.
    A habitat location alone does not establish this meaning. This semantic assessment
    is distinct from a formal endpoint-type violation.
  snapshot_sha256: 3120f8e09fcf819197ecf3b15f27d6633811b297e1f6a88aad8fd86d79b616bb
- evidence_id: model
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: ECOLOGY, CLASS, NONMECHANISTIC; node types; grounding policy; predicate
    mapping and v8 confers row
  accessed_at: '2026-10-20T07:07:22Z'
  support: supports
  summary: The broad ecological representation is permitted. Confers is a documented
    local proposal, not an active upstream identifier. Permissive predicate gates
    do not establish source support.
- evidence_id: search
  kind: search
  reference: Local repository working tree at f25e2af0b38a8303b13f627a9a5c33b36af4b3d2
  locator: Ignored-and-hidden-inclusive identity, owner and exclusion search
  accessed_at: '2026-10-20T07:02:39Z'
  support: context_only
  summary: The identifier identifies one maintained record. Its writer, proposal and
    history were located; no direct exclusion match was found.
  snapshot_sha256: 46a9884b1ba865391723a0cb915378eb25df1e27c948fd9233cf32446aef4cd6
  search_scope: rg --no-ignore --hidden for epiphytic, epiphyte, epiphytism, traitmech:000443
    and METPO:1039700 across data/traits, scripts, history, mappings, proposals, conf
    and DO_NOT_WORK.md. Complete captured METPO literal analysis is recorded separately.
    Ignored files were included.
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, label, aliases, polarity and kind'
  outcome: supported
  target_ids:
  - traitmech:000443
  summary: One ecological class with a documented fallback and reservation is identified.
    Epiphyte is conventional trait-bearing terminology; no equivalence to an organism
    class is asserted. Phyllosphere association is appropriately related rather than
    exact.
  evidence_ids:
  - record
  - identity
  - ownership
  - fones
  - search
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: definition and source boundary'
  outcome: supported
  target_ids:
  - traitmech:000443
  summary: The cited conceptual scope supports the maintained definition. The broader
    aerial-surface wording is supported by the older article as well as the introductory
    context of the definition source.
  evidence_ids:
  - record
  - fones
  - lindow
- assessment_id: hierarchy
  area: consistency
  topic: 'Native checklist: broader parent and proposal consistency'
  outcome: concern
  target_ids:
  - traitmech:000443
  summary: The local parent is broader and the internal/surface distinction is coherent.
    The proposal introduces an extra disease exclusion; its prose should be reconciled
    with the record and cited concept.
  evidence_ids:
  - record
  - hierarchy
  - ownership
  - fones
- assessment_id: category
  area: representation
  topic: 'Native checklist: category, term kind and graph scope'
  outcome: supported
  target_ids:
  - traitmech:000443
  summary: ECOLOGY and CLASS fit this habitat trait. NONMECHANISTIC explicitly avoids
    claiming one molecular route. Generic nodes are permitted.
  evidence_ids:
  - record
  - model
- assessment_id: examples
  area: completeness
  topic: 'Native checklist: canonical-example disposition'
  outcome: supported
  target_ids:
  - traitmech:000443
  summary: The record history explicitly defers examples. Examples are optional; no
    unsupported strain claim needs removal, and this review makes no claim that suitable
    examples do not exist.
  evidence_ids:
  - record
  - ownership
- assessment_id: evidence
  area: evidence
  topic: 'Native checklist: all citations and nearest support'
  outcome: concern
  target_ids:
  - traitmech:000443
  summary: Both DOI identities and all four quotation occurrences were verified through
    the combined automated and manual checks. Exact wording does not resolve the first
    edge’s stronger predicate interpretation.
  evidence_ids:
  - bibliography
  - fones
  - lindow
  - ro
  - check-epiphytic-snippets-network
- assessment_id: graph
  area: graph
  topic: 'Native checklist: all nodes, edges and anchors'
  outcome: concern
  target_ids:
  - traitmech:000443
  summary: Three unique nodes and both endpoint pairs resolve. The local trait grounding
    is exact. Edge0 overinterprets a habitat statement; edge1 is a conceptual realization
    bridge under a documented proposed predicate.
  evidence_ids:
  - record
  - ro
  - model
  - lindow
  - fones
  details: 'Zero-based ledger: node0 is an environmental habitat, node1 describes
    continuing microbial colonization/residence, and node2 is the ecological trait.
    Edge0 external_plant_surface/enables/epiphytic_colonization has a source-to-predicate
    mismatch. Edge1 epiphytic_colonization/confers/epiphytic_trait is appropriate
    only as the declared nonmechanistic conceptual bridge. No universal causal mechanism
    or experimental establishment of that relation is claimed.'
- assessment_id: discussion
  area: completeness
  topic: 'Native checklist: discussion and dataset fields'
  outcome: not_applicable
  target_ids:
  - traitmech:000443
  summary: The complete target has no discussion or dataset assertion. Optional fields
    need not be populated.
  evidence_ids:
  - record
- assessment_id: status
  area: provenance
  topic: 'Native checklist: status, curation history and checks'
  outcome: supported
  target_ids:
  - traitmech:000443
  summary: PROPOSED and explicitly AI-assisted history are coherent. Checks establish
    their stated technical scopes only; neither review nor green validation promotes
    scientific status or supplies human sign-off.
  evidence_ids:
  - record
  - ownership
  - check-epiphytic-validate
  - check-epiphytic-strict
  - check-epiphytic-proposal
  - check-validate-history
findings:
- finding_id: habitat-enables-overclaim
  issue_key: epiphytic-habitat-enables-overclaim
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Habitat evidence does not establish RO enables
  description: The first edge describes the plant surface as the place where the population
    occurs. Its RO identifier requires an actor that can execute the process. The
    citation does not establish that stronger relation. This is a semantic evidence
    mismatch, not a formal claim that a material surface violates the domain.
  target_ids:
  - traitmech:000443
  field_paths:
  - causal_graphs[0].edges[0].predicate_id
  - causal_graphs[0].edges[0].description
  - causal_graphs[0].edges[0].evidence
  evidence_ids:
  - record
  - lindow
  - ro
  - model
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/epiphytic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/add_epiphytic_trait.py
    role: Maintained creation constants; refuses to overwrite existing records
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: proposal-disease-exclusion
  issue_key: epiphytic-proposal-disease-exclusion
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Companion proposal adds an unsupported disease exclusion
  description: The proposal’s Proposed Classes paragraph excludes plant pathogenicity
    with apparent disease; its hierarchy prose and template comment reinforce that
    separation. The record definition has no such restriction. The definition source
    treats habitat and host effect as overlapping classifications. This is a bounded
    proposal-prose inconsistency, not a claim that the current target definition excludes
    disease.
  target_ids:
  - traitmech:000443
  field_paths:
  - definition
  - definition_source
  - curation_history[0].changes
  evidence_ids:
  - record
  - ownership
  - fones
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v320/proposal.md
    role: Maintained explanation of this target’s proposed upstream identity
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v320/metpo_proposal_classes_robot.tsv
    role: Maintained class proposal and boundary comment
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: align-habitat-relation
  description: Align the first relation and creation constants with the actual meaning
    supported by the habitat evidence.
  finding_ids:
  - habitat-enables-overclaim
  target_ids:
  - traitmech:000443
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/epiphytic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/add_epiphytic_trait.py
    role: Maintained creation constants; refuses to overwrite existing records
  acceptance_checks:
  - Inspect relation definitions, direction and endpoint types; label similarity alone
    is insufficient.
  - Retain the declared ecological scope without inventing a mechanism to justify
    an existing edge.
  - After separately authorized curation, use guarded writes/history and run focused
    validation, strict validation, source snippets, grounding/graph checks and applicable
    qc. Do not replay the creation-only writer as a migration.
- action_id: reconcile-proposal-boundary
  description: Reconcile the maintained proposal boundary prose and class-template
    comment with the target and its definition source.
  finding_ids:
  - proposal-disease-exclusion
  target_ids:
  - traitmech:000443
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v320/proposal.md
    role: Maintained explanation of this target’s proposed upstream identity
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v320/metpo_proposal_classes_robot.tsv
    role: Maintained class proposal and boundary comment
  acceptance_checks:
  - Distinguish different traits from mutually exclusive organisms or life-cycle phases.
  - Verify agreement among the proposal prose, class row and maintained definition;
    retain the documented fallback reservation.
  - Run native proposal verification and applicable validation after any separately
    authorized edit. No remote submission is authorized by this review.
limitations:
- The automated source check returned two UNRESOLVED occurrences for Lindow and Brandl.
  Its XML endpoint returned HTTP500; full PMC HTML was subsequently retrieved and
  the quoted sentence manually confirmed. These outcomes are not silently relabeled.
- This review inspected concept and habitat passages in the cited reviews, not every
  downstream reference or a comprehensive experimental literature set.
- No canonical examples, new causal steps or assay procedures were curated.
- RO evidence retains its actual earlier access time. No automated OWL entailment
  check is claimed.
- Native proposal verification skipped inapplicable enum coverage and did not compile
  or reason the proposal.
- Earlier full-corpus diagnostics are retained with actual same-base logs, baselines,
  superseded network failures and 123 no-adapter product skips; they do not certify
  every identifier.
- The review supplies no human sign-off and changes no scientific status.
notes:
- Batch002 is based on fresh origin/main f25e2af0b38a8303b13f627a9a5c33b36af4b3d2.
  Coverage includes locally committed batch001 through the native inventory union.
- Only this immutable review bundle is written; the scientific record, proposal, writer,
  history and generated products remain unchanged.
tags:
- record-review
- epiphytic
- ecology
- needs-curation
```
