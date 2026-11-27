# Scientific and source review of biosafety level 2 (METPO:1001103)

- Review: 20261020T032840Z-biosafety-level-2
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-19T23:39:27Z
- Finished UTC: 2026-10-20T03:28:40Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Local METPO identity and hierarchy are consistent. Three major findings concern misplaced classification evidence, automatic hazard/risk-group assignment, and unsupported discussion claims about measurement and risk. Three minor findings concern example scope, internally inconsistent control-summary wording and node semantics. All 10 nodes, 8 edges, both examples and the discussion were assessed.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Sixth previously uncovered record in lexicographic path order. Only this record is adjudicated; parent, source snapshots and native corpus checks provide context.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f25e2af0b38a8303b13f627a9a5c33b36af4b3d2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1001103 | data/traits/ecology/biosafety_level_2.yaml | maintained | biosafety level 2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1001103 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1001103 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1001103 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1001103 | 1276 history records checked, zero invalid links; integrity does not establish scientific correctness or human sign-off. |
| Initial full-product validation | failed | False | METPO:1001103 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1001103 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1001103 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1001103 | Selected record validates; syntax and shape do not establish scientific or classification support. |
| Focused strict closed-schema validation | passed | True | METPO:1001103 | One file scanned; zero error rows. |
| Focused source snippet verification | passed | True | METPO:1001103 | Three repetitions of one short snippet returned NOT_IN_ABSTRACT. This does not prove full-text absence or establish the classification assertions. |
| Expression module applicability | not_applicable | False | METPO:1001103 | This classification record has no gene/protein instance or expression dataset. Expression membership would not establish a containment level or its administrative requirements. |

## Scientific And Domain Assessments

### Native checklist: identity, polarity and term kind

identity: supported. Targets: METPO:1001103.

One locally defined BSL2 CLASS is denoted; its numerical synonym is RELATED and parent references resolve. Biological-agent properties and administrative classification still require scope distinction.

### Native checklist: definition source and contextual meaning

evidence: concern. Targets: METPO:1001103.

The broad moderate-risk description is recognizable as a classification summary, but the attached Ag43 review is inappropriate support. The graph makes a stronger intrinsic-hazard assignment claim than the inspected authorities support.

### Native checklist: broader parent and predicate identity

consistency: supported. Targets: METPO:1001103.

BSL2 belongs under the local biosafety-level class, consistent with inspected frameworks. rdfs:subClassOf direction is correct; its attached Ag43 citation is still misplaced. Proposed confers identity does not itself validate an administrative assignment meaning.

### Native checklist: classification, node types and conditions

representation: concern. Targets: METPO:1001103.

NONMECHANISTIC scope is appropriate. Several BIOLOGICAL_PROCESS nodes actually describe hazard/agent/capacity concepts. An unqualified trait-node control summary conflicts with conditional wording elsewhere in the same record.

### Native checklist: taxonomic and study context

evidence: concern. Targets: METPO:1001103.

The S. aureus paper directly labels that organism BSL2 in its laboratory context. The Salmonella paper documents one Enteritidis strain/activity in a BSL2 facility, while the record note drops that scope. Both species taxon IDs resolve.

### Native checklist: references, source types and provenance

evidence: concern. Targets: METPO:1001103.

All active identifiers and relevant source text were verified. Sources include a protein review, a contextual classification article, a biobank chapter, a laboratory-method paper and a primary study reporting facility context. Generic repeated snippets do not establish classification support; six additional edges omit snippets and require precise source locators when curated.

### Native checklist: all nodes and edges

graph: concern. Targets: METPO:1001103.

All 10 nodes and 8 edges were assessed. The separate procedure/control component is permissible for NONMECHANISTIC scope. Classification assignment is contextual, not a direct biological realization; the graph should preserve that distinction without adding mechanisms.

Zero-based edge ledger: 0 unsupported attached Ag43 citation and deterministic assignment; 1 hierarchy supported but citation misplaced; 2 risk-group association can inform assessment but are-assigned wording implies unsupported equivalence; 3 hazard relevance supported as one contextual input; 4 transmission relevance supported but categorical escalation drops source/record severity and activity qualifications; 5 broad conditional control relationship supported, while exclusive subtype wording exceeds its nearest chapter passage; 6 qualitative protection relation supported with no quantified effect asserted; 7 administrative access relation supported in the chapter context, not as a universal legal mandate. No operational table contents or procedural advice are reproduced.

### Native checklist: gap premises, inference and datasets

consistency: concern. Targets: METPO:1001103.

Anchors resolve and historical scan snippets are correctly excluded from support. The authored discussion nevertheless makes unsupported universal statements about the evidence gap and draws risk/classification conclusions from an exposure proxy. No dataset is asserted; the review does not extend or endorse the proposed experiment.

### Native checklist: status, history and native checks

provenance: unknown. Targets: METPO:1001103.

Focused schema/strict checks and corpus integrity checks pass within scope. Agent assistance is disclosed. Neither seed metadata nor captured AI curation establishes historical human sign-off for REVIEWED.

## Findings

### classification-citation: Ag43 review does not substantiate the definition or classification edges

major / open / confirmed; issue key: biosafety-level-2-classification-citation.

The exact cited article is a protein-specific E. coli review. Inspected identity and abstract do not establish the biosafety definition, moderate-hazard assignment or subclass assertion. A generic two-word snippet cannot supply that missing support.

