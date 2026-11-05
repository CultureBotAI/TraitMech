# Scientific review of biofilm formation (traitmech:000053)

- Review: 20261019T233732Z-biofilm-formation
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-19T23:30:53Z
- Finished UTC: 2026-10-19T23:37:32Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One complete record assessed, including all 14 nodes and 13 edges. Biological identity and scoped examples are supported. Two major findings concern a misattributed source and four incompatible RO predicate uses; three minor findings concern quotation provenance, discussion certainty and historical tissue attribution. A separate informational finding retains known identifier reconciliation work.

## Scope And Provenance

Entire selected record; local ontology, proposal, writers and history are contextual inputs, not additional review targets.

Selection: Third previously uncovered record in lexicographic path order, after animal pathogen and bacterial cannibalism. Initial validated inventory covered 57 of 1130 corpus records; two new one-record bundles have since passed native checks.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f25e2af0b38a8303b13f627a9a5c33b36af4b3d2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000053 | data/traits/ecology/biofilm_formation.yaml | maintained | biofilm formation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus structural graph audit | passed | True | traitmech:000053 | Full corpus: 74 baselined findings, zero new/blocking findings, 130 mechanistic graphs connected. This target graph is connected; connectivity is not evidence of correct causal or ontology semantics. |
| Full-corpus evidence snippet audit | passed | True | traitmech:000053 | Full corpus: 2419 baselined findings, zero new/blocking findings. Target quotations were separately checked with the focused recipe and manual source inspection. |
| Full-corpus pathway context link validation | passed | True | traitmech:000053 | Full corpus: 19 links checked against pinned PathwayMech; this target asserts no pathway link. |
| Full-corpus repository history link validation | passed | True | traitmech:000053 | Full corpus: 1276 history records, zero invalid links. Target creation event was also inspected; link validity is not human sign-off. |
| Initial product identifier-label validation | failed | False | traitmech:000053 | Initial full-product check failed with exit 2 during PATO/RO downloads, with 36 adapter errors and 123 no-adapter skips. Superseded by successful retry. |
| Product validation with isolated local cache | failed | False | traitmech:000053 | Intermediate isolated-cache attempt failed with exit 2, 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000053 | Full configured product validation passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. This is not focused verification of every target identifier. |
| Focused LinkML validation | passed | True | traitmech:000053 | Selected record validates; shape validation does not adjudicate science. |
| Focused strict closed-schema validation | passed | True | traitmech:000053 | One file scanned; zero error rows. |
| Focused source snippet verification | passed | True | traitmech:000053 | Four snippets across four references returned NOT_IN_ABSTRACT, which is inconclusive for full-text quotations. Manual full-text verification resolves their provenance below. |
| Structured expression adapter availability | unavailable | False | traitmech:000053 | No runner on PATH or at configured sibling culturebotai-claw location; public authoritative identifiers and primary source text supplied the fallback. No negative biological inference follows. |

## Scientific And Domain Assessments

### Native checklist: identity, polarity and term kind

identity: supported. Targets: traitmech:000053.

The local CLASS denotes a positive surface-associated biofilm-forming phenotype, distinct from an organism or the separately modeled process. RELATED_SYNONYM is appropriately nonexact. Known active-METPO overlap requires planned reconciliation rather than automatic replacement.

### Native checklist: definition and source scope

evidence: supported. Targets: traitmech:000053.

The noncircular definition is supported jointly by Flemming matrix/lifestyle context and Bohning surface-attachment text. Its surface-attached operational scope is explicit; not every broader aggregate usage is equated with it.

### Native checklist: broader parent and category

consistency: supported. Targets: traitmech:000053.

The phenotype parent is broader; ECOLOGY and CLASS fit the lifestyle capability. The process node is kept distinct from the trait node and proposed confers has the corresponding direction.

### Native checklist: taxon and protein examples

grounding: supported. Targets: traitmech:000053.

Species and PAO1 examples have appropriately bounded source support. Taxon, gene, UniProt status and proteome pairing resolve. Family-level InterPro and taxon-specific protein example remain separate.

### Native checklist: citation identity, quotations and evidence tier

evidence: concern. Targets: traitmech:000053.

A 2019 commentary is misattributed and overstates support. WspR function is supported but its quotation is paraphrased; ten of thirteen edge entries and both top-level evidence entries lack snippets. Other inspected full-text quotations match apart from two sentence-initial capitalization changes.

### Native checklist: node identity, edge semantics and scoped evidence

graph: concern. Targets: traitmech:000053.

All nodes and edges were assessed. Graph connectivity is satisfactory, but four RO relations conflict with endpoint semantics. Source support for a biological association does not fix those ontology mismatches. Matrix/fiber CHEMICAL typing is broad; compositional versus assembled-matrix distinction could be clearer, without a demonstrated closed-schema error.

Zero-based edge ledger: 0 matrix context supported, but RO enables is stronger than passive scaffolding; 1 bibliography/claim-support defect; 2 and 3 explicit Bohning review support; 4 Wang contextual support with RO mismatch; 5 primary WspR function supported, snippet not verbatim; 6 contextual prerequisite supported with RO mismatch; 7 context-dependent review support, no unconditional concentration claim; 8 and 9 explicit review-level eDNA assertions; 10 review-level QS support with RO mismatch; 11 explicit attachment-process support; 12 dispersal/loss-of-sessility interpretation supported with RO mismatch. The PAO1 scope note applies only to its branch, not all others.

### Native checklist: discussions, logical certainty and datasets

consistency: concern. Targets: traitmech:000053.

The discussion anchors resolve and topic is relevant, but its yes/no outcome interpretations claim more causal certainty than follows. Historical scan references are correctly disclaimed as evidence, with one incorrect tissue description. No dataset is asserted.

### Native checklist: required versus optional representation

completeness: supported. Targets: traitmech:000053.

Examples, graph and evidence are present. Optional datasets or extra synonyms are not required; omitted mechanism steps are not to be invented. Identified corrections concern retained claims and provenance.

### Native checklist: scientific status and audit

provenance: unknown. Targets: traitmech:000053.

Focused schema/strict checks and corpus gates pass within their scopes. REVIEWED promotion is attributed to an LLM-assisted agent; this review cannot establish historical human sign-off. Known identifier overlap remains recorded in release-review decisions.

## Findings

### global-citation: 2019 citation identity and claimed support are incorrect

major / open / confirmed; issue key: biofilm-formation-global-citation.

The exact DOI names Bar-On and Milo, not Flemming and Wuertz; its preview questions quantitative predominance. The target attributes the source to different authors and invokes established dominant lifestyle to support a specific process-to-trait assertion. Resolve the bibliography and nearest-claim support without automatic DOI substitution.

### ro-endpoint-semantics: Four RO groundings conflict with their endpoint types

major / open / confirmed; issue key: biofilm-formation-ro-endpoint-semantics.

Edges 4, 10 and 12 use process-regulation relations with chemical subjects and/or a STATE object. Edge 6 uses enables with a STATE subject, although the relation requires a material actor executing the process. Scientific contextual support and permissive mapping gates do not establish compatible ontology meaning.

### quotation-provenance: Edge quotations do not consistently expose source support

minor / open / confirmed; issue key: biofilm-formation-quotation-provenance.

Edge 5 presents a source-consistent paraphrase as a verbatim snippet; it was not found in the complete acquired publisher XML after whitespace/case normalization. Ten of thirteen edges and both top-level evidence entries have no snippets. Other full-text snippets are exact apart from initial case. Missing quotations are not by themselves proof the scientific claim is false.

