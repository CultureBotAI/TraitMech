# Evidence and ontology review of alkaliphily (METPO:1003002)

- Review: 20261021T084513Z-alkaliphilic
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T08:39:13Z
- Finished UTC: 2026-10-21T08:45:13Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The alkaliphilic record has the correct current METPO identity, synonyms and parent. Two major findings concern the cited Natronomonas optimum8.5 versus the strict above9 definition, and three RO relations with incompatible subject roles. Three minor findings concern numerical-definition attribution, Mrp organism scope and a bounded missing human-acceptance link. All eleven nodes and ten edges were assessed; all six excerpts are supported with explicit typography/ellipsis distinctions.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Fourth batch004 target in lexicographic path order. Entire target read before initial native capture; supplemental release-manifest capture retained all previous input hashes. Historical filename is preserved by the documented ontology migration.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1003002 | data/traits/environment/alkaphilic.yaml | maintained | alkaliphilic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1003002 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1003002 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1003002 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1003002 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1003002 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1003002 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1003002 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1003002 | Selected record validates. |
| Focused strict validation | passed | True | METPO:1003002 | One file scanned; zero errors. |
| Focused source snippet check | passed | True | METPO:1003002 | Six snippets across three references: two VERIFIED and four NOT_IN_ABSTRACT. Abstract misses are inconclusive; manual source assessment is recorded separately. |
| Structured-source runner discovery | unavailable | False | METPO:1003002 | Reused bounded discovery; official catalog fallback inspected. |
| Canonical-taxon expression applicability | not_applicable | False | METPO:1003002 | No matching dataset in the inspected catalog. |

## Scientific And Domain Assessments

### Native checklist: current concept, synonyms and hierarchy

identity: supported. Targets: METPO:1003002.

Active METPO1003002, three exact synonyms and broader1003000 match. The historical filename/node ID is deliberately preserved by migration, not a wrong current concept.

### Native checklist: exact optimum convention and nearest literature

evidence: concern. Targets: METPO:1003002.

The exact above9 optimum is directly supported by METPO. Inspected Krulwich glossary/extreme-growth passages provide broader pH context rather than that precise class convention; make the authority explicit.

### Native checklist: ENVIRONMENT/CLASS and contextual graph

representation: supported. Targets: METPO:1003002.

Category and contextual NONMECHANISTIC scope fit. The graph title, reviewed label-only proteins and optional evidence surfaces do not independently require scope promotion or token accessions.

### Native checklist: both canonical organisms and phenotype scope

evidence: concern. Targets: METPO:1003002.

Both current taxon identities resolve. Halodurans has appropriate high-pH growth support; the cited Natronomonas optimum8.5 conflicts with the strict class criterion despite legitimate broader haloalkaliphile terminology.

### Native checklist: current node identities and historical corrections

grounding: supported. Targets: METPO:1003002.

Current METPO/GO/PATO/CHEBI and taxonomy are coherent. Historical dead accessions, acidic PATO, replaced GO and microbe-domain imports were corrected or retracted and are not present defects.

### Native checklist: eleven nodes and ten edge roles

consistency: concern. Targets: METPO:1003002.

Edges6,7,9 use relations requiring roles their subjects do not denote. Protein/feature versus bearer and binding activity versus efficiency should be clarified during repair. Material components at edge8 remain compatible.

### Native checklist: all edge sources and six excerpts

evidence: concern. Targets: METPO:1003002.

All excerpts are supported at exact, typographic or explicit-ellipsis level. Mrp necessity needs its source’s Bacillus scope. ATP body/caption certainty is retained; selection remains a contextual inference. Generic contributions are not proof of a universal mechanism.

### Native checklist: required structure and optional surfaces

completeness: supported. Targets: METPO:1003002.

All endpoints resolve and required identity/evidence surfaces are present. Contextual scope does not demand one protein instance per label, datasets, or a uniquely necessary pathway.

### Native checklist: canonical-taxon database applicability

evidence: supported. Targets: METPO:1003002.

Neither canonical taxon matches the inspected catalog; no substitute species or negative phenotype inference was used.

### Native checklist: AI disclosure, human acceptance and recurrence owners

provenance: concern. Targets: METPO:1003002.

Fifteen events explicitly disclose AI assistance and the release history separately identifies its AI actor. No human acceptance is linked in bounded local provenance. Mapping recurrence and correction of existing IDs are distinct.

## Findings

### canonical-optimum-mismatch: Natronomonas example falls below the defined optimum threshold

major / open / confirmed; issue key: alkaliphilic-canonical-optimum-mismatch.

The nearest cited journal paper explicitly reports optimum pH8.5, while this record requires an optimum above9. Its haloalkaliphilic designation and high-pH isolation environment do not establish that strict class membership. This concerns the cited organism/conditions and operational boundary, not invalid taxonomy or denial of broader haloalkaliphile terminology.

### external-relation-semantics: Three grounded relations conflict with their subject roles

major / open / confirmed; issue key: alkaliphilic-external-relation-semantics.

Edge6 maps a motif/feature or protein-bearer subject to process regulation; edge7 maps binding activity or efficiency to a material enables actor; edge9 maps a retention process to a material contributor. These conflicts do not require assuming every molecular-function object is invalid. Native validation passes, and no failed OWL reasoner run is claimed.

### definition-cutoff-attribution: Attribute the exact optimum cutoff to its defining authority

minor / open / confirmed; issue key: alkaliphilic-definition-cutoff-attribution.

METPO directly supplies the optimum-above9 convention. The nearest inspected Krulwich glossary and extreme-alkaliphile passages discuss growth ranges and model physiology rather than stating that exact class definition. Clarify authority without changing the correct identity or claiming a whole-article absence beyond the inspected passages.

### mrp-organism-scope: Mrp indispensability needs the cited Bacillus scope

minor / open / confirmed; issue key: alkaliphilic-mrp-organism-scope.

The source’s indispensable-role statement explicitly concerns extremely alkaliphilic Bacillus. Node6 and edge5 omit that context in their categorical necessity wording. Retain the contextual mechanism while making its organism scope explicit; the generic NONMECHANISTIC graph is not itself a universal assertion.

