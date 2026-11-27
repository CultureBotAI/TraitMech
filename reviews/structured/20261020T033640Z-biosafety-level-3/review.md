# Scientific and source review of biosafety level 3 (METPO:1001104)

- Review: 20261020T033640Z-biosafety-level-3
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-19T23:41:16Z
- Finished UTC: 2026-10-20T03:36:40Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Identity and broader parent resolve. Four major findings concern classification evidence and scope, conflated verification claims, and an unsupported management-system outcome with mismatched predicate semantics. Four minor findings concern definition bearer, example citation context, node representation and quotation provenance. All 10 nodes, 8 edges, both examples and the discussion were assessed within the stated source-access limits.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Seventh previously uncovered record in lexicographic path order. Only this complete record is adjudicated; parent, ontology, proposals and writer inputs supply context.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f25e2af0b38a8303b13f627a9a5c33b36af4b3d2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1001104 | data/traits/ecology/biosafety_level_3.yaml | maintained | biosafety level 3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1001104 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1001104 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1001104 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1001104 | 1276 history records checked, zero invalid links; integrity does not establish scientific correctness or human sign-off. |
| Initial full-product validation | failed | False | METPO:1001104 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1001104 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1001104 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1001104 | Selected record validates; shape is independent of scientific support. |
| Focused strict closed-schema validation | passed | True | METPO:1001104 | One record scanned; zero error rows. |
| Focused source snippet verification | passed | True | METPO:1001104 | Three repeated Ag43 snippets returned NOT_IN_ABSTRACT. This does not establish full-text absence. |
| Expression-module applicability | not_applicable | False | METPO:1001104 | Administrative classification has no gene/protein instance or expression dataset. An expression module would not establish containment classification. |

## Scientific And Domain Assessments

### Native checklist: identity, synonyms and polarity

identity: supported. Targets: METPO:1001104.

The local BSL3 class is unambiguous; both numeric synonyms are related synonyms. Inherited wording has a bearer error but does not obscure which class is intended.

### Native checklist: definition and nearest support

evidence: concern. Targets: METPO:1001104.

A containment level cannot itself cause disease. The attached protein review does not supply the claimed classification support; contextual authority is needed.

### Native checklist: broader parent and subclass direction

consistency: supported. Targets: METPO:1001104.

The parent is broader and rdfs:subClassOf points in the correct direction. The hierarchy is supported by local ontology and classification context, while its attached Ag43 citation is misplaced.

### Native checklist: category, entities and conditions

representation: concern. Targets: METPO:1001104.

NONMECHANISTIC is appropriate. Hazard, environmental conditions, engineered controls and a management standard are not interchangeable entity types. Classification must retain work/authority context.

### Native checklist: taxon and study scope

evidence: unknown. Targets: METPO:1001104.

Species identifiers resolve. Both citations are strain-specific genome studies; available abstracts do not verify the example classification notes. The notes omit authority, edition and activity context.

### Native checklist: source identities, snippets and narrow support

evidence: concern. Targets: METPO:1001104.

All active reference identities and taxonomy identifiers were checked. Relevant full text was inspected for the readiness review and Morris communication; other limitations are explicit. Quoted notes include paraphrases rather than checked exact snippets.

### Native checklist: all nodes and eight edges

graph: concern. Targets: METPO:1001104.

All 10 nodes and 8 edges were assessed. The contextual management-system component is permitted in a NONMECHANISTIC graph. Findings concern claim support and semantics, not disconnectedness.

Zero-based edge ledger: 0 classification assigned as intrinsic biological realization, with misplaced citation; 1 valid broader relationship but misplaced citation; 2 hazard relevance recognizable, while a sufficient universal rule exceeds contextual authority; 3–4 qualitative controls and summaries appear in the cited review but need bounded source/authority context; 5 boundary verification has conditional support in the comparative study abstract; 6 test label and description conflict internally, with full-text terminology verification outstanding; 7 specific infection outcome is not established by the general management discussion, and the proposed predicate meaning does not fit. No operational parameter, procedure or test redesign is recommended.

### Native checklist: knowledge-gap premises and inference

consistency: concern. Targets: METPO:1001104.

Anchors resolve and historical snippets are correctly disclaimed. The active question inherits a conflated test label and an unsupported universal certification premise. A correlation involving one proxy cannot establish or invalidate an entire certification regime. No dataset is claimed.

### Native checklist: native status, history and checks

provenance: unknown. Targets: METPO:1001104.

Focused validation and applicable corpus diagnostics pass within their declared scope. AI assistance is disclosed; captured history does not independently prove human scientific sign-off for REVIEWED.

## Findings

### classification-citation: Protein review is misplaced as classification evidence

major / open / confirmed; issue key: biosafety-level-3-classification-citation.

The Ag43 article identity and inspected abstract do not support the definition or the two initial classification edges. A generic snippet cannot supply that missing support. This is a nearest-evidence mismatch, not an assertion that its unavailable full text contains no biosafety words.

### classification-scope: Hazard-to-classification language drops necessary context

major / open / confirmed; issue key: biosafety-level-3-classification-scope.

The graph treats agent properties as yielding a level and describes the parent as an agent hazard axis. BMBL and WHO distinguish contextual selection of controls from intrinsic hazard. The secondary readiness review cannot establish universal requirements merely by stating them categorically.

### verification-conflation: Test naming and certification inference are conflated

major / open / confirmed; issue key: biosafety-level-3-verification-conflation.

The node is named pressure decay but describes maintained steady pressure, and the discussion inherits that inconsistency. It then treats a particular test as a universal certification surrogate. The inspected comparative abstract does not establish that premise, and the proposed proxy conclusions exceed the asserted evidence.

### management-outcome: General safety discussion does not establish the infection outcome or predicate fit

major / open / confirmed; issue key: biosafety-level-3-management-outcome.

