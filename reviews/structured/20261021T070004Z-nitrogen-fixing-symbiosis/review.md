# Scientific and source review of nitrogen-fixing symbiosis (traitmech:000044)

- Review: 20261021T070004Z-nitrogen-fixing-symbiosis
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T06:54:20Z
- Finished UTC: 2026-10-21T07:00:04Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The ecological identity, mutualism parent and rhizobium–legume graph scope are coherent. All eleven nodes and ten edges were inspected. The GO/CHEBI identities and strain-matched NifH accession are correct; the historical UniProt version is supported. One major finding distinguishes a trait-domain mismatch from prerequisite/input roles under RO enables. Minor findings concern lost source qualification and the bounded lack of a human-acceptance link. Bibliographic resolution and current annotations are not substitutes for direct strain-specific experimental evidence.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Tenth target in batch002, selected in lexicographic path order using the validated inventory union; one entire previously uncovered TraitRecord.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f25e2af0b38a8303b13f627a9a5c33b36af4b3d2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000044 | data/traits/ecology/nitrogen_fixing_symbiosis.yaml | maintained | nitrogen-fixing symbiosis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000044 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000044 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000044 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | traitmech:000044 | 1276 history records checked, zero invalid links; integrity does not establish scientific correctness or human sign-off. |
| Initial full-product validation | failed | False | traitmech:000044 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000044 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000044 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | traitmech:000044 | The selected record validates. |
| Focused strict validation | passed | True | traitmech:000044 | One file scanned; zero strict errors. |
| Focused source snippet verification | passed | True | traitmech:000044 | One snippet over one reference returned NOT_IN_ABSTRACT. This is inconclusive, not proof that the snippet is absent from the paper. |
| Structured-source adapter runner discovery | unavailable | False | traitmech:000044 | No usable runner found within the documented bounded search. Official dataset API fallback completed. |
| Expression-module applicability | not_applicable | False | traitmech:000044 | Complete official catalog has no matching species/strain dataset. No module search is applicable and no phenotype inference is drawn from absence. |

## Scientific And Domain Assessments

### Native checklist: identifier, definition, aliases and polarity

identity: supported. Targets: traitmech:000044.

The fallback class denotes mutualistic plant-associated nitrogen fixation. The two related aliases retain ecological/root-nodule context without claiming exact synonymy for all wider associations.

### Native checklist: broader mutualism parent

consistency: supported. Targets: traitmech:000044.

The reciprocal-benefit parent is strictly broader than the specified nitrogen/carbon exchange association. The explicitly rhizobium–legume graph is narrower than the class rather than a universal mechanism claim.

### Native checklist: ecological class and mechanistic graph scope

representation: supported. Targets: traitmech:000044.

ECOLOGY/CLASS match the trait. A bacterial strain-matched component supports the mechanistic scope while the host protein remains explicitly contextual; no token accession is required for that family.

### Native checklist: species, strain and external node identities

grounding: supported. Targets: traitmech:000044.

Both taxa, active GO terms and the CHEBI chemical class match. The species synonym and later UniProt annotation update do not constitute identifier errors.

### Native checklist: species and strain/protein examples

evidence: concern. Targets: traitmech:000044.

The model species and reference strain are supported by the comparative-genomics source and exact database identity. The cited mutant experiment’s strain detail and exact snippet remain unverified because full text was unavailable. The superlative most-studied is likewise not independently established.

### Native checklist: all references and source notes

evidence: concern. Targets: traitmech:000044.

All eight reference identities resolve. Inspected full texts support the assigned signalling, oxygen, nutrient and ATP contexts. The diffusion-barrier note drops a source qualification; the sole exact snippet remains inconclusive.

### Native checklist: all eleven nodes and ten edges

graph: concern. Targets: traitmech:000044.

The graph is connected and the anchored component is correctly scoped. Three enables edges confuse disposition, prerequisite or input roles with material execution. The chemical signal edge is type-compatible and is not counted as a definite ontology error.

Zero-based ledger: node0 is the local trait; nodes1/2 are signalling/fixation processes, with node2 correctly grounded. Nodes3/4 are chemical signals; node5 is an explicitly contextual host-protein family. Node6 describes a cellular anatomical barrier; node7 is a low-oxygen condition. Node8 is the correctly grounded complex, with NifH explicitly just one component. Node9 is a broad chemical input and node10 iron availability. Edge0 fits provisional process-to-trait confers within the graph context, without establishing that signalling alone suffices for functional fixation. Edge1 has a disposition subject under material-executor enables. Edge2 has a supported ungrounded induction phrase. Edge3 is material-to-process compatible; its signal/trigger-versus-executor interpretation is a bounded precision question. Edge4 has supported buffering context. Edge5 has qualified source support and a stronger record formulation. Edge6 describes a prerequisite rather than an executor. Edge7 has compatible complex-to-process execution and the ATP number matches. Edge8 describes carbon input rather than execution. Edge9 has supported cofactor context and no external predicate assertion. Ungrounded local predicates are schema-permitted; graph connectivity is not proof of a complete molecular model.

### Native checklist: structured transcriptomic cross-check

evidence: not_applicable. Targets: traitmech:000044.

The official catalog supplies no matching species/strain dataset. Neither a different rhizobial genus nor similarity-based UniProt annotations establish direct strain-specific transcriptomic or experimental support.

### Native checklist: discussion and dataset slots

completeness: supported. Targets: traitmech:000044.

No discussion placeholder or asserted dataset accession requires resolution. Optional additions are not invented to make the review look more complete.

### Native checklist: REVIEWED, history and provider provenance

provenance: concern. Targets: traitmech:000044.

Eight AI-assisted events and a historical provider report document work, but no human-acceptance link was found in inspected target-specific materials. Provider output is provenance, not primary evidence or human scientific approval.

## Findings

### enables-endpoint-roles: Three enables edges do not express the required executor role

major / open / confirmed; issue key: nitrogen-fixing-symbiosis-enables-endpoint-roles.

Edge1 supplies a trait/disposition where RO:0002327 inherits a material-executor subject. Edge6 supplies a low-oxygen prerequisite condition. Edge8 supplies chemical fuel/reductant: its material type is compatible, but the described input role does not itself execute fixation. These are distinct domain/role problems under one relation; no formal material-domain error is asserted for the chemical. Edge3 is deliberately excluded from the definite error count.

