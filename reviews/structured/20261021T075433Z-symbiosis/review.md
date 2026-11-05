# Concept, source and ontology review of symbiosis (traitmech:000040)

- Review: 20261021T075433Z-symbiosis
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T07:48:44Z
- Finished UTC: 2026-10-21T07:54:33Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The symbiosis concept, fallback identity, parent and both organism examples are supported. Three minor findings concern contextual causal wording, two process descriptions and locally undocumented human acceptance; no definite major external type mismatch was found. All fields, thirteen nodes and eleven edges received conceptual/documentary review. Detailed biological support for edges2–10 remains explicitly unverified, so this is not a scientific clearance of those mechanisms.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Eighth batch003 target in lexicographic path order. Entire record read and native capture completed before assessment; preceding soil-dwelling bundle saved before final judgment. Supplemental capture added one migration owner and confirmed every original input unchanged.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000040 | data/traits/ecology/symbiosis.yaml | maintained | symbiosis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000040 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000040 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000040 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | traitmech:000040 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | traitmech:000040 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000040 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000040 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | traitmech:000040 | The selected record validates. |
| Focused strict validation | passed | True | traitmech:000040 | One file scanned; zero strict errors. |
| Focused snippet verification | passed | True | traitmech:000040 | Zero supporting_text snippets present; command checked zero snippets. This does not verify paraphrased scientific claims. |
| Structured-source runner availability | unavailable | False | traitmech:000040 | Reused bounded discovery; official catalog fallback inspected. |
| Expression dataset applicability | not_applicable | False | traitmech:000040 | Neither canonical organism has a matching entry in the checked official catalog, including the verified genus synonym. |

## Scientific And Domain Assessments

### Native checklist: identifier, label, synonym, polarity, definition and parent

identity: supported. Targets: traitmech:000040.

The record denotes an ecological association class. Related symbiotic synonym, phenotype parent and fallback identity agree. McFall supplies association context and Drew supplies more direct definition/continuum support; evolutionary wording does not exclude ecological shifts.

### Native checklist: category, term kind and contextual graph scope

representation: supported. Targets: traitmech:000040.

ECOLOGY/CLASS and NONMECHANISTIC scope fit this umbrella lifestyle. No universal mechanism or token protein example is required. Optional predicate identifiers, datasets and discussion slots are not treated as missing mandatory content.

### Native checklist: both organism examples and taxonomic identity

evidence: supported. Targets: traitmech:000040.

Both stated symbiotic lifestyles are directly supported at the generic level used. The meliloti genus is a recognized historical synonym of the current taxon.

### Native checklist: all node identities, type descriptions and current groundings

grounding: concern. Targets: traitmech:000040.

Both GO identifiers resolve; nodes2/6 descriptions need minor process-versus-relationship/result clarification. Contextual host and machinery wording does not alone establish an external domain failure.

### Native checklist: all edge endpoints, predicates and claim strength

consistency: concern. Targets: traitmech:000040.

All endpoints resolve. No definite external endpoint-type mismatch was found; edge0’s causal language overstates the inspected contextual support. The host node already presupposes interaction, limiting this to wording precision. Detailed biological claims in edges2–10 remain unverified.

### Native checklist: citation placement, paraphrases and access limits

evidence: unknown. Targets: traitmech:000040.

Six identities resolve. Concept and example claims have positive inspected support; source identity/scope alone does not establish the detailed biological assertions in edges2–10. The zero-snippet result makes no claim about paraphrase fidelity.

### Native checklist: graph structure and optional evidence surfaces

completeness: supported. Targets: traitmech:000040.

All thirteen nodes and eleven edges are present and internally linked. The record has definition, examples and source references; optional expression datasets and pathway links are not required here. Biological completeness of the detailed routes is unassessed.

### Native checklist: scientific status and eight history events

provenance: concern. Targets: traitmech:000040.

Eight events disclose AI assistance and the inspected migration owner explains one type-normalization event. Human scientific acceptance is not linked in the inspected bounded local provenance.

## Findings

### context-causality-wording: Contextual host presence is described as establishing an interaction

minor / open / confirmed; issue key: symbiosis-context-causality-wording.

Edge0 uses causes and says host presence establishes symbiotic interaction, whereas the inspected conceptual sources establish association context. Because the host node already describes a persistently interacting partner and the graph is NONMECHANISTIC, this is a bounded causal/context wording issue, not evidence that the record claims every nearby host causes symbiosis.

### process-description-precision: Formation description denotes the resulting community

minor / open / confirmed; issue key: symbiosis-process-description-precision.

Node6 describes the resulting community while its label and GO term denote formation. Node2 could also more precisely follow its GO process definition, although symbiotic interaction is a related GO synonym and its identity is not invalid. Anchor the correction in node6 and preserve both valid identifiers; no new biological route is needed.

### human-acceptance-link: Human scientific acceptance is not linked in local provenance

minor / open / confirmed; issue key: symbiosis-human-acceptance-link.

All eight target events disclose AI assistance. No explicit human acceptance link was located in the inspected target fields and bounded ignored-inclusive matches. This does not establish that remote or private acceptance never occurred.

## Recommended Actions And Acceptance Checks

### clarify-context

