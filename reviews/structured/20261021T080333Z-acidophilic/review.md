# Evidence and ontology review of acidophilic growth (METPO:1003003)

- Review: 20261021T080333Z-acidophilic
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T07:55:06Z
- Finished UTC: 2026-10-21T08:03:33Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The acidophilic identity, METPO below5 optimum convention, hierarchy, current ontology identifiers and canonical Picrophilus example are supported. One major finding concerns evolutionary selection used for immediate homeostasis-process demand. Three minor findings concern cutoff-source attribution, literal approximation notation and locally undocumented human acceptance. All thirteen nodes and eleven edges were assessed; four of six snippet occurrences were verified, one is a faithful notation expansion and one remains unverified in directly inspected primary text.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Ninth batch003 target in lexicographic path order, following the saved symbiosis review. The entire target was read and native source capture completed before scientific assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1003003 | data/traits/environment/acidophilic.yaml | maintained | acidophilic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1003003 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1003003 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1003003 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1003003 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1003003 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1003003 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1003003 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1003003 | The selected record validates. |
| Focused strict validation | passed | True | METPO:1003003 | One file scanned; zero strict errors. |
| Focused snippet verification | passed | True | METPO:1003003 | Six snippets over two references: two VERIFIED and four NOT_IN_ABSTRACT. Abstract nonmatches are inconclusive. Manual primary-source inspection yields four verified occurrences, one faithful notation expansion and one unverified Baker PMF quotation. |
| Structured-source runner availability | unavailable | False | METPO:1003003 | Reused bounded runner discovery; official source fallback completed. |
| Official expression-source context | passed | False | METPO:1003003 | Canonical-organism coverage not applicable; one explicitly sourced E. coli PspA lookup supplies bounded computational context only. |

## Scientific And Domain Assessments

### Native checklist: label, active ID, synonyms, polarity and hierarchy

identity: supported. Targets: METPO:1003003.

Active METPO1003003, both exact synonyms and the broader pH-growth-preference parent match. The cutoff is copied faithfully from upstream; historical corrected or rejected identifiers are not current errors.

### Native checklist: definition source and numerical convention

evidence: concern. Targets: METPO:1003003.

The below5 optimum convention is explicit in METPO. The cited definition review supports low-pH growth but its relevant glossary ranges concern a different quantity; Baker uses a narrower below3 optimum convention. Preserve these source distinctions rather than presenting one cutoff as directly established by all cited papers.

### Native checklist: environmental class and contextual graph scope

representation: supported. Targets: METPO:1003003.

ENVIRONMENT/CLASS and NONMECHANISTIC scope fit a broad growth-preference classification. Label-only protein aggregates and mixed membrane components are permitted; no universal shared program or token protein accession is required.

### Native checklist: species, historical names and numerical example

evidence: supported. Targets: METPO:1003003.

PNAS growth and optimum claims reconcile to current taxon46632 through the P. torridus synonym and DSM9790 type material. Direct primary P. oshimae evidence independently corroborates0.7. No wrong-species or citation-defect finding remains.

### Native checklist: all current node identifiers and node concepts

grounding: supported. Targets: METPO:1003003.

Current GO/PATO/CHEBI identifiers resolve in context. The native component enum permits membrane material; STATE correctly denotes the membrane-potential state. Current hydron nomenclature does not make the historical contextual proton label an original wrong-ID finding.

### Native checklist: all endpoints, predicate meaning and source strength

consistency: concern. Targets: METPO:1003003.

All endpoints resolve. Edge7 uses a prolonged evolutionary-selection relation for a process described as facing immediate homeostatic demands. Edge0 remains a bounded evolutionary interpretation of growth/habitat context rather than a directly tested selection result. Other graph statements retain review-level organism/context limits.

### Native checklist: six snippet occurrences and literal fidelity

evidence: concern. Targets: METPO:1003003.

Four occurrences are verified after routine whitespace/dash normalization, one faithfully expands an approximation symbol, and the Baker PMF phrase remains unverified in directly inspected primary text. This last access limit is not evidence that the quote or biology is false.

### Native checklist: acidophily versus acid-stress response and optional expression data

evidence: supported. Targets: METPO:1003003.

Several sources discuss broader pH stress or selected bacterial/archaeal systems. Their contextual use does not establish one universal acidophile program; expression-module membership supplies context only. No experimental transfer to Picrophilus is inferred.

### Native checklist: required fields, graph structure and optional surfaces

completeness: supported. Targets: METPO:1003003.

Definition, source references and a supported example are present; all graph endpoints resolve. Optional protein examples, pathway context links, discussion items and expression datasets are not missing required content.

### Native checklist: status, imported seed and curation events

provenance: concern. Targets: METPO:1003003.

Thirteen AI-assisted events and one automated import are explicit; no human acceptance link was found within the inspected bounded local provenance.

## Findings

### selection-process-mismatch: Evolutionary selection relation used for immediate homeostatic demand

major / open / confirmed; issue key: acidophilic-selection-process-mismatch.

Edge7 grounds selects for to provisionalMETPO2007401, whose maintained meaning is prolonged environmental selection favoring an adapted trait. The object instead is a homeostasis process, and the description/source discuss immediate acid-challenge demands. This is one combined semantic mismatch, not proof of a failed permissive schema or formal reasoner check.

### cutoff-source-attribution: Exact optimum cutoff is supported by METPO but not directly by the cited definition passage

minor / open / confirmed; issue key: acidophilic-cutoff-source-attribution.

The definition faithfully matches METPO’s below5 optimum. The cited Krulwich review provides low-pH/homeostasis context and growth-limit glossary ranges, rather than that exact optimum cutoff; Baker uses a narrower below3 convention. Make the numerical convention’s provenance explicit without treating the upstream identity or the biological examples as wrong.

### approximation-quote-fidelity: Verbatim snippet expands a source approximation symbol

minor / open / confirmed; issue key: acidophilic-approximation-quote-fidelity.