### barrier-source-qualification: The diffusion-barrier note loses the cited source qualification

minor / open / confirmed; issue key: nitrogen-fixing-symbiosis-barrier-source-qualification.

The inspected author PDF describes the barrier’s oxygen-limiting role with thought to, whereas the edge and note state it categorically. The additional multilayered-cortex/adaptable characterization was not located in the searchable cited PDF. Preserve the source’s certainty or provide a precise supporting source; this is bounded source precision, not a finding that the physiological barrier is false.

### reviewed-signoff-not-documented: The inspected REVIEWED provenance lacks a human-acceptance link

minor / open / confirmed; issue key: nitrogen-fixing-symbiosis-reviewed-signoff-not-documented.

All eight target events disclose AI assistance but do not identify human scientific acceptance. The native checklist requires it for REVIEWED. The finding is bounded to inspected local target-specific provenance and does not establish absence of private or remote approval.

## Recommended Actions And Acceptance Checks

### reconcile-relation-roles

Reconcile the existing endpoint concepts with relation meanings during separately authorized curation.

- Distinguish the trait/disposition, permissive condition, supplied input and executing complex; do not retype entities merely to fit an identifier.
- Inspect inherited external definitions and retain provisional status for local proposals.
- Review any shared mapping change separately; use guarded writes, new history and applicable validation/qc gates.

### preserve-source-qualification

Align the barrier wording with the source strength and precise locator.

- Retain the source qualification unless another inspected source supports stronger wording.
- Document the source and locator for any added anatomical/adaptability characterization.
- Do not infer that a failed word search disproves a physiological mechanism.

### document-status-basis

Locate and document the human-acceptance basis or retain the question as unresolved.

