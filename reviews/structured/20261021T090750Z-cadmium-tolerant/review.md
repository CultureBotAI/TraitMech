# Evidence and grounding review of cadmium tolerance (traitmech:000013)

- Review: 20261021T090750Z-cadmium-tolerant
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T09:01:13Z
- Finished UTC: 2026-10-21T09:07:50Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Cadmium tolerance has a justified fallback identity, supported strain examples and coherent chemical/protein identities. No major finding is established. Three minor findings concern broad transport grounding, provisionally unverified quotation fidelity and a bounded missing human-acceptance link. All eight nodes and seven edges were inspected, with four exact2023-review claims and remaining protein-anchor experimental provenance explicitly unresolved because full text was unavailable. The failed UniProt live-version check is retained alongside valid archived metadata.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Seventh batch004 target in lexicographic path order. Entire target read before native capture; eight nodes, seven edges, both canonical organisms and the single protein example are included.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000013 | data/traits/environment/cadmium_tolerant.yaml | maintained | cadmium tolerant |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000013 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000013 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000013 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | traitmech:000013 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | traitmech:000013 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000013 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000013 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | traitmech:000013 | Selected record validates. |
| Focused strict validation | passed | True | traitmech:000013 | One file scanned; zero strict errors. |
| Focused abstract snippet check | passed | True | traitmech:000013 | Three snippets across two references are NOT_IN_ABSTRACT. These misses are inconclusive; manual source verification and limitations are reported separately. |
| Native full-corpus protein/taxon coverage | passed | True | traitmech:000013 | Reused actual08:55:04–10Z execution:719graphs,129PASS,589NONMECHANISTIC,onePROTECTED,zero gaps/errors. TargetPASS has three label-only proteins, two cited canonical examples and one taxon-paired example. This is structural coverage, not source verification. |
| Native full-corpus live UniProt audit | failed | True | traitmech:000013 | Reused actual08:55:08–08:56:53Z execution:exit1,146uses/115accessions,110findings all ENTRY_VERSION_MISMATCH. P13511 matches primary accession, taxon, review status, sequence3 and proteome; stored153 versus current154 is the only target finding. Historical153 is assessed separately. |
| Structured-source runner discovery | unavailable | False | traitmech:000013 | Original bounded discovery reused; official catalog fallback inspected. |
| Canonical-organism dataset applicability | not_applicable | False | traitmech:000013 | No canonical Cupriavidus dataset matches; no organism substitution or expression queries. |

## Scientific And Domain Assessments

### Native checklist: fallback, term kind, polarity and hierarchy

identity: supported. Targets: traitmech:000013.

The accepted fallback is justified against the complete pinned ontology scan; its local proposal is not an upstream minted identity. Cadmium tolerance is a narrower positive environmental class under metal/metalloid tolerance.

### Native checklist: growth phenotype and typical efflux emphasis

evidence: supported. Targets: traitmech:000013.

The definition is a reasonable synthesis of the broad resistance review and cadmium-specific primary phenotype evidence. It does not require a universal czc system or assert a numerical growth cutoff.

### Native checklist: both canonical examples and CzcA component

evidence: supported. Targets: traitmech:000013.

Current taxon identities and CH34 cadmium-resistance context agree. P13511 identifies the declared reviewed inner-membrane component, and both the cited CzcP paper and CH34 source discuss CzcA. A component explicitly placed within the aggregate is not automatically a whole-complex error.

### Native checklist: scoped mechanistic graph and experimental provenance

representation: unknown. Targets: traitmech:000013.

ENVIRONMENT/CLASS and the explicit aggregate/component representation fit. Native protein/taxon coverage passes. Specific P13511 experimental provenance in the attached2009 article was not fully assessed because only Summary/Introduction were accessible; positive role support exists, so limited access does not establish an unsupported-anchor defect.

### Native checklist: all identifiers and transport specificity

grounding: concern. Targets: traitmech:000013.

Both chemical identities, taxonomy and the protein instance match. GO0030001 is a legitimate broad metal-transport concept but does not encode the exact cadmium/outward-transmembrane meaning of node3. This is bounded precision rather than wrong ion identity or an invalid process aspect.

### Native checklist: all seven edge roles and directions

consistency: supported. Targets: traitmech:000013.

Current executor/process and challenge/mitigation endpoint roles are compatible. The zinc induces label explicitly concerns expression and need not carry an invented predicate ID. Compartment interpretation is kept at the component/aggregate level with source differences retained.

### Native checklist: five references, three snippets and seven nearest claims

evidence: unknown. Targets: traitmech:000013.

The efflux/challenge claims have inspected support. Four2023-review-dependent claims remain unverified at their exact source because body access failed. One long snippet matches with typography normalization; top CzcP wording is a faithful compressed paraphrase and anchor exactness is unverified in inspected passages.

### Native checklist: historical version and later live-audit drift

provenance: supported. Targets: traitmech:000013.

Archived153/sequence3 matches the recorded snapshot; current154 is later. The native audit’s freshness failure is retained, while identity, taxon, review status and proteome remain correct. The past retrieval itself was not independently re-observed.

### Native checklist: required shape and optional discussions/datasets

completeness: supported. Targets: traitmech:000013.

All endpoints resolve and the scoped graph carries one structurally valid paired protein example. Additional instances or expression datasets are not automatically required for every contextual branch. Existing provider research remains a lead rather than primary evidence.

### Native checklist: canonical-taxon structured-source applicability

evidence: supported. Targets: traitmech:000013.

No matching Cupriavidus dataset occurs in the inspected catalog. No gene/module searches or taxon substitution followed, and noncoverage supplies no negative biology.

### Native checklist: AI disclosure, acceptance and maintained owners

provenance: concern. Targets: traitmech:000013.

Eight events disclose AI assistance. No human-acceptance link was found within bounded local provenance. Current literal owner searches do not establish that the broad GO grounding would recur from the maintained mapping.

## Findings

### transport-grounding-specificity: The transport grounding is broader than the stated process

minor / open / confirmed; issue key: cadmium-tolerant-transport-grounding-specificity.

