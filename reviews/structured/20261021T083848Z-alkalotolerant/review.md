# Evidence and ontology review of alkalotolerance (METPO:1003009)

- Review: 20261021T083848Z-alkalotolerant
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T08:33:02Z
- Finished UTC: 2026-10-21T08:38:48Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Alkalotolerant has the correct METPO identity, definition, synonym and parent, and all current external identifiers resolve. Three major findings concern unsupported neutral-optimum example membership, a material-domain relation assigned to a process, and two edges overstating a source hypothesis. Two minor findings concern the sodium-gradient node type and a bounded missing human-acceptance link. All eleven nodes, ten edges and six snippets were assessed; all six excerpts are exact.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Third batch004 target in path order, following the saved aerotolerant review. Entire record read before native capture; one complete target is assessed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1003009 | data/traits/environment/alkalotolerant.yaml | maintained | alkalotolerant |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1003009 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1003009 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1003009 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1003009 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1003009 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1003009 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1003009 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1003009 | Selected record validates. |
| Focused strict validation | passed | True | METPO:1003009 | One file scanned; zero errors. |
| Focused source snippet check | passed | True | METPO:1003009 | Six snippets across three references: four VERIFIED and two NOT_IN_ABSTRACT. Manual source review subsequently verified all six; an abstract miss is inconclusive. |
| Structured-source runner discovery | unavailable | False | METPO:1003009 | Reused bounded runner discovery; official catalog fallback inspected. |
| Canonical-organism expression applicability | not_applicable | False | METPO:1003009 | Neither canonical taxon has a matching dataset in the inspected catalog. |

## Scientific And Domain Assessments

### Native checklist: identifier, definition, synonym and hierarchy

identity: supported. Targets: METPO:1003009.

Active METPO identity, exact synonym and broader pH-growth parent match the intended neutral-optimum alkaline-tolerance class. The literature abstract supports its broader context; the precise neutral-optimum clause is directly verified in METPO.

### Native checklist: category and NONMECHANISTIC context

representation: supported. Targets: METPO:1003009.

ENVIRONMENT/CLASS and contextual scope are appropriate. The mechanism wording in the title does not by itself require scope promotion, protein examples or a reconstructed universal pathway.

### Native checklist: canonical organism membership versus taxonomy

evidence: concern. Targets: METPO:1003009.

Both taxon IDs resolve correctly, but the cited alkaliphile papers do not establish the neutral-optimum membership required here. The finding is scoped to these sources and examples, not every possible strain or growth condition.

### Native checklist: all current external node identifiers

grounding: supported. Targets: METPO:1003009.

GO activity and pH-process terms, alkaline quality, hydroxide and METPO identity fit the documented exact/close-match facets. Historical retracted identifiers are not present errors.

### Native checklist: all eleven nodes and ten edges

consistency: concern. Targets: METPO:1003009.

Edge2 uses a material-subject relation for proton retention as a process. Node10 denotes a gradient but is typed as a process. The protein actor on edge3, provisional challenges/confers and optional ungrounded predicates introduce no additional confirmed typing defects.

### Native checklist: all ten edge claims and six snippets

evidence: concern. Targets: METPO:1003009.

All six snippets are verified. General homeostasis and antiport context is supported; edges7–8 overstate a taxon-bounded source hypothesis. Edge6 remains unverified at its own inaccessible chapter body.

### Native checklist: required fields and optional evidence surfaces

completeness: supported. Targets: METPO:1003009.

The record has required identity, definition and evidence surfaces, with all graph endpoints present. Optional datasets, protein instances and external IDs are not compulsory additions to this contextual graph.

### Native checklist: canonical-taxon structured-source applicability

evidence: supported. Targets: METPO:1003009.

Neither canonical organism matches the inspected catalog, and no neighboring Bacillus species was substituted. Missing coverage is not negative biological evidence.

### Native checklist: AI history, human acceptance and maintained owners

provenance: concern. Targets: METPO:1003009.

AI involvement is explicit. The bounded local search lacks an acceptance link identifying this revision; mapping/writer recurrence is distinguished from existing record repair.

## Findings

### canonical-example-scope: Cited examples do not establish neutral-optimum alkalotolerance

major / open / confirmed; issue key: alkalotolerant-canonical-example-scope.

The canonical examples cite studies of alkaliphilic C-125 and extreme facultative alkaliphile OF4. Their taxon labels are correct, but the papers do not establish the neutral growth optimum required by this record. High-pH growth and facultative growth near neutrality are not equivalent to a neutral optimum. Do not infer that every strain or condition of these species is categorically excluded.

### contributes-to-domain: Proton-retention process is assigned a material-subject relation

major / open / confirmed; issue key: alkalotolerant-contributes-to-domain.

Edge2 uses RO0002326 contributes-to with the explicitly process-typed proton-retention subject. Its inherited domain is material entity. The process object fits, and the separate protein-to-process edge3 is compatible under native functional-facet policy. Native shape validation passing does not remove this semantic conflict.

### surface-hypothesis-scope: Surface-chemistry edges remove the source’s uncertainty and taxon scope

major / open / confirmed; issue key: alkalotolerant-surface-hypothesis-scope.

Edges7–8 state adsorption and repulsion categorically. The cited review presents them as a proposed explanation in alkaliphilic Bacillus, with possible growth assistance. Preserve those bounds rather than treating them as established generic mechanisms of neutral-optimum alkalotolerance. This is not a claim that the chemistry is false; the separate inaccessible chapter edge6 is not included as a confirmed error.

### sodium-gradient-type: Sodium gradient is typed as a biological process

minor / open / confirmed; issue key: alkalotolerant-sodium-gradient-type.

Node10’s description explicitly names a transmembrane sodium gradient. The native STATE enum distinguishes such a gradient from the process that establishes it. The correct description and unconstrained supports edge remain understandable, making this a bounded local type-precision issue.

### human-acceptance-link: Human scientific acceptance is not linked locally

minor / open / confirmed; issue key: alkalotolerant-human-acceptance-link.

The twelve AI-assisted events and original seed disclose provenance, but the bounded inspected local record/history/review surfaces do not link human acceptance to this revision. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### repair-examples