- AI assistance, validated schema and publication do not identify a human approver.
- Any change to scientific status requires separate authorization and a new history event.

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
| check-nitrogen_fixing_symbiosis-validate | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/nitrogen_fixing_symbiosis-validate.log; Executed 2026-10-21T06:54:39Z through 2026-10-21T06:54:41Z; metadata nitrogen_fixing_symbiosis-validate.json | context_only | The selected record validates. |
| check-nitrogen_fixing_symbiosis-strict | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/nitrogen_fixing_symbiosis-strict.log; Executed 2026-10-21T06:54:39Z through 2026-10-21T06:54:42Z; metadata nitrogen_fixing_symbiosis-strict.json | context_only | One file scanned; zero strict errors. |
| check-nitrogen_fixing_symbiosis-snippets | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/nitrogen_fixing_symbiosis-snippets.log; Executed 2026-10-21T06:54:44Z through 2026-10-21T06:54:52Z; metadata nitrogen_fixing_symbiosis-snippets.json | context_only | One snippet over one reference returned NOT_IN_ABSTRACT. This is inconclusive, not proof that the snippet is absent from the paper. |
| record | data/traits/ecology/nitrogen_fixing_symbiosis.yaml; Entire record, two taxon examples, one protein example, eleven nodes, ten edges and eight history events | partial | The broad plant-bacterium trait has an explicitly narrower rhizobium–legume mechanism. Scope notes distinguish the bacterial NifH component from the full nitrogenase complex and contextual host leghemoglobin. |
| identity | data/raw/metpo.owl; proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv; Complete parsed RDF normalized exact label/synonym scan, including deprecated entities; v5 class row46 | supports | No exact target/synonym match occurs in the captured ontology. Fallback traitmech:000044 and proposed METPO:1007643 agree. The parent proposal is the local mutualism class; no upstream acceptance is inferred. |
| parent | data/traits/ecology/mutualism.yaml; Entire parent definition | supports | Reciprocal nitrogen/carbon exchange in a plant-bacterium association narrows the reciprocal-benefit parent. The graph is not asserted as universal for every nitrogen-fixing association. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0009399%2CGO%3A0016610; Exact term responses, namespace and obsolete status | supports | GO:0009399 is active nitrogen fixation in biological_process; GO:0016610 is active nitrogenase complex in cellular_component. Both match the represented concepts. The complex grounding is not a molecular-function mismatch. |
| chebi | Previously downloaded CHEBI authority database; Exact CHEBI:64709 label, definition and related plural synonym | supports | CHEBI:64709 is organic acid and matches the broad node class. Identity does not imply that every organic acid supports the phenotype. |
| taxa | https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=266834; Live strain response and preceding species382 response | supports | Taxon266834 is strain Sinorhizobium meliloti1021 under382. Species382’s Sinorhizobium meliloti name is an authority-recognized synonym of Ensifer meliloti. The earlier species receipt retains its original06:49:38UTC acquisition time. |
| uniprot-current | https://rest.uniprot.org/uniprotkb/P00460.json; Accession, review status, gene, taxon, entry audit, FUNCTION and SUBUNIT | supports | P00460 is reviewed NifH for taxon266834. Current entry159/sequence2 was updated September2,2026. Functional comments use similarity evidence ECO:0000250, so this is database support for identity/component role, not independent direct evidence of the cited mutant. |
| uniprot-historical | https://rest.uniprot.org/unisave/P00460?format=txt&amp;versions=158; Historical flatfile header, gene, organism and taxon | supports | Version158 is reviewed, dated January28,2026, with sequence2 and the same nifH/taxon identity. The record’s August25 retrieval/version claim is historically coherent; later entry159 is not an original error. This establishes version availability, not an independent log of the historical curator’s actual request. |
| provisional | proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv; mappings/predicate_grounding.tsv; METPO:2007700 definition and allowed endpoint roles | supports | The locally proposed confers relation allows process-to-TRAIT. Its documented placeholder status is retained; it is not an active exact predicate in the captured METPO release. |
| shape | Read-only graph ledger; Eleven nodes, ten edges, all endpoints, undirected components and protein-example count | supports | All endpoints resolve and the mechanistic graph has one undirected component with one protein example. Connectivity does not establish scientific completeness. |
| poole | https://www.nature.com/articles/nrmicro.2017.171; Publisher preview Key Points, especially final bullet, and abstract; PMID29379215 | supports | The preview supports legume-associated nitrogen-fixing bacteroids receiving plant-derived dicarboxylate carbon in exchange for fixed nitrogen. Subscription full text was not inspected. |
| oldroyd | https://www.nature.com/articles/nrmicro2990; Publisher preview Key Points and abstract | supports | The review describes signalling in beneficial rhizobial and mycorrhizal associations. Its broader subject does not invalidate the record’s specifically rhizobial signalling context; signalling alone is not equated with completed nitrogen fixation. |
| example | https://pmc.ncbi.nlm.nih.gov/articles/PMC3164228/; Full XML abstract, Background and Discussion; PMID21569405 | partial | The paper supports S. meliloti as a model nitrogen-fixing symbiont of Medicago/alfalfa and Rm1021 as a laboratory/reference strain. The comparative superlative most-studied is not independently established by this paper. A legitimate public full-text XML service supplied the article; the separate browser challenge was not treated as article content. |
| policy | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/GROUNDING_POLICY.md; Claim-specific source scope, mechanistic graph examples, relation semantics and human sign-off | supports | A strain-matched component may anchor a broader complex when its limited role is explicit. Contextual host proteins need not receive unrelated bacterial accessions. Shape and automated validation do not supply human acceptance. |
| search | Local target identity/ownership/provenance search; Ignored-inclusive identifier, label, slug and P00460 search | partial | Eight target events identify AI assistance. Inspected target-specific maintained provenance does not identify human scientific acceptance; private or remote approval remains unknown. |
| relations | Previously downloaded RO authority database; RO:0002327 with recursive superproperties, definitions and inherited endpoint constraints | partial | Enables requires a material entity acting to execute a process. A trait/disposition violates the inherited subject meaning; a low-oxygen condition and a supplied carbon input express prerequisite/input roles rather than execution. Chemical subjects are not categorically excluded. The fresh read confirms earlier inspected statements and records the database hash. |
| bibliography | https://www.ebi.ac.uk/europepmc/webservices/rest/search; https://api.crossref.org/works/10.1017%2FS1062798724000309; Eight unique citation identities and complete claim/access ledger | supports | Seven references resolve through indexed biomedical metadata; the Cambridge article is independently identified through Crossref and its publisher PDF. Failure to find it in Europe PMC was not treated as an invalid DOI. |
| signals | https://pmc.ncbi.nlm.nih.gov/articles/PMC10810997/; Introduction s1 paragraph2; section s5 first paragraph; DOI10.3389/fpls.2023.1284720 | supports | The article supports the existing flavonoid/Nod-factor signalling notes, oxygen buffering by leghemoglobin and a low-oxygen requirement for proper nitrogenase activity. Source support for a prerequisite is distinct from the selected external executor relation. |
| nodule | https://www.sachslab.com/resources/2024_Porter_et_al.pdf; PDF p2, Legume–rhizobium cooperation requires coordination, paragraph2; DOI10.1038/s41564-024-01762-2 | partial | The paragraph supports host supply of organic-acid reductant and a tightly packed cellular diffusion barrier. It qualifies the barrier’s limiting role as thought to. The record’s stronger certainty and added multilayered/adaptable wording exceed what was located in that passage and searchable PDF; this does not establish that the biology is false. |
| atp | https://doi.org/10.1017/S1062798724000309; Publisher PDF printed p387, PDF p5, displayed nitrogenase reaction | supports | The displayed reaction explicitly consumes sixteen ATP per N2. The record’s numerical statement matches the cited source; no numerical defect is inferred. |
| iron | https://pmc.ncbi.nlm.nih.gov/articles/PMC11662446/; Introduction s1 paragraph4; DOI10.1093/pcp/pcae128 | supports | The text supports iron’s cofactor role in leghemoglobin and nitrogenase assembly. The edge represents the nitrogenase branch; the evidence note also supplies host-protein context. |
| nifh-paper | https://doi.org/10.1094/MPMI-06-25-0074-R; Indexed abstract, PMID40559515; ordinary publisher full-text access failures | partial | The abstract supports the S. meliloti–alfalfa association and a comparison involving non-fixing bacteria, but does not establish strain1021 or the exact nifH1491::Tn5 snippet. Those direct experimental details remain unverified. UniProt identity and similarity annotations do not substitute for inspection of the cited experiment. |
| expression | https://imodulondb.org/api/datasets; Complete official dataset catalog, twenty organism entries | context_only | No Ensifer/Sinorhizobium/Rhizobium meliloti dataset matches the target. Listed Bradyrhizobium is a different organism; its modules are not transferred to strain1021. This is lack of applicable expression evidence, not negative biological evidence. |
| runner | Local structured-source runner discovery; PATH, twenty-five pyprojects and twenty-seven standard environment entrypoints | context_only | No usable kg-microbe-sources runner was found within the stated bounded roots, so the skill’s official-source fallback was used. This is not a whole-disk absence claim. |

## Limits And Additional Notes

