# Evidence and ontology review of saprotrophy (traitmech:000055)

- Review: 20261021T074148Z-saprotrophy
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T07:35:16Z
- Finished UTC: 2026-10-21T07:41:48Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The saprotrophy concept, phenotype parent, canonical soil-model context and all eleven source snippets are supported. Two major findings concern three external relation mismatches and a plant-scoped InterPro family used for a microbial laccase node. One minor finding concerns the missing human-acceptance link in inspected local provenance. Fourteen nodes and nine edges were reviewed; genomic example evidence and fungal regulatory qualifications remain explicit limitations.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Sixth batch003 target in lexicographic path order after the saved rhizosphere-association review; one entire previously uncovered TraitRecord.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000055 | data/traits/ecology/saprotrophy.yaml | maintained | saprotrophy |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000055 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000055 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000055 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | traitmech:000055 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | traitmech:000055 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000055 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000055 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | traitmech:000055 | The selected record validates. |
| Focused strict validation | passed | True | traitmech:000055 | One file scanned; zero strict errors. |
| Initial snippet command invocation | failed | False | traitmech:000055 | An incorrect recipe name exited1 without verifying snippets. The corrected documented recipe below supersedes this invocation. |
| Focused snippet verification | passed | True | traitmech:000055 | Eleven snippets over five references: two VERIFIED and nine NOT_IN_ABSTRACT. Abstract nonmatches are inconclusive; manual full-text inspection is recorded separately. |
| Structured-source adapter availability | unavailable | False | traitmech:000055 | No usable runner in the bounded local search; official API fallback completed. |
| Official expression-source cross-check | passed | False | traitmech:000055 | Inspected s_coelicolor/modulome478 catalog, exact-term searches, two sampled genes and two relevant component summaries; no causal or universal inference. |

## Scientific And Domain Assessments

### Native checklist: fallback, label, synonyms and hierarchy

identity: supported. Targets: traitmech:000055.

Fallback000055 and the proposal identify one trophic lifestyle. Related synonyms are not asserted as exact lexical equivalences; phenotype is a broader parent.

### Native checklist: ECOLOGY/CLASS and NONMECHANISTIC context

representation: supported. Targets: traitmech:000055.

The ecological class and heterogeneous contextual graph are appropriate. Optional datasets, strain-specific proteins and a complete connected molecular route are not required.

### Native checklist: all grounded chemicals and enzymes

grounding: concern. Targets: traitmech:000055.

Chemical grounds and the enzyme-activity GO term resolve consistently with native policy. The laccase family is narrower than the microbial context asserted by the record.

### Native checklist: all nine edge roles and directions

consistency: concern. Targets: traitmech:000055.

Edges0/2/8 have external relation meaning conflicts; their local permissive validation does not validate those meanings. Edge1 consumes and edge4 derives into retain valid directions. Proposed hydrolysis/oxidation predicates retain their distinct meanings.

### Native checklist: optional computational expression context

evidence: supported. Targets: traitmech:000055.

The official matching-name dataset was inspected with explicit strain and inference limits. Gene/module membership is not promoted to proof of this trait.

### Native checklist: human acceptance and maintained owners

provenance: concern. Targets: traitmech:000055.

The record and matching repository history preserve AI-assisted provenance, including earlier evidence repairs, but the inspected target-specific fields do not link human scientific acceptance.

### Native checklist: dead-substrate lifestyle and source scope

evidence: supported. Targets: traitmech:000055.

Detrital resource use and decomposition/carbon cycling are supported. Schimel provides soil ecological discussion rather than a formal lexical definition; the model-organism source independently supports saprophytic decomposition.

### Native checklist: canonical species, strain and hydrolase evidence tier

evidence: concern. Targets: traitmech:000055.

Species1902 and strain100226 resolve consistently with the paper’s A3(2) context. The ecological example is supported; the hydrolase passage is a genomic prediction, which should remain explicit when expanding or reusing the example.

### Native checklist: all record and edge claims

evidence: supported. Targets: traitmech:000055.

All eleven snippets are verbatim after ordinary PDF text normalization. All nine edges have source-supported contextual biological claims; relation and family-grounding errors are assessed separately. The collective enzyme nodes do not assert identical activities for every member.

### Native checklist: contextual enzyme and regulatory qualifications

consistency: supported. Targets: traitmech:000055.

NONMECHANISTIC scope permits a heterogeneous sketch. The fungal cellulase/hemicellulase repression context should be preserved, but no class-wide universal CCR claim is inferred solely from the broad lignocellulolytic label. The lignin oxidative edge does not imply that GO activity identity alone proves every reaction detail.

### Native checklist: optional content and structural integrity

completeness: supported. Targets: traitmech:000055.

The ecological definition, example and source-backed context are present. All graph endpoints resolve. There are no asserted pathway-context links requiring target-specific checks, and optional protein examples, discussions or datasets are not prerequisites for this NONMECHANISTIC class.

## Findings

### relation-semantics: Three edge groundings conflict with their endpoint meanings

major / open / confirmed; issue key: saprotrophy-relation-semantics.

Edge0 places the saprotrophy trait itself in RO enables’ material-executor role. Edge2 sends RO contributes to to soluble chemical products, rather than an enabled activity/function. Edge8 places glucose in RO negative regulation’s process-to-process subject role. These are external semantic conflicts, not failures of the passing local schema. The process-consuming-substrate edge1 and substrate-to-product edge4 are not part of this finding.

### laccase-family-scope: Plant laccase family used for a microbial laccase node

major / open / confirmed; issue key: saprotrophy-laccase-family-scope.

Node10 is grounded to IPR017761 while edge6 notes identify a fungal and bacterial ligninolytic context. The current entry/model descriptions and taxonomic coverage establish a plant protein family. Reusing its matching label does not ground the intended broader microbial enzyme identity. This finding concerns this family assignment; it does not imply laccase activity is confined to plants.

### human-acceptance-link: Human scientific acceptance is not linked in inspected local provenance

minor / open / confirmed; issue key: saprotrophy-human-acceptance-link.

