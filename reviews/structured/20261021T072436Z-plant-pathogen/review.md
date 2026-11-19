# Documentary and ontology review of plant pathogen (METPO:1004003)

- Review: 20261021T072436Z-plant-pathogen
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T07:18:32Z
- Finished UTC: 2026-10-21T07:24:36Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The active METPO identity, broader parent, three current GO identities and generic species example are supported. Two major findings concern a currently unresolved citation used in three placements and ontology/linguistic inconsistencies in four edges. Three minor findings concern a provisional relation’s subject meaning, a historical bacterial-only scope gloss and locally undocumented human acceptance. All thirteen nodes and twelve edges were inspected for documentary and conceptual consistency; detailed plant-pathogenicity mechanisms remain unverified.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Fourth batch003 target, following the saved pathogenic-to-host review in lexicographic path order; one entire previously uncovered TraitRecord.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1004003 | data/traits/ecology/plant_pathogen.yaml | maintained | plant pathogen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1004003 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1004003 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1004003 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1004003 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1004003 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1004003 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1004003 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1004003 | The selected record validates. |
| Focused strict validation | passed | True | METPO:1004003 | One file scanned; zero strict errors. |
| Focused source snippet verification | passed | True | METPO:1004003 | Eight occurrences over two references: five NOT_IN_ABSTRACT and three UNRESOLVED. Completion with exit0 does not establish any full-text quotation. |
| Expression-module applicability | not_applicable | False | METPO:1004003 | Generic aggregates and the species-level example assert no strain/locus expression result. Expression modules are not used to establish the plant-host class or validate detailed mechanisms. |

## Scientific And Domain Assessments

### Native checklist: identifier, host boundary, synonyms and kind

identity: supported. Targets: METPO:1004003.

The active ontology class exactly matches the host-defined concept. Removing an upstream synonym identical to the label did not lose an alternative term.

### Native checklist: ontology wording and definition-source limits

evidence: concern. Targets: METPO:1004003.

The ontology supplies the exact host boundary. Glazebrook is a suitable broad plant-pathology context, but the inspected abstract does not independently establish that exact boundary or each attached detailed claim. No publication-category mismatch is asserted.

### Native checklist: broader parent

consistency: supported. Targets: METPO:1004003.

Pathogenic to host is strictly broader; neither the definition nor parent restricts the pathogen taxon to bacteria.

### Native checklist: ecological class and NONMECHANISTIC scope

representation: supported. Targets: METPO:1004003.

ECOLOGY/CLASS and the broad graph scope are coherent. Four reviewed generic aggregates need no token accessions.

### Native checklist: canonical species and secondary aside

evidence: concern. Targets: METPO:1004003.

Taxonomy and generic P. syringae model-pathogen wording are supported. The parenthetical mechanism and secondary Agrobacterium assertion are unverified from the inspected source; failure to retrieve XML is not evidence of absence.

### Native checklist: six references and eight snippets

evidence: concern. Targets: METPO:1004003.

Five identities resolve; the exact wall DOI remains unresolved after several ordinary registry/publisher attempts. None of the eight full-text quotations is verified by the abstract-only check. Metadata-only and abstract-only limits are retained, with no title-based mechanism contradiction.

### Native checklist: all thirteen nodes and twelve edges

graph: concern. Targets: METPO:1004003.

Four edges conflict with external endpoint meanings, with two also showing internal negation inconsistency. One provisional relation extends beyond its stated subject meaning. Detailed biological mechanisms remain unverified.

Zero-based ledger: node0 is the trait; nodes1–3/12 are reviewed generic material aggregates; nodes4–9/11 are process concepts; node10 is a matching GO cellular component. Node5 has no current external grounding following the documented retraction. Edge0 has compatible actor/process types, but its reference is unresolved. Edge1 uses an allowed local ungrounded phrase; exact source support is unverified. Edges2/11 have material subjects under process-to-process negative regulation; their suppression predicate applied to an already negative object also conflicts literally with the accompanying description. Edges3/8 use process subjects under enables. Edge4 has compatible broad Biolink endpoints but an unresolved citation. Edge5 uses the proposed microorganism-state manifestation relation for a host outcome. Edges6/7 have compatible process endpoints without biological certification. Edge9 fits the provisional relation’s admitted structure object but has only bibliographic source confirmation. Edge10 uses an allowed ungrounded local phrase and retains fungal/oomycete context. No alternative pathway, molecular target or experimental step is proposed.

### Native checklist: discussion and dataset slots

completeness: supported. Targets: METPO:1004003.

No discussion placeholder or dataset assertion requires resolution. Optional data are not invented for this classifier.

### Native checklist: retraction explanation and REVIEWED basis

provenance: concern. Targets: METPO:1004003.

The local unsupported grounding was withdrawn, which is distinct from ontology obsoletion. The historical bacterial-only gloss is narrower than current class/context. The inspected local provenance does not identify human acceptance.

## Findings

### reference-unresolved: An exact citation used in three placements remains unresolved

major / open / provisional; issue key: plant-pathogen-reference-unresolved.

DOI:10.1146/annurev.micro.55.1.535 did not resolve through the recorded Europe PMC, Crossref, DOI Handle and publisher attempts. It supports one record-level evidence item and two edges, preventing source inspection for those placements. This is a bounded resolution concern; nonexistence of the article and falsity of the biological assertions are not established.

### external-types-and-negation: Four relation uses conflict with their endpoint meanings

major / open / confirmed; issue key: plant-pathogen-external-types-and-negation.