### automatic-assignment: Hazard and risk-group descriptions imply automatic level assignment

major / open / confirmed; issue key: biosafety-level-2-automatic-assignment.

The graph describes hazard as yielding BSL2, RG2 agents as assigned to BSL2, and transmission alone as escalating beyond it. The cited chapter explicitly distinguishes risk group from laboratory level; the classification article itself includes work/activity context. Those sources support contextual inputs, not the implied sufficient rules.

### unsupported-discussion-premises: Discussion asserts an unverified evidence gap and overstates what its proxy establishes

major / open / confirmed; issue key: biosafety-level-2-unsupported-discussion-premises.

The record supplies no source for universal claims that one control determines most work, that relevant lists precede measurement, or that the relation has never been measured. Its stated surrogate readout does not itself establish infectious dose or prove the whole control boundary correct/incorrect. Historical off-topic references are properly disclaimed and cannot support these assertions.

### example-study-scope: Salmonella example note loses the study strain and activity scope

minor / open / confirmed; issue key: biosafety-level-2-example-study-scope.

The cited paper reports one Enteritidis strain and study in a BSL2 facility. The parent-species identifier is correct, but the bare classification note does not retain the evidence context. The example can remain informative without implying universality.

### conditional-control-summary: Unqualified summary conflicts with conditional source and record wording

minor / open / confirmed; issue key: biosafety-level-2-conditional-control-summary.

The trait-node description declares cabinet use required without a condition, whereas the cabinet node, edge and discussion use conditional scope. The edge also states an exclusive equipment-subtype formulation not established by the nearest cited chapter passage. Reconcile conceptual scope rather than turning a summary into a universal operational rule.

### node-semantics: Several biological-process nodes describe attributes or agents

minor / open / confirmed; issue key: biosafety-level-2-node-semantics.

moderate_pathogen_hazard, risk_group_2_pathogen and pathogenicity describe respectively a property collection, an agent and a capacity, while all use BIOLOGICAL_PROCESS. A permissive type gate for confers does not establish that an administrative classification is a biological trait realization.

## Recommended Actions And Acceptance Checks

### repair-classification-evidence

Reassess the retained classification claims and replace or remove unsupported attributions using inspected authority or documentary evidence.

- Verify nearest-claim support and exact bibliography independently of the source title.
- Use precise source/edition locators and checked short quotations where appropriate.
- After authorized curation run focused validate, validate-strict, verify-snippets and applicable qc.

### bound-assignment-statements

Preserve the distinction between agent hazard, risk group, work context and containment classification in the retained record.

- Remove unsupported sufficient-condition or universal escalation implications without issuing handling recommendations.
- Qualify claims to inspected authority/edition and contextual scope; preserve inherited ontology provenance.
- Use guarded curation/history and run strict, applicable graph/reference checks and qc after authorized edits.

### qualify-discussion-claims

Source and bound the asserted knowledge gap and distinguish an exposure proxy from risk or classification evidence.

- Use a documented bounded literature search before retaining any absence-of-measurement claim.
- Remove conclusions not entailed by the stated evidence; this review proposes no experiment or operational modification.
- Reconcile maintained discussion PLAN and replay behavior so later regeneration cannot restore unsupported text.
- Run focused strict validation and applicable qc after authorized correction.

### retain-example-context

Qualify the Salmonella example to the documented strain/study context.

- Preserve the distinction between species identifier, strain and observed facility/activity context.
- Do not infer a universal classification or add unsupported experimental detail.
- Run focused strict and reference checks after authorized curation.

### align-summary-scope

Make the classification summary and nearest evidence consistent with their conditional authority context.

- Read the node, edge, evidence and discussion together and retain consistent qualifications.
- Do not infer exclusive or universal operational requirements from summary prose.
- Run focused strict validation after authorized wording changes.

### review-node-entities

Review intended entities against the schema and proposal semantics; choose accurate representation or document the precise schema gap.