The fourteen target events and matching repository history disclose AI work. None of the inspected target-specific fields identifies the human acceptance required for REVIEWED. This is a bounded documentation finding, not proof that no human review occurred elsewhere.

## Recommended Actions And Acceptance Checks

### repair-relations

In a separately authorized curation, preserve each source-supported biological claim while reconciling the three relations and node roles with authoritative meanings. Reconcile maintained writer/replay expectations and shared mapping scope.

- Verify the chosen relation definitions and endpoint roles independently.
- Run focused validate and validate-strict, relevant predicate/graph audits and writer tests, then just qc.
- Append native record and repository curation history; regenerate affected derived artifacts through maintained recipes.

### repair-laccase-ground

Resolve an exact taxon-appropriate family/function grounding for the stated microbial context, or retain an explicit justified label-only decision when no exact match is verified. Reconcile the shared node mapping.

- Verify the replacement identifier’s definition and scope, rather than label alone.
- Do not substitute a broad multicopper-oxidase family or a token species-specific accession as an unverified exact match.
- Run focused strict validation, applicable grounding/protein audits and just qc; record curation history.

### link-acceptance

Locate and link existing human scientific acceptance or obtain it through the established curation process; preserve AI history and reassess status if acceptance remains unavailable.

- A human acceptance reference identifies this record/revision and scientific scope.
- Automated review validation is not used as human sign-off.

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
| check-saprotrophy-validate | /private/tmp/traitmech-record-sweep-003.4opxlhgf/saprotrophy-validate.log; Executed 2026-10-21T07:35:47Z through 2026-10-21T07:35:50Z; metadata saprotrophy-validate.json | context_only | The selected record validates. |
| check-saprotrophy-strict | /private/tmp/traitmech-record-sweep-003.4opxlhgf/saprotrophy-strict.log; Executed 2026-10-21T07:35:47Z through 2026-10-21T07:35:52Z; metadata saprotrophy-strict.json | context_only | One file scanned; zero strict errors. |
| check-saprotrophy-snippets | /private/tmp/traitmech-record-sweep-003.4opxlhgf/saprotrophy-snippets.log; Executed 2026-10-21T07:36:07Z through 2026-10-21T07:36:07Z; metadata saprotrophy-snippets.json | context_only | An incorrect recipe name exited1 without verifying snippets. The corrected documented recipe below supersedes this invocation. |
| check-saprotrophy-snippets-corrected | /private/tmp/traitmech-record-sweep-003.4opxlhgf/saprotrophy-snippets-corrected.log; Executed 2026-10-21T07:36:20Z through 2026-10-21T07:36:29Z; metadata saprotrophy-snippets-corrected.json | context_only | Eleven snippets over five references: two VERIFIED and nine NOT_IN_ABSTRACT. Abstract nonmatches are inconclusive; manual full-text inspection is recorded separately. |
| record | data/traits/ecology/saprotrophy.yaml; Entire record, fourteen nodes, nine edges and fourteen history events | partial | The record identifies nutrition from nonliving organic matter and retains a NONMECHANISTIC contextual graph. External relation and laccase-family meanings require curation. |
| identity | data/raw/metpo.owl; proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv; Complete RDF label/literal scan, active and deprecated classes; saprotrophy proposal row | supports | No exact active or deprecated saprotrophy class was found in the captured METPO release. Fallback000055 corresponds to proposed1007654. Parent1000059 is active phenotype; proposed chemical-interaction predicates2007808/2007803 are not upstream minted terms. |
| parent | data/traits/upper/phenotype.yaml; Entire context record, identifier and definition used for hierarchy | supports | The phenotype parent is broader than an organismal trophic lifestyle. The context parent is not an additional review target. |
| identifiers | QuickGO; ChEBI; NCBI Taxonomy; Exact live term responses listed in live-identity-receipts.json | supports | GO0016689 is active manganese peroxidase activity. Four ChEBI identifiers match the intended chemicals;18246 has cellulose as a synonym of its canonical beta-linked glucan label. NCBITaxon1902 resolves to Streptomyces coelicolor. Identifier resolution is distinct from source attribution. |
| protein-policy | docs/GROUNDING_POLICY.md; Section2 type-to-semantics table and Section4 graph scope | supports | Native policy permits taxon-agnostic enzyme activity grounds on legacy GENE_OR_PROTEIN nodes. GO MF aspect alone is not an error. Broad contextual enzyme groups may remain explicitly label-only, and this NONMECHANISTIC graph does not require token protein instances. |
| interpro | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017761/; Entry description, integrated TIGR03389, hierarchy and total protein count | refutes | The assigned family is a plant laccase/laccase-like family, rather than a generic family covering the record’s fungal and bacterial laccase context. The same label does not establish exact family identity. |
| interpro-scope | InterPro official taxonomy filters and NCBIfam TIGR03389 endpoint; Exact endpoint URLs/statuses in interpro-scope-receipts.json | refutes | The green-plant filter reports10650 proteins, equal to the entry total; the bacterial and fungal filters return204. The integrated model description also specifies plant proteins. This verifies the current family scope, not an assertion that laccase activity is exclusive to plants. |
| relations | Cached authoritative RO database; captured Biolink model; v9 predicate proposal; Recursive definitions/domains/ranges and explicit contextual chemical relations | partial | The external meanings of enables, contributes to and negatively regulates conflict with endpoints at edges0/2/8. Biolink consumes expressly allows a process consuming an entity, so edge1 is compatible. RO0001001 derives into correctly runs substrate-to-product at edge4. |
| shape | Read-only graph inspection; All node identifiers and edge endpoint references | supports | Fourteen unique nodes and nine edges; all endpoints resolve. This shape check is not scientific entailment. |
| owners | scripts/review_saprotrophy_graph_183.py; scripts/repair_pr664_adversarial_review.py; Source-specific before/after record and edge replacements; shared repair import and saprotrophy event dispatch | supports | The maintained source-specific writer embeds the current evidence and predicate choices; the later shared repair consumes those replacements. Future corrections must account for replay and drift behavior, rather than editing generated pages. |
| provenance | Target-specific local history and review inventory; Entire target history; all history YAML and structured review.yaml exact target matches via ignored-inclusive pathlib traversal | partial | Fourteen target events disclose AI assistance; the matching repository history identifies an AI agent. No human scientific acceptance link was identified in the inspected target-specific local fields. Private/remote approval is unknown. |
| local-search | Local ownership and provenance search; Identifier/label/slug search in scripts, history, mappings, reviews and research/traits/ecology | context_only | The ignored-inclusive search identifies the target-specific writer, repair writer, repository history and research provenance. Source-context mentions in other reviews are not target coverage. |
| status-rule | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md; Status/audit checklist and Verification status gate | supports | REVIEWED requires human curator sign-off. Automated review history and valid schema shape do not establish that acceptance. |
| runner | Structured-source runner discovery; Fresh bounded PATH/install/project search including ignored files | context_only | No usable kg-microbe-sources runner was identified in the declared local scope. Official API fallback was used. This is not a disk-wide absence assertion. |
| expression | https://imodulondb.org/api/datasets/s_coelicolor/modulome478/meta; Catalog, six exact-term searches, two first-returned gene membership tables and components88/91 | context_only | The matching named species dataset contains478 samples and multiple strain labels. Component88 is Hydrolytic enzymes with22 members;91 is Cellobiose utilization with4. These inspected computational annotations provide bounded context, not proof of saprotrophy, substrate specificity or a fungal regulatory mechanism. Four query nonmatches and no positive module flags for the two sampled genes are not negative biology. |
| ledger | Independent documentary ontology assessment; All fourteen nodes and nine edges, exact zero-based locators | partial | Independent inspection agrees with three relation mismatches and one laccase-family scope mismatch. Current species1902 and strain100226 resolve with the latter beneath the former. No extra MnP activity-type finding is made. |
| bibliography | Europe PMC, publisher and institutional full text; All six cited publication identities and all eleven snippet occurrences | supports | All six identities resolve and every current snippet was located in cited full text after ordinary whitespace/discretionary line-break normalization. Relevant passages, not every section, were inspected. Original retrieval timestamps, failed alternatives and reused-source hashes are retained. |
| schimel | https://pmc.ncbi.nlm.nih.gov/articles/PMC3458434/; Abstract; Consequences of soil community composition / Fate controlling step: allocation / Extracellular enzymes; Scaling up in space, first paragraph; DOI10.3389/fmicb.2012.00348 | supports | Supports detrital resources, extracellular decomposition and carbon cycling. This is ecological support rather than a glossary definition. Qualifications about microbial-composition effects across soil compartments do not contradict the record’s broad decomposition context. |
| fierer | https://www.fiererlab.org/s/Fierer_Nat_Rev_Micro_2017.pdf; PDFp1 opening body paragraph; DOI10.1038/nrmicro.2017.87 | supports | The top-level snippet is exact and supports general ecosystem roles of soil microbes. The record’s note does not assign these roles exclusively to saprotrophs. |
| example | https://www.nature.com/articles/417141a.pdf; PMID12000953 / DOI10.1038/417141a; PDFp1/printed141 introduction and p4/printed144 A plethora of proteins | partial | The paper supports the model A3(2) soil saprotroph context; the sequenced strain is its M145 derivative. Its hydrolase passage describes predicted potentially secreted proteins, so this citation is genomic support rather than a new direct secretion assay. |
| wang | https://pmc.ncbi.nlm.nih.gov/articles/PMC11104273/; sec7 Preferences for carbon and energy sources, cross-feeding paragraph; DOI10.1093/ismejo/wrae073 | supports | Supports extracellular reaction products and their diffusion to other microbial groups. The source treats predominance of this cross-feeding mode as an assumption; the current edge makes the narrower existence/contribution claim. |
| gurovic | https://ri.conicet.gov.ar/bitstream/handle/11336/202386/CONICET_Digital_Nro.571f72b9-484c-4a32-b3b8-fe4023801a8a_E.pdf?isAllowed=y&amp;sequence=5; DOI10.1093/jambio/lxac002; PDFp2 enzyme discussion, p3 Figure1 and following text, pp4–6 sugar regulation; initial browser read completed by07:36:38Z, focused follow-up by07:38:39Z | supports | All five snippets match the inspected browser PDF. The contextual cellulose system and oxidative enzyme claims are supported. Glucose repression is discussed for fungal cellulolytic expression with taxon/substrate qualifications; the broad target label is not by itself an assertion that all ligninolytic branches are repressed. |
| cragg | https://pure.port.ac.uk/ws/files/3141775/Lignocellulose_degradation_mechanisms_across_the_Tree_of_Life.pdf; DOI10.1016/j.cbpa.2015.10.018; PDFp2/printed109 Enzymatic depolymerisation of cellulose and hemicelluloses, first paragraph | supports | The exact snippet and adjacent text support collective CAZyme action, including glycosidic-bond cleavage. The record’s note selects hemicellulose-active enzymes; it does not require every CAZyme to share that activity. |