Node3 names cadmium ion transmembrane export but GO0030001 denotes general metal-ion transport. That is a genuine broad context for the process, yet it does not establish cadmium specificity or outward direction as an exact grounding. Clarify the relationship or use an exact supported term; no wrong chemical identity or formal type exclusion is asserted.

### quotation-fidelity: Two CzcP-source snippets need verbatim verification

minor / open / provisional; issue key: cadmium-tolerant-quotation-fidelity.

The top snippet is a faithful subject-substituted paraphrase of the inspected Summary, and the protein-anchor phrase was not verified in the accessed Summary/Introduction. Verify an exact passage or move interpretive wording into notes. The full2009body was not exhaustively inspected, so this is a provisional quotation concern rather than confirmed absence from the whole article.

### human-acceptance-link: Human scientific acceptance is not linked locally

minor / open / confirmed; issue key: cadmium-tolerant-human-acceptance-link.

The eight disclosed AI events, including status promotion, and ignored-inclusive local review/history search do not identify human scientific acceptance of this revision. Prior reviews reference the file as context, not as their target. Remote or private acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### clarify-transport-grounding

In separately authorized curation, reconcile node3’s exact process wording with the breadth of its grounding.

- The selected identifier and intended transport specificity/direction agree, or the broader relationship is explicitly represented without claiming exact identity.
- Do not invent a replacement accession or treat broad metal-ion transport as a wrong biological-process type.
- The current writer skips populated IDs; use guarded correction and run focused strict/term/graph checks and just qc, with native history and affected generated products after authorized edits.

### verify-snippets

Verify exact CzcP-paper passages for both snippets or move faithful paraphrase into notes.

- Retained quotation text has a precise inspected source location.
- Keep supported transport and CzcA background claims; source-access limits alone do not establish false biology.
- Run focused snippet verification and manual primary-text checking after authorized changes.

### link-acceptance

Locate and link existing human acceptance or obtain it through the established process, preserving AI history and reassessing status if necessary.

- Acceptance identifies the revision and scientific scope.
- Automated coverage, AI provenance and this review are not substituted for human scientific acceptance.

### resolve-source-limits

When full source text becomes available, assess the four2023-review claims and the remaining2009 experimental-anchor provenance at their exact passages before strengthening the verdict.