The final edge asserts an ISO35001-specific infection outcome. Its source discusses general safety performance; it does not establish that result. The proposed mitigates predicate concerns defense/homeostatic mechanisms, and its permissive type gate does not validate an organizational standard as such a mechanism.

### definition-bearer: Definition assigns disease causation to the containment level

minor / open / confirmed; issue key: biosafety-level-3-definition-bearer.

The definition makes the level itself the disease-causing entity. The wording is inherited verbatim from local METPO, so the correction should preserve and identify upstream provenance.

### example-context: Example classification notes lack directly verified contextual support

minor / open / confirmed; issue key: biosafety-level-3-example-context.

Both example notes are unqualified. The inspected genome-study abstracts do not substantiate those notes, and no classification passage or authority context is supplied. Full-paper support remains unresolved rather than refuted.

### node-representation: Some node types do not match their described entities

minor / open / confirmed; issue key: biosafety-level-3-node-representation.

The hazard node describes agent properties rather than a biological process. Control and management nodes use environmental-factor types despite describing engineered or organizational interventions. The intended entities need review under native containment-factor guidance.

### quotation-provenance: Quoted notes contain summaries without exact passage locators

minor / open / confirmed; issue key: biosafety-level-3-quotation-provenance.

Several edge notes present reconstructed wording in quotation marks. Comparison with the inspected readiness and Morris PDFs shows paraphrase rather than exact quotation. Bibliographic support and verbatim snippet provenance should remain distinct; boundary-paper quotations remain unverified.

## Recommended Actions And Acceptance Checks

### repair-classification-citations

Reassess and replace or remove unsupported attributions for retained classification claims.

- Inspect a suitable authority or documentary source and attach exact edition/section locators.
- Verify each claim independently; run focused validate, validate-strict and verify-snippets after authorized curation.

### retain-classification-context

Separate hazard description, laboratory/activity classification and source-specific summaries.

- Retained claims identify authority/edition and context without issuing handling requirements.
- Distinguish recommendations, review summaries and normative requirements.
- Use guarded curation/history and applicable strict, graph and qc checks after authorized changes.

### reconcile-verification-claims

Resolve the nomenclature against directly inspected source text and qualify the certification premise.

- Retain only source-supported test identity and conceptual scope; no replacement procedure is proposed here.
- Separate a measured proxy from a broader certification conclusion.
- Reconcile the maintained discussion PLAN and target; run strict and applicable qc after authorized curation.

### bound-management-relation

Remove or qualify the unsupported outcome and reassess predicate semantics for the intended organizational relation.

- Distinguish purpose, expectation and measured outcome.
- Do not broaden a shared predicate solely to make this edge pass.
- Inspect exact source support and run strict plus applicable graph/grounding checks after authorized correction.

### correct-bearer

Clarify which entity bears the hazard while preserving the classification identity.

- Avoid an automatic agent-to-level assignment rule.
- Preserve upstream provenance and run focused strict validation after authorized correction.

### verify-example-notes

Provide directly inspected, appropriately scoped documentary support or qualify the examples as unresolved.

- Retain species versus strain distinctions and relevant authority/activity context.
- Do not infer universal assignment from pathogenicity or taxon identity.
- Run focused reference and strict checks after authorized edits.

### review-node-types

Resolve intended entities before choosing native types or documenting a schema gap.

- Do not invent biological mechanisms or select merely adjacent ontology terms.
- Retain NONMECHANISTIC context and run strict plus graph/grounding checks after authorized changes.

### separate-quotes-and-notes

Use checked short verbatim snippets with locators, and retain interpretation as unquoted notes.