## Limits And Additional Notes

- The Gurovic full text was inspected through a public browser PDF; local download attempts failed, and no downloaded-byte hash is asserted for that source.
- Relevant passages were inspected for all six sources, not every section or all underlying primary experiments. Review articles support contextual claims without independently replicating them.
- The example’s hydrolase passage is genomic prediction, not a direct secretion assay. Its model-organism ecology is supported.
- The glucose regulatory context concerns fungal cellulolytic/hemicellulolytic expression; species, substrate and condition qualifications should be preserved. No universal repression defect is inferred solely from the broad node label.
- The official expression dataset uses multiple strain labels; sampled gene/module annotations do not establish ecological phenotype, secretion, substrate specificity or fungal mechanism.
- Optional structured-source runner unavailable; official API fallback inspected. Bounded query or membership nonmatches are not negative biological evidence.
- The initial incorrect snippet recipe invocation failed without scientific output and is retained; the corrected documented recipe and manual full-text checks completed.
- External ontology semantics are distinct from permissive local validation. No formal reasoner error is claimed. Pending METPO proposal IDs are not presented as minted upstream identities.
- Private or remote human acceptance was not searched. The provenance finding concerns documentation in the inspected local target-specific fields.
- Only this new review bundle is authorized scientific output here; no record, writer, mapping, status, history or generated page was curated.
- All field paths use zero-based indices.
- Severity retains the native rubric: material relation/family errors are major; bounded acceptance documentation is minor.
- The independent ontology ledger and source ledger agree on the distinct positive checks; no missing-mechanism finding is derived from optional content.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T074148Z-saprotrophy
kind: record
repository: CultureBotAI/TraitMech
title: Evidence and ontology review of saprotrophy (traitmech:000055)
started_at: '2026-10-21T07:35:16Z'
finished_at: '2026-10-21T07:41:48Z'
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
summary: The saprotrophy concept, phenotype parent, canonical soil-model context and
  all eleven source snippets are supported. Two major findings concern three external
  relation mismatches and a plant-scoped InterPro family used for a microbial laccase
  node. One minor finding concerns the missing human-acceptance link in inspected
  local provenance. Fourteen nodes and nine edges were reviewed; genomic example evidence
  and fungal regulatory qualifications remain explicit limitations.
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
  - path: data/traits/ecology/saprotrophy.yaml
    sha256: 74c1e3065e0ce9dfc86b1b8725061383de4e8800dd5e7c02f48179c85fa3b6f4
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
  - path: history/records/saprotrophy/2026-09-04T070000Z-codex-1d076e.yaml
    sha256: 848098e8b221461b7da318ff386e53713c9c2dfcb3304b7813c147db8067299b
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
  - path: proposals/metpo_traitmech_v9/metpo_proposal_properties_robot.tsv
    sha256: 5ae84dd1351a4bec39adf7bcd5b3a8982af2e95fbccd0b53c0efa3efbfc89b0e
    role: context
  - path: proposals/metpo_traitmech_v9/proposal.md
    sha256: 85fde22f4733863188b437cfcf7552a31fea07ad1d32c0400cf493295c1e1156
    role: context
  - path: research/traits/ecology/saprotrophy-deep-research-falcon.md
    sha256: a6e9c428c1357f23d55a2cec4e916f5b42a09790ff5c3e93c048a400198128fd
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
  - path: scripts/repair_pr664_adversarial_review.py
    sha256: 5717a89bee383aa0e12aec9bf30434ccff74efcbe64684d13ef9b290b1accf96
    role: context
  - path: scripts/review_saprotrophy_graph_183.py
    sha256: f6035be5ee0329d94c35fb6b111be3bc6c8ecb518daaa314008c52f60bc656d1
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
- target_id: traitmech:000055
  path: data/traits/ecology/saprotrophy.yaml
  label: saprotrophy
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/saprotrophy.yaml
    role: Maintained scientific record
  - repository: CultureBotAI/TraitMech
    path: scripts/review_saprotrophy_graph_183.py
    role: Maintained source-specific review writer
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Maintained subsequent evidence-repair writer
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Shared node mapping
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Sixth batch003 target in lexicographic path order after the saved rhizosphere-association
    review; one entire previously uncovered TraitRecord.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000055
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000055
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
  - traitmech:000055
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
  - traitmech:000055
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
  - traitmech:000055
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
  - traitmech:000055
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
  - traitmech:000055
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
  - traitmech:000055
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
- check_id: saprotrophy-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000055
  command: just validate data/traits/ecology/saprotrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The selected record validates.
  evidence_ids:
  - check-saprotrophy-validate
