# Scientific and source review of endosymbiosis (traitmech:000045)

- Review: 20261020T070034Z-endosymbiosis
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-20T04:10:06Z
- Finished UTC: 2026-10-20T07:00:34Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The fallback identifier, broader symbiosis parent and Buchnera example are supported. All ten nodes and seven edges were assessed. Two major findings concern the process subject of RO contributes to and the discussion’s unsupported binary causal interpretation. Two minor findings concern intracellular versus tissue-level wording and an inaccurate historical-source disclaimer. The graph’s explicit obligate/long-term qualifications and NONMECHANISTIC status are preserved; disconnected context alone is not treated as an error.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Second record in batch002, following endophytic in the validated cross-branch coverage union. Exactly one entire maintained TraitRecord.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f25e2af0b38a8303b13f627a9a5c33b36af4b3d2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000045 | data/traits/ecology/endosymbiosis.yaml | maintained | endosymbiosis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000045 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000045 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000045 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | traitmech:000045 | 1276 history records checked, zero invalid links; integrity does not establish scientific correctness or human sign-off. |
| Initial full-product validation | failed | False | traitmech:000045 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000045 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000045 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | traitmech:000045 | The selected record validates. |
| Focused strict validation | passed | True | traitmech:000045 | One file scanned; zero error rows. |
| Focused source snippet verification | passed | True | traitmech:000045 | Zero snippets and zero references were selected. Exit zero does not verify the record’s active citations or historical quotations; manual inspections are recorded separately. |
| Expression-module applicability | not_applicable | False | traitmech:000045 | The record asserts no exact gene, protein, strain or expression dataset key. Generic evolutionary processes and a species example do not establish an applicable iModulon component. The shared runner was not found on PATH; no negative biological inference is made. |

## Scientific And Domain Assessments

### Native checklist: identifier, label, synonym and term kind

identity: supported. Targets: traitmech:000045.

The exact historical METPO term is obsolete, and the local identifier has a documented pending class proposal. The target is an ecological trait rather than a taxon or organelle record.

### Native checklist: definition and narrower source scope

evidence: concern. Targets: traitmech:000045.

The intracellular concept and qualified reduced-genome observation have source support. The definition also allows tissue-level residence, while the graph labels that broader location intracellular. This wording distinction needs clarification; a universal genome-reduction claim is not attributed to the already qualified description.

### Native checklist: broader parent and proposed vocabulary

consistency: supported. Targets: traitmech:000045.

Symbiosis is broader. The v5/v7/v8 proposal vocabulary is identifiable and must remain distinguished from active upstream terms; the documented v7 hierarchy caveat is not silently resolved by this review.

### Native checklist: ecology category and nonmechanistic scope

representation: supported. Targets: traitmech:000045.

A broad ecological class can carry contextual examples of evolutionary consequences. Three components are documented but do not automatically fail NONMECHANISTIC scope. No forced universal molecular pathway or arbitrary protein instance is required.

### Native checklist: Buchnera example, identity and nearest evidence

scope: supported. Targets: traitmech:000045.

The example’s taxon, nutritional role, intracellular location and maternal transmission are directly supported by the cited profile. It is an illustrative obligate association, not evidence that every endosymbiotic lifestyle behaves identically.

### Native checklist: bibliography, narrow support and quotations

evidence: concern. Targets: traitmech:000045.

The source identities are sound and the contextual Song/Bai/Silva claims are traceable. No active snippets were tested by the native checker. Poole remains limited to its publisher preview; historical quotations were separately checked and their blanket irrelevance disclaimer is inaccurate.

### Native checklist: ten nodes and seven-edge ledger

graph: concern. Targets: traitmech:000045.

The contextual statements have identifiable support, but edge3 misuses RO contributes to. Node wording conflates cell-level and tissue-level localization. Detached context is correctly noticed by the discussion without establishing which causal links should be added.

Zero-based edge ledger: 0 localization/confers/trait is a conceptual bridge illustrated by rhizobia; detailed nearest-source cell-localization text remains an access limitation. 1 trait/causes/reductive evolution is explicitly qualified to long-term obligate intracellular life and small effective population size; the cited review supports that context, not inevitability for the entire class. 2 confined habitat/drives/metabolic loss is a contextual review-level explanation, not an independently isolated habitat effect. 3 metabolic loss/contributes to/reductive evolution has plausible ordinary-language meaning but incompatible RO subject semantics. 4 bottleneck/associated with/limited recombination is consistent with the cited small-founder/asexual context and retains an associative predicate. 5 pathway complementarity/supports/nutritional compensation is supported in the particular mealybug association; it does not prove universal loss of host-complemented functions. 6 genome reduction/leads to/dependence matches the named cockroach-symbiont introduction. All node IDs and discussion anchors resolve.

### Native checklist: scientific question, inference and retained scan history

scope: concern. Targets: traitmech:000045.

The discussion correctly identifies two detached pairs. Its opposing-loss-spectrum claim and causal support/refutation interpretations are stronger than the cited evidence, and one compensation claim reverses the nutritional direction in the graph. Historical sources are retained honestly as quotations but mischaracterized as uniformly off-topic.

### Native checklist: mapping status, history and checks

provenance: unknown. Targets: traitmech:000045.

Focused schema checks pass. The record and repository history disclose AI-assisted creation, promotion and subsequent changes; independent human sign-off for REVIEWED remains unestablished. No promotion or history mutation is performed here.

## Findings

### contributes-to-subject-type: RO contributes to is applied to a process subject

major / open / confirmed; issue key: endosymbiosis-contributes-to-subject-type.

The metabolic_gene_loss node is a biological process, while RO:0002326 inherits a material-entity subject constraint. A process can contribute to another process in ordinary language without satisfying this specific relation. Successful closed-schema or mapping checks do not establish semantic compatibility.

