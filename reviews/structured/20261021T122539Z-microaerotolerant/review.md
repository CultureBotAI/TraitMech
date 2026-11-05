# Whole-record review of microaerotolerant

- Review: 20261021T122539Z-microaerotolerant
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T12:14:15.209527Z
- Finished UTC: 2026-10-21T12:25:39Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Pass with limitations. Exact active identity and its explicit obsolete precursor replacement, general definition context, canonical species/type-strain classification and documentary node/predicate roles are supported. One minor finding concerns bounded human-acceptance attribution; no major or source-only finding is assigned. All thirteen nodes, eleven edges and fifteen citation placements are covered at the declared scope. Four excerpts are exact and three remain unverified. Detailed defense, host selection, fitness and numerical conditions remain unassessed.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Third record in the seventh path-ordered batch. The entire maintained TraitRecord, parent and captured canonical-example history were read. All 61 captured inputs, thirteen nodes, eleven edges, three components, three protein classes, one canonical example, seven external works, fifteen citation placements, seven snippets and fifteen history events are accounted for. Exact identity, general classification, canonical phenotype, documentary source identity and endpoint roles are assessed. Detailed pathogen-linked defense, colonization, fitness and selection biology and numeric conditions remain UNASSESSED_SCOPE. The captured provider report is a lead only; no biological mechanism, intervention or optimization is supplied.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000610 | data/traits/environment/microaerotolerant.yaml | maintained | microaerotolerant |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000610 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000610 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000610 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1000610 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000610 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000610 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000610 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native record validation | passed | True | METPO:1000610 | Actual execution at 12:14:33–12:14:34 UTC passed. Structural validity does not establish detailed biological correctness. |
| Focused strict validation | passed | True | METPO:1000610 | Actual execution at 12:14:33–12:14:34 UTC passed. Source support and documentary endpoint meanings are assessed separately. |
| Focused native snippet verification | passed | True | METPO:1000610 | Actual execution at 12:14:36–12:14:44 UTC passed. Seven fields yielded three VERIFIED and four NOT_IN_ABSTRACT results. Manual inspection establishes four exact excerpts and leaves three unverified; abstract nonmatches are not false quotations. |
| Reused corpus protein/taxon audit | passed | True | METPO:1000610 | Original batch-four execution at 08:55:04–08:55:10 UTC passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC, one protected, no gaps or errors. Unchanged inputs support reuse, not a fresh focused scientific check. |
| Reused batch-six maintained QC | passed | True | METPO:1000610 | Original just qc passed at 11:54:49–11:57:53 UTC. Qualified batch-seven byte comparisons support reuse; no fresh batch-seven QC execution is claimed. |
| Protein instance metadata applicability | not_applicable | False | METPO:1000610 | Three conceptual protein classes, two explicitly label-only, have zero individual instances or current UniProt accessions. NONMECHANISTIC scope does not require token examples; the historical removed accession is not a current defect. |

## Scientific And Domain Assessments

### Native checklist: exact active concept, parent, synonyms and obsolete precursor

identity: supported. Targets: METPO:1000610.

METPO1000610 is the exact active concept with oxygen-preference parent1000601. The current definition and retained oxygen typography agree with the pinned ontology. Its own-label duplicate synonym was intentionally removed without loss of meaning. Obsolete1000351 has an explicit IAO_0100001 replacement link to1000610, positively documented in the separate addendum.

### Native checklist: definition meaning and general primary classification context

evidence: supported. Targets: METPO:1000610.

The exact pinned definition and Nature keypoint support low-oxygen tolerance without an oxygen requirement. The assigned Bioresource Technology abstract supplies positive mixed-community context. Its exact class-definition phrase remains unverified without the body, so substantive concept support does not certify that nearest quotation.

### Native checklist: precise nearest-source wording

evidence: unknown. Targets: METPO:1000610.

Three occurrences of the assigned Bioresource Technology phrase remain unverified. A redirect-only HTTP200 response and failed publisher access are not article-body evidence. Positive mixed-community context is preserved; no false quotation or false definition is inferred from limited access.

### Native checklist: canonical species, type material and phenotype

evidence: supported. Targets: METPO:1000610.

Official NCBI2303410 and the primary species-description abstract support Simulacricoccus ruber and the MCy10636, DSM106554 and NCCB100651 aliases and microaerotolerant classification. PMID30113300 and the canonical DOI identify the same publication. No additional measured assay, universal species mechanism or detailed growth-condition verification is claimed.

### Native checklist: all thirteen node identities and represented facets

grounding: supported. Targets: METPO:1000610.

Active chemical identities and the permitted GO0050605 functional facet fit current node meanings. The environmental exposures, trait, growth activity, chemical donor class and reviewed label-only protein aggregates are documentarily compatible. Node12 permits an activity/process reading despite its systems label; the external gut environment is not automatically a cellular STATE.

Nodes0–2: trait, exposure and chemical class. Nodes3/7/9: contextual protein classes. Nodes4/12: growth/activity readings. Nodes5/11: external conditions. Nodes6/8/10: chemical identities or role bearers. These documentary facets do not verify detailed biological effects.

### Native checklist: all eleven predicate roles

consistency: supported. Targets: METPO:1000610.

The local mitigates, produces and redox-reduces properties permit the declared endpoint kinds. All remaining phrases are ungrounded text and do not inherit unasserted RO or Biolink restrictions. In particular, enables function of is not RO2327, and creates selection for is not the local grounded selects-for predicate. No formal relation finding is warranted at this scope.

Edges0/1/2/4/5/9/10 have no external predicate ID. Edges3/6/7/8 use three locally defined properties with compatible documentary roles. Source attribution and causal correctness remain separate questions.

### Native checklist: all eleven edge source placements

evidence: supported. Targets: METPO:1000610.

All edge references resolve with explicit access and assessment scope. General classification context in edges0/1/4 is supported at the stated level; nearest literal wording remains qualified. The edge5 precise class attribution is unknown, and detailed biology in edges2/3/6–10 remains UNASSESSED_SCOPE. Documentary coverage is not blanket mechanistic verification.

### Native checklist: detailed defense, host selection and fitness assertions

evidence: unknown. Targets: METPO:1000610.

Detailed pathogen-linked oxidative-defense, donor-dependence, host-colonization, fitness and selection assertions remain UNASSESSED_SCOPE. They are not validated, falsified, repaired or expanded. Literal abstract matches, source identities and permitted node/predicate kinds do not establish these mechanisms.

### Native checklist: all seven snippet fields

evidence: supported. Targets: METPO:1000610.

Four excerpts are exact in the actual canonical abstract, Nature keypoint, Lu abstract and SOD abstract. Three repeated Bioresource Technology occurrences remain unverified without the body. The SOD passage remains correlational; quotation fidelity does not transform it into detailed causal proof.

### Native checklist: intermediate-oxygen attribution and numerical conditions

quantity: unknown. Targets: METPO:1000610.

The precise edge5 CMR class attribution remains unverified because the body was unavailable. Numeric gut conditions and detailed growth or fitness implications are UNASSESSED_SCOPE. No threshold, condition optimization or alternative intervention is supplied, and no title-based contradiction is asserted.

### Native checklist: seven works, eight reference forms and fifteen placements

evidence: supported. Targets: METPO:1000610.

All seven publication identities resolve; the PMID and DOI aliases of the canonical paper are reconciled. Fifteen placements retain their actual inspected surfaces and access limits. Seven fresh status records provide bounded observations only, not exhaustive absence of notices.

### Native checklist: whole-record graph and protein scope

completeness: supported. Targets: METPO:1000610.

All thirteen nodes, eleven edges, three components, three protein classes, seven snippets and fifteen events have documentary coverage. Two reviewed label-only classes and zero instances are permissible in NONMECHANISTIC context. No connector, individual protein example, additional pathway or mechanism completion is required.

### Native checklist: canonical-only expression catalog applicability

evidence: not_applicable. Targets: METPO:1000610.

The canonical species and official type-material aliases have no match in the retained official catalog. No organism substitution or downstream gene/module/stress query was performed. Catalog noncoverage is not negative phenotype evidence or a mandatory-record defect; historical runner bounds remain explicit.

### Native checklist: current maintenance and recurrence

ownership: supported. Targets: METPO:1000610.

Current node/predicate mappings preserve permitted grounds. Retained typography, corrected historic domain annotations and removed dead accession are positive maintenance, not current defects. The captured AI canonical-example event explicitly targets this record. Only human-acceptance attribution remains unresolved.

### Native checklist: REVIEWED status and acceptance attribution

provenance: concern. Targets: METPO:1000610.

Fourteen AI events, one automated seed and the captured target-specific AI repository event do not attribute human scientific acceptance in the bounded ignored-inclusive local search. They are positive maintenance evidence. Private or remote acceptance is unknown, and no global absence claim is made.

### Native checklist: actual focused checks and scoped common reuse

schema: supported. Targets: METPO:1000610.

Focused validation, strict validation and snippet verification passed. Manual quotation review covers all seven fields. Historical B6 QC and common diagnostics retain original dates, failures/retry, baselines and skips. All 61 captured input hashes match; no fresh corpus execution is claimed.

## Findings

### human-acceptance-link: Local provenance does not attribute human scientific acceptance

minor / open / confirmed; issue key: microaerotolerant-human-acceptance-link.

REVIEWED status accompanies fifteen events: fourteen explicit AI maintenance events and one automated seed. The captured repository event explicitly documents the AI-authored canonical-example addition. The inspected ignored-inclusive own-repository provenance does not attribute human scientific acceptance for this target and revision. Positive maintenance is preserved. Private or remote acceptance is unknown; this is not a claim that no human review ever occurred.

## Recommended Actions And Acceptance Checks