Edges2/11 use material-protein subjects with RO process-to-process negative regulation; edges3/8 use biological processes as enables executors. Edges2/11 also literally negate an already negative object, whereas the accompanying descriptions state the opposite grammatical relationship. This is internal/ontology consistency analysis, not a corrected or validated biological route.

### provisional-manifestation-scope: A local manifestation relation is extended to a host outcome

minor / open / confirmed; issue key: plant-pathogen-provisional-manifestation-scope.

The local v2 proposal describes a physiological or molecular state of a microorganism manifesting its phenotype. The current edge5 subject is pathology in the plant host. The generic local endpoint mapping does not establish this semantic extension; this is not a formal validator failure.

### historical-bacterial-scope-gloss: Historical rationale calls a broader class a bacterial record

minor / open / confirmed; issue key: plant-pathogen-historical-bacterial-scope-gloss.

The grounding-retraction event calls this a bacterial record, whereas the definition is host-based and existing node11/evidence describe fungal/oomycete context. The narrower shorthand should not be interpreted as a class boundary. This does not establish that the retracted GO term was an exact match, and no reinstatement is proposed.

### reviewed-signoff-not-documented: Inspected REVIEWED provenance lacks a human-acceptance link

minor / open / confirmed; issue key: plant-pathogen-reviewed-signoff-not-documented.

Sixteen AI-assisted events and one scripted import do not identify human scientific acceptance in the inspected target-specific material. Private or remote approval is not ruled out.

## Recommended Actions And Acceptance Checks

### resolve-source-identity

Resolve the exact bibliographic identity for the three affected evidence placements in separately authorized curation.

- Recover an authoritative source identity and durable locator, preserving current failed-access provenance.
- Do not guess a replacement paper from topical similarity or infer biological falsity from lookup failure.
- This action concerns citation traceability; it proposes no new pathogen mechanism or experimental route.

### reconcile-graph-language

Reconcile existing entity meanings, selected relation definitions and literal edge wording.

- Check the actual external identifier and distinguish process, material actor, microorganism state and host outcome.
- Do not invent molecular intermediates or infer a corrected biological route from grammatical inconsistency.
- Any authorized future edit requires guarded writes, appended history and applicable strict/graph/qc checks.

### clarify-history

Append a bounded clarification of historical class-scope wording during separately authorized curation.

- Keep the host-defined class distinct from the context of an individual graph branch.
- Preserve prior history and do not reinstate the unsupported exact GO mapping.

### document-status

Locate and document human scientific acceptance or retain the status-basis question.