Edge4’s snippet spells out approximately where the publisher Key Points uses the approximation symbol. The number and meaning are supported; preserve the literal source wording or keep the expansion in notes. Ordinary hyphen/en-dash normalization in the repeated growth-range snippet needs no separate finding.

### human-acceptance-link: Human acceptance is not linked in inspected local provenance

minor / open / confirmed; issue key: acidophilic-human-acceptance-link.

The target has thirteen AI-assisted events plus one automated METPO-import event. No explicit human scientific acceptance reference was found in the inspected target fields and bounded ignored-inclusive local matches. Private or remote acceptance was not searched and is not ruled out.

## Recommended Actions And Acceptance Checks

### align-selection-claim

In separately authorized curation, reconcile edge7’s predicate, object and source claim with either an explicitly supported evolutionary statement or the immediate physiological-demand statement actually evidenced.

- Predicate definition, endpoint role and source describe the same temporal and biological claim.
- Check shared mapping replay so a generic label match does not silently restore the mismatch.
- Run focused strict validation and relevant graph checks, append native curation history, regenerate affected products and run just qc.

### clarify-cutoff-provenance

Document the pinned METPO optimum convention and attach source support at the correct level; preserve the distinction between growth limit, optimum and narrower usage in individual reviews.

- The evidence note identifies which authority supplies the exact cutoff.
- Do not change the correct upstream identity solely to match a narrower literature convention.
- Run focused validation and the applicable history/product gates after any authorized edit.

### preserve-literal-quote

Use literal inspected source wording for the edge4 snippet, or move its faithful notation expansion into a note.

- Snippet matches the chosen publisher surface; manuscript and preview wording are not conflated.
- Retain the supported numerical meaning and check source snippets after the authorized correction.

### link-acceptance

Locate and link existing human scientific acceptance or obtain it through the established process; preserve AI history and reassess status if acceptance remains unavailable.