### attribute-human-acceptance

Link an existing human scientific acceptance decision or leave attribution unresolved for the curator.

- Acceptance identifies the reviewed revision and scope, including the qualified pass, inaccessible precise source wording and unassessed detailed biological claims. Preserve all fifteen events and the captured canonical-example history.
- Automated seeding, successful checks, AI maintenance and this review do not substitute for human acceptance. Do not presume private or remote decisions absent. Any later scientific changes require separately authorized guarded curation and append-only provenance.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep-007.n_925exy/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-microaerotolerant-validate | /private/tmp/traitmech-record-sweep-007.n_925exy/microaerotolerant-validate.log; Executed 2026-10-21T12:14:33Z through 2026-10-21T12:14:34Z; metadata microaerotolerant-validate.json | context_only | Actual execution at 12:14:33–12:14:34 UTC passed. Structural validity does not establish detailed biological correctness. |
| check-microaerotolerant-strict | /private/tmp/traitmech-record-sweep-007.n_925exy/microaerotolerant-strict.log; Executed 2026-10-21T12:14:33Z through 2026-10-21T12:14:34Z; metadata microaerotolerant-strict.json | context_only | Actual execution at 12:14:33–12:14:34 UTC passed. Source support and documentary endpoint meanings are assessed separately. |
| check-microaerotolerant-snippets | /private/tmp/traitmech-record-sweep-007.n_925exy/microaerotolerant-snippets.log; Executed 2026-10-21T12:14:36Z through 2026-10-21T12:14:44Z; metadata microaerotolerant-snippets.json | context_only | Actual execution at 12:14:36–12:14:44 UTC passed. Seven fields yielded three VERIFIED and four NOT_IN_ABSTRACT results. Manual inspection establishes four exact excerpts and leaves three unverified; abstract nonmatches are not false quotations. |
| check-corpus-protein-taxa | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log; Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json | context_only | Original batch-four execution at 08:55:04–08:55:10 UTC passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC, one protected, no gaps or errors. Unchanged inputs support reuse, not a fresh focused scientific check. |
| check-batch006-qc | /private/tmp/traitmech-record-sweep-006.nq5qngor/batch006-qc.log; Executed 2026-10-21T11:54:49Z through 2026-10-21T11:57:53Z; metadata batch006-qc.json | context_only | Original just qc passed at 11:54:49–11:57:53 UTC. Qualified batch-seven byte comparisons support reuse; no fresh batch-seven QC execution is claimed. |
| capture | Native selected-record capture; 61 inputs; actual inspect 12:14:15.209527–12:14:15.974411 UTC | supports | All captured input hashes match, including the target-specific canonical-example history. Contextual policies, proposals, parent and mappings are not additional review targets. |
| record | data/traits/environment/microaerotolerant.yaml; Entire record, thirteen nodes, eleven edges and fifteen history events | partial | The record is REVIEWED with fourteen AI events and one automated seed. The graph is NONMECHANISTIC, with three conceptual protein classes and no instances. |
| native-policy | Native field-by-field review checklist; Source support, scope, completeness and attributed human acceptance | supports | Full coverage distinguishes positive classification evidence, unavailable exact source wording and unassessed detailed biology. Validation and AI review are not human scientific acceptance. |
| native-types | Native node kind definitions; CausalNodeTypeEnum, protein aggregates and external environmental conditions | supports | Current represented meanings govern type review. Protein classes can include aggregates, environmental conditions need not be cellular states, and contextual activities can have process readings. |
| protein-policy | Maintained grounding policy; Section 2 functional grounds and contextual label-only classes | supports | Taxon-agnostic enzymatic functional grounds are permitted on legacy protein nodes. Optional instances and label-only aggregates are not defects by themselves. |
| reuse | Original B6 to B7 byte comparison; Original verification 11:36:30.388266 UTC | context_only | Trait, history and common-input equality supports scoped historical diagnostics. Execution times are preserved separately from the later comparison. |
| reuse-supplement | Qualified B6 QC reuse proof; Qualified 12:01:47.374200 UTC; original QC 11:54:49–11:57:53 UTC | supports | The all-file and earlier YAML-only history comparisons are distinguished. Original check dates, failures, retries and skips are not recast as fresh execution. |
| identity | Pinned METPO identity and retention assessment; Active METPO1000610 and parent1000601; active-review line118 and release-delta line1286 | supports | Current exact identity, parent and retained oxygen typography agree. Removal of the own-label duplicate synonym preserves meaning. Read the separate positive replacement addendum with this original assessment. |
| metpo-primary | Pinned METPO ontology; Active 1000610, parent1000601 and obsolete1000351 explicit IAO_0100001 | supports | The active term has the exact definition and parent. Obsolete1000351 explicitly points to1000610 through term-replaced-by; this positive fact is not inferred merely from deprecation. |
| replacement-addendum | Explicit obsolete-term replacement qualification; Direct pinned ontology properties, assessed 12:21:24.813986 UTC | supports | The frozen identity assessment omitted the positive explicit IAO_0100001 link from obsolete1000351 to active1000610. This addendum supplies that fact without rewriting the original ledger or changing current identity. |
| db-go0050605 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0050605; Actual official response 2026-10-21T12:14:51.493637+00:00 through 2026-10-21T12:14:52.148488+00:00 | supports | The active molecular-function identity matches the permitted enzymatic facet. It does not identify a gene isoform, canonical strain or detailed defense route. |
| db-chebi18421 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18421; Actual official response 2026-10-21T12:14:51.494020+00:00 through 2026-10-21T12:14:52.400144+00:00 | supports | The active superoxide identity and radical-anion charge match the stated chemical meaning. No detailed biological claim follows from chemical identity. |
| db-taxon2303410 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2303410&amp;retmode=xml; Actual official response 2026-10-21T12:14:51.494124+00:00 through 2026-10-21T12:14:51.775151+00:00 | supports | The official species identity and MCy10636, DSM106554 and NCCB100651 type-material aliases match the canonical example. |
| db-chebi16240 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16240; Reused official response 2026-10-21T12:08:35.958139+00:00 through 2026-10-21T12:08:38.989724+00:00 | supports | The active chemical identity matches the assigned label. Original acquisition and later byte verification are distinct; chemical identity does not validate a biological mechanism. |
| db-chebi26523 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26523; Reused official response 2026-10-21T12:08:35.989739+00:00 through 2026-10-21T12:08:42.815809+00:00 | supports | The active chemical identity matches the assigned label. Original acquisition and later byte verification are distinct; chemical identity does not validate a biological mechanism. |
| authority-reuse | Chemical, catalog and bounded runner reuse receipts; Current byte verification 12:15:08.867483 UTC; original access times retained | supports | Two official chemical responses retain their 12:08 access times. The catalog and runner discovery retain their older timestamps and bounds; no fresh global runner search is asserted. |
| predicate-authority | Local proposal predicate roles; v2 mitigates row10; v9 produces row3 and reduces row5 | supports | The three local properties permit the current conceptual endpoint kinds. None of the free phrases asserts an RO or Biolink identifier, so no unasserted external role restriction is imported. Biological correctness is separate. |
| ground-ledger | Complete documentary grounding assessment; Thirteen nodes, eleven edges, three components and 61 inputs | supports | Current identity and endpoint roles are supported at documentary scope. The systems/activity wording and optional instances remain limitations, with no formal relation finding. |
| node-edges | Complete node and edge ledger; Nodes0–12 and edges0–10, zero-based | supports | All endpoints resolve. GO function grounding, chemical identities and local predicate roles are permitted. The external environmental gradient is not automatically a cellular state; the systems node permits a process reading. |
| owners | Maintained mapping, retention and writer recurrence; Predicate rows39/93/2; node rows144/157/278/138; regrounding row67 | supports | Existing-ID-preserving grounders retain the current permitted assignments. Explicit typography retention and historical accession/domain corrections are positive maintenance. The captured canonical-example history actually targets this record. |
| canonical-history | Target-specific canonical-example addition; history/other/canonical-examples-environment/2026-08-26T105411Z-codex-29d8602.yaml | context_only | The captured AI-authored event explicitly adds the current canonical example. It is positive target-specific provenance, not incidental context and not human acceptance. |
| provenance | Bounded local acceptance search; Own B7 repository; original search 12:15:08.879356–12:15:19.470261 UTC | partial | Fifteen events comprise fourteen AI events and one seed. The matching captured repository history is AI-authored; no human acceptance attribution was established locally. Private and remote decisions remain unknown. |
| provenance-assessment | History attribution and search integration; Fifteen local events and the captured canonical-example repository event | partial | Automated seeding, fourteen AI maintenance events and actual target-specific AI repository history are preserved. They do not attribute human scientific acceptance. |
| expression | Canonical-only expression catalog applicability; Catalog original 07:36:12.732638–07:36:12.858149 UTC; integration 12:16:48.778800 UTC | context_only | The retained twenty-organism, twenty-eight-dataset catalog has no match for the canonical species or documented type-material aliases. No substitute organism, gene, module, stress or conditions query was performed. |
| runner | Historical bounded structured-source runner discovery; Original B5 PATH/project search 09:27:57 UTC; external installation search 08:17:15 UTC | context_only | The retained bounded discovery and official API fallback are reused at their original scope. Copying the receipt does not establish fresh B7 or global runner absence. |
| source-ledger | Complete documentary source assessment; Seven publications, eight literal reference forms and fifteen placements | partial | All identities resolve. Canonical classification and general low-oxygen tolerance context are supported. The nearest definition quotation and intermediate-oxygen class attribution remain unverified; detailed defense and host-fitness biology remain unassessed. |
| placements | Complete citation-placement ledger; All fifteen top-level, canonical and edge placements | partial | PMID30113300 and DOI10.1099/ijsem.0.002936 denote one canonical publication. Every placement has explicit access and claim scope; resolved bibliography is not blanket biological support. |
| snippets | Complete seven-field quotation ledger; Four exact excerpts and three unverified occurrences | partial | Exact canonical, Nature keypoint, Lu abstract and SOD abstract wording was observed. Three Bioresource Technology occurrences remain unknown without the body; abstract nonmatch is not a false-quote finding. |
| edge-sources | All eleven edge source placements; General context edges0/1/4; edge5 exact class attribution unknown; other detailed biology unassessed | partial | General classification support is separate from detailed causal correctness. The SOD abstract reports correlation, and is not promoted to mechanistic proof. Host selection, colonization, numerical conditions and defense routes remain UNASSESSED_SCOPE. |
| meta-definition | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.biortech.2011.02.011&amp;format=json&amp;resultType=core; Actual indexed primary metadata/abstract 2026-10-21T12:14:51.100460+00:00 through 2026-10-21T12:14:51.837959+00:00 | partial | The actual abstract supports mixed-community oxygen-tolerant anaerobic fermentation context. It does not verify the exact assigned definition phrase or repeated quotations without the body. |
| meta-canonical | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A30113300+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Actual indexed primary metadata/abstract 2026-10-21T12:14:51.100860+00:00 through 2026-10-21T12:14:51.738766+00:00 | supports | The actual primary abstract explicitly supports the canonical microaerotolerant classification and type-strain identifiers. No complete-body read or universal species mechanism is claimed. |
| meta-nature | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrmicro2970&amp;format=json&amp;resultType=core; Actual indexed primary metadata/abstract 2026-10-21T12:14:51.100977+00:00 through 2026-10-21T12:14:52.056665+00:00 | partial | Identity and abstract context are resolved; the separate actual BioC keypoint provides the general classification support. |
| meta-lu | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41579-021-00583-y&amp;format=json&amp;resultType=core; Actual indexed primary metadata/abstract 2026-10-21T12:14:51.101076+00:00 through 2026-10-21T12:14:51.731374+00:00 | partial | Identity and abstract are resolved. The separately retained abstract passage is used only for literal quotation fidelity, not detailed defense biology. |
| meta-sod | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2Fiai.16.1.20-25.1977&amp;format=json&amp;resultType=core; Actual indexed primary metadata/abstract 2026-10-21T12:14:51.731443+00:00 through 2026-10-21T12:14:52.385966+00:00 | partial | The assigned short excerpt is exact in the actual abstract. Its correlational wording is retained and is not evidence of a fully verified causal route. |
| meta-cmr | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FCMR.00110-14&amp;format=json&amp;resultType=core; Actual indexed primary metadata/abstract 2026-10-21T12:14:51.738827+00:00 through 2026-10-21T12:14:52.405553+00:00 | partial | Identity and abstract are resolved. The precise intermediate-oxygen class attribution remains unverified because the article body was unavailable. |
| meta-iai | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FIAI.00502-24&amp;format=json&amp;resultType=core; Actual indexed primary metadata/abstract 2026-10-21T12:14:51.838012+00:00 through 2026-10-21T12:14:52.481620+00:00 | partial | The publication identity and high-level abstract were inspected only. Detailed host, defense, donor-dependence, fitness and quantitative statements remain UNASSESSED_SCOPE. |
| nature-primary | DOI:10.1038/nrmicro2970; Actual BioC keypoint offset38117; original acquisition 12:10:50.354660–12:10:50.676141 UTC | supports | The inspected keypoint positively supports general low or transient oxygen tolerance without requiring oxygen. This is classification evidence, not validation of detailed physiology. |
| lu-primary | DOI:10.1038/s41579-021-00583-y; Actual BioC abstract offset86; original acquisition 08:25:23 UTC | partial | The short assigned phrase is exact in the inspected abstract. Only quotation fidelity was assessed here; no detailed biological route was validated or extracted. |
| body-reuse | Byte-verified primary-body reuse; Nature and Lu copying 12:15:28.411660–12:15:28.412228 UTC | context_only | Both files match their original receipt hashes. Nature retains its 12:10 acquisition and Lu its 08:25 acquisition; copying and later reading are not fresh retrieval. |
| access-body-accesses | Bounded primary-source accessibility receipts; body-accesses.json; individual original attempt timestamps retained | context_only | Failed EPMC/BioC requests, publisher denials/challenges and the HTTP200 Elsevier redirect-only response supply no unseen article-body verification. Neither unavailable text nor title-only comparison proves a false claim. |
| access-alternate-body-accesses | Bounded primary-source accessibility receipts; alternate-body-accesses.json; individual original attempt timestamps retained | context_only | Failed EPMC/BioC requests, publisher denials/challenges and the HTTP200 Elsevier redirect-only response supply no unseen article-body verification. Neither unavailable text nor title-only comparison proves a false claim. |
| access-browser-access-receipts | Bounded primary-source accessibility receipts; browser-access-receipts.json; individual original attempt timestamps retained | context_only | Failed EPMC/BioC requests, publisher denials/challenges and the HTTP200 Elsevier redirect-only response supply no unseen article-body verification. Neither unavailable text nor title-only comparison proves a false claim. |
| publication-status | Bounded publication-status audit; Seven fresh indexed metadata records; completed 12:16:58.186980 UTC | context_only | No linked correction or retraction appeared in the inspected fields. This limited observation is not a global absence certificate across all registries or publishers. |
| root-primary-read | Independent bounded primary-passage reading; Read 12:16:17.386417 UTC; canonical/definition abstracts and Nature keypoint | supports | The parent inspected actual classification passages and fresh source identities. The CMR publisher re-open failed403 and supplied no body. Acquisition, reading and failed access remain distinct. |
| root-primary-supplement | Independent identity and quotation read supplement; Read 12:20:43.710309 UTC; official GO/CHEBI/NCBI, pinned METPO and bounded abstract quotations | supports | The parent directly read official identity responses and pinned current/obsolete properties. SOD and Lu passages were used only for quotation fidelity. Detailed biology remained unassessed. |
| adjudication | Final parent adjudication; Finalized 12:21:05.808705 UTC; qualified pass, zero major and one minor | supports | Positive identity, canonical classification, general context and documentary endpoint roles support pass_with_limitations. Only bounded human-acceptance traceability is a finding; source-access and unassessed biological scope are explicit limitations. |