### discussion-certainty: Discussion outcome interpretations overstate causal certainty

minor / open / confirmed; issue key: biofilm-formation-discussion-certainty.

Excluding one nominated intermediate cannot prove that no other intermediate exists or that the drawn direct edge is correct. Conversely, an absent outcome alone does not establish a uniquely necessary intermediate. The rationale also states intrinsic refractoriness without attached support, while its cited review already discusses an intermediate in a bounded model.

### scan-tissue-provenance: Historical scan note misidentifies the tissue context

minor / open / confirmed; issue key: biofilm-formation-scan-tissue-provenance.

PMID:42039744 and the retained quote concern lung/airway mucosal IgA homeostasis, not gut mucosa. The citation is already disclaimed as support for the current question, so this is a bounded provenance defect.

### known-metpo-reconciliation: Active METPO overlap is already recognized but not reconciled

informational / deferred / confirmed; issue key: biofilm-formation-known-metpo-reconciliation.

The captured ontology has active METPO:1007077 and the release-review table explicitly associates it with this local record while deferring primary-identifier migration. v5 still reserves a different proposed METPO ID. This is acknowledged follow-up, not a finding that the record denotes the wrong phenotype.

Disposition: Existing release-review inputs deliberately retain the local primary identifier; coordinated migration requires separate exact-scope reconciliation and is outside this read-only review.

## Recommended Actions And Acceptance Checks

### repair-global-citation

Reassess source identity and exact support for the retained ecological and process-to-trait statements.

- Inspect authoritative identity and actual source text; do not substitute a plausible DOI without review.
- Separate prevalence context from the ontology realization assertion.
- After authorized curation, run focused validate, validate-strict, verify-snippets and applicable native qc gates.

### reassess-ro-relations

Review the retained relation meanings and typed endpoints against exact ontology definitions; do not mechanically replace labels or infer new mechanisms.

- Demonstrate domain/range-compatible meanings for each retained grounded relation, including inherited constraints.
- Assess whether the maintained mapping gate would regenerate the same mismatch.
- Use guarded curation and history for any authorized change; run strict, audit-graphs, applicable grounding checks and qc.

### repair-quotation-provenance

Use short source-checked contiguous quotations for retained claims and put interpretation in notes.

- Replace or relabel the WspR paraphrase after inspecting the source; retain its supported functional scope.
- Fill provenance gaps only where actual source text supports the retained claim.
- Run focused verify-snippets and audit-snippets; interpret abstract-only nonmatches explicitly.

### bound-discussion-inference

Qualify the discussion conclusions and literature scope so the stated interpretations follow from the available evidence.

- Remove claims of directness or unique necessity that do not follow from the stated contrast.
- Reconcile the maintained discussion writer with any authorized text correction.
- Do not introduce a protocol, replacement mechanism, therapeutic efficacy claim or intervention recommendation; validate the revised record.

### correct-scan-context

Correct the tissue description in the preserved scan-provenance note and corresponding maintained writer.

- Check against the inspected PMID abstract and retain the original citation/quote as historical provenance.
- Preserve the disclaimer that these references do not support the current discussion.
- Run focused strict validation after any authorized edit.

### reconcile-known-metpo-match

When identifier migration is separately authorized, settle exact scope and reconcile the known active match, local references and legacy proposal consistently.