- Acceptance identifies this record/revision and scientific scope.
- Automated validation and review are not represented as human sign-off.

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
| check-acidophilic-validate | /private/tmp/traitmech-record-sweep-003.4opxlhgf/acidophilic-validate.log; Executed 2026-10-21T07:55:35Z through 2026-10-21T07:55:35Z; metadata acidophilic-validate.json | context_only | The selected record validates. |
| check-acidophilic-strict | /private/tmp/traitmech-record-sweep-003.4opxlhgf/acidophilic-strict.log; Executed 2026-10-21T07:55:35Z through 2026-10-21T07:55:36Z; metadata acidophilic-strict.json | context_only | One file scanned; zero strict errors. |
| check-acidophilic-snippets | /private/tmp/traitmech-record-sweep-003.4opxlhgf/acidophilic-snippets.log; Executed 2026-10-21T07:55:39Z through 2026-10-21T07:55:44Z; metadata acidophilic-snippets.json | context_only | Six snippets over two references: two VERIFIED and four NOT_IN_ABSTRACT. Abstract nonmatches are inconclusive. Manual primary-source inspection yields four verified occurrences, one faithful notation expansion and one unverified Baker PMF quotation. |
| record | data/traits/environment/acidophilic.yaml; Entire record; thirteen nodes, eleven edges and fourteen history events | partial | The record denotes an environmental growth-preference class. A selection predicate is used for an immediate homeostasis-process claim; other proposed follow-up concerns bounded evidence attribution and provenance. |
| parent | data/traits/environment/ph_growth_preference.yaml; Entire contextual parent; identity and definition | supports | The parent describes growth response to environmental pH and is strictly broader. It is context rather than an additional review target. |
| shape | Read-only graph and provenance inspection; All node IDs, edge endpoints and event assistance fields | supports | Thirteen unique nodes, eleven edges and all endpoints resolve. Thirteen of fourteen events disclose AI assistance; the remaining event is automated METPO seeding. No pathway context link is asserted. |
| policy | docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml; NONMECHANISTIC scope, REVIEWED_LABEL_ONLY and CausalNodeTypeEnum | supports | Broad environmental context permits reviewed label-only protein aggregates without token examples. CELLULAR_LOCALIZATION includes a cellular component, so a mixed membrane-component node is not automatically mistyped. Optional datasets and predicate IDs are not mandatory. |
| identity | data/raw/metpo.owl; mappings/trait_exact_match_review.tsv; METPO1003003 and parent1003000; exact synonyms; mapping row17 | supports | Active METPO identity exactly supplies the below-5 optimal-growth definition and the acidophil/acidophile synonyms. The rejected histological-dye PATO match is a documented exclusion, not a current erroneous cross-reference. |
| identifiers | QuickGO, ChEBI and NCBI Taxonomy official endpoints; GO0051453 and historical0030641; CHEBI15378; NCBITaxon46632 | supports | Current GO0051453 is active intracellular-pH regulation; the historical replaced GO term is obsolete. CHEBI15378 is currently hydron, compatible with contextual H+ usage. Taxon46632 is P. oshimae and includes P. torridus as a synonym, preserving the historical example citation. |
| pato | Cached authoritative PATO database; PATO0001429, historical0001428 and rejected0002418 | supports | Current1429 denotes acidic, while1428 is broader medium acidity. Histological-dye affinity2418 is distinct and already rejected in the mapping table. An environmental-condition node can carry the acidic-quality grounding. |
| selection-rule | proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv; METPO2007401 selects for, row4 | partial | The maintained definition denotes prolonged selection pressure favoring organisms expressing an adapted trait. It does not denote immediate physiological demand on a process. Permissive generic causal-node domain/range do not erase the intended semantics. |
| other-relations | proposals/metpo_traitmech_v6/metpo_proposal_properties_robot.tsv; proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv; authoritative RO; Gradient-imposition and confers proposal meanings; RO0002327 inherited roles | supports | The gradient and process-to-trait proposal meanings fit their contextual uses and remain provisional. Material membrane components can fill the RO material-executor role; no blanket chemical-actor or component-domain error is inferred. |
| provenance | Target history and bounded local provenance; Ignored-inclusive identifier, graph ID and record-path search | partial | No explicit human acceptance reference was found in the inspected target events or matching local provenance. The non-AI seed event is not human scientific sign-off; remote/private acceptance remains unknown. |
| status-rule | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md; Status/audit and human Verification gate | supports | REVIEWED requires human scientific acceptance; automated seeding, AI-assisted events and deterministic checks do not provide it. |
| expression | https://imodulondb.org/api/datasets; Original07:36:12Z catalog; one e_coli/modulome PspA query and selected component summary07:57:25–47Z | context_only | No canonical Picrophilus dataset is listed. The cited review explicitly names E. coli in its PspA bibliography, motivating a bounded source-context lookup: b1304 belongs to component0 Phage Shock with eight genes. This is computational membership, not acidophily, proton-exclusion causality or transfer to Picrophilus. |
| runner | Local structured-source runner discovery; Reused bounded ignored-inclusive search07:35:50Z | context_only | No usable runner was found in the original install/PATH/project scope. The official API fallback completed; this is not a fresh or whole-filesystem absence assertion. |
| ledger | Independent documentary node/edge assessment; All thirteen nodes and eleven edges; zero-based locators | partial | Confirms the edge7 selection-versus-immediate-process mismatch. Current identities and historic correction records remain distinct; no additional component or material-actor failure was found. |
| bibliography | Europe PMC, NCBI BioC, publisher and institutional sources; Five cited identities plus one supplementary primary source; twenty initial access attempts and fourteen hashed responses | partial | All cited identities resolve. Initial ledger reported five literal matches plus one notation expansion; the later Baker qualification supersedes the literal count because the PMF phrase was only exposed in search-rendered publisher excerpts. Initial failures, challenge HTML and preview-only responses are retained. |
| krulwich | https://pmc.ncbi.nlm.nih.gov/articles/PMC3247762/; DOI10.1038/nrmicro2549; NCBI BioC manuscript offsets3309,3940,9793,10376,37515,45420–45441 | partial | Supports pH gradients, homeostasis and contextual proton transport, including neutralophile acid challenge. The homeostatic-demand passage does not establish evolutionary selection. Glossary growth-limit ranges do not supply the exact optimal-growth cutoff in the METPO definition. |
| krulwich-preview | https://www.nature.com/articles/nrmicro2549; Publisher Key Points bullet1 and Glossary; HTML response from attempted PDF URL | partial | The repeated growth-range snippets match after dash normalization. The cytoplasmic-pH snippet expands the approximation symbol into a word, preserving meaning but not literal wording. This response is HTML preview, despite its local .pdf suffix. |
| baker | https://pubmed.ncbi.nlm.nih.gov/17331729/; DOI10.1016/j.tim.2007.02.005; inspected indexed abstract sentences1–4 | partial | The abstract supports a transmembrane pH gradient, low membrane permeability and reversed potential; two abstract snippets match exactly. It uses an optimal-growth cutoff below3, narrower than this record’s pinned METPO convention. The PMF quotation was not verified in directly inspected primary text; search-rendered section excerpts remain leads. |
| example | https://pmc.ncbi.nlm.nih.gov/articles/PMC428478/; DOI10.1073/pnas.0401356101; root Abstract/Introduction read completed by07:58:23Z; source-agent publisher Abstract/Introduction/Methods strain identification completed by07:56:33Z | supports | The paper names both historical species as growing near pH0 and gives optimum0.7 for historical P. torridus DSM9790. Current NCBI46632 includes that synonym and type material, reconciling the example. The same article notes an intracellular-pH exception; not every contextual graph branch must apply to this example. |
| example-corroboration | https://pubmed.ncbi.nlm.nih.gov/9672680/; DOI10.1007/s007920050044; abstract first sentence | supports | Independent primary evidence explicitly reports P. oshimae optimal growth at pH0.7. This supports the stated value without implying that the cited historical species names remain separate current taxa. |
| cation | https://pmc.ncbi.nlm.nih.gov/articles/PMC11471286/; DOI10.1111/1758-2229.70019; Living under acidic conditions sec0004 paragraphs2–3 and linked bibliography | supports | Directly supports the contextual cation-uptake and structural-adaptation review statements. The PspA bibliography names E. coli, so acid-stress protection is not itself evidence of an acidophilic optimum or applicability to the canonical archaeon. |
| lipids | https://www.frontiersin.org/journals/biophysics/articles/10.3389/frbis.2023.1338019/pdf; Abstractp1, Effects of growth pH p3, Conclusionp5 and Table1 | supports | The membrane review supports tetraether/lower-permeability synthesis for thermoacidophilic archaea, distinguishes model-membrane results from cellular inference and notes Picrophilus intracellularpH4.6. Retain this context; the broad graph does not assert that every branch applies to every acidophile. |
| baker-qualification | Direct-source access qualification superseding the initial source ledger; Supplement created08:01:32Z and updated08:01:41Z; original ledger preserved | supports | The PMF phrase was visible only in search-rendered publisher excerpts. Direct-source verification is unavailable, so the correct count is four verified occurrences, one faithful notation expansion and one unverified quotation. General gradient support remains in the inspected abstract. |

## Limits And Additional Notes