- AI history, import scripts and deterministic checks do not identify a human approver.
- Any status change requires separate curation authorization.

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
| check-plant_pathogen-validate | /private/tmp/traitmech-record-sweep-003.4opxlhgf/plant_pathogen-validate.log; Executed 2026-10-21T07:19:03Z through 2026-10-21T07:19:07Z; metadata plant_pathogen-validate.json | context_only | The selected record validates. |
| check-plant_pathogen-strict | /private/tmp/traitmech-record-sweep-003.4opxlhgf/plant_pathogen-strict.log; Executed 2026-10-21T07:19:03Z through 2026-10-21T07:19:09Z; metadata plant_pathogen-strict.json | context_only | One file scanned; zero strict errors. |
| check-plant_pathogen-snippets | /private/tmp/traitmech-record-sweep-003.4opxlhgf/plant_pathogen-snippets.log; Executed 2026-10-21T07:19:06Z through 2026-10-21T07:19:17Z; metadata plant_pathogen-snippets.json | context_only | Eight occurrences over two references: five NOT_IN_ABSTRACT and three UNRESOLVED. Completion with exit0 does not establish any full-text quotation. |
| record | data/traits/ecology/plant_pathogen.yaml; Entire target, thirteen nodes, twelve edges and seventeen history events | partial | The host-defined class is clear; graph endpoint meaning and source traceability have bounded concerns. |
| identity | data/raw/metpo.owl; Complete captured RDF exact labels and target/parent/provisional entity inspection | supports | METPO:1004003 is active with the stated Viridiplantae-host definition and active parent METPO:1004000. The duplicate upstream label-synonym was removed locally without losing an alternative name. METPO:2007400 and METPO:2007809 are absent from the captured release and documented in local proposals. |
| parent | data/traits/ecology/pathogenic_to_host.yaml; Definition and active identifier | supports | Pathogenicity to a host is broader than the plant-host subclass; the current class is not restricted to bacterial pathogens. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0009372%2CGO%3A0042710%2CGO%3A0009505%2CGO%3A0140649; Live exact term labels, aspects and status; current versus historical locators distinguished | supports | The three current node identifiers match their concepts and types. GO:0140649 is only a historical, locally retracted assignment; it is not a current grounding and must not be counted as a remaining current-ID error. |
| taxon | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=317; Exact live species identity | supports | NCBITaxon:317 resolves to Pseudomonas syringae. This verifies identity rather than a molecular phenotype. |
| secondary-name | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy&amp;term=Agrobacterium%20tumefaciens%5BAll%20Names%5D&amp;retmode=json; Live name lookup and returned taxonomy entity | context_only | The secondary name can be resolved taxonomically; that does not establish the separate disease/genetic-tool characterization from the record’s cited paper. |
| relations | Cached authoritative RO database; captured Biolink model; v2/v9 local proposals; Recursive predicate definitions and inherited endpoint meanings; exact proposal rows | partial | RO regulation is process-to-process; enables has independent-continuant/executor subject semantics. Four edges conflict with these meanings. The provisional degrades relation admits a cellular structure, while the provisional manifestation relation describes a microorganism state. |
| ledger | Documentary node/edge ledger; All thirteen nodes and twelve edges, zero-based indices | partial | Every endpoint and stated type was examined; literal predicate/object negation in two edges does not agree with their accompanying descriptions. No corrected biological route is supplied. |
| shape | Read-only graph shape check; Thirteen unique node IDs, twelve edges, seventeen events including sixteen AI-assisted | supports | All endpoints resolve. Passing structural validation does not establish biological evidence or relation semantics. |
| history-owner | scripts/migrate_name_match_groundings.py; history/mappings/name-match-groundings/2026-08-17T042357Z-claude-code-2a9f93.yaml; Maintained local retraction, companion history and target curation_history[15] | partial | The current node is ungrounded following a recorded retraction. The explanation’s bacterial-record shorthand is narrower than the host-defined class and existing fungal/oomycete context. Retraction of an unsupported exact term should not be reversed on that basis. |
| bibliography | https://www.ebi.ac.uk/europepmc/webservices/rest/search; https://api.crossref.org/works/; Six unique references, exact source/access ledger | partial | Five citation identities resolve; the wall DOI remains unresolved. Eight snippets comprise five distinct phrases. Source qualification separately corrects an overstrong preliminary review-category inference. |
| qualification | Source assessment qualification; Correction to preliminary Glazebrook characterization, preserving original evidence receipts | supports | The target says plant-pathology review, which fits Glazebrook. It does not call the paper a dedicated secretion review. Title/abstract focus and unmatched abstract snippets do not establish a citation-category mismatch or false full-text quotation. |
| definition-source | https://doi.org/10.1146/annurev.phyto.43.040204.135923; PMID16078883 title and abstract conceptual framing | partial | Glazebrook reviews plant defense against biotrophic and necrotrophic pathogens. Broad context is appropriate; the exact kingdom boundary and attached detailed assertions are not independently established by the inspected abstract. No claim of absent full-text support follows. |
| unresolved-reference | DOI:10.1146/annurev.micro.55.1.535; Exact Europe PMC, Crossref, DOI Handle and publisher attempts | partial | Europe PMC returned no result at07:19:19; Crossref404 at07:19:46; Handle404 and publisher403 at07:20:22; browser access was unavailable. The exact reference remains unresolved in this bounded review. No replacement is guessed and no biological assertion is declared false. |
| example | https://pubmed.ncbi.nlm.nih.gov/29479077/; Title and abstract first sentence | supports | Directly supports P. syringae as a well-studied model plant pathogen. The mechanistic parenthetical and separate Agrobacterium aside remain unverified; a public XML attempt failed500. |
| plants | https://doi.org/10.3390/plants12112207; PMID37299186 title and abstract review framing | partial | The review concerns biofilm-forming phytopathogenic bacteria. Identity/context are verified; detailed necessity, directionality and mechanisms are not. |
| mb | https://doi.org/10.21608/mb.2024.307263.1134; Crossref title, journal and publisher metadata | partial | Resolves to Plant Diseases: Pathogenicity and integrated management overview in Microbial Biosystems. A Europe PMC miss is an indexing limit. No abstract or article text was inspected, so its detailed note remains unverified. |
| mpmi | https://doi.org/10.1094/MPMI-12-23-0212-CR; PMID38949402 title and abstract review framing | partial | The review concerns fungal and oomycete pathogens. Its unconventional-secretion title alone does not contradict a contextual statement about a conventional pathway. Detailed assertions remain unverified. |
| search | Local identity, ownership and provenance search; Ignored-inclusive identifier, label/slug and graph searches | partial | Seventeen events comprise sixteen AI-assisted and one seed import event. No explicit human-acceptance link was identified in inspected target-specific local material; private/remote approval remains unknown. |
| policy | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/GROUNDING_POLICY.md; Source scope, graph meaning, optional examples and human sign-off rules | supports | NONMECHANISTIC scope does not require token protein examples or a universal graph. Source-access limits must remain explicit and REVIEWED requires human scientific acceptance. |

## Limits And Additional Notes