### discussion-causal-overclaim: The discussion treats interacting explanations as a decisive binary

major / open / confirmed; issue key: endosymbiosis-discussion-causal-overclaim.

The rationale says drift and compensation predict opposite loss spectra and assigns exact losses to host supply. The reviewed sources preserve functional constraints and interacting causes; the graph’s nutritional_compensation node concerns host nutritional needs, not a proof that the host supplies all lost symbiont functions. The proposed comparative association also cannot uniquely establish the stated causal dominance or dismiss the other explanation.

### cell-tissue-scope: Intracellular wording includes the broader tissue-level location

minor / open / confirmed; issue key: endosymbiosis-cell-tissue-scope.

The localization node is labelled intracellular but describes residence inside cells or tissues. A tissue can contain both intracellular and extracellular locations. The broad trait definition and narrower genome-reduction graph can coexist, but those two meanings should not be treated as interchangeable.

### historical-source-description: Historical references are not uniformly unrelated to endosymbiosis

minor / open / confirmed; issue key: endosymbiosis-historical-source-description.

The note says the three additional references concern neither the original sentence nor this trait. Their inspected abstracts include a bacterial endosymbiosis study, endosymbiotic plastid origins, and an explicit unresolved endosymbiont question. They need not support this particular genome-reduction discussion, but that is a narrower and more accurate disclaimer.

## Recommended Actions And Acceptance Checks

### reassess-process-relation

Reconcile the intended process relationship with a source-supported, endpoint-compatible representation.

- Inspect the exact relation definition and inherited constraints, not just its English label.
- Do not change a process into a material entity solely to satisfy the existing identifier.
- After authorized curation run focused validate/strict, applicable graph and grounding checks, guarded history requirements and qc.

### bound-causal-interpretation

Preserve a useful comparative question while qualifying its causal conclusions and nutritional direction.

- Distinguish an observed association from a unique causal explanation and allow interacting processes.
- Describe the same host-versus-symbiont nutritional relation in the graph and discussion.
- Do not invent missing mechanisms or redesign a biological intervention; the correction is interpretation and source scope.
- Reconcile the maintained discussion writer and use focused strict/source checks plus applicable qc after authorized edits.

### clarify-localization-scope

Keep the broader trait boundary and the selected intracellular graph context explicit and internally consistent.

- Retain a source-backed distinction between residence within host tissue and residence within a host cell.
- Do not broaden the reduced-genome consequence to all tissue-associated symbioses.
- Run focused strict and source checks after authorized wording changes.

### correct-source-disclaimer

Describe the historical references’ relevance precisely while preserving their non-evidentiary status for the current question.