- Baker’s indexed abstract was inspected; direct publisher-page/PDF attempts failed or timed out. Search-rendered publisher section excerpts remain leads and do not verify the exact PMF quotation. Its absence from the abstract does not establish falsity.
- Krulwich author-manuscript text and publisher preview differ in wording; quotation fidelity was checked against the stated surface. The attempted publisher PDF response was HTML preview, and PMC shell HTML responses were challenges.
- PNAS relevant source text was inspected through the browser without a downloaded body hash; current NCBI synonym and type-material mapping reconcile historical names. The earlier possible species/citation issue was withdrawn before saving.
- The exact below5 optimum comes from pinned METPO. Literature usages and lowest-growth versus optimal-growth quantities remain distinguished.
- Edge0 selection wording is an interpretive bridge from ecological context, not directly tested evolution in the cited snippet; it is not added as a duplicate major finding.
- Contextual proton transport, membrane-adaptation and near-neutral intracellular-pH statements have taxon/physiology exceptions. A broad NONMECHANISTIC graph does not make all branches universal or specific to the canonical example.
- Only one source-context E. coli PspA query and selected module summary were inspected. No canonical Picrophilus dataset, study/dataset strain equivalence, activity-response interpretation or cross-species transfer was asserted.
- Semantic predicate concerns are distinct from passing native schema checks; no failed formal reasoner result is claimed.
- Human acceptance outside the inspected target fields and bounded ignored-inclusive local search remains unknown.
- No scientific record, schema, mapping, writer, history, status or generated page was changed.
- Field paths use zero-based indices.
- The earlier apparent historical-species mismatch was resolved through current taxonomy before saving; no finding is retained for it.
- The Baker direct-source access qualification supersedes the initial source-ledger exact-match count.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T080333Z-acidophilic
kind: record
repository: CultureBotAI/TraitMech
title: Evidence and ontology review of acidophilic growth (METPO:1003003)
started_at: '2026-10-21T07:55:06Z'
finished_at: '2026-10-21T08:03:33Z'
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
summary: The acidophilic identity, METPO below5 optimum convention, hierarchy, current
  ontology identifiers and canonical Picrophilus example are supported. One major
  finding concerns evolutionary selection used for immediate homeostasis-process demand.
  Three minor findings concern cutoff-source attribution, literal approximation notation
  and locally undocumented human acceptance. All thirteen nodes and eleven edges were
  assessed; four of six snippet occurrences were verified, one is a faithful notation
  expansion and one remains unverified in directly inspected primary text.
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
  - path: data/traits/environment/acidophilic.yaml
    sha256: 4170ebccedecf6a0d53cd984fc98feb9a670ab224f6b66774e937f9ebd93486b
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
  - path: mappings/node_grounding.tsv
    sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
    role: context
  - path: mappings/predicate_grounding.tsv
    sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
    role: context
  - path: mappings/trait_exact_match_review.tsv
    sha256: 7728593d526d9a723716e5daad64beb7e1ab5c2e4221ae8d43dd9480cd02f62b
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
  - path: research/traits/environment/acidophilic-deep-research-falcon.md
    sha256: 1c03c4b3d6fbd59a812c506d82ebd1ab260e4a7941c6c5dbba91b5f3944a475a
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
  - path: scripts/migrate_process_quality_consistency.py
    sha256: 1a83ad3dba79ed0c958b875a6fcc4b9e562259af26da2f248d32d5cf7784f80a
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
- target_id: METPO:1003003
  path: data/traits/environment/acidophilic.yaml
  label: acidophilic
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/acidophilic.yaml
    role: Maintained scientific record
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
  selection: Ninth batch003 target in lexicographic path order, following the saved
    symbiosis review. The entire target was read and native source capture completed
    before scientific assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1003003
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1003003
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
  - METPO:1003003
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
  - METPO:1003003
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
  - METPO:1003003
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
  - METPO:1003003
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
  - METPO:1003003
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
  - METPO:1003003
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
- check_id: acidophilic-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1003003
  command: just validate data/traits/environment/acidophilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The selected record validates.
  evidence_ids:
  - check-acidophilic-validate
- check_id: acidophilic-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1003003
  command: just validate-strict data/traits/environment/acidophilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero strict errors.
  evidence_ids:
  - check-acidophilic-strict
- check_id: acidophilic-snippets
  name: Focused snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1003003
  command: just verify-snippets --record data/traits/environment/acidophilic.yaml
    --out /private/tmp/traitmech-record-sweep-003.4opxlhgf/acidophilic-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Six snippets over two references: two VERIFIED and four NOT_IN_ABSTRACT.
    Abstract nonmatches are inconclusive. Manual primary-source inspection yields
    four verified occurrences, one faithful notation expansion and one unverified
    Baker PMF quotation.'
  evidence_ids:
  - check-acidophilic-snippets
- check_id: structured-source-runner
  name: Structured-source runner availability
  status: unavailable
  required: false
  target_ids:
  - METPO:1003003
  summary: Reused bounded runner discovery; official source fallback completed.
  evidence_ids:
  - runner
- check_id: expression-context
  name: Official expression-source context
  status: passed
  required: false
  target_ids:
  - METPO:1003003
  summary: Canonical-organism coverage not applicable; one explicitly sourced E. coli
    PspA lookup supplies bounded computational context only.
  evidence_ids:
  - expression
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T08:03:33Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T08:03:33Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T08:03:33Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T08:03:33Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T08:03:33Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T08:03:33Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T08:03:33Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-acidophilic-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/acidophilic-validate.log
  locator: Executed 2026-10-21T07:55:35Z through 2026-10-21T07:55:35Z; metadata acidophilic-validate.json
  accessed_at: '2026-10-21T08:03:33Z'
  support: context_only
  summary: The selected record validates.
  snapshot_sha256: d20bd0a2ca7c57246d373b0cb12caf1955faf3a04c799d56f55a0cff091db56b
- evidence_id: check-acidophilic-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/acidophilic-strict.log
  locator: Executed 2026-10-21T07:55:35Z through 2026-10-21T07:55:36Z; metadata acidophilic-strict.json
  accessed_at: '2026-10-21T08:03:33Z'
  support: context_only
  summary: One file scanned; zero strict errors.
  snapshot_sha256: ba03b362d1cce9ee87d355ca0290f2d77f53d6741447a9c8359e507d4681c54a
- evidence_id: check-acidophilic-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/acidophilic-snippets.log
  locator: Executed 2026-10-21T07:55:39Z through 2026-10-21T07:55:44Z; metadata acidophilic-snippets.json
  accessed_at: '2026-10-21T08:03:33Z'
  support: context_only
  summary: 'Six snippets over two references: two VERIFIED and four NOT_IN_ABSTRACT.
    Abstract nonmatches are inconclusive. Manual primary-source inspection yields
    four verified occurrences, one faithful notation expansion and one unverified
    Baker PMF quotation.'
  snapshot_sha256: 6ddcc0b3842980ed135a135f6e8c3f212f24ca36d336dcf66675566b0636ba57
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/acidophilic.yaml
  locator: Entire record; thirteen nodes, eleven edges and fourteen history events
  accessed_at: '2026-10-21T08:03:33Z'
  support: partial
  summary: The record denotes an environmental growth-preference class. A selection
    predicate is used for an immediate homeostasis-process claim; other proposed follow-up
    concerns bounded evidence attribution and provenance.
  snapshot_sha256: 4170ebccedecf6a0d53cd984fc98feb9a670ab224f6b66774e937f9ebd93486b