- All fields were inspected for documentary/conceptual consistency. Detailed virulence, plant-immune-suppression and host-exploitation mechanisms were not independently certified, reconstructed, corrected or improved.
- Five citation identities resolve and one exact DOI remains unresolved. Failed registry/access results do not establish nonexistent literature or false biology.
- Eight snippets are inconclusive: five not in inspected abstracts, three attached to the unresolved DOI. Complete full-text exactness remains unverified.
- The secondary Agrobacterium attribution and mechanistic parenthetical remain unverified. The model P. syringae species claim is directly supported.
- Glazebrook is not called a wrong publication category; the MPMI title is not used to infer a contradiction. Metadata-only confirmation of the Microbial Biosystems item does not verify its evidence note.
- GO:0140649 is locally retracted, not a current node grounding. The existing ungrounded node is not filled by guessing a near match.
- Local predicate proposals, bounded human-acceptance search, and historical corpus-check failures/skips remain explicit.
- No scientific record, mapping, writer, history, native status or generated product is changed.
- Native input capture preceded judgment. Source-agent overstatement about the definition citation was explicitly corrected before authoring this review; original access receipts were preserved.
- The unresolved-reference finding is provisional, while the recorded resolution failures and existing graph wording are direct observations.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T072436Z-plant-pathogen
kind: record
repository: CultureBotAI/TraitMech
title: Documentary and ontology review of plant pathogen (METPO:1004003)
started_at: '2026-10-21T07:18:32Z'
finished_at: '2026-10-21T07:24:36Z'
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
summary: The active METPO identity, broader parent, three current GO identities and
  generic species example are supported. Two major findings concern a currently unresolved
  citation used in three placements and ontology/linguistic inconsistencies in four
  edges. Three minor findings concern a provisional relation’s subject meaning, a
  historical bacterial-only scope gloss and locally undocumented human acceptance.
  All thirteen nodes and twelve edges were inspected for documentary and conceptual
  consistency; detailed plant-pathogenicity mechanisms remain unverified.
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
  - path: data/traits/ecology/pathogenic_to_host.yaml
    sha256: 6086ef781d3871684a8a21c77330be972673657b83b5fa0d4ba9c52e376ca451
    role: context
  - path: data/traits/ecology/plant_pathogen.yaml
    sha256: 4c8c4cf20790c060a91495e96a13656c7d7b72ef0856b0fbc2598ff53a99eb00
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
  - path: history/mappings/name-match-groundings/2026-08-17T042357Z-claude-code-2a9f93.yaml
    sha256: c3f93d5c8c0da5c538af391bfdbad3a8bcbe238a26a8727764c3f0ddc3422ad8
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
  - path: research/traits/ecology/plant_pathogen-deep-research-falcon.md
    sha256: 123cf4c58bc637a174c6cf1627f0d7f2deb823f71b5e938495c3dfad101c5f20
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
  - path: scripts/migrate_name_match_groundings.py
    sha256: 9b3ea1153839b9b260638cef95eba2d1ccc6d7b3825e7352c33cceb21bfe4dd4
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
- target_id: METPO:1004003
  path: data/traits/ecology/plant_pathogen.yaml
  label: plant pathogen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/plant_pathogen.yaml
    role: Maintained scientific record
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_name_match_groundings.py
    role: Maintained historical grounding correction
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Fourth batch003 target, following the saved pathogenic-to-host review
    in lexicographic path order; one entire previously uncovered TraitRecord.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1004003
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1004003
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
  - METPO:1004003
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
  - METPO:1004003
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
  - METPO:1004003
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
  - METPO:1004003
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
  - METPO:1004003
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
  - METPO:1004003
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
- check_id: plant_pathogen-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1004003
  command: just validate data/traits/ecology/plant_pathogen.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The selected record validates.
  evidence_ids:
  - check-plant_pathogen-validate
- check_id: plant_pathogen-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1004003
  command: just validate-strict data/traits/ecology/plant_pathogen.yaml --out /private/tmp/traitmech-record-sweep-003.4opxlhgf/plant_pathogen-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero strict errors.
  evidence_ids:
  - check-plant_pathogen-strict
- check_id: plant_pathogen-snippets
  name: Focused source snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1004003
  command: just verify-snippets --record data/traits/ecology/plant_pathogen.yaml --out
    /private/tmp/traitmech-record-sweep-003.4opxlhgf/plant_pathogen-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Eight occurrences over two references: five NOT_IN_ABSTRACT and three
    UNRESOLVED. Completion with exit0 does not establish any full-text quotation.'
  evidence_ids:
  - check-plant_pathogen-snippets
- check_id: expression-applicability
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1004003
  summary: Generic aggregates and the species-level example assert no strain/locus
    expression result. Expression modules are not used to establish the plant-host
    class or validate detailed mechanisms.
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T07:24:18Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T07:24:18Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T07:24:18Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T07:24:18Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T07:24:18Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T07:24:18Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T07:24:18Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-plant_pathogen-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/plant_pathogen-validate.log
  locator: Executed 2026-10-21T07:19:03Z through 2026-10-21T07:19:07Z; metadata plant_pathogen-validate.json
  accessed_at: '2026-10-21T07:24:18Z'
  support: context_only
  summary: The selected record validates.
  snapshot_sha256: 542b3021328c0eb0acd4cc214d3f78f51164d893b03d21260627e84c0d06844f
- evidence_id: check-plant_pathogen-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/plant_pathogen-strict.log
  locator: Executed 2026-10-21T07:19:03Z through 2026-10-21T07:19:09Z; metadata plant_pathogen-strict.json
  accessed_at: '2026-10-21T07:24:18Z'
  support: context_only
  summary: One file scanned; zero strict errors.
  snapshot_sha256: 06f99b4a77157e967ad050226db9d68b267918c7e8cd0d430069cbf17008e379
- evidence_id: check-plant_pathogen-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/plant_pathogen-snippets.log
  locator: Executed 2026-10-21T07:19:06Z through 2026-10-21T07:19:17Z; metadata plant_pathogen-snippets.json
  accessed_at: '2026-10-21T07:24:18Z'
  support: context_only
  summary: 'Eight occurrences over two references: five NOT_IN_ABSTRACT and three
    UNRESOLVED. Completion with exit0 does not establish any full-text quotation.'
  snapshot_sha256: 942bbb14b7748eb4db26443b15d454269b8c2314d973d760af5221196e016259
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/plant_pathogen.yaml
  locator: Entire target, thirteen nodes, twelve edges and seventeen history events
  accessed_at: '2026-10-21T07:24:18Z'
  support: partial
  summary: The host-defined class is clear; graph endpoint meaning and source traceability
    have bounded concerns.
  snapshot_sha256: 4c8c4cf20790c060a91495e96a13656c7d7b72ef0856b0fbc2598ff53a99eb00
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl
  locator: Complete captured RDF exact labels and target/parent/provisional entity
    inspection
  accessed_at: '2026-10-21T07:21:15Z'
  support: supports
  summary: METPO:1004003 is active with the stated Viridiplantae-host definition and
    active parent METPO:1004000. The duplicate upstream label-synonym was removed
    locally without losing an alternative name. METPO:2007400 and METPO:2007809 are
    absent from the captured release and documented in local proposals.
  snapshot_sha256: 8da9c4b729483fbb9ccb830274b9ab4b041af7ca4d9ee328547a01c514c335b6