- Check actual source bytes; do not silently promote summaries or indexed excerpts to quotations.
- Preserve source-access limits and rerun verify-snippets plus strict validation after authorized edits.

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
| check-biosafety-level-3-validate | /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-3-validate.log; Executed 2026-10-20T03:29:08Z through 2026-10-20T03:29:09Z; metadata biosafety-level-3-validate.json | context_only | Selected record validates; shape is independent of scientific support. |
| check-biosafety-level-3-strict | /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-3-strict.log; Executed 2026-10-20T03:29:08Z through 2026-10-20T03:29:09Z; metadata biosafety-level-3-strict.json | context_only | One record scanned; zero error rows. |
| check-biosafety-level-3-snippets-network | /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-3-snippets-network.log; Executed 2026-10-20T03:29:10Z through 2026-10-20T03:29:12Z; metadata biosafety-level-3-snippets-network.json | context_only | Three repeated Ag43 snippets returned NOT_IN_ABSTRACT. This does not establish full-text absence. |
| record | data/traits/ecology/biosafety_level_3.yaml; Entire target, including 10 nodes, 8 edges, two examples and discussion | partial | Exact target read; local identity resolves but several evidence and representation claims need curation. |
| identity | data/raw/metpo.owl; METPO:1001104 and direct parent METPO:1001101; related numeric synonyms | supports | Identifier, label, definition and parent match the captured ontology. Ignored-inclusive corpus searches resolve one target, and exclusion-file searches found no direct target match. All graph endpoints and discussion anchors resolve. |
| model | src/traitmech/schema/traitmech.yaml; Node types; CURATION_PLAYBOOK containment-factor guidance; captured v8 confers and v2 mitigates proposals and predicate mapping | partial | Confers and mitigates are documented proposed placeholders, not subjects in the captured METPO release. Mitigates is defined for defense/homeostatic mechanisms, which does not establish an organizational-standard relation. Permissive type checks do not establish intended entity semantics. |
| owners | scripts/curate_knowledge_gaps.py; PLAN kgscan-2ee31ba13f9c and replay loop; captured source histories and guarded writer | context_only | Discussion replay overwrites authored fields and drops evidence. Future corrections must consider the maintained PLAN and record. Historical AI curation and seed provenance do not independently establish human sign-off. |
| bmbl | https://www.cdc.gov/covid/media/pdfs/2024/07/SF__19_308133-A_BMBL6_00-BOOK-WEB-final-3.pdf; Foreword printed p iii; Section II printed p11; Section III Biosafety Levels printed p27 (PDF page index54) | supports | Official PDF text. Four BSLs describe combinations of facilities, equipment, practices and PPE selected through facility-specific risk assessment; risk groups correlate but are not equivalent. BMBL is advisory rather than itself regulatory. Contextual laboratory containment classification, not an intrinsic microbial trait determined only by hazard. Does not establish absence of fifth-level proposals or levels in every national framework. |
| who | https://www.who.int/publications/i/item/9789240011311; Overview and Composition of the manual | supports | Official WHO overview says risk assessment permits controls appropriate to particular activities/circumstances and should precede activities. PDF on iris.who.int was inaccessible in this check. Risk-based contextual containment; does not establish intrinsic hazard-to-level equivalence. |
| ag43 | https://www.annualreviews.org/content/journals/10.1146/annurev.micro.62.081307.162938; Title, citation and abstract | refutes | van der Woude and Henderson, Regulation and Function of Ag43 (Flu), Annual Review of Microbiology 62:153–169 (2008), Review. Abstract concerns one E. coli surface protein; full text not accessible. Citation identity mismatch with claimed general virulence-factor review and inadequate inspected support for biosafety definition, tiers or mandates. |
| readiness | https://www.saudijmph.com/index.php/pub/article/download/115/91/172; Bawshkhah et al.; printed pp392–394; introduction, classification summary and facility-design section | partial | Publisher PDF identifies a review article in volume 1(1), pp392–399 (2024). It contains the qualitative control claims and numerical summaries paraphrased by the record. This is secondary literature, not an authoritative universal requirement or a primary efficacy measurement. Its categorical language must be distinguished from activity-specific authority guidance. |
| boundary | https://pubmed.ncbi.nlm.nih.gov/38434104/; Ziegler and Tremblay; DOI10.1089/apb.2023.0017; complete abstract and bibliographic metadata | partial | Applied Biosafety 29(1):10–18 (2024). Comparative guideline and facility-data study describes conditional applicability and proposes criteria where definitive guidance is lacking. It supports boundary testing in context, not universal certification or a particular equivalence between test labels. Publisher/PMC full text could not be directly retrieved; indexed search excerpts are leads only. |
| morris | https://ojs.wgtn.ac.nz/nzjhsp/article/download/9540/8453/15049; Emma Morris, Worth the risk?; DOI10.26686/nzjhsp.v1i2.9540; sections2.2–2.4 and conclusion | partial | Full five-page 2024 graduate communication discusses implementation, certification barriers and general safety performance. It provides no measured ISO35001-specific infection-reduction result. Its general claim cannot by itself establish the graph outcome. |
| iso | https://www.iso.org/standard/71293.html; Official ISO35001:2019 identity, abstract and edition metadata | supports | Official scope describes a biorisk-management process. Edition 1 is published, with a 2024 amendment and revision under development. Abstract/metadata only; paid standard text was not acquired. This verifies standard identity, not a measured infection outcome. |
| examples | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC%3AMED%20AND%20%28EXT_ID%3A9634230%20OR%20EXT_ID%3A11586360%29&amp;resultType=core&amp;format=json; Complete abstracts and bibliography for Cole1998 and Parkhill2001; Nature preview for DOI10.1038/31159 | partial | Both references resolve to primary genome papers about particular strains. Their inspected abstracts establish organism/study identity, not a BSL3 classification statement. Full text was unavailable, so absence of a classification passage from the complete papers is not asserted. |
| taxa | https://rest.uniprot.org/taxonomy/1773; Taxonomy1773 and 632 JSON records | supports | 1773 resolves to Mycobacterium tuberculosis and 632 to Yersinia pestis, both species. Taxon identity does not determine a laboratory classification. |
| historical | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC%3AMED%20AND%20%28EXT_ID%3A41494000%20OR%20EXT_ID%3A40514544%20OR%20EXT_ID%3A41552424%20OR%20EXT_ID%3A41917383%29&amp;resultType=core&amp;format=json; Four complete database abstracts and their retained discussion fragments | context_only | All four historical PMIDs resolve; the retained fragments are present in their abstracts. They concern different scientific questions and remain explicitly disclaimed as support for the active discussion. No pathogen mechanism from these papers is adjudicated or expanded. |

## Limits And Additional Notes

- Ag43 and both genome papers were assessed at abstract/preview level; complete-paper absence is not asserted.
- Boundary-study bibliography and complete abstract were inspected. Direct publisher retrieval failed, PMC returned a browser challenge, Europe PMC XML failed and BioC returned no result. Indexed full-text search excerpts were treated only as leads.
- The readiness review and Morris communication were inspected in publisher PDFs. Source fidelity does not establish every claim in a secondary article as independently true.
- ISO official abstract and edition metadata were inspected; paid standard text was not acquired. BMBL6 and WHO overview checks retain their original actual timestamps.
- No operational requirements, procedure changes, facility suitability, quantitative protection or pathogen mechanisms are evaluated or recommended. The existing proposed experiment is assessed only for evidentiary logic.
- Historical sign-off remains unresolved; corpus adapter skips and superseded diagnostic failures are retained.
- Review integration resumed after an interruption; the start and finish span the actual work interval.
- Only this new review bundle is written; no record, history, writer, ontology or generated page is changed.
- Original captured hashes were preserved. External access failures and successful fallbacks are distinguished.
- The isolated sweep began with 1130 record paths; this bundle has exactly one target and denominator 1.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T033640Z-biosafety-level-3
kind: record
repository: CultureBotAI/TraitMech
title: Scientific and source review of biosafety level 3 (METPO:1001104)
started_at: '2026-10-19T23:41:16Z'
finished_at: '2026-10-20T03:36:40Z'
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
summary: Identity and broader parent resolve. Four major findings concern classification
  evidence and scope, conflated verification claims, and an unsupported management-system
  outcome with mismatched predicate semantics. Four minor findings concern definition
  bearer, example citation context, node representation and quotation provenance.
  All 10 nodes, 8 edges, both examples and the discussion were assessed within the
  stated source-access limits.