- evidence_id: parent
  kind: record_content
  reference: data/traits/environment/ph_growth_preference.yaml
  locator: Entire contextual parent; identity and definition
  accessed_at: '2026-10-21T08:03:33Z'
  support: supports
  summary: The parent describes growth response to environmental pH and is strictly
    broader. It is context rather than an additional review target.
- evidence_id: shape
  kind: validation
  reference: Read-only graph and provenance inspection
  locator: All node IDs, edge endpoints and event assistance fields
  accessed_at: '2026-10-21T07:55:57Z'
  support: supports
  summary: Thirteen unique nodes, eleven edges and all endpoints resolve. Thirteen
    of fourteen events disclose AI assistance; the remaining event is automated METPO
    seeding. No pathway context link is asserted.
  snapshot_sha256: e5f6093c340f41aa1fc2c787efe7344377036449834049e5f3c5bdb981055727
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml
  locator: NONMECHANISTIC scope, REVIEWED_LABEL_ONLY and CausalNodeTypeEnum
  accessed_at: '2026-10-21T08:03:33Z'
  support: supports
  summary: Broad environmental context permits reviewed label-only protein aggregates
    without token examples. CELLULAR_LOCALIZATION includes a cellular component, so
    a mixed membrane-component node is not automatically mistyped. Optional datasets
    and predicate IDs are not mandatory.
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl; mappings/trait_exact_match_review.tsv
  locator: METPO1003003 and parent1003000; exact synonyms; mapping row17
  accessed_at: '2026-10-21T07:58:06Z'
  support: supports
  summary: Active METPO identity exactly supplies the below-5 optimal-growth definition
    and the acidophil/acidophile synonyms. The rejected histological-dye PATO match
    is a documented exclusion, not a current erroneous cross-reference.
  snapshot_sha256: da7e9e8b9246ea5021405afccbebf389c1c43f1cd9e1b2ddfec005f410456ad1
- evidence_id: identifiers
  kind: authority
  reference: QuickGO, ChEBI and NCBI Taxonomy official endpoints
  locator: GO0051453 and historical0030641; CHEBI15378; NCBITaxon46632
  accessed_at: '2026-10-21T07:58:26Z'
  support: supports
  summary: Current GO0051453 is active intracellular-pH regulation; the historical
    replaced GO term is obsolete. CHEBI15378 is currently hydron, compatible with
    contextual H+ usage. Taxon46632 is P. oshimae and includes P. torridus as a synonym,
    preserving the historical example citation.
  snapshot_sha256: dadb8accf2eeb053007a66715423d9f99c59e86d4e8dc608cbb5dab3946e067a
- evidence_id: pato
  kind: authority
  reference: Cached authoritative PATO database
  locator: PATO0001429, historical0001428 and rejected0002418
  accessed_at: '2026-10-21T07:58:06Z'
  support: supports
  summary: Current1429 denotes acidic, while1428 is broader medium acidity. Histological-dye
    affinity2418 is distinct and already rejected in the mapping table. An environmental-condition
    node can carry the acidic-quality grounding.
  snapshot_sha256: 5d27d7ee9d795d62e3390f51b567ae2364b0456dd59ac69349854fd17b79728f
- evidence_id: selection-rule
  kind: authority
  reference: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
  locator: METPO2007401 selects for, row4
  accessed_at: '2026-10-21T08:03:33Z'
  support: partial
  summary: The maintained definition denotes prolonged selection pressure favoring
    organisms expressing an adapted trait. It does not denote immediate physiological
    demand on a process. Permissive generic causal-node domain/range do not erase
    the intended semantics.
  snapshot_sha256: 4ab5ca37ff8595210254b1099563b4425ecd737ed375dc5a932b44e2ad5c332e
- evidence_id: other-relations
  kind: authority
  reference: proposals/metpo_traitmech_v6/metpo_proposal_properties_robot.tsv; proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv;
    authoritative RO
  locator: Gradient-imposition and confers proposal meanings; RO0002327 inherited
    roles
  accessed_at: '2026-10-21T07:58:06Z'
  support: supports
  summary: The gradient and process-to-trait proposal meanings fit their contextual
    uses and remain provisional. Material membrane components can fill the RO material-executor
    role; no blanket chemical-actor or component-domain error is inferred.
  snapshot_sha256: 18b7b768a0a61a01bf26b64314431b1efd2df6aae72e1484c54903250e340c1e
- evidence_id: provenance
  kind: search
  reference: Target history and bounded local provenance
  locator: Ignored-inclusive identifier, graph ID and record-path search
  accessed_at: '2026-10-21T07:55:57Z'
  support: partial
  summary: No explicit human acceptance reference was found in the inspected target
    events or matching local provenance. The non-AI seed event is not human scientific
    sign-off; remote/private acceptance remains unknown.
  snapshot_sha256: 530b218310b9f3c202403a6c9ada8838e90d28d6e86ca18de50484db24e4379c
  search_scope: rg --no-ignore --hidden across scripts, history, mappings, reviews
    and research/traits/environment, plus all fourteen target events. References in
    other review input lists are not reviews targeting this record. No global or remote/private
    absence claim.