- check_id: saprotrophy-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000055
  command: just validate-strict data/traits/ecology/saprotrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero strict errors.
  evidence_ids:
  - check-saprotrophy-strict
- check_id: saprotrophy-snippets
  name: Initial snippet command invocation
  status: failed
  required: false
  target_ids:
  - traitmech:000055
  command: just verify-evidence-snippets data/traits/ecology/saprotrophy.yaml
  exit_code: 1
  expected_exit_code: 0
  summary: An incorrect recipe name exited1 without verifying snippets. The corrected
    documented recipe below supersedes this invocation.
  evidence_ids:
  - check-saprotrophy-snippets
- check_id: saprotrophy-snippets-corrected
  name: Focused snippet verification
  status: passed
  required: true
  target_ids:
  - traitmech:000055
  command: just verify-snippets --record data/traits/ecology/saprotrophy.yaml --out
    /private/tmp/traitmech-record-sweep-003.4opxlhgf/saprotrophy-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Eleven snippets over five references: two VERIFIED and nine NOT_IN_ABSTRACT.
    Abstract nonmatches are inconclusive; manual full-text inspection is recorded
    separately.'
  evidence_ids:
  - check-saprotrophy-snippets-corrected
- check_id: structured-source-runner
  name: Structured-source adapter availability
  status: unavailable
  required: false
  target_ids:
  - traitmech:000055
  summary: No usable runner in the bounded local search; official API fallback completed.
  evidence_ids:
  - runner
- check_id: expression-context
  name: Official expression-source cross-check
  status: passed
  required: false
  target_ids:
  - traitmech:000055
  summary: Inspected s_coelicolor/modulome478 catalog, exact-term searches, two sampled
    genes and two relevant component summaries; no causal or universal inference.
  evidence_ids:
  - expression
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-saprotrophy-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/saprotrophy-validate.log
  locator: Executed 2026-10-21T07:35:47Z through 2026-10-21T07:35:50Z; metadata saprotrophy-validate.json
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: The selected record validates.
  snapshot_sha256: 7091780c1e021adb42d2e684247bbb7f4e8b79614a15ec1d008f4011366dc03f
- evidence_id: check-saprotrophy-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/saprotrophy-strict.log
  locator: Executed 2026-10-21T07:35:47Z through 2026-10-21T07:35:52Z; metadata saprotrophy-strict.json
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: One file scanned; zero strict errors.
  snapshot_sha256: a5294da277c2ff1bcfd003fd05151dc2506e4a53bb911a77b5c8df61520358f6
- evidence_id: check-saprotrophy-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/saprotrophy-snippets.log
  locator: Executed 2026-10-21T07:36:07Z through 2026-10-21T07:36:07Z; metadata saprotrophy-snippets.json
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: An incorrect recipe name exited1 without verifying snippets. The corrected
    documented recipe below supersedes this invocation.
  snapshot_sha256: b31fe0d3845b6c3ae43611123cd4a8ede64a4f861407f6c87121158d93cb384b