In separately authorized curation, clarify edge0 as supported association context or provide evidence for any retained causal statement; retain the host node’s existing interaction scope.

- The description and predicate express the same claim strength as the inspected conceptual source.
- No universal nearby-host sufficiency claim or new mechanism is inferred.
- Run focused strict validation and relevant graph checks, append native curation history, regenerate affected products and run just qc.

### align-descriptions

Align the two descriptions with their existing process labels and GO definitions, preserving the distinction between a process, a relationship and a resulting community.

- Both descriptions denote the same kind of concept as their GO groundings.
- No biological target, route or experimental optimization is introduced.
- Run focused validation and applicable grounding checks; record authorized changes through native history and run just qc.

### link-acceptance

Locate and link existing human scientific acceptance or obtain it through the established process; preserve AI provenance and reassess status if acceptance remains unavailable.

- Acceptance identifies the record/revision and scientific scope.
- Automated review and schema validation are not represented as human sign-off.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-symbiosis-validate | /private/tmp/traitmech-record-sweep-003.4opxlhgf/symbiosis-validate.log; Executed 2026-10-21T07:52:30Z through 2026-10-21T07:52:31Z; metadata symbiosis-validate.json | context_only | The selected record validates. |
| check-symbiosis-strict | /private/tmp/traitmech-record-sweep-003.4opxlhgf/symbiosis-strict.log; Executed 2026-10-21T07:52:30Z through 2026-10-21T07:52:31Z; metadata symbiosis-strict.json | context_only | One file scanned; zero strict errors. |
| check-symbiosis-snippets | /private/tmp/traitmech-record-sweep-003.4opxlhgf/symbiosis-snippets.log; Executed 2026-10-21T07:52:30Z through 2026-10-21T07:52:30Z; metadata symbiosis-snippets.json | context_only | Zero supporting_text snippets present; command checked zero snippets. This does not verify paraphrased scientific claims. |
| record | data/traits/ecology/symbiosis.yaml; Entire record: definition, parent, synonym, two examples, thirteen nodes, eleven edges and eight events | partial | Conceptual and documentary assessment covers every field. Detailed biological support for edges2–10 is explicitly unverified; no reconstructed mechanism or corrected molecular target is supplied. |
| capture | Native source inspection and supplemental input capture; Original07:48:44–45Z; supplemental07:53:09–10Z | supports | The supplemental capture adds only the process/quality migration owner. All original input hashes remain unchanged. |
| parent | data/traits/upper/phenotype.yaml; Entire parent context record; identifier and definition | supports | Phenotype is strictly broader than this symbiotic ecological lifestyle. No separate scientific verdict on the parent is made. |
| shape | Read-only endpoint and history inspection; All thirteen node identifiers and eleven edge endpoints | supports | Every endpoint resolves; eight events disclose AI assistance. No pathway context link is asserted. |
| policy | docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml; NONMECHANISTIC scope, REVIEWED_LABEL_ONLY and optional CausalEdge.predicate_id | supports | Contextual protein aggregates are permitted without token protein examples. Six unassigned predicate IDs are optional, and neither a universal mechanism nor an expression dataset is required. |
| identity | data/raw/metpo.owl; proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv; Complete RDF scan; v5row42 placeholder1007639; parent1000059 | supports | An exact deprecated precursor1000297 exists, without an inspected replacement assertion; no active exact symbiosis match was found in the complete pinned snapshot. Fallback000040 remains appropriate and the proposed placeholder is distinguished from a minted identifier. |
| identifiers | QuickGO and NCBI Taxonomy official endpoints; GO0044403/0042710; NCBITaxon9/382 | supports | Both GO terms are active biological processes. Taxon9 matches Buchnera aphidicola. Taxon382 is currently Ensifer meliloti with Sinorhizobium meliloti as a synonym; this is a retained historical label, not a wrong organism. |
| relations | Cached authoritative RO and pinned Biolink; v8 predicate proposal; Declared endpoint roles and optional predicate fields | supports | No definite external type mismatch was established. Process-like PATHWAY descriptions may fit RO process roles; chemical material can fit the material-contributor role. Proposed2007700 remains provisional and admits process-to-trait context. These semantic checks do not establish biological causation. |
| ledger | Independent documentary node/edge ledger; All thirteen nodes and eleven edges, zero-based locators | partial | Two node descriptions blur a biological process with a relationship or resulting community. No mandatory identifier or protein-example requirement was invented. Detailed biological routes remain unverified. |
| bibliography | Europe PMC and inspected PMC source text; Six resolved citation identities; exact access modes, three new and five reused hashed receipts | supports | Both example lifestyle statements are supported. McFall and Drew conceptual passages were inspected; Wiesmann and Lin were checked only for identity and broad scope. No supporting_text snippets occur. Reused sources retain original acquisition timestamps. |
| mcfall | https://pmc.ncbi.nlm.nih.gov/articles/PMC3587249/; DOI10.1073/pnas.1218525110; Abstract, Bacteria and the Origin of Animals, Nested Ecosystems | partial | Supports animal-bacterial association context and distinguishes shared ecosystems from intimate associations. It is not a comprehensive formal definition of all symbioses or proof that host presence alone establishes them. |
| drew | https://pmc.ncbi.nlm.nih.gov/articles/PMC8054256/; DOI10.1038/s41579-021-00550-7; Glossary, Introduction Sec1, Context-dependent shifts Sec12 | supports | Supports physical association, the parasite-mutualist continuum and both ecological and evolutionary shifts. The record’s evolutionary-continuum wording does not assert that evolution is the only route. Persistent association is its operational boundary; the source says association can be long lasting. |
| buchnera | https://pubmed.ncbi.nlm.nih.gov/19909925/; DOI10.1016/j.crvi.2009.09.007; abstract first sentence | supports | Directly identifies Buchnera aphidicola as an obligate intracellular aphid symbiont; the article focuses on pea aphid symbiosis. No more specific strain claim is made in the example. |
| meliloti | https://pubmed.ncbi.nlm.nih.gov/12620125/; DOI10.1186/gb-2003-4-2-r15; abstract Background and Results | supports | The root-nodule symbiosis study names S. meliloti and Medicago sativa/truncatula, supporting the generic legume-symbiont example. Transcriptomic measurements are not used to infer a universal mechanism. |
| wiesmann | https://pubmed.ncbi.nlm.nih.gov/36521845/; DOI10.1093/femsre/fuac048; title/abstract high-level scope only | context_only | The review spans selected plant/animal bacterial associations and multiple lifestyles. Its identity and broad review characterization resolve; detailed graph claims attributed to it remain unverified. |
| lin | https://pubmed.ncbi.nlm.nih.gov/38792855/; DOI10.3390/microorganisms12051026; title/abstract high-level scope only | context_only | The cited review concerns mammal-gut colonization. Preserve this source context; detailed prerequisite assertions are unverified, and narrow source focus alone does not prove a generic contextual statement false. |
| provenance | Target-specific local provenance; Ignored-inclusive identifier/slug/path search plus all eight target events | partial | All eight events disclose AI assistance. No explicit human acceptance reference was found in the inspected target events or bounded matching local provenance; private/remote acceptance remains unknown. |
| status-rule | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md; Status/audit and Verification gate | supports | REVIEWED requires human scientific acceptance; AI events and deterministic validation do not establish it. |
| owner | scripts/migrate_process_quality_consistency.py; Lines39–58 and227–237; history[6] writer context | context_only | The existing process-type event matches the maintained migration rationale and timestamp. No writer was executed and no biological route is certified. |
| expression | https://imodulondb.org/api/datasets; Complete official catalog originally retrieved07:36:12Z, taxonomy synonym check07:50:22Z | context_only | No Buchnera, Sinorhizobium or Ensifer organism entry matches the named examples. No gene/module query was issued; dataset absence is not negative biological evidence. |
| runner | Local structured-source runner discovery; Reused bounded ignored-inclusive discovery07:35:50Z | context_only | No usable runner was found in the original bounded install/PATH/project search. The official source catalog provides the fallback applicability check; no fresh or global absence assertion is made. |

