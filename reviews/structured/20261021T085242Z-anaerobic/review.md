# Evidence and ontology review of anaerobic growth (METPO:1000603)

- Review: 20261021T085242Z-anaerobic
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T08:45:58Z
- Finished UTC: 2026-10-21T08:52:42Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The broad anaerobic-growth record has the correct METPO identity, hierarchy and current identifiers. One major finding covers two distinct relation-role errors: process inhibition applied to chemical/trait endpoints, and an executor relation applied to a described chemical input. Three minor findings concern strict-source terminology, a physical-site/activity facet ambiguity and the bounded missing human-acceptance link. All ten nodes and ten edges were inspected, all six snippets are exact, and detailed pathogen fitness/defense mechanisms remain unassessed.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Fifth batch004 target in lexicographic path order. Entire target read before native capture. One complete record assessed, with detailed pathogen fitness/defense mechanisms outside the biological verification scope and retained as explicit limitations.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000603 | data/traits/environment/anaerobic.yaml | maintained | anaerobic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000603 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000603 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000603 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1000603 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000603 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000603 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000603 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1000603 | Selected record validates. |
| Focused strict validation | passed | True | METPO:1000603 | One file scanned; zero strict errors. |
| Focused source snippet check | passed | True | METPO:1000603 | Six snippets across three references: five VERIFIED and one NOT_IN_ABSTRACT. The abstract miss is inconclusive; manual source assessment is recorded separately. |
| Structured-source runner discovery | unavailable | False | METPO:1000603 | Reused bounded discovery with official catalog fallback. |
| Canonical-taxon dataset applicability | not_applicable | False | METPO:1000603 | Neither canonical organism matches the inspected catalog; no gene/module queries. |

## Scientific And Domain Assessments

### Native checklist: concept, synonyms, hierarchy and xref

identity: supported. Targets: METPO:1000603.

Active METPO1000603, oxygen-preference parent1000601 and related synonyms denote the intended broad trait. PATO1456 is oxygen independence. Explicit obsolete-term replacements were inspected rather than inferred.

### Native checklist: broad class versus strict source usage

evidence: concern. Targets: METPO:1000603.

The definition matches METPO, but the nearest chapter quotation uses a narrower strict-anaerobe sense. The distinction should be explicit, preserving broad growth capability without importing universal oxygen intolerance.

### Native checklist: category, term kind and graph scope

representation: supported. Targets: METPO:1000603.

ENVIRONMENT/CLASS and contextual NONMECHANISTIC scope fit the target. Optional label-only protein aggregates, datasets and accession instances are not mandatory merely because biochemical context is present.

### Native checklist: both canonical organisms and limits

evidence: unknown. Targets: METPO:1000603.

Taxon identities resolve and both sources support their generic anaerobic phenotype contexts. The B. fragilis gut adjective was not independently verified on available title/abstract text; failed body access leaves it unknown. No mutant result was generalized to the species and no detailed defense route was assessed.

### Native checklist: current identifiers and represented facets

grounding: concern. Targets: METPO:1000603.

Current METPO, GO, CHEBI, PATO and taxonomy match their intended concepts. Node4 mixes physical catalytic sites/metal centers with an activity type; this requires clarification of the represented facet, not an invented mandatory accession.

### Native checklist: all ten endpoint pairs and relation roles

consistency: concern. Targets: METPO:1000603.

Edge1 misuses process regulation for chemical-to-trait inhibition. Edge8 uses the executor relation for a described chemical input; its broad endpoint classes fit, so this is a narrower meaning mismatch. Compatible protein-executor edge5 and provisional contextual confers edges are retained.

### Native checklist: all citations, excerpts and causal interpretation

evidence: unknown. Targets: METPO:1000603.

All six quotations are exact. Obligately anaerobic and environmental anammox sources retain their scopes. Hypoxic-habitat association is not experimental trait conferral. The gut-respiration reference was assessed at conceptual level; detailed pathogen fitness and defense claims remain explicitly unassessed.

### Native checklist: required structure, discussions and optional surfaces

completeness: supported. Targets: METPO:1000603.

All endpoints resolve and required identity/evidence structures are present. No invented protein instances, datasets or universal respiratory pathway are needed for contextual scope. Relevant existing research is a provenance lead, not primary evidence.

### Native checklist: canonical-taxon structured-source applicability

evidence: supported. Targets: METPO:1000603.

Neither canonical taxon matches the inspected dataset catalog. No substitute organism or expression module was used; noncoverage supplies no negative phenotype evidence.

### Native checklist: history, acceptance and future input owners

provenance: concern. Targets: METPO:1000603.

Twelve events disclose AI assistance alongside the seed. APPROVED mapping status and automated history integrity do not establish human acceptance; none is linked in the bounded local search. Existing-edge correction and mapping recurrence are distinct follow-up tasks.

## Findings

### external-relation-semantics: Two external relations assign unsupported endpoint roles

major / open / confirmed; issue key: anaerobic-external-relation-semantics.

Edge1 uses RO inhibits between oxygen and the trait although it inherits process-to-process regulation roles. Edge8 uses RO enables for an electron acceptor described as an available input. Its broad material/process types are compatible, but the description does not establish the executing role required by enables. These are separate semantic defects; neither native schema success nor a blanket ban on chemical actors resolves them. No OWL reasoner execution is claimed.

### strict-source-broad-definition: Distinguish broad anaerobic growth from strict source terminology

minor / open / confirmed; issue key: anaerobic-strict-source-broad-definition.

The record correctly defines the broad METPO capability to grow without oxygen. Its nearest definition quotation and the Lu abstract use a stricter obligate-anaerobe scope. Make the distinction explicit instead of treating oxygen intolerance as a necessary property of every member of the broad class. This is bounded attribution/scope precision, not an incorrect ontology identity.