## Limits And Additional Notes

- General definition meaning is supported by the exact pinned ontology and the actual Nature keypoint. The nearest Bioresource Technology source supplies positive mixed-community context, while its exact definition phrase and three repeated excerpts remain unverified without article-body access.
- The CMR intermediate-oxygen class attribution remains unknown. HTTP200 redirect-only text, failed EPMC/BioC retrievals and publisher denials/challenges are not article bodies, and unavailable text or titles alone do not prove false claims.
- Detailed pathogen-linked oxidative-defense, donor-dependence, host-colonization, fitness and selection biology, numeric gut conditions and growth optimization are UNASSESSED_SCOPE. No mechanism repair, reconstruction, new target, condition or intervention is supplied.
- Canonical species and type-material identity and primary phenotype classification are positively supported. No new measured assay, complete-body reading or universal mechanism across the species is implied.
- The Nature keypoint is general classification evidence. Lu and SOD excerpts were checked for wording only; the SOD abstract remains correlational. Exact quotation, valid ontology identity and permitted predicate roles do not certify detailed biology.
- The systems label of node12 permits either machinery wording or an activity reading; its description allows the current process interpretation. External environmental gradients are not automatically cellular STATE nodes. These are bounded precision limitations, not forced retypes.
- Three local predicate IDs remain provisional proposal terms rather than active upstream terms. Their documentary roles are permitted. Free phrases do not acquire unasserted RO or Biolink restrictions, and no OWL reasoner result is claimed.
- Three components, two label-only protein classes and zero instances are allowed in NONMECHANISTIC context. Optional absent instances, catalog coverage or connectors are not defects, and historical deleted accessions/domain IDs are not current assertions.
- The identity addendum supplies direct positive IAO_0100001 replacement evidence from obsolete1000351 to1000610. It qualifies the frozen assessment without inferring replacement from deprecation or changing current exact identity.
- Fresh source and official identity responses retain actual times. Nature BioC retains its 12:10 acquisition, Lu BioC its 08:25 acquisition, and the two reused chemical responses their 12:08 acquisitions. Later copying, hash verification and independent reading are distinct events.
- Catalog and bounded runner receipts retain original 07:36 and 09:27/08:17 times. No canonical catalog match or substitute-organism query was used; noncoverage is not negative evidence. No fresh B7 or global runner absence is asserted.
- Publication-status inspection is bounded to seven current indexed records. The ignored-inclusive local provenance search does not cover private or remote acceptance. Fourteen AI events, one seed and the target-specific AI repository event remain positive maintenance, not human acceptance.
- The captured provider report is a lead and provenance context only, not a claim of full report reading or independent primary mechanism verification.
- Reused B6 QC, B4 corpus protein audit, B3 history and OLD product failures/retry retain original times and meanings. The qualified proof distinguishes 1,277 history YAML records from 1,278 total files. Builder preparation performs no native validation, review save, scientific input, Git, state or environment mutation.
- One minor finding and zero major findings. Both canonical and native verdicts are pass_with_limitations. Positive identity, canonical and general context evidence supports the verdict; explicit limitations retain unknown source wording and unassessed biology.
- All 61 captured input hashes match. Coverage includes thirteen nodes, eleven edges, three components, three protein classes, two label-only classes, zero instances, fifteen events, seven publications, eight literal reference forms, fifteen placements and seven snippets.
- Source assessment completed at12:16:58.187282 UTC and grounding at12:16:48.780126 UTC. Final parent adjudication is12:21:05.808705 UTC; the separate positive replacement addendum is12:21:24.813986 UTC. Original acquisition dates remain distinct from later assessment times.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T122539Z-microaerotolerant
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of microaerotolerant
started_at: '2026-10-21T12:14:15.209527Z'
finished_at: '2026-10-21T12:25:39Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: This session did not author or modify the captured scientific
    record. Separate source and grounding agents supplied complete ledgers. The parent
    inspected bounded primary passages and official identities, qualified the explicit
    obsolete-term replacement, and adjudicated the verdict before reading the complete
    builder. This AI review and automated maintenance are distinct from human scientific
    acceptance.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Pass with limitations. Exact active identity and its explicit obsolete precursor
  replacement, general definition context, canonical species/type-strain classification
  and documentary node/predicate roles are supported. One minor finding concerns bounded
  human-acceptance attribution; no major or source-only finding is assigned. All thirteen
  nodes, eleven edges and fifteen citation placements are covered at the declared
  scope. Four excerpts are exact and three remain unverified. Detailed defense, host
  selection, fitness and numerical conditions remain unassessed.
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
  - path: data/traits/environment/microaerotolerant.yaml
    sha256: 10a2073270238f7569ea0b93d131438699d93217724f45547f840f707389cbe6
    role: target
  - path: data/traits/environment/oxygen_preference.yaml
    sha256: 16829173ea947f2fef083f673c51519aad962d6812fcd54826ea86f055c5a40b
    role: context
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
  - path: history/other/canonical-examples-environment/2026-08-26T105411Z-codex-29d8602.yaml
    sha256: 6e602707db80e54519a6f46d5bf2b79f5c6b2fc294d75176ba4406cac22fc2c2
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
  - path: proposals/metpo_traitmech_v7/proposal.md
    sha256: bc6ea10ebc4bec0f446cee92578602889ec464295ce5ecce27fed76eb06528ce
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
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/ontology_snapshot_manifest.tsv
    sha256: 4a157279a8c4e3fc2afb5382a45c31961991bbd1f330f26d0061b0cfd0b4d213
    role: context
  - path: research/traits/environment/microaerotolerant-deep-research-falcon.md
    sha256: bdebcec9da0b72c05b4f211242d2ad4ae62bde1e63327ffb63234789d5f4d704
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
  - path: scripts/finalize_metpo_2026_06_12_review.py
    sha256: b850b386183b2d86647dada43f7f157059017dbb881f7e1fb2e220ae697d3bea
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
- target_id: METPO:1000610
  path: data/traits/environment/microaerotolerant.yaml
  label: microaerotolerant
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/microaerotolerant.yaml
    role: Maintained TraitRecord; scientific edits require separate curation authorization
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Third record in the seventh path-ordered batch. The entire maintained
    TraitRecord, parent and captured canonical-example history were read. All 61 captured
    inputs, thirteen nodes, eleven edges, three components, three protein classes,
    one canonical example, seven external works, fifteen citation placements, seven
    snippets and fifteen history events are accounted for. Exact identity, general
    classification, canonical phenotype, documentary source identity and endpoint
    roles are assessed. Detailed pathogen-linked defense, colonization, fitness and
    selection biology and numeric conditions remain UNASSESSED_SCOPE. The captured
    provider report is a lead only; no biological mechanism, intervention or optimization
    is supplied.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000610
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000610
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000610
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000610
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000610
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000610
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000610
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000610
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    007 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: microaerotolerant-validate
  name: Focused native record validation
  status: passed
  required: true
  target_ids:
  - METPO:1000610
  command: just validate data/traits/environment/microaerotolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual execution at 12:14:33–12:14:34 UTC passed. Structural validity does
    not establish detailed biological correctness.
  evidence_ids:
  - check-microaerotolerant-validate