- Retain the original identifiers and exact historical fragments.
- Distinguish being related to the broad trait from supporting this specific question.
- Reconcile the maintained provenance text and run focused strict validation after authorized edits.

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
| check-endosymbiosis-validate | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endosymbiosis-validate.log; Executed 2026-10-20T04:10:36Z through 2026-10-20T04:10:37Z; metadata endosymbiosis-validate.json | context_only | The selected record validates. |
| check-endosymbiosis-strict | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endosymbiosis-strict.log; Executed 2026-10-20T04:10:36Z through 2026-10-20T04:10:37Z; metadata endosymbiosis-strict.json | context_only | One file scanned; zero error rows. |
| check-endosymbiosis-snippets-network | /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endosymbiosis-snippets-network.log; Executed 2026-10-20T06:52:47Z through 2026-10-20T06:52:47Z; metadata endosymbiosis-snippets-network.json | context_only | Zero snippets and zero references were selected. Exit zero does not verify the record’s active citations or historical quotations; manual inspections are recorded separately. |
| record | data/traits/ecology/endosymbiosis.yaml; Entire record, including ten nodes, seven edges, example, discussion and all history | partial | The definition is broader than the intracellular graph. The genome-reduction edge explicitly qualifies the claim to long-term obligate intracellular associations with small effective population size; this review does not misread it as an unqualified universal rule. |
| identity | data/raw/metpo.owl; Complete-ontology normalized exact endosymbiosis/endosymbiotic search, including obsolete-label forms | supports | The exact historical term METPO:1000105 is obsolete and has no replacement in the inspected statements. The local fallback is defensible; the obsolete identifier should not be substituted. |
| structure | data/traits/ecology/endosymbiosis.yaml; All endpoints, discussion anchors, undirected components and selected ontology subjects | supports | Ten nodes and seven edges form three components. The two detached pairs described in the discussion are present, and every endpoint and anchor resolves. Proposed METPO:1007644, METPO:1007721 and METPO:2007700 are absent as subjects from the captured ontology. |
| model | proposals/metpo_traitmech_v7/metpo_proposal_classes_robot.tsv; METPO:1007721 row and proposal hierarchy caveat; node mapping; v5 endosymbiosis/parent row; v8 confers row; native schema and grounding guidance | partial | The process grounding and confers predicate are documented local proposals, not released upstream terms. The v7 proposal explicitly flags its generic phenotype parent for upstream review. NONMECHANISTIC context permits a scoped conceptual graph and does not require inventing links between every contextual pair. |
| hierarchy | data/traits/ecology/symbiosis.yaml; Parent definition and identity | supports | The parent covers persistent host/partner association, including several host-effect relationships. Internal association is narrower; related endosymbiont terminology does not assert organism-class identity. |
| owners | scripts/curate_knowledge_gaps.py; PLAN kgscan-a6758e26f5a6 and retained scan provenance; captured record/repository histories and mapping tables | context_only | The maintained discussion writer reproduces the disputed inference and historical-source language. AI-assisted history records promotion and graph changes. Those events establish provenance, not independent human scientific sign-off. |
| bibliography | https://www.ebi.ac.uk/europepmc/webservices/rest/search; Exact lookup for all six active article DOIs, including the DOI embedded in the example URL | supports | All six references resolve to the intended articles. McCutcheon/Moran, Poole, Song and the Buchnera profile are contextual syntheses; Bai and Silva report particular host–symbiont studies. These evidence types are not interchangeable. |
| mccutcheon | https://doi.org/10.1038/nrmicro2670; Extreme genome reduction in symbiotic bacteria; publisher abstract/key points/glossary and browser-returned primary PDF, printed pp13,16 Box1 and17 glossary | partial | The reviewed passages support reduced genomes in particular obligate host-associated lineages and explain reduced efficacy of purifying selection. They retain functional constraints and do not imply that all functions are equally dispensable. The glossary defines endosymbionts intracellularly. |
| mccutcheon-access | https://fire.biol.wwu.edu/cmoyer/zztemp_fire/biol345_F12/papers/Moran_extreme_genome_reduction_nrmicro12.pdf; Browser-returned14-page PDF versus direct-download attempt | context_only | The browser supplied a cached primary PDF for passage inspection, while the direct download returned404. No raw-file snapshot hash or successful direct download is claimed. |
| poole | https://doi.org/10.1038/nrmicro.2017.171; Rhizobia: from saprophytes to endosymbionts; publisher abstract/key points and bibliographic record | partial | The inspected material supports rhizobial endosymbiotic lifestyles and describes large, flexible genomes. It reinforces the distinction between the broad lifestyle and the obligate-reduced-genome subset. Full accepted-manuscript retrieval failed, so detailed cell-localization passages were not independently verified. |
| song | https://doi.org/10.1093/ismejo/wrae117; Cellular interactions and evolutionary origins of endosymbiotic relationships with ciliates; abstract and paragraphs on confined habitats, gene reduction, small ancestral populations and recombination | supports | The review supports the contextual assertions behind edges2–4, including the approximate size comparison and limited-recombination association. It also explicitly discusses genetic drift and complex interacting causes. Its statements do not justify an exclusive spatial-confinement mechanism. |
| bai | https://doi.org/10.1093/ismejo/wrae052; Study of Tremblaya phenacola and its mealybug host; abstract and discussion of host–symbiont amino-acid complementarity | supports | The source supports nutritional complementarity in that host–symbiont system. The graph describes compensation of host nutritional needs. This is not equivalent to demonstrating that the host supplies every product corresponding to a lost symbiont gene. |
| silva | https://doi.org/10.3390/ijms25084228; Comparative Transcriptomics of Fat Bodies between Symbiotic and Quasi-Aposymbiotic Adult Females of Blattella germanica; introduction on Blattabacterium association | supports | The introduction explicitly links severe genome reduction with dependence in the named cockroach–bacterial association. This supports the contextual edge; it is not a universal result for every endosymbiont. |
| buchnera | https://doi.org/10.1099/mic.0.001127; Microbe Profile: Buchnera aphidicola: ancient aphid accomplice and endosymbiont exemplar; abstract and biology/ecology discussion, PMC10228527 HTML | supports | The source directly supports the example’s obligate aphid association, nutritional role, residence in bacteriocytes and maternal transmission. It describes variation among host-associated strains without invalidating the species-level illustrative example. |
| taxon | https://rest.uniprot.org/taxonomy/9; Taxonomy identifier9 and scientific name | supports | Identifier9 resolves to Buchnera aphidicola. Taxonomy and phenotype evidence were assessed separately. |
| ro | http://purl.obolibrary.org/obo/ro.owl; RO:0002326 and recursively inspected superproperties, including RO:0002216, RO:0002500 and RO:0002595 | refutes | The contributes-to relation inherits material-entity-to-process semantics. The record’s metabolic_gene_loss subject is explicitly a biological process. This is a manual ontology-semantic finding; native mapping wildcards do not remove the inherited constraint. |
| historical | https://www.ebi.ac.uk/europepmc/webservices/rest/search; PMIDs42130304,41612704,40831140 and41764142; titles, abstracts and exact retained-fragment checks | partial | All identifiers resolve and all retained fragments match. The weevil–bacterial study directly concerns endosymbiosis; the plastid review concerns endosymbiotic origins; the insect-microbiome paper explicitly leaves endosymbiont identity unresolved. Their failure to support the current reduction question does not make them unrelated to the trait. |

## Limits And Additional Notes