In separately authorized curation, replace or re-scope the two examples using direct evidence that meets the neutral-optimum definition; retain correct taxonomy and source-strain distinctions.

- Each retained canonical example has source-backed alkaline tolerance and a neutral growth optimum in its stated conditions.
- Do not substitute high-pH growth or facultative neutral-pH growth for an optimum measurement.
- Run focused record/taxon validation, preserve native provenance and regenerate affected products after authorized edits.

### repair-relation

Reconcile edge2 with its actual process subject and review the wildcard mapping to prevent recurrence.

- Verify the chosen relation’s inherited endpoint roles and intended meaning.
- Preserve the compatible material-protein edge3 and allowed GO function facet.
- Use the maintained ground-predicates dry run to inspect recurrence; its empty-ID behavior cannot correct existing nonempty IDs.
- After authorized curation, run strict validation, graph checks and just qc with required history and derived products.

### qualify-surface-evidence

Preserve the proposed nature and alkaliphilic Bacillus context of the adsorption/repulsion explanation, or supply direct evidence for a stronger claim at the intended scope.

- Edges7–8 retain the nearest source’s uncertainty and organism context.
- Do not describe the underlying chemistry as disproven.
- Keep edge6’s unavailable chapter evidence separate; verify its actual body before claiming direct support.
- Run focused validation after any authorized change.

### repair-state-type

Align the sodium-motive-force node with the native gradient-versus-process distinction while retaining the documented contextual meaning.

- Node10’s type agrees with its gradient description, or any revised process meaning has its own support.
- Do not duplicate the same issue as an extra unconstrained supports-edge error.
- Run focused strict and graph validation after authorized curation.

### link-acceptance

Locate and link existing human scientific acceptance or obtain it through the established process; preserve AI history and reassess status if acceptance remains unavailable.