- evidence_id: parent
  kind: record_content
  reference: data/traits/ecology/pathogenic_to_host.yaml
  locator: Definition and active identifier
  accessed_at: '2026-10-21T07:24:18Z'
  support: supports
  summary: Pathogenicity to a host is broader than the plant-host subclass; the current
    class is not restricted to bacterial pathogens.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0009372%2CGO%3A0042710%2CGO%3A0009505%2CGO%3A0140649
  locator: Live exact term labels, aspects and status; current versus historical locators
    distinguished
  accessed_at: '2026-10-21T07:21:30Z'
  support: supports
  summary: The three current node identifiers match their concepts and types. GO:0140649
    is only a historical, locally retracted assignment; it is not a current grounding
    and must not be counted as a remaining current-ID error.
  snapshot_sha256: 30726be6448613e3644a5cacf4be374395fef224fbc0058bc0c844be9c3311e9
- evidence_id: taxon
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=317
  locator: Exact live species identity
  accessed_at: '2026-10-21T07:21:31Z'
  support: supports
  summary: NCBITaxon:317 resolves to Pseudomonas syringae. This verifies identity
    rather than a molecular phenotype.
  snapshot_sha256: 019b68972363518e79fa93f8c77be082dcd48c20c206d6df014fe6c74eff0562
- evidence_id: secondary-name
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy&term=Agrobacterium%20tumefaciens%5BAll%20Names%5D&retmode=json
  locator: Live name lookup and returned taxonomy entity
  accessed_at: '2026-10-21T07:21:31Z'
  support: context_only
  summary: The secondary name can be resolved taxonomically; that does not establish
    the separate disease/genetic-tool characterization from the record’s cited paper.
  snapshot_sha256: a9fff5ee6d5ca9caceafdf2dc1a9c3c1b4cd079c65a67a337a5873be9a6b649e
- evidence_id: relations
  kind: authority
  reference: Cached authoritative RO database; captured Biolink model; v2/v9 local
    proposals
  locator: Recursive predicate definitions and inherited endpoint meanings; exact
    proposal rows
  accessed_at: '2026-10-21T07:21:16.116169Z'
  support: partial
  summary: RO regulation is process-to-process; enables has independent-continuant/executor
    subject semantics. Four edges conflict with these meanings. The provisional degrades
    relation admits a cellular structure, while the provisional manifestation relation
    describes a microorganism state.
  snapshot_sha256: a9328fbfff5663325651fadf4732adab956221646342a7830c5957c4d608af4f
- evidence_id: ledger
  kind: validation
  reference: Documentary node/edge ledger
  locator: All thirteen nodes and twelve edges, zero-based indices
  accessed_at: '2026-10-21T07:22:58.046094Z'
  support: partial
  summary: Every endpoint and stated type was examined; literal predicate/object negation
    in two edges does not agree with their accompanying descriptions. No corrected
    biological route is supplied.
  snapshot_sha256: 67784536f0c57d5410eeb974ca20e976287fa3ff1556302a42f95b3774d7a690
- evidence_id: shape
  kind: validation
  reference: Read-only graph shape check
  locator: Thirteen unique node IDs, twelve edges, seventeen events including sixteen
    AI-assisted
  accessed_at: '2026-10-21T07:19:28Z'
  support: supports
  summary: All endpoints resolve. Passing structural validation does not establish
    biological evidence or relation semantics.
  snapshot_sha256: ab2090d6c55e7c05cfc82f4b568fe1fb8719b110fa377a1781913398b5c2985e
- evidence_id: history-owner
  kind: record_content
  reference: scripts/migrate_name_match_groundings.py; history/mappings/name-match-groundings/2026-08-17T042357Z-claude-code-2a9f93.yaml
  locator: Maintained local retraction, companion history and target curation_history[15]
  accessed_at: '2026-10-21T07:22:58.047755Z'
  support: partial
  summary: The current node is ungrounded following a recorded retraction. The explanation’s
    bacterial-record shorthand is narrower than the host-defined class and existing
    fungal/oomycete context. Retraction of an unsupported exact term should not be
    reversed on that basis.
  snapshot_sha256: 35841534398d44716084e1921c9166f50a124fcfdeab7dca9fc88ab7b56fea80
- evidence_id: bibliography
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search; https://api.crossref.org/works/
  locator: Six unique references, exact source/access ledger
  accessed_at: '2026-10-21T07:20:59Z'
  support: partial
  summary: Five citation identities resolve; the wall DOI remains unresolved. Eight
    snippets comprise five distinct phrases. Source qualification separately corrects
    an overstrong preliminary review-category inference.
  snapshot_sha256: 30701246a1f87f49c03debc1825e8076eaa723a104d9f23077b248aa40c9bcf3