- Poole full text was not retrieved; the review inspected its publisher abstract/key points and bibliographic record. No full-paper absence claim is made.
- McCutcheon/Moran was inspected through publisher material and browser-returned cached PDF passages; a direct PDF download returned404 and no local raw PDF hash is claimed.
- The Song review and Bai/Silva studies support contextual claims at different taxonomic and evidentiary scopes. These are not treated as a universal model for all endosymbioses.
- The full-corpus graph connectivity report is not a focused mechanistic assessment of this NONMECHANISTIC graph. Its three components are separately documented.
- Ontology semantics were inspected manually. The review does not claim an OWL reasoning run or upstream adoption of proposed METPO terms.
- The source snapshot supports the local fallback and pending-proposal distinction; it does not establish absence from all newer ontology releases.
- Human sign-off remains unresolved. Earlier corpus checks retain their actual same-base timestamps, baseline findings, adapter skips and superseded failures.
- No experimental redesign, pest-control intervention, pathogenic mechanism improvement or biological engineering is proposed.
- Ignored-and-hidden-inclusive searches covered data/traits, scripts, history, mappings, proposals, conf and DO_NOT_WORK.md for endosymbiosis, endosymbiont, traitmech:000045 and METPO:1007721. Exact ontology searches separately inspected the complete captured OWL.
- Only the new immutable review is saved. The scientific target, mappings, discussion writer, history and generated artifacts remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T070034Z-endosymbiosis
kind: record
repository: CultureBotAI/TraitMech
title: Scientific and source review of endosymbiosis (traitmech:000045)
started_at: '2026-10-20T04:10:06Z'
finished_at: '2026-10-20T07:00:34Z'
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
summary: The fallback identifier, broader symbiosis parent and Buchnera example are
  supported. All ten nodes and seven edges were assessed. Two major findings concern
  the process subject of RO contributes to and the discussion’s unsupported binary
  causal interpretation. Two minor findings concern intracellular versus tissue-level
  wording and an inaccurate historical-source disclaimer. The graph’s explicit obligate/long-term
  qualifications and NONMECHANISTIC status are preserved; disconnected context alone
  is not treated as an error.
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
  - path: data/traits/ecology/endosymbiosis.yaml
    sha256: e42e413a5d2a662aabbd7add9be674718bfc392a1bcc16f1d55fdb8d3c37cb91
    role: target
  - path: data/traits/ecology/symbiosis.yaml
    sha256: 86ad9516ff0879731da3792de1495ba1d0e107394edfcc754be03d052a677b21
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
  - path: history/infrastructure/curate-knowledge-gaps/2026-08-17T214933Z-claude-code-9c4af0.yaml
    sha256: a58b53be777e58ac29eb1c1571feb2593633c83d158aff4b6c96b8a1b9214c0f
    role: context
  - path: history/infrastructure/protein-taxon-event-backfill/2026-08-26T032525Z-claude-936bf3.yaml
    sha256: e32f537bb5192c12e9dae5f37ca07f71221402373551506429ce30445137fbab
    role: context
  - path: history/other/protein-taxon-review-tranche/2026-08-26T032524Z-codex-f46ce8.yaml
    sha256: dbd304ce7c2dfaf1525a12c1d5b4bf04a1ec66f00b92e4917d642c5fba6370fd
    role: context
  - path: mappings/node_grounding.tsv
    sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
    role: context
  - path: mappings/predicate_grounding.tsv
    sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
    role: context
  - path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
    role: context
  - path: proposals/metpo_traitmech_v7/metpo_proposal_classes_robot.tsv
    sha256: 99e779afa894363b32966bd15415417035d246970aab02931ce896f37c910a73
    role: context
  - path: proposals/metpo_traitmech_v7/proposal.md
    sha256: bc6ea10ebc4bec0f446cee92578602889ec464295ce5ecce27fed76eb06528ce
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
- target_id: traitmech:000045
  path: data/traits/ecology/endosymbiosis.yaml
  label: endosymbiosis
  record_class: TraitRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endosymbiosis.yaml
    role: Maintained scientific record; future changes require guarded curation and
      history
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Second record in batch002, following endophytic in the validated cross-branch
    coverage union. Exactly one entire maintained TraitRecord.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000045
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000045
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
  - traitmech:000045
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
  - traitmech:000045
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
  - traitmech:000045
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
  - traitmech:000045
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
  - traitmech:000045
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
  - traitmech:000045
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: Actual earlier command at the same unchanged source base; only new structured
    review files have been added. Original timestamps and failed attempts are retained.
- check_id: endosymbiosis-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - traitmech:000045
  command: just validate data/traits/ecology/endosymbiosis.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The selected record validates.
  evidence_ids:
  - check-endosymbiosis-validate
- check_id: endosymbiosis-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000045
  command: just validate-strict data/traits/ecology/endosymbiosis.yaml --out /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endosymbiosis-strict.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero error rows.
  evidence_ids:
  - check-endosymbiosis-strict
- check_id: endosymbiosis-snippets-network
  name: Focused source snippet verification
  status: passed
  required: true
  target_ids:
  - traitmech:000045
  command: just verify-snippets --record data/traits/ecology/endosymbiosis.yaml --out
    /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endosymbiosis-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Zero snippets and zero references were selected. Exit zero does not verify
    the record’s active citations or historical quotations; manual inspections are
    recorded separately.
  evidence_ids:
  - check-endosymbiosis-snippets-network
- check_id: expression-applicability
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000045
  summary: The record asserts no exact gene, protein, strain or expression dataset
    key. Generic evolutionary processes and a species example do not establish an
    applicable iModulon component. The shared runner was not found on PATH; no negative
    biological inference is made.
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-20T07:00:34Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-20T07:00:34Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-20T07:00:34Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-history.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:24Z; metadata validate-history.json
  accessed_at: '2026-10-20T07:00:34Z'
  support: context_only
  summary: 1276 history records checked, zero invalid links; integrity does not establish
    scientific correctness or human sign-off.
  snapshot_sha256: 1fc48f1203fbfcd27b1243e4e147afb367aebfc592b496b352201058c6ee85d2
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-20T07:00:34Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-20T07:00:34Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-20T07:00:34Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-endosymbiosis-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endosymbiosis-validate.log
  locator: Executed 2026-10-20T04:10:36Z through 2026-10-20T04:10:37Z; metadata endosymbiosis-validate.json
  accessed_at: '2026-10-20T07:00:34Z'
  support: context_only
  summary: The selected record validates.
  snapshot_sha256: 5ce21fc7c05a2c88366222d79e9ee6a45d293900312805f102345080d5088fb2
- evidence_id: check-endosymbiosis-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endosymbiosis-strict.log
  locator: Executed 2026-10-20T04:10:36Z through 2026-10-20T04:10:37Z; metadata endosymbiosis-strict.json
  accessed_at: '2026-10-20T07:00:34Z'
  support: context_only
  summary: One file scanned; zero error rows.
  snapshot_sha256: 6f100bf2413eca11c20ba588fc68352608ad19f748ec3b6a530e867042564527