- Acceptance identifies the record revision and scientific scope.
- Automated checks and AI history are not presented as human approval.

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
| check-alkalotolerant-validate | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkalotolerant-validate.log; Executed 2026-10-21T08:33:43Z through 2026-10-21T08:33:45Z; metadata alkalotolerant-validate.json | context_only | Selected record validates. |
| check-alkalotolerant-strict | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkalotolerant-strict.log; Executed 2026-10-21T08:33:43Z through 2026-10-21T08:33:46Z; metadata alkalotolerant-strict.json | context_only | One file scanned; zero errors. |
| check-alkalotolerant-snippets | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkalotolerant-snippets.log; Executed 2026-10-21T08:33:49Z through 2026-10-21T08:33:54Z; metadata alkalotolerant-snippets.json | context_only | Six snippets across three references: four VERIFIED and two NOT_IN_ABSTRACT. Manual source review subsequently verified all six; an abstract miss is inconclusive. |
| record | data/traits/environment/alkalotolerant.yaml; Entire record, including two examples, eleven nodes, ten edges and thirteen events | partial | The identity and definition match METPO. The examples do not establish neutral-optimum membership; one external relation conflicts with its subject role, two surface-chemistry edges omit source uncertainty, and a gradient is typed as a process. |
| shape | Complete graph/history inspection; All node IDs, endpoints, snippets and events | supports | Eleven nodes and ten edges have resolved endpoints; six snippets and thirteen events, twelve AI-assisted plus seeding. No pathway-context link is asserted. |
| identity | data/raw/metpo.owl; data/traits/environment/ph_growth_preference.yaml; Active1003009 and parent1003000; complete exact-name/synonym scan | supports | Neutral-optimum alkaline tolerance, exact synonym alkalitolerant and broader pH growth preference match the pinned ontology. A high-pH growth observation alone does not establish the neutral-optimum clause. |
| current-identifiers | QuickGO, ChEBI and NCBI Taxonomy; GO0051139, CHEBI16234 and taxa86665/79885; live responses08:34:19–21Z | supports | The active antiporter activity, hydroxide and both current taxon labels resolve correctly. Historical Bacillus names explain citation nomenclature; taxon correctness does not establish the phenotype. |
| go-reuse | Official QuickGO response; GO0051453; original07:58:24Z retrieval, current byte verification | supports | Regulation of intracellular pH is active and the maintained close-match supports the contextual cytoplasmic-homeostasis node. The historical replaced GO identifier is not a current error. |
| pato | Read-only PATO snapshot; PATO0001430 current cache inspection | supports | Alkaline is the intended environmental-condition quality facet. Reusing this cached authority does not certify a new release. |
| ro | Read-only RO snapshot; RO0002326 inherited domain/range; original08:04:46Z inspection, current hash verification | partial | Contributes-to inherits material subject and process object via RO0002216, RO0002500 and RO0002595. Proton retention is explicitly a process; the separate antiporter protein is a compatible material subject. Native validation is not a domain reasoner. |
| graph-ledger | Independent documentary node/edge inspection; All eleven nodes and ten edges, zero-based indices | partial | Edge2 has the inherited material-domain mismatch. Node10 describes a sodium gradient but is typed BIOLOGICAL_PROCESS. Other optional labels, aggregate ion node, allowed GO function facet and provisional challenges/confers relations do not justify extra errors. |
| owners | mappings/predicate_grounding.tsv; scripts/ground_causal_predicates.py; native enum and proposals; Wildcard contributes-to mapping; writer empty-ID contract; v2 challenges/v8 confers | partial | The wildcard mapping can recreate edge2 when its ID is empty, while existing IDs are skipped. The provisional predicates accommodate the current roles. Sodium-gradient correction belongs to the maintained record; the bounded ignored-inclusive owner search found no separate sodium-specific rule. |
| policy | src/traitmech/schema/traitmech.yaml; docs/GROUNDING_POLICY.md; CausalNodeTypeEnum STATE and protein function facets; NONMECHANISTIC scope | supports | STATE explicitly denotes a gradient or steady value, distinct from its establishment. A GO activity grounding may describe the function of a protein actor. Contextual scope does not require token protein accessions, datasets or one universal mechanism. |
| provenance | Target history and bounded local provenance; All thirteen events; exact identifier/path/slug search across history,mappings,scripts,reviews/structured | partial | Twelve AI-assisted events and the seed are explicit. The ignored-inclusive search found only other reviews listing this record as an input, with no explicit human acceptance link for this target revision. Private and remote acceptance remains unknown. |
| status-rule | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md; Status/audit and human verification gate | supports | REVIEWED requires human scientific acceptance; AI assistance and successful automated checks are distinct provenance. |
| expression | https://imodulondb.org/api/datasets; Official catalog originally07:36:12Z, hash-verified applicability assessment08:34:21Z | context_only | Neither canonical taxon has a matching dataset. Historical Bacillus names were not used to substitute B. subtilis. No gene/module query or negative biological inference followed. |
| runner | Reused structured-source runner discovery; Original bounded ignored-inclusive discovery08:17:15Z | context_only | No usable runner was found in the originally declared PATH/project/install/B4 bounds. This is reused evidence, not a new global filesystem-absence claim; the official catalog was the fallback. |
| definition-source | https://doi.org/10.1016/j.bbamem.2005.09.010; Complete indexed abstract; definition and edges0/2 | partial | The abstract supports the alkali-tolerant versus extremely alkaliphilic distinction and proton-capture/retention context; all three associated snippet occurrences are exact. It does not independently establish the precise neutral-optimum clause available in METPO. Full body access failed, so that clause is not declared disproven. |
| halodurans | https://oup.silverchair-cdn.com/article-minimal/2376264; PMID11058132; Introduction paragraphs1–2 and Results/Discussion General features first paragraph; browser by08:35:40Z, downloaded article08:36:09Z | partial | The cited C-125 genome paper places the organism in an alkaliphilic Bacillus context, with poor/no neutral-pH growth and strong alkaline growth. It does not establish neutral-optimum membership. This is a mismatch in the cited example evidence, not a claim that no strain or condition could meet the trait. |
| pseudofirmus | https://pmc.ncbi.nlm.nih.gov/articles/PMC3228905/; PMID21951522; BioC abstract offset155, Introduction1439 and3620 | partial | The source identifies OF4 as an extreme facultative alkaliphile, in a class defined by alkaline growth optima. It supports alkaliphilic adaptation, not the record’s neutral-optimum example claim. Taxonomic identity is correct and physiological conditions can affect optima. |
| homeostasis | https://doi.org/10.1038/nrmicro2549; Publisher Abstract preview; BioC Conclusions offset44016, Introduction671 and alkaline-homeostasis discussion10376; original retrievals07:55:43/07:56:36/07:57:33Z | supports | The two short excerpts are exact. The source supports homeostasis during growth beyond the cytoplasmic pH range and its cell-wide character; generic contextual support is distinct from proof that either canonical organism meets the neutral-optimum definition. |
| antiporter-source | https://pmc.ncbi.nlm.nih.gov/articles/PMC7349511/; DOI10.3390/ijms21124566; Abstract sentence1 and Section3.2 (sec3dot2-ijms-21-04566) paragraph1 | supports | The snippet is exact and the source supports cation/proton antiporters in ion and pH homeostasis. Its generic protein-function context supports edge3 without making an antiporter universally necessary for the trait. |
| electrogenic-source | https://pmc.ncbi.nlm.nih.gov/articles/PMC9408914/; DOI10.3390/ijms23169156; Section3 (sec3-ijms-23-09156) paragraph1 | supports | The source supports increased importance of electrogenic antiport at alkaline external pH. This is a general prokaryotic contextual claim, not evidence of one exclusive alkalotolerance route. |
| chapter | https://link.springer.com/chapter/10.1007/978-4-431-55408-0_4; Publisher landing page and Crossref metadata; body unavailable | context_only | The chapter citation resolves, but the particular surface-polymer homeostasis statement at edge6 was not verified in its own source body. Similar claims elsewhere are not silently substituted for this citation. |
| surface-hypothesis | https://doi.org/10.1128/MMBR.63.4.735-750.1999; Actual PDF p739, Cell Walls → Acidic polymers; p736 condition-scope warning | partial | The source proposes adsorption of sodium/hydronium and repulsion of hydroxide by acidic wall components in alkaliphilic Bacillus. It qualifies both that explanation and consequent growth assistance as possible. Edges7–8 omit those uncertainty and taxon-context bounds. The chemistry is not declared false. |
| sodium-source | https://link.springer.com/article/10.1007/s11244-024-01919-7; Actual full HTML section3.3; separately inspected linked correction | supports | The reviewed source explicitly discusses sodium motive force in intracellular pH control. Its linked correction concerns acknowledgement/funding text, not this scientific statement. This establishes contextual source support, not the correctness of the graph node’s process type. Its alkaliphile context does not independently establish the neutral-optimum conjunction. |
| bibliography | Primary-source identity and claim ledger; Nine references, ten edges and all six snippet occurrences | partial | All references resolve and all six snippets are exact. Twenty-eight new acquisition attempts and twenty-two hashed responses retain failures, API-help and browser challenges separately from article text. Three Krulwich reuses retain original timestamps/hashes. Definition-source and chapter body limitations remain explicit. |

## Limits And Additional Notes