### catalytic-site-facet: Clarify physical catalytic sites versus molecular activity

minor / open / confirmed; issue key: anaerobic-catalytic-site-facet.

Node4 names physical catalytic sites and its description includes metal centers, while its type is MOLECULAR_FUNCTION. Clarify whether the node denotes an activity or a physical bearer/site and align wording and type. No specific replacement enum or ontology accession is asserted without further curation.

### human-acceptance-link: Human scientific acceptance is not linked locally

minor / open / confirmed; issue key: anaerobic-human-acceptance-link.

The ignored-inclusive local record/history/mapping/writer/review search did not identify explicit human scientific acceptance of this revision. Twelve AI-assisted events, the original seed and an APPROVED exact-match row are not that acceptance. Private or remote approval remains unknown.

## Recommended Actions And Acceptance Checks

### repair-relations

In separately authorized curation, choose relations matching the two documented endpoint roles and review wildcard mapping recurrence.

- Edge1 respects the selected relation’s inherited domain/range and biological meaning.
- Edge8 distinguishes process execution from chemical input availability without asserting a blanket formal exclusion of chemical actors.
- A maintained ground-predicates dry run assesses recurrence; existing nonempty IDs require guarded correction and are not overwritten by that writer.
- Run focused strict/graph checks and just qc, append native curation/history and regenerate affected products after authorized edits.

### clarify-source-scope

Make the broad METPO definition and narrower obligate-anaerobe source scope explicit, preserving contextual claims at their evidenced level.

- Definition authority and source terminology are distinguishable.
- No universal oxygen intolerance or experimentally established habitat conferral is inferred from these excerpts.
- Run focused record validation after any authorized changes.

### clarify-node-facet

Resolve whether node4 denotes catalytic activity or a physical site/bearer, and align its label, description and type.

- The represented entity facet is unambiguous and compatible with its node type.
- No arbitrary accession or detailed pathogen mechanism is introduced.
- Run focused strict/graph validation after authorized changes.

### link-acceptance

Locate and link existing human acceptance or obtain it through the established process, preserving AI provenance and reassessing status if acceptance remains unavailable.