- evidence_id: check-saprotrophy-snippets-corrected
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/saprotrophy-snippets-corrected.log
  locator: Executed 2026-10-21T07:36:20Z through 2026-10-21T07:36:29Z; metadata saprotrophy-snippets-corrected.json
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: 'Eleven snippets over five references: two VERIFIED and nine NOT_IN_ABSTRACT.
    Abstract nonmatches are inconclusive; manual full-text inspection is recorded
    separately.'
  snapshot_sha256: 47b381017743f74c78a07a755d31ba19e142cecf876d7aaab656a8825c58b883
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/saprotrophy.yaml
  locator: Entire record, fourteen nodes, nine edges and fourteen history events
  accessed_at: '2026-10-21T07:41:48Z'
  support: partial
  summary: The record identifies nutrition from nonliving organic matter and retains
    a NONMECHANISTIC contextual graph. External relation and laccase-family meanings
    require curation.
  snapshot_sha256: 74c1e3065e0ce9dfc86b1b8725061383de4e8800dd5e7c02f48179c85fa3b6f4
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl; proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
  locator: Complete RDF label/literal scan, active and deprecated classes; saprotrophy
    proposal row
  accessed_at: '2026-10-21T07:36:01Z'
  support: supports
  summary: No exact active or deprecated saprotrophy class was found in the captured
    METPO release. Fallback000055 corresponds to proposed1007654. Parent1000059 is
    active phenotype; proposed chemical-interaction predicates2007808/2007803 are
    not upstream minted terms.
  snapshot_sha256: cf26f4943d55a236b0c26bfb9323d0075c01f91a3fb8b95e616d63a062cf9379
- evidence_id: parent
  kind: record_content
  reference: data/traits/upper/phenotype.yaml
  locator: Entire context record, identifier and definition used for hierarchy
  accessed_at: '2026-10-21T07:41:48Z'
  support: supports
  summary: The phenotype parent is broader than an organismal trophic lifestyle. The
    context parent is not an additional review target.
- evidence_id: identifiers
  kind: authority
  reference: QuickGO; ChEBI; NCBI Taxonomy
  locator: Exact live term responses listed in live-identity-receipts.json
  accessed_at: '2026-10-21T07:36:19Z'
  support: supports
  summary: GO0016689 is active manganese peroxidase activity. Four ChEBI identifiers
    match the intended chemicals;18246 has cellulose as a synonym of its canonical
    beta-linked glucan label. NCBITaxon1902 resolves to Streptomyces coelicolor. Identifier
    resolution is distinct from source attribution.
  snapshot_sha256: d7622977d159eac1297040cc44e8d2b954d7e1711f0aa764d3180646ddc8aa8a
- evidence_id: protein-policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Section2 type-to-semantics table and Section4 graph scope
  accessed_at: '2026-10-21T07:41:48Z'
  support: supports
  summary: Native policy permits taxon-agnostic enzyme activity grounds on legacy
    GENE_OR_PROTEIN nodes. GO MF aspect alone is not an error. Broad contextual enzyme
    groups may remain explicitly label-only, and this NONMECHANISTIC graph does not
    require token protein instances.
- evidence_id: interpro
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017761/
  locator: Entry description, integrated TIGR03389, hierarchy and total protein count
  accessed_at: '2026-10-21T07:36:18Z'
  support: refutes
  summary: The assigned family is a plant laccase/laccase-like family, rather than
    a generic family covering the record’s fungal and bacterial laccase context. The
    same label does not establish exact family identity.
  snapshot_sha256: f4277a4ff9a9b3580e135855001abdaf6c48965f337386eeb730d8500971ef06
- evidence_id: interpro-scope
  kind: authority
  reference: InterPro official taxonomy filters and NCBIfam TIGR03389 endpoint
  locator: Exact endpoint URLs/statuses in interpro-scope-receipts.json
  accessed_at: '2026-10-21T07:38:00Z'
  support: refutes
  summary: The green-plant filter reports10650 proteins, equal to the entry total;
    the bacterial and fungal filters return204. The integrated model description also
    specifies plant proteins. This verifies the current family scope, not an assertion
    that laccase activity is exclusive to plants.
  snapshot_sha256: 12294895d14974d86646f48fd24a407e6b6e4b92da73ecf677d37f8ea21f20e8
- evidence_id: relations
  kind: authority
  reference: Cached authoritative RO database; captured Biolink model; v9 predicate
    proposal
  locator: Recursive definitions/domains/ranges and explicit contextual chemical relations
  accessed_at: '2026-10-21T07:36:02Z'
  support: partial
  summary: The external meanings of enables, contributes to and negatively regulates
    conflict with endpoints at edges0/2/8. Biolink consumes expressly allows a process
    consuming an entity, so edge1 is compatible. RO0001001 derives into correctly
    runs substrate-to-product at edge4.
  snapshot_sha256: ff8ef8034dbf220468304d9cc94a2dc99bb4754c356fc3f8171282d15fa66965
- evidence_id: shape
  kind: validation
  reference: Read-only graph inspection
  locator: All node identifiers and edge endpoint references
  accessed_at: '2026-10-21T07:36:21Z'
  support: supports
  summary: Fourteen unique nodes and nine edges; all endpoints resolve. This shape
    check is not scientific entailment.
  snapshot_sha256: 8c428d80946fba7cce56d1dcbb70b380d3a08f3a14f09dcb9627b77b6f1d21c5
- evidence_id: owners
  kind: record_content
  reference: scripts/review_saprotrophy_graph_183.py; scripts/repair_pr664_adversarial_review.py
  locator: Source-specific before/after record and edge replacements; shared repair
    import and saprotrophy event dispatch
  accessed_at: '2026-10-21T07:41:48Z'
  support: supports
  summary: The maintained source-specific writer embeds the current evidence and predicate
    choices; the later shared repair consumes those replacements. Future corrections
    must account for replay and drift behavior, rather than editing generated pages.
  snapshot_sha256: f6035be5ee0329d94c35fb6b111be3bc6c8ecb518daaa314008c52f60bc656d1