- Verify exact scope/equivalence against the chosen METPO release; retain the release-review decision provenance.
- Apply the maintained identifier policy and check all internal references and proposal ownership before any migration.
- Run native identifier/reference, strict, history and qc gates after authorized changes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; command metadata audit-graphs.json | context_only | Full corpus: 74 baselined findings, zero new/blocking findings, 130 mechanistic graphs connected. This target graph is connected; connectivity is not evidence of correct causal or ontology semantics. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; command metadata audit-snippets.json | context_only | Full corpus: 2419 baselined findings, zero new/blocking findings. Target quotations were separately checked with the focused recipe and manual source inspection. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; command metadata check-pathway-links.json | context_only | Full corpus: 19 links checked against pinned PathwayMech; this target asserts no pathway link. |
| check-validate-history | /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; command metadata validate-history.json | context_only | Full corpus: 1276 history records, zero invalid links. Target creation event was also inspected; link validity is not human sign-off. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; command metadata validate-products.json | context_only | Initial full-product check failed with exit 2 during PATO/RO downloads, with 36 adapter errors and 123 no-adapter skips. Superseded by successful retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; command metadata validate-products-retry-local.json | context_only | Intermediate isolated-cache attempt failed with exit 2, 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; command metadata validate-products-retry-network.json | context_only | Full configured product validation passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. This is not focused verification of every target identifier. |
| check-biofilm-validate | /private/tmp/traitmech-record-sweep.FU79Gr/biofilm-validate.log; Executed 2026-10-19T23:32:40Z through 2026-10-19T23:32:42Z | context_only | Selected record validates; shape validation does not adjudicate science. |
| check-biofilm-strict | /private/tmp/traitmech-record-sweep.FU79Gr/biofilm-strict.log; Executed 2026-10-19T23:32:40Z through 2026-10-19T23:32:42Z | context_only | One file scanned; zero error rows. |
| check-biofilm-snippets-network | /private/tmp/traitmech-record-sweep.FU79Gr/biofilm-snippets-network.log; Executed 2026-10-19T23:32:43Z through 2026-10-19T23:32:50Z | context_only | Four snippets across four references returned NOT_IN_ABSTRACT, which is inconclusive for full-text quotations. Manual full-text verification resolves their provenance below. |
| record | data/traits/ecology/biofilm_formation.yaml; Entire record, all 14 nodes, 13 edges, examples, history and discussion | partial | Correct biological concept with explicit WspR scope; sources, predicates and some provenance require curation. |
| metpo-identity | data/raw/metpo.owl; METPO:1000059, active METPO:1007077, deprecated METPO:1000036; v5 reservation and release-review decision row | supports | Unique local identity and phenotype parent resolve. Active surface-attached biofilm capability METPO:1007077 overlaps this record; reports/metpo_2026_06_12_active_review.tsv explicitly records DUPLICATE_NO_NEW_PRIMARY and defers migration. v5 retains proposed METPO:1007652, absent as an OWL subject in the captured snapshot. Searches included ignored/hidden corpus files. |
| owners-history | scripts/curate_knowledge_gaps.py; Target history, connector writer, guarded writer, related infrastructure histories and DO_NOT_WORK | partial | Scientific edits belong to the target; discussion content also occurs in the maintained knowledge-gap writer and connector content in scripts/connect_mechanistic_graphs_183.py. Promotion event is agent-attributed. Ignored-inclusive relevant history and exclusion searches do not establish human sign-off; target is not an exclusion match. |
| flemming | https://pubmed.ncbi.nlm.nih.gov/27510863/; DOI:10.1038/nrmicro.2016.94; complete abstract and metadata | partial | Review supports EPS-enclosed bacterial communities, matrix structural/function importance and ecological lifestyle. It is review context rather than a new primary experiment; surface-attachment wording is additionally supported by the matrix review. |
| global-comment | https://www.nature.com/articles/s41579-019-0162-0; Publisher preview; PMID:30792541 and Europe PMC identity | refutes | The DOI denotes Bar-On and Milo, Towards a quantitative view of the global ubiquity of biofilms, a News &amp; Views commentary. It is not Flemming and Wuertz and explicitly leaves a microbial-majority claim awaiting quantification. It does not establish the particular process-to-trait relation. |
| matrix-review | https://pmc.ncbi.nlm.nih.gov/articles/PMC10903470/; DOI:10.1042/BCJ20210301; Introduction s1 and eDNA section s1c | supports | Bohning et al. review explicitly describes attachment initiation, defining ECM, eDNA structural roles and fiber nucleation. Edge 11 quotation is contiguous apart from sentence-initial capitalization. These are review-level bacterial assertions, not proof for every taxon. |
| water-review | https://mdpi-res.com/d_attachment/water/water-17-01944/article_deploy/water-17-01944.pdf; DOI:10.3390/w17131944; Introduction page 2, section 2.2 page 4 | supports | Wang et al. discuss c-di-GMP, EPS, motility and transition to sessile growth in a wastewater-treatment/bacterial review context. Supports the biological context of edges 4 and 6, without establishing their selected RO semantics or universality. |
| wsp-function | https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0060067; Publisher XML: Abstract, author summary, relevant Results; entire XML text searched for quoted span | partial | Primary study supports WspR diguanylate-cyclase function. The edge 5 snippet is not a contiguous span anywhere in inspected XML, including body/captions/references after whitespace and case normalization; supplements were not searched. The scientific claim is supported but the snippet is paraphrased. |
| wsp-example | https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1004480; Publisher XML Results paragraph comparing PA14 and PAO1, accompanying Figure 5 | supports | Primary PAO1 study supports the scoped WspR surface-colonization example. Its protein-example snippet is exact after whitespace normalization. It does not establish the other branches for PAO1; the record explicitly recognizes that boundary. |
| no-review | https://pmc.ncbi.nlm.nih.gov/articles/PMC11591520/; DOI:10.3390/antibiotics13111047; section 4.2 | partial | Review supports context-dependent NO-associated dispersal and release from matrix; it discusses an intermediate in a named bacterial model and contains inconsistent concentration-direction prose. Edge 12 quotation is contiguous except sentence-initial capitalization. It does not establish a direct molecular edge, universal response or the discussion categorical causal conclusions. |
| qs-review | https://mdpi-res.com/d_attachment/bacteria/bacteria-03-00008/article_deploy/bacteria-03-00008.pdf; DOI:10.3390/bacteria3030008; abstract/introduction pages 118-119 and section 6 | supports | Erkihun et al. review describes AHL/AIP/AI-2 signaling categories and biofilm roles. It supports scoped regulatory association rather than every signal in every organism or the chosen RO domain semantics. |
| species-example | https://pubmed.ncbi.nlm.nih.gov/35335624/; Complete abstract; DOI:10.3390/pathogens11030300, PMC8950561 | supports | Tuon et al. review supports P. aeruginosa as a biofilm-forming model species. Its pathogenic context does not establish every ecological mechanism for all isolates. |
| live-identifiers | https://rest.uniprot.org/uniprotkb/Q9HXT9.json; Entry identity/audit, organism, gene, InterPro and proteome cross-references; live taxonomy/proteome endpoints | supports | Q9HXT9 is active unreviewed wspR/PA3702 in PAO1 taxon 208964, reference proteome UP000002438. Species 287 and child strain 208964 resolve. Current entry version 153 and sequence 1 do not invalidate an explicitly dated historical version-152 observation. |
| interpro-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050469/; Family name/type and UniProt Q9HXT9 explicit family cross-reference | supports | IPR050469 is a broader bacterial Dgc-like diguanylate-cyclase family and Q9HXT9 belongs to it. The schema permits family grounding separate from taxon-paired instances; this is compatible as a family anchor, not WspR-specific equivalence or primary experimental proof. InterPro description is marked LLM-assisted. |
| ontology-nodes | https://purl.obolibrary.org/obo/GO_0042710; Hashed local GO/CHEBI caches: GO:0042710, GO:0031012 and CHEBI:16480 label/definition | supports | Process, extracellular matrix and nitric oxide node identities match. GO annotation-exclusion subset is not deprecation. Cached release freshness is unknown. |
| ro-semantics | https://purl.obolibrary.org/obo/RO_0002211; Cached rdfs:domain/range/definitions/subproperties for RO:0002211, 0002212, 0002213, 0002327 and ancestors | refutes | Regulates explicitly has process domain/range, inherited by positive/negative regulation. Enables requires a material actor executing a process through its parent relations. Edges 4, 6, 10 and 12 use chemical/state endpoints inconsistently. Wildcard mapping gates do not override ontology semantics; this is manual interpretation, not a reasoner result. |
| confers-proposal | proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv; METPO:2007700 row, SSSOM and mappings/predicate_grounding.tsv | supports | Locally proposed confers describes process realization of a trait and matches this endpoint direction. Its identifier remains a documented placeholder, not a verified minted upstream predicate. |
| scan-provenance | https://pubmed.ncbi.nlm.nih.gov/42039744/; Complete Europe PMC abstract and three other retained scan abstracts: PMID:41245847, 41661098, 42125129 | partial | All four identifiers resolve and preserved quotations match their abstracts. The first concerns lung/airway mucosal IgA homeostasis, while the record says gut mucosa. The other scan statements are explicitly historical and do not support the NO-specific discussion. |

## Limits And Additional Notes