- The exact nifH1491::Tn5 snippet and strain1021-specific experiment in DOI10.1094/MPMI-06-25-0074-R remain unverified after ordinary public full-text access failed. The abstract check is inconclusive, and similarity-based UniProt comments do not replace experimental evidence.
- Poole and Oldroyd were inspected through publisher previews and abstracts, not complete subscription articles. Public full text was inspected for the other five sources.
- The most-studied ranking in canonical example0 is not independently established. The model/reference-strain identity is supported.
- Edge3’s signal-versus-executor interpretation remains a bounded question; material-subject typing alone does not establish an error.
- The bounded local runner search found no usable structured adapter; the official dataset API fallback was inspected. No matching strain dataset exists in that retrieved catalog, which is not negative biological evidence.
- Historical UniSave supports version158/sequence2 availability. It cannot independently establish that a curator made the claimed retrieval on August25; current159 is a later update.
- CHEBI and RO authority checks use the captured/downloaded releases. The local METPO confers identifier remains a proposal.
- Earlier full-corpus diagnostics retain actual timestamps, baselines, superseded network failures and product-adapter skips at the unchanged source base.
- No scientific record, mapping, proposal, history or native status is changed. No human scientific sign-off is supplied.
- Initial native inspection captured32inputs; the expanded33-input capture added the inspected provider provenance header and verified all original hashes unchanged.
- Independent source/ontology checks informed this manually authored complete-record review. No experimental procedure or microbial engineering recommendation is proposed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070004Z-nitrogen-fixing-symbiosis
kind: record
repository: CultureBotAI/TraitMech
title: Scientific and source review of nitrogen-fixing symbiosis (traitmech:000044)
started_at: '2026-10-21T06:54:20Z'
finished_at: '2026-10-21T07:00:04Z'
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
summary: The ecological identity, mutualism parent and rhizobium–legume graph scope
  are coherent. All eleven nodes and ten edges were inspected. The GO/CHEBI identities
  and strain-matched NifH accession are correct; the historical UniProt version is
  supported. One major finding distinguishes a trait-domain mismatch from prerequisite/input
  roles under RO enables. Minor findings concern lost source qualification and the
  bounded lack of a human-acceptance link. Bibliographic resolution and current annotations
  are not substitutes for direct strain-specific experimental evidence.
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
  - path: data/traits/ecology/mutualism.yaml
    sha256: 7247ae4be59ce2eb7f1cc9d7303e1a338af82cd49d255c60aa1442f6dc1c48a3
    role: context
  - path: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    sha256: d4d85f1d5e370d5862b086ae52a716dee3fc5f8880639bffa4e2dff65e9d1574
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
  - path: research/traits/ecology/nitrogen_fixing_symbiosis-deep-research-falcon.md
    sha256: 572ea0c6910655f00cbb4e862082f151761d4f59f05599d7aaeef3d073b2539d
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
  - path: scripts/run_trait_graph_audit.py
    sha256: ed4d1d36057c5b0278f410cb83fdcccd864c28e895fdc4a711dbb06a71472d7c
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
- target_id: traitmech:000044
  path: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
  label: nitrogen-fixing symbiosis
  kind: maintained
  record_class: TraitRecord
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    role: Maintained scientific record
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Shared node mapping
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Tenth target in batch002, selected in lexicographic path order using
    the validated inventory union; one entire previously uncovered TraitRecord.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000044
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000044
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
  - traitmech:000044
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
  - traitmech:000044
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
  - traitmech:000044
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
  - traitmech:000044
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
  - traitmech:000044
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
  - traitmech:000044
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: nitrogen_fixing_symbiosis-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000044
  command: just validate data/traits/ecology/nitrogen_fixing_symbiosis.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The selected record validates.
  evidence_ids:
  - check-nitrogen_fixing_symbiosis-validate
- check_id: nitrogen_fixing_symbiosis-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000044
  command: just validate-strict data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    --out /private/tmp/traitmech-record-sweep-002.mdt7dqwk/nitrogen_fixing_symbiosis-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero strict errors.
  evidence_ids:
  - check-nitrogen_fixing_symbiosis-strict
- check_id: nitrogen_fixing_symbiosis-snippets
  name: Focused source snippet verification
  status: passed
  required: true
  target_ids:
  - traitmech:000044
  command: just verify-snippets --record data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    --out /private/tmp/traitmech-record-sweep-002.mdt7dqwk/nitrogen_fixing_symbiosis-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: One snippet over one reference returned NOT_IN_ABSTRACT. This is inconclusive,
    not proof that the snippet is absent from the paper.
  evidence_ids:
  - check-nitrogen_fixing_symbiosis-snippets
- check_id: structured-runner
  name: Structured-source adapter runner discovery
  status: unavailable
  required: false
  target_ids:
  - traitmech:000044
  summary: No usable runner found within the documented bounded search. Official dataset
    API fallback completed.
  evidence_ids:
  - runner
- check_id: expression-applicability
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000044
  summary: Complete official catalog has no matching species/strain dataset. No module
    search is applicable and no phenotype inference is drawn from absence.
  evidence_ids:
  - expression
  - runner
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T07:00:04Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T07:00:04Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T07:00:04Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; metadata validate-history.json
  accessed_at: '2026-10-21T07:00:04Z'
  support: context_only
  summary: 1276 history records checked, zero invalid links; integrity does not establish
    scientific correctness or human sign-off.
  snapshot_sha256: 1fc48f1203fbfcd27b1243e4e147afb367aebfc592b496b352201058c6ee85d2
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T07:00:04Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T07:00:04Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T07:00:04Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-nitrogen_fixing_symbiosis-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/nitrogen_fixing_symbiosis-validate.log
  locator: Executed 2026-10-21T06:54:39Z through 2026-10-21T06:54:41Z; metadata nitrogen_fixing_symbiosis-validate.json
  accessed_at: '2026-10-21T07:00:04Z'
  support: context_only
  summary: The selected record validates.
  snapshot_sha256: a5f7af6903de23af68e2d7b6a53d4795488784bd021ee8fb82c5d00721964981
- evidence_id: check-nitrogen_fixing_symbiosis-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/nitrogen_fixing_symbiosis-strict.log
  locator: Executed 2026-10-21T06:54:39Z through 2026-10-21T06:54:42Z; metadata nitrogen_fixing_symbiosis-strict.json
  accessed_at: '2026-10-21T07:00:04Z'
  support: context_only
  summary: One file scanned; zero strict errors.
  snapshot_sha256: 6b659df558ddc315c23965f87db00c6432cc693cb9be3fa19751f9f23ba99d0b