- check_id: microaerotolerant-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000610
  command: just validate-strict data/traits/environment/microaerotolerant.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual execution at 12:14:33–12:14:34 UTC passed. Source support and documentary
    endpoint meanings are assessed separately.
  evidence_ids:
  - check-microaerotolerant-strict
- check_id: microaerotolerant-snippets
  name: Focused native snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1000610
  command: just verify-snippets --record data/traits/environment/microaerotolerant.yaml
    --out /private/tmp/traitmech-record-sweep-007.n_925exy/microaerotolerant-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Actual execution at 12:14:36–12:14:44 UTC passed. Seven fields yielded
    three VERIFIED and four NOT_IN_ABSTRACT results. Manual inspection establishes
    four exact excerpts and leaves three unverified; abstract nonmatches are not false
    quotations.
  evidence_ids:
  - check-microaerotolerant-snippets
- check_id: corpus-protein-taxa
  name: Reused corpus protein/taxon audit
  status: passed
  required: true
  target_ids:
  - METPO:1000610
  command: just audit-graph-protein-taxa --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Original batch-four execution at 08:55:04–08:55:10 UTC passed: 719 graphs,
    129 PASS, 589 NONMECHANISTIC, one protected, no gaps or errors. Unchanged inputs
    support reuse, not a fresh focused scientific check.'
  evidence_ids:
  - check-corpus-protein-taxa
- check_id: batch006-qc
  name: Reused batch-six maintained QC
  status: passed
  required: true
  target_ids:
  - METPO:1000610
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Original just qc passed at 11:54:49–11:57:53 UTC. Qualified batch-seven
    byte comparisons support reuse; no fresh batch-seven QC execution is claimed.
  evidence_ids:
  - check-batch006-qc
  scope_note: The qualified proof covers 1,130 traits, 1,278 total history files and
    19 common inputs, distinguishing 1,277 YAML history records from history/README.md.
    B3 history and OLD product failures, successful retry, baselines and adapter skips
    retain their original times and meanings.
- check_id: uniprot-applicability
  name: Protein instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000610
  summary: Three conceptual protein classes, two explicitly label-only, have zero
    individual instances or current UniProt accessions. NONMECHANISTIC scope does
    not require token examples; the historical removed accession is not a current
    defect.
  evidence_ids:
  - record
  - protein-policy
  - node-edges
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-007.n_925exy/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-microaerotolerant-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-007.n_925exy/microaerotolerant-validate.log
  locator: Executed 2026-10-21T12:14:33Z through 2026-10-21T12:14:34Z; metadata microaerotolerant-validate.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: Actual execution at 12:14:33–12:14:34 UTC passed. Structural validity does
    not establish detailed biological correctness.
  snapshot_sha256: 62ecc4d89c4f9c20e369bfd1421a4a29469029df59d2544d34c425ab78392110
- evidence_id: check-microaerotolerant-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-007.n_925exy/microaerotolerant-strict.log
  locator: Executed 2026-10-21T12:14:33Z through 2026-10-21T12:14:34Z; metadata microaerotolerant-strict.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: Actual execution at 12:14:33–12:14:34 UTC passed. Source support and documentary
    endpoint meanings are assessed separately.
  snapshot_sha256: 50f69faf989d2aff16d9e928a67b6b2fe94d5a13901629b6b175df55c0ac9ff3
- evidence_id: check-microaerotolerant-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-007.n_925exy/microaerotolerant-snippets.log
  locator: Executed 2026-10-21T12:14:36Z through 2026-10-21T12:14:44Z; metadata microaerotolerant-snippets.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: Actual execution at 12:14:36–12:14:44 UTC passed. Seven fields yielded
    three VERIFIED and four NOT_IN_ABSTRACT results. Manual inspection establishes
    four exact excerpts and leaves three unverified; abstract nonmatches are not false
    quotations.
  snapshot_sha256: 1c4557b8afb0e4e85a070ca5170c0108ae58022346567543cf1759acde69941d
- evidence_id: check-corpus-protein-taxa
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log
  locator: Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: 'Original batch-four execution at 08:55:04–08:55:10 UTC passed: 719 graphs,
    129 PASS, 589 NONMECHANISTIC, one protected, no gaps or errors. Unchanged inputs
    support reuse, not a fresh focused scientific check.'
  snapshot_sha256: f5f1a6be7789f2b3e487fcbc354361f8f1f0d0d0f90a9ba59864d26ed7ac49ef
- evidence_id: check-batch006-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/batch006-qc.log
  locator: Executed 2026-10-21T11:54:49Z through 2026-10-21T11:57:53Z; metadata batch006-qc.json
  accessed_at: '2026-10-21T12:25:39Z'
  support: context_only
  summary: Original just qc passed at 11:54:49–11:57:53 UTC. Qualified batch-seven
    byte comparisons support reuse; no fresh batch-seven QC execution is claimed.
  snapshot_sha256: 8d583fb60333a9fc3c697349f3684d7f35e85ed7f49e71f11acab84142106853
- evidence_id: capture
  kind: validation
  reference: Native selected-record capture
  locator: 61 inputs; actual inspect 12:14:15.209527–12:14:15.974411 UTC
  accessed_at: '2026-10-21T12:14:15.974411Z'
  support: supports
  summary: All captured input hashes match, including the target-specific canonical-example
    history. Contextual policies, proposals, parent and mappings are not additional
    review targets.
  snapshot_sha256: f20211ce4f11825b17c4b539195a16d3d200f65fd814c052bfd756f0593ff57e
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/microaerotolerant.yaml
  locator: Entire record, thirteen nodes, eleven edges and fifteen history events
  accessed_at: '2026-10-21T12:16:48.780126Z'
  support: partial
  summary: The record is REVIEWED with fourteen AI events and one automated seed.
    The graph is NONMECHANISTIC, with three conceptual protein classes and no instances.
  snapshot_sha256: 10a2073270238f7569ea0b93d131438699d93217724f45547f840f707389cbe6