- The definition’s exact neutral-optimum clause is verified in METPO but not in the accessible abstract of its nearest literature source; body-access failure does not disprove it.
- Edge6’s chapter citation resolves but its body was unavailable. Other sources are not silently substituted for nearest-citation verification.
- The examples finding concerns the cited strains and source scopes; growth optima can depend on conditions, so species-wide impossibility is not inferred.
- The surface-chemistry finding concerns the source’s uncertainty and alkaliphilic Bacillus context, not a claim that adsorption or repulsion is false.
- Broad homeostasis, antiport and sodium-motive-force context does not by itself establish sufficiency for the full neutral-optimum trait definition.
- The sodium-motive-force source is a broad narrative review in alkaliphile context; its linked correction changes funding/acknowledgement text only.
- Krulwich primary text, RO, GO and expression-catalog reuse preserve original timestamps/hashes. A preview stored with a PDF suffix is identified as HTML; API-help/challenge responses are excluded.
- No matching canonical-taxon expression dataset was found in the inspected catalog. No neighboring organism was substituted and no negative biological inference follows.
- Human acceptance outside the bounded local search remains unknown.
- The existing research-provider report was inspected only as provenance and leads; no provider recommendation was automatically accepted and no paid call was made.
- No scientific record, schema, mapping, writer, status, history or generated page was changed.
- All field indices are zero-based.
- The full record was read before native capture08:33:02–03Z, which retained52input hashes.
- The existing contextual graph scope does not require token protein examples, mandatory external IDs on every node/predicate, or a universal mechanism.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T083848Z-alkalotolerant
kind: record
repository: CultureBotAI/TraitMech
title: Evidence and ontology review of alkalotolerance (METPO:1003009)
started_at: '2026-10-21T08:33:02Z'
finished_at: '2026-10-21T08:38:48Z'
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
summary: Alkalotolerant has the correct METPO identity, definition, synonym and parent,
  and all current external identifiers resolve. Three major findings concern unsupported
  neutral-optimum example membership, a material-domain relation assigned to a process,
  and two edges overstating a source hypothesis. Two minor findings concern the sodium-gradient
  node type and a bounded missing human-acceptance link. All eleven nodes, ten edges
  and six snippets were assessed; all six excerpts are exact.
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
  - path: data/traits/environment/alkalotolerant.yaml
    sha256: 54f2507b6a29cbfcfe4158addebc27aa973f605374c89e526dc267100577ac63
    role: target
  - path: data/traits/environment/ph_growth_preference.yaml
    sha256: e9ee5a74bff604a7b3ba06ff6610deb83d7df762d7e8b3647699b799be72201f
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
  - path: research/traits/environment/alkalotolerant-deep-research-falcon.md
    sha256: dc3ae63d8aed9bdd567cc83487188b31b697167ab619b7a185eeb5593509b327
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
- target_id: METPO:1003009
  path: data/traits/environment/alkalotolerant.yaml
  label: alkalotolerant
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkalotolerant.yaml
    role: Maintained TraitRecord; scientific changes require guarded curation
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Original METPO import identity/provenance
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Third batch004 target in path order, following the saved aerotolerant
    review. Entire record read before native capture; one complete target is assessed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1003009
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1003009
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
  - METPO:1003009
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
  - METPO:1003009
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
  - METPO:1003009
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
  - METPO:1003009
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
  - METPO:1003009
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
  - METPO:1003009
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
- check_id: alkalotolerant-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1003009
  command: just validate data/traits/environment/alkalotolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Selected record validates.
  evidence_ids:
  - check-alkalotolerant-validate
- check_id: alkalotolerant-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1003009
  command: just validate-strict data/traits/environment/alkalotolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero errors.
  evidence_ids:
  - check-alkalotolerant-strict
- check_id: alkalotolerant-snippets
  name: Focused source snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1003009
  command: just verify-snippets --record data/traits/environment/alkalotolerant.yaml
    --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkalotolerant-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Six snippets across three references: four VERIFIED and two NOT_IN_ABSTRACT.
    Manual source review subsequently verified all six; an abstract miss is inconclusive.'
  evidence_ids:
  - check-alkalotolerant-snippets
- check_id: structured-source-runner
  name: Structured-source runner discovery
  status: unavailable
  required: false
  target_ids:
  - METPO:1003009
  summary: Reused bounded runner discovery; official catalog fallback inspected.
  evidence_ids:
  - runner
- check_id: expression-context
  name: Canonical-organism expression applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1003009
  summary: Neither canonical taxon has a matching dataset in the inspected catalog.
  evidence_ids:
  - expression
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T08:38:48Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T08:38:48Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T08:38:48Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T08:38:48Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T08:38:48Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T08:38:48Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T08:38:48Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-alkalotolerant-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkalotolerant-validate.log
  locator: Executed 2026-10-21T08:33:43Z through 2026-10-21T08:33:45Z; metadata alkalotolerant-validate.json
  accessed_at: '2026-10-21T08:38:48Z'
  support: context_only
  summary: Selected record validates.
  snapshot_sha256: 89e715e2dc31dfedf8ba4da3feff9300d5fcb010549943094dd1524a99200875
- evidence_id: check-alkalotolerant-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkalotolerant-strict.log
  locator: Executed 2026-10-21T08:33:43Z through 2026-10-21T08:33:46Z; metadata alkalotolerant-strict.json
  accessed_at: '2026-10-21T08:38:48Z'
  support: context_only
  summary: One file scanned; zero errors.
  snapshot_sha256: d5ab5ac04b21476f86ac603726028ce03249bdd68b2973624522aeca2fa52980
- evidence_id: check-alkalotolerant-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkalotolerant-snippets.log
  locator: Executed 2026-10-21T08:33:49Z through 2026-10-21T08:33:54Z; metadata alkalotolerant-snippets.json
  accessed_at: '2026-10-21T08:38:48Z'
  support: context_only
  summary: 'Six snippets across three references: four VERIFIED and two NOT_IN_ABSTRACT.
    Manual source review subsequently verified all six; an abstract miss is inconclusive.'
  snapshot_sha256: d09ce698d0374fed87c7211dc7bf6d35d27abc30ebac8fdfe3c15ef496ed9f92
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/alkalotolerant.yaml
  locator: Entire record, including two examples, eleven nodes, ten edges and thirteen
    events
  accessed_at: '2026-10-21T08:38:48Z'
  support: partial
  summary: The identity and definition match METPO. The examples do not establish
    neutral-optimum membership; one external relation conflicts with its subject role,
    two surface-chemistry edges omit source uncertainty, and a gradient is typed as
    a process.
  snapshot_sha256: 54f2507b6a29cbfcfe4158addebc27aa973f605374c89e526dc267100577ac63