- Flemming 2016 was assessed from its complete abstract and metadata, and Bar-On/Milo 2019 from publisher preview plus metadata; subscription full texts were not inspected.
- Other literature was inspected through publisher or Europe PMC XML and publisher PDFs. No supplements or actual figure images were evaluated, and no experimental or clinical recommendation is made.
- Most broad graph branches rely on review articles, not independently reassessed primary experiments. The record appropriately bounds the PAO1 WspR exemplar; that example does not establish every other branch or a universal microbial mechanism.
- The NO review contains inconsistent concentration-direction descriptions. This review retains only context-dependent dispersal support and does not infer a concentration-response rule.
- The current UniProt entry is version 153, sequence version 1. The record explicitly preserves its 2026-08-25 retrieval and version 152; historical bytes were not retrieved, so that historical version is not certified or treated as an error.
- METPO identity/proposal conclusions use the captured repository release. GO/CHEBI/RO terms were read from hashed session-local caches; their release freshness was not established. No OWL reasoning run is claimed.
- The inspected curation event and target/infrastructure history attribute promotion to an LLM-assisted agent. Human sign-off was not traceable in that bounded, ignored-inclusive history search; this does not establish that approval never occurred.
- No structured-source runner was available on PATH or at the configured sibling CLAW location. Direct authoritative identifiers and source text were used instead; expression-module membership is not phenotype or mechanism proof.
- Full-corpus diagnostics are reused from the unchanged source base, with their actual results and times. Product validation retains 123 no-adapter skips.
- No trait, writer, proposal, history or generated page was changed. A completed review is not human scientific sign-off.
- Source capture expansions preserved all earlier hashes. Owner paths identify future curation inputs, not permission to run those writers.
- The pending active-METPO match is not evidence that the local record denotes the wrong biological trait; identifier reconciliation is already acknowledged by the release-review table.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233732Z-biofilm-formation
kind: record
repository: CultureBotAI/TraitMech
title: Scientific review of biofilm formation (traitmech:000053)
started_at: '2026-10-19T23:30:53Z'
finished_at: '2026-10-19T23:37:32Z'
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
summary: One complete record assessed, including all 14 nodes and 13 edges. Biological
  identity and scoped examples are supported. Two major findings concern a misattributed
  source and four incompatible RO predicate uses; three minor findings concern quotation
  provenance, discussion certainty and historical tissue attribution. A separate informational
  finding retains known identifier reconciliation work.
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
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/ecology/biofilm_formation.yaml
    sha256: 8936e72d19f99bb3f7bb7ad47037a421a1e94d2d1ee3528ee77edcf57c237964
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
  - path: history/infrastructure/canonical-examples/2026-08-19T183734Z-claude-code-44a170.yaml
    sha256: b6155e63f3c4719b794f7d71c65f9ccaa3e01030b0d5b676b33e4dd5a542cc62
    role: context
  - path: history/infrastructure/curate-knowledge-gaps/2026-08-17T214933Z-claude-code-9c4af0.yaml
    sha256: a58b53be777e58ac29eb1c1571feb2593633c83d158aff4b6c96b8a1b9214c0f
    role: context
  - path: history/records/biofilm_formation/2026-08-31T054807Z-codex-66f8c6.yaml
    sha256: 1bf8c5676241dd0c18f19c63144d49b1af8e7e95fe216d16d7c943d7f9cf1711
    role: context
  - path: mappings/predicate_grounding.tsv
    sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
    role: context
  - path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
    role: context
  - path: proposals/metpo_traitmech_v8/metpo_proposal_mappings.sssom.tsv
    sha256: b5870c3789b4bd51db844caf80dec3e795622c99c0a72d9953d655597d289959
    role: context
  - path: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
    role: context
  - path: proposals/metpo_traitmech_v8/proposal.md
    sha256: 119d51e7b7194890514a9e313505212bab92aeba607f7c1b8f9d9d2edeef67e7
    role: context
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: scripts/connect_mechanistic_graphs_183.py
    sha256: bc74ca1af0c611b4653f6e526a0e5f3e1647619005129eb0ebc48976c85d5b72
    role: context
  - path: scripts/curate_knowledge_gaps.py
    sha256: 9e0fb7e01a901d84189a28f1912a2552f28d2da8733c113589e4947359d48c73
    role: context
  - path: scripts/finalize_metpo_2026_06_12_review.py
    sha256: b850b386183b2d86647dada43f7f157059017dbb881f7e1fb2e220ae697d3bea
    role: context
  - path: scripts/migrate_enables_range_edges.py
    sha256: 3d0d1bddcaa76baef5833973e2e979e4fee1f834c67d1abcc69a8d866ecb8f32
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
- target_id: traitmech:000053
  path: data/traits/ecology/biofilm_formation.yaml
  label: biofilm formation
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: maintained TraitRecord; guarded curation required
scope:
  description: Entire selected record; local ontology, proposal, writers and history
    are contextual inputs, not additional review targets.
  selection: Third previously uncovered record in lexicographic path order, after
    animal pathogen and bacterial cannibalism. Initial validated inventory covered
    57 of 1130 corpus records; two new one-record bundles have since passed native
    checks.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000053
checks:
- check_id: audit-graphs
  name: Full-corpus structural graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000053
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-audit-graphs
  summary: 'Full corpus: 74 baselined findings, zero new/blocking findings, 130 mechanistic
    graphs connected. This target graph is connected; connectivity is not evidence
    of correct causal or ontology semantics.'
  scope_note: Reused actual full-corpus result at unchanged captured Git base; only
    new structured review files have been added since execution.
- check_id: audit-snippets
  name: Full-corpus evidence snippet audit
  status: passed
  required: true
  target_ids:
  - traitmech:000053
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-audit-snippets
  summary: 'Full corpus: 2419 baselined findings, zero new/blocking findings. Target
    quotations were separately checked with the focused recipe and manual source inspection.'
  scope_note: Reused actual full-corpus result at unchanged captured Git base; only
    new structured review files have been added since execution.
- check_id: check-pathway-links
  name: Full-corpus pathway context link validation
  status: passed
  required: true
  target_ids:
  - traitmech:000053
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-check-pathway-links
  summary: 'Full corpus: 19 links checked against pinned PathwayMech; this target
    asserts no pathway link.'
  scope_note: Reused actual full-corpus result at unchanged captured Git base; only
    new structured review files have been added since execution.
- check_id: validate-history
  name: Full-corpus repository history link validation
  status: passed
  required: true
  target_ids:
  - traitmech:000053
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  summary: 'Full corpus: 1276 history records, zero invalid links. Target creation
    event was also inspected; link validity is not human sign-off.'
  scope_note: Reused actual full-corpus result at unchanged captured Git base; only
    new structured review files have been added since execution.
- check_id: validate-products
  name: Initial product identifier-label validation
  status: failed
  required: false
  target_ids:
  - traitmech:000053
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  evidence_ids:
  - check-validate-products
  summary: Initial full-product check failed with exit 2 during PATO/RO downloads,
    with 36 adapter errors and 123 no-adapter skips. Superseded by successful retry.
  scope_note: Reused actual full-corpus result at unchanged captured Git base; only
    new structured review files have been added since execution.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - traitmech:000053
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  evidence_ids:
  - check-validate-products-retry-local
  summary: Intermediate isolated-cache attempt failed with exit 2, 36 adapter errors
    and 123 no-adapter skips. Superseded by successful network retry.
  scope_note: Reused actual full-corpus result at unchanged captured Git base; only
    new structured review files have been added since execution.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - traitmech:000053
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-products-retry-network
  summary: 'Full configured product validation passed: 361 canonical matches, two
    synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. This is not focused
    verification of every target identifier.'
  scope_note: Reused actual full-corpus result at unchanged captured Git base; only
    new structured review files have been added since execution.
- check_id: biofilm-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000053
  command: just validate data/traits/ecology/biofilm_formation.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-biofilm-validate
  summary: Selected record validates; shape validation does not adjudicate science.
- check_id: biofilm-strict
  name: Focused strict closed-schema validation
  status: passed
  required: true
  target_ids:
  - traitmech:000053
  command: just validate-strict data/traits/ecology/biofilm_formation.yaml --out /private/tmp/traitmech-record-sweep.FU79Gr/biofilm-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-biofilm-strict
  summary: One file scanned; zero error rows.
- check_id: biofilm-snippets-network
  name: Focused source snippet verification
  status: passed
  required: true
  target_ids:
  - traitmech:000053
  command: just verify-snippets --record data/traits/ecology/biofilm_formation.yaml
    --out /private/tmp/traitmech-record-sweep.FU79Gr/biofilm-snippets-network.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-biofilm-snippets-network
  summary: Four snippets across four references returned NOT_IN_ABSTRACT, which is
    inconclusive for full-text quotations. Manual full-text verification resolves
    their provenance below.