- evidence_id: check-nitrogen_fixing_symbiosis-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/nitrogen_fixing_symbiosis-snippets.log
  locator: Executed 2026-10-21T06:54:44Z through 2026-10-21T06:54:52Z; metadata nitrogen_fixing_symbiosis-snippets.json
  accessed_at: '2026-10-21T07:00:04Z'
  support: context_only
  summary: One snippet over one reference returned NOT_IN_ABSTRACT. This is inconclusive,
    not proof that the snippet is absent from the paper.
  snapshot_sha256: 70b94864dfac161414e4764c7e3df5ad53c4f0f7af03ffcef1238f9a03db62d7
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
  locator: Entire record, two taxon examples, one protein example, eleven nodes, ten
    edges and eight history events
  accessed_at: '2026-10-21T07:00:04Z'
  support: partial
  summary: The broad plant-bacterium trait has an explicitly narrower rhizobium–legume
    mechanism. Scope notes distinguish the bacterial NifH component from the full
    nitrogenase complex and contextual host leghemoglobin.
  snapshot_sha256: d4d85f1d5e370d5862b086ae52a716dee3fc5f8880639bffa4e2dff65e9d1574
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl; proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
  locator: Complete parsed RDF normalized exact label/synonym scan, including deprecated
    entities; v5 class row46
  accessed_at: '2026-10-21T06:54:55Z'
  support: supports
  summary: No exact target/synonym match occurs in the captured ontology. Fallback
    traitmech:000044 and proposed METPO:1007643 agree. The parent proposal is the
    local mutualism class; no upstream acceptance is inferred.
  snapshot_sha256: 3efa4e1c39c7cfe9284823bdedf81e479f01c26cbd1b4eb0454b132a413b7613
- evidence_id: parent
  kind: record_content
  reference: data/traits/ecology/mutualism.yaml
  locator: Entire parent definition
  accessed_at: '2026-10-21T07:00:04Z'
  support: supports
  summary: Reciprocal nitrogen/carbon exchange in a plant-bacterium association narrows
    the reciprocal-benefit parent. The graph is not asserted as universal for every
    nitrogen-fixing association.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0009399%2CGO%3A0016610
  locator: Exact term responses, namespace and obsolete status
  accessed_at: '2026-10-21T06:55:09Z'
  support: supports
  summary: GO:0009399 is active nitrogen fixation in biological_process; GO:0016610
    is active nitrogenase complex in cellular_component. Both match the represented
    concepts. The complex grounding is not a molecular-function mismatch.
  snapshot_sha256: 4f7d87f40563bf26c51231975aba7ea536ba82967f97e9f4846483f993bcb8fe
- evidence_id: chebi
  kind: authority
  reference: Previously downloaded CHEBI authority database
  locator: Exact CHEBI:64709 label, definition and related plural synonym
  accessed_at: '2026-10-21T06:54:55Z'
  support: supports
  summary: CHEBI:64709 is organic acid and matches the broad node class. Identity
    does not imply that every organic acid supports the phenotype.
  snapshot_sha256: d3ec57726087e6b7dafde02e6f2fe9fc356f631e0fca3ada12023c11abb9a718
- evidence_id: taxa
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=266834
  locator: Live strain response and preceding species382 response
  accessed_at: '2026-10-21T06:55:08Z'
  support: supports
  summary: Taxon266834 is strain Sinorhizobium meliloti1021 under382. Species382’s
    Sinorhizobium meliloti name is an authority-recognized synonym of Ensifer meliloti.
    The earlier species receipt retains its original06:49:38UTC acquisition time.
  snapshot_sha256: afe6d4359c41607ed74aecadf98d6a11c6b76fc33ad2bb2d9fc9037b111bdd8c
- evidence_id: uniprot-current
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P00460.json
  locator: Accession, review status, gene, taxon, entry audit, FUNCTION and SUBUNIT
  accessed_at: '2026-10-21T06:55:11Z'
  support: supports
  summary: P00460 is reviewed NifH for taxon266834. Current entry159/sequence2 was
    updated September2,2026. Functional comments use similarity evidence ECO:0000250,
    so this is database support for identity/component role, not independent direct
    evidence of the cited mutant.
  snapshot_sha256: ccec314bdde14a4eb6390e54ac232e623d84940a0fda03310f852cd845f1c062
- evidence_id: uniprot-historical
  kind: database
  reference: https://rest.uniprot.org/unisave/P00460?format=txt&versions=158
  locator: Historical flatfile header, gene, organism and taxon
  accessed_at: '2026-10-21T06:55:09Z'
  support: supports
  summary: Version158 is reviewed, dated January28,2026, with sequence2 and the same
    nifH/taxon identity. The record’s August25 retrieval/version claim is historically
    coherent; later entry159 is not an original error. This establishes version availability,
    not an independent log of the historical curator’s actual request.
  snapshot_sha256: 40dd9e33a764602aa46ab0c8eb719ec7268d7f95fcf289484b01b3097dee8b0d
- evidence_id: provisional
  kind: authority
  reference: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv; mappings/predicate_grounding.tsv
  locator: METPO:2007700 definition and allowed endpoint roles
  accessed_at: '2026-10-21T07:00:04Z'
  support: supports
  summary: The locally proposed confers relation allows process-to-TRAIT. Its documented
    placeholder status is retained; it is not an active exact predicate in the captured
    METPO release.
- evidence_id: shape
  kind: validation
  reference: Read-only graph ledger
  locator: Eleven nodes, ten edges, all endpoints, undirected components and protein-example
    count
  accessed_at: '2026-10-21T06:55:52Z'
  support: supports
  summary: All endpoints resolve and the mechanistic graph has one undirected component
    with one protein example. Connectivity does not establish scientific completeness.
  snapshot_sha256: 262c606cbcefaa702b11025a4000b9e4c8efdb1546270d8a8fc9ab1235377d07
- evidence_id: poole
  kind: primary_source
  reference: https://www.nature.com/articles/nrmicro.2017.171
  locator: Publisher preview Key Points, especially final bullet, and abstract; PMID29379215
  accessed_at: '2026-10-21T06:55:31Z'
  support: supports
  summary: The preview supports legume-associated nitrogen-fixing bacteroids receiving
    plant-derived dicarboxylate carbon in exchange for fixed nitrogen. Subscription
    full text was not inspected.
  snapshot_sha256: 7b4ebff99dfd916a0e486edc82e879980e66d4adc383ee7b8ccb7fa1c68c11df
- evidence_id: oldroyd
  kind: primary_source
  reference: https://www.nature.com/articles/nrmicro2990
  locator: Publisher preview Key Points and abstract
  accessed_at: '2026-10-21T06:55:31Z'
  support: supports
  summary: The review describes signalling in beneficial rhizobial and mycorrhizal
    associations. Its broader subject does not invalidate the record’s specifically
    rhizobial signalling context; signalling alone is not equated with completed nitrogen
    fixation.
  snapshot_sha256: 7b4ebff99dfd916a0e486edc82e879980e66d4adc383ee7b8ccb7fa1c68c11df