- Acceptance identifies this record revision and scientific scope.
- Mapping decisions, AI events and validator success are not represented as human scientific sign-off.

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
| check-anaerobic-validate | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/anaerobic-validate.log; Executed 2026-10-21T08:46:27Z through 2026-10-21T08:46:31Z; metadata anaerobic-validate.json | context_only | Selected record validates. |
| check-anaerobic-strict | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/anaerobic-strict.log; Executed 2026-10-21T08:46:27Z through 2026-10-21T08:46:31Z; metadata anaerobic-strict.json | context_only | One file scanned; zero strict errors. |
| check-anaerobic-snippets | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/anaerobic-snippets.log; Executed 2026-10-21T08:46:29Z through 2026-10-21T08:46:35Z; metadata anaerobic-snippets.json | context_only | Six snippets across three references: five VERIFIED and one NOT_IN_ABSTRACT. The abstract miss is inconclusive; manual source assessment is recorded separately. |
| record | data/traits/environment/anaerobic.yaml; Whole record: definition, two related synonyms, xref, two examples, ten nodes/edges and thirteen events | partial | Broad oxygen-independent growth is correctly identified. The cited strict-anaerobe framing needs its narrower scope, and external relations require endpoint-role review. Detailed pathogen defense and fitness mechanisms were not reconstructed. |
| shape | Whole graph/history inspection; Ten nodes, ten edge endpoints, thirteen events and six snippets | supports | All endpoints resolve. Twelve events explicitly disclose AI assistance plus the original seed. No pathway-context link is asserted. |
| identity | data/raw/metpo.owl; data/traits/environment/oxygen_preference.yaml; Active1000603, parent1000601 and related synonyms | supports | The pinned METPO identity describes growth in the absence of molecular oxygen. Parent oxygen preference is broader; related-synonym scope is preserved. This definition does not itself require inability to grow in oxygen. |
| policy | docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml; Contextual graph scope and node-type meaning | supports | NONMECHANISTIC context permits reviewed label-only proteins and does not require token accessions, universal mechanisms or datasets. A physical catalytic site and a molecular activity are different facets even when both occur in a broad biochemical description. |
| provenance | Target history and bounded local source/mapping/writer/review search; All thirteen events and ignored-inclusive exact identifier/path/label matches | partial | The exact-match decision row is APPROVED, but the linked record event is AI-assisted. Neither this status nor other reviews listing the file as an input establishes human acceptance of the target revision. No explicit local acceptance link was found; private/remote approval remains unknown. |
| status-rule | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md; Status/audit and verification gate | supports | REVIEWED requires human scientific acceptance; AI provenance and automated checks are different evidence. |
| expression | https://imodulondb.org/api/datasets; Original07:36:12Z catalog with current hash-verified applicability check | context_only | Neither C. acetobutylicum nor B. fragilis matches the inspected catalog. No other organism was substituted and no gene/module query was made. No negative phenotype or protein claim follows from catalog noncoverage. |
| runner | Reused structured-source runner discovery; Original bounded ignored-inclusive08:17:15Z search | context_only | The runner was unavailable in the original declared bounds; official catalog fallback was inspected. This preserves original times and scope, not a fresh/global runner-absence claim. |
| live-identifiers | QuickGO GO:0009061; NCBI taxonomy1488/817; Current identity responses08:46:57–58Z | supports | Anaerobic respiration is an active biological process. Both canonical organism labels match the resolved taxon identities. Identity alone does not verify phenotype or host association. |
| reused-identifiers | OLS CHEBI:15379 and CHEBI:26523; Original08:17:52Z responses, current hash verification | supports | Molecular oxygen and reactive oxygen species identities match their nodes. Original acquisition times are retained; this is not a new release check. |
| ro-pato | RO ontology and PATO authority snapshots; RO2212 inherited regulation roles; RO2327 executor meaning; PATO1456 oxygen independence | partial | RO inhibits inherits process endpoints. RO enables has broad material/process endpoints but specifies an executing actor, not merely any required input. PATO oxygen independence agrees with the broad trait and does not require oxygen intolerance. Original RO inspections were08:04:46Z and07:58:06Z; the cached PATO entry was inspected08:46:52Z. |
| ledger | Independent complete node/edge documentary ledger; Ten nodes and ten edges; zero-based indices | partial | Edge1 conflicts with inherited process endpoints. Edge8 has broadly compatible types but its input-availability description does not substantiate the narrower executor relation. Node4 mixes a physical site with an activity facet. Optional label-only aggregates and contextual confers edges are not automatic type defects. |
| owners | mappings/predicate_grounding.tsv; scripts/ground_causal_predicates.py; scripts/migrate_enables_trait_edges.py; local proposal tables; Wildcard rows9/58 and writer lines159–175; migration lines90–97 | partial | The wildcard enables/inhibits mappings can recur when an empty ID is filled. The writer skips existing nonempty IDs, and the trait-object migration does not repair edge8 because its object is a process. Proposal distinctions support keeping executor and input roles separate. |
| bibliography | Primary-source identity and scoped claim ledger; Six references, six quotations, ten edge annotations | partial | All six identities resolve and all six snippets are exact at their inspected locations. One snippet is an article-title phrase rather than abstract text. Four new acquisition attempts yielded three hashed metadata responses; five reused files retain original receipts. Failed body responses are not source evidence. |
| hentges | https://pubmed.ncbi.nlm.nih.gov/21413255/; Anaerobes: General Characteristics; complete indexed chapter summary | partial | The definition quotation is exact, but this source uses anaerobes for organisms unable to grow with oxygen and distinguishes facultative organisms. That narrower classification does not directly supply the entire broad METPO growth-without-oxygen definition. No fresh chapter-body access is claimed. |
| clostridium | https://pubmed.ncbi.nlm.nih.gov/18430081/; DOI10.1111/j.1365-2958.2008.06192.x; title and abstract opening | supports | The source supports the generic obligate-anaerobe note for C. acetobutylicum. Detailed engineering and defense mechanisms were outside this verification scope. |
| fragilis | https://pubmed.ncbi.nlm.nih.gov/22778399/; DOI10.1073/pnas.1203796109; exact title phrase and abstract opening | partial | The cited phrase is exact in the title. Generic anaerobe and limited oxygen-tolerance context are supported; a genetically modified experimental result is not transferred to the unmodified species. The gut adjective was not independently established by the inspected title/abstract, and failed body access is inconclusive. Detailed genetic or fitness mechanisms were not assessed. |
| lu | https://doi.org/10.1038/s41579-021-00583-y; PMID34183820; PMC9191689 BioC abstract offset86 | partial | All four graph excerpts match the abstract. It expressly discusses obligate anaerobes, hypoxic habitat and broad oxygen-stress context. Hypoxia does not mean zero oxygen, and habitat association alone does not experimentally establish trait conferral. Detailed catalyst vulnerability and pathogen defense routes remain unassessed. |
| anammox | https://doi.org/10.1038/s43705-023-00251-7; PMID37137967; PMC10156729 Introduction section1 paragraph4 and abstract | supports | The environmental anammox study provides generic context for enzyme classes and detoxification, with variable activities among the studied enrichments. It does not establish identical activities in every anaerobe, and its details were not transferred to pathogen defense. |
| respiration | https://doi.org/10.1038/s41564-023-01560-2; PMID38177297; title and first conceptual abstract sentence | partial | The conceptual source text supports reductase-mediated use of nonoxygen acceptors in anaerobic ecosystems, in a gut-bacterial context. Specific substrate/reductase routes, host metabolism, colonization and fitness were not validated or reconstructed. Anaerobic respiration remains one possible route rather than a universal condition of anaerobic growth. |

## Limits And Additional Notes