- evidence_id: qualification
  kind: record_content
  reference: Source assessment qualification
  locator: Correction to preliminary Glazebrook characterization, preserving original
    evidence receipts
  accessed_at: '2026-10-21T07:22:14Z'
  support: supports
  summary: The target says plant-pathology review, which fits Glazebrook. It does
    not call the paper a dedicated secretion review. Title/abstract focus and unmatched
    abstract snippets do not establish a citation-category mismatch or false full-text
    quotation.
  snapshot_sha256: 04a3fdf29c8a61ab5a13eeaa6d8ee3e153817c219afe54fc2397fccb8e7de667
- evidence_id: definition-source
  kind: primary_source
  reference: https://doi.org/10.1146/annurev.phyto.43.040204.135923
  locator: PMID16078883 title and abstract conceptual framing
  accessed_at: '2026-10-21T07:19:19Z'
  support: partial
  summary: Glazebrook reviews plant defense against biotrophic and necrotrophic pathogens.
    Broad context is appropriate; the exact kingdom boundary and attached detailed
    assertions are not independently established by the inspected abstract. No claim
    of absent full-text support follows.
  snapshot_sha256: 6996a4609b1b0c02c4c2404e9544a4578a837a1edad26db9cd3c2ce50427c5c0
- evidence_id: unresolved-reference
  kind: database
  reference: DOI:10.1146/annurev.micro.55.1.535
  locator: Exact Europe PMC, Crossref, DOI Handle and publisher attempts
  accessed_at: '2026-10-21T07:20:22Z'
  support: partial
  summary: Europe PMC returned no result at07:19:19; Crossref404 at07:19:46; Handle404
    and publisher403 at07:20:22; browser access was unavailable. The exact reference
    remains unresolved in this bounded review. No replacement is guessed and no biological
    assertion is declared false.
  snapshot_sha256: 30701246a1f87f49c03debc1825e8076eaa723a104d9f23077b248aa40c9bcf3
- evidence_id: example
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/29479077/
  locator: Title and abstract first sentence
  accessed_at: '2026-10-21T07:19:19Z'
  support: supports
  summary: Directly supports P. syringae as a well-studied model plant pathogen. The
    mechanistic parenthetical and separate Agrobacterium aside remain unverified;
    a public XML attempt failed500.
  snapshot_sha256: 4885239b458f9d4d741653f1203fe83e7cbc9f95bce0f31c9e74e310b891862e
- evidence_id: plants
  kind: primary_source
  reference: https://doi.org/10.3390/plants12112207
  locator: PMID37299186 title and abstract review framing
  accessed_at: '2026-10-21T07:19:19Z'
  support: partial
  summary: The review concerns biofilm-forming phytopathogenic bacteria. Identity/context
    are verified; detailed necessity, directionality and mechanisms are not.
  snapshot_sha256: e697235c78cd79bee84620bc0e678e273ae7efd2ef1a10f4dc5bc61d1b6e82ec
- evidence_id: mb
  kind: database
  reference: https://doi.org/10.21608/mb.2024.307263.1134
  locator: Crossref title, journal and publisher metadata
  accessed_at: '2026-10-21T07:19:46Z'
  support: partial
  summary: 'Resolves to Plant Diseases: Pathogenicity and integrated management overview
    in Microbial Biosystems. A Europe PMC miss is an indexing limit. No abstract or
    article text was inspected, so its detailed note remains unverified.'
  snapshot_sha256: 105ffaabbe08ff47c5914cb4119db4325529faa8dd1d861f8cb8466c2cb092fa
- evidence_id: mpmi
  kind: primary_source
  reference: https://doi.org/10.1094/MPMI-12-23-0212-CR
  locator: PMID38949402 title and abstract review framing
  accessed_at: '2026-10-21T07:19:20Z'
  support: partial
  summary: The review concerns fungal and oomycete pathogens. Its unconventional-secretion
    title alone does not contradict a contextual statement about a conventional pathway.
    Detailed assertions remain unverified.
  snapshot_sha256: 1c0e494ccd2add229f7e04cb8e20b21dcc2c4e0898c70385000645f921be4cdd
- evidence_id: search
  kind: search
  reference: Local identity, ownership and provenance search
  locator: Ignored-inclusive identifier, label/slug and graph searches
  accessed_at: '2026-10-21T07:22:08.310175Z'
  support: partial
  summary: Seventeen events comprise sixteen AI-assisted and one seed import event.
    No explicit human-acceptance link was identified in inspected target-specific
    local material; private/remote approval remains unknown.
  snapshot_sha256: 49601a7eff4a6a9344eea4eb3fcfc2b51fd398b17bff6343d799239f2afa7526
  search_scope: Ignored-inclusive local target/identifier/slug search and complete
    captured METPO inspection. Search receipt records exact bounded directories; provider
    header used as provenance. Private and remote approvals were not searched.
- evidence_id: policy
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/GROUNDING_POLICY.md
  locator: Source scope, graph meaning, optional examples and human sign-off rules
  accessed_at: '2026-10-21T07:24:18Z'
  support: supports
  summary: NONMECHANISTIC scope does not require token protein examples or a universal
    graph. Source-access limits must remain explicit and REVIEWED requires human scientific
    acceptance.
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, host boundary, synonyms and kind'
  outcome: supported
  target_ids:
  - METPO:1004003
  summary: The active ontology class exactly matches the host-defined concept. Removing
    an upstream synonym identical to the label did not lose an alternative term.
  evidence_ids:
  - record
  - identity
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: ontology wording and definition-source limits'
  outcome: concern
  target_ids:
  - METPO:1004003
  summary: The ontology supplies the exact host boundary. Glazebrook is a suitable
    broad plant-pathology context, but the inspected abstract does not independently
    establish that exact boundary or each attached detailed claim. No publication-category
    mismatch is asserted.
  evidence_ids:
  - identity
  - definition-source
  - qualification