- check_id: structured-source-runner
  name: Structured expression adapter availability
  status: unavailable
  required: false
  target_ids:
  - traitmech:000053
  summary: No runner on PATH or at configured sibling culturebotai-claw location;
    public authoritative identifiers and primary source text supplied the fallback.
    No negative biological inference follows.
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; command metadata
    audit-graphs.json
  accessed_at: '2026-10-19T23:32:49Z'
  support: context_only
  summary: 'Full corpus: 74 baselined findings, zero new/blocking findings, 130 mechanistic
    graphs connected. This target graph is connected; connectivity is not evidence
    of correct causal or ontology semantics.'
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; command metadata
    audit-snippets.json
  accessed_at: '2026-10-19T23:32:49Z'
  support: context_only
  summary: 'Full corpus: 2419 baselined findings, zero new/blocking findings. Target
    quotations were separately checked with the focused recipe and manual source inspection.'
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; command metadata
    check-pathway-links.json
  accessed_at: '2026-10-19T23:32:49Z'
  support: context_only
  summary: 'Full corpus: 19 links checked against pinned PathwayMech; this target
    asserts no pathway link.'
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; command metadata
    validate-history.json
  accessed_at: '2026-10-19T23:32:49Z'
  support: context_only
  summary: 'Full corpus: 1276 history records, zero invalid links. Target creation
    event was also inspected; link validity is not human sign-off.'
  snapshot_sha256: 1fc48f1203fbfcd27b1243e4e147afb367aebfc592b496b352201058c6ee85d2
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; command metadata
    validate-products.json
  accessed_at: '2026-10-19T23:32:49Z'
  support: context_only
  summary: Initial full-product check failed with exit 2 during PATO/RO downloads,
    with 36 adapter errors and 123 no-adapter skips. Superseded by successful retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; command metadata
    validate-products-retry-local.json
  accessed_at: '2026-10-19T23:32:49Z'
  support: context_only
  summary: Intermediate isolated-cache attempt failed with exit 2, 36 adapter errors
    and 123 no-adapter skips. Superseded by successful network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; command metadata
    validate-products-retry-network.json
  accessed_at: '2026-10-19T23:32:49Z'
  support: context_only
  summary: 'Full configured product validation passed: 361 canonical matches, two
    synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. This is not focused
    verification of every target identifier.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-biofilm-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/biofilm-validate.log
  locator: Executed 2026-10-19T23:32:40Z through 2026-10-19T23:32:42Z
  accessed_at: '2026-10-19T23:37:32Z'
  support: context_only
  summary: Selected record validates; shape validation does not adjudicate science.
  snapshot_sha256: 94d0f10bf8095988e552f85f1bd7b3e5ea34c27f945c323d589f52de5745454e
- evidence_id: check-biofilm-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/biofilm-strict.log
  locator: Executed 2026-10-19T23:32:40Z through 2026-10-19T23:32:42Z
  accessed_at: '2026-10-19T23:37:32Z'
  support: context_only
  summary: One file scanned; zero error rows.
  snapshot_sha256: 0061b64a07e0a853185225476d79de7fc86d9e923224633a370e4435b988d5c3
- evidence_id: check-biofilm-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/biofilm-snippets-network.log
  locator: Executed 2026-10-19T23:32:43Z through 2026-10-19T23:32:50Z
  accessed_at: '2026-10-19T23:37:32Z'
  support: context_only
  summary: Four snippets across four references returned NOT_IN_ABSTRACT, which is
    inconclusive for full-text quotations. Manual full-text verification resolves
    their provenance below.
  snapshot_sha256: 65c6983a6570189e97aed38b849859a5243914e4f370c5095d5774b68aabb2cf
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/biofilm_formation.yaml
  locator: Entire record, all 14 nodes, 13 edges, examples, history and discussion
  accessed_at: '2026-10-19T23:37:32Z'
  support: partial
  summary: Correct biological concept with explicit WspR scope; sources, predicates
    and some provenance require curation.
  snapshot_sha256: 8936e72d19f99bb3f7bb7ad47037a421a1e94d2d1ee3528ee77edcf57c237964
- evidence_id: metpo-identity
  kind: authority
  reference: data/raw/metpo.owl
  locator: METPO:1000059, active METPO:1007077, deprecated METPO:1000036; v5 reservation
    and release-review decision row
  accessed_at: '2026-10-19T23:37:32Z'
  support: supports
  summary: Unique local identity and phenotype parent resolve. Active surface-attached
    biofilm capability METPO:1007077 overlaps this record; reports/metpo_2026_06_12_active_review.tsv
    explicitly records DUPLICATE_NO_NEW_PRIMARY and defers migration. v5 retains proposed
    METPO:1007652, absent as an OWL subject in the captured snapshot. Searches included
    ignored/hidden corpus files.
- evidence_id: owners-history
  kind: record_content
  reference: scripts/curate_knowledge_gaps.py
  locator: Target history, connector writer, guarded writer, related infrastructure
    histories and DO_NOT_WORK
  accessed_at: '2026-10-19T23:37:32Z'
  support: partial
  summary: Scientific edits belong to the target; discussion content also occurs in
    the maintained knowledge-gap writer and connector content in scripts/connect_mechanistic_graphs_183.py.
    Promotion event is agent-attributed. Ignored-inclusive relevant history and exclusion
    searches do not establish human sign-off; target is not an exclusion match.
- evidence_id: flemming
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/27510863/
  locator: DOI:10.1038/nrmicro.2016.94; complete abstract and metadata
  accessed_at: '2026-10-19T23:32:08Z'
  support: partial
  summary: Review supports EPS-enclosed bacterial communities, matrix structural/function
    importance and ecological lifestyle. It is review context rather than a new primary
    experiment; surface-attachment wording is additionally supported by the matrix
    review.
  snapshot_sha256: 4707913c0c6c9d369b34ffc277b5823bff93f02da0cc441e46a60fc849dec2ea
- evidence_id: global-comment
  kind: primary_source
  reference: https://www.nature.com/articles/s41579-019-0162-0
  locator: Publisher preview; PMID:30792541 and Europe PMC identity
  accessed_at: '2026-10-19T23:31:39Z'
  support: refutes
  summary: The DOI denotes Bar-On and Milo, Towards a quantitative view of the global
    ubiquity of biofilms, a News & Views commentary. It is not Flemming and Wuertz
    and explicitly leaves a microbial-majority claim awaiting quantification. It does
    not establish the particular process-to-trait relation.
  snapshot_sha256: 471766734c383bde3ff8f0e3a055d7f3d5b8bdef7f6887c56713305bad1589ba
- evidence_id: matrix-review
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10903470/
  locator: DOI:10.1042/BCJ20210301; Introduction s1 and eDNA section s1c
  accessed_at: '2026-10-19T23:32:31Z'
  support: supports
  summary: Bohning et al. review explicitly describes attachment initiation, defining
    ECM, eDNA structural roles and fiber nucleation. Edge 11 quotation is contiguous
    apart from sentence-initial capitalization. These are review-level bacterial assertions,
    not proof for every taxon.
  snapshot_sha256: b142c4cf4d24aee25ce2c7b649d66d935f13ee169f4c1fcf83761106793478c0
- evidence_id: water-review
  kind: primary_source
  reference: https://mdpi-res.com/d_attachment/water/water-17-01944/article_deploy/water-17-01944.pdf
  locator: DOI:10.3390/w17131944; Introduction page 2, section 2.2 page 4
  accessed_at: '2026-10-19T23:33:06Z'
  support: supports
  summary: Wang et al. discuss c-di-GMP, EPS, motility and transition to sessile growth
    in a wastewater-treatment/bacterial review context. Supports the biological context
    of edges 4 and 6, without establishing their selected RO semantics or universality.
  snapshot_sha256: 3efd51f8aed20f4f20560263f92c437192a80311e870d10ed10daa5c31cb046c
- evidence_id: wsp-function
  kind: primary_source
  reference: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0060067
  locator: 'Publisher XML: Abstract, author summary, relevant Results; entire XML
    text searched for quoted span'
  accessed_at: '2026-10-19T23:32:31Z'
  support: partial
  summary: Primary study supports WspR diguanylate-cyclase function. The edge 5 snippet
    is not a contiguous span anywhere in inspected XML, including body/captions/references
    after whitespace and case normalization; supplements were not searched. The scientific
    claim is supported but the snippet is paraphrased.
  snapshot_sha256: 3190528d33d5e3b45592c54680ad1086ebc08d3fa2daaccd79373aea8dd30c4b