- evidence_id: shape
  kind: validation
  reference: Complete graph/history inspection
  locator: All node IDs, endpoints, snippets and events
  accessed_at: '2026-10-21T08:34:03Z'
  support: supports
  summary: Eleven nodes and ten edges have resolved endpoints; six snippets and thirteen
    events, twelve AI-assisted plus seeding. No pathway-context link is asserted.
  snapshot_sha256: 1d23282b1b3d9c63c8c1fefdba6e49602bd284bb86d580b834b1ef4f44c1f75d
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl; data/traits/environment/ph_growth_preference.yaml
  locator: Active1003009 and parent1003000; complete exact-name/synonym scan
  accessed_at: '2026-10-21T08:34:09Z'
  support: supports
  summary: Neutral-optimum alkaline tolerance, exact synonym alkalitolerant and broader
    pH growth preference match the pinned ontology. A high-pH growth observation alone
    does not establish the neutral-optimum clause.
  snapshot_sha256: b6d7d0b3727c3d5bccb1f87931da8a6ba5714928192e1126b7a43b52813716b2
- evidence_id: current-identifiers
  kind: authority
  reference: QuickGO, ChEBI and NCBI Taxonomy
  locator: GO0051139, CHEBI16234 and taxa86665/79885; live responses08:34:19–21Z
  accessed_at: '2026-10-21T08:36:22Z'
  support: supports
  summary: The active antiporter activity, hydroxide and both current taxon labels
    resolve correctly. Historical Bacillus names explain citation nomenclature; taxon
    correctness does not establish the phenotype.
  snapshot_sha256: 4eb1fac328bcce38aaadf6756189fca4712b8391830b2699bdabd4185d8130dc
- evidence_id: go-reuse
  kind: authority
  reference: Official QuickGO response
  locator: GO0051453; original07:58:24Z retrieval, current byte verification
  accessed_at: '2026-10-21T07:58:24Z'
  support: supports
  summary: Regulation of intracellular pH is active and the maintained close-match
    supports the contextual cytoplasmic-homeostasis node. The historical replaced
    GO identifier is not a current error.
  snapshot_sha256: 6ffa8306863b989f7ab01e0875ee21dab4a09e90d76d00fd9d5e46cc103aa6fe
- evidence_id: pato
  kind: authority
  reference: Read-only PATO snapshot
  locator: PATO0001430 current cache inspection
  accessed_at: '2026-10-21T08:34:09Z'
  support: supports
  summary: Alkaline is the intended environmental-condition quality facet. Reusing
    this cached authority does not certify a new release.
  snapshot_sha256: f3cba9fd93904b1ffd263729d99fc2b2f46958faa2fbf2fb1f9a9855c8678882
- evidence_id: ro
  kind: authority
  reference: Read-only RO snapshot
  locator: RO0002326 inherited domain/range; original08:04:46Z inspection, current
    hash verification
  accessed_at: '2026-10-21T08:04:46Z'
  support: partial
  summary: Contributes-to inherits material subject and process object via RO0002216,
    RO0002500 and RO0002595. Proton retention is explicitly a process; the separate
    antiporter protein is a compatible material subject. Native validation is not
    a domain reasoner.
  snapshot_sha256: 72a1497f02ad73de8740e3b1ff51b1a33c106418b2b931e107da6b4cbd1592cb
- evidence_id: graph-ledger
  kind: validation
  reference: Independent documentary node/edge inspection
  locator: All eleven nodes and ten edges, zero-based indices
  accessed_at: '2026-10-21T08:36:22Z'
  support: partial
  summary: Edge2 has the inherited material-domain mismatch. Node10 describes a sodium
    gradient but is typed BIOLOGICAL_PROCESS. Other optional labels, aggregate ion
    node, allowed GO function facet and provisional challenges/confers relations do
    not justify extra errors.
  snapshot_sha256: a6732f24748b026e2efa3421fa9d05cdf57bb9f47141ba43b0cc03b5e11fa0be
- evidence_id: owners
  kind: record_content
  reference: mappings/predicate_grounding.tsv; scripts/ground_causal_predicates.py;
    native enum and proposals
  locator: Wildcard contributes-to mapping; writer empty-ID contract; v2 challenges/v8
    confers
  accessed_at: '2026-10-21T08:36:22Z'
  support: partial
  summary: The wildcard mapping can recreate edge2 when its ID is empty, while existing
    IDs are skipped. The provisional predicates accommodate the current roles. Sodium-gradient
    correction belongs to the maintained record; the bounded ignored-inclusive owner
    search found no separate sodium-specific rule.
  snapshot_sha256: 7897efb4a93ef859823304c28207445a4c865687d9bc6b4dcc4acea0dedd0cbf
- evidence_id: policy
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml; docs/GROUNDING_POLICY.md
  locator: CausalNodeTypeEnum STATE and protein function facets; NONMECHANISTIC scope
  accessed_at: '2026-10-21T08:38:48Z'
  support: supports
  summary: STATE explicitly denotes a gradient or steady value, distinct from its
    establishment. A GO activity grounding may describe the function of a protein
    actor. Contextual scope does not require token protein accessions, datasets or
    one universal mechanism.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: provenance
  kind: search
  reference: Target history and bounded local provenance
  locator: All thirteen events; exact identifier/path/slug search across history,mappings,scripts,reviews/structured
  accessed_at: '2026-10-21T08:34:03Z'
  support: partial
  summary: Twelve AI-assisted events and the seed are explicit. The ignored-inclusive
    search found only other reviews listing this record as an input, with no explicit
    human acceptance link for this target revision. Private and remote acceptance
    remains unknown.
  snapshot_sha256: 02959e4ea7d847a7bb24d6b2c897618166875abc8c13e732c926a27af185c9ea
  search_scope: rg --no-ignore --hidden across history,mappings,scripts,reviews/structured;
    original command and all268 matching lines retained. Input mentions do not count
    as target reviews. Unsearched remote/private approvals remain unknown.
- evidence_id: status-rule
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md
  locator: Status/audit and human verification gate
  accessed_at: '2026-10-21T08:38:48Z'
  support: supports
  summary: REVIEWED requires human scientific acceptance; AI assistance and successful
    automated checks are distinct provenance.
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Official catalog originally07:36:12Z, hash-verified applicability assessment08:34:21Z
  accessed_at: '2026-10-21T08:34:21Z'
  support: context_only
  summary: Neither canonical taxon has a matching dataset. Historical Bacillus names
    were not used to substitute B. subtilis. No gene/module query or negative biological
    inference followed.
  snapshot_sha256: e4459bc9aa595278beef47b56ba077482f8203a8329312f3510894221d946a74