- Do not select a merely similar term or invent a biological mechanism to satisfy a type gate.
- Retain NONMECHANISTIC classification context.
- Run strict and applicable graph/grounding checks after authorized edits.

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
| check-biosafety-level-2-validate | /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-2-validate.log; Executed 2026-10-19T23:41:46Z through 2026-10-19T23:41:47Z; metadata biosafety-level-2-validate.json | context_only | Selected record validates; syntax and shape do not establish scientific or classification support. |
| check-biosafety-level-2-strict | /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-2-strict.log; Executed 2026-10-19T23:41:46Z through 2026-10-19T23:41:48Z; metadata biosafety-level-2-strict.json | context_only | One file scanned; zero error rows. |
| check-biosafety-level-2-snippets-network | /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-2-snippets-network.log; Executed 2026-10-19T23:41:47Z through 2026-10-19T23:41:48Z; metadata biosafety-level-2-snippets-network.json | context_only | Three repetitions of one short snippet returned NOT_IN_ABSTRACT. This does not prove full-text absence or establish the classification assertions. |
| record | data/traits/ecology/biosafety_level_2.yaml; Entire record: identity, 10 nodes, 8 edges, two examples, discussion and history | partial | Local identity resolves; classification scope and unsupported discussion premises require correction. |
| local-identity | data/raw/metpo.owl; METPO:1001103 label/definition/synonym/parent; maintained METPO:1001101 parent | supports | Captured ontology agrees with identifier, related numeric synonym and broader parent. Ignored-inclusive corpus and exclusion searches resolve one exact target and no direct exclusion match. All graph endpoints and discussion anchors resolve. |
| local-model | src/traitmech/schema/traitmech.yaml; CausalNodeTypeEnum; v8 METPO:2007700 proposal; predicate mapping; native curation guidance | partial | Confers is a locally proposed process-to-trait realization relation, not a verified minted predicate or automatic model for administrative classification. Hazard attributes, agents and capacities are not identical to biological processes. Subclass direction matches the local ontology. |
| local-owners | scripts/curate_knowledge_gaps.py; PLAN kgscan-066a51aacfb6 and application loop; captured history and guarded writer | partial | Discussion replay overwrites authored fields and removes evidence, so future correction must consider the maintained PLAN as well as the target. Seeder skips existing records by default; the historical predicate-migration script is not a guarded writer. Captured history does not independently establish human sign-off. |
| pathol | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7524674/fullTextXML; Laboratory biosafety: working with microbial pathogens; Tables1–3. | partial | Kaufer et al., Laboratory biosafety measures involving SARS-CoV-2 and the classification as a Risk Group 3 biological agent (2020). A 2020 Australian-context classification discussion. The general section supports relevance of hazard criteria and contextual controls, but also includes activity type. Its own Table3 assigns different levels to different activities involving the same risk-group agent. Thus fixed RG-to-BSL mapping and transmission-only escalation do not follow. No operational table content reproduced. |
| springer | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7120677/fullTextXML; Biohazardous Agents Risk Assessment; Biosafety Level2; BSL2 Procedures and Practices; Safety Equipment for BSL2. | partial | Ta, Gosa and Nathanson, Biosafety and Biohazards: Understanding Biosafety Levels and Meeting Safety Requirements of a Biobank (2019 book chapter). Chapter based on CDC BMBL5 describes contextual laboratory controls. Explicitly distinguishes risk groups from laboratory biosafety levels. Supports the graph’s broad contextual control/access statements. Specific universal or exclusive requirements should not be inferred from its short overview; detailed chapter text admits contextual alternatives. |
| example-senterica | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7597915/fullTextXML; Material and methods, opening paragraph; organism identification at start of Preparation of Inoculum. | partial | Muckey et al., Research Note: Evaluating the roles of surface sanitation and feed sequencing on mitigating Salmonella Enteritidis contamination on animal food manufacturing equipment (2020). Explicitly reports study conducted in a BSL2 facility. Study organism is an Enteritidis strain, ATCC13076. Supports a documented strain/activity-specific example, not a universal classification for every S. enterica strain or activity. No experimental details reproduced. |
| example-saureus | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC4070006/ascii; Introductory CAUTION paragraph. | supports | Vitko and Richardson, Laboratory maintenance of methicillin-resistant Staphylococcus aureus (MRSA) (2013). The paper explicitly identifies S. aureus as BSL2; canonical_examples[0] is directly supported in the paper’s laboratory context. No culture or other procedural contents assessed or reproduced. |
| ag43-reused | https://www.annualreviews.org/content/journals/10.1146/annurev.micro.62.081307.162938; /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-source-notes.json, ag43 | partial | Already verified protein-specific Ag43 review, not the claimed general virulence/classification authority. Inspected identity/abstract do not support definition, evidence[0], or edges0–1. Full-text exactness of virulence factors snippet remains unverified; lexical presence would not establish these classification claims. |
| bmbl-reused | https://www.cdc.gov/covid/media/pdfs/2024/07/SF__19_308133-A_BMBL6_00-BOOK-WEB-final-3.pdf; Foreword piii; SectionII p11; SectionIII Biosafety Levels p27. | supports | Previously directly inspected authority: contextual laboratory classification, four recognized primary levels, agent risk group not equivalent to level, advisory rather than universal regulatory authority. |
| who-reused | https://www.who.int/publications/i/item/9789240011311; Overview; Composition of the manual. | supports | Previously directly inspected official overview supports case-specific assessment informing controls; core PDF not inspected. |
| taxa | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1280; NCBI taxonomy pages for 1280 and 28901 | supports | NCBITaxon:1280 resolves to Staphylococcus aureus and NCBITaxon:28901 to Salmonella enterica. These verify species identity, not containment assignment. |
| historical-scan | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC%3AMED+AND+%28EXT_ID%3A41683313+OR+EXT_ID%3A41413233+OR+EXT_ID%3A41640410+OR+EXT_ID%3A41490313%29&amp;resultType=core&amp;format=json; Four complete database abstracts and preserved fragments | context_only | All four historical PMIDs resolve and their retained fragments match normalized abstracts. Their topics are unrelated to the active containment discussion and are expressly disclaimed as support. |

## Limits And Additional Notes