source:
  git_revision: f25e2af0b38a8303b13f627a9a5c33b36af4b3d2
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
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
  - path: data/traits/ecology/biosafety_level.yaml
    sha256: 11d1e21fa511aedf4e453875ed0c2508b35e82d0e24399e9aa4aa5547c5aa39a
    role: context
  - path: data/traits/ecology/biosafety_level_3.yaml
    sha256: 0a0c3454b5eeae41f0e9f6c6202a22df48104afd6324897209ce3d908a475744
    role: target
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
  - path: history/README.md
    sha256: f795a191e17978454a8bb80da91ed6873a9405a240e6e5758837dd9bdc3b5c07
    role: context
  - path: history/infrastructure/curate-knowledge-gaps/2026-08-17T214933Z-claude-code-9c4af0.yaml
    sha256: a58b53be777e58ac29eb1c1571feb2593633c83d158aff4b6c96b8a1b9214c0f
    role: context
  - path: history/infrastructure/protein-taxon-event-backfill/2026-08-26T032525Z-claude-936bf3.yaml
    sha256: e32f537bb5192c12e9dae5f37ca07f71221402373551506429ce30445137fbab
    role: context
  - path: history/other/protein-taxon-review-tranche/2026-08-26T032524Z-codex-f46ce8.yaml
    sha256: dbd304ce7c2dfaf1525a12c1d5b4bf04a1ec66f00b92e4917d642c5fba6370fd
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
  - path: proposals/metpo_traitmech_v6/proposal.md
    sha256: aecbd48fd73712ccab57619d753b6084a7fa2fbf616f80623f63ce15b65871ae
    role: context
  - path: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
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
- target_id: METPO:1001104
  path: data/traits/ecology/biosafety_level_3.yaml
  label: biosafety level 3
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: maintained curated TraitRecord; use guarded writer for any authorized correction
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Seventh previously uncovered record in lexicographic path order. Only
    this complete record is adjudicated; parent, ontology, proposals and writer inputs
    supply context.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1001104
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1001104
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
  - METPO:1001104
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
  - METPO:1001104
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
  - METPO:1001104
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
  - METPO:1001104
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
  - METPO:1001104
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
  - METPO:1001104
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: biosafety-level-3-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1001104
  command: just validate data/traits/ecology/biosafety_level_3.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Selected record validates; shape is independent of scientific support.
  evidence_ids:
  - check-biosafety-level-3-validate
- check_id: biosafety-level-3-strict
  name: Focused strict closed-schema validation
  status: passed
  required: true
  target_ids:
  - METPO:1001104
  command: just validate-strict data/traits/ecology/biosafety_level_3.yaml --out /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-3-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: One record scanned; zero error rows.
  evidence_ids:
  - check-biosafety-level-3-strict
- check_id: biosafety-level-3-snippets-network
  name: Focused source snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1001104
  command: just verify-snippets --record data/traits/ecology/biosafety_level_3.yaml
    --out /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-3-snippets-network.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Three repeated Ag43 snippets returned NOT_IN_ABSTRACT. This does not establish
    full-text absence.
  evidence_ids:
  - check-biosafety-level-3-snippets-network
- check_id: expression-applicability
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1001104
  summary: Administrative classification has no gene/protein instance or expression
    dataset. An expression module would not establish containment classification.
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-20T03:36:40Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-20T03:36:40Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-20T03:36:40Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; metadata validate-history.json
  accessed_at: '2026-10-20T03:36:40Z'
  support: context_only
  summary: 1276 history records checked, zero invalid links; integrity does not establish
    scientific correctness or human sign-off.
  snapshot_sha256: 1fc48f1203fbfcd27b1243e4e147afb367aebfc592b496b352201058c6ee85d2
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-20T03:36:40Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-20T03:36:40Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-20T03:36:40Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-biosafety-level-3-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-3-validate.log
  locator: Executed 2026-10-20T03:29:08Z through 2026-10-20T03:29:09Z; metadata biosafety-level-3-validate.json
  accessed_at: '2026-10-20T03:36:40Z'
  support: context_only
  summary: Selected record validates; shape is independent of scientific support.
  snapshot_sha256: 516cba5225898ccf6fb33563be37637a347468c39d535b5424d6d98fbeb611bc
- evidence_id: check-biosafety-level-3-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-3-strict.log
  locator: Executed 2026-10-20T03:29:08Z through 2026-10-20T03:29:09Z; metadata biosafety-level-3-strict.json
  accessed_at: '2026-10-20T03:36:40Z'
  support: context_only
  summary: One record scanned; zero error rows.
  snapshot_sha256: 65ac7eb35cdb9e844e45e956da54044bf882b99f85c0e60906ac51ae46bdaf51