- evidence_id: runner
  kind: search
  reference: Reused structured-source runner discovery
  locator: Original bounded ignored-inclusive discovery08:17:15Z
  accessed_at: '2026-10-21T08:17:15Z'
  support: context_only
  summary: No usable runner was found in the originally declared PATH/project/install/B4
    bounds. This is reused evidence, not a new global filesystem-absence claim; the
    official catalog was the fallback.
  snapshot_sha256: 39b52930f52e898f85ac3bbb88f11ac674a355967b5704e2b62f0bda259d404f
  search_scope: Exact original search roots/command are retained in runner-discovery.json;
    ignored files were included, unsearched directories remain unknown.
- evidence_id: definition-source
  kind: primary_source
  reference: https://doi.org/10.1016/j.bbamem.2005.09.010
  locator: Complete indexed abstract; definition and edges0/2
  accessed_at: '2026-10-21T08:33:34Z'
  support: partial
  summary: The abstract supports the alkali-tolerant versus extremely alkaliphilic
    distinction and proton-capture/retention context; all three associated snippet
    occurrences are exact. It does not independently establish the precise neutral-optimum
    clause available in METPO. Full body access failed, so that clause is not declared
    disproven.
  snapshot_sha256: aaeca721aa72bd6bf7652b6c9540c4249317490bac744a2ccf90c7ba2b1f2027
- evidence_id: halodurans
  kind: primary_source
  reference: https://oup.silverchair-cdn.com/article-minimal/2376264
  locator: PMID11058132; Introduction paragraphs1–2 and Results/Discussion General
    features first paragraph; browser by08:35:40Z, downloaded article08:36:09Z
  accessed_at: '2026-10-21T08:36:09Z'
  support: partial
  summary: The cited C-125 genome paper places the organism in an alkaliphilic Bacillus
    context, with poor/no neutral-pH growth and strong alkaline growth. It does not
    establish neutral-optimum membership. This is a mismatch in the cited example
    evidence, not a claim that no strain or condition could meet the trait.
  snapshot_sha256: 9ec63b1769da9c25e9c8838a2698819c9d038509f85412e83dab45ebedb0600e
- evidence_id: pseudofirmus
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3228905/
  locator: PMID21951522; BioC abstract offset155, Introduction1439 and3620
  accessed_at: '2026-10-21T08:33:57Z'
  support: partial
  summary: The source identifies OF4 as an extreme facultative alkaliphile, in a class
    defined by alkaline growth optima. It supports alkaliphilic adaptation, not the
    record’s neutral-optimum example claim. Taxonomic identity is correct and physiological
    conditions can affect optima.
  snapshot_sha256: 8ad911c17e31457639d3de36b251ecdc3d8c8267718b6139251be325fbfa6fef
- evidence_id: homeostasis
  kind: primary_source
  reference: https://doi.org/10.1038/nrmicro2549
  locator: Publisher Abstract preview; BioC Conclusions offset44016, Introduction671
    and alkaline-homeostasis discussion10376; original retrievals07:55:43/07:56:36/07:57:33Z
  accessed_at: '2026-10-21T07:57:33Z'
  support: supports
  summary: The two short excerpts are exact. The source supports homeostasis during
    growth beyond the cytoplasmic pH range and its cell-wide character; generic contextual
    support is distinct from proof that either canonical organism meets the neutral-optimum
    definition.
  snapshot_sha256: 903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f
- evidence_id: antiporter-source
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7349511/
  locator: DOI10.3390/ijms21124566; Abstract sentence1 and Section3.2 (sec3dot2-ijms-21-04566)
    paragraph1
  accessed_at: '2026-10-21T08:33:36Z'
  support: supports
  summary: The snippet is exact and the source supports cation/proton antiporters
    in ion and pH homeostasis. Its generic protein-function context supports edge3
    without making an antiporter universally necessary for the trait.
  snapshot_sha256: 7a18d066a70c24ab6761a2e3a3e790c755f4d74e7a114b67ee1dcd0a0ce7550f
- evidence_id: electrogenic-source
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9408914/
  locator: DOI10.3390/ijms23169156; Section3 (sec3-ijms-23-09156) paragraph1
  accessed_at: '2026-10-21T08:33:36Z'
  support: supports
  summary: The source supports increased importance of electrogenic antiport at alkaline
    external pH. This is a general prokaryotic contextual claim, not evidence of one
    exclusive alkalotolerance route.
  snapshot_sha256: d70d2f55d4e7d550bfe09d7c3c278eabdbfc21ae5815cd54696093cc33efe3a5
- evidence_id: chapter
  kind: primary_source
  reference: https://link.springer.com/chapter/10.1007/978-4-431-55408-0_4
  locator: Publisher landing page and Crossref metadata; body unavailable
  accessed_at: '2026-10-21T08:33:58Z'
  support: context_only
  summary: The chapter citation resolves, but the particular surface-polymer homeostasis
    statement at edge6 was not verified in its own source body. Similar claims elsewhere
    are not silently substituted for this citation.
  snapshot_sha256: 802c04efb1752453f04ccdfc1f5d3d15c4e1b409787fcaecaf64d6c49458357b
- evidence_id: surface-hypothesis
  kind: primary_source
  reference: https://doi.org/10.1128/MMBR.63.4.735-750.1999
  locator: Actual PDF p739, Cell Walls → Acidic polymers; p736 condition-scope warning
  accessed_at: '2026-10-21T08:35:02Z'
  support: partial
  summary: The source proposes adsorption of sodium/hydronium and repulsion of hydroxide
    by acidic wall components in alkaliphilic Bacillus. It qualifies both that explanation
    and consequent growth assistance as possible. Edges7–8 omit those uncertainty
    and taxon-context bounds. The chemistry is not declared false.
  snapshot_sha256: fdf11ffdb50d7ce72faad4913b474361537f59e6e014ddffc05bfe9927fa8fb6