- evidence_id: status-rule
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md
  locator: Status/audit and human Verification gate
  accessed_at: '2026-10-21T08:03:33Z'
  support: supports
  summary: REVIEWED requires human scientific acceptance; automated seeding, AI-assisted
    events and deterministic checks do not provide it.
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Original07:36:12Z catalog; one e_coli/modulome PspA query and selected
    component summary07:57:25–47Z
  accessed_at: '2026-10-21T07:58:12Z'
  support: context_only
  summary: 'No canonical Picrophilus dataset is listed. The cited review explicitly
    names E. coli in its PspA bibliography, motivating a bounded source-context lookup:
    b1304 belongs to component0 Phage Shock with eight genes. This is computational
    membership, not acidophily, proton-exclusion causality or transfer to Picrophilus.'
  snapshot_sha256: 8232635a53d8510dc15a81b4361bbb9f73cb1aae907c6594e43e6dca12702430
- evidence_id: runner
  kind: search
  reference: Local structured-source runner discovery
  locator: Reused bounded ignored-inclusive search07:35:50Z
  accessed_at: '2026-10-21T07:35:50Z'
  support: context_only
  summary: No usable runner was found in the original install/PATH/project scope.
    The official API fallback completed; this is not a fresh or whole-filesystem absence
    assertion.
  snapshot_sha256: 255ec15986d2ece8ee78c72591e43429c1bb5f22c3326a349667326e3fe1b380
  search_scope: Original bounded PATH/install/project roots and ignored-inclusive
    traversal are listed in the reused receipt; unsearched directories remain unknown.
- evidence_id: ledger
  kind: validation
  reference: Independent documentary node/edge assessment
  locator: All thirteen nodes and eleven edges; zero-based locators
  accessed_at: '2026-10-21T07:59:55Z'
  support: partial
  summary: Confirms the edge7 selection-versus-immediate-process mismatch. Current
    identities and historic correction records remain distinct; no additional component
    or material-actor failure was found.
  snapshot_sha256: 46c6a8658c79b60d0e406fd4534ba71fce79cb39f0cb653c13ed8bb3bc7d792c
- evidence_id: bibliography
  kind: database
  reference: Europe PMC, NCBI BioC, publisher and institutional sources
  locator: Five cited identities plus one supplementary primary source; twenty initial
    access attempts and fourteen hashed responses
  accessed_at: '2026-10-21T08:00:27Z'
  support: partial
  summary: All cited identities resolve. Initial ledger reported five literal matches
    plus one notation expansion; the later Baker qualification supersedes the literal
    count because the PMF phrase was only exposed in search-rendered publisher excerpts.
    Initial failures, challenge HTML and preview-only responses are retained.
  snapshot_sha256: ec71dae12506450a9825727034354379541922248188852f1de7c1b28702f9f0
- evidence_id: krulwich
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3247762/
  locator: DOI10.1038/nrmicro2549; NCBI BioC manuscript offsets3309,3940,9793,10376,37515,45420–45441
  accessed_at: '2026-10-21T07:57:33Z'
  support: partial
  summary: Supports pH gradients, homeostasis and contextual proton transport, including
    neutralophile acid challenge. The homeostatic-demand passage does not establish
    evolutionary selection. Glossary growth-limit ranges do not supply the exact optimal-growth
    cutoff in the METPO definition.
  snapshot_sha256: 903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f
- evidence_id: krulwich-preview
  kind: primary_source
  reference: https://www.nature.com/articles/nrmicro2549
  locator: Publisher Key Points bullet1 and Glossary; HTML response from attempted
    PDF URL
  accessed_at: '2026-10-21T07:56:36Z'
  support: partial
  summary: The repeated growth-range snippets match after dash normalization. The
    cytoplasmic-pH snippet expands the approximation symbol into a word, preserving
    meaning but not literal wording. This response is HTML preview, despite its local
    .pdf suffix.
  snapshot_sha256: 4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66
- evidence_id: baker
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/17331729/
  locator: DOI10.1016/j.tim.2007.02.005; inspected indexed abstract sentences1–4
  accessed_at: '2026-10-21T07:55:43Z'
  support: partial
  summary: The abstract supports a transmembrane pH gradient, low membrane permeability
    and reversed potential; two abstract snippets match exactly. It uses an optimal-growth
    cutoff below3, narrower than this record’s pinned METPO convention. The PMF quotation
    was not verified in directly inspected primary text; search-rendered section excerpts
    remain leads.
  snapshot_sha256: e12f1b09a1467a8985fae8d345351ad5ef2fc532f35fb10be67203ec41ea939b
- evidence_id: example
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC428478/
  locator: DOI10.1073/pnas.0401356101; root Abstract/Introduction read completed by07:58:23Z;
    source-agent publisher Abstract/Introduction/Methods strain identification completed
    by07:56:33Z
  accessed_at: '2026-10-21T07:58:23Z'
  support: supports
  summary: The paper names both historical species as growing near pH0 and gives optimum0.7
    for historical P. torridus DSM9790. Current NCBI46632 includes that synonym and
    type material, reconciling the example. The same article notes an intracellular-pH
    exception; not every contextual graph branch must apply to this example.
- evidence_id: example-corroboration
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/9672680/
  locator: DOI10.1007/s007920050044; abstract first sentence
  accessed_at: '2026-10-21T07:57:34Z'
  support: supports
  summary: Independent primary evidence explicitly reports P. oshimae optimal growth
    at pH0.7. This supports the stated value without implying that the cited historical
    species names remain separate current taxa.
  snapshot_sha256: a3e2bcdebb6c88b6e5c1096568352b40886ee6ad5da6d48b183ae6eb87f62ccd
- evidence_id: cation
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC11471286/
  locator: DOI10.1111/1758-2229.70019; Living under acidic conditions sec0004 paragraphs2–3
    and linked bibliography
  accessed_at: '2026-10-21T07:55:45Z'
  support: supports
  summary: Directly supports the contextual cation-uptake and structural-adaptation
    review statements. The PspA bibliography names E. coli, so acid-stress protection
    is not itself evidence of an acidophilic optimum or applicability to the canonical
    archaeon.
  snapshot_sha256: 481a4f647bc7a835d74f7ec75d5f5ee8fa54ac76294f3c721a6711fd941ec58e