- evidence_id: check-endosymbiosis-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-002.mdt7dqwk/endosymbiosis-snippets-network.log
  locator: Executed 2026-10-20T06:52:47Z through 2026-10-20T06:52:47Z; metadata endosymbiosis-snippets-network.json
  accessed_at: '2026-10-20T07:00:34Z'
  support: context_only
  summary: Zero snippets and zero references were selected. Exit zero does not verify
    the record’s active citations or historical quotations; manual inspections are
    recorded separately.
  snapshot_sha256: 3ba911e89bdb519f3f808104249757e69ea87df1948c11855e61a3ae695b990f
- evidence_id: record
  kind: record_content
  reference: data/traits/ecology/endosymbiosis.yaml
  locator: Entire record, including ten nodes, seven edges, example, discussion and
    all history
  accessed_at: '2026-10-20T07:00:34Z'
  support: partial
  summary: The definition is broader than the intracellular graph. The genome-reduction
    edge explicitly qualifies the claim to long-term obligate intracellular associations
    with small effective population size; this review does not misread it as an unqualified
    universal rule.
  snapshot_sha256: e42e413a5d2a662aabbd7add9be674718bfc392a1bcc16f1d55fdb8d3c37cb91
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl
  locator: Complete-ontology normalized exact endosymbiosis/endosymbiotic search,
    including obsolete-label forms
  accessed_at: '2026-10-20T04:10:36Z'
  support: supports
  summary: The exact historical term METPO:1000105 is obsolete and has no replacement
    in the inspected statements. The local fallback is defensible; the obsolete identifier
    should not be substituted.
  snapshot_sha256: 2309de056a00e5a9b6cccca2794787c411256ecefa5a29eca50a9008c8cc51f0
- evidence_id: structure
  kind: record_content
  reference: data/traits/ecology/endosymbiosis.yaml
  locator: All endpoints, discussion anchors, undirected components and selected ontology
    subjects
  accessed_at: '2026-10-20T06:57:24Z'
  support: supports
  summary: Ten nodes and seven edges form three components. The two detached pairs
    described in the discussion are present, and every endpoint and anchor resolves.
    Proposed METPO:1007644, METPO:1007721 and METPO:2007700 are absent as subjects
    from the captured ontology.
  snapshot_sha256: 52c0c68059885bd0817febe0fac62f0e26477ee63d9ab662ecbc6ce79c89bf4b
- evidence_id: model
  kind: authority
  reference: proposals/metpo_traitmech_v7/metpo_proposal_classes_robot.tsv
  locator: METPO:1007721 row and proposal hierarchy caveat; node mapping; v5 endosymbiosis/parent
    row; v8 confers row; native schema and grounding guidance
  accessed_at: '2026-10-20T07:00:34Z'
  support: partial
  summary: The process grounding and confers predicate are documented local proposals,
    not released upstream terms. The v7 proposal explicitly flags its generic phenotype
    parent for upstream review. NONMECHANISTIC context permits a scoped conceptual
    graph and does not require inventing links between every contextual pair.
- evidence_id: hierarchy
  kind: record_content
  reference: data/traits/ecology/symbiosis.yaml
  locator: Parent definition and identity
  accessed_at: '2026-10-20T07:00:34Z'
  support: supports
  summary: The parent covers persistent host/partner association, including several
    host-effect relationships. Internal association is narrower; related endosymbiont
    terminology does not assert organism-class identity.
- evidence_id: owners
  kind: record_content
  reference: scripts/curate_knowledge_gaps.py
  locator: PLAN kgscan-a6758e26f5a6 and retained scan provenance; captured record/repository
    histories and mapping tables
  accessed_at: '2026-10-20T07:00:34Z'
  support: context_only
  summary: The maintained discussion writer reproduces the disputed inference and
    historical-source language. AI-assisted history records promotion and graph changes.
    Those events establish provenance, not independent human scientific sign-off.
- evidence_id: bibliography
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search
  locator: Exact lookup for all six active article DOIs, including the DOI embedded
    in the example URL
  accessed_at: '2026-10-20T06:53:22Z'
  support: supports
  summary: All six references resolve to the intended articles. McCutcheon/Moran,
    Poole, Song and the Buchnera profile are contextual syntheses; Bai and Silva report
    particular host–symbiont studies. These evidence types are not interchangeable.
  snapshot_sha256: 149be1ffbb47f6c8fcfc4603be8fb94c648daff24c4bdf03bddeba558fb11b94
- evidence_id: mccutcheon
  kind: primary_source
  reference: https://doi.org/10.1038/nrmicro2670
  locator: Extreme genome reduction in symbiotic bacteria; publisher abstract/key
    points/glossary and browser-returned primary PDF, printed pp13,16 Box1 and17 glossary
  accessed_at: '2026-10-20T07:00:06Z'
  support: partial
  summary: The reviewed passages support reduced genomes in particular obligate host-associated
    lineages and explain reduced efficacy of purifying selection. They retain functional
    constraints and do not imply that all functions are equally dispensable. The glossary
    defines endosymbionts intracellularly.
- evidence_id: mccutcheon-access
  kind: authority
  reference: https://fire.biol.wwu.edu/cmoyer/zztemp_fire/biol345_F12/papers/Moran_extreme_genome_reduction_nrmicro12.pdf
  locator: Browser-returned14-page PDF versus direct-download attempt
  accessed_at: '2026-10-20T06:55:30Z'
  support: context_only
  summary: The browser supplied a cached primary PDF for passage inspection, while
    the direct download returned404. No raw-file snapshot hash or successful direct
    download is claimed.
  snapshot_sha256: 80a123036a9dffaeb0aa043dfb808a71796cfa1a2ccc815ffcf28bd0019cea82
- evidence_id: poole
  kind: primary_source
  reference: https://doi.org/10.1038/nrmicro.2017.171
  locator: 'Rhizobia: from saprophytes to endosymbionts; publisher abstract/key points
    and bibliographic record'
  accessed_at: '2026-10-20T06:53:22Z'
  support: partial
  summary: The inspected material supports rhizobial endosymbiotic lifestyles and
    describes large, flexible genomes. It reinforces the distinction between the broad
    lifestyle and the obligate-reduced-genome subset. Full accepted-manuscript retrieval
    failed, so detailed cell-localization passages were not independently verified.
  snapshot_sha256: 149be1ffbb47f6c8fcfc4603be8fb94c648daff24c4bdf03bddeba558fb11b94