- evidence_id: example
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3164228/
  locator: Full XML abstract, Background and Discussion; PMID21569405
  accessed_at: '2026-10-21T06:55:47Z'
  support: partial
  summary: The paper supports S. meliloti as a model nitrogen-fixing symbiont of Medicago/alfalfa
    and Rm1021 as a laboratory/reference strain. The comparative superlative most-studied
    is not independently established by this paper. A legitimate public full-text
    XML service supplied the article; the separate browser challenge was not treated
    as article content.
  snapshot_sha256: 5843dd7d16c34c6d959140c4624637ee51ece986afef31953862f9dffc193038
- evidence_id: policy
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/GROUNDING_POLICY.md
  locator: Claim-specific source scope, mechanistic graph examples, relation semantics
    and human sign-off
  accessed_at: '2026-10-21T07:00:04Z'
  support: supports
  summary: A strain-matched component may anchor a broader complex when its limited
    role is explicit. Contextual host proteins need not receive unrelated bacterial
    accessions. Shape and automated validation do not supply human acceptance.
- evidence_id: search
  kind: search
  reference: Local target identity/ownership/provenance search
  locator: Ignored-inclusive identifier, label, slug and P00460 search
  accessed_at: '2026-10-21T06:57:16Z'
  support: partial
  summary: Eight target events identify AI assistance. Inspected target-specific maintained
    provenance does not identify human scientific acceptance; private or remote approval
    remains unknown.
  snapshot_sha256: 755ea76e7a86e62cf9802206446a66cf7d44b074d83c9e42354a676fd8c2b863
  search_scope: rg --no-ignore --hidden over data/traits, scripts, history, mappings,
    proposals, conf, docs and DO_NOT_WORK.md; ignored files included. The provider
    report header was inspected separately as provenance and included in the expanded
    native capture. No absence of private/remote approval is claimed.
- evidence_id: relations
  kind: authority
  reference: Previously downloaded RO authority database
  locator: RO:0002327 with recursive superproperties, definitions and inherited endpoint
    constraints
  accessed_at: '2026-10-21T06:58:20Z'
  support: partial
  summary: Enables requires a material entity acting to execute a process. A trait/disposition
    violates the inherited subject meaning; a low-oxygen condition and a supplied
    carbon input express prerequisite/input roles rather than execution. Chemical
    subjects are not categorically excluded. The fresh read confirms earlier inspected
    statements and records the database hash.
  snapshot_sha256: 1d7b65b3528f37e457d2faa1737b8a2a294e912373ff5dcb4ee0e412f2320efb
- evidence_id: bibliography
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search; https://api.crossref.org/works/10.1017%2FS1062798724000309
  locator: Eight unique citation identities and complete claim/access ledger
  accessed_at: '2026-10-21T06:58:41Z'
  support: supports
  summary: Seven references resolve through indexed biomedical metadata; the Cambridge
    article is independently identified through Crossref and its publisher PDF. Failure
    to find it in Europe PMC was not treated as an invalid DOI.
  snapshot_sha256: 073d6432e72bf55008a89959002347c43f35613f7a35cfbfcbd42fa0690be526
- evidence_id: signals
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10810997/
  locator: Introduction s1 paragraph2; section s5 first paragraph; DOI10.3389/fpls.2023.1284720
  accessed_at: '2026-10-21T06:54:56Z'
  support: supports
  summary: The article supports the existing flavonoid/Nod-factor signalling notes,
    oxygen buffering by leghemoglobin and a low-oxygen requirement for proper nitrogenase
    activity. Source support for a prerequisite is distinct from the selected external
    executor relation.
  snapshot_sha256: 393aab3f5dd38cbc8bb6b1c799d502a8ef497150ca036a15f25958ec581fe573
- evidence_id: nodule
  kind: primary_source
  reference: https://www.sachslab.com/resources/2024_Porter_et_al.pdf
  locator: PDF p2, Legume–rhizobium cooperation requires coordination, paragraph2;
    DOI10.1038/s41564-024-01762-2
  accessed_at: '2026-10-21T06:57:43Z'
  support: partial
  summary: The paragraph supports host supply of organic-acid reductant and a tightly
    packed cellular diffusion barrier. It qualifies the barrier’s limiting role as
    thought to. The record’s stronger certainty and added multilayered/adaptable wording
    exceed what was located in that passage and searchable PDF; this does not establish
    that the biology is false.
  snapshot_sha256: 78df16f5e90837cdeb16a3474de901da2a4f7a5a49ea50ad062a4826adecabe7
- evidence_id: atp
  kind: primary_source
  reference: https://doi.org/10.1017/S1062798724000309
  locator: Publisher PDF printed p387, PDF p5, displayed nitrogenase reaction
  accessed_at: '2026-10-21T06:57:43Z'
  support: supports
  summary: The displayed reaction explicitly consumes sixteen ATP per N2. The record’s
    numerical statement matches the cited source; no numerical defect is inferred.
  snapshot_sha256: 42f959e50ebecd5313c9f6872775a326e9a90a615eb9ec8a234728ffdbcac40c
- evidence_id: iron
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC11662446/
  locator: Introduction s1 paragraph4; DOI10.1093/pcp/pcae128
  accessed_at: '2026-10-21T06:55:03Z'
  support: supports
  summary: The text supports iron’s cofactor role in leghemoglobin and nitrogenase
    assembly. The edge represents the nitrogenase branch; the evidence note also supplies
    host-protein context.
  snapshot_sha256: 5b1c11018427c1a34bdc7590a0af82eb2eba6478305f62e5aa492fd01d498805