- evidence_id: check-biosafety-level-3-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-3-snippets-network.log
  locator: Executed 2026-10-20T03:29:10Z through 2026-10-20T03:29:12Z; metadata biosafety-level-3-snippets-network.json
  accessed_at: '2026-10-20T03:36:40Z'
  support: context_only
  summary: Three repeated Ag43 snippets returned NOT_IN_ABSTRACT. This does not establish
    full-text absence.
  snapshot_sha256: b79991dcd9fd0fb527d91a941965bed79e512934ee9631197f128faa8cb2703d
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/biosafety_level_3.yaml
  locator: Entire target, including 10 nodes, 8 edges, two examples and discussion
  accessed_at: '2026-10-20T03:36:40Z'
  support: partial
  summary: Exact target read; local identity resolves but several evidence and representation
    claims need curation.
  snapshot_sha256: 0a0c3454b5eeae41f0e9f6c6202a22df48104afd6324897209ce3d908a475744
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl
  locator: METPO:1001104 and direct parent METPO:1001101; related numeric synonyms
  accessed_at: '2026-10-19T23:41:35Z'
  support: supports
  summary: Identifier, label, definition and parent match the captured ontology. Ignored-inclusive
    corpus searches resolve one target, and exclusion-file searches found no direct
    target match. All graph endpoints and discussion anchors resolve.
  snapshot_sha256: 9caef2dc72b05d01546c03e5777f2a1e7a4c008eea0a707f55804b8dfa074f27
- evidence_id: model
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Node types; CURATION_PLAYBOOK containment-factor guidance; captured v8
    confers and v2 mitigates proposals and predicate mapping
  accessed_at: '2026-10-20T03:36:40Z'
  support: partial
  summary: Confers and mitigates are documented proposed placeholders, not subjects
    in the captured METPO release. Mitigates is defined for defense/homeostatic mechanisms,
    which does not establish an organizational-standard relation. Permissive type
    checks do not establish intended entity semantics.
- evidence_id: owners
  kind: record_content
  reference: scripts/curate_knowledge_gaps.py
  locator: PLAN kgscan-2ee31ba13f9c and replay loop; captured source histories and
    guarded writer
  accessed_at: '2026-10-19T23:42:16Z'
  support: context_only
  summary: Discussion replay overwrites authored fields and drops evidence. Future
    corrections must consider the maintained PLAN and record. Historical AI curation
    and seed provenance do not independently establish human sign-off.
  snapshot_sha256: ee318a8f4ca5e18318c7274338939cd68bb863a211d9938252b177627746058f
- evidence_id: bmbl
  kind: authority
  reference: https://www.cdc.gov/covid/media/pdfs/2024/07/SF__19_308133-A_BMBL6_00-BOOK-WEB-final-3.pdf
  locator: Foreword printed p iii; Section II printed p11; Section III Biosafety Levels
    printed p27 (PDF page index54)
  accessed_at: '2026-10-19T23:34:20Z'
  support: supports
  summary: Official PDF text. Four BSLs describe combinations of facilities, equipment,
    practices and PPE selected through facility-specific risk assessment; risk groups
    correlate but are not equivalent. BMBL is advisory rather than itself regulatory.
    Contextual laboratory containment classification, not an intrinsic microbial trait
    determined only by hazard. Does not establish absence of fifth-level proposals
    or levels in every national framework.
- evidence_id: who
  kind: authority
  reference: https://www.who.int/publications/i/item/9789240011311
  locator: Overview and Composition of the manual
  accessed_at: '2026-10-19T23:35:15Z'
  support: supports
  summary: Official WHO overview says risk assessment permits controls appropriate
    to particular activities/circumstances and should precede activities. PDF on iris.who.int
    was inaccessible in this check. Risk-based contextual containment; does not establish
    intrinsic hazard-to-level equivalence.
- evidence_id: ag43
  kind: primary_source
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev.micro.62.081307.162938
  locator: Title, citation and abstract
  accessed_at: '2026-10-19T23:34:48Z'
  support: refutes
  summary: van der Woude and Henderson, Regulation and Function of Ag43 (Flu), Annual
    Review of Microbiology 62:153–169 (2008), Review. Abstract concerns one E. coli
    surface protein; full text not accessible. Citation identity mismatch with claimed
    general virulence-factor review and inadequate inspected support for biosafety
    definition, tiers or mandates.
- evidence_id: readiness
  kind: primary_source
  reference: https://www.saudijmph.com/index.php/pub/article/download/115/91/172
  locator: Bawshkhah et al.; printed pp392–394; introduction, classification summary
    and facility-design section
  accessed_at: '2026-10-20T03:33:07Z'
  support: partial
  summary: Publisher PDF identifies a review article in volume 1(1), pp392–399 (2024).
    It contains the qualitative control claims and numerical summaries paraphrased
    by the record. This is secondary literature, not an authoritative universal requirement
    or a primary efficacy measurement. Its categorical language must be distinguished
    from activity-specific authority guidance.
  snapshot_sha256: 11a3adf4c632bbc96fcfedda786501ab4e00bc196aeb0ec8239d6616c2dce099
- evidence_id: boundary
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/38434104/
  locator: Ziegler and Tremblay; DOI10.1089/apb.2023.0017; complete abstract and bibliographic
    metadata
  accessed_at: '2026-10-20T03:36:40Z'
  support: partial
  summary: Applied Biosafety 29(1):10–18 (2024). Comparative guideline and facility-data
    study describes conditional applicability and proposes criteria where definitive
    guidance is lacking. It supports boundary testing in context, not universal certification
    or a particular equivalence between test labels. Publisher/PMC full text could
    not be directly retrieved; indexed search excerpts are leads only.
- evidence_id: morris
  kind: primary_source
  reference: https://ojs.wgtn.ac.nz/nzjhsp/article/download/9540/8453/15049
  locator: Emma Morris, Worth the risk?; DOI10.26686/nzjhsp.v1i2.9540; sections2.2–2.4
    and conclusion
  accessed_at: '2026-10-20T03:29:44Z'
  support: partial
  summary: Full five-page 2024 graduate communication discusses implementation, certification
    barriers and general safety performance. It provides no measured ISO35001-specific
    infection-reduction result. Its general claim cannot by itself establish the graph
    outcome.
  snapshot_sha256: 5562edc7b058e1119a01ab16d07f21b08c0e470ad001d5b7e302a7e674a2eebb