- evidence_id: lipids
  kind: primary_source
  reference: https://www.frontiersin.org/journals/biophysics/articles/10.3389/frbis.2023.1338019/pdf
  locator: Abstractp1, Effects of growth pH p3, Conclusionp5 and Table1
  accessed_at: '2026-10-21T07:56:34Z'
  support: supports
  summary: The membrane review supports tetraether/lower-permeability synthesis for
    thermoacidophilic archaea, distinguishes model-membrane results from cellular
    inference and notes Picrophilus intracellularpH4.6. Retain this context; the broad
    graph does not assert that every branch applies to every acidophile.
  snapshot_sha256: 6049ec0d36851a2b18f6cc546949b1c90bf02663e8dc4693d74c98cf02c0ecd9
- evidence_id: baker-qualification
  kind: validation
  reference: Direct-source access qualification superseding the initial source ledger
  locator: Supplement created08:01:32Z and updated08:01:41Z; original ledger preserved
  accessed_at: '2026-10-21T08:01:41Z'
  support: supports
  summary: The PMF phrase was visible only in search-rendered publisher excerpts.
    Direct-source verification is unavailable, so the correct count is four verified
    occurrences, one faithful notation expansion and one unverified quotation. General
    gradient support remains in the inspected abstract.
  snapshot_sha256: f4a7f302f31385b7e882d6aea23a4e81224ad7c273e6c1614fe4381756da758c
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: label, active ID, synonyms, polarity and hierarchy'
  outcome: supported
  target_ids:
  - METPO:1003003
  summary: Active METPO1003003, both exact synonyms and the broader pH-growth-preference
    parent match. The cutoff is copied faithfully from upstream; historical corrected
    or rejected identifiers are not current errors.
  evidence_ids:
  - record
  - identity
  - parent
  - identifiers
  - pato
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: definition source and numerical convention'
  outcome: concern
  target_ids:
  - METPO:1003003
  summary: The below5 optimum convention is explicit in METPO. The cited definition
    review supports low-pH growth but its relevant glossary ranges concern a different
    quantity; Baker uses a narrower below3 optimum convention. Preserve these source
    distinctions rather than presenting one cutoff as directly established by all
    cited papers.
  evidence_ids:
  - identity
  - krulwich
  - krulwich-preview
  - baker
- assessment_id: model
  area: representation
  topic: 'Native checklist: environmental class and contextual graph scope'
  outcome: supported
  target_ids:
  - METPO:1003003
  summary: ENVIRONMENT/CLASS and NONMECHANISTIC scope fit a broad growth-preference
    classification. Label-only protein aggregates and mixed membrane components are
    permitted; no universal shared program or token protein accession is required.
  evidence_ids:
  - record
  - policy
  - ledger
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: species, historical names and numerical example'
  outcome: supported
  target_ids:
  - METPO:1003003
  summary: PNAS growth and optimum claims reconcile to current taxon46632 through
    the P. torridus synonym and DSM9790 type material. Direct primary P. oshimae evidence
    independently corroborates0.7. No wrong-species or citation-defect finding remains.
  evidence_ids:
  - example
  - example-corroboration
  - identifiers
- assessment_id: grounding
  area: grounding
  topic: 'Native checklist: all current node identifiers and node concepts'
  outcome: supported
  target_ids:
  - METPO:1003003
  summary: Current GO/PATO/CHEBI identifiers resolve in context. The native component
    enum permits membrane material; STATE correctly denotes the membrane-potential
    state. Current hydron nomenclature does not make the historical contextual proton
    label an original wrong-ID finding.
  evidence_ids:
  - identifiers
  - pato
  - identity
  - policy
  - ledger
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all endpoints, predicate meaning and source strength'
  outcome: concern
  target_ids:
  - METPO:1003003
  summary: All endpoints resolve. Edge7 uses a prolonged evolutionary-selection relation
    for a process described as facing immediate homeostatic demands. Edge0 remains
    a bounded evolutionary interpretation of growth/habitat context rather than a
    directly tested selection result. Other graph statements retain review-level organism/context
    limits.
  evidence_ids:
  - shape
  - selection-rule
  - other-relations
  - ledger
  - krulwich
  - baker
  - cation
  - lipids
  - baker-qualification
- assessment_id: snippets
  area: evidence
  topic: 'Native checklist: six snippet occurrences and literal fidelity'
  outcome: concern
  target_ids:
  - METPO:1003003
  summary: Four occurrences are verified after routine whitespace/dash normalization,
    one faithfully expands an approximation symbol, and the Baker PMF phrase remains
    unverified in directly inspected primary text. This last access limit is not evidence
    that the quote or biology is false.
  evidence_ids:
  - bibliography
  - krulwich-preview
  - baker
  - baker-qualification
- assessment_id: context
  area: evidence
  topic: 'Native checklist: acidophily versus acid-stress response and optional expression
    data'
  outcome: supported
  target_ids:
  - METPO:1003003
  summary: Several sources discuss broader pH stress or selected bacterial/archaeal
    systems. Their contextual use does not establish one universal acidophile program;
    expression-module membership supplies context only. No experimental transfer to
    Picrophilus is inferred.
  evidence_ids:
  - krulwich
  - cation
  - lipids
  - expression
  - record
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: required fields, graph structure and optional surfaces'
  outcome: supported
  target_ids:
  - METPO:1003003
  summary: Definition, source references and a supported example are present; all
    graph endpoints resolve. Optional protein examples, pathway context links, discussion
    items and expression datasets are not missing required content.
  evidence_ids:
  - record
  - shape
  - policy
  - expression
- assessment_id: audit
  area: provenance
  topic: 'Native checklist: status, imported seed and curation events'
  outcome: concern
  target_ids:
  - METPO:1003003
  summary: Thirteen AI-assisted events and one automated import are explicit; no human
    acceptance link was found within the inspected bounded local provenance.
  evidence_ids:
  - provenance
  - status-rule
  - shape