- evidence_id: provenance
  kind: search
  reference: Target-specific local history and review inventory
  locator: Entire target history; all history YAML and structured review.yaml exact
    target matches via ignored-inclusive pathlib traversal
  accessed_at: '2026-10-21T07:37:52Z'
  support: partial
  summary: Fourteen target events disclose AI assistance; the matching repository
    history identifies an AI agent. No human scientific acceptance link was identified
    in the inspected target-specific local fields. Private/remote approval is unknown.
  snapshot_sha256: ba82229eb59df8c552d3db143c0d7b05bd788bf3fd984aeb334df67d71b557e7
  search_scope: All YAML under history and all review.yaml under reviews/structured,
    including hidden/ignored files; exact target path matching. Entire target history
    and its provider header were inspected. No search of private/remote approvals.
- evidence_id: local-search
  kind: search
  reference: Local ownership and provenance search
  locator: Identifier/label/slug search in scripts, history, mappings, reviews and
    research/traits/ecology
  accessed_at: '2026-10-21T07:36:21Z'
  support: context_only
  summary: The ignored-inclusive search identifies the target-specific writer, repair
    writer, repository history and research provenance. Source-context mentions in
    other reviews are not target coverage.
  snapshot_sha256: c5697e13cdd82431cf51a661a10ed9e36551d7f0e3020b6ceeaf89b59f519f9c
  search_scope: Exact rg --no-ignore --hidden command and bounded repository roots
    are retained in the receipt; private/remote approvals and .git internals are outside
    scope.
- evidence_id: status-rule
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md
  locator: Status/audit checklist and Verification status gate
  accessed_at: '2026-10-21T07:41:48Z'
  support: supports
  summary: REVIEWED requires human curator sign-off. Automated review history and
    valid schema shape do not establish that acceptance.
- evidence_id: runner
  kind: search
  reference: Structured-source runner discovery
  locator: Fresh bounded PATH/install/project search including ignored files
  accessed_at: '2026-10-21T07:41:48Z'
  support: context_only
  summary: No usable kg-microbe-sources runner was identified in the declared local
    scope. Official API fallback was used. This is not a disk-wide absence assertion.
  snapshot_sha256: 255ec15986d2ece8ee78c72591e43429c1bb5f22c3326a349667326e3fe1b380
  search_scope: Exact PATH/install/project locations and ignored-inclusive traversal
    are retained in runner-discovery.json; unsearched roots remain unknown.
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets/s_coelicolor/modulome478/meta
  locator: Catalog, six exact-term searches, two first-returned gene membership tables
    and components88/91
  accessed_at: '2026-10-21T07:38:10Z'
  support: context_only
  summary: The matching named species dataset contains478 samples and multiple strain
    labels. Component88 is Hydrolytic enzymes with22 members;91 is Cellobiose utilization
    with4. These inspected computational annotations provide bounded context, not
    proof of saprotrophy, substrate specificity or a fungal regulatory mechanism.
    Four query nonmatches and no positive module flags for the two sampled genes are
    not negative biology.
  snapshot_sha256: 4def472fddb0a46aac1fa60ead63ac85545900c455c2446d232c9dd661b3df47
- evidence_id: ledger
  kind: validation
  reference: Independent documentary ontology assessment
  locator: All fourteen nodes and nine edges, exact zero-based locators
  accessed_at: '2026-10-21T07:39:45Z'
  support: partial
  summary: Independent inspection agrees with three relation mismatches and one laccase-family
    scope mismatch. Current species1902 and strain100226 resolve with the latter beneath
    the former. No extra MnP activity-type finding is made.
  snapshot_sha256: 571004921d511b83cd9f52370e7f4fa8478d195e490ec93e23d400afe540281f
- evidence_id: bibliography
  kind: database
  reference: Europe PMC, publisher and institutional full text
  locator: All six cited publication identities and all eleven snippet occurrences
  accessed_at: '2026-10-21T07:40:55Z'
  support: supports
  summary: All six identities resolve and every current snippet was located in cited
    full text after ordinary whitespace/discretionary line-break normalization. Relevant
    passages, not every section, were inspected. Original retrieval timestamps, failed
    alternatives and reused-source hashes are retained.
  snapshot_sha256: 80d1457511ebd6220a855bfb046945471f1292f37ca143267f4168eb73cc868d
- evidence_id: schimel
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3458434/
  locator: 'Abstract; Consequences of soil community composition / Fate controlling
    step: allocation / Extracellular enzymes; Scaling up in space, first paragraph;
    DOI10.3389/fmicb.2012.00348'
  accessed_at: '2026-10-21T07:36:02Z'
  support: supports
  summary: Supports detrital resources, extracellular decomposition and carbon cycling.
    This is ecological support rather than a glossary definition. Qualifications about
    microbial-composition effects across soil compartments do not contradict the record’s
    broad decomposition context.
  snapshot_sha256: 89c923b73f00409acd56415d94345c8eda63df9453b9a00dc416c47c463c3e85
- evidence_id: fierer
  kind: primary_source
  reference: https://www.fiererlab.org/s/Fierer_Nat_Rev_Micro_2017.pdf
  locator: PDFp1 opening body paragraph; DOI10.1038/nrmicro.2017.87
  accessed_at: '2026-10-21T06:34:33Z'
  support: supports
  summary: The top-level snippet is exact and supports general ecosystem roles of
    soil microbes. The record’s note does not assign these roles exclusively to saprotrophs.
  snapshot_sha256: eb3930ba598e301f098d61bab6f5f4a0047c8b1c55726618cce1494621ac31d4
- evidence_id: example
  kind: primary_source
  reference: https://www.nature.com/articles/417141a.pdf
  locator: PMID12000953 / DOI10.1038/417141a; PDFp1/printed141 introduction and p4/printed144
    A plethora of proteins
  accessed_at: '2026-10-21T07:37:45Z'
  support: partial
  summary: The paper supports the model A3(2) soil saprotroph context; the sequenced
    strain is its M145 derivative. Its hydrolase passage describes predicted potentially
    secreted proteins, so this citation is genomic support rather than a new direct
    secretion assay.
  snapshot_sha256: d77a97e644c2be7fb60ac98ddff856d4981dc39737b076295b38880bdf51b5d5