- evidence_id: native-policy
  kind: authority
  reference: Native field-by-field review checklist
  locator: Source support, scope, completeness and attributed human acceptance
  accessed_at: '2026-10-21T12:16:48.780126Z'
  support: supports
  summary: Full coverage distinguishes positive classification evidence, unavailable
    exact source wording and unassessed detailed biology. Validation and AI review
    are not human scientific acceptance.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: native-types
  kind: authority
  reference: Native node kind definitions
  locator: CausalNodeTypeEnum, protein aggregates and external environmental conditions
  accessed_at: '2026-10-21T12:16:48.780126Z'
  support: supports
  summary: Current represented meanings govern type review. Protein classes can include
    aggregates, environmental conditions need not be cellular states, and contextual
    activities can have process readings.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: protein-policy
  kind: authority
  reference: Maintained grounding policy
  locator: Section 2 functional grounds and contextual label-only classes
  accessed_at: '2026-10-21T12:16:48.780126Z'
  support: supports
  summary: Taxon-agnostic enzymatic functional grounds are permitted on legacy protein
    nodes. Optional instances and label-only aggregates are not defects by themselves.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: reuse
  kind: validation
  reference: Original B6 to B7 byte comparison
  locator: Original verification 11:36:30.388266 UTC
  accessed_at: '2026-10-21T11:36:30.388266Z'
  support: context_only
  summary: Trait, history and common-input equality supports scoped historical diagnostics.
    Execution times are preserved separately from the later comparison.
  snapshot_sha256: c574f87e084e0f076ffb7d60ec06f9f86c2dcd4f16512746c9120854e88f0bf1
- evidence_id: reuse-supplement
  kind: validation
  reference: Qualified B6 QC reuse proof
  locator: Qualified 12:01:47.374200 UTC; original QC 11:54:49–11:57:53 UTC
  accessed_at: '2026-10-21T12:01:47.374200Z'
  support: supports
  summary: The all-file and earlier YAML-only history comparisons are distinguished.
    Original check dates, failures, retries and skips are not recast as fresh execution.
  snapshot_sha256: 26b4a1e134156fe6cb29f9c238316c846eb1e7b517adcdf25c73bace6aa28355
- evidence_id: identity
  kind: validation
  reference: Pinned METPO identity and retention assessment
  locator: Active METPO1000610 and parent1000601; active-review line118 and release-delta
    line1286
  accessed_at: '2026-10-21T12:16:48.775517Z'
  support: supports
  summary: Current exact identity, parent and retained oxygen typography agree. Removal
    of the own-label duplicate synonym preserves meaning. Read the separate positive
    replacement addendum with this original assessment.
  snapshot_sha256: b453ad25b90aaea774ca6a2dec2a17b8962b803b5dc71bc1f49538185d91edec
- evidence_id: metpo-primary
  kind: authority
  reference: Pinned METPO ontology
  locator: Active 1000610, parent1000601 and obsolete1000351 explicit IAO_0100001
  accessed_at: '2026-10-21T12:21:24.813986Z'
  support: supports
  summary: The active term has the exact definition and parent. Obsolete1000351 explicitly
    points to1000610 through term-replaced-by; this positive fact is not inferred
    merely from deprecation.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: replacement-addendum
  kind: validation
  reference: Explicit obsolete-term replacement qualification
  locator: Direct pinned ontology properties, assessed 12:21:24.813986 UTC
  accessed_at: '2026-10-21T12:21:24.813986Z'
  support: supports
  summary: The frozen identity assessment omitted the positive explicit IAO_0100001
    link from obsolete1000351 to active1000610. This addendum supplies that fact without
    rewriting the original ledger or changing current identity.
  snapshot_sha256: 0f4c728fdd166275a374a968ae0059726db066d70ca3b51c790742e407fe31f2
- evidence_id: db-go0050605
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0050605
  locator: Actual official response 2026-10-21T12:14:51.493637+00:00 through 2026-10-21T12:14:52.148488+00:00
  accessed_at: '2026-10-21T12:14:52.148488Z'
  support: supports
  summary: The active molecular-function identity matches the permitted enzymatic
    facet. It does not identify a gene isoform, canonical strain or detailed defense
    route.
  snapshot_sha256: ddb3d4bb8e2c7004ec43862c44563ed5e6443324712c3ebdb78d3f6a02c1d3a5
- evidence_id: db-chebi18421
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18421
  locator: Actual official response 2026-10-21T12:14:51.494020+00:00 through 2026-10-21T12:14:52.400144+00:00
  accessed_at: '2026-10-21T12:14:52.400144Z'
  support: supports
  summary: The active superoxide identity and radical-anion charge match the stated
    chemical meaning. No detailed biological claim follows from chemical identity.
  snapshot_sha256: 99b1d89eb378c2df50376680eb6a8a896763c68155f4a5bc46ddbe96a8f5ae62
- evidence_id: db-taxon2303410
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2303410&retmode=xml
  locator: Actual official response 2026-10-21T12:14:51.494124+00:00 through 2026-10-21T12:14:51.775151+00:00
  accessed_at: '2026-10-21T12:14:51.775151Z'
  support: supports
  summary: The official species identity and MCy10636, DSM106554 and NCCB100651 type-material
    aliases match the canonical example.
  snapshot_sha256: 8714b4be3d680edba8f984fa1d5208f6b9c5418bd68b884d55a04f049ef72f59
- evidence_id: db-chebi16240
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16240
  locator: Reused official response 2026-10-21T12:08:35.958139+00:00 through 2026-10-21T12:08:38.989724+00:00
  accessed_at: '2026-10-21T12:08:38.989724Z'
  support: supports
  summary: The active chemical identity matches the assigned label. Original acquisition
    and later byte verification are distinct; chemical identity does not validate
    a biological mechanism.
  snapshot_sha256: 8df24a48076f1aa959b2162d2c2bbc1c8075f337f79b4d0b4295453fd4dbf9c0
- evidence_id: db-chebi26523
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26523
  locator: Reused official response 2026-10-21T12:08:35.989739+00:00 through 2026-10-21T12:08:42.815809+00:00
  accessed_at: '2026-10-21T12:08:42.815809Z'
  support: supports
  summary: The active chemical identity matches the assigned label. Original acquisition
    and later byte verification are distinct; chemical identity does not validate
    a biological mechanism.
  snapshot_sha256: 9cefa8d93653be094db7dd4023cfbe0f27878acc859a58b8390eb1d14d9e9ba5
- evidence_id: authority-reuse
  kind: validation
  reference: Chemical, catalog and bounded runner reuse receipts
  locator: Current byte verification 12:15:08.867483 UTC; original access times retained
  accessed_at: '2026-10-21T12:15:08.867483Z'
  support: supports
  summary: Two official chemical responses retain their 12:08 access times. The catalog
    and runner discovery retain their older timestamps and bounds; no fresh global
    runner search is asserted.
  snapshot_sha256: f9e7f80fb3c2a4d950166419e07b41bea7f991519f3e9c04975e62bc8fdba4d4
- evidence_id: predicate-authority
  kind: validation
  reference: Local proposal predicate roles
  locator: v2 mitigates row10; v9 produces row3 and reduces row5
  accessed_at: '2026-10-21T12:16:48.776274Z'
  support: supports
  summary: The three local properties permit the current conceptual endpoint kinds.
    None of the free phrases asserts an RO or Biolink identifier, so no unasserted
    external role restriction is imported. Biological correctness is separate.
  snapshot_sha256: 6dd3b546cbab474ff1f943b738fe537253457652983db82d4137af6ba6cac0f8
- evidence_id: ground-ledger
  kind: validation
  reference: Complete documentary grounding assessment
  locator: Thirteen nodes, eleven edges, three components and 61 inputs
  accessed_at: '2026-10-21T12:16:48.780126Z'
  support: supports
  summary: Current identity and endpoint roles are supported at documentary scope.
    The systems/activity wording and optional instances remain limitations, with no
    formal relation finding.
  snapshot_sha256: 9e70a231096d7d09e82fe4e15e535bdc96bf55a5bd541609e9fc7de1309e1d3d
- evidence_id: node-edges
  kind: validation
  reference: Complete node and edge ledger
  locator: Nodes0–12 and edges0–10, zero-based
  accessed_at: '2026-10-21T12:16:48.777013Z'
  support: supports
  summary: All endpoints resolve. GO function grounding, chemical identities and local
    predicate roles are permitted. The external environmental gradient is not automatically
    a cellular state; the systems node permits a process reading.
  snapshot_sha256: 8c927623c22f138b21e154f5471d0b6baaa3e271d8f7674fe3a64c32d0f15b89
- evidence_id: owners
  kind: validation
  reference: Maintained mapping, retention and writer recurrence
  locator: Predicate rows39/93/2; node rows144/157/278/138; regrounding row67
  accessed_at: '2026-10-21T12:16:48.777790Z'
  support: supports
  summary: Existing-ID-preserving grounders retain the current permitted assignments.
    Explicit typography retention and historical accession/domain corrections are
    positive maintenance. The captured canonical-example history actually targets
    this record.
  snapshot_sha256: e5976b6da1b9be0d5bad097839c3426fc04e9112d49e87208ae904e5fa5c0548
- evidence_id: canonical-history
  kind: record_content
  reference: Target-specific canonical-example addition
  locator: history/other/canonical-examples-environment/2026-08-26T105411Z-codex-29d8602.yaml
  accessed_at: '2026-10-21T12:16:48.779520Z'
  support: context_only
  summary: The captured AI-authored event explicitly adds the current canonical example.
    It is positive target-specific provenance, not incidental context and not human
    acceptance.
  snapshot_sha256: 6e602707db80e54519a6f46d5bf2b79f5c6b2fc294d75176ba4406cac22fc2c2