- evidence_id: sodium-source
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/s11244-024-01919-7
  locator: Actual full HTML section3.3; separately inspected linked correction
  accessed_at: '2026-10-21T08:33:58Z'
  support: supports
  summary: The reviewed source explicitly discusses sodium motive force in intracellular
    pH control. Its linked correction concerns acknowledgement/funding text, not this
    scientific statement. This establishes contextual source support, not the correctness
    of the graph node’s process type. Its alkaliphile context does not independently
    establish the neutral-optimum conjunction.
  snapshot_sha256: 09ae2a2fdd56dacc31267861694eedca4e04eda8e534844dccdbf8cf10abbdea
- evidence_id: bibliography
  kind: database
  reference: Primary-source identity and claim ledger
  locator: Nine references, ten edges and all six snippet occurrences
  accessed_at: '2026-10-21T08:37:28Z'
  support: partial
  summary: All references resolve and all six snippets are exact. Twenty-eight new
    acquisition attempts and twenty-two hashed responses retain failures, API-help
    and browser challenges separately from article text. Three Krulwich reuses retain
    original timestamps/hashes. Definition-source and chapter body limitations remain
    explicit.
  snapshot_sha256: 095687972c2730458cf48b78a75e5e20f5096cf22ab92ab2e710f0b05e8d0c66
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, definition, synonym and hierarchy'
  outcome: supported
  target_ids:
  - METPO:1003009
  summary: Active METPO identity, exact synonym and broader pH-growth parent match
    the intended neutral-optimum alkaline-tolerance class. The literature abstract
    supports its broader context; the precise neutral-optimum clause is directly verified
    in METPO.
  evidence_ids:
  - identity
  - definition-source
  - record
- assessment_id: model
  area: representation
  topic: 'Native checklist: category and NONMECHANISTIC context'
  outcome: supported
  target_ids:
  - METPO:1003009
  summary: ENVIRONMENT/CLASS and contextual scope are appropriate. The mechanism wording
    in the title does not by itself require scope promotion, protein examples or a
    reconstructed universal pathway.
  evidence_ids:
  - record
  - policy
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: canonical organism membership versus taxonomy'
  outcome: concern
  target_ids:
  - METPO:1003009
  summary: Both taxon IDs resolve correctly, but the cited alkaliphile papers do not
    establish the neutral-optimum membership required here. The finding is scoped
    to these sources and examples, not every possible strain or growth condition.
  evidence_ids:
  - current-identifiers
  - halodurans
  - pseudofirmus
  - identity
- assessment_id: grounding
  area: grounding
  topic: 'Native checklist: all current external node identifiers'
  outcome: supported
  target_ids:
  - METPO:1003009
  summary: GO activity and pH-process terms, alkaline quality, hydroxide and METPO
    identity fit the documented exact/close-match facets. Historical retracted identifiers
    are not present errors.
  evidence_ids:
  - current-identifiers
  - go-reuse
  - pato
  - graph-ledger
  - policy
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all eleven nodes and ten edges'
  outcome: concern
  target_ids:
  - METPO:1003009
  summary: Edge2 uses a material-subject relation for proton retention as a process.
    Node10 denotes a gradient but is typed as a process. The protein actor on edge3,
    provisional challenges/confers and optional ungrounded predicates introduce no
    additional confirmed typing defects.
  evidence_ids:
  - ro
  - graph-ledger
  - owners
  - policy
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: all ten edge claims and six snippets'
  outcome: concern
  target_ids:
  - METPO:1003009
  summary: All six snippets are verified. General homeostasis and antiport context
    is supported; edges7–8 overstate a taxon-bounded source hypothesis. Edge6 remains
    unverified at its own inaccessible chapter body.
  evidence_ids:
  - definition-source
  - homeostasis
  - antiporter-source
  - electrogenic-source
  - surface-hypothesis
  - chapter
  - sodium-source
  - bibliography
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: required fields and optional evidence surfaces'
  outcome: supported
  target_ids:
  - METPO:1003009
  summary: The record has required identity, definition and evidence surfaces, with
    all graph endpoints present. Optional datasets, protein instances and external
    IDs are not compulsory additions to this contextual graph.
  evidence_ids:
  - record
  - shape
  - policy
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: canonical-taxon structured-source applicability'
  outcome: supported
  target_ids:
  - METPO:1003009
  summary: Neither canonical organism matches the inspected catalog, and no neighboring
    Bacillus species was substituted. Missing coverage is not negative biological
    evidence.
  evidence_ids:
  - expression
  - runner
- assessment_id: provenance
  area: provenance
  topic: 'Native checklist: AI history, human acceptance and maintained owners'
  outcome: concern
  target_ids:
  - METPO:1003009
  summary: AI involvement is explicit. The bounded local search lacks an acceptance
    link identifying this revision; mapping/writer recurrence is distinguished from
    existing record repair.
  evidence_ids:
  - provenance
  - status-rule
  - owners
  - shape