- Record support, qualification or contradiction separately for edges3–6 and the P13511 anchor.
- Preserve current unknowns until actual source text is inspected; HTTP200 help/error content is excluded.
- No experimental design or expanded mechanism is needed for this documentary follow-up.

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
| check-cadmium_tolerant-validate | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/cadmium_tolerant-validate.log; Executed 2026-10-21T09:01:38Z through 2026-10-21T09:01:42Z; metadata cadmium_tolerant-validate.json | context_only | Selected record validates. |
| check-cadmium_tolerant-strict | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/cadmium_tolerant-strict.log; Executed 2026-10-21T09:01:38Z through 2026-10-21T09:01:42Z; metadata cadmium_tolerant-strict.json | context_only | One file scanned; zero strict errors. |
| check-cadmium_tolerant-snippets | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/cadmium_tolerant-snippets.log; Executed 2026-10-21T09:01:41Z through 2026-10-21T09:01:45Z; metadata cadmium_tolerant-snippets.json | context_only | Three snippets across two references are NOT_IN_ABSTRACT. These misses are inconclusive; manual source verification and limitations are reported separately. |
| check-corpus-protein-taxa | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log; Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json | context_only | Reused actual08:55:04–10Z execution:719graphs,129PASS,589NONMECHANISTIC,onePROTECTED,zero gaps/errors. TargetPASS has three label-only proteins, two cited canonical examples and one taxon-paired example. This is structural coverage, not source verification. |
| check-corpus-uniprot | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-uniprot.log; Executed 2026-10-21T08:55:08Z through 2026-10-21T08:56:53Z; metadata corpus-uniprot.json | context_only | Reused actual08:55:08–08:56:53Z execution:exit1,146uses/115accessions,110findings all ENTRY_VERSION_MISMATCH. P13511 matches primary accession, taxon, review status, sequence3 and proteome; stored153 versus current154 is the only target finding. Historical153 is assessed separately. |
| check-reuse | Scientific snapshot comparison before audit reuse; All1130trait files plus native audit implementations | supports | All trait bytes match the previous owned scientific snapshot; the target hash agrees with its native capture. Original full-corpus executions are reused with actual scope and failures, not relabelled as new focused checks. |
| record | data/traits/environment/cadmium_tolerant.yaml; Entire identity, evidence, graph, protein example and eight events | partial | The target describes environmental cadmium tolerance with a scoped CzcCBA/CzcP aggregate and a specifically labelled CzcA component example. Component, aggregate and transport-route claims must remain distinguishable. |
| shape | Whole graph/history inspection; Eight nodes, seven edges and eight AI-assisted events | supports | All endpoints resolve; one protein instance is present and no pathway-context link is asserted. All eight events explicitly disclose AI assistance. |
| policy | docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml; Family/aggregate versus taxon-paired component; retrieval-time versions | supports | Reviewed label-only aggregates can retain scoped protein instances. An explicitly identified component is not automatically an erroneous whole-complex identifier. Entry/sequence versions describe retrieval-time snapshots; current version drift must be distinguished from historical error. |
| identity | Pinned data/raw/metpo.owl; v5 proposal class table; parent metal_tolerant.yaml; Complete METPO search, fallback and broader parent | supports | The pinned ontology contains no active exact cadmium-tolerance term; the local v5 proposal remains a proposal rather than an upstream minted identity. The accepted traitmech fallback and broader metal/metalloid-tolerance parent fit. |
| grounding | Official ChEBI48775/29105; QuickGO GO0030001; NCBI119219/266264; Fresh chemical identities09:02:07–09Z; hash-verified GO/taxonomy originals08:54:06–07Z | partial | Cadmium(2+) and zinc(2+) labels agree with their ChEBI terms. GO0030001 is valid general metal-ion transport: a true broader context for cadmium transport, but it lacks cadmium specificity and outward direction. Taxon identities match. |
| protein | UniProtKB:P13511; UniSave version153; UP000002429; Current and archived CzcA identity plus reference proteome | supports | P13511 is primary reviewed CzcA/Rmet5980 in CH34 with the stated reference proteome. Archived153/sequence3 is consistent with the declared2026-08-25 snapshot; current154 is a later update. Neither review status nor a current version difference substitutes for primary mechanism evidence. |
| ledger | Independent complete node/edge ledger; Eight nodes, seven edges, one instance | partial | No formal current relation-role conflict was confirmed. The instance role expressly identifies CzcA as a component of a broader CzcCBA/CzcP aggregate. GO precision is a bounded concern; exact biological source scope is assessed separately. |
| owners | mappings,scripts,src,proposals; scripts/ground_causal_nodes.py; Ignored-inclusive exact-label/identifier writer search | context_only | No dedicated current literal mapping/writer reference for the target groundings was identified within the declared bounds. The node writer skips populated IDs; there is no evidence that clearing a value would automatically recreate this broad grounding. Historical ownership outside the search remains unknown. |
| provenance | Whole target history and bounded local history/mapping/writer/review search; Eight AI events and268ignored-inclusive matching lines | partial | All eight events explicitly disclose AI assistance. Prior-review matches are contextual input references, not target coverage or human acceptance. No acceptance link identifying this revision was found within the inspected local bounds; remote/private acceptance remains unknown. |
| status-rule | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md; Status/audit gate | supports | REVIEWED requires human scientific acceptance, distinct from AI history, mapping decisions and validation. |
| expression | https://imodulondb.org/api/datasets; Original07:36:12Z catalog; hash-verified current applicability assessment | context_only | No Cupriavidus/metallidurans/CH34/BS1 dataset matches the inspected catalog. No species was substituted and no gene/module query was warranted. Noncoverage is not evidence against protein function or cadmium tolerance. |
| runner | Structured-source runner discovery; Original bounded ignored-inclusive08:17:15Z discovery | context_only | The original runner search is reused with its exact bounds and official-catalog fallback. This is not a fresh or global absence claim. |
| bibliography | Complete primary-source claim and acquisition ledger; Five references, thirteen citation placements and three snippets | partial | All five identities resolve. Two complete primary XMLs were reused with verified hashes; the CzcP publisher Summary/Introduction was actually inspected. Definition and2023review remain abstract-limited. Ten download attempts yielded three usable hashed metadata responses and one hashed nonarticle BioC error response; that HTTP200 help page is excluded from source evidence. |
| definition-source | https://pubmed.ncbi.nlm.nih.gov/12829273/; DOI10.1016/s0168-6445(03)00048-2; complete indexed abstract, primary issue TOC208–216 | supports | The review supports layered efflux-mediated prokaryotic metal resistance. It supplies broad mechanism context rather than a formal cadmium growth threshold. The definition is a synthesis, with the record’s primary strain sources supplying cadmium phenotype support. Body access was unavailable. |
| czcp | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2009.06792.x; PMID19602147; successful publisher Summary80–82, Introduction87–90/93/102–105 | partial | The study supports CzcP metal export and explicitly discusses CzcA as an inner-membrane CzcCBA component. Its title does not make it a wrong CzcA citation. The top snippet substitutes CzcP for the source’s anaphoric subject and is a faithful compressed paraphrase of the inspected Summary. The anchor phrase remains unverified in the accessed passages. No whole-body absence is claimed. |
| sequestration-source | https://doi.org/10.1007/s40201-023-00887-6; PMID38887775, PMC11180082; indexed abstract and publisher preview42–48 | partial | The review broadly covers microbial cadmium sequestration and efflux. Its abstract does not verify the four precise existing claims on metallothionein binding/free-pool change, CadA compartment detail and zinc cross-induction. Failed full-text access leaves those claims unknown, not false or absent from the source. |
| bs1 | https://doi.org/10.3389/fmicb.2020.00047; PMID32117100, PMC7019866; ResultsS3.SS1/body11 and Table1 | supports | BS1 cadmium MIC2.5mM is exact under the reported assay; CH34 comparison is3.5mM. The long quote matches apart from harmless uM/μM typography. MIC is an inhibitory endpoint and the record already labels it as such; no unsupported growth-at-MIC or universal species threshold is inferred. |
| ch34 | https://doi.org/10.1371/journal.pone.0010433; PMID20463976, PMC2864759; Introductionbody3, Resultss2f/body53–54, Table5czc row | supports | The primary genome article directly describes CH34 cadmium resistance, CzcCBA/CzcA function and a locus combining CzcCBA,CzcD,CzcP for detoxification. Its transenvelope account differs from the2009 paper’s compartment framing. Preserve those source distinctions and the record’s explicit aggregate/component roles rather than asserting a universal contradiction. |

## Limits And Additional Notes