- evidence_id: song
  kind: primary_source
  reference: https://doi.org/10.1093/ismejo/wrae117
  locator: Cellular interactions and evolutionary origins of endosymbiotic relationships
    with ciliates; abstract and paragraphs on confined habitats, gene reduction, small
    ancestral populations and recombination
  accessed_at: '2026-10-20T06:53:29Z'
  support: supports
  summary: The review supports the contextual assertions behind edges2–4, including
    the approximate size comparison and limited-recombination association. It also
    explicitly discusses genetic drift and complex interacting causes. Its statements
    do not justify an exclusive spatial-confinement mechanism.
  snapshot_sha256: 254a9114c76e8d633b8a73bdedfe855d7c7b29f070367babb30b0feb9a82436f
- evidence_id: bai
  kind: primary_source
  reference: https://doi.org/10.1093/ismejo/wrae052
  locator: Study of Tremblaya phenacola and its mealybug host; abstract and discussion
    of host–symbiont amino-acid complementarity
  accessed_at: '2026-10-20T06:53:29Z'
  support: supports
  summary: The source supports nutritional complementarity in that host–symbiont system.
    The graph describes compensation of host nutritional needs. This is not equivalent
    to demonstrating that the host supplies every product corresponding to a lost
    symbiont gene.
  snapshot_sha256: 5a3cd5a2ecca0530466dd86053bc7f0810676fa3d38f8c5905b3ad63380c7647
- evidence_id: silva
  kind: primary_source
  reference: https://doi.org/10.3390/ijms25084228
  locator: Comparative Transcriptomics of Fat Bodies between Symbiotic and Quasi-Aposymbiotic
    Adult Females of Blattella germanica; introduction on Blattabacterium association
  accessed_at: '2026-10-20T06:53:29Z'
  support: supports
  summary: The introduction explicitly links severe genome reduction with dependence
    in the named cockroach–bacterial association. This supports the contextual edge;
    it is not a universal result for every endosymbiont.
  snapshot_sha256: 3e5aefa7a8cd08459827145d582c57e9cd8d9b7b00a77290b820f7026a4d211c
- evidence_id: buchnera
  kind: primary_source
  reference: https://doi.org/10.1099/mic.0.001127
  locator: 'Microbe Profile: Buchnera aphidicola: ancient aphid accomplice and endosymbiont
    exemplar; abstract and biology/ecology discussion, PMC10228527 HTML'
  accessed_at: '2026-10-20T06:55:30Z'
  support: supports
  summary: The source directly supports the example’s obligate aphid association,
    nutritional role, residence in bacteriocytes and maternal transmission. It describes
    variation among host-associated strains without invalidating the species-level
    illustrative example.
  snapshot_sha256: 7be319e73fe5cd80bcaed11f6feefdbc85c014d3dc14d1d5eec2afddd52d716c
- evidence_id: taxon
  kind: database
  reference: https://rest.uniprot.org/taxonomy/9
  locator: Taxonomy identifier9 and scientific name
  accessed_at: '2026-10-20T06:53:31Z'
  support: supports
  summary: Identifier9 resolves to Buchnera aphidicola. Taxonomy and phenotype evidence
    were assessed separately.
  snapshot_sha256: d4d39f7cba61c260a6a0b178b76ef323140cf2aa86a5d8d5ca868b281e614c52
- evidence_id: ro
  kind: authority
  reference: http://purl.obolibrary.org/obo/ro.owl
  locator: RO:0002326 and recursively inspected superproperties, including RO:0002216,
    RO:0002500 and RO:0002595
  accessed_at: '2026-10-20T06:53:47Z'
  support: refutes
  summary: The contributes-to relation inherits material-entity-to-process semantics.
    The record’s metabolic_gene_loss subject is explicitly a biological process. This
    is a manual ontology-semantic finding; native mapping wildcards do not remove
    the inherited constraint.
  snapshot_sha256: ed07ffc7b5aa53a820164c0d859290f088314719117946acb6dd8dd35fa5ca3c
- evidence_id: historical
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search
  locator: PMIDs42130304,41612704,40831140 and41764142; titles, abstracts and exact
    retained-fragment checks
  accessed_at: '2026-10-20T06:53:30Z'
  support: partial
  summary: All identifiers resolve and all retained fragments match. The weevil–bacterial
    study directly concerns endosymbiosis; the plastid review concerns endosymbiotic
    origins; the insect-microbiome paper explicitly leaves endosymbiont identity unresolved.
    Their failure to support the current reduction question does not make them unrelated
    to the trait.
  snapshot_sha256: 50a43b4e5a87d2baa9e7ffa3363212ee33ae16540bd1217a778b50b662278ba5
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: identifier, label, synonym and term kind'
  outcome: supported
  target_ids:
  - traitmech:000045
  summary: The exact historical METPO term is obsolete, and the local identifier has
    a documented pending class proposal. The target is an ecological trait rather
    than a taxon or organelle record.
  evidence_ids:
  - record
  - identity
  - model
  - hierarchy
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: definition and narrower source scope'
  outcome: concern
  target_ids:
  - traitmech:000045
  summary: The intracellular concept and qualified reduced-genome observation have
    source support. The definition also allows tissue-level residence, while the graph
    labels that broader location intracellular. This wording distinction needs clarification;
    a universal genome-reduction claim is not attributed to the already qualified
    description.
  evidence_ids:
  - record
  - mccutcheon
  - poole