- This is a complete documentary and scoped scientific review of the whole record, not validation of detailed pathogen survival, defense, colonization or host-derived respiratory pathways. Those claims were not reconstructed or optimized.
- The B. fragilis source was inspected at title/abstract level. Its gut adjective remains unverified; HTTP500 and challenge pages are not evidence of falsehood. Genetic intervention results were not transferred to the unmodified species.
- Hentges was assessed through the complete indexed chapter summary; fresh chapter-body access was not available. Its strict terminology is distinct from the broader METPO trait.
- The Lu full-text file was reused with its original hash/time, but the current assessment used the abstract passage for generic context and exact quotations; detailed catalyst-vulnerability and pathogen-defense passages were not adjudicated.
- The environmental anammox source supports contextual enzyme classes with study-specific variation; its detailed findings were not generalized to every anaerobe or transferred to pathogens.
- The gut-respiration source was assessed only from its title and opening conceptual abstract sentence. Specific substrates, reductase routes, host metabolism and fitness mechanisms remain unassessed.
- Hypoxic habitat is reduced oxygen, not necessarily anoxia. Association with that habitat alone does not establish experimental trait conferral. Contextual NONMECHANISTIC scope is not a universal mechanism claim.
- Edge8 has compatible broad RO endpoint types; the finding concerns executor versus input meaning, not an alleged formal ban on chemical subjects.
- No exact dataset matched either canonical organism. Expression-module absence is not negative biological evidence.
- Ontology, literature and catalog reuse retain original timestamps/hashes rather than claiming fresh external releases.
- Private or remote human scientific acceptance remains unknown outside the declared ignored-inclusive local search.
- Provider reports supplied provenance/leads only; no paid research was run. No scientific record, mapping, schema, writer, status, history or generated page was changed.
- All field indices are zero-based.
- Native input capture08:45:58–59Z retained53inputs after the whole target was read.
- Source quotation matching does not by itself certify the biological interpretation of a causal edge.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T085242Z-anaerobic
kind: record
repository: CultureBotAI/TraitMech
title: Evidence and ontology review of anaerobic growth (METPO:1000603)
started_at: '2026-10-21T08:45:58Z'
finished_at: '2026-10-21T08:52:42Z'
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
summary: 'The broad anaerobic-growth record has the correct METPO identity, hierarchy
  and current identifiers. One major finding covers two distinct relation-role errors:
  process inhibition applied to chemical/trait endpoints, and an executor relation
  applied to a described chemical input. Three minor findings concern strict-source
  terminology, a physical-site/activity facet ambiguity and the bounded missing human-acceptance
  link. All ten nodes and ten edges were inspected, all six snippets are exact, and
  detailed pathogen fitness/defense mechanisms remain unassessed.'
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
  - path: data/traits/environment/anaerobic.yaml
    sha256: bdee031c6277b96ab3f66dbdf1e6782aa21fd74e02676fd287d2f2e70ee6773f
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
  - path: reports/ontology_snapshot_manifest.tsv
    sha256: 4a157279a8c4e3fc2afb5382a45c31961991bbd1f330f26d0061b0cfd0b4d213
    role: context
  - path: research/traits/environment/anaerobic-deep-research-falcon.md
    sha256: 88d19a671c32cb835159227abc0f17de7a8c531be56afa45717d35f79012fdea
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
  - path: scripts/ground_causal_nodes.py
    sha256: 204ce4162544154b1752b65da2136538847ea25ced26a52f5708eadff08f5d42
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
  - path: scripts/migrate_uniprot_instance_groundings.py
    sha256: 07d2a5405cff5857239757e0a3791f411b1d25709a5760c1e49553eed066993d
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
- target_id: METPO:1000603
  path: data/traits/environment/anaerobic.yaml
  label: anaerobic
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/anaerobic.yaml
    role: Maintained TraitRecord; scientific changes require guarded curation
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Original METPO import identity/provenance
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Fifth batch004 target in lexicographic path order. Entire target read
    before native capture. One complete record assessed, with detailed pathogen fitness/defense
    mechanisms outside the biological verification scope and retained as explicit
    limitations.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000603
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000603
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
  - METPO:1000603
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
  - METPO:1000603
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
  - METPO:1000603
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
  - METPO:1000603
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
  - METPO:1000603
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
  - METPO:1000603
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
- check_id: anaerobic-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1000603
  command: just validate data/traits/environment/anaerobic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Selected record validates.
  evidence_ids:
  - check-anaerobic-validate
- check_id: anaerobic-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000603
  command: just validate-strict data/traits/environment/anaerobic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero strict errors.
  evidence_ids:
  - check-anaerobic-strict
- check_id: anaerobic-snippets
  name: Focused source snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000603
  command: just verify-snippets --record data/traits/environment/anaerobic.yaml --out
    /private/tmp/traitmech-record-sweep-004.f7_g5r4w/anaerobic-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Six snippets across three references: five VERIFIED and one NOT_IN_ABSTRACT.
    The abstract miss is inconclusive; manual source assessment is recorded separately.'
  evidence_ids:
  - check-anaerobic-snippets
- check_id: structured-source-runner
  name: Structured-source runner discovery
  status: unavailable
  required: false
  target_ids:
  - METPO:1000603
  summary: Reused bounded discovery with official catalog fallback.
  evidence_ids:
  - runner
- check_id: expression-context
  name: Canonical-taxon dataset applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000603
  summary: Neither canonical organism matches the inspected catalog; no gene/module
    queries.
  evidence_ids:
  - expression
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T08:52:42Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T08:52:42Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T08:52:42Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T08:52:42Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T08:52:42Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T08:52:42Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T08:52:42Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-anaerobic-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/anaerobic-validate.log
  locator: Executed 2026-10-21T08:46:27Z through 2026-10-21T08:46:31Z; metadata anaerobic-validate.json
  accessed_at: '2026-10-21T08:52:42Z'
  support: context_only
  summary: Selected record validates.
  snapshot_sha256: c74e6ff468cccc5cdcb36615448c0c29cd0ab027d502bb0242e295b92ad33655
- evidence_id: check-anaerobic-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/anaerobic-strict.log
  locator: Executed 2026-10-21T08:46:27Z through 2026-10-21T08:46:31Z; metadata anaerobic-strict.json
  accessed_at: '2026-10-21T08:52:42Z'
  support: context_only
  summary: One file scanned; zero strict errors.
  snapshot_sha256: 5f0e5ee76d35629672cc5f1d85a5cbf1cc6223b8bd631496dfe086acad6f62d9