- evidence_id: provenance
  kind: search
  reference: Bounded local acceptance search
  locator: Own B7 repository; original search 12:15:08.879356–12:15:19.470261 UTC
  accessed_at: '2026-10-21T12:15:19.470261Z'
  support: partial
  summary: Fifteen events comprise fourteen AI events and one seed. The matching captured
    repository history is AI-authored; no human acceptance attribution was established
    locally. Private and remote decisions remain unknown.
  snapshot_sha256: ddac45a32272664136df8bf19b258cc79233eb066254948802cd98b727502059
  search_scope: Own B7 repository, rg --hidden --no-ignore, excluding .git/** and
    .venv/**; exact target ID, slug and selected graph/node IDs; 170 matching files
    and matching review target arrays inspected. Supplemental ignored-inclusive history/scripts/mappings/proposals
    searches are bounded in their retained receipt. No private, remote or global absence
    claim.
- evidence_id: provenance-assessment
  kind: validation
  reference: History attribution and search integration
  locator: Fifteen local events and the captured canonical-example repository event
  accessed_at: '2026-10-21T12:16:48.779520Z'
  support: partial
  summary: Automated seeding, fourteen AI maintenance events and actual target-specific
    AI repository history are preserved. They do not attribute human scientific acceptance.
  snapshot_sha256: f2e2807b759695393854748d445ba86c0e1078079d81f7e86568816a689e6f30
- evidence_id: expression
  kind: validation
  reference: Canonical-only expression catalog applicability
  locator: Catalog original 07:36:12.732638–07:36:12.858149 UTC; integration 12:16:48.778800
    UTC
  accessed_at: '2026-10-21T12:16:48.778800Z'
  support: context_only
  summary: The retained twenty-organism, twenty-eight-dataset catalog has no match
    for the canonical species or documented type-material aliases. No substitute organism,
    gene, module, stress or conditions query was performed.
  snapshot_sha256: e319ba6aecbf7cf303a41125209bb6825fd050f0448c8facbd3dce88e3cfcee9
- evidence_id: runner
  kind: validation
  reference: Historical bounded structured-source runner discovery
  locator: Original B5 PATH/project search 09:27:57 UTC; external installation search
    08:17:15 UTC
  accessed_at: '2026-10-21T09:27:57Z'
  support: context_only
  summary: The retained bounded discovery and official API fallback are reused at
    their original scope. Copying the receipt does not establish fresh B7 or global
    runner absence.
  snapshot_sha256: 43597ec8b007fc605fabf9069534281f331a33bda5615b9ce9c473facf744179
- evidence_id: source-ledger
  kind: validation
  reference: Complete documentary source assessment
  locator: Seven publications, eight literal reference forms and fifteen placements
  accessed_at: '2026-10-21T12:16:58.187282Z'
  support: partial
  summary: All identities resolve. Canonical classification and general low-oxygen
    tolerance context are supported. The nearest definition quotation and intermediate-oxygen
    class attribution remain unverified; detailed defense and host-fitness biology
    remain unassessed.
  snapshot_sha256: 1c1c92553ef7eb9e946dd5ad1e594962d4491f054bf6094c9256caeb0ef9747f
- evidence_id: placements
  kind: validation
  reference: Complete citation-placement ledger
  locator: All fifteen top-level, canonical and edge placements
  accessed_at: '2026-10-21T12:16:58.187282Z'
  support: partial
  summary: PMID30113300 and DOI10.1099/ijsem.0.002936 denote one canonical publication.
    Every placement has explicit access and claim scope; resolved bibliography is
    not blanket biological support.
  snapshot_sha256: fe17b36f3de865e0140b0f27da2d5b2afe780195b93e881a508738674f7300d6
- evidence_id: snippets
  kind: validation
  reference: Complete seven-field quotation ledger
  locator: Four exact excerpts and three unverified occurrences
  accessed_at: '2026-10-21T12:16:58.187282Z'
  support: partial
  summary: Exact canonical, Nature keypoint, Lu abstract and SOD abstract wording
    was observed. Three Bioresource Technology occurrences remain unknown without
    the body; abstract nonmatch is not a false-quote finding.
  snapshot_sha256: e43cabf67dee93b3f29f7c8726fe26d80a8ad4b13f562b88ddd24bacf5a57c95
- evidence_id: edge-sources
  kind: validation
  reference: All eleven edge source placements
  locator: General context edges0/1/4; edge5 exact class attribution unknown; other
    detailed biology unassessed
  accessed_at: '2026-10-21T12:16:58.187282Z'
  support: partial
  summary: General classification support is separate from detailed causal correctness.
    The SOD abstract reports correlation, and is not promoted to mechanistic proof.
    Host selection, colonization, numerical conditions and defense routes remain UNASSESSED_SCOPE.
  snapshot_sha256: b4e8d0b4418a33a88d870933fef8705eb7225bec0f604908d506b5c60cfe1f6f
- evidence_id: meta-definition
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.biortech.2011.02.011&format=json&resultType=core
  locator: Actual indexed primary metadata/abstract 2026-10-21T12:14:51.100460+00:00
    through 2026-10-21T12:14:51.837959+00:00
  accessed_at: '2026-10-21T12:14:51.837959Z'
  support: partial
  summary: The actual abstract supports mixed-community oxygen-tolerant anaerobic
    fermentation context. It does not verify the exact assigned definition phrase
    or repeated quotations without the body.
  snapshot_sha256: 8dec0203a75be9305d47dbf2818918e352bfe92145856bd01da4330384afcaab
- evidence_id: meta-canonical
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A30113300+AND+SRC%3AMED&format=json&resultType=core
  locator: Actual indexed primary metadata/abstract 2026-10-21T12:14:51.100860+00:00
    through 2026-10-21T12:14:51.738766+00:00
  accessed_at: '2026-10-21T12:14:51.738766Z'
  support: supports
  summary: The actual primary abstract explicitly supports the canonical microaerotolerant
    classification and type-strain identifiers. No complete-body read or universal
    species mechanism is claimed.
  snapshot_sha256: b99b9984deddd0aaedf8d155c3a46c4b8b75a82b4faea30dd4ee63710b3c7ac4
- evidence_id: meta-nature
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrmicro2970&format=json&resultType=core
  locator: Actual indexed primary metadata/abstract 2026-10-21T12:14:51.100977+00:00
    through 2026-10-21T12:14:52.056665+00:00
  accessed_at: '2026-10-21T12:14:52.056665Z'
  support: partial
  summary: Identity and abstract context are resolved; the separate actual BioC keypoint
    provides the general classification support.
  snapshot_sha256: d112e656f5c1ba595ea7da0fabf334d106ebd119d5afdf47382dc70ad5478b8b
- evidence_id: meta-lu
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41579-021-00583-y&format=json&resultType=core
  locator: Actual indexed primary metadata/abstract 2026-10-21T12:14:51.101076+00:00
    through 2026-10-21T12:14:51.731374+00:00
  accessed_at: '2026-10-21T12:14:51.731374Z'
  support: partial
  summary: Identity and abstract are resolved. The separately retained abstract passage
    is used only for literal quotation fidelity, not detailed defense biology.
  snapshot_sha256: 4b8cdffffc0337d85afc76d1b18681be8cd3b60ec314c832262b18bc135e81f0
- evidence_id: meta-sod
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2Fiai.16.1.20-25.1977&format=json&resultType=core
  locator: Actual indexed primary metadata/abstract 2026-10-21T12:14:51.731443+00:00
    through 2026-10-21T12:14:52.385966+00:00
  accessed_at: '2026-10-21T12:14:52.385966Z'
  support: partial
  summary: The assigned short excerpt is exact in the actual abstract. Its correlational
    wording is retained and is not evidence of a fully verified causal route.
  snapshot_sha256: ce3a76361187dd9a3d2d3ee4db02012f0bab660f1279ed901eb1e4b3ac77aaf1
- evidence_id: meta-cmr
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FCMR.00110-14&format=json&resultType=core
  locator: Actual indexed primary metadata/abstract 2026-10-21T12:14:51.738827+00:00
    through 2026-10-21T12:14:52.405553+00:00
  accessed_at: '2026-10-21T12:14:52.405553Z'
  support: partial
  summary: Identity and abstract are resolved. The precise intermediate-oxygen class
    attribution remains unverified because the article body was unavailable.
  snapshot_sha256: fc4107cc2d26641b0085e6b21febdf80371d8761194d73c81c9a9c2912901308
- evidence_id: meta-iai
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FIAI.00502-24&format=json&resultType=core
  locator: Actual indexed primary metadata/abstract 2026-10-21T12:14:51.838012+00:00
    through 2026-10-21T12:14:52.481620+00:00
  accessed_at: '2026-10-21T12:14:52.481620Z'
  support: partial
  summary: The publication identity and high-level abstract were inspected only. Detailed
    host, defense, donor-dependence, fitness and quantitative statements remain UNASSESSED_SCOPE.
  snapshot_sha256: 4b3094848857acf4d8615950b6a6548f3010fff87bf8b787fed07221783ba3bc
- evidence_id: nature-primary
  kind: primary_source
  reference: DOI:10.1038/nrmicro2970
  locator: Actual BioC keypoint offset38117; original acquisition 12:10:50.354660–12:10:50.676141
    UTC
  accessed_at: '2026-10-21T12:10:50.676141Z'
  support: supports
  summary: The inspected keypoint positively supports general low or transient oxygen
    tolerance without requiring oxygen. This is classification evidence, not validation
    of detailed physiology.
  snapshot_sha256: 08f399475a6ff5040a7cf2d442f95d5221cba25190c2b4ee1fb815eee76c30ea
- evidence_id: lu-primary
  kind: primary_source
  reference: DOI:10.1038/s41579-021-00583-y
  locator: Actual BioC abstract offset86; original acquisition 08:25:23 UTC
  accessed_at: '2026-10-21T08:25:23Z'
  support: partial
  summary: The short assigned phrase is exact in the inspected abstract. Only quotation
    fidelity was assessed here; no detailed biological route was validated or extracted.
  snapshot_sha256: 8ce53770e39dc8f72cd5dc03fff9676954ed0f43c0ac36be40e2b78466239430
- evidence_id: body-reuse
  kind: validation
  reference: Byte-verified primary-body reuse
  locator: Nature and Lu copying 12:15:28.411660–12:15:28.412228 UTC
  accessed_at: '2026-10-21T12:15:28.412228Z'
  support: context_only
  summary: Both files match their original receipt hashes. Nature retains its 12:10
    acquisition and Lu its 08:25 acquisition; copying and later reading are not fresh
    retrieval.
  snapshot_sha256: fed02bb455e77f442e55a5d301ce6afc943847927c6c40c330962123f08304e2
- evidence_id: access-body-accesses
  kind: validation
  reference: Bounded primary-source accessibility receipts
  locator: body-accesses.json; individual original attempt timestamps retained
  accessed_at: '2026-10-21T12:16:58.187282Z'
  support: context_only
  summary: Failed EPMC/BioC requests, publisher denials/challenges and the HTTP200
    Elsevier redirect-only response supply no unseen article-body verification. Neither
    unavailable text nor title-only comparison proves a false claim.
  snapshot_sha256: 874e1aa7764d2b8644494fb4e1c38b00c3fc1f6c37d035cce98045d6f4eedd54
- evidence_id: access-alternate-body-accesses
  kind: validation
  reference: Bounded primary-source accessibility receipts
  locator: alternate-body-accesses.json; individual original attempt timestamps retained
  accessed_at: '2026-10-21T12:16:58.187282Z'
  support: context_only
  summary: Failed EPMC/BioC requests, publisher denials/challenges and the HTTP200
    Elsevier redirect-only response supply no unseen article-body verification. Neither
    unavailable text nor title-only comparison proves a false claim.
  snapshot_sha256: 35cb81549d96ffc896e754607f5a2749cb9388e66dc8e0dff3890cc2a9a486a1
- evidence_id: access-browser-access-receipts
  kind: validation
  reference: Bounded primary-source accessibility receipts
  locator: browser-access-receipts.json; individual original attempt timestamps retained
  accessed_at: '2026-10-21T12:16:58.187282Z'
  support: context_only
  summary: Failed EPMC/BioC requests, publisher denials/challenges and the HTTP200
    Elsevier redirect-only response supply no unseen article-body verification. Neither
    unavailable text nor title-only comparison proves a false claim.
  snapshot_sha256: 0e8f151c889fa81bf68521e9706b90f67698772c241145a7d9aae84e4171d1f3
- evidence_id: publication-status
  kind: validation
  reference: Bounded publication-status audit
  locator: Seven fresh indexed metadata records; completed 12:16:58.186980 UTC
  accessed_at: '2026-10-21T12:16:58.186980Z'
  support: context_only
  summary: No linked correction or retraction appeared in the inspected fields. This
    limited observation is not a global absence certificate across all registries
    or publishers.
  snapshot_sha256: 6a803adab5ce2026958eb4f2c4a3b20d33a3b59b8ce9a097c8de988f5b020573
- evidence_id: root-primary-read
  kind: validation
  reference: Independent bounded primary-passage reading
  locator: Read 12:16:17.386417 UTC; canonical/definition abstracts and Nature keypoint
  accessed_at: '2026-10-21T12:16:17.386417Z'
  support: supports
  summary: The parent inspected actual classification passages and fresh source identities.
    The CMR publisher re-open failed403 and supplied no body. Acquisition, reading
    and failed access remain distinct.
  snapshot_sha256: 46b0a72799cc74812a0b225e7becd0a0e6b5aecad819c6d9ea960fd744948041
- evidence_id: root-primary-supplement
  kind: validation
  reference: Independent identity and quotation read supplement
  locator: Read 12:20:43.710309 UTC; official GO/CHEBI/NCBI, pinned METPO and bounded
    abstract quotations
  accessed_at: '2026-10-21T12:20:43.710309Z'
  support: supports
  summary: The parent directly read official identity responses and pinned current/obsolete
    properties. SOD and Lu passages were used only for quotation fidelity. Detailed
    biology remained unassessed.
  snapshot_sha256: a4b59b84c705af986f11ce584da335a4800eae03237e10a5bfb9fdb9cdd66868
- evidence_id: adjudication
  kind: validation
  reference: Final parent adjudication
  locator: Finalized 12:21:05.808705 UTC; qualified pass, zero major and one minor
  accessed_at: '2026-10-21T12:21:05.808705Z'
  support: supports
  summary: Positive identity, canonical classification, general context and documentary
    endpoint roles support pass_with_limitations. Only bounded human-acceptance traceability
    is a finding; source-access and unassessed biological scope are explicit limitations.
  snapshot_sha256: bddfe67158ffa2edff804d3d07b9c2f625d710e5ac5c0dcaab8e80276f139b8e
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: exact active concept, parent, synonyms and obsolete precursor'
  outcome: supported
  target_ids:
  - METPO:1000610
  summary: METPO1000610 is the exact active concept with oxygen-preference parent1000601.
    The current definition and retained oxygen typography agree with the pinned ontology.
    Its own-label duplicate synonym was intentionally removed without loss of meaning.
    Obsolete1000351 has an explicit IAO_0100001 replacement link to1000610, positively
    documented in the separate addendum.
  evidence_ids:
  - identity
  - metpo-primary
  - replacement-addendum
  - record
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: definition meaning and general primary classification
    context'
  outcome: supported
  target_ids:
  - METPO:1000610
  summary: The exact pinned definition and Nature keypoint support low-oxygen tolerance
    without an oxygen requirement. The assigned Bioresource Technology abstract supplies
    positive mixed-community context. Its exact class-definition phrase remains unverified
    without the body, so substantive concept support does not certify that nearest
    quotation.
  evidence_ids:
  - metpo-primary
  - nature-primary
  - meta-definition
  - placements
  - root-primary-read
- assessment_id: nearest-definition-source
  area: evidence
  topic: 'Native checklist: precise nearest-source wording'
  outcome: unknown
  target_ids:
  - METPO:1000610
  summary: Three occurrences of the assigned Bioresource Technology phrase remain
    unverified. A redirect-only HTTP200 response and failed publisher access are not
    article-body evidence. Positive mixed-community context is preserved; no false
    quotation or false definition is inferred from limited access.
  evidence_ids:
  - meta-definition
  - snippets
  - access-body-accesses
  - access-alternate-body-accesses
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: canonical species, type material and phenotype'
  outcome: supported
  target_ids:
  - METPO:1000610
  summary: Official NCBI2303410 and the primary species-description abstract support
    Simulacricoccus ruber and the MCy10636, DSM106554 and NCCB100651 aliases and microaerotolerant
    classification. PMID30113300 and the canonical DOI identify the same publication.
    No additional measured assay, universal species mechanism or detailed growth-condition
    verification is claimed.
  evidence_ids:
  - db-taxon2303410
  - meta-canonical
  - placements
  - canonical-history
- assessment_id: nodes
  area: grounding
  topic: 'Native checklist: all thirteen node identities and represented facets'
  outcome: supported
  target_ids:
  - METPO:1000610
  summary: Active chemical identities and the permitted GO0050605 functional facet
    fit current node meanings. The environmental exposures, trait, growth activity,
    chemical donor class and reviewed label-only protein aggregates are documentarily
    compatible. Node12 permits an activity/process reading despite its systems label;
    the external gut environment is not automatically a cellular STATE.
  evidence_ids:
  - node-edges
  - ground-ledger
  - native-types
  - protein-policy
  - db-go0050605
  - db-chebi18421
  - db-chebi16240
  - db-chebi26523
  details: 'Nodes0–2: trait, exposure and chemical class. Nodes3/7/9: contextual protein
    classes. Nodes4/12: growth/activity readings. Nodes5/11: external conditions.
    Nodes6/8/10: chemical identities or role bearers. These documentary facets do
    not verify detailed biological effects.'
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all eleven predicate roles'
  outcome: supported
  target_ids:
  - METPO:1000610
  summary: The local mitigates, produces and redox-reduces properties permit the declared
    endpoint kinds. All remaining phrases are ungrounded text and do not inherit unasserted
    RO or Biolink restrictions. In particular, enables function of is not RO2327,
    and creates selection for is not the local grounded selects-for predicate. No
    formal relation finding is warranted at this scope.
  evidence_ids:
  - predicate-authority
  - node-edges
  - owners
  - adjudication
  details: Edges0/1/2/4/5/9/10 have no external predicate ID. Edges3/6/7/8 use three
    locally defined properties with compatible documentary roles. Source attribution
    and causal correctness remain separate questions.
- assessment_id: source-context
  area: evidence
  topic: 'Native checklist: all eleven edge source placements'
  outcome: supported
  target_ids:
  - METPO:1000610
  summary: All edge references resolve with explicit access and assessment scope.
    General classification context in edges0/1/4 is supported at the stated level;
    nearest literal wording remains qualified. The edge5 precise class attribution
    is unknown, and detailed biology in edges2/3/6–10 remains UNASSESSED_SCOPE. Documentary
    coverage is not blanket mechanistic verification.
  evidence_ids:
  - edge-sources
  - source-ledger
  - placements
  - nature-primary
  - meta-definition
- assessment_id: detailed-biology
  area: evidence
  topic: 'Native checklist: detailed defense, host selection and fitness assertions'
  outcome: unknown
  target_ids:
  - METPO:1000610
  summary: Detailed pathogen-linked oxidative-defense, donor-dependence, host-colonization,
    fitness and selection assertions remain UNASSESSED_SCOPE. They are not validated,
    falsified, repaired or expanded. Literal abstract matches, source identities and
    permitted node/predicate kinds do not establish these mechanisms.
  evidence_ids:
  - edge-sources
  - source-ledger
  - adjudication
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: all seven snippet fields'
  outcome: supported
  target_ids:
  - METPO:1000610
  summary: Four excerpts are exact in the actual canonical abstract, Nature keypoint,
    Lu abstract and SOD abstract. Three repeated Bioresource Technology occurrences
    remain unverified without the body. The SOD passage remains correlational; quotation
    fidelity does not transform it into detailed causal proof.
  evidence_ids:
  - snippets
  - meta-canonical
  - nature-primary
  - lu-primary
  - meta-sod
  - check-microaerotolerant-snippets
- assessment_id: quantity
  area: quantity
  topic: 'Native checklist: intermediate-oxygen attribution and numerical conditions'
  outcome: unknown
  target_ids:
  - METPO:1000610
  summary: The precise edge5 CMR class attribution remains unverified because the
    body was unavailable. Numeric gut conditions and detailed growth or fitness implications
    are UNASSESSED_SCOPE. No threshold, condition optimization or alternative intervention
    is supplied, and no title-based contradiction is asserted.
  evidence_ids:
  - meta-cmr
  - edge-sources
  - access-browser-access-receipts
  - adjudication
- assessment_id: bibliography
  area: evidence
  topic: 'Native checklist: seven works, eight reference forms and fifteen placements'
  outcome: supported
  target_ids:
  - METPO:1000610
  summary: All seven publication identities resolve; the PMID and DOI aliases of the
    canonical paper are reconciled. Fifteen placements retain their actual inspected
    surfaces and access limits. Seven fresh status records provide bounded observations
    only, not exhaustive absence of notices.
  evidence_ids:
  - source-ledger
  - placements
  - publication-status
  - body-reuse
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: whole-record graph and protein scope'
  outcome: supported
  target_ids:
  - METPO:1000610
  summary: All thirteen nodes, eleven edges, three components, three protein classes,
    seven snippets and fifteen events have documentary coverage. Two reviewed label-only
    classes and zero instances are permissible in NONMECHANISTIC context. No connector,
    individual protein example, additional pathway or mechanism completion is required.
  evidence_ids:
  - capture
  - node-edges
  - protein-policy
  - check-corpus-protein-taxa
  - placements
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: canonical-only expression catalog applicability'
  outcome: not_applicable
  target_ids:
  - METPO:1000610
  summary: The canonical species and official type-material aliases have no match
    in the retained official catalog. No organism substitution or downstream gene/module/stress
    query was performed. Catalog noncoverage is not negative phenotype evidence or
    a mandatory-record defect; historical runner bounds remain explicit.
  evidence_ids:
  - expression
  - runner
  - authority-reuse
- assessment_id: ownership
  area: ownership
  topic: 'Native checklist: current maintenance and recurrence'
  outcome: supported
  target_ids:
  - METPO:1000610
  summary: Current node/predicate mappings preserve permitted grounds. Retained typography,
    corrected historic domain annotations and removed dead accession are positive
    maintenance, not current defects. The captured AI canonical-example event explicitly
    targets this record. Only human-acceptance attribution remains unresolved.
  evidence_ids:
  - owners
  - identity
  - canonical-history
  - provenance-assessment
- assessment_id: human-acceptance
  area: provenance
  topic: 'Native checklist: REVIEWED status and acceptance attribution'
  outcome: concern
  target_ids:
  - METPO:1000610
  summary: Fourteen AI events, one automated seed and the captured target-specific
    AI repository event do not attribute human scientific acceptance in the bounded
    ignored-inclusive local search. They are positive maintenance evidence. Private
    or remote acceptance is unknown, and no global absence claim is made.
  evidence_ids:
  - provenance
  - provenance-assessment
  - canonical-history
  - native-policy
- assessment_id: checks
  area: schema
  topic: 'Native checklist: actual focused checks and scoped common reuse'
  outcome: supported
  target_ids:
  - METPO:1000610
  summary: Focused validation, strict validation and snippet verification passed.
    Manual quotation review covers all seven fields. Historical B6 QC and common diagnostics
    retain original dates, failures/retry, baselines and skips. All 61 captured input
    hashes match; no fresh corpus execution is claimed.
  evidence_ids:
  - check-microaerotolerant-validate
  - check-microaerotolerant-strict
  - check-microaerotolerant-snippets
  - check-batch006-qc
  - reuse-supplement
  - capture
findings:
- finding_id: human-acceptance-link
  issue_key: microaerotolerant-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Local provenance does not attribute human scientific acceptance
  description: 'REVIEWED status accompanies fifteen events: fourteen explicit AI maintenance
    events and one automated seed. The captured repository event explicitly documents
    the AI-authored canonical-example addition. The inspected ignored-inclusive own-repository
    provenance does not attribute human scientific acceptance for this target and
    revision. Positive maintenance is preserved. Private or remote acceptance is unknown;
    this is not a claim that no human review ever occurred.'
  target_ids:
  - METPO:1000610
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - provenance-assessment
  - canonical-history
  - native-policy
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/microaerotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: attribute-human-acceptance
  description: Link an existing human scientific acceptance decision or leave attribution
    unresolved for the curator.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000610
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/microaerotolerant.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies the reviewed revision and scope, including the qualified
    pass, inaccessible precise source wording and unassessed detailed biological claims.
    Preserve all fifteen events and the captured canonical-example history.
  - Automated seeding, successful checks, AI maintenance and this review do not substitute
    for human acceptance. Do not presume private or remote decisions absent. Any later
    scientific changes require separately authorized guarded curation and append-only
    provenance.
limitations:
- General definition meaning is supported by the exact pinned ontology and the actual
  Nature keypoint. The nearest Bioresource Technology source supplies positive mixed-community
  context, while its exact definition phrase and three repeated excerpts remain unverified
  without article-body access.
- The CMR intermediate-oxygen class attribution remains unknown. HTTP200 redirect-only
  text, failed EPMC/BioC retrievals and publisher denials/challenges are not article
  bodies, and unavailable text or titles alone do not prove false claims.
- Detailed pathogen-linked oxidative-defense, donor-dependence, host-colonization,
  fitness and selection biology, numeric gut conditions and growth optimization are
  UNASSESSED_SCOPE. No mechanism repair, reconstruction, new target, condition or
  intervention is supplied.
- Canonical species and type-material identity and primary phenotype classification
  are positively supported. No new measured assay, complete-body reading or universal
  mechanism across the species is implied.
- The Nature keypoint is general classification evidence. Lu and SOD excerpts were
  checked for wording only; the SOD abstract remains correlational. Exact quotation,
  valid ontology identity and permitted predicate roles do not certify detailed biology.
- The systems label of node12 permits either machinery wording or an activity reading;
  its description allows the current process interpretation. External environmental
  gradients are not automatically cellular STATE nodes. These are bounded precision
  limitations, not forced retypes.
- Three local predicate IDs remain provisional proposal terms rather than active upstream
  terms. Their documentary roles are permitted. Free phrases do not acquire unasserted
  RO or Biolink restrictions, and no OWL reasoner result is claimed.
- Three components, two label-only protein classes and zero instances are allowed
  in NONMECHANISTIC context. Optional absent instances, catalog coverage or connectors
  are not defects, and historical deleted accessions/domain IDs are not current assertions.
- The identity addendum supplies direct positive IAO_0100001 replacement evidence
  from obsolete1000351 to1000610. It qualifies the frozen assessment without inferring
  replacement from deprecation or changing current exact identity.
- Fresh source and official identity responses retain actual times. Nature BioC retains
  its 12:10 acquisition, Lu BioC its 08:25 acquisition, and the two reused chemical
  responses their 12:08 acquisitions. Later copying, hash verification and independent
  reading are distinct events.
- Catalog and bounded runner receipts retain original 07:36 and 09:27/08:17 times.
  No canonical catalog match or substitute-organism query was used; noncoverage is
  not negative evidence. No fresh B7 or global runner absence is asserted.
- Publication-status inspection is bounded to seven current indexed records. The ignored-inclusive
  local provenance search does not cover private or remote acceptance. Fourteen AI
  events, one seed and the target-specific AI repository event remain positive maintenance,
  not human acceptance.
- The captured provider report is a lead and provenance context only, not a claim
  of full report reading or independent primary mechanism verification.
- Reused B6 QC, B4 corpus protein audit, B3 history and OLD product failures/retry
  retain original times and meanings. The qualified proof distinguishes 1,277 history
  YAML records from 1,278 total files. Builder preparation performs no native validation,
  review save, scientific input, Git, state or environment mutation.
notes:
- One minor finding and zero major findings. Both canonical and native verdicts are
  pass_with_limitations. Positive identity, canonical and general context evidence
  supports the verdict; explicit limitations retain unknown source wording and unassessed
  biology.
- All 61 captured input hashes match. Coverage includes thirteen nodes, eleven edges,
  three components, three protein classes, two label-only classes, zero instances,
  fifteen events, seven publications, eight literal reference forms, fifteen placements
  and seven snippets.
- Source assessment completed at12:16:58.187282 UTC and grounding at12:16:48.780126
  UTC. Final parent adjudication is12:21:05.808705 UTC; the separate positive replacement
  addendum is12:21:24.813986 UTC. Original acquisition dates remain distinct from
  later assessment times.
tags:
- record-review
- microaerotolerant
- environment
- pass-with-limitations
native_verdict: pass_with_limitations
```