## Limits And Additional Notes

- Full record coverage means every field was read and assessed at the stated level, not that every biological assertion was verified. Detailed colonization, immune-evasion, envelope and signaling claims in edges2–10 remain unverified.
- McFall and Drew were inspected in bounded conceptual full-text passages. Both examples were checked from abstracts; Wiesmann/Lin only for citation identity and high-level scope. No lack of support is inferred from uninspected text.
- McFall is animal-focused; Drew provides more direct umbrella concept support. Persistent physical association is the record’s operational boundary rather than a verbatim comprehensive glossary definition.
- No corrected molecular target, reconstructed route, protocol or biological optimization is supplied.
- Authority/type compatibility is distinct from biological causality and from formal reasoner certification; no formal reasoner result is claimed.
- Expression-source coverage is limited to the timestamped official catalog; no gene/module queries were appropriate and catalog absence is not negative biology.
- Human acceptance outside the inspected local fields and bounded ignored-inclusive search remains unknown.
- No scientific record, schema, mapping, writer, history, status or generated page was changed.
- Field paths use zero-based indices.
- Optional empty predicate IDs and contextual REVIEWED_LABEL_ONLY protein aggregates are permitted by the native schema/policy.
- The migration owner was captured as a supplemental input; all initial hashes were rechecked unchanged before finalization.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075433Z-symbiosis
kind: record
repository: CultureBotAI/TraitMech
title: Concept, source and ontology review of symbiosis (traitmech:000040)
started_at: '2026-10-21T07:48:44Z'
finished_at: '2026-10-21T07:54:33Z'
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
summary: The symbiosis concept, fallback identity, parent and both organism examples
  are supported. Three minor findings concern contextual causal wording, two process
  descriptions and locally undocumented human acceptance; no definite major external
  type mismatch was found. All fields, thirteen nodes and eleven edges received conceptual/documentary
  review. Detailed biological support for edges2–10 remains explicitly unverified,
  so this is not a scientific clearance of those mechanisms.
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
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/ecology/symbiosis.yaml
    sha256: 86ad9516ff0879731da3792de1495ba1d0e107394edfcc754be03d052a677b21
    role: target
  - path: data/traits/upper/phenotype.yaml
    sha256: 502760fa1b7179bf4e25ab56ecb91d0b25d5f50ed5cfe44133c63a9b821cc4a4
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
  - path: mappings/node_grounding.tsv
    sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
    role: context
  - path: mappings/predicate_grounding.tsv
    sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
    role: context
  - path: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
    sha256: 4ab5ca37ff8595210254b1099563b4425ecd737ed375dc5a932b44e2ad5c332e
    role: context
  - path: proposals/metpo_traitmech_v2/proposal.md
    sha256: fe0601356b120ef9babc6f90a417f860bf02aa628c46af661517f168e01bc48f
    role: context
  - path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
    role: context
  - path: proposals/metpo_traitmech_v5/proposal.md
    sha256: 5d54623dd00ac80a8d67a0eab7b70385f7f57b36daa205c28aa1f9d6f9be6167
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
  - path: research/traits/ecology/symbiosis-deep-research-falcon.md
    sha256: fb384daaf8fba83204067f2578993093867475e8a4ae8dfa0f89cd91d8097b3b
    role: context
  - path: scripts/audit_causal_graphs.py
    sha256: e0c26506c9de712700317284f142097e7bf69334806b8010db5d6517e905e834
    role: context
  - path: scripts/curate_knowledge_gaps.py
    sha256: 9e0fb7e01a901d84189a28f1912a2552f28d2da8733c113589e4947359d48c73
    role: context
  - path: scripts/migrate_enables_trait_edges.py
    sha256: a5e7965ee4f6b6ba5bae3a06bced2a83cbf755f3b9b150ce6acc0cd808cb1d88
    role: context
  - path: scripts/migrate_microbe_domain_edges.py
    sha256: 5187ccfb2897d415b243792a27afd6002c0eea4b167068639ff5be73ed583bb6
    role: context
  - path: scripts/migrate_process_quality_consistency.py
    sha256: 1a83ad3dba79ed0c958b875a6fcc4b9e562259af26da2f248d32d5cf7784f80a
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
- target_id: traitmech:000040
  path: data/traits/ecology/symbiosis.yaml
  label: symbiosis
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/symbiosis.yaml
    role: Maintained scientific record
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Eighth batch003 target in lexicographic path order. Entire record read
    and native capture completed before assessment; preceding soil-dwelling bundle
    saved before final judgment. Supplemental capture added one migration owner and
    confirmed every original input unchanged.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000040
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000040
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: History validation ran at the current 8eee base. Other commands ran
    at f25; the full Git delta contains only seven added workflow/skill/infrastructure-history
    files, with scientific records and existing validation inputs unchanged. Original
    timestamps, failures and skips are retained; these checks do not certify later
    ontology releases.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - traitmech:000040
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: History validation ran at the current 8eee base. Other commands ran
    at f25; the full Git delta contains only seven added workflow/skill/infrastructure-history
    files, with scientific records and existing validation inputs unchanged. Original
    timestamps, failures and skips are retained; these checks do not certify later
    ontology releases.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - traitmech:000040
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: History validation ran at the current 8eee base. Other commands ran
    at f25; the full Git delta contains only seven added workflow/skill/infrastructure-history
    files, with scientific records and existing validation inputs unchanged. Original
    timestamps, failures and skips are retained; these checks do not certify later
    ontology releases.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - traitmech:000040
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: History validation ran at the current 8eee base. Other commands ran
    at f25; the full Git delta contains only seven added workflow/skill/infrastructure-history
    files, with scientific records and existing validation inputs unchanged. Original
    timestamps, failures and skips are retained; these checks do not certify later
    ontology releases.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - traitmech:000040
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: History validation ran at the current 8eee base. Other commands ran
    at f25; the full Git delta contains only seven added workflow/skill/infrastructure-history
    files, with scientific records and existing validation inputs unchanged. Original
    timestamps, failures and skips are retained; these checks do not certify later
    ontology releases.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - traitmech:000040
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: History validation ran at the current 8eee base. Other commands ran
    at f25; the full Git delta contains only seven added workflow/skill/infrastructure-history
    files, with scientific records and existing validation inputs unchanged. Original
    timestamps, failures and skips are retained; these checks do not certify later
    ontology releases.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - traitmech:000040
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: History validation ran at the current 8eee base. Other commands ran
    at f25; the full Git delta contains only seven added workflow/skill/infrastructure-history
    files, with scientific records and existing validation inputs unchanged. Original
    timestamps, failures and skips are retained; these checks do not certify later
    ontology releases.