- assessment_id: hierarchy
  area: consistency
  topic: 'Native checklist: broader parent'
  outcome: supported
  target_ids:
  - METPO:1004003
  summary: Pathogenic to host is strictly broader; neither the definition nor parent
    restricts the pathogen taxon to bacteria.
  evidence_ids:
  - record
  - identity
  - parent
- assessment_id: category
  area: representation
  topic: 'Native checklist: ecological class and NONMECHANISTIC scope'
  outcome: supported
  target_ids:
  - METPO:1004003
  summary: ECOLOGY/CLASS and the broad graph scope are coherent. Four reviewed generic
    aggregates need no token accessions.
  evidence_ids:
  - record
  - policy
- assessment_id: example
  area: evidence
  topic: 'Native checklist: canonical species and secondary aside'
  outcome: concern
  target_ids:
  - METPO:1004003
  summary: Taxonomy and generic P. syringae model-pathogen wording are supported.
    The parenthetical mechanism and secondary Agrobacterium assertion are unverified
    from the inspected source; failure to retrieve XML is not evidence of absence.
  evidence_ids:
  - taxon
  - secondary-name
  - example
- assessment_id: evidence
  area: evidence
  topic: 'Native checklist: six references and eight snippets'
  outcome: concern
  target_ids:
  - METPO:1004003
  summary: Five identities resolve; the exact wall DOI remains unresolved after several
    ordinary registry/publisher attempts. None of the eight full-text quotations is
    verified by the abstract-only check. Metadata-only and abstract-only limits are
    retained, with no title-based mechanism contradiction.
  evidence_ids:
  - bibliography
  - qualification
  - definition-source
  - unresolved-reference
  - example
  - plants
  - mb
  - mpmi
  - check-plant_pathogen-snippets
- assessment_id: graph
  area: graph
  topic: 'Native checklist: all thirteen nodes and twelve edges'
  outcome: concern
  target_ids:
  - METPO:1004003
  summary: Four edges conflict with external endpoint meanings, with two also showing
    internal negation inconsistency. One provisional relation extends beyond its stated
    subject meaning. Detailed biological mechanisms remain unverified.
  evidence_ids:
  - record
  - relations
  - go
  - ledger
  - shape
  - definition-source
  - unresolved-reference
  - plants
  - mb
  - mpmi
  details: 'Zero-based ledger: node0 is the trait; nodes1–3/12 are reviewed generic
    material aggregates; nodes4–9/11 are process concepts; node10 is a matching GO
    cellular component. Node5 has no current external grounding following the documented
    retraction. Edge0 has compatible actor/process types, but its reference is unresolved.
    Edge1 uses an allowed local ungrounded phrase; exact source support is unverified.
    Edges2/11 have material subjects under process-to-process negative regulation;
    their suppression predicate applied to an already negative object also conflicts
    literally with the accompanying description. Edges3/8 use process subjects under
    enables. Edge4 has compatible broad Biolink endpoints but an unresolved citation.
    Edge5 uses the proposed microorganism-state manifestation relation for a host
    outcome. Edges6/7 have compatible process endpoints without biological certification.
    Edge9 fits the provisional relation’s admitted structure object but has only bibliographic
    source confirmation. Edge10 uses an allowed ungrounded local phrase and retains
    fungal/oomycete context. No alternative pathway, molecular target or experimental
    step is proposed.'
- assessment_id: optional
  area: completeness
  topic: 'Native checklist: discussion and dataset slots'
  outcome: supported
  target_ids:
  - METPO:1004003
  summary: No discussion placeholder or dataset assertion requires resolution. Optional
    data are not invented for this classifier.
  evidence_ids:
  - record
  - policy
- assessment_id: history
  area: provenance
  topic: 'Native checklist: retraction explanation and REVIEWED basis'
  outcome: concern
  target_ids:
  - METPO:1004003
  summary: The local unsupported grounding was withdrawn, which is distinct from ontology
    obsoletion. The historical bacterial-only gloss is narrower than current class/context.
    The inspected local provenance does not identify human acceptance.
  evidence_ids:
  - record
  - history-owner
  - go
  - search
  - policy
  - check-validate-history