findings:
- finding_id: selection-process-mismatch
  issue_key: acidophilic-selection-process-mismatch
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Evolutionary selection relation used for immediate homeostatic demand
  description: Edge7 grounds selects for to provisionalMETPO2007401, whose maintained
    meaning is prolonged environmental selection favoring an adapted trait. The object
    instead is a homeostasis process, and the description/source discuss immediate
    acid-challenge demands. This is one combined semantic mismatch, not proof of a
    failed permissive schema or formal reasoner check.
  target_ids:
  - METPO:1003003
  field_paths:
  - causal_graphs[0].edges[7]
  evidence_ids:
  - record
  - selection-rule
  - krulwich
  - ledger
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/acidophilic.yaml
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
- finding_id: cutoff-source-attribution
  issue_key: acidophilic-cutoff-source-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Exact optimum cutoff is supported by METPO but not directly by the cited
    definition passage
  description: The definition faithfully matches METPO’s below5 optimum. The cited
    Krulwich review provides low-pH/homeostasis context and growth-limit glossary
    ranges, rather than that exact optimum cutoff; Baker uses a narrower below3 convention.
    Make the numerical convention’s provenance explicit without treating the upstream
    identity or the biological examples as wrong.
  target_ids:
  - METPO:1003003
  field_paths:
  - definition_source
  - definition
  evidence_ids:
  - identity
  - krulwich
  - krulwich-preview
  - baker
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/acidophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: approximation-quote-fidelity
  issue_key: acidophilic-approximation-quote-fidelity
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Verbatim snippet expands a source approximation symbol
  description: Edge4’s snippet spells out approximately where the publisher Key Points
    uses the approximation symbol. The number and meaning are supported; preserve
    the literal source wording or keep the expansion in notes. Ordinary hyphen/en-dash
    normalization in the repeated growth-range snippet needs no separate finding.
  target_ids:
  - METPO:1003003
  field_paths:
  - causal_graphs[0].edges[4].evidence[0].snippet
  evidence_ids:
  - record
  - krulwich-preview
  - bibliography
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/acidophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: acidophilic-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human acceptance is not linked in inspected local provenance
  description: The target has thirteen AI-assisted events plus one automated METPO-import
    event. No explicit human scientific acceptance reference was found in the inspected
    target fields and bounded ignored-inclusive local matches. Private or remote acceptance
    was not searched and is not ruled out.
  target_ids:
  - METPO:1003003
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - status-rule
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/acidophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: align-selection-claim
  description: In separately authorized curation, reconcile edge7’s predicate, object
    and source claim with either an explicitly supported evolutionary statement or
    the immediate physiological-demand statement actually evidenced.
  finding_ids:
  - selection-process-mismatch
  target_ids:
  - METPO:1003003
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/acidophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Predicate definition, endpoint role and source describe the same temporal and
    biological claim.
  - Check shared mapping replay so a generic label match does not silently restore
    the mismatch.
  - Run focused strict validation and relevant graph checks, append native curation
    history, regenerate affected products and run just qc.
- action_id: clarify-cutoff-provenance
  description: Document the pinned METPO optimum convention and attach source support
    at the correct level; preserve the distinction between growth limit, optimum and
    narrower usage in individual reviews.
  finding_ids:
  - cutoff-source-attribution
  target_ids:
  - METPO:1003003
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/acidophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The evidence note identifies which authority supplies the exact cutoff.
  - Do not change the correct upstream identity solely to match a narrower literature
    convention.
  - Run focused validation and the applicable history/product gates after any authorized
    edit.
- action_id: preserve-literal-quote
  description: Use literal inspected source wording for the edge4 snippet, or move
    its faithful notation expansion into a note.
  finding_ids:
  - approximation-quote-fidelity
  target_ids:
  - METPO:1003003
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/acidophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Snippet matches the chosen publisher surface; manuscript and preview wording are
    not conflated.
  - Retain the supported numerical meaning and check source snippets after the authorized
    correction.
- action_id: link-acceptance
  description: Locate and link existing human scientific acceptance or obtain it through
    the established process; preserve AI history and reassess status if acceptance
    remains unavailable.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1003003
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/acidophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies this record/revision and scientific scope.
  - Automated validation and review are not represented as human sign-off.
limitations:
- Baker’s indexed abstract was inspected; direct publisher-page/PDF attempts failed
  or timed out. Search-rendered publisher section excerpts remain leads and do not
  verify the exact PMF quotation. Its absence from the abstract does not establish
  falsity.
- Krulwich author-manuscript text and publisher preview differ in wording; quotation
  fidelity was checked against the stated surface. The attempted publisher PDF response
  was HTML preview, and PMC shell HTML responses were challenges.
- PNAS relevant source text was inspected through the browser without a downloaded
  body hash; current NCBI synonym and type-material mapping reconcile historical names.
  The earlier possible species/citation issue was withdrawn before saving.
- The exact below5 optimum comes from pinned METPO. Literature usages and lowest-growth
  versus optimal-growth quantities remain distinguished.
- Edge0 selection wording is an interpretive bridge from ecological context, not directly
  tested evolution in the cited snippet; it is not added as a duplicate major finding.
- Contextual proton transport, membrane-adaptation and near-neutral intracellular-pH
  statements have taxon/physiology exceptions. A broad NONMECHANISTIC graph does not
  make all branches universal or specific to the canonical example.
- Only one source-context E. coli PspA query and selected module summary were inspected.
  No canonical Picrophilus dataset, study/dataset strain equivalence, activity-response
  interpretation or cross-species transfer was asserted.
- Semantic predicate concerns are distinct from passing native schema checks; no failed
  formal reasoner result is claimed.
- Human acceptance outside the inspected target fields and bounded ignored-inclusive
  local search remains unknown.
- No scientific record, schema, mapping, writer, history, status or generated page
  was changed.
notes:
- Field paths use zero-based indices.
- The earlier apparent historical-species mismatch was resolved through current taxonomy
  before saving; no finding is retained for it.
- The Baker direct-source access qualification supersedes the initial source-ledger
  exact-match count.
tags:
- record-review
- acidophilic
- environment
- needs-curation
```