### human-acceptance-link: Human scientific acceptance is not linked locally

minor / open / confirmed; issue key: alkaliphilic-human-acceptance-link.

The inspected local target/history/review scope lacks a link to human scientific acceptance of this revision. Fifteen explicit AI events plus AI-authored release history disclose provenance; the omitted release-event flag and PR link do not establish human sign-off. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### repair-example

In separately authorized curation, reconcile the Natronomonas example with the strict optimum threshold using the cited measured value or a genuinely matching replacement example.

- A retained canonical example satisfies optimum above9 in its documented conditions.
- Keep valid taxonomy and broader haloalkaliphile terminology distinct from this operational class.
- Run focused record/taxon validation and preserve native provenance after any authorized change.

### repair-relations

Reconcile the three grounded predicates with their intended subjects, clarifying motif versus protein bearer and binding activity versus efficiency where needed; review wildcard mapping recurrence.

- Each selected relation’s inherited endpoint roles and meaning agree with the clarified nodes.
- Retain compatible Mrp and material-envelope enables edges; do not reject all molecular-function objects or cellular-component actors.
- The maintained ground-predicates dry run reviews recurrence but does not overwrite existing IDs; correct existing edges through the guarded writer.
- After authorized curation run focused strict/graph checks and just qc, append native history and regenerate affected products.

### clarify-definition-authority

Make the exact pH-optimum convention’s METPO authority explicit while retaining literature support for broader physiology.

- Readers can distinguish the exact operational cutoff from the cited extreme-growth ranges.
- No unsupported numerical boundary or changed ontology identity is introduced.
- Run focused validation after authorized edits.

### scope-mrp

Qualify the Mrp indispensable-role statement to the extremely alkaliphilic Bacillus context supported by the cited passage.

- Node6 and edge5 preserve the source organism scope.
- Do not convert a contextual protein into a universal trait requirement or remove supported physiology.
- Run focused validation after authorized edits.

### link-acceptance

Locate and link existing human scientific acceptance or obtain it through the established process; preserve AI history and reassess status if acceptance remains unavailable.