findings:
- finding_id: reference-unresolved
  issue_key: plant-pathogen-reference-unresolved
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: An exact citation used in three placements remains unresolved
  description: DOI:10.1146/annurev.micro.55.1.535 did not resolve through the recorded
    Europe PMC, Crossref, DOI Handle and publisher attempts. It supports one record-level
    evidence item and two edges, preventing source inspection for those placements.
    This is a bounded resolution concern; nonexistence of the article and falsity
    of the biological assertions are not established.
  target_ids:
  - METPO:1004003
  field_paths:
  - evidence[1].reference
  - causal_graphs[0].edges[0].evidence
  - causal_graphs[0].edges[4].evidence
  evidence_ids:
  - record
  - unresolved-reference
  - bibliography
  - check-plant_pathogen-snippets
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/plant_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: external-types-and-negation
  issue_key: plant-pathogen-external-types-and-negation
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Four relation uses conflict with their endpoint meanings
  description: Edges2/11 use material-protein subjects with RO process-to-process
    negative regulation; edges3/8 use biological processes as enables executors. Edges2/11
    also literally negate an already negative object, whereas the accompanying descriptions
    state the opposite grammatical relationship. This is internal/ontology consistency
    analysis, not a corrected or validated biological route.
  target_ids:
  - METPO:1004003
  field_paths:
  - causal_graphs[0].edges[2]
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[8].predicate_id
  - causal_graphs[0].edges[11]
  evidence_ids:
  - record
  - relations
  - ledger
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/plant_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping; future changes require separate scope review
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: provisional-manifestation-scope
  issue_key: plant-pathogen-provisional-manifestation-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: A local manifestation relation is extended to a host outcome
  description: The local v2 proposal describes a physiological or molecular state
    of a microorganism manifesting its phenotype. The current edge5 subject is pathology
    in the plant host. The generic local endpoint mapping does not establish this
    semantic extension; this is not a formal validator failure.
  target_ids:
  - METPO:1004003
  field_paths:
  - causal_graphs[0].edges[5].predicate_id
  - causal_graphs[0].nodes[6]
  evidence_ids:
  - record
  - relations
  - identity
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/plant_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping; future changes require separate scope review
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: historical-bacterial-scope-gloss
  issue_key: plant-pathogen-historical-bacterial-scope-gloss
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical rationale calls a broader class a bacterial record
  description: The grounding-retraction event calls this a bacterial record, whereas
    the definition is host-based and existing node11/evidence describe fungal/oomycete
    context. The narrower shorthand should not be interpreted as a class boundary.
    This does not establish that the retracted GO term was an exact match, and no
    reinstatement is proposed.
  target_ids:
  - METPO:1004003
  field_paths:
  - curation_history[15].changes
  evidence_ids:
  - record
  - identity
  - history-owner
  - mpmi
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/plant_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_name_match_groundings.py
    role: Maintained record of historical grounding correction, to be clarified rather
      than silently rewritten
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: reviewed-signoff-not-documented
  issue_key: plant-pathogen-reviewed-signoff-not-documented
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Inspected REVIEWED provenance lacks a human-acceptance link
  description: Sixteen AI-assisted events and one scripted import do not identify
    human scientific acceptance in the inspected target-specific material. Private
    or remote approval is not ruled out.
  target_ids:
  - METPO:1004003
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - record
  - search
  - policy
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/plant_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: resolve-source-identity
  description: Resolve the exact bibliographic identity for the three affected evidence
    placements in separately authorized curation.
  finding_ids:
  - reference-unresolved
  target_ids:
  - METPO:1004003
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/plant_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Recover an authoritative source identity and durable locator, preserving current
    failed-access provenance.
  - Do not guess a replacement paper from topical similarity or infer biological falsity
    from lookup failure.
  - This action concerns citation traceability; it proposes no new pathogen mechanism
    or experimental route.
- action_id: reconcile-graph-language
  description: Reconcile existing entity meanings, selected relation definitions and
    literal edge wording.
  finding_ids:
  - external-types-and-negation
  - provisional-manifestation-scope
  target_ids:
  - METPO:1004003
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/plant_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping; future changes require separate scope review
  acceptance_checks:
  - Check the actual external identifier and distinguish process, material actor,
    microorganism state and host outcome.
  - Do not invent molecular intermediates or infer a corrected biological route from
    grammatical inconsistency.
  - Any authorized future edit requires guarded writes, appended history and applicable
    strict/graph/qc checks.
- action_id: clarify-history
  description: Append a bounded clarification of historical class-scope wording during
    separately authorized curation.
  finding_ids:
  - historical-bacterial-scope-gloss
  target_ids:
  - METPO:1004003
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/plant_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_name_match_groundings.py
    role: Maintained record of historical grounding correction, to be clarified rather
      than silently rewritten
  acceptance_checks:
  - Keep the host-defined class distinct from the context of an individual graph branch.
  - Preserve prior history and do not reinstate the unsupported exact GO mapping.
- action_id: document-status
  description: Locate and document human scientific acceptance or retain the status-basis
    question.
  finding_ids:
  - reviewed-signoff-not-documented
  target_ids:
  - METPO:1004003
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/plant_pathogen.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - AI history, import scripts and deterministic checks do not identify a human approver.
  - Any status change requires separate curation authorization.
limitations:
- All fields were inspected for documentary/conceptual consistency. Detailed virulence,
  plant-immune-suppression and host-exploitation mechanisms were not independently
  certified, reconstructed, corrected or improved.
- Five citation identities resolve and one exact DOI remains unresolved. Failed registry/access
  results do not establish nonexistent literature or false biology.
- 'Eight snippets are inconclusive: five not in inspected abstracts, three attached
  to the unresolved DOI. Complete full-text exactness remains unverified.'
- The secondary Agrobacterium attribution and mechanistic parenthetical remain unverified.
  The model P. syringae species claim is directly supported.
- Glazebrook is not called a wrong publication category; the MPMI title is not used
  to infer a contradiction. Metadata-only confirmation of the Microbial Biosystems
  item does not verify its evidence note.
- GO:0140649 is locally retracted, not a current node grounding. The existing ungrounded
  node is not filled by guessing a near match.
- Local predicate proposals, bounded human-acceptance search, and historical corpus-check
  failures/skips remain explicit.
- No scientific record, mapping, writer, history, native status or generated product
  is changed.
notes:
- Native input capture preceded judgment. Source-agent overstatement about the definition
  citation was explicitly corrected before authoring this review; original access
  receipts were preserved.
- The unresolved-reference finding is provisional, while the recorded resolution failures
  and existing graph wording are direct observations.
tags:
- record-review
- plant-pathogen
- ecology
- needs-curation
```