- Ag43 was inspected at title/abstract level; full text was unavailable, and no exhaustive full-text absence claim is made.
- The other four active references had relevant full-text passages inspected. A failed Europe PMC S. aureus fetch was resolved by NCBI BioC and PMC HTML.
- Authority sources are specific historical editions and contexts, not a current legal or all-jurisdiction classification determination. WHO overview was inspected; its core PDF was not.
- No quantitative protective efficacy, infectious-dose estimate, procedure recommendation or suitability assessment was performed. The existing proposed experiment is assessed only for evidentiary logic.
- Taxonomy identity is separate from containment assignment. Historical scan references remain provenance only.
- Human sign-off for REVIEWED was not independently established; corpus product-adapter skips and earlier diagnostic failures remain explicit.
- Review work was interrupted between original capture/source inspection and final integration; actual start/finish timestamps retain that interval.
- No trait, history, writer, ontology or generated page changed. Only this new structured review is saved.
- All source-capture expansions preserved original hashes; source identity and local graph semantics were assessed separately.
- Correction owners identify future authorized work; no outbound communication or operational change is performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T032840Z-biosafety-level-2
kind: record
repository: CultureBotAI/TraitMech
title: Scientific and source review of biosafety level 2 (METPO:1001103)
started_at: '2026-10-19T23:39:27Z'
finished_at: '2026-10-20T03:28:40Z'
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
summary: Local METPO identity and hierarchy are consistent. Three major findings concern
  misplaced classification evidence, automatic hazard/risk-group assignment, and unsupported
  discussion claims about measurement and risk. Three minor findings concern example
  scope, internally inconsistent control-summary wording and node semantics. All 10
  nodes, 8 edges, both examples and the discussion were assessed.
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
  - path: data/traits/ecology/biosafety_level_2.yaml
    sha256: cc0fd06d66a12cda1f4d229d91fd7f9c0dd98c69d9d77e756cce8fdfccfb3a8b
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
- target_id: METPO:1001103
  path: data/traits/ecology/biosafety_level_2.yaml
  label: biosafety level 2
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: maintained curated TraitRecord; use guarded writer for any authorized correction
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Sixth previously uncovered record in lexicographic path order. Only this
    record is adjudicated; parent, source snapshots and native corpus checks provide
    context.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1001103
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1001103
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
  - METPO:1001103
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
  - METPO:1001103
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
  - METPO:1001103
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
  - METPO:1001103
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
  - METPO:1001103
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
  - METPO:1001103
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: biosafety-level-2-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1001103
  command: just validate data/traits/ecology/biosafety_level_2.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Selected record validates; syntax and shape do not establish scientific
    or classification support.
  evidence_ids:
  - check-biosafety-level-2-validate
- check_id: biosafety-level-2-strict
  name: Focused strict closed-schema validation
  status: passed
  required: true
  target_ids:
  - METPO:1001103
  command: just validate-strict data/traits/ecology/biosafety_level_2.yaml --out /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-2-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero error rows.
  evidence_ids:
  - check-biosafety-level-2-strict
- check_id: biosafety-level-2-snippets-network
  name: Focused source snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1001103
  command: just verify-snippets --record data/traits/ecology/biosafety_level_2.yaml
    --out /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-2-snippets-network.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Three repetitions of one short snippet returned NOT_IN_ABSTRACT. This does
    not prove full-text absence or establish the classification assertions.
  evidence_ids:
  - check-biosafety-level-2-snippets-network
- check_id: structured-expression-context
  name: Expression module applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1001103
  summary: This classification record has no gene/protein instance or expression dataset.
    Expression membership would not establish a containment level or its administrative
    requirements.
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-20T03:28:40Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-20T03:28:40Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-20T03:28:40Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; metadata validate-history.json
  accessed_at: '2026-10-20T03:28:40Z'
  support: context_only
  summary: 1276 history records checked, zero invalid links; integrity does not establish
    scientific correctness or human sign-off.
  snapshot_sha256: 1fc48f1203fbfcd27b1243e4e147afb367aebfc592b496b352201058c6ee85d2
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-20T03:28:40Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-20T03:28:40Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-20T03:28:40Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-biosafety-level-2-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-2-validate.log
  locator: Executed 2026-10-19T23:41:46Z through 2026-10-19T23:41:47Z; metadata biosafety-level-2-validate.json
  accessed_at: '2026-10-20T03:28:40Z'
  support: context_only
  summary: Selected record validates; syntax and shape do not establish scientific
    or classification support.
  snapshot_sha256: f3ab38b1476636bc9b3b5bf18334455b43f4f7957b105560fc8de766b8b9cb1a
- evidence_id: check-biosafety-level-2-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-2-strict.log
  locator: Executed 2026-10-19T23:41:46Z through 2026-10-19T23:41:48Z; metadata biosafety-level-2-strict.json
  accessed_at: '2026-10-20T03:28:40Z'
  support: context_only
  summary: One file scanned; zero error rows.
  snapshot_sha256: 9808003d148600352f545366357a4969e861721392e58c07cbe4daaab08ffd44
- evidence_id: check-biosafety-level-2-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-2-snippets-network.log
  locator: Executed 2026-10-19T23:41:47Z through 2026-10-19T23:41:48Z; metadata biosafety-level-2-snippets-network.json
  accessed_at: '2026-10-20T03:28:40Z'
  support: context_only
  summary: Three repetitions of one short snippet returned NOT_IN_ABSTRACT. This does
    not prove full-text absence or establish the classification assertions.
  snapshot_sha256: 828fdedb08a6cf321d2d3fe017e41b349d9c0c4957605eeb1faad954c4fa08b4
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/biosafety_level_2.yaml
  locator: 'Entire record: identity, 10 nodes, 8 edges, two examples, discussion and
    history'
  accessed_at: '2026-10-20T03:28:40Z'
  support: partial
  summary: Local identity resolves; classification scope and unsupported discussion
    premises require correction.
  snapshot_sha256: cc0fd06d66a12cda1f4d229d91fd7f9c0dd98c69d9d77e756cce8fdfccfb3a8b