- check_id: symbiosis-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000040
  command: just validate data/traits/ecology/symbiosis.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The selected record validates.
  evidence_ids:
  - check-symbiosis-validate
- check_id: symbiosis-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000040
  command: just validate-strict data/traits/ecology/symbiosis.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero strict errors.
  evidence_ids:
  - check-symbiosis-strict
- check_id: symbiosis-snippets
  name: Focused snippet verification
  status: passed
  required: true
  target_ids:
  - traitmech:000040
  command: just verify-snippets --record data/traits/ecology/symbiosis.yaml --out
    /private/tmp/traitmech-record-sweep-003.4opxlhgf/symbiosis-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Zero supporting_text snippets present; command checked zero snippets. This
    does not verify paraphrased scientific claims.
  evidence_ids:
  - check-symbiosis-snippets
- check_id: structured-source-runner
  name: Structured-source runner availability
  status: unavailable
  required: false
  target_ids:
  - traitmech:000040
  summary: Reused bounded discovery; official catalog fallback inspected.
  evidence_ids:
  - runner
- check_id: expression-applicability
  name: Expression dataset applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000040
  summary: Neither canonical organism has a matching entry in the checked official
    catalog, including the verified genus synonym.
  evidence_ids:
  - expression
  - identifiers
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T07:54:33Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T07:54:33Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T07:54:33Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T07:54:33Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T07:54:33Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T07:54:33Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T07:54:33Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-symbiosis-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/symbiosis-validate.log
  locator: Executed 2026-10-21T07:52:30Z through 2026-10-21T07:52:31Z; metadata symbiosis-validate.json
  accessed_at: '2026-10-21T07:54:33Z'
  support: context_only
  summary: The selected record validates.
  snapshot_sha256: f71e6c88342b77fb0004bf455ff5d6fa7f302c9015bb71b786800cfd7e8d41be