- Acceptance identifies this record revision and scientific scope.
- Automated checks, AI history and a migration PR link are not represented as human scientific sign-off.

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
| check-alkaphilic-validate | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkaphilic-validate.log; Executed 2026-10-21T08:39:36Z through 2026-10-21T08:39:38Z; metadata alkaphilic-validate.json | context_only | Selected record validates. |
| check-alkaphilic-strict | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkaphilic-strict.log; Executed 2026-10-21T08:39:36Z through 2026-10-21T08:39:39Z; metadata alkaphilic-strict.json | context_only | One file scanned; zero errors. |
| check-alkaphilic-snippets | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkaphilic-snippets.log; Executed 2026-10-21T08:39:39Z through 2026-10-21T08:39:44Z; metadata alkaphilic-snippets.json | context_only | Six snippets across three references: two VERIFIED and four NOT_IN_ABSTRACT. Abstract misses are inconclusive; manual source assessment is recorded separately. |
| record | data/traits/environment/alkaphilic.yaml; Entire record: identity, three synonyms, two examples, eleven nodes, ten edges and seventeen events | partial | The active alkaliphilic identity is correct. The Natronomonas example conflicts with the strict optimum threshold; three relations mismatch their endpoint roles. Source context and acceptance provenance need bounded clarification. |
| shape | Whole graph/history inspection; All eleven nodes and ten edge endpoints; seventeen events | supports | All endpoints resolve. Fifteen events explicitly disclose AI assistance, the seed is false, and the release event omits that flag; its repository history independently identifies an AI actor. No pathway-context link is asserted. |
| identity | data/raw/metpo.owl; reports/ontology_snapshot_manifest.tsv; pH-growth parent; Active1003002, parent1003000 and all exact synonyms | supports | The above9 optimum definition and exact alkaliphile, alkalophile and alkalophilic synonyms match the locked METPO2026-06-12 bytes. The parent is strictly broader. |
| migration | scripts/migrate_metpo_2026_06_12.py; history/infrastructure/metpo-2026-06-12-migration/2026-08-26T075914Z-codex-cf43c0.yaml; Guarded source-owned label migration and repository AI-agent event | supports | The migration deliberately preserves filenames and graph/node IDs while updating the label and ontology-owned synonyms. The old alkaphilic filename is not evidence of wrong identity. Its AI-agent history is not human scientific acceptance. |
| live-identifiers | ChEBI and NCBI Taxonomy; CHEBI29101 and taxon2257 official responses08:40:46–47Z | supports | Sodium(1+) and Natronomonas pharaonis resolve to the recorded meanings; valid taxonomy does not validate the strict optimum criterion. |
| reused-identifiers | Official QuickGO, ChEBI and NCBI responses; GO0051453 original07:58:24Z; CHEBI15378 original07:58:25Z; taxon86665 original08:34:20Z | supports | Intracellular-pH regulation, proton/hydron and current Halalkalibacterium halodurans identity match. Reuse preserves original retrieval times and verified body hashes. |
| ro-pato | Read-only RO and PATO snapshots; Inherited RO2327/2326 material-subject and RO2213 process-subject constraints; alkaline quality | partial | Original RO inspections07:58:06/08:04:46Z and PATO08:34:09Z are reused with unchanged authority hashes. Motif features are not a regulating process; binding activity/efficiency and surface retention are not material enables/contributes actors. PATO alkaline matches. |
| policy | docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml; Contextual scope, allowed protein facets and CELLULAR_LOCALIZATION | supports | Reviewed label-only proteins are permitted here. CELLULAR_LOCALIZATION includes material cellular components, so the envelope components can enable retention. Optional protein accessions and datasets are not required merely because the title says mechanism. |
| provenance | Target and bounded local history/mapping/writer/review search; Seventeen events and ignored-inclusive identifier/path/old-and-current-label matches | partial | The inspected local provenance does not link human scientific acceptance of this revision. Repository release history explicitly names AI involvement despite an omitted per-record flag. A release PR link is not by itself scientific sign-off; remote/private approvals remain unknown. |
| status-rule | .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md; Status/audit and verification gate | supports | REVIEWED requires human scientific acceptance; validation and AI provenance remain distinct. |
| expression | https://imodulondb.org/api/datasets; Hash-verified original07:36:12Z catalog; current canonical-taxon applicability assessment | context_only | Neither Halalkalibacterium halodurans nor Natronomonas pharaonis matches the inspected catalog. No B. subtilis substitution or gene/module query followed; noncoverage is not negative biology. |
| runner | Reused structured-source runner discovery; Original bounded ignored-inclusive08:17:15Z discovery | context_only | The runner was unavailable within the original declared scope. The original receipt and official-catalog fallback are retained; no fresh or global filesystem-absence claim is made. |
| ledger | Independent ontology node/edge ledger; All eleven nodes and ten edges, zero-based indices | partial | Confirmed role conflicts at edges6,7,9. Material Mrp and cell-envelope components are compatible enables actors. Motif/bearer and binding-activity/efficiency wording should be clarified during repair without inventing a mandatory replacement enum. |
| owners | mappings/predicate_grounding.tsv; scripts/ground_causal_predicates.py; local proposal tables; Wildcard increases/enables/contributes-to; provisional selects-for/challenges/confers/imports | partial | The wildcard mappings could refill emptied IDs with the same mismatches; the writer skips existing nonempty IDs. The current local proposal meanings fit endpoint roles. Protein feature wording remains a record-level precision issue, not a missing arbitrary accession. |
| bibliography | Primary-source citation and claim ledger; Six references, ten edge claims and six excerpts | partial | All six cited identities resolve. Three excerpts are exact, two use harmless dash normalization and one is faithfully ellipsized. Ten new acquisition attempts include seven hashed responses, with failed/error surfaces excluded; six reused files retain original receipts. |
| krulwich | https://doi.org/10.1038/nrmicro2549; BioC Extreme alkaliphiles39253, Mrp40107, ATP42119/43296, Fig4caption67131, Glossary45575/45597; publisher Key Points3 | partial | Supports alkaline growth/homeostasis and Bacillus-centered contextual mechanisms. The glossary and extreme-growth passages do not directly define the precise optimum-above9 convention. Mrp indispensability is scoped to extremely alkaliphilic Bacillus. ATP binding-site explanation is proposed in the body and expressed more directly in Fig4; both formulations are retained. Growth-range evidence alone does not demonstrate evolutionary selection. |
| publisher-quotes | https://www.nature.com/articles/nrmicro2549; Original publisher preview07:56:36Z; Key Points paragraph3 and abstract | supports | Two repeated range snippets differ only by dash typography, the pH-control excerpt marks its omission explicitly, and the homeostasis phrase is exact. These are supported excerpts without a false-quote finding. The original PDF endpoint yielded HTML preview, correctly classified here. |
| halodurans | https://oup.silverchair-cdn.com/article-minimal/2376264; DOI10.1093/nar/28.21.4317; Introduction paragraphs1–2 and General features paragraph1 | supports | The C-125/JCM9153 genome paper supports the alkaliphilic high-pH growth example. Its historical Bacillus name corresponds to the current recorded species. The evidence remains strain-scoped. |
| natronomonas | https://pmc.ncbi.nlm.nih.gov/articles/PMC1240075/; PMID16169924, DOI10.1101/gr.3952905; successful actual journal browser Introduction line114, identity35/107, type strain124 | refutes | The cited paper reports optimum pH8.5 for N. pharaonis, below the record’s strict above9 threshold. Haloalkaliphilic terminology and isolation near pH11 do not override that measured optimum. Browser access succeeded by08:41:41Z despite other failed/challenge requests; no local body hash is fabricated. |
| sodium-cycle | https://doi.org/10.1007/BF00762685; Complete indexed abstract and publisher abstract preview; PMID2687260 | supports | The exact antiporter excerpt and contextual exchanger role are supported for extreme aerobic nonmarine bacilli. The source does not establish identical sodium-cycle architecture in all bacterial and archaeal alkaliphiles; body text was subscription-limited. |
| padan | https://doi.org/10.1016/j.bbamem.2005.09.010; Original complete abstract08:33:34Z; adaptation sentence | partial | The proton-capture/retention excerpt is exact and broad antiporter context is supported. The short nearest excerpt is less specific than electrogenic import direction; other already-cited sodium-cycle and Krulwich text corroborates that direction, without replacing the nearest source silently. |
| surface | https://pmc.ncbi.nlm.nih.gov/articles/PMC8992544/; DOI10.3389/fmicb.2022.842785; Introduction SecS1 paragraph3 | supports | The passage discusses acidic surface components, proton attraction/retention and local protection, with Bacillaceae examples and variation among strains. S-layer interpretation is qualified. It supports contextual biological contributions without establishing one universal surface mechanism. |

## Limits And Additional Notes