- evidence_id: wsp-example
  kind: primary_source
  reference: https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1004480
  locator: Publisher XML Results paragraph comparing PA14 and PAO1, accompanying Figure
    5
  accessed_at: '2026-10-19T23:32:31Z'
  support: supports
  summary: Primary PAO1 study supports the scoped WspR surface-colonization example.
    Its protein-example snippet is exact after whitespace normalization. It does not
    establish the other branches for PAO1; the record explicitly recognizes that boundary.
  snapshot_sha256: 5d1935a0e9ab3def3556f4b88e9c95cae419bc7a968aca01feeac487baf00180
- evidence_id: no-review
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC11591520/
  locator: DOI:10.3390/antibiotics13111047; section 4.2
  accessed_at: '2026-10-19T23:32:31Z'
  support: partial
  summary: Review supports context-dependent NO-associated dispersal and release from
    matrix; it discusses an intermediate in a named bacterial model and contains inconsistent
    concentration-direction prose. Edge 12 quotation is contiguous except sentence-initial
    capitalization. It does not establish a direct molecular edge, universal response
    or the discussion categorical causal conclusions.
  snapshot_sha256: d61c6f464f799663c5b41dc349d9c58302ec95c24b6f933b34a8a512ed9a8f8e
- evidence_id: qs-review
  kind: primary_source
  reference: https://mdpi-res.com/d_attachment/bacteria/bacteria-03-00008/article_deploy/bacteria-03-00008.pdf
  locator: DOI:10.3390/bacteria3030008; abstract/introduction pages 118-119 and section
    6
  accessed_at: '2026-10-19T23:33:07Z'
  support: supports
  summary: Erkihun et al. review describes AHL/AIP/AI-2 signaling categories and biofilm
    roles. It supports scoped regulatory association rather than every signal in every
    organism or the chosen RO domain semantics.
  snapshot_sha256: 44461bd1283fb7223bab21641176ab1aaf1b4252233e6d055ee33f189db99949
- evidence_id: species-example
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/35335624/
  locator: Complete abstract; DOI:10.3390/pathogens11030300, PMC8950561
  accessed_at: '2026-10-19T23:32:09Z'
  support: supports
  summary: Tuon et al. review supports P. aeruginosa as a biofilm-forming model species.
    Its pathogenic context does not establish every ecological mechanism for all isolates.
  snapshot_sha256: d13fa604534e71cc808e73e262767e471ab0e0db5ef84258900e56a0028783a9
- evidence_id: live-identifiers
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9HXT9.json
  locator: Entry identity/audit, organism, gene, InterPro and proteome cross-references;
    live taxonomy/proteome endpoints
  accessed_at: '2026-10-19T23:33:13Z'
  support: supports
  summary: Q9HXT9 is active unreviewed wspR/PA3702 in PAO1 taxon 208964, reference
    proteome UP000002438. Species 287 and child strain 208964 resolve. Current entry
    version 153 and sequence 1 do not invalidate an explicitly dated historical version-152
    observation.
  snapshot_sha256: 09af3bf7033d3c6e020dc50439733b62cee5e10e0beee358f0e3ef295bdd8247
- evidence_id: interpro-family
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050469/
  locator: Family name/type and UniProt Q9HXT9 explicit family cross-reference
  accessed_at: '2026-10-19T23:33:13Z'
  support: supports
  summary: IPR050469 is a broader bacterial Dgc-like diguanylate-cyclase family and
    Q9HXT9 belongs to it. The schema permits family grounding separate from taxon-paired
    instances; this is compatible as a family anchor, not WspR-specific equivalence
    or primary experimental proof. InterPro description is marked LLM-assisted.
  snapshot_sha256: add23a6366425ba77c81f770650597e92205cbaaa8eb6a134e91880928ad0bae
- evidence_id: ontology-nodes
  kind: authority
  reference: https://purl.obolibrary.org/obo/GO_0042710
  locator: 'Hashed local GO/CHEBI caches: GO:0042710, GO:0031012 and CHEBI:16480 label/definition'
  accessed_at: '2026-10-19T23:33:53Z'
  support: supports
  summary: Process, extracellular matrix and nitric oxide node identities match. GO
    annotation-exclusion subset is not deprecation. Cached release freshness is unknown.
  snapshot_sha256: 8580ea6c5c95535f4e1bea85cca51fb491d618e880080abc7f86276654d717e4
- evidence_id: ro-semantics
  kind: authority
  reference: https://purl.obolibrary.org/obo/RO_0002211
  locator: Cached rdfs:domain/range/definitions/subproperties for RO:0002211, 0002212,
    0002213, 0002327 and ancestors
  accessed_at: '2026-10-19T23:33:53Z'
  support: refutes
  summary: Regulates explicitly has process domain/range, inherited by positive/negative
    regulation. Enables requires a material actor executing a process through its
    parent relations. Edges 4, 6, 10 and 12 use chemical/state endpoints inconsistently.
    Wildcard mapping gates do not override ontology semantics; this is manual interpretation,
    not a reasoner result.
  snapshot_sha256: 3120f8e09fcf819197ecf3b15f27d6633811b297e1f6a88aad8fd86d79b616bb
- evidence_id: confers-proposal
  kind: authority
  reference: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
  locator: METPO:2007700 row, SSSOM and mappings/predicate_grounding.tsv
  accessed_at: '2026-10-19T23:37:32Z'
  support: supports
  summary: Locally proposed confers describes process realization of a trait and matches
    this endpoint direction. Its identifier remains a documented placeholder, not
    a verified minted upstream predicate.
- evidence_id: scan-provenance
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/42039744/
  locator: 'Complete Europe PMC abstract and three other retained scan abstracts:
    PMID:41245847, 41661098, 42125129'
  accessed_at: '2026-10-19T23:32:09Z'
  support: partial
  summary: All four identifiers resolve and preserved quotations match their abstracts.
    The first concerns lung/airway mucosal IgA homeostasis, while the record says
    gut mucosa. The other scan statements are explicitly historical and do not support
    the NO-specific discussion.
  snapshot_sha256: 0cbe35b27bbeca6fe36a1ff41e0e83672f26e5efff5a834a60aa97991f01f90f
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identity, polarity and term kind'
  outcome: supported
  target_ids:
  - traitmech:000053
  evidence_ids:
  - record
  - metpo-identity
  summary: The local CLASS denotes a positive surface-associated biofilm-forming phenotype,
    distinct from an organism or the separately modeled process. RELATED_SYNONYM is
    appropriately nonexact. Known active-METPO overlap requires planned reconciliation
    rather than automatic replacement.
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: definition and source scope'
  outcome: supported
  target_ids:
  - traitmech:000053
  evidence_ids:
  - flemming
  - matrix-review
  - record
  summary: The noncircular definition is supported jointly by Flemming matrix/lifestyle
    context and Bohning surface-attachment text. Its surface-attached operational
    scope is explicit; not every broader aggregate usage is equated with it.
- assessment_id: hierarchy
  area: consistency
  topic: 'Native checklist: broader parent and category'
  outcome: supported
  target_ids:
  - traitmech:000053
  evidence_ids:
  - metpo-identity
  - confers-proposal
  - record
  summary: The phenotype parent is broader; ECOLOGY and CLASS fit the lifestyle capability.
    The process node is kept distinct from the trait node and proposed confers has
    the corresponding direction.