- evidence_id: nifh-paper
  kind: primary_source
  reference: https://doi.org/10.1094/MPMI-06-25-0074-R
  locator: Indexed abstract, PMID40559515; ordinary publisher full-text access failures
  accessed_at: '2026-10-21T06:54:54Z'
  support: partial
  summary: The abstract supports the S. meliloti–alfalfa association and a comparison
    involving non-fixing bacteria, but does not establish strain1021 or the exact
    nifH1491::Tn5 snippet. Those direct experimental details remain unverified. UniProt
    identity and similarity annotations do not substitute for inspection of the cited
    experiment.
  snapshot_sha256: cd7de0d2e6b925fae095ce1f440ebad4e30d642d913b7bb3af5ba675f5cbab61
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete official dataset catalog, twenty organism entries
  accessed_at: '2026-10-21T06:56:06Z'
  support: context_only
  summary: No Ensifer/Sinorhizobium/Rhizobium meliloti dataset matches the target.
    Listed Bradyrhizobium is a different organism; its modules are not transferred
    to strain1021. This is lack of applicable expression evidence, not negative biological
    evidence.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: runner
  kind: search
  reference: Local structured-source runner discovery
  locator: PATH, twenty-five pyprojects and twenty-seven standard environment entrypoints
  accessed_at: '2026-10-21T06:58:48Z'
  support: context_only
  summary: No usable kg-microbe-sources runner was found within the stated bounded
    roots, so the skill’s official-source fallback was used. This is not a whole-disk
    absence claim.
  snapshot_sha256: ed39e030e16124a47c97e599bf02a4f44fd492af7142325cfc10576dd2cc5386
  search_scope: PATH lookup plus rg --files --no-ignore --hidden under /Users/marcin/Documents/VIMSS/ontology/claw,
    wizard-claw and Mechs, excluding .git and .venv internals for project discovery;
    inspected all25 discovered pyprojects and explicitly checked27 standard .venv/bin/kg-microbe-sources
    locations. Ignored/hidden project files included; private/other roots not claimed.
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, definition, aliases and polarity'
  outcome: supported
  target_ids:
  - traitmech:000044
  summary: The fallback class denotes mutualistic plant-associated nitrogen fixation.
    The two related aliases retain ecological/root-nodule context without claiming
    exact synonymy for all wider associations.
  evidence_ids:
  - record
  - identity
  - poole
  - oldroyd
- assessment_id: hierarchy
  area: consistency
  topic: 'Native checklist: broader mutualism parent'
  outcome: supported
  target_ids:
  - traitmech:000044
  summary: The reciprocal-benefit parent is strictly broader than the specified nitrogen/carbon
    exchange association. The explicitly rhizobium–legume graph is narrower than the
    class rather than a universal mechanism claim.
  evidence_ids:
  - record
  - parent
  - poole
- assessment_id: category
  area: representation
  topic: 'Native checklist: ecological class and mechanistic graph scope'
  outcome: supported
  target_ids:
  - traitmech:000044
  summary: ECOLOGY/CLASS match the trait. A bacterial strain-matched component supports
    the mechanistic scope while the host protein remains explicitly contextual; no
    token accession is required for that family.
  evidence_ids:
  - record
  - policy
  - uniprot-current
  - uniprot-historical
- assessment_id: taxa
  area: grounding
  topic: 'Native checklist: species, strain and external node identities'
  outcome: supported
  target_ids:
  - traitmech:000044
  summary: Both taxa, active GO terms and the CHEBI chemical class match. The species
    synonym and later UniProt annotation update do not constitute identifier errors.
  evidence_ids:
  - taxa
  - go
  - chebi
  - uniprot-current
  - uniprot-historical
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: species and strain/protein examples'
  outcome: concern
  target_ids:
  - traitmech:000044
  summary: The model species and reference strain are supported by the comparative-genomics
    source and exact database identity. The cited mutant experiment’s strain detail
    and exact snippet remain unverified because full text was unavailable. The superlative
    most-studied is likewise not independently established.
  evidence_ids:
  - example
  - taxa
  - uniprot-current
  - uniprot-historical
  - nifh-paper
  - check-nitrogen_fixing_symbiosis-snippets
- assessment_id: evidence
  area: evidence
  topic: 'Native checklist: all references and source notes'
  outcome: concern
  target_ids:
  - traitmech:000044
  summary: All eight reference identities resolve. Inspected full texts support the
    assigned signalling, oxygen, nutrient and ATP contexts. The diffusion-barrier
    note drops a source qualification; the sole exact snippet remains inconclusive.
  evidence_ids:
  - bibliography
  - poole
  - oldroyd
  - example
  - signals
  - nodule
  - atp
  - iron
  - nifh-paper
- assessment_id: graph
  area: graph
  topic: 'Native checklist: all eleven nodes and ten edges'
  outcome: concern
  target_ids:
  - traitmech:000044
  summary: The graph is connected and the anchored component is correctly scoped.
    Three enables edges confuse disposition, prerequisite or input roles with material
    execution. The chemical signal edge is type-compatible and is not counted as a
    definite ontology error.
  evidence_ids:
  - record
  - shape
  - relations
  - provisional
  - go
  - chebi
  - signals
  - nodule
  - atp
  - iron
  - nifh-paper
  - policy
  details: 'Zero-based ledger: node0 is the local trait; nodes1/2 are signalling/fixation
    processes, with node2 correctly grounded. Nodes3/4 are chemical signals; node5
    is an explicitly contextual host-protein family. Node6 describes a cellular anatomical
    barrier; node7 is a low-oxygen condition. Node8 is the correctly grounded complex,
    with NifH explicitly just one component. Node9 is a broad chemical input and node10
    iron availability. Edge0 fits provisional process-to-trait confers within the
    graph context, without establishing that signalling alone suffices for functional
    fixation. Edge1 has a disposition subject under material-executor enables. Edge2
    has a supported ungrounded induction phrase. Edge3 is material-to-process compatible;
    its signal/trigger-versus-executor interpretation is a bounded precision question.
    Edge4 has supported buffering context. Edge5 has qualified source support and
    a stronger record formulation. Edge6 describes a prerequisite rather than an executor.
    Edge7 has compatible complex-to-process execution and the ATP number matches.
    Edge8 describes carbon input rather than execution. Edge9 has supported cofactor
    context and no external predicate assertion. Ungrounded local predicates are schema-permitted;
    graph connectivity is not proof of a complete molecular model.'
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: structured transcriptomic cross-check'
  outcome: not_applicable
  target_ids:
  - traitmech:000044
  summary: The official catalog supplies no matching species/strain dataset. Neither
    a different rhizobial genus nor similarity-based UniProt annotations establish
    direct strain-specific transcriptomic or experimental support.
  evidence_ids:
  - expression
  - runner
  - uniprot-current