- evidence_id: check-anaerobic-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/anaerobic-snippets.log
  locator: Executed 2026-10-21T08:46:29Z through 2026-10-21T08:46:35Z; metadata anaerobic-snippets.json
  accessed_at: '2026-10-21T08:52:42Z'
  support: context_only
  summary: 'Six snippets across three references: five VERIFIED and one NOT_IN_ABSTRACT.
    The abstract miss is inconclusive; manual source assessment is recorded separately.'
  snapshot_sha256: 8b62bce44ed7e82378dc1291ede411d0fda31b80287321e5b1446537f63550e4
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/anaerobic.yaml
  locator: 'Whole record: definition, two related synonyms, xref, two examples, ten
    nodes/edges and thirteen events'
  accessed_at: '2026-10-21T08:52:42Z'
  support: partial
  summary: Broad oxygen-independent growth is correctly identified. The cited strict-anaerobe
    framing needs its narrower scope, and external relations require endpoint-role
    review. Detailed pathogen defense and fitness mechanisms were not reconstructed.
  snapshot_sha256: bdee031c6277b96ab3f66dbdf1e6782aa21fd74e02676fd287d2f2e70ee6773f
- evidence_id: shape
  kind: validation
  reference: Whole graph/history inspection
  locator: Ten nodes, ten edge endpoints, thirteen events and six snippets
  accessed_at: '2026-10-21T08:46:46Z'
  support: supports
  summary: All endpoints resolve. Twelve events explicitly disclose AI assistance
    plus the original seed. No pathway-context link is asserted.
  snapshot_sha256: 54842dae629a756d74a6d58fc193366daf5d8de3269b7095161c88a110925a09
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl; data/traits/environment/oxygen_preference.yaml
  locator: Active1000603, parent1000601 and related synonyms
  accessed_at: '2026-10-21T08:52:42Z'
  support: supports
  summary: The pinned METPO identity describes growth in the absence of molecular
    oxygen. Parent oxygen preference is broader; related-synonym scope is preserved.
    This definition does not itself require inability to grow in oxygen.
  snapshot_sha256: 322d8b076cd8769f364af42db67154ee637e4d6a190e113a5d8a5dfd4afd2afc
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml
  locator: Contextual graph scope and node-type meaning
  accessed_at: '2026-10-21T08:52:42Z'
  support: supports
  summary: NONMECHANISTIC context permits reviewed label-only proteins and does not
    require token accessions, universal mechanisms or datasets. A physical catalytic
    site and a molecular activity are different facets even when both occur in a broad
    biochemical description.
- evidence_id: provenance
  kind: search
  reference: Target history and bounded local source/mapping/writer/review search
  locator: All thirteen events and ignored-inclusive exact identifier/path/label matches
  accessed_at: '2026-10-21T08:46:46Z'
  support: partial
  summary: The exact-match decision row is APPROVED, but the linked record event is
    AI-assisted. Neither this status nor other reviews listing the file as an input
    establishes human acceptance of the target revision. No explicit local acceptance
    link was found; private/remote approval remains unknown.
  snapshot_sha256: d0503c2fdeaa8150fb4b9b1d17b9ba2fddd354c489cf9c539355c97a43176a49
  search_scope: rg --no-ignore --hidden across history,mappings,scripts,reviews/structured;
    exact command and399matching lines retained. The whole target history was read;
    unsearched remote/private acceptance remains unknown.
- evidence_id: status-rule
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md
  locator: Status/audit and verification gate
  accessed_at: '2026-10-21T08:52:42Z'
  support: supports
  summary: REVIEWED requires human scientific acceptance; AI provenance and automated
    checks are different evidence.
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Original07:36:12Z catalog with current hash-verified applicability check
  accessed_at: '2026-10-21T08:52:42Z'
  support: context_only
  summary: Neither C. acetobutylicum nor B. fragilis matches the inspected catalog.
    No other organism was substituted and no gene/module query was made. No negative
    phenotype or protein claim follows from catalog noncoverage.
  snapshot_sha256: 72df0bcf2ee13acd5c38d10aa98a78c4b2eb40e11f0582bddcb23cb931e5848e
- evidence_id: runner
  kind: search
  reference: Reused structured-source runner discovery
  locator: Original bounded ignored-inclusive08:17:15Z search
  accessed_at: '2026-10-21T08:17:15Z'
  support: context_only
  summary: The runner was unavailable in the original declared bounds; official catalog
    fallback was inspected. This preserves original times and scope, not a fresh/global
    runner-absence claim.
  snapshot_sha256: 39b52930f52e898f85ac3bbb88f11ac674a355967b5704e2b62f0bda259d404f
  search_scope: Original PATH/project/install/B4 bounds are retained in runner-discovery.json;
    ignored files were included and unsearched directories remain unknown.
- evidence_id: live-identifiers
  kind: authority
  reference: QuickGO GO:0009061; NCBI taxonomy1488/817
  locator: Current identity responses08:46:57–58Z
  accessed_at: '2026-10-21T08:46:58Z'
  support: supports
  summary: Anaerobic respiration is an active biological process. Both canonical organism
    labels match the resolved taxon identities. Identity alone does not verify phenotype
    or host association.
  snapshot_sha256: f6c7f8ce8a9e56505abdd837b349de83c4492c293cf7fd8c42f9d4da8ac13a70
- evidence_id: reused-identifiers
  kind: authority
  reference: OLS CHEBI:15379 and CHEBI:26523
  locator: Original08:17:52Z responses, current hash verification
  accessed_at: '2026-10-21T08:17:52Z'
  support: supports
  summary: Molecular oxygen and reactive oxygen species identities match their nodes.
    Original acquisition times are retained; this is not a new release check.
  snapshot_sha256: dd69f6c0e6248bfb8caba96da7242d84febc6e008ced5a2d2d751634256a6d17