- assessment_id: examples
  area: grounding
  topic: 'Native checklist: taxon and protein examples'
  outcome: supported
  target_ids:
  - traitmech:000053
  evidence_ids:
  - species-example
  - wsp-example
  - live-identifiers
  - interpro-family
  summary: Species and PAO1 examples have appropriately bounded source support. Taxon,
    gene, UniProt status and proteome pairing resolve. Family-level InterPro and taxon-specific
    protein example remain separate.
  dimensions:
  - name: example_rank
    value: Species 287; strain 208964
    definition: Distinct scopes of the general biofilm exemplar and PAO1 WspR branch.
    evidence_ids:
    - live-identifiers
    - species-example
    - wsp-example
  - name: protein_entry_status
    value: UNREVIEWED; current entry153/sequence1; historical record152
    definition: Database provenance, not experimental certification or an instruction
      to refresh dated metadata.
    evidence_ids:
    - live-identifiers
- assessment_id: evidence
  area: evidence
  topic: 'Native checklist: citation identity, quotations and evidence tier'
  outcome: concern
  target_ids:
  - traitmech:000053
  evidence_ids:
  - global-comment
  - wsp-function
  - matrix-review
  - no-review
  - wsp-example
  - check-biofilm-snippets-network
  - record
  summary: A 2019 commentary is misattributed and overstates support. WspR function
    is supported but its quotation is paraphrased; ten of thirteen edge entries and
    both top-level evidence entries lack snippets. Other inspected full-text quotations
    match apart from two sentence-initial capitalization changes.
- assessment_id: graph
  area: graph
  topic: 'Native checklist: node identity, edge semantics and scoped evidence'
  outcome: concern
  target_ids:
  - traitmech:000053
  evidence_ids:
  - record
  - ro-semantics
  - ontology-nodes
  - confers-proposal
  - check-audit-graphs
  - flemming
  - global-comment
  - matrix-review
  - water-review
  - wsp-function
  - no-review
  - qs-review
  summary: All nodes and edges were assessed. Graph connectivity is satisfactory,
    but four RO relations conflict with endpoint semantics. Source support for a biological
    association does not fix those ontology mismatches. Matrix/fiber CHEMICAL typing
    is broad; compositional versus assembled-matrix distinction could be clearer,
    without a demonstrated closed-schema error.
  details: 'Zero-based edge ledger: 0 matrix context supported, but RO enables is
    stronger than passive scaffolding; 1 bibliography/claim-support defect; 2 and
    3 explicit Bohning review support; 4 Wang contextual support with RO mismatch;
    5 primary WspR function supported, snippet not verbatim; 6 contextual prerequisite
    supported with RO mismatch; 7 context-dependent review support, no unconditional
    concentration claim; 8 and 9 explicit review-level eDNA assertions; 10 review-level
    QS support with RO mismatch; 11 explicit attachment-process support; 12 dispersal/loss-of-sessility
    interpretation supported with RO mismatch. The PAO1 scope note applies only to
    its branch, not all others.'
- assessment_id: discussions
  area: consistency
  topic: 'Native checklist: discussions, logical certainty and datasets'
  outcome: concern
  target_ids:
  - traitmech:000053
  evidence_ids:
  - record
  - no-review
  - scan-provenance
  summary: The discussion anchors resolve and topic is relevant, but its yes/no outcome
    interpretations claim more causal certainty than follows. Historical scan references
    are correctly disclaimed as evidence, with one incorrect tissue description. No
    dataset is asserted.
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: required versus optional representation'
  outcome: supported
  target_ids:
  - traitmech:000053
  evidence_ids:
  - record
  summary: Examples, graph and evidence are present. Optional datasets or extra synonyms
    are not required; omitted mechanism steps are not to be invented. Identified corrections
    concern retained claims and provenance.
- assessment_id: status
  area: provenance
  topic: 'Native checklist: scientific status and audit'
  outcome: unknown
  target_ids:
  - traitmech:000053
  evidence_ids:
  - owners-history
  - metpo-identity
  - check-biofilm-validate
  - check-biofilm-strict
  - check-validate-history
  summary: Focused schema/strict checks and corpus gates pass within their scopes.
    REVIEWED promotion is attributed to an LLM-assisted agent; this review cannot
    establish historical human sign-off. Known identifier overlap remains recorded
    in release-review decisions.
findings:
- finding_id: global-citation
  issue_key: biofilm-formation-global-citation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 2019 citation identity and claimed support are incorrect
  description: The exact DOI names Bar-On and Milo, not Flemming and Wuertz; its preview
    questions quantitative predominance. The target attributes the source to different
    authors and invokes established dominant lifestyle to support a specific process-to-trait
    assertion. Resolve the bibliography and nearest-claim support without automatic
    DOI substitution.
  target_ids:
  - traitmech:000053
  field_paths:
  - evidence[1]
  - causal_graphs[0].edges[1].evidence[0]
  evidence_ids:
  - global-comment
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  rule_id: 'review-yaml-record: Evidence Rules; native field-by-field checklist'
  native_severity: major
  normalization_reason: Material support/grounding defects are major; bounded provenance
    or wording defects minor; known reconciliation context informational.
- finding_id: ro-endpoint-semantics
  issue_key: biofilm-formation-ro-endpoint-semantics
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Four RO groundings conflict with their endpoint types
  description: Edges 4, 10 and 12 use process-regulation relations with chemical subjects
    and/or a STATE object. Edge 6 uses enables with a STATE subject, although the
    relation requires a material actor executing the process. Scientific contextual
    support and permissive mapping gates do not establish compatible ontology meaning.
  target_ids:
  - traitmech:000053
  field_paths:
  - causal_graphs[0].edges[4].predicate_id
  - causal_graphs[0].edges[6].predicate_id
  - causal_graphs[0].edges[10].predicate_id
  - causal_graphs[0].edges[12].predicate_id
  evidence_ids:
  - ro-semantics
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained predicate candidates and type gates; any systemic correction
      requires independent scope review
  rule_id: 'review-yaml-record: Evidence Rules; native field-by-field checklist'
  native_severity: major
  normalization_reason: Material support/grounding defects are major; bounded provenance
    or wording defects minor; known reconciliation context informational.
- finding_id: quotation-provenance
  issue_key: biofilm-formation-quotation-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Edge quotations do not consistently expose source support
  description: Edge 5 presents a source-consistent paraphrase as a verbatim snippet;
    it was not found in the complete acquired publisher XML after whitespace/case
    normalization. Ten of thirteen edges and both top-level evidence entries have
    no snippets. Other full-text snippets are exact apart from initial case. Missing
    quotations are not by themselves proof the scientific claim is false.
  target_ids:
  - traitmech:000053
  field_paths:
  - causal_graphs[0].edges[5].evidence[0].snippet
  - causal_graphs[0].edges
  - evidence
  evidence_ids:
  - wsp-function
  - record
  - matrix-review
  - no-review
  - wsp-example
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  rule_id: 'review-yaml-record: Evidence Rules; native field-by-field checklist'
  native_severity: minor
  normalization_reason: Material support/grounding defects are major; bounded provenance
    or wording defects minor; known reconciliation context informational.
- finding_id: discussion-certainty
  issue_key: biofilm-formation-discussion-certainty
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Discussion outcome interpretations overstate causal certainty
  description: Excluding one nominated intermediate cannot prove that no other intermediate
    exists or that the drawn direct edge is correct. Conversely, an absent outcome
    alone does not establish a uniquely necessary intermediate. The rationale also
    states intrinsic refractoriness without attached support, while its cited review
    already discusses an intermediate in a bounded model.
  target_ids:
  - traitmech:000053
  field_paths:
  - discussions[0].rationale
  - discussions[0].proposed_experiments[0].would_support
  - discussions[0].proposed_experiments[0].would_refute
  evidence_ids:
  - record
  - no-review
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion text and guarded regeneration path
  rule_id: 'review-yaml-record: Evidence Rules; native field-by-field checklist'
  native_severity: minor
  normalization_reason: Material support/grounding defects are major; bounded provenance
    or wording defects minor; known reconciliation context informational.