- The Natronomonas journal body was successfully inspected through an actual browser open by08:41:41Z; other requests returned challenge/error pages. No local hash is fabricated for that browser-only text. The author dissertation is corroboration, not the sole basis.
- The Padan and1989 sodium-cycle sources were assessed from complete indexed abstracts and publisher previews. Their body text was not available.
- The exact optimum cutoff is verified in METPO; the literature-attribution observation is bounded to the inspected glossary/extreme-alkaliphile passages, not an asserted exhaustive absence from the whole paper.
- Evolutionary selection at edge0 remains a contextual inference from adaptation/growth discussion, not direct experimental selection evidence from the short range snippet.
- Mrp necessity and ATP adaptation evidence are Bacillus-centered. The ATP body’s proposed affinity explanation and more direct figure-caption wording are both retained; neither alone supports a claim of false chemistry.
- Cell-envelope sources preserve Bacillaceae variation and qualified S-layer interpretation; no universal surface composition or mechanism is inferred.
- Motif/protein-bearer and activity/efficiency distinctions remain bounded wording questions; relation conflicts do not depend on inventing a replacement enum or arbitrary protein accession.
- RO/PATO/GO/CHEBI, primary-text and catalog reuse retain original timestamps/hashes. Current reinspection is not a new external ontology release check.
- Neither canonical taxon matches the inspected expression catalog. No substitute organism or negative biological inference followed.
- Private or remote human acceptance remains unknown outside the bounded local search.
- The existing provider report was used only as provenance/leads; no paid call or automatic conversion of its recommendations occurred.
- No scientific record, schema, mapping, writer, status, history or generated page was changed.
- Field indices are zero-based.
- Initial native capture08:39:13–15Z retained54inputs; supplemental locked-manifest capture08:40:37–39Z retainedall54unchanged and addedone input.
- The historical filename alkaphilic.yaml and node ID are explicitly preserved by the source migration; the reviewed label is alkaliphilic.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T084513Z-alkaliphilic
kind: record
repository: CultureBotAI/TraitMech
title: Evidence and ontology review of alkaliphily (METPO:1003002)
started_at: '2026-10-21T08:39:13Z'
finished_at: '2026-10-21T08:45:13Z'
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
summary: The alkaliphilic record has the correct current METPO identity, synonyms
  and parent. Two major findings concern the cited Natronomonas optimum8.5 versus
  the strict above9 definition, and three RO relations with incompatible subject roles.
  Three minor findings concern numerical-definition attribution, Mrp organism scope
  and a bounded missing human-acceptance link. All eleven nodes and ten edges were
  assessed; all six excerpts are supported with explicit typography/ellipsis distinctions.
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
  - path: data/traits/environment/alkaphilic.yaml
    sha256: 9dd8c1ed07700d7960f64e7539118441a563cd71fe78b22d39ee70b058b0fa65
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
  - path: history/infrastructure/metpo-2026-06-12-migration/2026-08-26T075914Z-codex-cf43c0.yaml
    sha256: 8fed746ed8287d41ccd98157d20d58bc22e06ce72ae22dc2e521997f4c040968
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
  - path: research/traits/environment/alkaphilic-deep-research-falcon.md
    sha256: a0d748c9153accca56f4603846f603906cd5fc136e0de345f55157b777025f0f
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
  - path: scripts/migrate_metpo_2026_06_12.py
    sha256: 0f3945e7b8e6ddccdc9eaeed32737a2a1cf0832748af2b72a6a0195ba661188f
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
- target_id: METPO:1003002
  path: data/traits/environment/alkaphilic.yaml
  label: alkaliphilic
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkaphilic.yaml
    role: Maintained TraitRecord; scientific changes require guarded curation
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Original METPO import identity/provenance
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Fourth batch004 target in lexicographic path order. Entire target read
    before initial native capture; supplemental release-manifest capture retained
    all previous input hashes. Historical filename is preserved by the documented
    ontology migration.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1003002
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1003002
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
  - METPO:1003002
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
  - METPO:1003002
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
  - METPO:1003002
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
  - METPO:1003002
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
  - METPO:1003002
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
  - METPO:1003002
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
- check_id: alkaphilic-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1003002
  command: just validate data/traits/environment/alkaphilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Selected record validates.
  evidence_ids:
  - check-alkaphilic-validate
- check_id: alkaphilic-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1003002
  command: just validate-strict data/traits/environment/alkaphilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: One file scanned; zero errors.
  evidence_ids:
  - check-alkaphilic-strict
- check_id: alkaphilic-snippets
  name: Focused source snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1003002
  command: just verify-snippets --record data/traits/environment/alkaphilic.yaml --out
    /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkaphilic-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Six snippets across three references: two VERIFIED and four NOT_IN_ABSTRACT.
    Abstract misses are inconclusive; manual source assessment is recorded separately.'
  evidence_ids:
  - check-alkaphilic-snippets
- check_id: structured-source-runner
  name: Structured-source runner discovery
  status: unavailable
  required: false
  target_ids:
  - METPO:1003002
  summary: Reused bounded discovery; official catalog fallback inspected.
  evidence_ids:
  - runner
- check_id: expression-context
  name: Canonical-taxon expression applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1003002
  summary: No matching dataset in the inspected catalog.
  evidence_ids:
  - expression
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T08:45:13Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T08:45:13Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T08:45:13Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T08:45:13Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T08:45:13Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T08:45:13Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T08:45:13Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-alkaphilic-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkaphilic-validate.log
  locator: Executed 2026-10-21T08:39:36Z through 2026-10-21T08:39:38Z; metadata alkaphilic-validate.json
  accessed_at: '2026-10-21T08:45:13Z'
  support: context_only
  summary: Selected record validates.
  snapshot_sha256: 1f664d76ea0d9d46e9091ae129e9a9dba63214d8eb9e93a8073e6ee6757df2ab
- evidence_id: check-alkaphilic-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkaphilic-strict.log
  locator: Executed 2026-10-21T08:39:36Z through 2026-10-21T08:39:39Z; metadata alkaphilic-strict.json
  accessed_at: '2026-10-21T08:45:13Z'
  support: context_only
  summary: One file scanned; zero errors.
  snapshot_sha256: 2acae5aad170d5a6d10e25f61aca8c5a54652c3d8548274847fcb4684a740892
- evidence_id: check-alkaphilic-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/alkaphilic-snippets.log
  locator: Executed 2026-10-21T08:39:39Z through 2026-10-21T08:39:44Z; metadata alkaphilic-snippets.json
  accessed_at: '2026-10-21T08:45:13Z'
  support: context_only
  summary: 'Six snippets across three references: two VERIFIED and four NOT_IN_ABSTRACT.
    Abstract misses are inconclusive; manual source assessment is recorded separately.'
  snapshot_sha256: 292b65f173d6115f9e76d4378282f4fd053a6aef9f964dac3026149b94514948
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/alkaphilic.yaml
  locator: 'Entire record: identity, three synonyms, two examples, eleven nodes, ten
    edges and seventeen events'
  accessed_at: '2026-10-21T08:45:13Z'
  support: partial
  summary: The active alkaliphilic identity is correct. The Natronomonas example conflicts
    with the strict optimum threshold; three relations mismatch their endpoint roles.
    Source context and acceptance provenance need bounded clarification.
  snapshot_sha256: 9dd8c1ed07700d7960f64e7539118441a563cd71fe78b22d39ee70b058b0fa65