- evidence_id: ro-pato
  kind: authority
  reference: RO ontology and PATO authority snapshots
  locator: RO2212 inherited regulation roles; RO2327 executor meaning; PATO1456 oxygen
    independence
  accessed_at: '2026-10-21T08:48:24Z'
  support: partial
  summary: RO inhibits inherits process endpoints. RO enables has broad material/process
    endpoints but specifies an executing actor, not merely any required input. PATO
    oxygen independence agrees with the broad trait and does not require oxygen intolerance.
    Original RO inspections were08:04:46Z and07:58:06Z; the cached PATO entry was
    inspected08:46:52Z.
  snapshot_sha256: 88639f1034f225cc27e7fd3606408f97a9d4d0b821a99d5055fd9da393de9d62
- evidence_id: ledger
  kind: validation
  reference: Independent complete node/edge documentary ledger
  locator: Ten nodes and ten edges; zero-based indices
  accessed_at: '2026-10-21T08:48:24Z'
  support: partial
  summary: Edge1 conflicts with inherited process endpoints. Edge8 has broadly compatible
    types but its input-availability description does not substantiate the narrower
    executor relation. Node4 mixes a physical site with an activity facet. Optional
    label-only aggregates and contextual confers edges are not automatic type defects.
  snapshot_sha256: 8a943237658d2b8f1e107a5b6072adb43e4bd565cf8340458e5127cd47b16b5f
- evidence_id: owners
  kind: record_content
  reference: mappings/predicate_grounding.tsv; scripts/ground_causal_predicates.py;
    scripts/migrate_enables_trait_edges.py; local proposal tables
  locator: Wildcard rows9/58 and writer lines159–175; migration lines90–97
  accessed_at: '2026-10-21T08:48:24Z'
  support: partial
  summary: The wildcard enables/inhibits mappings can recur when an empty ID is filled.
    The writer skips existing nonempty IDs, and the trait-object migration does not
    repair edge8 because its object is a process. Proposal distinctions support keeping
    executor and input roles separate.
  snapshot_sha256: 4be4648e0cea40a869e1cfd53f69636ec3d2e8fdd2c76c247000279541de3239
- evidence_id: bibliography
  kind: database
  reference: Primary-source identity and scoped claim ledger
  locator: Six references, six quotations, ten edge annotations
  accessed_at: '2026-10-21T08:48:49Z'
  support: partial
  summary: All six identities resolve and all six snippets are exact at their inspected
    locations. One snippet is an article-title phrase rather than abstract text. Four
    new acquisition attempts yielded three hashed metadata responses; five reused
    files retain original receipts. Failed body responses are not source evidence.
  snapshot_sha256: 7c1250c207117fba9e326fff2b3163ccc36ca387be3e3af6de948fc1dd7da546
- evidence_id: hentges
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/21413255/
  locator: 'Anaerobes: General Characteristics; complete indexed chapter summary'
  accessed_at: '2026-10-21T08:16:47Z'
  support: partial
  summary: The definition quotation is exact, but this source uses anaerobes for organisms
    unable to grow with oxygen and distinguishes facultative organisms. That narrower
    classification does not directly supply the entire broad METPO growth-without-oxygen
    definition. No fresh chapter-body access is claimed.
  snapshot_sha256: 15b83e8e2ef49c300ee19bd40d28783bb19b5b8759aed9f301138b2e8236e341
- evidence_id: clostridium
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/18430081/
  locator: DOI10.1111/j.1365-2958.2008.06192.x; title and abstract opening
  accessed_at: '2026-10-21T08:46:39Z'
  support: supports
  summary: The source supports the generic obligate-anaerobe note for C. acetobutylicum.
    Detailed engineering and defense mechanisms were outside this verification scope.
  snapshot_sha256: c402d0d945b9d0a856de2332beed91580b1153f55baac7f4846c303b90f58bd8
- evidence_id: fragilis
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/22778399/
  locator: DOI10.1073/pnas.1203796109; exact title phrase and abstract opening
  accessed_at: '2026-10-21T08:46:36Z'
  support: partial
  summary: The cited phrase is exact in the title. Generic anaerobe and limited oxygen-tolerance
    context are supported; a genetically modified experimental result is not transferred
    to the unmodified species. The gut adjective was not independently established
    by the inspected title/abstract, and failed body access is inconclusive. Detailed
    genetic or fitness mechanisms were not assessed.
  snapshot_sha256: 20668fd36a6869a1db050a7586e8fa2fb422773b15a93789d1ce43017f1738b1
- evidence_id: lu
  kind: primary_source
  reference: https://doi.org/10.1038/s41579-021-00583-y
  locator: PMID34183820; PMC9191689 BioC abstract offset86
  accessed_at: '2026-10-21T08:25:23Z'
  support: partial
  summary: All four graph excerpts match the abstract. It expressly discusses obligate
    anaerobes, hypoxic habitat and broad oxygen-stress context. Hypoxia does not mean
    zero oxygen, and habitat association alone does not experimentally establish trait
    conferral. Detailed catalyst vulnerability and pathogen defense routes remain
    unassessed.
  snapshot_sha256: 8ce53770e39dc8f72cd5dc03fff9676954ed0f43c0ac36be40e2b78466239430
- evidence_id: anammox
  kind: primary_source
  reference: https://doi.org/10.1038/s43705-023-00251-7
  locator: PMID37137967; PMC10156729 Introduction section1 paragraph4 and abstract
  accessed_at: '2026-10-21T08:24:58Z'
  support: supports
  summary: The environmental anammox study provides generic context for enzyme classes
    and detoxification, with variable activities among the studied enrichments. It
    does not establish identical activities in every anaerobe, and its details were
    not transferred to pathogen defense.
  snapshot_sha256: 3b77abf7cca79062999afc25a02058a2207f166919f1a6ff49eab543503eaa4b