- assessment_id: hierarchy
  area: consistency
  topic: 'Native checklist: broader parent and proposed vocabulary'
  outcome: supported
  target_ids:
  - traitmech:000045
  summary: Symbiosis is broader. The v5/v7/v8 proposal vocabulary is identifiable
    and must remain distinguished from active upstream terms; the documented v7 hierarchy
    caveat is not silently resolved by this review.
  evidence_ids:
  - hierarchy
  - identity
  - model
  - structure
- assessment_id: category
  area: representation
  topic: 'Native checklist: ecology category and nonmechanistic scope'
  outcome: supported
  target_ids:
  - traitmech:000045
  summary: A broad ecological class can carry contextual examples of evolutionary
    consequences. Three components are documented but do not automatically fail NONMECHANISTIC
    scope. No forced universal molecular pathway or arbitrary protein instance is
    required.
  evidence_ids:
  - record
  - model
  - structure
- assessment_id: examples
  area: scope
  topic: 'Native checklist: Buchnera example, identity and nearest evidence'
  outcome: supported
  target_ids:
  - traitmech:000045
  summary: The example’s taxon, nutritional role, intracellular location and maternal
    transmission are directly supported by the cited profile. It is an illustrative
    obligate association, not evidence that every endosymbiotic lifestyle behaves
    identically.
  evidence_ids:
  - record
  - buchnera
  - taxon
  dimensions:
  - name: example_context
    value: Buchnera aphidicola in aphid bacteriocytes
    definition: Context supported by the canonical-example citation, distinct from
      rhizobial or other host associations.
    evidence_ids:
    - buchnera
    - taxon
  - name: graph_scope
    value: NONMECHANISTIC; contextual obligate and other endosymbiotic examples
    definition: Declared scope assessed with textual qualifications; no single universal
      causal program is inferred.
    evidence_ids:
    - record
    - model
- assessment_id: evidence
  area: evidence
  topic: 'Native checklist: bibliography, narrow support and quotations'
  outcome: concern
  target_ids:
  - traitmech:000045
  summary: The source identities are sound and the contextual Song/Bai/Silva claims
    are traceable. No active snippets were tested by the native checker. Poole remains
    limited to its publisher preview; historical quotations were separately checked
    and their blanket irrelevance disclaimer is inaccurate.
  evidence_ids:
  - bibliography
  - mccutcheon
  - poole
  - song
  - bai
  - silva
  - buchnera
  - historical
  - check-endosymbiosis-snippets-network
- assessment_id: graph
  area: graph
  topic: 'Native checklist: ten nodes and seven-edge ledger'
  outcome: concern
  target_ids:
  - traitmech:000045
  summary: The contextual statements have identifiable support, but edge3 misuses
    RO contributes to. Node wording conflates cell-level and tissue-level localization.
    Detached context is correctly noticed by the discussion without establishing which
    causal links should be added.
  evidence_ids:
  - record
  - structure
  - ro
  - mccutcheon
  - poole
  - song
  - bai
  - silva
  details: 'Zero-based edge ledger: 0 localization/confers/trait is a conceptual bridge
    illustrated by rhizobia; detailed nearest-source cell-localization text remains
    an access limitation. 1 trait/causes/reductive evolution is explicitly qualified
    to long-term obligate intracellular life and small effective population size;
    the cited review supports that context, not inevitability for the entire class.
    2 confined habitat/drives/metabolic loss is a contextual review-level explanation,
    not an independently isolated habitat effect. 3 metabolic loss/contributes to/reductive
    evolution has plausible ordinary-language meaning but incompatible RO subject
    semantics. 4 bottleneck/associated with/limited recombination is consistent with
    the cited small-founder/asexual context and retains an associative predicate.
    5 pathway complementarity/supports/nutritional compensation is supported in the
    particular mealybug association; it does not prove universal loss of host-complemented
    functions. 6 genome reduction/leads to/dependence matches the named cockroach-symbiont
    introduction. All node IDs and discussion anchors resolve.'
- assessment_id: discussion
  area: scope
  topic: 'Native checklist: scientific question, inference and retained scan history'
  outcome: concern
  target_ids:
  - traitmech:000045
  summary: The discussion correctly identifies two detached pairs. Its opposing-loss-spectrum
    claim and causal support/refutation interpretations are stronger than the cited
    evidence, and one compensation claim reverses the nutritional direction in the
    graph. Historical sources are retained honestly as quotations but mischaracterized
    as uniformly off-topic.
  evidence_ids:
  - record
  - structure
  - mccutcheon
  - song
  - bai
  - historical
  - owners
- assessment_id: status
  area: provenance
  topic: 'Native checklist: mapping status, history and checks'
  outcome: unknown
  target_ids:
  - traitmech:000045
  summary: Focused schema checks pass. The record and repository history disclose
    AI-assisted creation, promotion and subsequent changes; independent human sign-off
    for REVIEWED remains unestablished. No promotion or history mutation is performed
    here.
  evidence_ids:
  - record
  - owners
  - check-endosymbiosis-validate
  - check-endosymbiosis-strict
  - check-validate-history