- evidence_id: shape
  kind: validation
  reference: Whole graph/history inspection
  locator: All eleven nodes and ten edge endpoints; seventeen events
  accessed_at: '2026-10-21T08:40:12Z'
  support: supports
  summary: All endpoints resolve. Fifteen events explicitly disclose AI assistance,
    the seed is false, and the release event omits that flag; its repository history
    independently identifies an AI actor. No pathway-context link is asserted.
  snapshot_sha256: 674854279fd9676f8e2a42768eb45c76423b9cae2b3718d47262d72f387dc65b
- evidence_id: identity
  kind: authority
  reference: data/raw/metpo.owl; reports/ontology_snapshot_manifest.tsv; pH-growth
    parent
  locator: Active1003002, parent1003000 and all exact synonyms
  accessed_at: '2026-10-21T08:40:35Z'
  support: supports
  summary: The above9 optimum definition and exact alkaliphile, alkalophile and alkalophilic
    synonyms match the locked METPO2026-06-12 bytes. The parent is strictly broader.
  snapshot_sha256: 7eb64660b8d39ad90a2438f9af767ba51ae3a72eb86f08e1ce0110f1904d1809
- evidence_id: migration
  kind: record_content
  reference: scripts/migrate_metpo_2026_06_12.py; history/infrastructure/metpo-2026-06-12-migration/2026-08-26T075914Z-codex-cf43c0.yaml
  locator: Guarded source-owned label migration and repository AI-agent event
  accessed_at: '2026-10-21T08:45:13Z'
  support: supports
  summary: The migration deliberately preserves filenames and graph/node IDs while
    updating the label and ontology-owned synonyms. The old alkaphilic filename is
    not evidence of wrong identity. Its AI-agent history is not human scientific acceptance.
  snapshot_sha256: 8fed746ed8287d41ccd98157d20d58bc22e06ce72ae22dc2e521997f4c040968
- evidence_id: live-identifiers
  kind: authority
  reference: ChEBI and NCBI Taxonomy
  locator: CHEBI29101 and taxon2257 official responses08:40:46–47Z
  accessed_at: '2026-10-21T08:40:47Z'
  support: supports
  summary: Sodium(1+) and Natronomonas pharaonis resolve to the recorded meanings;
    valid taxonomy does not validate the strict optimum criterion.
  snapshot_sha256: cd74fb4e40a1fd459e85d6e77978131e4a2744e8d737b226a6c9a75acbe6d5c0
- evidence_id: reused-identifiers
  kind: authority
  reference: Official QuickGO, ChEBI and NCBI responses
  locator: GO0051453 original07:58:24Z; CHEBI15378 original07:58:25Z; taxon86665 original08:34:20Z
  accessed_at: '2026-10-21T08:40:35Z'
  support: supports
  summary: Intracellular-pH regulation, proton/hydron and current Halalkalibacterium
    halodurans identity match. Reuse preserves original retrieval times and verified
    body hashes.
  snapshot_sha256: bd70c12516f3cadf2fb0247fcbebd896c0eda823abfdbd7d7c1104e9f2b79e9e
- evidence_id: ro-pato
  kind: authority
  reference: Read-only RO and PATO snapshots
  locator: Inherited RO2327/2326 material-subject and RO2213 process-subject constraints;
    alkaline quality
  accessed_at: '2026-10-21T08:40:35Z'
  support: partial
  summary: Original RO inspections07:58:06/08:04:46Z and PATO08:34:09Z are reused
    with unchanged authority hashes. Motif features are not a regulating process;
    binding activity/efficiency and surface retention are not material enables/contributes
    actors. PATO alkaline matches.
  snapshot_sha256: 0bdb894a9af95e78d52a76234dee32a814828fae9df2215558b98ceeb4cf787b
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md; src/traitmech/schema/traitmech.yaml
  locator: Contextual scope, allowed protein facets and CELLULAR_LOCALIZATION
  accessed_at: '2026-10-21T08:45:13Z'
  support: supports
  summary: Reviewed label-only proteins are permitted here. CELLULAR_LOCALIZATION
    includes material cellular components, so the envelope components can enable retention.
    Optional protein accessions and datasets are not required merely because the title
    says mechanism.
- evidence_id: provenance
  kind: search
  reference: Target and bounded local history/mapping/writer/review search
  locator: Seventeen events and ignored-inclusive identifier/path/old-and-current-label
    matches
  accessed_at: '2026-10-21T08:40:12Z'
  support: partial
  summary: The inspected local provenance does not link human scientific acceptance
    of this revision. Repository release history explicitly names AI involvement despite
    an omitted per-record flag. A release PR link is not by itself scientific sign-off;
    remote/private approvals remain unknown.
  snapshot_sha256: 960b28cc5dac3e3ec2a2e2d11af2c44b1e30ccafdb508988f47ba75b6195c145
  search_scope: rg --no-ignore --hidden over history,mappings,scripts,reviews/structured
    for METPO1003002, exact path and historical/current labels; original command and1107matching
    lines retained. Remote/private acceptance was not searched.
- evidence_id: status-rule
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md; docs/CURATION_PLAYBOOK.md
  locator: Status/audit and verification gate
  accessed_at: '2026-10-21T08:45:13Z'
  support: supports
  summary: REVIEWED requires human scientific acceptance; validation and AI provenance
    remain distinct.
- evidence_id: expression
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Hash-verified original07:36:12Z catalog; current canonical-taxon applicability
    assessment
  accessed_at: '2026-10-21T08:45:13Z'
  support: context_only
  summary: Neither Halalkalibacterium halodurans nor Natronomonas pharaonis matches
    the inspected catalog. No B. subtilis substitution or gene/module query followed;
    noncoverage is not negative biology.
  snapshot_sha256: 1e88db1742fc852b80b36af771cfe2f329d78e22d7f936f299821bc948af57fe