findings:
- finding_id: canonical-example-scope
  issue_key: alkalotolerant-canonical-example-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Cited examples do not establish neutral-optimum alkalotolerance
  description: The canonical examples cite studies of alkaliphilic C-125 and extreme
    facultative alkaliphile OF4. Their taxon labels are correct, but the papers do
    not establish the neutral growth optimum required by this record. High-pH growth
    and facultative growth near neutrality are not equivalent to a neutral optimum.
    Do not infer that every strain or condition of these species is categorically
    excluded.
  target_ids:
  - METPO:1003009
  field_paths:
  - canonical_examples[0]
  - canonical_examples[1]
  evidence_ids:
  - identity
  - halodurans
  - pseudofirmus
  - current-identifiers
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkalotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: contributes-to-domain
  issue_key: alkalotolerant-contributes-to-domain
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Proton-retention process is assigned a material-subject relation
  description: Edge2 uses RO0002326 contributes-to with the explicitly process-typed
    proton-retention subject. Its inherited domain is material entity. The process
    object fits, and the separate protein-to-process edge3 is compatible under native
    functional-facet policy. Native shape validation passing does not remove this
    semantic conflict.
  target_ids:
  - METPO:1003009
  field_paths:
  - causal_graphs[0].edges[2]
  evidence_ids:
  - ro
  - graph-ledger
  - owners
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkalotolerant.yaml
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
- finding_id: surface-hypothesis-scope
  issue_key: alkalotolerant-surface-hypothesis-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Surface-chemistry edges remove the source’s uncertainty and taxon scope
  description: Edges7–8 state adsorption and repulsion categorically. The cited review
    presents them as a proposed explanation in alkaliphilic Bacillus, with possible
    growth assistance. Preserve those bounds rather than treating them as established
    generic mechanisms of neutral-optimum alkalotolerance. This is not a claim that
    the chemistry is false; the separate inaccessible chapter edge6 is not included
    as a confirmed error.
  target_ids:
  - METPO:1003009
  field_paths:
  - causal_graphs[0].edges[7]
  - causal_graphs[0].edges[8]
  evidence_ids:
  - surface-hypothesis
  - record
  - identity
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkalotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: sodium-gradient-type
  issue_key: alkalotolerant-sodium-gradient-type
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Sodium gradient is typed as a biological process
  description: Node10’s description explicitly names a transmembrane sodium gradient.
    The native STATE enum distinguishes such a gradient from the process that establishes
    it. The correct description and unconstrained supports edge remain understandable,
    making this a bounded local type-precision issue.
  target_ids:
  - METPO:1003009
  field_paths:
  - causal_graphs[0].nodes[10].node_type
  evidence_ids:
  - record
  - policy
  - graph-ledger
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkalotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: alkalotolerant-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human scientific acceptance is not linked locally
  description: The twelve AI-assisted events and original seed disclose provenance,
    but the bounded inspected local record/history/review surfaces do not link human
    acceptance to this revision. Private or remote acceptance remains unknown.
  target_ids:
  - METPO:1003009
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - status-rule
  - shape
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkalotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: repair-examples
  description: In separately authorized curation, replace or re-scope the two examples
    using direct evidence that meets the neutral-optimum definition; retain correct
    taxonomy and source-strain distinctions.
  finding_ids:
  - canonical-example-scope
  target_ids:
  - METPO:1003009
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkalotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Each retained canonical example has source-backed alkaline tolerance and a neutral
    growth optimum in its stated conditions.
  - Do not substitute high-pH growth or facultative neutral-pH growth for an optimum
    measurement.
  - Run focused record/taxon validation, preserve native provenance and regenerate
    affected products after authorized edits.
- action_id: repair-relation
  description: Reconcile edge2 with its actual process subject and review the wildcard
    mapping to prevent recurrence.
  finding_ids:
  - contributes-to-domain
  target_ids:
  - METPO:1003009
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkalotolerant.yaml
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
  - Verify the chosen relation’s inherited endpoint roles and intended meaning.
  - Preserve the compatible material-protein edge3 and allowed GO function facet.
  - Use the maintained ground-predicates dry run to inspect recurrence; its empty-ID
    behavior cannot correct existing nonempty IDs.
  - After authorized curation, run strict validation, graph checks and just qc with
    required history and derived products.
- action_id: qualify-surface-evidence
  description: Preserve the proposed nature and alkaliphilic Bacillus context of the
    adsorption/repulsion explanation, or supply direct evidence for a stronger claim
    at the intended scope.
  finding_ids:
  - surface-hypothesis-scope
  target_ids:
  - METPO:1003009
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkalotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Edges7–8 retain the nearest source’s uncertainty and organism context.
  - Do not describe the underlying chemistry as disproven.
  - Keep edge6’s unavailable chapter evidence separate; verify its actual body before
    claiming direct support.
  - Run focused validation after any authorized change.
- action_id: repair-state-type
  description: Align the sodium-motive-force node with the native gradient-versus-process
    distinction while retaining the documented contextual meaning.
  finding_ids:
  - sodium-gradient-type
  target_ids:
  - METPO:1003009
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkalotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Node10’s type agrees with its gradient description, or any revised process meaning
    has its own support.
  - Do not duplicate the same issue as an extra unconstrained supports-edge error.
  - Run focused strict and graph validation after authorized curation.
- action_id: link-acceptance
  description: Locate and link existing human scientific acceptance or obtain it through
    the established process; preserve AI history and reassess status if acceptance
    remains unavailable.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1003009
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkalotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies the record revision and scientific scope.
  - Automated checks and AI history are not presented as human approval.
limitations:
- The definition’s exact neutral-optimum clause is verified in METPO but not in the
  accessible abstract of its nearest literature source; body-access failure does not
  disprove it.
- Edge6’s chapter citation resolves but its body was unavailable. Other sources are
  not silently substituted for nearest-citation verification.
- The examples finding concerns the cited strains and source scopes; growth optima
  can depend on conditions, so species-wide impossibility is not inferred.
- The surface-chemistry finding concerns the source’s uncertainty and alkaliphilic
  Bacillus context, not a claim that adsorption or repulsion is false.
- Broad homeostasis, antiport and sodium-motive-force context does not by itself establish
  sufficiency for the full neutral-optimum trait definition.
- The sodium-motive-force source is a broad narrative review in alkaliphile context;
  its linked correction changes funding/acknowledgement text only.
- Krulwich primary text, RO, GO and expression-catalog reuse preserve original timestamps/hashes.
  A preview stored with a PDF suffix is identified as HTML; API-help/challenge responses
  are excluded.
- No matching canonical-taxon expression dataset was found in the inspected catalog.
  No neighboring organism was substituted and no negative biological inference follows.
- Human acceptance outside the bounded local search remains unknown.
- The existing research-provider report was inspected only as provenance and leads;
  no provider recommendation was automatically accepted and no paid call was made.
- No scientific record, schema, mapping, writer, status, history or generated page
  was changed.
notes:
- All field indices are zero-based.
- The full record was read before native capture08:33:02–03Z, which retained52input
  hashes.
- The existing contextual graph scope does not require token protein examples, mandatory
  external IDs on every node/predicate, or a universal mechanism.
tags:
- record-review
- alkalotolerant
- environment
- needs-curation
```