- finding_id: scan-tissue-provenance
  issue_key: biofilm-formation-scan-tissue-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical scan note misidentifies the tissue context
  description: PMID:42039744 and the retained quote concern lung/airway mucosal IgA
    homeostasis, not gut mucosa. The citation is already disclaimed as support for
    the current question, so this is a bounded provenance defect.
  target_ids:
  - traitmech:000053
  field_paths:
  - discussions[0].notes
  evidence_ids:
  - scan-provenance
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion text and guarded regeneration path
  rule_id: 'review-yaml-record: Evidence Rules; native field-by-field checklist'
  native_severity: minor
  normalization_reason: Material support/grounding defects are major; bounded provenance
    or wording defects minor; known reconciliation context informational.
- finding_id: known-metpo-reconciliation
  issue_key: biofilm-formation-known-metpo-reconciliation
  category: identity
  severity: informational
  status: deferred
  certainty: confirmed
  title: Active METPO overlap is already recognized but not reconciled
  description: The captured ontology has active METPO:1007077 and the release-review
    table explicitly associates it with this local record while deferring primary-identifier
    migration. v5 still reserves a different proposed METPO ID. This is acknowledged
    follow-up, not a finding that the record denotes the wrong phenotype.
  target_ids:
  - traitmech:000053
  field_paths:
  - identifier
  - causal_graphs[0].nodes[0].grounding
  evidence_ids:
  - metpo-identity
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    role: Legacy proposed identity requiring reconciliation with the known active
      upstream match
  rule_id: 'review-yaml-record: Evidence Rules; native field-by-field checklist'
  native_severity: informational
  normalization_reason: Material support/grounding defects are major; bounded provenance
    or wording defects minor; known reconciliation context informational.
  disposition_reason: Existing release-review inputs deliberately retain the local
    primary identifier; coordinated migration requires separate exact-scope reconciliation
    and is outside this read-only review.
actions:
- action_id: repair-global-citation
  description: Reassess source identity and exact support for the retained ecological
    and process-to-trait statements.
  finding_ids:
  - global-citation
  target_ids:
  - traitmech:000053
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  acceptance_checks:
  - Inspect authoritative identity and actual source text; do not substitute a plausible
    DOI without review.
  - Separate prevalence context from the ontology realization assertion.
  - After authorized curation, run focused validate, validate-strict, verify-snippets
    and applicable native qc gates.
- action_id: reassess-ro-relations
  description: Review the retained relation meanings and typed endpoints against exact
    ontology definitions; do not mechanically replace labels or infer new mechanisms.
  finding_ids:
  - ro-endpoint-semantics
  target_ids:
  - traitmech:000053
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained predicate candidates and type gates; any systemic correction
      requires independent scope review
  acceptance_checks:
  - Demonstrate domain/range-compatible meanings for each retained grounded relation,
    including inherited constraints.
  - Assess whether the maintained mapping gate would regenerate the same mismatch.
  - Use guarded curation and history for any authorized change; run strict, audit-graphs,
    applicable grounding checks and qc.
- action_id: repair-quotation-provenance
  description: Use short source-checked contiguous quotations for retained claims
    and put interpretation in notes.
  finding_ids:
  - quotation-provenance
  target_ids:
  - traitmech:000053
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  acceptance_checks:
  - Replace or relabel the WspR paraphrase after inspecting the source; retain its
    supported functional scope.
  - Fill provenance gaps only where actual source text supports the retained claim.
  - Run focused verify-snippets and audit-snippets; interpret abstract-only nonmatches
    explicitly.
- action_id: bound-discussion-inference
  description: Qualify the discussion conclusions and literature scope so the stated
    interpretations follow from the available evidence.
  finding_ids:
  - discussion-certainty
  target_ids:
  - traitmech:000053
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion text and guarded regeneration path
  acceptance_checks:
  - Remove claims of directness or unique necessity that do not follow from the stated
    contrast.
  - Reconcile the maintained discussion writer with any authorized text correction.
  - Do not introduce a protocol, replacement mechanism, therapeutic efficacy claim
    or intervention recommendation; validate the revised record.
- action_id: correct-scan-context
  description: Correct the tissue description in the preserved scan-provenance note
    and corresponding maintained writer.
  finding_ids:
  - scan-tissue-provenance
  target_ids:
  - traitmech:000053
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion text and guarded regeneration path
  acceptance_checks:
  - Check against the inspected PMID abstract and retain the original citation/quote
    as historical provenance.
  - Preserve the disclaimer that these references do not support the current discussion.
  - Run focused strict validation after any authorized edit.
- action_id: reconcile-known-metpo-match
  description: When identifier migration is separately authorized, settle exact scope
    and reconcile the known active match, local references and legacy proposal consistently.
  finding_ids:
  - known-metpo-reconciliation
  target_ids:
  - traitmech:000053
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biofilm_formation.yaml
    role: Maintained scientific record; corrections require guarded curation and history
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    role: Legacy proposed identity requiring reconciliation with the known active
      upstream match
  acceptance_checks:
  - Verify exact scope/equivalence against the chosen METPO release; retain the release-review
    decision provenance.
  - Apply the maintained identifier policy and check all internal references and proposal
    ownership before any migration.
  - Run native identifier/reference, strict, history and qc gates after authorized
    changes.
limitations:
- Flemming 2016 was assessed from its complete abstract and metadata, and Bar-On/Milo
  2019 from publisher preview plus metadata; subscription full texts were not inspected.
- Other literature was inspected through publisher or Europe PMC XML and publisher
  PDFs. No supplements or actual figure images were evaluated, and no experimental
  or clinical recommendation is made.
- Most broad graph branches rely on review articles, not independently reassessed
  primary experiments. The record appropriately bounds the PAO1 WspR exemplar; that
  example does not establish every other branch or a universal microbial mechanism.
- The NO review contains inconsistent concentration-direction descriptions. This review
  retains only context-dependent dispersal support and does not infer a concentration-response
  rule.
- The current UniProt entry is version 153, sequence version 1. The record explicitly
  preserves its 2026-08-25 retrieval and version 152; historical bytes were not retrieved,
  so that historical version is not certified or treated as an error.
- METPO identity/proposal conclusions use the captured repository release. GO/CHEBI/RO
  terms were read from hashed session-local caches; their release freshness was not
  established. No OWL reasoning run is claimed.
- The inspected curation event and target/infrastructure history attribute promotion
  to an LLM-assisted agent. Human sign-off was not traceable in that bounded, ignored-inclusive
  history search; this does not establish that approval never occurred.
- No structured-source runner was available on PATH or at the configured sibling CLAW
  location. Direct authoritative identifiers and source text were used instead; expression-module
  membership is not phenotype or mechanism proof.
- Full-corpus diagnostics are reused from the unchanged source base, with their actual
  results and times. Product validation retains 123 no-adapter skips.
notes:
- No trait, writer, proposal, history or generated page was changed. A completed review
  is not human scientific sign-off.
- Source capture expansions preserved all earlier hashes. Owner paths identify future
  curation inputs, not permission to run those writers.
- The pending active-METPO match is not evidence that the local record denotes the
  wrong biological trait; identifier reconciliation is already acknowledged by the
  release-review table.
tags:
- record-review
- biofilm-formation
- ecology
- needs-curation
```