- evidence_id: runner
  kind: search
  reference: Reused structured-source runner discovery
  locator: Original bounded ignored-inclusive08:17:15Z discovery
  accessed_at: '2026-10-21T08:17:15Z'
  support: context_only
  summary: The runner was unavailable within the original declared scope. The original
    receipt and official-catalog fallback are retained; no fresh or global filesystem-absence
    claim is made.
  snapshot_sha256: 39b52930f52e898f85ac3bbb88f11ac674a355967b5704e2b62f0bda259d404f
  search_scope: Exact original PATH/project/install/B4 bounds are in runner-discovery.json;
    ignored files were included; unsearched directories remain unknown.
- evidence_id: ledger
  kind: validation
  reference: Independent ontology node/edge ledger
  locator: All eleven nodes and ten edges, zero-based indices
  accessed_at: '2026-10-21T08:42:34Z'
  support: partial
  summary: Confirmed role conflicts at edges6,7,9. Material Mrp and cell-envelope
    components are compatible enables actors. Motif/bearer and binding-activity/efficiency
    wording should be clarified during repair without inventing a mandatory replacement
    enum.
  snapshot_sha256: e485bd936d57a045215da543f79762002b70e3ebb1f7d1bd718ec137ede083a1
- evidence_id: owners
  kind: record_content
  reference: mappings/predicate_grounding.tsv; scripts/ground_causal_predicates.py;
    local proposal tables
  locator: Wildcard increases/enables/contributes-to; provisional selects-for/challenges/confers/imports
  accessed_at: '2026-10-21T08:42:34Z'
  support: partial
  summary: The wildcard mappings could refill emptied IDs with the same mismatches;
    the writer skips existing nonempty IDs. The current local proposal meanings fit
    endpoint roles. Protein feature wording remains a record-level precision issue,
    not a missing arbitrary accession.
  snapshot_sha256: cf843ac57c5bd2584a807ed895b453368fd967a93617702960e3fe874aa90b7f
- evidence_id: bibliography
  kind: database
  reference: Primary-source citation and claim ledger
  locator: Six references, ten edge claims and six excerpts
  accessed_at: '2026-10-21T08:43:12Z'
  support: partial
  summary: All six cited identities resolve. Three excerpts are exact, two use harmless
    dash normalization and one is faithfully ellipsized. Ten new acquisition attempts
    include seven hashed responses, with failed/error surfaces excluded; six reused
    files retain original receipts.
  snapshot_sha256: 6b4efb8729bf55a12b3bd00640777a18bb93f17003c2e9263bb886553c5cf69f
- evidence_id: krulwich
  kind: primary_source
  reference: https://doi.org/10.1038/nrmicro2549
  locator: BioC Extreme alkaliphiles39253, Mrp40107, ATP42119/43296, Fig4caption67131,
    Glossary45575/45597; publisher Key Points3
  accessed_at: '2026-10-21T07:57:33Z'
  support: partial
  summary: Supports alkaline growth/homeostasis and Bacillus-centered contextual mechanisms.
    The glossary and extreme-growth passages do not directly define the precise optimum-above9
    convention. Mrp indispensability is scoped to extremely alkaliphilic Bacillus.
    ATP binding-site explanation is proposed in the body and expressed more directly
    in Fig4; both formulations are retained. Growth-range evidence alone does not
    demonstrate evolutionary selection.
  snapshot_sha256: 903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f
- evidence_id: publisher-quotes
  kind: primary_source
  reference: https://www.nature.com/articles/nrmicro2549
  locator: Original publisher preview07:56:36Z; Key Points paragraph3 and abstract
  accessed_at: '2026-10-21T07:56:36Z'
  support: supports
  summary: Two repeated range snippets differ only by dash typography, the pH-control
    excerpt marks its omission explicitly, and the homeostasis phrase is exact. These
    are supported excerpts without a false-quote finding. The original PDF endpoint
    yielded HTML preview, correctly classified here.
  snapshot_sha256: 4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66
- evidence_id: halodurans
  kind: primary_source
  reference: https://oup.silverchair-cdn.com/article-minimal/2376264
  locator: DOI10.1093/nar/28.21.4317; Introduction paragraphs1–2 and General features
    paragraph1
  accessed_at: '2026-10-21T08:36:09Z'
  support: supports
  summary: The C-125/JCM9153 genome paper supports the alkaliphilic high-pH growth
    example. Its historical Bacillus name corresponds to the current recorded species.
    The evidence remains strain-scoped.
  snapshot_sha256: 9ec63b1769da9c25e9c8838a2698819c9d038509f85412e83dab45ebedb0600e
- evidence_id: natronomonas
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1240075/
  locator: PMID16169924, DOI10.1101/gr.3952905; successful actual journal browser
    Introduction line114, identity35/107, type strain124
  accessed_at: '2026-10-21T08:41:41Z'
  support: refutes
  summary: The cited paper reports optimum pH8.5 for N. pharaonis, below the record’s
    strict above9 threshold. Haloalkaliphilic terminology and isolation near pH11
    do not override that measured optimum. Browser access succeeded by08:41:41Z despite
    other failed/challenge requests; no local body hash is fabricated.
- evidence_id: sodium-cycle
  kind: primary_source
  reference: https://doi.org/10.1007/BF00762685
  locator: Complete indexed abstract and publisher abstract preview; PMID2687260
  accessed_at: '2026-10-21T08:39:49Z'
  support: supports
  summary: The exact antiporter excerpt and contextual exchanger role are supported
    for extreme aerobic nonmarine bacilli. The source does not establish identical
    sodium-cycle architecture in all bacterial and archaeal alkaliphiles; body text
    was subscription-limited.
  snapshot_sha256: 7d7c4d3953d91a502200be332114dfd2094efc4cd298f15a041f144a4690c8c3
- evidence_id: padan
  kind: primary_source
  reference: https://doi.org/10.1016/j.bbamem.2005.09.010
  locator: Original complete abstract08:33:34Z; adaptation sentence
  accessed_at: '2026-10-21T08:33:34Z'
  support: partial
  summary: The proton-capture/retention excerpt is exact and broad antiporter context
    is supported. The short nearest excerpt is less specific than electrogenic import
    direction; other already-cited sodium-cycle and Krulwich text corroborates that
    direction, without replacing the nearest source silently.
  snapshot_sha256: aaeca721aa72bd6bf7652b6c9540c4249317490bac744a2ccf90c7ba2b1f2027