- evidence_id: check-symbiosis-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/symbiosis-strict.log
  locator: Executed 2026-10-21T07:52:30Z through 2026-10-21T07:52:31Z; metadata symbiosis-strict.json
  accessed_at: '2026-10-21T07:54:33Z'
  support: context_only
  summary: One file scanned; zero strict errors.
  snapshot_sha256: 318ab9024d53de0034b05cfa208442efa4bf2915beb0f069e5cfd0223cb867f0
- evidence_id: check-symbiosis-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/symbiosis-snippets.log
  locator: Executed 2026-10-21T07:52:30Z through 2026-10-21T07:52:30Z; metadata symbiosis-snippets.json
  accessed_at: '2026-10-21T07:54:33Z'
  support: context_only
  summary: Zero supporting_text snippets present; command checked zero snippets. This
    does not verify paraphrased scientific claims.
  snapshot_sha256: 842ad175815c1f5442424dcf233c542407a9fbb566717fd450b0f9d66d328ebb
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/symbiosis.yaml
  locator: 'Entire record: definition, parent, synonym, two examples, thirteen nodes,
    eleven edges and eight events'
  accessed_at: '2026-10-21T07:54:33Z'
  support: partial
  summary: Conceptual and documentary assessment covers every field. Detailed biological
    support for edges2–10 is explicitly unverified; no reconstructed mechanism or
    corrected molecular target is supplied.
  snapshot_sha256: 86ad9516ff0879731da3792de1495ba1d0e107394edfcc754be03d052a677b21
- evidence_id: capture
  kind: validation
  reference: Native source inspection and supplemental input capture
  locator: Original07:48:44–45Z; supplemental07:53:09–10Z
  accessed_at: '2026-10-21T07:53:10Z'
  support: supports
  summary: The supplemental capture adds only the process/quality migration owner.
    All original input hashes remain unchanged.
  snapshot_sha256: 8b6ecd7c993f8fc30f6b8918c28182062ac1a3a56bec7c66f09301bd46d89c42
- evidence_id: parent
  kind: record_content
  reference: data/traits/upper/phenotype.yaml
  locator: Entire parent context record; identifier and definition
  accessed_at: '2026-10-21T07:54:33Z'
  support: supports
  summary: Phenotype is strictly broader than this symbiotic ecological lifestyle.
    No separate scientific verdict on the parent is made.
- evidence_id: shape
  kind: validation
  reference: Read-only endpoint and history inspection
  locator: All thirteen node identifiers and eleven edge endpoints
  accessed_at: '2026-10-21T07:53:10Z'
  support: supports
  summary: Every endpoint resolves; eight events disclose AI assistance. No pathway
    context link is asserted.
  snapshot_sha256: ed0df4c0159dbbca2c5e630bbf1ae6903378fb51b5789d33105512b4e225a33a
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml
  locator: NONMECHANISTIC scope, REVIEWED_LABEL_ONLY and optional CausalEdge.predicate_id
  accessed_at: '2026-10-21T07:54:33Z'
  support: supports
  summary: Contextual protein aggregates are permitted without token protein examples.
    Six unassigned predicate IDs are optional, and neither a universal mechanism nor
    an expression dataset is required.
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl; proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
  locator: Complete RDF scan; v5row42 placeholder1007639; parent1000059
  accessed_at: '2026-10-21T07:51:50Z'
  support: supports
  summary: An exact deprecated precursor1000297 exists, without an inspected replacement
    assertion; no active exact symbiosis match was found in the complete pinned snapshot.
    Fallback000040 remains appropriate and the proposed placeholder is distinguished
    from a minted identifier.
  snapshot_sha256: 3e61a4d2f6ba9bbd342a3029d200adbc27b5fd6451b2aecb330be042e7cd6ce9
- evidence_id: identifiers
  kind: authority
  reference: QuickGO and NCBI Taxonomy official endpoints
  locator: GO0044403/0042710; NCBITaxon9/382
  accessed_at: '2026-10-21T07:50:22Z'
  support: supports
  summary: Both GO terms are active biological processes. Taxon9 matches Buchnera
    aphidicola. Taxon382 is currently Ensifer meliloti with Sinorhizobium meliloti
    as a synonym; this is a retained historical label, not a wrong organism.
  snapshot_sha256: 4dda410c46f906b8f25c5145aa4627208dc67dc94465873304c0605ba8fd397b