- evidence_id: local-identity
  kind: authority
  reference: data/raw/metpo.owl
  locator: METPO:1001103 label/definition/synonym/parent; maintained METPO:1001101
    parent
  accessed_at: '2026-10-20T03:28:40Z'
  support: supports
  summary: Captured ontology agrees with identifier, related numeric synonym and broader
    parent. Ignored-inclusive corpus and exclusion searches resolve one exact target
    and no direct exclusion match. All graph endpoints and discussion anchors resolve.
- evidence_id: local-model
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: CausalNodeTypeEnum; v8 METPO:2007700 proposal; predicate mapping; native
    curation guidance
  accessed_at: '2026-10-20T03:28:40Z'
  support: partial
  summary: Confers is a locally proposed process-to-trait realization relation, not
    a verified minted predicate or automatic model for administrative classification.
    Hazard attributes, agents and capacities are not identical to biological processes.
    Subclass direction matches the local ontology.
- evidence_id: local-owners
  kind: record_content
  reference: scripts/curate_knowledge_gaps.py
  locator: PLAN kgscan-066a51aacfb6 and application loop; captured history and guarded
    writer
  accessed_at: '2026-10-20T03:28:40Z'
  support: partial
  summary: Discussion replay overwrites authored fields and removes evidence, so future
    correction must consider the maintained PLAN as well as the target. Seeder skips
    existing records by default; the historical predicate-migration script is not
    a guarded writer. Captured history does not independently establish human sign-off.
  snapshot_sha256: cc0acb3aed5d5b837f1e4edf38ef0297440ef3378dd6ccf56584cd777508e0dc
- evidence_id: pathol
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7524674/fullTextXML
  locator: 'Laboratory biosafety: working with microbial pathogens; Tables1–3.'
  accessed_at: '2026-10-19T23:41:40.152773Z'
  support: partial
  summary: Kaufer et al., Laboratory biosafety measures involving SARS-CoV-2 and the
    classification as a Risk Group 3 biological agent (2020). A 2020 Australian-context
    classification discussion. The general section supports relevance of hazard criteria
    and contextual controls, but also includes activity type. Its own Table3 assigns
    different levels to different activities involving the same risk-group agent.
    Thus fixed RG-to-BSL mapping and transmission-only escalation do not follow. No
    operational table content reproduced.
  snapshot_sha256: 7794394a8f7bc1adafd659c015845f6af8bde5ed152d0f066797e412741e0aca
- evidence_id: springer
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7120677/fullTextXML
  locator: Biohazardous Agents Risk Assessment; Biosafety Level2; BSL2 Procedures
    and Practices; Safety Equipment for BSL2.
  accessed_at: '2026-10-19T23:41:40.153314Z'
  support: partial
  summary: 'Ta, Gosa and Nathanson, Biosafety and Biohazards: Understanding Biosafety
    Levels and Meeting Safety Requirements of a Biobank (2019 book chapter). Chapter
    based on CDC BMBL5 describes contextual laboratory controls. Explicitly distinguishes
    risk groups from laboratory biosafety levels. Supports the graph’s broad contextual
    control/access statements. Specific universal or exclusive requirements should
    not be inferred from its short overview; detailed chapter text admits contextual
    alternatives.'
  snapshot_sha256: b61104ab157fe97119491310e2ccbf2d5e1ac14ce46cca92cf097fa45eda9d09
- evidence_id: example-senterica
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7597915/fullTextXML
  locator: Material and methods, opening paragraph; organism identification at start
    of Preparation of Inoculum.
  accessed_at: '2026-10-19T23:41:40.883496Z'
  support: partial
  summary: 'Muckey et al., Research Note: Evaluating the roles of surface sanitation
    and feed sequencing on mitigating Salmonella Enteritidis contamination on animal
    food manufacturing equipment (2020). Explicitly reports study conducted in a BSL2
    facility. Study organism is an Enteritidis strain, ATCC13076. Supports a documented
    strain/activity-specific example, not a universal classification for every S.
    enterica strain or activity. No experimental details reproduced.'
  snapshot_sha256: 4a25c267cdad4a2834b7a61bd6d70bfc21114bf2caf8a5fd9a9456b8fc99eddc
- evidence_id: example-saureus
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC4070006/ascii
  locator: Introductory CAUTION paragraph.
  accessed_at: '2026-10-19T23:42:03.119337Z'
  support: supports
  summary: Vitko and Richardson, Laboratory maintenance of methicillin-resistant Staphylococcus
    aureus (MRSA) (2013). The paper explicitly identifies S. aureus as BSL2; canonical_examples[0]
    is directly supported in the paper’s laboratory context. No culture or other procedural
    contents assessed or reproduced.
  snapshot_sha256: 408e3f132a56b2ef5e6f29b449102c7635b61adfe70f32c8f34e3210d477b729
- evidence_id: ag43-reused
  kind: primary_source
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev.micro.62.081307.162938
  locator: /private/tmp/traitmech-record-sweep.FU79Gr/biosafety-level-source-notes.json,
    ag43
  accessed_at: '2026-10-19T23:34:48Z'
  support: partial
  summary: Already verified protein-specific Ag43 review, not the claimed general
    virulence/classification authority. Inspected identity/abstract do not support
    definition, evidence[0], or edges0–1. Full-text exactness of virulence factors
    snippet remains unverified; lexical presence would not establish these classification
    claims.