- evidence_id: surface
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8992544/
  locator: DOI10.3389/fmicb.2022.842785; Introduction SecS1 paragraph3
  accessed_at: '2026-10-21T08:39:59Z'
  support: supports
  summary: The passage discusses acidic surface components, proton attraction/retention
    and local protection, with Bacillaceae examples and variation among strains. S-layer
    interpretation is qualified. It supports contextual biological contributions without
    establishing one universal surface mechanism.
  snapshot_sha256: 213c93b570bbe530b62afa307fa2b0b12fd46c0bf5d1ebb864dbbc8c2fa0c6a2
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: current concept, synonyms and hierarchy'
  outcome: supported
  target_ids:
  - METPO:1003002
  summary: Active METPO1003002, three exact synonyms and broader1003000 match. The
    historical filename/node ID is deliberately preserved by migration, not a wrong
    current concept.
  evidence_ids:
  - identity
  - migration
  - record
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: exact optimum convention and nearest literature'
  outcome: concern
  target_ids:
  - METPO:1003002
  summary: The exact above9 optimum is directly supported by METPO. Inspected Krulwich
    glossary/extreme-growth passages provide broader pH context rather than that precise
    class convention; make the authority explicit.
  evidence_ids:
  - identity
  - krulwich
  - publisher-quotes
- assessment_id: model
  area: representation
  topic: 'Native checklist: ENVIRONMENT/CLASS and contextual graph'
  outcome: supported
  target_ids:
  - METPO:1003002
  summary: Category and contextual NONMECHANISTIC scope fit. The graph title, reviewed
    label-only proteins and optional evidence surfaces do not independently require
    scope promotion or token accessions.
  evidence_ids:
  - record
  - policy
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: both canonical organisms and phenotype scope'
  outcome: concern
  target_ids:
  - METPO:1003002
  summary: Both current taxon identities resolve. Halodurans has appropriate high-pH
    growth support; the cited Natronomonas optimum8.5 conflicts with the strict class
    criterion despite legitimate broader haloalkaliphile terminology.
  evidence_ids:
  - live-identifiers
  - reused-identifiers
  - halodurans
  - natronomonas
  - identity
- assessment_id: grounding
  area: grounding
  topic: 'Native checklist: current node identities and historical corrections'
  outcome: supported
  target_ids:
  - METPO:1003002
  summary: Current METPO/GO/PATO/CHEBI and taxonomy are coherent. Historical dead
    accessions, acidic PATO, replaced GO and microbe-domain imports were corrected
    or retracted and are not present defects.
  evidence_ids:
  - identity
  - live-identifiers
  - reused-identifiers
  - ro-pato
  - ledger
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: eleven nodes and ten edge roles'
  outcome: concern
  target_ids:
  - METPO:1003002
  summary: Edges6,7,9 use relations requiring roles their subjects do not denote.
    Protein/feature versus bearer and binding activity versus efficiency should be
    clarified during repair. Material components at edge8 remain compatible.
  evidence_ids:
  - ledger
  - ro-pato
  - owners
  - policy
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: all edge sources and six excerpts'
  outcome: concern
  target_ids:
  - METPO:1003002
  summary: All excerpts are supported at exact, typographic or explicit-ellipsis level.
    Mrp necessity needs its source’s Bacillus scope. ATP body/caption certainty is
    retained; selection remains a contextual inference. Generic contributions are
    not proof of a universal mechanism.
  evidence_ids:
  - bibliography
  - krulwich
  - publisher-quotes
  - sodium-cycle
  - padan
  - surface
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: required structure and optional surfaces'
  outcome: supported
  target_ids:
  - METPO:1003002
  summary: All endpoints resolve and required identity/evidence surfaces are present.
    Contextual scope does not demand one protein instance per label, datasets, or
    a uniquely necessary pathway.
  evidence_ids:
  - shape
  - record
  - policy
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: canonical-taxon database applicability'
  outcome: supported
  target_ids:
  - METPO:1003002
  summary: Neither canonical taxon matches the inspected catalog; no substitute species
    or negative phenotype inference was used.
  evidence_ids:
  - expression
  - runner
- assessment_id: audit
  area: provenance
  topic: 'Native checklist: AI disclosure, human acceptance and recurrence owners'
  outcome: concern
  target_ids:
  - METPO:1003002
  summary: Fifteen events explicitly disclose AI assistance and the release history
    separately identifies its AI actor. No human acceptance is linked in bounded local
    provenance. Mapping recurrence and correction of existing IDs are distinct.
  evidence_ids:
  - provenance
  - status-rule
  - migration
  - owners