- evidence_id: relations
  kind: authority
  reference: Cached authoritative RO and pinned Biolink; v8 predicate proposal
  locator: Declared endpoint roles and optional predicate fields
  accessed_at: '2026-10-21T07:49:50Z'
  support: supports
  summary: No definite external type mismatch was established. Process-like PATHWAY
    descriptions may fit RO process roles; chemical material can fit the material-contributor
    role. Proposed2007700 remains provisional and admits process-to-trait context.
    These semantic checks do not establish biological causation.
  snapshot_sha256: 051907f3edb2461e233bffc42638b42caf8ad99a5665e00381c2c02886b1a4ed
- evidence_id: ledger
  kind: validation
  reference: Independent documentary node/edge ledger
  locator: All thirteen nodes and eleven edges, zero-based locators
  accessed_at: '2026-10-21T07:52:53Z'
  support: partial
  summary: Two node descriptions blur a biological process with a relationship or
    resulting community. No mandatory identifier or protein-example requirement was
    invented. Detailed biological routes remain unverified.
  snapshot_sha256: b174d04eb8ca9d3b9754aaba055eaef71e6666636f16509e17c617186604dd08
- evidence_id: bibliography
  kind: database
  reference: Europe PMC and inspected PMC source text
  locator: Six resolved citation identities; exact access modes, three new and five
    reused hashed receipts
  accessed_at: '2026-10-21T07:52:41Z'
  support: supports
  summary: Both example lifestyle statements are supported. McFall and Drew conceptual
    passages were inspected; Wiesmann and Lin were checked only for identity and broad
    scope. No supporting_text snippets occur. Reused sources retain original acquisition
    timestamps.
  snapshot_sha256: 433d3953cd1d9daacbe7429e62b77e5754331966b1e1f634678c716b795bd93a
- evidence_id: mcfall
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3587249/
  locator: DOI10.1073/pnas.1218525110; Abstract, Bacteria and the Origin of Animals,
    Nested Ecosystems
  accessed_at: '2026-10-20T07:21:00Z'
  support: partial
  summary: Supports animal-bacterial association context and distinguishes shared
    ecosystems from intimate associations. It is not a comprehensive formal definition
    of all symbioses or proof that host presence alone establishes them.
  snapshot_sha256: 9b5d60a370751beacc2464ed17c810d45b2f450d1fa6901e71fbd472fd7fd014
- evidence_id: drew
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8054256/
  locator: DOI10.1038/s41579-021-00550-7; Glossary, Introduction Sec1, Context-dependent
    shifts Sec12
  accessed_at: '2026-10-21T07:04:00Z'
  support: supports
  summary: Supports physical association, the parasite-mutualist continuum and both
    ecological and evolutionary shifts. The record’s evolutionary-continuum wording
    does not assert that evolution is the only route. Persistent association is its
    operational boundary; the source says association can be long lasting.
  snapshot_sha256: a431624c1430ff8e3076a79cf7304c19127c8a3813e2e49f018dc35a8eb2d5d6
- evidence_id: buchnera
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/19909925/
  locator: DOI10.1016/j.crvi.2009.09.007; abstract first sentence
  accessed_at: '2026-10-21T07:49:48Z'
  support: supports
  summary: Directly identifies Buchnera aphidicola as an obligate intracellular aphid
    symbiont; the article focuses on pea aphid symbiosis. No more specific strain
    claim is made in the example.
  snapshot_sha256: f72f7fb02dc469a45889d6695916b0ec49c77f0beddacf70a54f945f746c4dd1
- evidence_id: meliloti
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/12620125/
  locator: DOI10.1186/gb-2003-4-2-r15; abstract Background and Results
  accessed_at: '2026-10-21T07:49:48Z'
  support: supports
  summary: The root-nodule symbiosis study names S. meliloti and Medicago sativa/truncatula,
    supporting the generic legume-symbiont example. Transcriptomic measurements are
    not used to infer a universal mechanism.
  snapshot_sha256: 6c4cbd1409b0bd1754121b9cd5b68b6ea175779a86b42db94e24a9034bce00c0
- evidence_id: wiesmann
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/36521845/
  locator: DOI10.1093/femsre/fuac048; title/abstract high-level scope only
  accessed_at: '2026-10-21T07:49:48Z'
  support: context_only
  summary: The review spans selected plant/animal bacterial associations and multiple
    lifestyles. Its identity and broad review characterization resolve; detailed graph
    claims attributed to it remain unverified.
  snapshot_sha256: 47bf75df18db70888c90f533bb9a42b4d91f9c94862eae5dc311f5fb7dadb0a5
- evidence_id: lin
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/38792855/
  locator: DOI10.3390/microorganisms12051026; title/abstract high-level scope only
  accessed_at: '2026-10-20T07:20:58Z'
  support: context_only
  summary: The cited review concerns mammal-gut colonization. Preserve this source
    context; detailed prerequisite assertions are unverified, and narrow source focus
    alone does not prove a generic contextual statement false.
  snapshot_sha256: e506250b22939c7e68e2ae7bb0d3c1c3f4becbd97d9bc7f23d930948ddf8cca2