- evidence_id: wang
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC11104273/
  locator: sec7 Preferences for carbon and energy sources, cross-feeding paragraph;
    DOI10.1093/ismejo/wrae073
  accessed_at: '2026-10-21T07:36:02Z'
  support: supports
  summary: Supports extracellular reaction products and their diffusion to other microbial
    groups. The source treats predominance of this cross-feeding mode as an assumption;
    the current edge makes the narrower existence/contribution claim.
  snapshot_sha256: 8acb85e3b38c709cbd838522d2567c204028decc403d8ccc67390406f4feef52
- evidence_id: gurovic
  kind: primary_source
  reference: https://ri.conicet.gov.ar/bitstream/handle/11336/202386/CONICET_Digital_Nro.571f72b9-484c-4a32-b3b8-fe4023801a8a_E.pdf?isAllowed=y&sequence=5
  locator: DOI10.1093/jambio/lxac002; PDFp2 enzyme discussion, p3 Figure1 and following
    text, pp4–6 sugar regulation; initial browser read completed by07:36:38Z, focused
    follow-up by07:38:39Z
  accessed_at: '2026-10-21T07:38:39Z'
  support: supports
  summary: All five snippets match the inspected browser PDF. The contextual cellulose
    system and oxidative enzyme claims are supported. Glucose repression is discussed
    for fungal cellulolytic expression with taxon/substrate qualifications; the broad
    target label is not by itself an assertion that all ligninolytic branches are
    repressed.
- evidence_id: cragg
  kind: primary_source
  reference: https://pure.port.ac.uk/ws/files/3141775/Lignocellulose_degradation_mechanisms_across_the_Tree_of_Life.pdf
  locator: DOI10.1016/j.cbpa.2015.10.018; PDFp2/printed109 Enzymatic depolymerisation
    of cellulose and hemicelluloses, first paragraph
  accessed_at: '2026-10-21T07:39:00Z'
  support: supports
  summary: The exact snippet and adjacent text support collective CAZyme action, including
    glycosidic-bond cleavage. The record’s note selects hemicellulose-active enzymes;
    it does not require every CAZyme to share that activity.
  snapshot_sha256: 8d0b638bccdb155a2c9dbdd6c4f465672ae2a23269976b57d837d31af1d542a9
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: fallback, label, synonyms and hierarchy'
  outcome: supported
  target_ids:
  - traitmech:000055
  summary: Fallback000055 and the proposal identify one trophic lifestyle. Related
    synonyms are not asserted as exact lexical equivalences; phenotype is a broader
    parent.
  evidence_ids:
  - record
  - identity
  - parent
- assessment_id: category
  area: representation
  topic: 'Native checklist: ECOLOGY/CLASS and NONMECHANISTIC context'
  outcome: supported
  target_ids:
  - traitmech:000055
  summary: The ecological class and heterogeneous contextual graph are appropriate.
    Optional datasets, strain-specific proteins and a complete connected molecular
    route are not required.
  evidence_ids:
  - record
  - protein-policy
- assessment_id: grounding
  area: grounding
  topic: 'Native checklist: all grounded chemicals and enzymes'
  outcome: concern
  target_ids:
  - traitmech:000055
  summary: Chemical grounds and the enzyme-activity GO term resolve consistently with
    native policy. The laccase family is narrower than the microbial context asserted
    by the record.
  evidence_ids:
  - identifiers
  - protein-policy
  - interpro
  - interpro-scope
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all nine edge roles and directions'
  outcome: concern
  target_ids:
  - traitmech:000055
  summary: Edges0/2/8 have external relation meaning conflicts; their local permissive
    validation does not validate those meanings. Edge1 consumes and edge4 derives
    into retain valid directions. Proposed hydrolysis/oxidation predicates retain
    their distinct meanings.
  evidence_ids:
  - record
  - relations
  - shape
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: optional computational expression context'
  outcome: supported
  target_ids:
  - traitmech:000055
  summary: The official matching-name dataset was inspected with explicit strain and
    inference limits. Gene/module membership is not promoted to proof of this trait.
  evidence_ids:
  - expression
  - runner
- assessment_id: provenance
  area: provenance
  topic: 'Native checklist: human acceptance and maintained owners'
  outcome: concern
  target_ids:
  - traitmech:000055
  summary: The record and matching repository history preserve AI-assisted provenance,
    including earlier evidence repairs, but the inspected target-specific fields do
    not link human scientific acceptance.
  evidence_ids:
  - provenance
  - status-rule
  - owners
  - local-search
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: dead-substrate lifestyle and source scope'
  outcome: supported
  target_ids:
  - traitmech:000055
  summary: Detrital resource use and decomposition/carbon cycling are supported. Schimel
    provides soil ecological discussion rather than a formal lexical definition; the
    model-organism source independently supports saprophytic decomposition.
  evidence_ids:
  - record
  - schimel
  - example
- assessment_id: example
  area: evidence
  topic: 'Native checklist: canonical species, strain and hydrolase evidence tier'
  outcome: concern
  target_ids:
  - traitmech:000055
  summary: Species1902 and strain100226 resolve consistently with the paper’s A3(2)
    context. The ecological example is supported; the hydrolase passage is a genomic
    prediction, which should remain explicit when expanding or reusing the example.
  evidence_ids:
  - identifiers
  - ledger
  - example
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: all record and edge claims'
  outcome: supported
  target_ids:
  - traitmech:000055
  summary: All eleven snippets are verbatim after ordinary PDF text normalization.
    All nine edges have source-supported contextual biological claims; relation and
    family-grounding errors are assessed separately. The collective enzyme nodes do
    not assert identical activities for every member.
  evidence_ids:
  - bibliography
  - schimel
  - fierer
  - wang
  - gurovic
  - cragg