- evidence_id: respiration
  kind: primary_source
  reference: https://doi.org/10.1038/s41564-023-01560-2
  locator: PMID38177297; title and first conceptual abstract sentence
  accessed_at: '2026-10-21T08:46:36Z'
  support: partial
  summary: The conceptual source text supports reductase-mediated use of nonoxygen
    acceptors in anaerobic ecosystems, in a gut-bacterial context. Specific substrate/reductase
    routes, host metabolism, colonization and fitness were not validated or reconstructed.
    Anaerobic respiration remains one possible route rather than a universal condition
    of anaerobic growth.
  snapshot_sha256: 66df827b7589e4e7e26f8c31e1516305c7bce3a76e470c437ff430e1078ceffa
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: concept, synonyms, hierarchy and xref'
  outcome: supported
  target_ids:
  - METPO:1000603
  summary: Active METPO1000603, oxygen-preference parent1000601 and related synonyms
    denote the intended broad trait. PATO1456 is oxygen independence. Explicit obsolete-term
    replacements were inspected rather than inferred.
  evidence_ids:
  - identity
  - ro-pato
  - record
  - ledger
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: broad class versus strict source usage'
  outcome: concern
  target_ids:
  - METPO:1000603
  summary: The definition matches METPO, but the nearest chapter quotation uses a
    narrower strict-anaerobe sense. The distinction should be explicit, preserving
    broad growth capability without importing universal oxygen intolerance.
  evidence_ids:
  - identity
  - hentges
  - lu
- assessment_id: model
  area: representation
  topic: 'Native checklist: category, term kind and graph scope'
  outcome: supported
  target_ids:
  - METPO:1000603
  summary: ENVIRONMENT/CLASS and contextual NONMECHANISTIC scope fit the target. Optional
    label-only protein aggregates, datasets and accession instances are not mandatory
    merely because biochemical context is present.
  evidence_ids:
  - record
  - policy
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: both canonical organisms and limits'
  outcome: unknown
  target_ids:
  - METPO:1000603
  summary: Taxon identities resolve and both sources support their generic anaerobic
    phenotype contexts. The B. fragilis gut adjective was not independently verified
    on available title/abstract text; failed body access leaves it unknown. No mutant
    result was generalized to the species and no detailed defense route was assessed.
  evidence_ids:
  - live-identifiers
  - clostridium
  - fragilis
  - bibliography
- assessment_id: grounding
  area: grounding
  topic: 'Native checklist: current identifiers and represented facets'
  outcome: concern
  target_ids:
  - METPO:1000603
  summary: Current METPO, GO, CHEBI, PATO and taxonomy match their intended concepts.
    Node4 mixes physical catalytic sites/metal centers with an activity type; this
    requires clarification of the represented facet, not an invented mandatory accession.
  evidence_ids:
  - identity
  - live-identifiers
  - reused-identifiers
  - ro-pato
  - ledger
  - policy
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all ten endpoint pairs and relation roles'
  outcome: concern
  target_ids:
  - METPO:1000603
  summary: Edge1 misuses process regulation for chemical-to-trait inhibition. Edge8
    uses the executor relation for a described chemical input; its broad endpoint
    classes fit, so this is a narrower meaning mismatch. Compatible protein-executor
    edge5 and provisional contextual confers edges are retained.
  evidence_ids:
  - ledger
  - ro-pato
  - owners
  - record
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: all citations, excerpts and causal interpretation'
  outcome: unknown
  target_ids:
  - METPO:1000603
  summary: All six quotations are exact. Obligately anaerobic and environmental anammox
    sources retain their scopes. Hypoxic-habitat association is not experimental trait
    conferral. The gut-respiration reference was assessed at conceptual level; detailed
    pathogen fitness and defense claims remain explicitly unassessed.
  evidence_ids:
  - bibliography
  - hentges
  - lu
  - anammox
  - respiration
  - fragilis
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: required structure, discussions and optional surfaces'
  outcome: supported
  target_ids:
  - METPO:1000603
  summary: All endpoints resolve and required identity/evidence structures are present.
    No invented protein instances, datasets or universal respiratory pathway are needed
    for contextual scope. Relevant existing research is a provenance lead, not primary
    evidence.
  evidence_ids:
  - shape
  - record
  - policy
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: canonical-taxon structured-source applicability'
  outcome: supported
  target_ids:
  - METPO:1000603
  summary: Neither canonical taxon matches the inspected dataset catalog. No substitute
    organism or expression module was used; noncoverage supplies no negative phenotype
    evidence.
  evidence_ids:
  - expression
  - runner
- assessment_id: audit
  area: provenance
  topic: 'Native checklist: history, acceptance and future input owners'
  outcome: concern
  target_ids:
  - METPO:1000603
  summary: Twelve events disclose AI assistance alongside the seed. APPROVED mapping
    status and automated history integrity do not establish human acceptance; none
    is linked in the bounded local search. Existing-edge correction and mapping recurrence
    are distinct follow-up tasks.
  evidence_ids:
  - provenance
  - status-rule
  - shape
  - owners