- evidence_id: iso
  kind: authority
  reference: https://www.iso.org/standard/71293.html
  locator: Official ISO35001:2019 identity, abstract and edition metadata
  accessed_at: '2026-10-20T03:36:40Z'
  support: supports
  summary: Official scope describes a biorisk-management process. Edition 1 is published,
    with a 2024 amendment and revision under development. Abstract/metadata only;
    paid standard text was not acquired. This verifies standard identity, not a measured
    infection outcome.
- evidence_id: examples
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC%3AMED%20AND%20%28EXT_ID%3A9634230%20OR%20EXT_ID%3A11586360%29&resultType=core&format=json
  locator: Complete abstracts and bibliography for Cole1998 and Parkhill2001; Nature
    preview for DOI10.1038/31159
  accessed_at: '2026-10-20T03:29:44Z'
  support: partial
  summary: Both references resolve to primary genome papers about particular strains.
    Their inspected abstracts establish organism/study identity, not a BSL3 classification
    statement. Full text was unavailable, so absence of a classification passage from
    the complete papers is not asserted.
  snapshot_sha256: 75c3feb78a57ce8c7140b4923cafbd5f0ab847308b2b20870c821831dae38e0d
- evidence_id: taxa
  kind: database
  reference: https://rest.uniprot.org/taxonomy/1773
  locator: Taxonomy1773 and 632 JSON records
  accessed_at: '2026-10-20T03:29:44Z'
  support: supports
  summary: 1773 resolves to Mycobacterium tuberculosis and 632 to Yersinia pestis,
    both species. Taxon identity does not determine a laboratory classification.
  snapshot_sha256: 35c41a013523449f34936fa2bba824b09bd6611d659a28783134b9dc128e2464
- evidence_id: historical
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC%3AMED%20AND%20%28EXT_ID%3A41494000%20OR%20EXT_ID%3A40514544%20OR%20EXT_ID%3A41552424%20OR%20EXT_ID%3A41917383%29&resultType=core&format=json
  locator: Four complete database abstracts and their retained discussion fragments
  accessed_at: '2026-10-20T03:33:41Z'
  support: context_only
  summary: All four historical PMIDs resolve; the retained fragments are present in
    their abstracts. They concern different scientific questions and remain explicitly
    disclaimed as support for the active discussion. No pathogen mechanism from these
    papers is adjudicated or expanded.
  snapshot_sha256: cad0118e8dd3104b23231b5a3ce00b7f9f68810747156cd067764ca70d717317
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identity, synonyms and polarity'
  outcome: supported
  target_ids:
  - METPO:1001104
  summary: The local BSL3 class is unambiguous; both numeric synonyms are related
    synonyms. Inherited wording has a bearer error but does not obscure which class
    is intended.
  evidence_ids:
  - record
  - identity
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: definition and nearest support'
  outcome: concern
  target_ids:
  - METPO:1001104
  summary: A containment level cannot itself cause disease. The attached protein review
    does not supply the claimed classification support; contextual authority is needed.
  evidence_ids:
  - record
  - identity
  - ag43
  - bmbl
- assessment_id: hierarchy
  area: consistency
  topic: 'Native checklist: broader parent and subclass direction'
  outcome: supported
  target_ids:
  - METPO:1001104
  summary: The parent is broader and rdfs:subClassOf points in the correct direction.
    The hierarchy is supported by local ontology and classification context, while
    its attached Ag43 citation is misplaced.
  evidence_ids:
  - identity
  - bmbl
  - ag43
- assessment_id: category
  area: representation
  topic: 'Native checklist: category, entities and conditions'
  outcome: concern
  target_ids:
  - METPO:1001104
  summary: NONMECHANISTIC is appropriate. Hazard, environmental conditions, engineered
    controls and a management standard are not interchangeable entity types. Classification
    must retain work/authority context.
  evidence_ids:
  - record
  - model
  - bmbl
  - who
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: taxon and study scope'
  outcome: unknown
  target_ids:
  - METPO:1001104
  summary: Species identifiers resolve. Both citations are strain-specific genome
    studies; available abstracts do not verify the example classification notes. The
    notes omit authority, edition and activity context.
  evidence_ids:
  - examples
  - taxa
  - record
  dimensions:
  - name: example_evidence
    value: Two strain-specific genome papers; species-level taxon identifiers
    definition: Inspected source category and taxon rank, not universal containment
      assignments.
    evidence_ids:
    - examples
    - taxa
  - name: authority_context
    value: BMBL6 and WHO LBM4 overview; ISO35001:2019 metadata; narrative and comparative
      literature
    definition: Frameworks and source types inspected; no all-jurisdiction or legal
      compliance determination.
    evidence_ids:
    - bmbl
    - who
    - iso
    - readiness
    - boundary
- assessment_id: evidence
  area: evidence
  topic: 'Native checklist: source identities, snippets and narrow support'
  outcome: concern
  target_ids:
  - METPO:1001104
  summary: All active reference identities and taxonomy identifiers were checked.
    Relevant full text was inspected for the readiness review and Morris communication;
    other limitations are explicit. Quoted notes include paraphrases rather than checked
    exact snippets.
  evidence_ids:
  - ag43
  - readiness
  - boundary
  - morris
  - iso
  - examples
  - taxa
  - check-biosafety-level-3-snippets-network