- evidence_id: bmbl-reused
  kind: authority
  reference: https://www.cdc.gov/covid/media/pdfs/2024/07/SF__19_308133-A_BMBL6_00-BOOK-WEB-final-3.pdf
  locator: Foreword piii; SectionII p11; SectionIII Biosafety Levels p27.
  accessed_at: '2026-10-19T23:38:50Z'
  support: supports
  summary: 'Previously directly inspected authority: contextual laboratory classification,
    four recognized primary levels, agent risk group not equivalent to level, advisory
    rather than universal regulatory authority.'
- evidence_id: who-reused
  kind: authority
  reference: https://www.who.int/publications/i/item/9789240011311
  locator: Overview; Composition of the manual.
  accessed_at: '2026-10-19T23:38:39Z'
  support: supports
  summary: Previously directly inspected official overview supports case-specific
    assessment informing controls; core PDF not inspected.
- evidence_id: taxa
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1280
  locator: NCBI taxonomy pages for 1280 and 28901
  accessed_at: '2026-10-19T23:42:57Z'
  support: supports
  summary: NCBITaxon:1280 resolves to Staphylococcus aureus and NCBITaxon:28901 to
    Salmonella enterica. These verify species identity, not containment assignment.
- evidence_id: historical-scan
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC%3AMED+AND+%28EXT_ID%3A41683313+OR+EXT_ID%3A41413233+OR+EXT_ID%3A41640410+OR+EXT_ID%3A41490313%29&resultType=core&format=json
  locator: Four complete database abstracts and preserved fragments
  accessed_at: '2026-10-19T23:42:39Z'
  support: context_only
  summary: All four historical PMIDs resolve and their retained fragments match normalized
    abstracts. Their topics are unrelated to the active containment discussion and
    are expressly disclaimed as support.
  snapshot_sha256: eea3cb37cc65f87f5fb99d784df20d51a4242da3a0360f7ce2855fa55d9a67f3
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identity, polarity and term kind'
  outcome: supported
  target_ids:
  - METPO:1001103
  summary: One locally defined BSL2 CLASS is denoted; its numerical synonym is RELATED
    and parent references resolve. Biological-agent properties and administrative
    classification still require scope distinction.
  evidence_ids:
  - record
  - local-identity
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: definition source and contextual meaning'
  outcome: concern
  target_ids:
  - METPO:1001103
  summary: The broad moderate-risk description is recognizable as a classification
    summary, but the attached Ag43 review is inappropriate support. The graph makes
    a stronger intrinsic-hazard assignment claim than the inspected authorities support.
  evidence_ids:
  - ag43-reused
  - bmbl-reused
  - springer
  - record
- assessment_id: hierarchy
  area: consistency
  topic: 'Native checklist: broader parent and predicate identity'
  outcome: supported
  target_ids:
  - METPO:1001103
  summary: BSL2 belongs under the local biosafety-level class, consistent with inspected
    frameworks. rdfs:subClassOf direction is correct; its attached Ag43 citation is
    still misplaced. Proposed confers identity does not itself validate an administrative
    assignment meaning.
  evidence_ids:
  - local-identity
  - local-model
  - bmbl-reused
- assessment_id: category
  area: representation
  topic: 'Native checklist: classification, node types and conditions'
  outcome: concern
  target_ids:
  - METPO:1001103
  summary: NONMECHANISTIC scope is appropriate. Several BIOLOGICAL_PROCESS nodes actually
    describe hazard/agent/capacity concepts. An unqualified trait-node control summary
    conflicts with conditional wording elsewhere in the same record.
  evidence_ids:
  - record
  - local-model
  - springer
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: taxonomic and study context'
  outcome: concern
  target_ids:
  - METPO:1001103
  summary: The S. aureus paper directly labels that organism BSL2 in its laboratory
    context. The Salmonella paper documents one Enteritidis strain/activity in a BSL2
    facility, while the record note drops that scope. Both species taxon IDs resolve.
  evidence_ids:
  - example-saureus
  - example-senterica
  - taxa
  dimensions:
  - name: example_scope
    value: S. aureus laboratory classification; S. enterica Enteritidis ATCC13076
      in one study/facility
    definition: Scope of the inspected evidence, not universal containment assignment
      for every strain/activity.
    evidence_ids:
    - example-saureus
    - example-senterica
  - name: authority_context
    value: 2019 biobank chapter based on BMBL5; 2020 Australian-context article; BMBL6
      and WHO LBM4 overview
    definition: Specific source frameworks/editions; no current legal or all-jurisdiction
      claim.
    evidence_ids:
    - springer
    - pathol
    - bmbl-reused
    - who-reused
- assessment_id: evidence
  area: evidence
  topic: 'Native checklist: references, source types and provenance'
  outcome: concern
  target_ids:
  - METPO:1001103
  summary: All active identifiers and relevant source text were verified. Sources
    include a protein review, a contextual classification article, a biobank chapter,
    a laboratory-method paper and a primary study reporting facility context. Generic
    repeated snippets do not establish classification support; six additional edges
    omit snippets and require precise source locators when curated.
  evidence_ids:
  - ag43-reused
  - pathol
  - springer
  - example-saureus
  - example-senterica
  - record
  - check-biosafety-level-2-snippets-network