findings:
- finding_id: canonical-optimum-mismatch
  issue_key: alkaliphilic-canonical-optimum-mismatch
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Natronomonas example falls below the defined optimum threshold
  description: The nearest cited journal paper explicitly reports optimum pH8.5, while
    this record requires an optimum above9. Its haloalkaliphilic designation and high-pH
    isolation environment do not establish that strict class membership. This concerns
    the cited organism/conditions and operational boundary, not invalid taxonomy or
    denial of broader haloalkaliphile terminology.
  target_ids:
  - METPO:1003002
  field_paths:
  - canonical_examples[1]
  evidence_ids:
  - natronomonas
  - identity
  - live-identifiers
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkaphilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: external-relation-semantics
  issue_key: alkaliphilic-external-relation-semantics
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Three grounded relations conflict with their subject roles
  description: Edge6 maps a motif/feature or protein-bearer subject to process regulation;
    edge7 maps binding activity or efficiency to a material enables actor; edge9 maps
    a retention process to a material contributor. These conflicts do not require
    assuming every molecular-function object is invalid. Native validation passes,
    and no failed OWL reasoner run is claimed.
  target_ids:
  - METPO:1003002
  field_paths:
  - causal_graphs[0].edges[6]
  - causal_graphs[0].edges[7]
  - causal_graphs[0].edges[9]
  evidence_ids:
  - ledger
  - ro-pato
  - owners
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkaphilic.yaml
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
- finding_id: definition-cutoff-attribution
  issue_key: alkaliphilic-definition-cutoff-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Attribute the exact optimum cutoff to its defining authority
  description: METPO directly supplies the optimum-above9 convention. The nearest
    inspected Krulwich glossary and extreme-alkaliphile passages discuss growth ranges
    and model physiology rather than stating that exact class definition. Clarify
    authority without changing the correct identity or claiming a whole-article absence
    beyond the inspected passages.
  target_ids:
  - METPO:1003002
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - identity
  - krulwich
  - publisher-quotes
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkaphilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: mrp-organism-scope
  issue_key: alkaliphilic-mrp-organism-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Mrp indispensability needs the cited Bacillus scope
  description: The source’s indispensable-role statement explicitly concerns extremely
    alkaliphilic Bacillus. Node6 and edge5 omit that context in their categorical
    necessity wording. Retain the contextual mechanism while making its organism scope
    explicit; the generic NONMECHANISTIC graph is not itself a universal assertion.
  target_ids:
  - METPO:1003002
  field_paths:
  - causal_graphs[0].nodes[6].description
  - causal_graphs[0].edges[5]
  evidence_ids:
  - krulwich
  - record
  - bibliography
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkaphilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: alkaliphilic-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human scientific acceptance is not linked locally
  description: The inspected local target/history/review scope lacks a link to human
    scientific acceptance of this revision. Fifteen explicit AI events plus AI-authored
    release history disclose provenance; the omitted release-event flag and PR link
    do not establish human sign-off. Private or remote acceptance remains unknown.
  target_ids:
  - METPO:1003002
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - status-rule
  - shape
  - migration
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkaphilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: repair-example
  description: In separately authorized curation, reconcile the Natronomonas example
    with the strict optimum threshold using the cited measured value or a genuinely
    matching replacement example.
  finding_ids:
  - canonical-optimum-mismatch
  target_ids:
  - METPO:1003002
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkaphilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - A retained canonical example satisfies optimum above9 in its documented conditions.
  - Keep valid taxonomy and broader haloalkaliphile terminology distinct from this
    operational class.
  - Run focused record/taxon validation and preserve native provenance after any authorized
    change.
- action_id: repair-relations
  description: Reconcile the three grounded predicates with their intended subjects,
    clarifying motif versus protein bearer and binding activity versus efficiency
    where needed; review wildcard mapping recurrence.
  finding_ids:
  - external-relation-semantics
  target_ids:
  - METPO:1003002
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkaphilic.yaml
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
  - Each selected relation’s inherited endpoint roles and meaning agree with the clarified
    nodes.
  - Retain compatible Mrp and material-envelope enables edges; do not reject all molecular-function
    objects or cellular-component actors.
  - The maintained ground-predicates dry run reviews recurrence but does not overwrite
    existing IDs; correct existing edges through the guarded writer.
  - After authorized curation run focused strict/graph checks and just qc, append
    native history and regenerate affected products.
- action_id: clarify-definition-authority
  description: Make the exact pH-optimum convention’s METPO authority explicit while
    retaining literature support for broader physiology.
  finding_ids:
  - definition-cutoff-attribution
  target_ids:
  - METPO:1003002
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkaphilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Readers can distinguish the exact operational cutoff from the cited extreme-growth
    ranges.
  - No unsupported numerical boundary or changed ontology identity is introduced.
  - Run focused validation after authorized edits.
- action_id: scope-mrp
  description: Qualify the Mrp indispensable-role statement to the extremely alkaliphilic
    Bacillus context supported by the cited passage.
  finding_ids:
  - mrp-organism-scope
  target_ids:
  - METPO:1003002
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkaphilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Node6 and edge5 preserve the source organism scope.
  - Do not convert a contextual protein into a universal trait requirement or remove
    supported physiology.
  - Run focused validation after authorized edits.
- action_id: link-acceptance
  description: Locate and link existing human scientific acceptance or obtain it through
    the established process; preserve AI history and reassess status if acceptance
    remains unavailable.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1003002
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/alkaphilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies this record revision and scientific scope.
  - Automated checks, AI history and a migration PR link are not represented as human
    scientific sign-off.
limitations:
- The Natronomonas journal body was successfully inspected through an actual browser
  open by08:41:41Z; other requests returned challenge/error pages. No local hash is
  fabricated for that browser-only text. The author dissertation is corroboration,
  not the sole basis.
- The Padan and1989 sodium-cycle sources were assessed from complete indexed abstracts
  and publisher previews. Their body text was not available.
- The exact optimum cutoff is verified in METPO; the literature-attribution observation
  is bounded to the inspected glossary/extreme-alkaliphile passages, not an asserted
  exhaustive absence from the whole paper.
- Evolutionary selection at edge0 remains a contextual inference from adaptation/growth
  discussion, not direct experimental selection evidence from the short range snippet.
- Mrp necessity and ATP adaptation evidence are Bacillus-centered. The ATP body’s
  proposed affinity explanation and more direct figure-caption wording are both retained;
  neither alone supports a claim of false chemistry.
- Cell-envelope sources preserve Bacillaceae variation and qualified S-layer interpretation;
  no universal surface composition or mechanism is inferred.
- Motif/protein-bearer and activity/efficiency distinctions remain bounded wording
  questions; relation conflicts do not depend on inventing a replacement enum or arbitrary
  protein accession.
- RO/PATO/GO/CHEBI, primary-text and catalog reuse retain original timestamps/hashes.
  Current reinspection is not a new external ontology release check.
- Neither canonical taxon matches the inspected expression catalog. No substitute
  organism or negative biological inference followed.
- Private or remote human acceptance remains unknown outside the bounded local search.
- The existing provider report was used only as provenance/leads; no paid call or
  automatic conversion of its recommendations occurred.
- No scientific record, schema, mapping, writer, status, history or generated page
  was changed.
notes:
- Field indices are zero-based.
- Initial native capture08:39:13–15Z retained54inputs; supplemental locked-manifest
  capture08:40:37–39Z retainedall54unchanged and addedone input.
- The historical filename alkaphilic.yaml and node ID are explicitly preserved by
  the source migration; the reviewed label is alkaliphilic.
tags:
- record-review
- alkaliphilic
- environment
- needs-curation
```