- assessment_id: scope
  area: consistency
  topic: 'Native checklist: contextual enzyme and regulatory qualifications'
  outcome: supported
  target_ids:
  - traitmech:000055
  summary: NONMECHANISTIC scope permits a heterogeneous sketch. The fungal cellulase/hemicellulase
    repression context should be preserved, but no class-wide universal CCR claim
    is inferred solely from the broad lignocellulolytic label. The lignin oxidative
    edge does not imply that GO activity identity alone proves every reaction detail.
  evidence_ids:
  - record
  - gurovic
  - cragg
  - protein-policy
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: optional content and structural integrity'
  outcome: supported
  target_ids:
  - traitmech:000055
  summary: The ecological definition, example and source-backed context are present.
    All graph endpoints resolve. There are no asserted pathway-context links requiring
    target-specific checks, and optional protein examples, discussions or datasets
    are not prerequisites for this NONMECHANISTIC class.
  evidence_ids:
  - record
  - shape
  - protein-policy
findings:
- finding_id: relation-semantics
  issue_key: saprotrophy-relation-semantics
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Three edge groundings conflict with their endpoint meanings
  description: Edge0 places the saprotrophy trait itself in RO enables’ material-executor
    role. Edge2 sends RO contributes to to soluble chemical products, rather than
    an enabled activity/function. Edge8 places glucose in RO negative regulation’s
    process-to-process subject role. These are external semantic conflicts, not failures
    of the passing local schema. The process-consuming-substrate edge1 and substrate-to-product
    edge4 are not part of this finding.
  target_ids:
  - traitmech:000055
  field_paths:
  - causal_graphs[0].edges[0]
  - causal_graphs[0].edges[2]
  - causal_graphs[0].edges[8]
  evidence_ids:
  - record
  - relations
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/saprotrophy.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/review_saprotrophy_graph_183.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: laccase-family-scope
  issue_key: saprotrophy-laccase-family-scope
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Plant laccase family used for a microbial laccase node
  description: Node10 is grounded to IPR017761 while edge6 notes identify a fungal
    and bacterial ligninolytic context. The current entry/model descriptions and taxonomic
    coverage establish a plant protein family. Reusing its matching label does not
    ground the intended broader microbial enzyme identity. This finding concerns this
    family assignment; it does not imply laccase activity is confined to plants.
  target_ids:
  - traitmech:000055
  field_paths:
  - causal_graphs[0].nodes[10].grounding
  - causal_graphs[0].edges[6].evidence[0].notes
  evidence_ids:
  - record
  - interpro
  - interpro-scope
  - protein-policy
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/saprotrophy.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: saprotrophy-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human scientific acceptance is not linked in inspected local provenance
  description: The fourteen target events and matching repository history disclose
    AI work. None of the inspected target-specific fields identifies the human acceptance
    required for REVIEWED. This is a bounded documentation finding, not proof that
    no human review occurred elsewhere.
  target_ids:
  - traitmech:000055
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - status-rule
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/saprotrophy.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: history/records/saprotrophy/2026-09-04T070000Z-codex-1d076e.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: repair-relations
  description: In a separately authorized curation, preserve each source-supported
    biological claim while reconciling the three relations and node roles with authoritative
    meanings. Reconcile maintained writer/replay expectations and shared mapping scope.
  finding_ids:
  - relation-semantics
  target_ids:
  - traitmech:000055
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/saprotrophy.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/review_saprotrophy_graph_183.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Verify the chosen relation definitions and endpoint roles independently.
  - Run focused validate and validate-strict, relevant predicate/graph audits and
    writer tests, then just qc.
  - Append native record and repository curation history; regenerate affected derived
    artifacts through maintained recipes.
- action_id: repair-laccase-ground
  description: Resolve an exact taxon-appropriate family/function grounding for the
    stated microbial context, or retain an explicit justified label-only decision
    when no exact match is verified. Reconcile the shared node mapping.
  finding_ids:
  - laccase-family-scope
  target_ids:
  - traitmech:000055
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/saprotrophy.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Verify the replacement identifier’s definition and scope, rather than label alone.
  - Do not substitute a broad multicopper-oxidase family or a token species-specific
    accession as an unverified exact match.
  - Run focused strict validation, applicable grounding/protein audits and just qc;
    record curation history.
- action_id: link-acceptance
  description: Locate and link existing human scientific acceptance or obtain it through
    the established curation process; preserve AI history and reassess status if acceptance
    remains unavailable.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - traitmech:000055
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/saprotrophy.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - A human acceptance reference identifies this record/revision and scientific scope.
  - Automated review validation is not used as human sign-off.
limitations:
- The Gurovic full text was inspected through a public browser PDF; local download
  attempts failed, and no downloaded-byte hash is asserted for that source.
- Relevant passages were inspected for all six sources, not every section or all underlying
  primary experiments. Review articles support contextual claims without independently
  replicating them.
- The example’s hydrolase passage is genomic prediction, not a direct secretion assay.
  Its model-organism ecology is supported.
- The glucose regulatory context concerns fungal cellulolytic/hemicellulolytic expression;
  species, substrate and condition qualifications should be preserved. No universal
  repression defect is inferred solely from the broad node label.
- The official expression dataset uses multiple strain labels; sampled gene/module
  annotations do not establish ecological phenotype, secretion, substrate specificity
  or fungal mechanism.
- Optional structured-source runner unavailable; official API fallback inspected.
  Bounded query or membership nonmatches are not negative biological evidence.
- The initial incorrect snippet recipe invocation failed without scientific output
  and is retained; the corrected documented recipe and manual full-text checks completed.
- External ontology semantics are distinct from permissive local validation. No formal
  reasoner error is claimed. Pending METPO proposal IDs are not presented as minted
  upstream identities.
- Private or remote human acceptance was not searched. The provenance finding concerns
  documentation in the inspected local target-specific fields.
- Only this new review bundle is authorized scientific output here; no record, writer,
  mapping, status, history or generated page was curated.
notes:
- All field paths use zero-based indices.
- 'Severity retains the native rubric: material relation/family errors are major;
  bounded acceptance documentation is minor.'
- The independent ontology ledger and source ledger agree on the distinct positive
  checks; no missing-mechanism finding is derived from optional content.
tags:
- record-review
- saprotrophy
- ecology
- needs-curation
```