findings:
- finding_id: contributes-to-subject-type
  issue_key: endosymbiosis-contributes-to-subject-type
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: RO contributes to is applied to a process subject
  description: The metabolic_gene_loss node is a biological process, while RO:0002326
    inherits a material-entity subject constraint. A process can contribute to another
    process in ordinary language without satisfying this specific relation. Successful
    closed-schema or mapping checks do not establish semantic compatibility.
  target_ids:
  - traitmech:000045
  field_paths:
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].nodes[4].node_type
  evidence_ids:
  - record
  - ro
  - model
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endosymbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate-label mapping; semantic constraints remain despite permissive
      type gates
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: discussion-causal-overclaim
  issue_key: endosymbiosis-discussion-causal-overclaim
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The discussion treats interacting explanations as a decisive binary
  description: The rationale says drift and compensation predict opposite loss spectra
    and assigns exact losses to host supply. The reviewed sources preserve functional
    constraints and interacting causes; the graph’s nutritional_compensation node
    concerns host nutritional needs, not a proof that the host supplies all lost symbiont
    functions. The proposed comparative association also cannot uniquely establish
    the stated causal dominance or dismiss the other explanation.
  target_ids:
  - traitmech:000045
  field_paths:
  - discussions[0].rationale
  - discussions[0].proposed_experiments[0].would_support
  - discussions[0].proposed_experiments[0].would_refute
  evidence_ids:
  - record
  - mccutcheon
  - song
  - bai
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endosymbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion PLAN and retained scan-provenance text
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: cell-tissue-scope
  issue_key: endosymbiosis-cell-tissue-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Intracellular wording includes the broader tissue-level location
  description: The localization node is labelled intracellular but describes residence
    inside cells or tissues. A tissue can contain both intracellular and extracellular
    locations. The broad trait definition and narrower genome-reduction graph can
    coexist, but those two meanings should not be treated as interchangeable.
  target_ids:
  - traitmech:000045
  field_paths:
  - definition
  - causal_graphs[0].nodes[1].label
  - causal_graphs[0].nodes[1].description
  evidence_ids:
  - record
  - mccutcheon
  - poole
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endosymbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: historical-source-description
  issue_key: endosymbiosis-historical-source-description
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical references are not uniformly unrelated to endosymbiosis
  description: The note says the three additional references concern neither the original
    sentence nor this trait. Their inspected abstracts include a bacterial endosymbiosis
    study, endosymbiotic plastid origins, and an explicit unresolved endosymbiont
    question. They need not support this particular genome-reduction discussion, but
    that is a narrower and more accurate disclaimer.
  target_ids:
  - traitmech:000045
  field_paths:
  - discussions[0].notes
  evidence_ids:
  - record
  - historical
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endosymbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion PLAN and retained scan-provenance text
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reassess-process-relation
  description: Reconcile the intended process relationship with a source-supported,
    endpoint-compatible representation.
  finding_ids:
  - contributes-to-subject-type
  target_ids:
  - traitmech:000045
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endosymbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Shared predicate-label mapping; semantic constraints remain despite permissive
      type gates
  acceptance_checks:
  - Inspect the exact relation definition and inherited constraints, not just its
    English label.
  - Do not change a process into a material entity solely to satisfy the existing
    identifier.
  - After authorized curation run focused validate/strict, applicable graph and grounding
    checks, guarded history requirements and qc.
- action_id: bound-causal-interpretation
  description: Preserve a useful comparative question while qualifying its causal
    conclusions and nutritional direction.
  finding_ids:
  - discussion-causal-overclaim
  target_ids:
  - traitmech:000045
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endosymbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion PLAN and retained scan-provenance text
  acceptance_checks:
  - Distinguish an observed association from a unique causal explanation and allow
    interacting processes.
  - Describe the same host-versus-symbiont nutritional relation in the graph and discussion.
  - Do not invent missing mechanisms or redesign a biological intervention; the correction
    is interpretation and source scope.
  - Reconcile the maintained discussion writer and use focused strict/source checks
    plus applicable qc after authorized edits.
- action_id: clarify-localization-scope
  description: Keep the broader trait boundary and the selected intracellular graph
    context explicit and internally consistent.
  finding_ids:
  - cell-tissue-scope
  target_ids:
  - traitmech:000045
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endosymbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain a source-backed distinction between residence within host tissue and residence
    within a host cell.
  - Do not broaden the reduced-genome consequence to all tissue-associated symbioses.
  - Run focused strict and source checks after authorized wording changes.
- action_id: correct-source-disclaimer
  description: Describe the historical references’ relevance precisely while preserving
    their non-evidentiary status for the current question.
  finding_ids:
  - historical-source-description
  target_ids:
  - traitmech:000045
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/endosymbiosis.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/curate_knowledge_gaps.py
    role: Maintained discussion PLAN and retained scan-provenance text
  acceptance_checks:
  - Retain the original identifiers and exact historical fragments.
  - Distinguish being related to the broad trait from supporting this specific question.
  - Reconcile the maintained provenance text and run focused strict validation after
    authorized edits.
limitations:
- Poole full text was not retrieved; the review inspected its publisher abstract/key
  points and bibliographic record. No full-paper absence claim is made.
- McCutcheon/Moran was inspected through publisher material and browser-returned cached
  PDF passages; a direct PDF download returned404 and no local raw PDF hash is claimed.
- The Song review and Bai/Silva studies support contextual claims at different taxonomic
  and evidentiary scopes. These are not treated as a universal model for all endosymbioses.
- The full-corpus graph connectivity report is not a focused mechanistic assessment
  of this NONMECHANISTIC graph. Its three components are separately documented.
- Ontology semantics were inspected manually. The review does not claim an OWL reasoning
  run or upstream adoption of proposed METPO terms.
- The source snapshot supports the local fallback and pending-proposal distinction;
  it does not establish absence from all newer ontology releases.
- Human sign-off remains unresolved. Earlier corpus checks retain their actual same-base
  timestamps, baseline findings, adapter skips and superseded failures.
- No experimental redesign, pest-control intervention, pathogenic mechanism improvement
  or biological engineering is proposed.
notes:
- Ignored-and-hidden-inclusive searches covered data/traits, scripts, history, mappings,
  proposals, conf and DO_NOT_WORK.md for endosymbiosis, endosymbiont, traitmech:000045
  and METPO:1007721. Exact ontology searches separately inspected the complete captured
  OWL.
- Only the new immutable review is saved. The scientific target, mappings, discussion
  writer, history and generated artifacts remain unchanged.
tags:
- record-review
- endosymbiosis
- ecology
- needs-curation
```