- The2023cadmium-review body was unavailable after finite primary/PMC/BioC/PDF attempts. A single delayed BioC retry returnedHTTP200 API error/help, not article content. Edges3–6 remain unverified at their nearest cited source, not demonstrated false or absent from the paper.
- CzcP2009 publisher Summary/Introduction were successfully inspected before later403responses. No local full-text hash is fabricated, and the complete results/discussion were not assessed.
- The attached CzcP paper explicitly discusses CzcA; its title alone does not make the reference wrong. Known reviewed protein-level support and component role are positive evidence, while exact experimental provenance in that attached paper remains partly unassessed.
- Source compartment framings differ:2009 distinguishes RND periplasmic export from ATPase cytoplasmic export, whereas2010 describes a transenvelope route and a combined locus. The record’s aggregate includes both; no universal compartment contradiction is asserted.
- The top CzcP quotation is a faithful compressed paraphrase of the inspected Summary; the anchor phrase is unverified in accessed passages. Neither observation establishes absence from every part of the paper.
- The definition review was assessed through its complete indexed abstract and primary journal identity. Its body was unavailable; the definition is a supported synthesis rather than a quoted formal class definition.
- BS1 MIC2.5mM and CH34 comparison3.5mM are assay/strain-specific inhibitory endpoints. The record already says MIC, so no growth-at-threshold falsehood is inferred.
- The UniProt audit failed because current entry versions differ from historical snapshots. For P13511, archived153/sequence3 is consistent and current154is later; no version-only scientific defect is introduced.
- All1130trait bytes were rechecked against the previous owned scientific snapshot before reusing the08:55corpus audits. Original times, scope and failures are retained.
- No matching Cupriavidus expression dataset was found in the inspected catalog; no organism substitution or negative functional inference followed.
- Human acceptance remains unknown outside the declared ignored-inclusive local search.
- No paid provider call, experimental optimization, scientific record edit, status/history change or generated-page mutation was performed.
- All field indices are zero-based.
- Native capture09:01:13–15Z retained55inputs after the complete target was read.
- A completed review records unresolved source checks honestly; it does not certify every mechanistic claim or confer human acceptance.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T090750Z-cadmium-tolerant
kind: record
repository: CultureBotAI/TraitMech
title: Evidence and grounding review of cadmium tolerance (traitmech:000013)
started_at: '2026-10-21T09:01:13Z'
finished_at: '2026-10-21T09:07:50Z'
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
summary: Cadmium tolerance has a justified fallback identity, supported strain examples
  and coherent chemical/protein identities. No major finding is established. Three
  minor findings concern broad transport grounding, provisionally unverified quotation
  fidelity and a bounded missing human-acceptance link. All eight nodes and seven
  edges were inspected, with four exact2023-review claims and remaining protein-anchor
  experimental provenance explicitly unresolved because full text was unavailable.
  The failed UniProt live-version check is retained alongside valid archived metadata.
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
  - path: data/traits/environment/cadmium_tolerant.yaml
    sha256: 219579b7eab2bfdb4787cb3f168f0492fbc5b951f69ffe70d1c6ffdb51683c5b
    role: target
  - path: data/traits/environment/metal_tolerant.yaml
    sha256: 907f78048e48c547d03e3b2b073216a32007a0c0608fb361fba976a3812710c5
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
  - path: research/traits/environment/cadmium_tolerant-deep-research-falcon.md
    sha256: 628b8317475de5ec44061901b0ce34471382bba70008676cd3ec59df32b7bf44
    role: context
  - path: scripts/audit_causal_graphs.py
    sha256: e0c26506c9de712700317284f142097e7bf69334806b8010db5d6517e905e834
    role: context
  - path: scripts/audit_graph_protein_taxa.py
    sha256: d3375861829c612483b3545dd0f5e2b79872a4576b626edc08714a09fbd9a24d
    role: context
  - path: scripts/audit_uniprot_grounding.py
    sha256: 91eb2165c69b3a4fcb53154dc8c835ac1070577f88065a43dfc881284d3d1052
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
- target_id: traitmech:000013
  path: data/traits/environment/cadmium_tolerant.yaml
  label: cadmium tolerant
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/cadmium_tolerant.yaml
    role: Maintained TraitRecord; scientific changes require guarded curation
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: METPO-first identifier comparison; target was curator proposed
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Seventh batch004 target in lexicographic path order. Entire target read
    before native capture; eight nodes, seven edges, both canonical organisms and
    the single protein example are included.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000013
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000013
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
  - traitmech:000013
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
  - traitmech:000013
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
  - traitmech:000013
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
  - traitmech:000013
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
  - traitmech:000013
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
  - traitmech:000013
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
- check_id: cadmium_tolerant-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000013
  command: just validate data/traits/environment/cadmium_tolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Selected record validates.
  evidence_ids:
  - check-cadmium_tolerant-validate
- check_id: cadmium_tolerant-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000013
  command: just validate-strict data/traits/environment/cadmium_tolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero strict errors.
  evidence_ids:
  - check-cadmium_tolerant-strict
- check_id: cadmium_tolerant-snippets
  name: Focused abstract snippet check
  status: passed
  required: true
  target_ids:
  - traitmech:000013
  command: just verify-snippets --record data/traits/environment/cadmium_tolerant.yaml
    --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/cadmium_tolerant-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Three snippets across two references are NOT_IN_ABSTRACT. These misses
    are inconclusive; manual source verification and limitations are reported separately.
  evidence_ids:
  - check-cadmium_tolerant-snippets
- check_id: corpus-protein-taxa
  name: Native full-corpus protein/taxon coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000013
  command: just audit-graph-protein-taxa --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Reused actual08:55:04–10Z execution:719graphs,129PASS,589NONMECHANISTIC,onePROTECTED,zero
    gaps/errors. TargetPASS has three label-only proteins, two cited canonical examples
    and one taxon-paired example. This is structural coverage, not source verification.
  evidence_ids:
  - check-corpus-protein-taxa
- check_id: corpus-uniprot
  name: Native full-corpus live UniProt audit
  status: failed
  required: true
  target_ids:
  - traitmech:000013
  command: just audit-uniprot --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-uniprot.tsv
  exit_code: 1
  expected_exit_code: 0
  summary: Reused actual08:55:08–08:56:53Z execution:exit1,146uses/115accessions,110findings
    all ENTRY_VERSION_MISMATCH. P13511 matches primary accession, taxon, review status,
    sequence3 and proteome; stored153 versus current154 is the only target finding.
    Historical153 is assessed separately.
  evidence_ids:
  - check-corpus-uniprot
- check_id: structured-source-runner
  name: Structured-source runner discovery
  status: unavailable
  required: false
  target_ids:
  - traitmech:000013
  summary: Original bounded discovery reused; official catalog fallback inspected.
  evidence_ids:
  - runner
- check_id: expression-context
  name: Canonical-organism dataset applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000013
  summary: No canonical Cupriavidus dataset matches; no organism substitution or expression
    queries.
  evidence_ids:
  - expression
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-cadmium_tolerant-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/cadmium_tolerant-validate.log
  locator: Executed 2026-10-21T09:01:38Z through 2026-10-21T09:01:42Z; metadata cadmium_tolerant-validate.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: Selected record validates.
  snapshot_sha256: 3d952a930424483916b1a0f8f5e3b9347adcb63e28eff0e147d0592dd53eedc1
- evidence_id: check-cadmium_tolerant-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/cadmium_tolerant-strict.log
  locator: Executed 2026-10-21T09:01:38Z through 2026-10-21T09:01:42Z; metadata cadmium_tolerant-strict.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: One file scanned; zero strict errors.
  snapshot_sha256: 3620a84ae01a4ae7617c01cb11e454afab53a13b90fdc7ddc92a05a72868a923