- evidence_id: provenance
  kind: search
  reference: Target-specific local provenance
  locator: Ignored-inclusive identifier/slug/path search plus all eight target events
  accessed_at: '2026-10-21T07:53:10Z'
  support: partial
  summary: All eight events disclose AI assistance. No explicit human acceptance reference
    was found in the inspected target events or bounded matching local provenance;
    private/remote acceptance remains unknown.
  snapshot_sha256: 9d07a843882cc18253425749bd55b12c2a8a5002050c87637267759a10175c2d
  search_scope: rg --no-ignore --hidden across scripts, history, mappings, reviews
    and research/traits/ecology for exact identifier, graph ID and record path; all
    target events read. No whole-filesystem or remote/private absence claim.
- evidence_id: status-rule
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md
  locator: Status/audit and Verification gate
  accessed_at: '2026-10-21T07:54:33Z'
  support: supports
  summary: REVIEWED requires human scientific acceptance; AI events and deterministic
    validation do not establish it.
- evidence_id: owner
  kind: record_content
  reference: scripts/migrate_process_quality_consistency.py
  locator: Lines39–58 and227–237; history[6] writer context
  accessed_at: '2026-10-21T07:54:33Z'
  support: context_only
  summary: The existing process-type event matches the maintained migration rationale
    and timestamp. No writer was executed and no biological route is certified.
  snapshot_sha256: 1a83ad3dba79ed0c958b875a6fcc4b9e562259af26da2f248d32d5cf7784f80a
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete official catalog originally retrieved07:36:12Z, taxonomy synonym
    check07:50:22Z
  accessed_at: '2026-10-21T07:51:05Z'
  support: context_only
  summary: No Buchnera, Sinorhizobium or Ensifer organism entry matches the named
    examples. No gene/module query was issued; dataset absence is not negative biological
    evidence.
  snapshot_sha256: a3fa26093b7299ef5a33fe448ec673219e0333615b04cf6d43fcc550065b156e
- evidence_id: runner
  kind: search
  reference: Local structured-source runner discovery
  locator: Reused bounded ignored-inclusive discovery07:35:50Z
  accessed_at: '2026-10-21T07:35:50Z'
  support: context_only
  summary: No usable runner was found in the original bounded install/PATH/project
    search. The official source catalog provides the fallback applicability check;
    no fresh or global absence assertion is made.
  snapshot_sha256: 255ec15986d2ece8ee78c72591e43429c1bb5f22c3326a349667326e3fe1b380
  search_scope: Original PATH/install/project roots and ignored-inclusive traversal
    are recorded in the reused receipt; other directories remain unknown.
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, label, synonym, polarity, definition and parent'
  outcome: supported
  target_ids:
  - traitmech:000040
  summary: The record denotes an ecological association class. Related symbiotic synonym,
    phenotype parent and fallback identity agree. McFall supplies association context
    and Drew supplies more direct definition/continuum support; evolutionary wording
    does not exclude ecological shifts.
  evidence_ids:
  - record
  - identity
  - parent
  - mcfall
  - drew
- assessment_id: model
  area: representation
  topic: 'Native checklist: category, term kind and contextual graph scope'
  outcome: supported
  target_ids:
  - traitmech:000040
  summary: ECOLOGY/CLASS and NONMECHANISTIC scope fit this umbrella lifestyle. No
    universal mechanism or token protein example is required. Optional predicate identifiers,
    datasets and discussion slots are not treated as missing mandatory content.
  evidence_ids:
  - record
  - policy
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: both organism examples and taxonomic identity'
  outcome: supported
  target_ids:
  - traitmech:000040
  summary: Both stated symbiotic lifestyles are directly supported at the generic
    level used. The meliloti genus is a recognized historical synonym of the current
    taxon.
  evidence_ids:
  - buchnera
  - meliloti
  - identifiers
- assessment_id: nodes
  area: grounding
  topic: 'Native checklist: all node identities, type descriptions and current groundings'
  outcome: concern
  target_ids:
  - traitmech:000040
  summary: Both GO identifiers resolve; nodes2/6 descriptions need minor process-versus-relationship/result
    clarification. Contextual host and machinery wording does not alone establish
    an external domain failure.
  evidence_ids:
  - record
  - identifiers
  - ledger
  - relations
- assessment_id: edges
  area: consistency
  topic: 'Native checklist: all edge endpoints, predicates and claim strength'
  outcome: concern
  target_ids:
  - traitmech:000040
  summary: All endpoints resolve. No definite external endpoint-type mismatch was
    found; edge0’s causal language overstates the inspected contextual support. The
    host node already presupposes interaction, limiting this to wording precision.
    Detailed biological claims in edges2–10 remain unverified.
  evidence_ids:
  - shape
  - relations
  - ledger
  - mcfall
  - drew
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: citation placement, paraphrases and access limits'
  outcome: unknown
  target_ids:
  - traitmech:000040
  summary: Six identities resolve. Concept and example claims have positive inspected
    support; source identity/scope alone does not establish the detailed biological
    assertions in edges2–10. The zero-snippet result makes no claim about paraphrase
    fidelity.
  evidence_ids:
  - bibliography
  - mcfall
  - drew
  - buchnera
  - meliloti
  - wiesmann
  - lin
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: graph structure and optional evidence surfaces'
  outcome: supported
  target_ids:
  - traitmech:000040
  summary: All thirteen nodes and eleven edges are present and internally linked.
    The record has definition, examples and source references; optional expression
    datasets and pathway links are not required here. Biological completeness of the
    detailed routes is unassessed.
  evidence_ids:
  - shape
  - record
  - policy
  - expression