- assessment_id: graph
  area: graph
  topic: 'Native checklist: all nodes and eight edges'
  outcome: concern
  target_ids:
  - METPO:1001104
  summary: All 10 nodes and 8 edges were assessed. The contextual management-system
    component is permitted in a NONMECHANISTIC graph. Findings concern claim support
    and semantics, not disconnectedness.
  evidence_ids:
  - record
  - model
  - ag43
  - readiness
  - boundary
  - morris
  - iso
  - bmbl
  details: 'Zero-based edge ledger: 0 classification assigned as intrinsic biological
    realization, with misplaced citation; 1 valid broader relationship but misplaced
    citation; 2 hazard relevance recognizable, while a sufficient universal rule exceeds
    contextual authority; 3–4 qualitative controls and summaries appear in the cited
    review but need bounded source/authority context; 5 boundary verification has
    conditional support in the comparative study abstract; 6 test label and description
    conflict internally, with full-text terminology verification outstanding; 7 specific
    infection outcome is not established by the general management discussion, and
    the proposed predicate meaning does not fit. No operational parameter, procedure
    or test redesign is recommended.'
- assessment_id: discussion
  area: consistency
  topic: 'Native checklist: knowledge-gap premises and inference'
  outcome: concern
  target_ids:
  - METPO:1001104
  summary: Anchors resolve and historical snippets are correctly disclaimed. The active
    question inherits a conflated test label and an unsupported universal certification
    premise. A correlation involving one proxy cannot establish or invalidate an entire
    certification regime. No dataset is claimed.
  evidence_ids:
  - record
  - boundary
  - historical
  - owners
- assessment_id: status
  area: provenance
  topic: 'Native checklist: native status, history and checks'
  outcome: unknown
  target_ids:
  - METPO:1001104
  summary: Focused validation and applicable corpus diagnostics pass within their
    declared scope. AI assistance is disclosed; captured history does not independently
    prove human scientific sign-off for REVIEWED.
  evidence_ids:
  - record
  - owners
  - check-biosafety-level-3-validate
  - check-biosafety-level-3-strict
  - check-validate-history
findings:
- finding_id: classification-citation
  issue_key: biosafety-level-3-classification-citation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Protein review is misplaced as classification evidence
  description: The Ag43 article identity and inspected abstract do not support the
    definition or the two initial classification edges. A generic snippet cannot supply
    that missing support. This is a nearest-evidence mismatch, not an assertion that
    its unavailable full text contains no biosafety words.
  target_ids:
  - METPO:1001104
  field_paths:
  - definition_source
  - evidence[0]
  - causal_graphs[0].edges[0].evidence
  - causal_graphs[0].edges[1].evidence
  evidence_ids:
  - ag43
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: classification-scope
  issue_key: biosafety-level-3-classification-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Hazard-to-classification language drops necessary context
  description: The graph treats agent properties as yielding a level and describes
    the parent as an agent hazard axis. BMBL and WHO distinguish contextual selection
    of controls from intrinsic hazard. The secondary readiness review cannot establish
    universal requirements merely by stating them categorically.
  target_ids:
  - METPO:1001104
  field_paths:
  - causal_graphs[0].description
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].edges[0]
  - causal_graphs[0].edges[2]
  - causal_graphs[0].edges[3]
  - causal_graphs[0].edges[4]
  evidence_ids:
  - record
  - bmbl
  - who
  - readiness
  - model
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: verification-conflation
  issue_key: biosafety-level-3-verification-conflation
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Test naming and certification inference are conflated
  description: The node is named pressure decay but describes maintained steady pressure,
    and the discussion inherits that inconsistency. It then treats a particular test
    as a universal certification surrogate. The inspected comparative abstract does
    not establish that premise, and the proposed proxy conclusions exceed the asserted
    evidence.
  target_ids:
  - METPO:1001104
  field_paths:
  - causal_graphs[0].nodes[7]
  - causal_graphs[0].edges[6]
  - discussions[0].prompt
  - discussions[0].rationale
  - discussions[0].proposed_experiments[0].would_support
  - discussions[0].proposed_experiments[0].would_refute
  evidence_ids:
  - record
  - boundary
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion PLAN and replay behavior
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: management-outcome
  issue_key: biosafety-level-3-management-outcome
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: General safety discussion does not establish the infection outcome or predicate
    fit
  description: The final edge asserts an ISO35001-specific infection outcome. Its
    source discusses general safety performance; it does not establish that result.
    The proposed mitigates predicate concerns defense/homeostatic mechanisms, and
    its permissive type gate does not validate an organizational standard as such
    a mechanism.
  target_ids:
  - METPO:1001104
  field_paths:
  - causal_graphs[0].edges[7]
  - causal_graphs[0].nodes[8]
  evidence_ids:
  - morris
  - iso
  - model
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
    role: Proposed predicate definition; semantic context rather than automatic authority
      to broaden it
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: definition-bearer
  issue_key: biosafety-level-3-definition-bearer
  category: nomenclature
  severity: minor
  status: open
  certainty: confirmed
  title: Definition assigns disease causation to the containment level
  description: The definition makes the level itself the disease-causing entity. The
    wording is inherited verbatim from local METPO, so the correction should preserve
    and identify upstream provenance.
  target_ids:
  - METPO:1001104
  field_paths:
  - definition
  evidence_ids:
  - record
  - identity
  - bmbl
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Inherited ontology definition/identity provenance; avoid force regeneration
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: example-context
  issue_key: biosafety-level-3-example-context
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Example classification notes lack directly verified contextual support
  description: Both example notes are unqualified. The inspected genome-study abstracts
    do not substantiate those notes, and no classification passage or authority context
    is supplied. Full-paper support remains unresolved rather than refuted.
  target_ids:
  - METPO:1001104
  field_paths:
  - canonical_examples[0]
  - canonical_examples[1]
  evidence_ids:
  - examples
  - taxa
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: node-representation
  issue_key: biosafety-level-3-node-representation
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Some node types do not match their described entities
  description: The hazard node describes agent properties rather than a biological
    process. Control and management nodes use environmental-factor types despite describing
    engineered or organizational interventions. The intended entities need review
    under native containment-factor guidance.
  target_ids:
  - METPO:1001104
  field_paths:
  - causal_graphs[0].nodes[2].node_type
  - causal_graphs[0].nodes[4].node_type
  - causal_graphs[0].nodes[5].node_type
  - causal_graphs[0].nodes[8].node_type
  evidence_ids:
  - record
  - model
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: quotation-provenance
  issue_key: biosafety-level-3-quotation-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Quoted notes contain summaries without exact passage locators
  description: Several edge notes present reconstructed wording in quotation marks.
    Comparison with the inspected readiness and Morris PDFs shows paraphrase rather
    than exact quotation. Bibliographic support and verbatim snippet provenance should
    remain distinct; boundary-paper quotations remain unverified.
  target_ids:
  - METPO:1001104
  field_paths:
  - causal_graphs[0].edges[2].evidence
  - causal_graphs[0].edges[3].evidence
  - causal_graphs[0].edges[4].evidence
  - causal_graphs[0].edges[5].evidence
  - causal_graphs[0].edges[6].evidence
  - causal_graphs[0].edges[7].evidence
  evidence_ids:
  - record
  - readiness
  - morris
  - boundary
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: repair-classification-citations
  description: Reassess and replace or remove unsupported attributions for retained
    classification claims.
  finding_ids:
  - classification-citation
  target_ids:
  - METPO:1001104
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Inspect a suitable authority or documentary source and attach exact edition/section
    locators.
  - Verify each claim independently; run focused validate, validate-strict and verify-snippets
    after authorized curation.