- evidence_id: check-cadmium_tolerant-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/cadmium_tolerant-snippets.log
  locator: Executed 2026-10-21T09:01:41Z through 2026-10-21T09:01:45Z; metadata cadmium_tolerant-snippets.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: Three snippets across two references are NOT_IN_ABSTRACT. These misses
    are inconclusive; manual source verification and limitations are reported separately.
  snapshot_sha256: 60bf68a403925cad465e6a02ae53f3cfed40ae8f3590b3a1d577b8dde6fe6f2b
- evidence_id: check-corpus-protein-taxa
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log
  locator: Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: Reused actual08:55:04–10Z execution:719graphs,129PASS,589NONMECHANISTIC,onePROTECTED,zero
    gaps/errors. TargetPASS has three label-only proteins, two cited canonical examples
    and one taxon-paired example. This is structural coverage, not source verification.
  snapshot_sha256: f5f1a6be7789f2b3e487fcbc354361f8f1f0d0d0f90a9ba59864d26ed7ac49ef
- evidence_id: check-corpus-uniprot
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-uniprot.log
  locator: Executed 2026-10-21T08:55:08Z through 2026-10-21T08:56:53Z; metadata corpus-uniprot.json
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: Reused actual08:55:08–08:56:53Z execution:exit1,146uses/115accessions,110findings
    all ENTRY_VERSION_MISMATCH. P13511 matches primary accession, taxon, review status,
    sequence3 and proteome; stored153 versus current154 is the only target finding.
    Historical153 is assessed separately.
  snapshot_sha256: 6ad9ec31ef33837fb5f0d72d8c306af0ec862745d08c88240437e2e5012607b6
- evidence_id: check-reuse
  kind: validation
  reference: Scientific snapshot comparison before audit reuse
  locator: All1130trait files plus native audit implementations
  accessed_at: '2026-10-21T09:04:06Z'
  support: supports
  summary: All trait bytes match the previous owned scientific snapshot; the target
    hash agrees with its native capture. Original full-corpus executions are reused
    with actual scope and failures, not relabelled as new focused checks.
  snapshot_sha256: 5b7e6da9aec165f896b02b3f904bcec8172c6e0b018f8fe00541f99fc6d6f0d1
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/cadmium_tolerant.yaml
  locator: Entire identity, evidence, graph, protein example and eight events
  accessed_at: '2026-10-21T09:07:50Z'
  support: partial
  summary: The target describes environmental cadmium tolerance with a scoped CzcCBA/CzcP
    aggregate and a specifically labelled CzcA component example. Component, aggregate
    and transport-route claims must remain distinguishable.
  snapshot_sha256: 219579b7eab2bfdb4787cb3f168f0492fbc5b951f69ffe70d1c6ffdb51683c5b
- evidence_id: shape
  kind: validation
  reference: Whole graph/history inspection
  locator: Eight nodes, seven edges and eight AI-assisted events
  accessed_at: '2026-10-21T09:01:43Z'
  support: supports
  summary: All endpoints resolve; one protein instance is present and no pathway-context
    link is asserted. All eight events explicitly disclose AI assistance.
  snapshot_sha256: 42abc41603d2928f46ee2a837e6f1612c1f4507653e9f292b9628a264100e352
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml
  locator: Family/aggregate versus taxon-paired component; retrieval-time versions
  accessed_at: '2026-10-21T09:07:50Z'
  support: supports
  summary: Reviewed label-only aggregates can retain scoped protein instances. An
    explicitly identified component is not automatically an erroneous whole-complex
    identifier. Entry/sequence versions describe retrieval-time snapshots; current
    version drift must be distinguished from historical error.
- evidence_id: identity
  kind: authority
  reference: Pinned data/raw/metpo.owl; v5 proposal class table; parent metal_tolerant.yaml
  locator: Complete METPO search, fallback and broader parent
  accessed_at: '2026-10-21T09:07:50Z'
  support: supports
  summary: The pinned ontology contains no active exact cadmium-tolerance term; the
    local v5 proposal remains a proposal rather than an upstream minted identity.
    The accepted traitmech fallback and broader metal/metalloid-tolerance parent fit.
  snapshot_sha256: d9e99ebb4cd8c74029e0dca024f8abdb1daa4ae7abd72493e3f5d4d7ab02b0eb
- evidence_id: grounding
  kind: authority
  reference: Official ChEBI48775/29105; QuickGO GO0030001; NCBI119219/266264
  locator: Fresh chemical identities09:02:07–09Z; hash-verified GO/taxonomy originals08:54:06–07Z
  accessed_at: '2026-10-21T09:03:33Z'
  support: partial
  summary: 'Cadmium(2+) and zinc(2+) labels agree with their ChEBI terms. GO0030001
    is valid general metal-ion transport: a true broader context for cadmium transport,
    but it lacks cadmium specificity and outward direction. Taxon identities match.'
  snapshot_sha256: e1d44bc110a79e9325b37b60e5f09f17cdb8a5135fd9efebef675751b1fc432e
- evidence_id: protein
  kind: database
  reference: UniProtKB:P13511; UniSave version153; UP000002429
  locator: Current and archived CzcA identity plus reference proteome
  accessed_at: '2026-10-21T09:03:33Z'
  support: supports
  summary: P13511 is primary reviewed CzcA/Rmet5980 in CH34 with the stated reference
    proteome. Archived153/sequence3 is consistent with the declared2026-08-25 snapshot;
    current154 is a later update. Neither review status nor a current version difference
    substitutes for primary mechanism evidence.
  snapshot_sha256: ece6609ab06f57a2babe0a11a85b38b4a5ece2cd41a22ef3de66ef2e53a79a0a
- evidence_id: ledger
  kind: validation
  reference: Independent complete node/edge ledger
  locator: Eight nodes, seven edges, one instance
  accessed_at: '2026-10-21T09:03:33Z'
  support: partial
  summary: No formal current relation-role conflict was confirmed. The instance role
    expressly identifies CzcA as a component of a broader CzcCBA/CzcP aggregate. GO
    precision is a bounded concern; exact biological source scope is assessed separately.
  snapshot_sha256: 377ccb1bcec64d2b03eaf6585e39596241c6aa35b014da21ced0a873706c25b1