- assessment_id: graph
  area: graph
  topic: 'Native checklist: all nodes and edges'
  outcome: concern
  target_ids:
  - METPO:1001103
  summary: All 10 nodes and 8 edges were assessed. The separate procedure/control
    component is permissible for NONMECHANISTIC scope. Classification assignment is
    contextual, not a direct biological realization; the graph should preserve that
    distinction without adding mechanisms.
  evidence_ids:
  - record
  - local-model
  - ag43-reused
  - pathol
  - springer
  - bmbl-reused
  details: 'Zero-based edge ledger: 0 unsupported attached Ag43 citation and deterministic
    assignment; 1 hierarchy supported but citation misplaced; 2 risk-group association
    can inform assessment but are-assigned wording implies unsupported equivalence;
    3 hazard relevance supported as one contextual input; 4 transmission relevance
    supported but categorical escalation drops source/record severity and activity
    qualifications; 5 broad conditional control relationship supported, while exclusive
    subtype wording exceeds its nearest chapter passage; 6 qualitative protection
    relation supported with no quantified effect asserted; 7 administrative access
    relation supported in the chapter context, not as a universal legal mandate. No
    operational table contents or procedural advice are reproduced.'
- assessment_id: discussion
  area: consistency
  topic: 'Native checklist: gap premises, inference and datasets'
  outcome: concern
  target_ids:
  - METPO:1001103
  summary: Anchors resolve and historical scan snippets are correctly excluded from
    support. The authored discussion nevertheless makes unsupported universal statements
    about the evidence gap and draws risk/classification conclusions from an exposure
    proxy. No dataset is asserted; the review does not extend or endorse the proposed
    experiment.
  evidence_ids:
  - record
  - historical-scan
  - springer
  - bmbl-reused
- assessment_id: status
  area: provenance
  topic: 'Native checklist: status, history and native checks'
  outcome: unknown
  target_ids:
  - METPO:1001103
  summary: Focused schema/strict checks and corpus integrity checks pass within scope.
    Agent assistance is disclosed. Neither seed metadata nor captured AI curation
    establishes historical human sign-off for REVIEWED.
  evidence_ids:
  - record
  - local-owners
  - check-biosafety-level-2-validate
  - check-biosafety-level-2-strict
  - check-validate-history
findings:
- finding_id: classification-citation
  issue_key: biosafety-level-2-classification-citation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Ag43 review does not substantiate the definition or classification edges
  description: The exact cited article is a protein-specific E. coli review. Inspected
    identity and abstract do not establish the biosafety definition, moderate-hazard
    assignment or subclass assertion. A generic two-word snippet cannot supply that
    missing support.
  target_ids:
  - METPO:1001103
  field_paths:
  - definition_source
  - evidence[0]
  - causal_graphs[0].edges[0].evidence
  - causal_graphs[0].edges[1].evidence
  evidence_ids:
  - ag43-reused
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: automatic-assignment
  issue_key: biosafety-level-2-automatic-assignment
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Hazard and risk-group descriptions imply automatic level assignment
  description: The graph describes hazard as yielding BSL2, RG2 agents as assigned
    to BSL2, and transmission alone as escalating beyond it. The cited chapter explicitly
    distinguishes risk group from laboratory level; the classification article itself
    includes work/activity context. Those sources support contextual inputs, not the
    implied sufficient rules.
  target_ids:
  - METPO:1001103
  field_paths:
  - causal_graphs[0].description
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].nodes[3].description
  - causal_graphs[0].edges[0]
  - causal_graphs[0].edges[2].description
  - causal_graphs[0].edges[4].description
  evidence_ids:
  - pathol
  - springer
  - bmbl-reused
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Original inherited ontology identity/definition; preserve provenance rather
      than force regeneration
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: unsupported-discussion-premises
  issue_key: biosafety-level-2-unsupported-discussion-premises
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Discussion asserts an unverified evidence gap and overstates what its proxy
    establishes
  description: The record supplies no source for universal claims that one control
    determines most work, that relevant lists precede measurement, or that the relation
    has never been measured. Its stated surrogate readout does not itself establish
    infectious dose or prove the whole control boundary correct/incorrect. Historical
    off-topic references are properly disclaimed and cannot support these assertions.
  target_ids:
  - METPO:1001103
  field_paths:
  - discussions[0].rationale
  - discussions[0].proposed_experiments[0].decision_criterion
  - discussions[0].proposed_experiments[0].would_support
  - discussions[0].proposed_experiments[0].would_refute
  evidence_ids:
  - record
  - historical-scan
  - springer
  - bmbl-reused
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion PLAN and replay logic; authorized corrections must
      consider both record and source
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: example-study-scope
  issue_key: biosafety-level-2-example-study-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Salmonella example note loses the study strain and activity scope
  description: The cited paper reports one Enteritidis strain and study in a BSL2
    facility. The parent-species identifier is correct, but the bare classification
    note does not retain the evidence context. The example can remain informative
    without implying universality.
  target_ids:
  - METPO:1001103
  field_paths:
  - canonical_examples[1].note
  evidence_ids:
  - example-senterica
  - taxa
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: conditional-control-summary
  issue_key: biosafety-level-2-conditional-control-summary
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Unqualified summary conflicts with conditional source and record wording
  description: The trait-node description declares cabinet use required without a
    condition, whereas the cabinet node, edge and discussion use conditional scope.
    The edge also states an exclusive equipment-subtype formulation not established
    by the nearest cited chapter passage. Reconcile conceptual scope rather than turning
    a summary into a universal operational rule.
  target_ids:
  - METPO:1001103
  field_paths:
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].edges[5].description
  - causal_graphs[0].edges[5].evidence
  evidence_ids:
  - record
  - springer
  - pathol
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: node-semantics
  issue_key: biosafety-level-2-node-semantics
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Several biological-process nodes describe attributes or agents
  description: moderate_pathogen_hazard, risk_group_2_pathogen and pathogenicity describe
    respectively a property collection, an agent and a capacity, while all use BIOLOGICAL_PROCESS.
    A permissive type gate for confers does not establish that an administrative classification
    is a biological trait realization.
  target_ids:
  - METPO:1001103
  field_paths:
  - causal_graphs[0].nodes[2].node_type
  - causal_graphs[0].nodes[3].node_type
  - causal_graphs[0].nodes[4].node_type
  evidence_ids:
  - record
  - local-model
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: repair-classification-evidence
  description: Reassess the retained classification claims and replace or remove unsupported
    attributions using inspected authority or documentary evidence.
  finding_ids:
  - classification-citation
  target_ids:
  - METPO:1001103
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Verify nearest-claim support and exact bibliography independently of the source
    title.
  - Use precise source/edition locators and checked short quotations where appropriate.
  - After authorized curation run focused validate, validate-strict, verify-snippets
    and applicable qc.