findings:
- finding_id: external-relation-semantics
  issue_key: anaerobic-external-relation-semantics
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Two external relations assign unsupported endpoint roles
  description: Edge1 uses RO inhibits between oxygen and the trait although it inherits
    process-to-process regulation roles. Edge8 uses RO enables for an electron acceptor
    described as an available input. Its broad material/process types are compatible,
    but the description does not establish the executing role required by enables.
    These are separate semantic defects; neither native schema success nor a blanket
    ban on chemical actors resolves them. No OWL reasoner execution is claimed.
  target_ids:
  - METPO:1000603
  field_paths:
  - causal_graphs[0].edges[1]
  - causal_graphs[0].edges[8]
  evidence_ids:
  - ledger
  - ro-pato
  - owners
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/anaerobic.yaml
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
- finding_id: strict-source-broad-definition
  issue_key: anaerobic-strict-source-broad-definition
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish broad anaerobic growth from strict source terminology
  description: The record correctly defines the broad METPO capability to grow without
    oxygen. Its nearest definition quotation and the Lu abstract use a stricter obligate-anaerobe
    scope. Make the distinction explicit instead of treating oxygen intolerance as
    a necessary property of every member of the broad class. This is bounded attribution/scope
    precision, not an incorrect ontology identity.
  target_ids:
  - METPO:1000603
  field_paths:
  - definition_source
  - evidence[0]
  - causal_graphs[0].scope_notes
  evidence_ids:
  - identity
  - hentges
  - lu
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: catalytic-site-facet
  issue_key: anaerobic-catalytic-site-facet
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Clarify physical catalytic sites versus molecular activity
  description: Node4 names physical catalytic sites and its description includes metal
    centers, while its type is MOLECULAR_FUNCTION. Clarify whether the node denotes
    an activity or a physical bearer/site and align wording and type. No specific
    replacement enum or ontology accession is asserted without further curation.
  target_ids:
  - METPO:1000603
  field_paths:
  - causal_graphs[0].nodes[4]
  evidence_ids:
  - ledger
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: anaerobic-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human scientific acceptance is not linked locally
  description: The ignored-inclusive local record/history/mapping/writer/review search
    did not identify explicit human scientific acceptance of this revision. Twelve
    AI-assisted events, the original seed and an APPROVED exact-match row are not
    that acceptance. Private or remote approval remains unknown.
  target_ids:
  - METPO:1000603
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - status-rule
  - shape
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: repair-relations
  description: In separately authorized curation, choose relations matching the two
    documented endpoint roles and review wildcard mapping recurrence.
  finding_ids:
  - external-relation-semantics
  target_ids:
  - METPO:1000603
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/anaerobic.yaml
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
  - Edge1 respects the selected relation’s inherited domain/range and biological meaning.
  - Edge8 distinguishes process execution from chemical input availability without
    asserting a blanket formal exclusion of chemical actors.
  - A maintained ground-predicates dry run assesses recurrence; existing nonempty
    IDs require guarded correction and are not overwritten by that writer.
  - Run focused strict/graph checks and just qc, append native curation/history and
    regenerate affected products after authorized edits.
- action_id: clarify-source-scope
  description: Make the broad METPO definition and narrower obligate-anaerobe source
    scope explicit, preserving contextual claims at their evidenced level.
  finding_ids:
  - strict-source-broad-definition
  target_ids:
  - METPO:1000603
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Definition authority and source terminology are distinguishable.
  - No universal oxygen intolerance or experimentally established habitat conferral
    is inferred from these excerpts.
  - Run focused record validation after any authorized changes.
- action_id: clarify-node-facet
  description: Resolve whether node4 denotes catalytic activity or a physical site/bearer,
    and align its label, description and type.
  finding_ids:
  - catalytic-site-facet
  target_ids:
  - METPO:1000603
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The represented entity facet is unambiguous and compatible with its node type.
  - No arbitrary accession or detailed pathogen mechanism is introduced.
  - Run focused strict/graph validation after authorized changes.
- action_id: link-acceptance
  description: Locate and link existing human acceptance or obtain it through the
    established process, preserving AI provenance and reassessing status if acceptance
    remains unavailable.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000603
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/anaerobic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies this record revision and scientific scope.
  - Mapping decisions, AI events and validator success are not represented as human
    scientific sign-off.
limitations:
- This is a complete documentary and scoped scientific review of the whole record,
  not validation of detailed pathogen survival, defense, colonization or host-derived
  respiratory pathways. Those claims were not reconstructed or optimized.
- The B. fragilis source was inspected at title/abstract level. Its gut adjective
  remains unverified; HTTP500 and challenge pages are not evidence of falsehood. Genetic
  intervention results were not transferred to the unmodified species.
- Hentges was assessed through the complete indexed chapter summary; fresh chapter-body
  access was not available. Its strict terminology is distinct from the broader METPO
  trait.
- The Lu full-text file was reused with its original hash/time, but the current assessment
  used the abstract passage for generic context and exact quotations; detailed catalyst-vulnerability
  and pathogen-defense passages were not adjudicated.
- The environmental anammox source supports contextual enzyme classes with study-specific
  variation; its detailed findings were not generalized to every anaerobe or transferred
  to pathogens.
- The gut-respiration source was assessed only from its title and opening conceptual
  abstract sentence. Specific substrates, reductase routes, host metabolism and fitness
  mechanisms remain unassessed.
- Hypoxic habitat is reduced oxygen, not necessarily anoxia. Association with that
  habitat alone does not establish experimental trait conferral. Contextual NONMECHANISTIC
  scope is not a universal mechanism claim.
- Edge8 has compatible broad RO endpoint types; the finding concerns executor versus
  input meaning, not an alleged formal ban on chemical subjects.
- No exact dataset matched either canonical organism. Expression-module absence is
  not negative biological evidence.
- Ontology, literature and catalog reuse retain original timestamps/hashes rather
  than claiming fresh external releases.
- Private or remote human scientific acceptance remains unknown outside the declared
  ignored-inclusive local search.
- Provider reports supplied provenance/leads only; no paid research was run. No scientific
  record, mapping, schema, writer, status, history or generated page was changed.
notes:
- All field indices are zero-based.
- Native input capture08:45:58–59Z retained53inputs after the whole target was read.
- Source quotation matching does not by itself certify the biological interpretation
  of a causal edge.
tags:
- record-review
- anaerobic
- environment
- needs-curation
```