- evidence_id: owners
  kind: search
  reference: mappings,scripts,src,proposals; scripts/ground_causal_nodes.py
  locator: Ignored-inclusive exact-label/identifier writer search
  accessed_at: '2026-10-21T09:07:50Z'
  support: context_only
  summary: No dedicated current literal mapping/writer reference for the target groundings
    was identified within the declared bounds. The node writer skips populated IDs;
    there is no evidence that clearing a value would automatically recreate this broad
    grounding. Historical ownership outside the search remains unknown.
  snapshot_sha256: 5f395152fbe79642e47931a89e4b822dcfc26864f1c4e1f9c81470b8848b9a3f
  search_scope: Exact ignored-inclusive search commands and bounded mappings/scripts/src/proposals
    roots are recorded in the receipt. No historical or whole-filesystem absence is
    asserted.
- evidence_id: provenance
  kind: search
  reference: Whole target history and bounded local history/mapping/writer/review
    search
  locator: Eight AI events and268ignored-inclusive matching lines
  accessed_at: '2026-10-21T09:01:43Z'
  support: partial
  summary: All eight events explicitly disclose AI assistance. Prior-review matches
    are contextual input references, not target coverage or human acceptance. No acceptance
    link identifying this revision was found within the inspected local bounds; remote/private
    acceptance remains unknown.
  snapshot_sha256: 2bf82be58d15ab617f098440be6485160aaa08e189072f2ba84036dcf0c21409
  search_scope: rg --no-ignore --hidden over history,mappings,scripts,reviews/structured
    using exact traitmech000013, record path and cadmium_tolerant/cadmium tolerant.
    Exact command and268matching lines retained; all67matching review target lists
    were independently checked.
- evidence_id: status-rule
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md
  locator: Status/audit gate
  accessed_at: '2026-10-21T09:07:50Z'
  support: supports
  summary: REVIEWED requires human scientific acceptance, distinct from AI history,
    mapping decisions and validation.
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Original07:36:12Z catalog; hash-verified current applicability assessment
  accessed_at: '2026-10-21T09:03:19Z'
  support: context_only
  summary: No Cupriavidus/metallidurans/CH34/BS1 dataset matches the inspected catalog.
    No species was substituted and no gene/module query was warranted. Noncoverage
    is not evidence against protein function or cadmium tolerance.
  snapshot_sha256: f3b269c7df68eb74b21636374b1e827ef8e98f8cc4ff746cbb09449e898b6228
- evidence_id: runner
  kind: search
  reference: Structured-source runner discovery
  locator: Original bounded ignored-inclusive08:17:15Z discovery
  accessed_at: '2026-10-21T08:17:15Z'
  support: context_only
  summary: The original runner search is reused with its exact bounds and official-catalog
    fallback. This is not a fresh or global absence claim.
  snapshot_sha256: 39b52930f52e898f85ac3bbb88f11ac674a355967b5704e2b62f0bda259d404f
  search_scope: Original PATH/project/install/B4 bounds include hidden/ignored and
    virtual-environment contents, excluding Git internals; unsearched directories
    remain unknown.
- evidence_id: bibliography
  kind: database
  reference: Complete primary-source claim and acquisition ledger
  locator: Five references, thirteen citation placements and three snippets
  accessed_at: '2026-10-21T09:07:50Z'
  support: partial
  summary: All five identities resolve. Two complete primary XMLs were reused with
    verified hashes; the CzcP publisher Summary/Introduction was actually inspected.
    Definition and2023review remain abstract-limited. Ten download attempts yielded
    three usable hashed metadata responses and one hashed nonarticle BioC error response;
    that HTTP200 help page is excluded from source evidence.
  snapshot_sha256: 75b062cc295db96818ffd19c6dc651f792b9b763551bbd5edf47fef3dff1bc3a
- evidence_id: definition-source
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/12829273/
  locator: DOI10.1016/s0168-6445(03)00048-2; complete indexed abstract, primary issue
    TOC208–216
  accessed_at: '2026-10-21T09:01:42Z'
  support: supports
  summary: The review supports layered efflux-mediated prokaryotic metal resistance.
    It supplies broad mechanism context rather than a formal cadmium growth threshold.
    The definition is a synthesis, with the record’s primary strain sources supplying
    cadmium phenotype support. Body access was unavailable.
  snapshot_sha256: ab66a791a5245cbb2bd7274916dba2349cf69ed1b105f965af95e8f3d6279302
- evidence_id: czcp
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2009.06792.x
  locator: PMID19602147; successful publisher Summary80–82, Introduction87–90/93/102–105
  accessed_at: '2026-10-21T09:02:00Z'
  support: partial
  summary: The study supports CzcP metal export and explicitly discusses CzcA as an
    inner-membrane CzcCBA component. Its title does not make it a wrong CzcA citation.
    The top snippet substitutes CzcP for the source’s anaphoric subject and is a faithful
    compressed paraphrase of the inspected Summary. The anchor phrase remains unverified
    in the accessed passages. No whole-body absence is claimed.
- evidence_id: sequestration-source
  kind: primary_source
  reference: https://doi.org/10.1007/s40201-023-00887-6
  locator: PMID38887775, PMC11180082; indexed abstract and publisher preview42–48
  accessed_at: '2026-10-21T09:01:42Z'
  support: partial
  summary: The review broadly covers microbial cadmium sequestration and efflux. Its
    abstract does not verify the four precise existing claims on metallothionein binding/free-pool
    change, CadA compartment detail and zinc cross-induction. Failed full-text access
    leaves those claims unknown, not false or absent from the source.
  snapshot_sha256: c5f53cf45e3e76735cfe589fcedceed5f9d51840f0eaba27cf0ffc555d70f291