- assessment_id: optional
  area: completeness
  topic: 'Native checklist: discussion and dataset slots'
  outcome: supported
  target_ids:
  - traitmech:000044
  summary: No discussion placeholder or asserted dataset accession requires resolution.
    Optional additions are not invented to make the review look more complete.
  evidence_ids:
  - record
  - policy
- assessment_id: status
  area: provenance
  topic: 'Native checklist: REVIEWED, history and provider provenance'
  outcome: concern
  target_ids:
  - traitmech:000044
  summary: Eight AI-assisted events and a historical provider report document work,
    but no human-acceptance link was found in inspected target-specific materials.
    Provider output is provenance, not primary evidence or human scientific approval.
  evidence_ids:
  - record
  - search
  - policy
  - check-validate-history
findings:
- finding_id: enables-endpoint-roles
  issue_key: nitrogen-fixing-symbiosis-enables-endpoint-roles
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Three enables edges do not express the required executor role
  description: 'Edge1 supplies a trait/disposition where RO:0002327 inherits a material-executor
    subject. Edge6 supplies a low-oxygen prerequisite condition. Edge8 supplies chemical
    fuel/reductant: its material type is compatible, but the described input role
    does not itself execute fixation. These are distinct domain/role problems under
    one relation; no formal material-domain error is asserted for the chemical. Edge3
    is deliberately excluded from the definite error count.'
  target_ids:
  - traitmech:000044
  field_paths:
  - causal_graphs[0].edges[1].predicate_id
  - causal_graphs[0].edges[6].predicate_id
  - causal_graphs[0].edges[8].predicate_id
  evidence_ids:
  - record
  - relations
  - signals
  - nodule
  - shape
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping; future changes require separately scoped review
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: barrier-source-qualification
  issue_key: nitrogen-fixing-symbiosis-barrier-source-qualification
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The diffusion-barrier note loses the cited source qualification
  description: The inspected author PDF describes the barrier’s oxygen-limiting role
    with thought to, whereas the edge and note state it categorically. The additional
    multilayered-cortex/adaptable characterization was not located in the searchable
    cited PDF. Preserve the source’s certainty or provide a precise supporting source;
    this is bounded source precision, not a finding that the physiological barrier
    is false.
  target_ids:
  - traitmech:000044
  field_paths:
  - causal_graphs[0].nodes[6].description
  - causal_graphs[0].edges[5].description
  - causal_graphs[0].edges[5].evidence
  evidence_ids:
  - record
  - nodule
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: reviewed-signoff-not-documented
  issue_key: nitrogen-fixing-symbiosis-reviewed-signoff-not-documented
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The inspected REVIEWED provenance lacks a human-acceptance link
  description: All eight target events disclose AI assistance but do not identify
    human scientific acceptance. The native checklist requires it for REVIEWED. The
    finding is bounded to inspected local target-specific provenance and does not
    establish absence of private or remote approval.
  target_ids:
  - traitmech:000044
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - record
  - search
  - policy
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-relation-roles
  description: Reconcile the existing endpoint concepts with relation meanings during
    separately authorized curation.
  finding_ids:
  - enables-endpoint-roles
  target_ids:
  - traitmech:000044
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate mapping; future changes require separately scoped review
  acceptance_checks:
  - Distinguish the trait/disposition, permissive condition, supplied input and executing
    complex; do not retype entities merely to fit an identifier.
  - Inspect inherited external definitions and retain provisional status for local
    proposals.
  - Review any shared mapping change separately; use guarded writes, new history and
    applicable validation/qc gates.
- action_id: preserve-source-qualification
  description: Align the barrier wording with the source strength and precise locator.
  finding_ids:
  - barrier-source-qualification
  target_ids:
  - traitmech:000044
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain the source qualification unless another inspected source supports stronger
    wording.
  - Document the source and locator for any added anatomical/adaptability characterization.
  - Do not infer that a failed word search disproves a physiological mechanism.
- action_id: document-status-basis
  description: Locate and document the human-acceptance basis or retain the question
    as unresolved.
  finding_ids:
  - reviewed-signoff-not-documented
  target_ids:
  - traitmech:000044
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - AI assistance, validated schema and publication do not identify a human approver.
  - Any change to scientific status requires separate authorization and a new history
    event.
limitations:
- The exact nifH1491::Tn5 snippet and strain1021-specific experiment in DOI10.1094/MPMI-06-25-0074-R
  remain unverified after ordinary public full-text access failed. The abstract check
  is inconclusive, and similarity-based UniProt comments do not replace experimental
  evidence.
- Poole and Oldroyd were inspected through publisher previews and abstracts, not complete
  subscription articles. Public full text was inspected for the other five sources.
- The most-studied ranking in canonical example0 is not independently established.
  The model/reference-strain identity is supported.
- Edge3’s signal-versus-executor interpretation remains a bounded question; material-subject
  typing alone does not establish an error.
- The bounded local runner search found no usable structured adapter; the official
  dataset API fallback was inspected. No matching strain dataset exists in that retrieved
  catalog, which is not negative biological evidence.
- Historical UniSave supports version158/sequence2 availability. It cannot independently
  establish that a curator made the claimed retrieval on August25; current159 is a
  later update.
- CHEBI and RO authority checks use the captured/downloaded releases. The local METPO
  confers identifier remains a proposal.
- Earlier full-corpus diagnostics retain actual timestamps, baselines, superseded
  network failures and product-adapter skips at the unchanged source base.
- No scientific record, mapping, proposal, history or native status is changed. No
  human scientific sign-off is supplied.
notes:
- Initial native inspection captured32inputs; the expanded33-input capture added the
  inspected provider provenance header and verified all original hashes unchanged.
- Independent source/ontology checks informed this manually authored complete-record
  review. No experimental procedure or microbial engineering recommendation is proposed.
tags:
- record-review
- nitrogen-fixing-symbiosis
- ecology
- needs-curation
```