- action_id: bound-assignment-statements
  description: Preserve the distinction between agent hazard, risk group, work context
    and containment classification in the retained record.
  finding_ids:
  - automatic-assignment
  target_ids:
  - METPO:1001103
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Original inherited ontology identity/definition; preserve provenance rather
      than force regeneration
  acceptance_checks:
  - Remove unsupported sufficient-condition or universal escalation implications without
    issuing handling recommendations.
  - Qualify claims to inspected authority/edition and contextual scope; preserve inherited
    ontology provenance.
  - Use guarded curation/history and run strict, applicable graph/reference checks
    and qc after authorized edits.
- action_id: qualify-discussion-claims
  description: Source and bound the asserted knowledge gap and distinguish an exposure
    proxy from risk or classification evidence.
  finding_ids:
  - unsupported-discussion-premises
  target_ids:
  - METPO:1001103
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion PLAN and replay logic; authorized corrections must
      consider both record and source
  acceptance_checks:
  - Use a documented bounded literature search before retaining any absence-of-measurement
    claim.
  - Remove conclusions not entailed by the stated evidence; this review proposes no
    experiment or operational modification.
  - Reconcile maintained discussion PLAN and replay behavior so later regeneration
    cannot restore unsupported text.
  - Run focused strict validation and applicable qc after authorized correction.
- action_id: retain-example-context
  description: Qualify the Salmonella example to the documented strain/study context.
  finding_ids:
  - example-study-scope
  target_ids:
  - METPO:1001103
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve the distinction between species identifier, strain and observed facility/activity
    context.
  - Do not infer a universal classification or add unsupported experimental detail.
  - Run focused strict and reference checks after authorized curation.
- action_id: align-summary-scope
  description: Make the classification summary and nearest evidence consistent with
    their conditional authority context.
  finding_ids:
  - conditional-control-summary
  target_ids:
  - METPO:1001103
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Read the node, edge, evidence and discussion together and retain consistent qualifications.
  - Do not infer exclusive or universal operational requirements from summary prose.
  - Run focused strict validation after authorized wording changes.
- action_id: review-node-entities
  description: Review intended entities against the schema and proposal semantics;
    choose accurate representation or document the precise schema gap.
  finding_ids:
  - node-semantics
  target_ids:
  - METPO:1001103
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/biosafety_level_2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Do not select a merely similar term or invent a biological mechanism to satisfy
    a type gate.
  - Retain NONMECHANISTIC classification context.
  - Run strict and applicable graph/grounding checks after authorized edits.
limitations:
- Ag43 was inspected at title/abstract level; full text was unavailable, and no exhaustive
  full-text absence claim is made.
- The other four active references had relevant full-text passages inspected. A failed
  Europe PMC S. aureus fetch was resolved by NCBI BioC and PMC HTML.
- Authority sources are specific historical editions and contexts, not a current legal
  or all-jurisdiction classification determination. WHO overview was inspected; its
  core PDF was not.
- No quantitative protective efficacy, infectious-dose estimate, procedure recommendation
  or suitability assessment was performed. The existing proposed experiment is assessed
  only for evidentiary logic.
- Taxonomy identity is separate from containment assignment. Historical scan references
  remain provenance only.
- Human sign-off for REVIEWED was not independently established; corpus product-adapter
  skips and earlier diagnostic failures remain explicit.
- Review work was interrupted between original capture/source inspection and final
  integration; actual start/finish timestamps retain that interval.
notes:
- No trait, history, writer, ontology or generated page changed. Only this new structured
  review is saved.
- All source-capture expansions preserved original hashes; source identity and local
  graph semantics were assessed separately.
- Correction owners identify future authorized work; no outbound communication or
  operational change is performed.
tags:
- record-review
- biosafety-level-2
- ecology
- needs-curation
```