- evidence_id: bs1
  kind: primary_source
  reference: https://doi.org/10.3389/fmicb.2020.00047
  locator: PMID32117100, PMC7019866; ResultsS3.SS1/body11 and Table1
  accessed_at: '2026-10-21T08:55:31Z'
  support: supports
  summary: BS1 cadmium MIC2.5mM is exact under the reported assay; CH34 comparison
    is3.5mM. The long quote matches apart from harmless uM/μM typography. MIC is an
    inhibitory endpoint and the record already labels it as such; no unsupported growth-at-MIC
    or universal species threshold is inferred.
  snapshot_sha256: 64d52eb8778d5b00a469f8d82deeeeb5d3a0102de2faa89badc5d55f7e72db81
- evidence_id: ch34
  kind: primary_source
  reference: https://doi.org/10.1371/journal.pone.0010433
  locator: PMID20463976, PMC2864759; Introductionbody3, Resultss2f/body53–54, Table5czc
    row
  accessed_at: '2026-10-21T08:55:43Z'
  support: supports
  summary: The primary genome article directly describes CH34 cadmium resistance,
    CzcCBA/CzcA function and a locus combining CzcCBA,CzcD,CzcP for detoxification.
    Its transenvelope account differs from the2009 paper’s compartment framing. Preserve
    those source distinctions and the record’s explicit aggregate/component roles
    rather than asserting a universal contradiction.
  snapshot_sha256: bc3ff60f3133a5ec3ac949d7f319d52401370ffaa038d9c498d330529cccd821
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: fallback, term kind, polarity and hierarchy'
  outcome: supported
  target_ids:
  - traitmech:000013
  summary: The accepted fallback is justified against the complete pinned ontology
    scan; its local proposal is not an upstream minted identity. Cadmium tolerance
    is a narrower positive environmental class under metal/metalloid tolerance.
  evidence_ids:
  - identity
  - record
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: growth phenotype and typical efflux emphasis'
  outcome: supported
  target_ids:
  - traitmech:000013
  summary: The definition is a reasonable synthesis of the broad resistance review
    and cadmium-specific primary phenotype evidence. It does not require a universal
    czc system or assert a numerical growth cutoff.
  evidence_ids:
  - definition-source
  - bs1
  - ch34
  - record
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: both canonical examples and CzcA component'
  outcome: supported
  target_ids:
  - traitmech:000013
  summary: Current taxon identities and CH34 cadmium-resistance context agree. P13511
    identifies the declared reviewed inner-membrane component, and both the cited
    CzcP paper and CH34 source discuss CzcA. A component explicitly placed within
    the aggregate is not automatically a whole-complex error.
  evidence_ids:
  - grounding
  - protein
  - czcp
  - ch34
  - policy
- assessment_id: model
  area: representation
  topic: 'Native checklist: scoped mechanistic graph and experimental provenance'
  outcome: unknown
  target_ids:
  - traitmech:000013
  summary: ENVIRONMENT/CLASS and the explicit aggregate/component representation fit.
    Native protein/taxon coverage passes. Specific P13511 experimental provenance
    in the attached2009 article was not fully assessed because only Summary/Introduction
    were accessible; positive role support exists, so limited access does not establish
    an unsupported-anchor defect.
  evidence_ids:
  - record
  - policy
  - protein
  - czcp
  - ch34
  - check-corpus-protein-taxa
- assessment_id: grounding
  area: grounding
  topic: 'Native checklist: all identifiers and transport specificity'
  outcome: concern
  target_ids:
  - traitmech:000013
  summary: Both chemical identities, taxonomy and the protein instance match. GO0030001
    is a legitimate broad metal-transport concept but does not encode the exact cadmium/outward-transmembrane
    meaning of node3. This is bounded precision rather than wrong ion identity or
    an invalid process aspect.
  evidence_ids:
  - grounding
  - ledger
  - owners
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all seven edge roles and directions'
  outcome: supported
  target_ids:
  - traitmech:000013
  summary: Current executor/process and challenge/mitigation endpoint roles are compatible.
    The zinc induces label explicitly concerns expression and need not carry an invented
    predicate ID. Compartment interpretation is kept at the component/aggregate level
    with source differences retained.
  evidence_ids:
  - ledger
  - record
  - czcp
  - ch34
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: five references, three snippets and seven nearest claims'
  outcome: unknown
  target_ids:
  - traitmech:000013
  summary: The efflux/challenge claims have inspected support. Four2023-review-dependent
    claims remain unverified at their exact source because body access failed. One
    long snippet matches with typography normalization; top CzcP wording is a faithful
    compressed paraphrase and anchor exactness is unverified in inspected passages.
  evidence_ids:
  - bibliography
  - czcp
  - sequestration-source
  - bs1
  - ch34
- assessment_id: protein-history
  area: provenance
  topic: 'Native checklist: historical version and later live-audit drift'
  outcome: supported
  target_ids:
  - traitmech:000013
  summary: Archived153/sequence3 matches the recorded snapshot; current154 is later.
    The native audit’s freshness failure is retained, while identity, taxon, review
    status and proteome remain correct. The past retrieval itself was not independently
    re-observed.
  evidence_ids:
  - protein
  - policy
  - check-corpus-uniprot
  - check-reuse
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: required shape and optional discussions/datasets'
  outcome: supported
  target_ids:
  - traitmech:000013
  summary: All endpoints resolve and the scoped graph carries one structurally valid
    paired protein example. Additional instances or expression datasets are not automatically
    required for every contextual branch. Existing provider research remains a lead
    rather than primary evidence.
  evidence_ids:
  - shape
  - record
  - policy
  - check-corpus-protein-taxa
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: canonical-taxon structured-source applicability'
  outcome: supported
  target_ids:
  - traitmech:000013
  summary: No matching Cupriavidus dataset occurs in the inspected catalog. No gene/module
    searches or taxon substitution followed, and noncoverage supplies no negative
    biology.
  evidence_ids:
  - expression
  - runner
- assessment_id: audit
  area: provenance
  topic: 'Native checklist: AI disclosure, acceptance and maintained owners'
  outcome: concern
  target_ids:
  - traitmech:000013
  summary: Eight events disclose AI assistance. No human-acceptance link was found
    within bounded local provenance. Current literal owner searches do not establish
    that the broad GO grounding would recur from the maintained mapping.
  evidence_ids:
  - provenance
  - status-rule
  - shape
  - owners