- assessment_id: audit
  area: provenance
  topic: 'Native checklist: scientific status and eight history events'
  outcome: concern
  target_ids:
  - traitmech:000040
  summary: Eight events disclose AI assistance and the inspected migration owner explains
    one type-normalization event. Human scientific acceptance is not linked in the
    inspected bounded local provenance.
  evidence_ids:
  - provenance
  - status-rule
  - owner
findings:
- finding_id: context-causality-wording
  issue_key: symbiosis-context-causality-wording
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Contextual host presence is described as establishing an interaction
  description: Edge0 uses causes and says host presence establishes symbiotic interaction,
    whereas the inspected conceptual sources establish association context. Because
    the host node already describes a persistently interacting partner and the graph
    is NONMECHANISTIC, this is a bounded causal/context wording issue, not evidence
    that the record claims every nearby host causes symbiosis.
  target_ids:
  - traitmech:000040
  field_paths:
  - causal_graphs[0].edges[0]
  evidence_ids:
  - record
  - mcfall
  - drew
  - ledger
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: process-description-precision
  issue_key: symbiosis-process-description-precision
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Formation description denotes the resulting community
  description: Node6 describes the resulting community while its label and GO term
    denote formation. Node2 could also more precisely follow its GO process definition,
    although symbiotic interaction is a related GO synonym and its identity is not
    invalid. Anchor the correction in node6 and preserve both valid identifiers; no
    new biological route is needed.
  target_ids:
  - traitmech:000040
  field_paths:
  - causal_graphs[0].nodes[6].description
  - causal_graphs[0].nodes[2].description
  evidence_ids:
  - record
  - identifiers
  - ledger
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: symbiosis-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human scientific acceptance is not linked in local provenance
  description: All eight target events disclose AI assistance. No explicit human acceptance
    link was located in the inspected target fields and bounded ignored-inclusive
    matches. This does not establish that remote or private acceptance never occurred.
  target_ids:
  - traitmech:000040
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - status-rule
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: clarify-context
  description: In separately authorized curation, clarify edge0 as supported association
    context or provide evidence for any retained causal statement; retain the host
    node’s existing interaction scope.
  finding_ids:
  - context-causality-wording
  target_ids:
  - traitmech:000040
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The description and predicate express the same claim strength as the inspected
    conceptual source.
  - No universal nearby-host sufficiency claim or new mechanism is inferred.
  - Run focused strict validation and relevant graph checks, append native curation
    history, regenerate affected products and run just qc.
- action_id: align-descriptions
  description: Align the two descriptions with their existing process labels and GO
    definitions, preserving the distinction between a process, a relationship and
    a resulting community.
  finding_ids:
  - process-description-precision
  target_ids:
  - traitmech:000040
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Both descriptions denote the same kind of concept as their GO groundings.
  - No biological target, route or experimental optimization is introduced.
  - Run focused validation and applicable grounding checks; record authorized changes
    through native history and run just qc.
- action_id: link-acceptance
  description: Locate and link existing human scientific acceptance or obtain it through
    the established process; preserve AI provenance and reassess status if acceptance
    remains unavailable.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - traitmech:000040
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies the record/revision and scientific scope.
  - Automated review and schema validation are not represented as human sign-off.
limitations:
- Full record coverage means every field was read and assessed at the stated level,
  not that every biological assertion was verified. Detailed colonization, immune-evasion,
  envelope and signaling claims in edges2–10 remain unverified.
- McFall and Drew were inspected in bounded conceptual full-text passages. Both examples
  were checked from abstracts; Wiesmann/Lin only for citation identity and high-level
  scope. No lack of support is inferred from uninspected text.
- McFall is animal-focused; Drew provides more direct umbrella concept support. Persistent
  physical association is the record’s operational boundary rather than a verbatim
  comprehensive glossary definition.
- No corrected molecular target, reconstructed route, protocol or biological optimization
  is supplied.
- Authority/type compatibility is distinct from biological causality and from formal
  reasoner certification; no formal reasoner result is claimed.
- Expression-source coverage is limited to the timestamped official catalog; no gene/module
  queries were appropriate and catalog absence is not negative biology.
- Human acceptance outside the inspected local fields and bounded ignored-inclusive
  search remains unknown.
- No scientific record, schema, mapping, writer, history, status or generated page
  was changed.
notes:
- Field paths use zero-based indices.
- Optional empty predicate IDs and contextual REVIEWED_LABEL_ONLY protein aggregates
  are permitted by the native schema/policy.
- The migration owner was captured as a supplemental input; all initial hashes were
  rechecked unchanged before finalization.
tags:
- record-review
- symbiosis
- ecology
- needs-curation
```