- action_id: retain-classification-context
  description: Separate hazard description, laboratory/activity classification and
    source-specific summaries.
  finding_ids:
  - classification-scope
  target_ids:
  - METPO:1001104
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retained claims identify authority/edition and context without issuing handling
    requirements.
  - Distinguish recommendations, review summaries and normative requirements.
  - Use guarded curation/history and applicable strict, graph and qc checks after
    authorized changes.
- action_id: reconcile-verification-claims
  description: Resolve the nomenclature against directly inspected source text and
    qualify the certification premise.
  finding_ids:
  - verification-conflation
  target_ids:
  - METPO:1001104
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion PLAN and replay behavior
  acceptance_checks:
  - Retain only source-supported test identity and conceptual scope; no replacement
    procedure is proposed here.
  - Separate a measured proxy from a broader certification conclusion.
  - Reconcile the maintained discussion PLAN and target; run strict and applicable
    qc after authorized curation.
- action_id: bound-management-relation
  description: Remove or qualify the unsupported outcome and reassess predicate semantics
    for the intended organizational relation.
  finding_ids:
  - management-outcome
  target_ids:
  - METPO:1001104
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
    role: Proposed predicate definition; semantic context rather than automatic authority
      to broaden it
  acceptance_checks:
  - Distinguish purpose, expectation and measured outcome.
  - Do not broaden a shared predicate solely to make this edge pass.
  - Inspect exact source support and run strict plus applicable graph/grounding checks
    after authorized correction.
- action_id: correct-bearer
  description: Clarify which entity bears the hazard while preserving the classification
    identity.
  finding_ids:
  - definition-bearer
  target_ids:
  - METPO:1001104
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Inherited ontology definition/identity provenance; avoid force regeneration
  acceptance_checks:
  - Avoid an automatic agent-to-level assignment rule.
  - Preserve upstream provenance and run focused strict validation after authorized
    correction.
- action_id: verify-example-notes
  description: Provide directly inspected, appropriately scoped documentary support
    or qualify the examples as unresolved.
  finding_ids:
  - example-context
  target_ids:
  - METPO:1001104
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain species versus strain distinctions and relevant authority/activity context.
  - Do not infer universal assignment from pathogenicity or taxon identity.
  - Run focused reference and strict checks after authorized edits.
- action_id: review-node-types
  description: Resolve intended entities before choosing native types or documenting
    a schema gap.
  finding_ids:
  - node-representation
  target_ids:
  - METPO:1001104
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Do not invent biological mechanisms or select merely adjacent ontology terms.
  - Retain NONMECHANISTIC context and run strict plus graph/grounding checks after
    authorized changes.
- action_id: separate-quotes-and-notes
  description: Use checked short verbatim snippets with locators, and retain interpretation
    as unquoted notes.
  finding_ids:
  - quotation-provenance
  target_ids:
  - METPO:1001104
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_3.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Check actual source bytes; do not silently promote summaries or indexed excerpts
    to quotations.
  - Preserve source-access limits and rerun verify-snippets plus strict validation
    after authorized edits.
limitations:
- Ag43 and both genome papers were assessed at abstract/preview level; complete-paper
  absence is not asserted.
- Boundary-study bibliography and complete abstract were inspected. Direct publisher
  retrieval failed, PMC returned a browser challenge, Europe PMC XML failed and BioC
  returned no result. Indexed full-text search excerpts were treated only as leads.
- The readiness review and Morris communication were inspected in publisher PDFs.
  Source fidelity does not establish every claim in a secondary article as independently
  true.
- ISO official abstract and edition metadata were inspected; paid standard text was
  not acquired. BMBL6 and WHO overview checks retain their original actual timestamps.
- No operational requirements, procedure changes, facility suitability, quantitative
  protection or pathogen mechanisms are evaluated or recommended. The existing proposed
  experiment is assessed only for evidentiary logic.
- Historical sign-off remains unresolved; corpus adapter skips and superseded diagnostic
  failures are retained.
- Review integration resumed after an interruption; the start and finish span the
  actual work interval.
notes:
- Only this new review bundle is written; no record, history, writer, ontology or
  generated page is changed.
- Original captured hashes were preserved. External access failures and successful
  fallbacks are distinguished.
- The isolated sweep began with 1130 record paths; this bundle has exactly one target
  and denominator 1.
tags:
- record-review
- biosafety-level-3
- ecology
- needs-curation
```