findings:
- finding_id: transport-grounding-specificity
  issue_key: cadmium-tolerant-transport-grounding-specificity
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The transport grounding is broader than the stated process
  description: Node3 names cadmium ion transmembrane export but GO0030001 denotes
    general metal-ion transport. That is a genuine broad context for the process,
    yet it does not establish cadmium specificity or outward direction as an exact
    grounding. Clarify the relationship or use an exact supported term; no wrong chemical
    identity or formal type exclusion is asserted.
  target_ids:
  - traitmech:000013
  field_paths:
  - causal_graphs[0].nodes[3]
  evidence_ids:
  - grounding
  - ledger
  - owners
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/cadmium_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: quotation-fidelity
  issue_key: cadmium-tolerant-quotation-fidelity
  category: evidence
  severity: minor
  status: open
  certainty: provisional
  title: Two CzcP-source snippets need verbatim verification
  description: The top snippet is a faithful subject-substituted paraphrase of the
    inspected Summary, and the protein-anchor phrase was not verified in the accessed
    Summary/Introduction. Verify an exact passage or move interpretive wording into
    notes. The full2009body was not exhaustively inspected, so this is a provisional
    quotation concern rather than confirmed absence from the whole article.
  target_ids:
  - traitmech:000013
  field_paths:
  - evidence[0].snippet
  - causal_graphs[0].nodes[2].protein_examples[0].evidence[0].snippet
  evidence_ids:
  - czcp
  - bibliography
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/cadmium_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: cadmium-tolerant-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human scientific acceptance is not linked locally
  description: The eight disclosed AI events, including status promotion, and ignored-inclusive
    local review/history search do not identify human scientific acceptance of this
    revision. Prior reviews reference the file as context, not as their target. Remote
    or private acceptance remains unknown.
  target_ids:
  - traitmech:000013
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - status-rule
  - shape
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/cadmium_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: clarify-transport-grounding
  description: In separately authorized curation, reconcile node3’s exact process
    wording with the breadth of its grounding.
  finding_ids:
  - transport-grounding-specificity
  target_ids:
  - traitmech:000013
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/cadmium_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The selected identifier and intended transport specificity/direction agree, or
    the broader relationship is explicitly represented without claiming exact identity.
  - Do not invent a replacement accession or treat broad metal-ion transport as a
    wrong biological-process type.
  - The current writer skips populated IDs; use guarded correction and run focused
    strict/term/graph checks and just qc, with native history and affected generated
    products after authorized edits.
- action_id: verify-snippets
  description: Verify exact CzcP-paper passages for both snippets or move faithful
    paraphrase into notes.
  finding_ids:
  - quotation-fidelity
  target_ids:
  - traitmech:000013
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/cadmium_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retained quotation text has a precise inspected source location.
  - Keep supported transport and CzcA background claims; source-access limits alone
    do not establish false biology.
  - Run focused snippet verification and manual primary-text checking after authorized
    changes.
- action_id: link-acceptance
  description: Locate and link existing human acceptance or obtain it through the
    established process, preserving AI history and reassessing status if necessary.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - traitmech:000013
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/cadmium_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies the revision and scientific scope.
  - Automated coverage, AI provenance and this review are not substituted for human
    scientific acceptance.
- action_id: resolve-source-limits
  description: When full source text becomes available, assess the four2023-review
    claims and the remaining2009 experimental-anchor provenance at their exact passages
    before strengthening the verdict.
  finding_ids: []
  target_ids:
  - traitmech:000013
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/cadmium_tolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Record support, qualification or contradiction separately for edges3–6 and the
    P13511 anchor.
  - Preserve current unknowns until actual source text is inspected; HTTP200 help/error
    content is excluded.
  - No experimental design or expanded mechanism is needed for this documentary follow-up.
limitations:
- The2023cadmium-review body was unavailable after finite primary/PMC/BioC/PDF attempts.
  A single delayed BioC retry returnedHTTP200 API error/help, not article content.
  Edges3–6 remain unverified at their nearest cited source, not demonstrated false
  or absent from the paper.
- CzcP2009 publisher Summary/Introduction were successfully inspected before later403responses.
  No local full-text hash is fabricated, and the complete results/discussion were
  not assessed.
- The attached CzcP paper explicitly discusses CzcA; its title alone does not make
  the reference wrong. Known reviewed protein-level support and component role are
  positive evidence, while exact experimental provenance in that attached paper remains
  partly unassessed.
- Source compartment framings differ:2009 distinguishes RND periplasmic export from
  ATPase cytoplasmic export, whereas2010 describes a transenvelope route and a combined
  locus. The record’s aggregate includes both; no universal compartment contradiction
  is asserted.
- The top CzcP quotation is a faithful compressed paraphrase of the inspected Summary;
  the anchor phrase is unverified in accessed passages. Neither observation establishes
  absence from every part of the paper.
- The definition review was assessed through its complete indexed abstract and primary
  journal identity. Its body was unavailable; the definition is a supported synthesis
  rather than a quoted formal class definition.
- BS1 MIC2.5mM and CH34 comparison3.5mM are assay/strain-specific inhibitory endpoints.
  The record already says MIC, so no growth-at-threshold falsehood is inferred.
- The UniProt audit failed because current entry versions differ from historical snapshots.
  For P13511, archived153/sequence3 is consistent and current154is later; no version-only
  scientific defect is introduced.
- All1130trait bytes were rechecked against the previous owned scientific snapshot
  before reusing the08:55corpus audits. Original times, scope and failures are retained.
- No matching Cupriavidus expression dataset was found in the inspected catalog; no
  organism substitution or negative functional inference followed.
- Human acceptance remains unknown outside the declared ignored-inclusive local search.
- No paid provider call, experimental optimization, scientific record edit, status/history
  change or generated-page mutation was performed.
notes:
- All field indices are zero-based.
- Native capture09:01:13–15Z retained55inputs after the complete target was read.
- A completed review records unresolved source checks honestly; it does not certify
  every mechanistic claim or confer human acceptance.
tags:
- record-review
- cadmium-tolerant
- environment
- needs-curation
```
