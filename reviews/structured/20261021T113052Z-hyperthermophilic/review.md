# Whole-record review of hyperthermophilic

- Review: 20261021T113052Z-hyperthermophilic
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T11:22:39.905671Z
- Finished UTC: 2026-10-21T11:30:52Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Active identity, the typical temperature definition and the canonical P. furiosus optimum have direct support. Two major findings concern four imported RO endpoint conflicts and a methylation claim overgeneralized from a valid three-culture abundance result. Four minors concern membrane-composition facet wording, quotation continuity/context, tentative rigidity wording and local human-acceptance attribution. All thirteen nodes and eleven edges are covered. Eleven works support fifteen placements; five of seven snippets are literal exact, one is abridged and one remains unknown. Valid functional grounding, optional proteins and two contextual graph components are retained.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: One complete maintained environmental TraitRecord, fully read with its parent, four captured AI history contexts and the 350-line historical provider report. The final 63-input capture preserves the original 59. All thirteen nodes, eleven edges, one canonical example, one top-level organism example, eleven assigned works, fifteen placements, seven snippets and nineteen history events are accounted for. Existing benign physiological claims receive source-bounded review. No new route, molecular target, intervention, experimental condition or optimization is supplied; incidental pathogen-specific biology remains unassessed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000617 | data/traits/environment/hyperthermophilic.yaml | maintained | hyperthermophilic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000617 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000617 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000617 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1000617 | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000617 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000617 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000617 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused LinkML validation | passed | True | METPO:1000617 | Actual execution at 11:22:56–57Z passed. Structural acceptance does not establish scientific support. |
| Focused strict validation | passed | True | METPO:1000617 | Actual execution at 11:22:56–58Z passed. Native acceptance is distinct from external semantic and source assessment. |
| Initial focused snippet invocation | failed | False | METPO:1000617 | Actual invocation at 11:22:56Z exited 2 because the supplied script path did not exist. No source verification occurred. This optional failed invocation is superseded by the successful required retry. |
| Sandbox snippet retry | failed | False | METPO:1000617 | Actual execution at 11:23:02–45Z exited 2 with DNS failures for six references. It proves nothing about source support and is superseded by the network retry. |
| Successful focused network retry | passed | True | METPO:1000617 | Actual execution at 11:23:52–11:24:03Z exited 0: seven snippets over six references, two VERIFIED, two NOT_IN_ABSTRACT and three UNRESOLVED. Manual source assessment is separate; successful command completion does not verify every quotation. |
| Reused corpus protein/taxon audit | passed | True | METPO:1000617 | B4 execution at 08:55:04–10Z passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC, one protected, zero gaps and zero errors. Historical corpus coverage is not a new focused scientific check. |
| Reused full-corpus QC | passed | True | METPO:1000617 | B5 actual execution at 10:21:03–10:23:38Z passed. Separate B6 common/scientific byte comparison and environment readiness support scoped historical reuse. |
| UniProt instance audit applicability | not_applicable | False | METPO:1000617 | Five generic protein classes assert zero instances or accessions. Four are REVIEWED_LABEL_ONLY; the remaining functional GO grounding is allowed. Deleted historical UniProt grounds are not current audit targets. |

## Scientific And Domain Assessments

### Native checklist: ID, related synonym, definition and parent

identity: supported. Targets: METPO:1000617.

Active METPO:1000617 and broader temperature preference agree with the current record. The related synonym is literal upstream wording. Retained scientific typography preserves the same typically-at-least-80 boundary; no fallback, exact-equivalence or obsolete-replacement inference is needed.

### Native checklist: nearest-source definition and typical boundary

evidence: supported. Targets: METPO:1000617.

The actual OUP abstract directly supports the assigned optimum classification and both literal range occurrences. PATO supplies relative temperature through explicit closeMatch, while numeric context comes from definition/source. The environmental selection relation is contextual interpretation rather than a measured evolutionary experiment, retained as a limitation.

### Native checklist: canonical optimum and top organism example

evidence: supported. Targets: METPO:1000617.

The current taxon resolves to P. furiosus. The original Springer title/abstract directly supports approximately 100 °C optimum, and PMID9348040 contains the top organism-classification phrase in its title. Other-record rejected comparator measurements do not contradict this independently supported source. No new growth conditions or species-uniform assay is inferred.

### Native checklist: native facets and optional completeness

representation: concern. Targets: METPO:1000617.

Node 5 leaves composition versus material membrane component unclear; CELLULAR_LOCALIZATION does permit actual components, so this is bounded facet precision. Rigidity is correctly a QUALITY. Five protein classes, four label-only nodes, zero instances and two NONMECHANISTIC components require no token accessions or invented links.

### Native checklist: all thirteen nodes

grounding: supported. Targets: METPO:1000617.

Active trait, PATO closeMatch, allowed reverse-gyrase functional GO ground and exact macrocyclic-archaeol identity are supported. Other chemical and protein classes may remain ungrounded or label-only. Node 5 facet wording is assessed separately, not promoted to an unsupported identifier failure.

Nodes 0–1: trait and temperature context. Nodes 2–4: material protein classes, including an allowed functional ground. Node 5: composition/component precision. Node 6: optional ungrounded chemical. Node 7: protein aggregate. Node 8: oxidative-damage event/process. Nodes 9–10: material lipid and enzyme. Node 11: valid rigidity QUALITY. Node 12: exact named chemical, with effect certainty assessed separately.

### Native checklist: all eleven relations

consistency: concern. Targets: METPO:1000617.

RO assignments on edges 2, 3, 9 and 10 conflict with process endpoint meanings. Material subjects of RO:0002326 are not themselves invalid; its trait/quality objects are. Local selects-for/confers fit declared roles. Free-text edges 5–8 carry no unasserted RO constraints, and optional IDs are not completeness defects.

Edges 0/1/4: compatible local proposal roles. Edge 2: trait object conflicts with process range. Edge 3: two material proteins conflict with regulation roles. Edges 5/6: free-text protective context. Edges 7/8: free-text production/function context. Edge 9: quality object conflicts with process range. Edge 10: chemical/quality endpoints conflict with process regulation. Retain valid material and quality facets rather than forcing retypes.

### Native checklist: all eleven nearest-source claims

evidence: concern. Targets: METPO:1000617.

Most existing contextual claims have positive inspected support with taxon and evidence-tier bounds. PNAS supports increased GMGT abundance in all three cultures, but its methylation result is species-dependent and directly contradicts the all-three note. Rigidity interpretations remain tentative. Chaperonin exact body support is unknown; cDPG protective statements are cited background, not the principal new experiment.

### Native checklist: eleven assigned works and status scope

evidence: supported. Targets: METPO:1000617.

All eleven identities and fifteen placements resolve through eight fresh indexed articles, two registry/publisher identities and one historical indexed abstract. PNAS links its preprint, not a corrective notice. No global status absence is claimed. Metadata-only and browser-preview access remain distinct from five acquired JATS bodies.

### Native checklist: seven occurrences, continuity and context

evidence: concern. Targets: METPO:1000617.

Five occurrences are literal exact, including the reverse-gyrase prefix that immediately precedes an exception. One enzyme excerpt is an explicit noncontiguous abridgement with supported meaning; the chaperonin body quotation remains unknown. Group continuity/context precision as one minor without calling the exact prefix nonliteral or declaring a universal graph claim.

### Native checklist: optimum, abundance and methylation measures

quantity: concern. Targets: METPO:1000617.

The canonical optimum and typical class boundary have direct source support. PNAS relative abundance and degree of methylation are distinct measured outcomes and must not be joined as a uniform result. No unit conversion, cultivation recommendation, new threshold or class-wide monotonic behavior is inferred.

### Native checklist: whole-record and contextual graph coverage

completeness: supported. Targets: METPO:1000617.

Thirteen nodes, eleven edges, both example locations, eleven works, fifteen placements, seven snippets and nineteen history events are covered. The disconnected protective-solute context is allowed in this NONMECHANISTIC graph. Unknown source access and conditional biology are explicit; no token route, accession or connector is required.

### Native checklist: canonical catalog applicability

evidence: not_applicable. Targets: METPO:1000617.

The complete retained catalog has no canonical Pyrococcus or genus entry. No alternative organism was substituted and no downstream module query performed. Catalog noncoverage is not negative phenotype evidence or a mandatory dataset defect.

### Native checklist: mapping recurrence and maintained type decisions

ownership: concern. Targets: METPO:1000617.

Current record, wildcard predicate mappings and existing-ID skips own recurrence of relation conflicts. Preserve the explicit rigidity QUALITY decision, permitted GO functional ground, local proposal roles and typography retention. Wider canonical searches found context rather than a target-specific writer; record/history ownership remains and no global absence is inferred.

### Native checklist: REVIEWED and local human attribution

provenance: concern. Targets: METPO:1000617.

Eighteen AI record changes plus seed and four captured AI contexts document maintenance. The inspected local material does not attribute a human acceptance decision for this target. Remote/private review is unassessed; this is bounded traceability rather than no-history or no-human-review-ever.

### Native checklist: actual failures, successful retry and historical reuse

schema: supported. Targets: METPO:1000617.

Focused validation and strict checks passed. Initial snippet script-path failure and DNS retry failure remain optional superseded attempts; the actual required network retry passed with mixed item statuses. B4/B5/B3/OLD checks retain original dates, failures, retry and skips. These invocation failures are not structured-review serialization failures.

## Findings

### ro-endpoint-roles: Four imported RO relations conflict with represented endpoint kinds

major / open / confirmed; issue key: hyperthermophilic-ro-endpoint-roles.

Edges 2 and 9 use RO:0002326 with trait and membrane-quality objects rather than processes; their material protein/chemical subjects are compatible. Edge 3 uses process regulation between material proteins. Edge 10 uses positive process regulation from a chemical to a quality. Preserve valid material, functional and QUALITY facets while reconciling these imported relations. The allowed GO functional ground is not an additional defect, and native acceptance is not external semantic validity.

### methylation-scope: The evidence note extends a three-culture abundance result to methylation

major / open / confirmed; issue key: hyperthermophilic-methylation-scope.

Edge 7 notes combine increased GMGT production and methylation as a broad conclusion across three cultured archaea. PNAS paragraphs 21–22 support the all-three relative-abundance result, while paragraph 24 explicitly reports no clear methylation trend in A. profundus and a different result in another studied species. The combined note materially overgeneralizes the measured outcome. Retain the supported abundance statement and qualify only the methylation claim; no blanket false-chemistry or source-invalidity inference is made.

### composition-facet: Membrane composition and material-component wording leave the intended facet unclear

minor / open / confirmed; issue key: hyperthermophilic-composition-facet.

Node 5 is CELLULAR_LOCALIZATION but names composition and describes lipid features. Native policy permits actual material membrane components, so this is a bounded attribute-versus-component clarification rather than a blanket prohibition on lipids in that enum. Make the intended existing referent consistent without prescribing a forced process retype or new mechanism.

### quotation-continuity-context: Two snippets need contiguous wording or immediate source qualification

minor / open / confirmed; issue key: hyperthermophilic-quotation-continuity-context.

Edge 1 visibly uses an ellipsis joining separated parts of a supported source sentence. Edge 2 is a literal substring, but stops just before an explicit exception in the same sentence. The graph prose already describes association, so do not infer that the entire graph asserts universal presence. Group these as bounded evidence continuity/context precision; the unknown chaperonin body quotation is not called false.

### rigidity-certainty: Node and edge wording is firmer than the qualified rigidity interpretation

minor / open / confirmed; issue key: hyperthermophilic-rigidity-certainty.

Edges 9 and 10 and node 12 describe physical rigidity/stability effects directly, while the nearest papers frame them as proposed or possible and discuss contextual limitations. Existing evidence notes already retain thought/could qualifiers. Align these descriptions with the supported confidence rather than treating the effect as disproven. This source-certainty concern is separate from imported predicate endpoint semantics.

### human-acceptance-link: Inspected local provenance does not attribute human scientific acceptance

minor / open / confirmed; issue key: hyperthermophilic-human-acceptance-link.

REVIEWED is accompanied by eighteen AI changes and seed. Four fully read AI infrastructure/batch/other-record histories document context and maintained decisions, not a current-target human acceptance decision. Ignored-inclusive local searches have explicit bounds; remote/private content remains unassessed. This is a traceability concern, not a claim that no human review has ever occurred.

## Recommended Actions And Acceptance Checks

### reconcile-ro-roles

Reconcile the four imported RO assignments with the current represented entity kinds.

- Any retained identifier satisfies inherited process meanings. Preserve legitimate material proteins, chemicals, trait and QUALITY nodes rather than forcing retypes.
- Keep the permitted functional GO ground and local/free-text predicates distinct; no replacement route or arbitrary CURIE is prescribed.
- After separately authorized curation, use guarded writes, append-only record/repository history, focused validation/strict/source checks and relevant maintained audits/QC; regenerate affected outputs through maintained recipes. This review makes no scientific mutation.

### bound-methylation-claim

Separate the supported abundance result from the narrower methylation observation.

- The note preserves positive all-three abundance evidence and does not claim a uniform all-three methylation increase contradicted by paragraph 24.
- Retain studied-taxon and outcome scope without adding experimental conditions, optimization or universal extrapolation.
- After separately authorized curation, use guarded writes, append-only record/repository history, focused validation/strict/source checks and relevant maintained audits/QC; regenerate affected outputs through maintained recipes. This review makes no scientific mutation.

### clarify-composition-facet

Clarify whether the existing node denotes membrane material or its compositional attribute.

- Label, description and native entity kind consistently express the intended existing facet. Native component allowance remains respected.
- No forced pathway, protein instance or additional mechanism is required.
- After separately authorized curation, use guarded writes, append-only record/repository history, focused validation/strict/source checks and relevant maintained audits/QC; regenerate affected outputs through maintained recipes. This review makes no scientific mutation.

### preserve-quotation-context

Use contiguous source wording and preserve the adjacent qualification.

- The enzyme snippet satisfies the native contiguous-excerpt convention while retaining supported meaning. The literal gyrase excerpt does not silently discard its immediate source qualification.
- Retain association wording and the distinct unknown chaperonin-body status; no universal requirement or source-falsity inference is introduced.
- After separately authorized curation, use guarded writes, append-only record/repository history, focused validation/strict/source checks and relevant maintained audits/QC; regenerate affected outputs through maintained recipes. This review makes no scientific mutation.

### align-rigidity-confidence

Align node and edge certainty with qualifications already retained in the evidence notes.

- Descriptions preserve the papers’ tentative interpretation and contextual limits, without presenting it as a universal direct measurement or disproven effect.
- Relation endpoint semantics remain a separate issue; no new biological mechanism or experimental validation is prescribed.
- After separately authorized curation, use guarded writes, append-only record/repository history, focused validation/strict/source checks and relevant maintained audits/QC; regenerate affected outputs through maintained recipes. This review makes no scientific mutation.

### attribute-human-acceptance

Link existing human scientific acceptance or obtain it through the established process.

- Acceptance identifies the revision and scope, including unknown source text and qualified physical interpretations. Preserve current AI and contextual history.
- Automated validation and this agent review do not substitute for human acceptance; reassess status if necessary.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep-006.nq5qngor/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the current 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-hyperthermophilic-validate | /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-validate.log; Executed 2026-10-21T11:22:56Z through 2026-10-21T11:22:57Z; metadata hyperthermophilic-validate.json | context_only | Actual execution at 11:22:56–57Z passed. Structural acceptance does not establish scientific support. |
| check-hyperthermophilic-strict | /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-strict.log; Executed 2026-10-21T11:22:56Z through 2026-10-21T11:22:58Z; metadata hyperthermophilic-strict.json | context_only | Actual execution at 11:22:56–58Z passed. Native acceptance is distinct from external semantic and source assessment. |
| check-hyperthermophilic-snippets | /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-snippets.log; Executed 2026-10-21T11:22:56Z through 2026-10-21T11:22:56Z; metadata hyperthermophilic-snippets.json | context_only | Actual invocation at 11:22:56Z exited 2 because the supplied script path did not exist. No source verification occurred. This optional failed invocation is superseded by the successful required retry. |
| check-hyperthermophilic-snippets-retry | /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-snippets-retry.log; Executed 2026-10-21T11:23:02Z through 2026-10-21T11:23:45Z; metadata hyperthermophilic-snippets-retry.json | context_only | Actual execution at 11:23:02–45Z exited 2 with DNS failures for six references. It proves nothing about source support and is superseded by the network retry. |
| check-hyperthermophilic-snippets-network-retry | /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-snippets-network-retry.log; Executed 2026-10-21T11:23:52Z through 2026-10-21T11:24:03Z; metadata hyperthermophilic-snippets-network-retry.json | context_only | Actual execution at 11:23:52–11:24:03Z exited 0: seven snippets over six references, two VERIFIED, two NOT_IN_ABSTRACT and three UNRESOLVED. Manual source assessment is separate; successful command completion does not verify every quotation. |
| check-corpus-protein-taxa | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log; Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json | context_only | B4 execution at 08:55:04–10Z passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC, one protected, zero gaps and zero errors. Historical corpus coverage is not a new focused scientific check. |
| check-batch005-qc | /private/tmp/traitmech-record-sweep-005.klfwsp1f/batch005-qc.log; Executed 2026-10-21T10:21:03Z through 2026-10-21T10:23:38Z; metadata batch005-qc.json | context_only | B5 actual execution at 10:21:03–10:23:38Z passed. Separate B6 common/scientific byte comparison and environment readiness support scoped historical reuse. |
| capture | Native final selected-record capture; 63 inputs at 11:24:42.075849–11:24:43.536329Z | supports | All current captured hashes match and preserve the original 59. Parent and four AI histories were fully read as context, not additional review targets. |
| preparation | Whole-record and provenance preparation; Complete target, parent, four histories and 350-line provider report | context_only | Factual coverage was derived before adjudication. Historical report recommendations are provenance, not instructions or independently verified primary evidence. |
| record | data/traits/environment/hyperthermophilic.yaml; Entire current record; thirteen nodes, eleven edges and nineteen events | partial | The qualitative temperature class is REVIEWED with eighteen explicit AI changes plus seed. Current assertions are distinguished from historical deleted identifiers and other-record comparisons. |
| native-policy | Native field-by-field checklist; Evidence, completeness, facet consistency and Status/audit guidance | supports | Source support, consistent represented meanings and attributed human acceptance apply. Optional protein/dataset fields and NONMECHANISTIC contextual components do not require artificial completion. |
| grounding-policy | Native grounding policy; Lines 75–88, taxon-agnostic enzyme functional grounds | supports | An enzymatic GO molecular-function ground may describe the functional facet of a protein class. GO:0160097 is not an automatic protein/activity error or mandatory family-accession replacement. |
| snippet-policy | Native curation playbook; Lines 649–650 and 673–676, contiguous verbatim evidence and interpretation | supports | A literal excerpt must retain source wording and relevant context. An explicit ellipsis can preserve meaning while still falling short of the native contiguous-snippet convention. |
| native-types | Native CausalNodeTypeEnum; Component/localization and measurable-attribute definitions, lines 683–700 | supports | CELLULAR_LOCALIZATION permits real cellular components; composition may denote an attribute instead. Membrane rigidity is a valid QUALITY and need not be forced into a process to satisfy an imported relation. |
| reuse | B6 common-input comparison; Original verification at 10:14:46.298715Z | supports | 1130 traits, 1278 history files and 19 common inputs match the preceding batch. This setup receipt predates B5 final QC, whose actual result is recorded separately. |
| reuse-supplement | B5 checks and B6 readiness supplement; Original supplement 10:28:10.859819Z; QC 10:21:03–10:23:38Z | supports | Historical command/log hashes, readiness, failed attempts and successful retry remain distinct. B3 validated 1277 history records while byte comparison inventories 1278 files. No fresh B6 corpus execution is claimed. |
| identity | Pinned METPO identity, hierarchy and retention policy; METPO:1000617 and parent 1000613; active-review row 124 and release-delta row 1292 | supports | Active identity and related synonym agree. The local ≥80 °C typography is explicitly retained and semantically agrees with upstream &gt;=80 C. Typical boundary wording is not a newly invented universal cutoff. |
| go-functional | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0160097; Active reverse-gyrase molecular function; original access completed 09:50:46.974059Z | supports | The functional ground agrees with the current named protein class under native policy. This identity check does not establish universal presence or organism-level sufficiency. |
| pato-temperature | https://www.ebi.ac.uk/ols4/api/ontologies/pato/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPATO_0001305; Relative increased-temperature quality; original access completed 09:50:46.963303Z | supports | The explicit closeMatch supplies relative temperature meaning. Numeric context comes from the trait definition and cited source, so no PATO numeric-threshold finding is assigned. |
| chemical | https://www.ebi.ac.uk/chebi/backend/api/public/compound/193595/; Fresh request 11:23:20.504731–11:23:21.180326Z | supports | The released macrocyclic-archaeol identity matches the named chemical. Source claims about physical effects remain a separate question. |
| taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2261&amp;retmode=xml; Fresh request 11:23:20.505352–11:23:20.878116Z | supports | NCBI2261 resolves to Pyrococcus furiosus. The optimum is supported separately by the original publisher preview, not inferred from taxonomy. |
| local-authority | Maintained mappings, local proposals and writers; Node rows 56/68/184; predicate rows 10–11/33/65/102; v2/v8 | supports | Functional GO and relative-temperature closeMatch mappings are permitted. Local selects-for/confers roles fit. Existing-ID skips and wildcard mappings explain recurrence; rigidity QUALITY is explicitly maintained. |
| predicate-authority | Retained recursive RO semantics; Original RO access 08:04:46.869674Z; BFO context 09:52:45.989262Z; integration 11:26:16.386370Z | supports | RO:0002326 inherits material/process roles through RO:0002216 → RO:0002500 → RO:0002595. RO:0002329 is another superproperty branch, not itself the material/process constraint. RO:0002211 and RO:0002213 require process-regulation roles. Four current assignments conflict; this is semantic assessment, not an executed OWL failure. |
| authority-reuse | Original authority and catalog reuse chain; Hash/copy verification at 11:23:56.648415Z | supports | Reused GO/PATO, RO, catalog and runner receipts retain original acquisition bounds and hashes. Fresh ChEBI and taxonomy are separate. Copying or integration is not a new external request. |
| grounding-ledger | Complete documentary grounding assessment; Thirteen nodes, eleven edges, two components and 63 matching inputs | partial | Identity, current chemical/function grounds and optional protein scope are supported. One grouped RO concern and bounded membrane-composition facet concern remain; no new topology or accession requirement is imposed. |
| node-edges | Complete current node and edge ledger; nodes[0–12] and edges[0–10], zero-based | partial | Every endpoint resolves. Four grounded RO assignments conflict with endpoint meanings; free-text edges 5–8 do not inherit unasserted RO constraints. Two contextual components are compatible with NONMECHANISTIC scope. |
| owners | Maintained mappings, type migration and identity writers; Grounding guards 156–174/152–176; rigidity migration 110–121; typography retention 125–150 | supports | Current mapping/writer owners can retain or recreate imported relation conflicts. Preserve valid QUALITY, material proteins and chemicals, current functional grounds and retained typography. Historical withdrawn grounds are not current defects. |
| provenance | Bounded ignored-inclusive target and node provenance search; Completed 11:24:11.071611Z; 199 matching files, no targeted saved review | partial | Eighteen AI changes plus seed and four captured AI history contexts establish maintenance but do not attribute current-target human acceptance. Other-record comparator observations do not refute the present canonical example. |
| expression | Canonical catalog applicability; Original official catalog request 07:36:12.732638–07:36:12.858149Z; twenty organisms and twenty-eight datasets | context_only | No Pyrococcus furiosus or genus match occurs in the complete retained catalog. No alternative archaeon is substituted, and noncoverage is not negative phenotype evidence. No downstream gene/module query occurred. |
| runner | Retained structured-runner discovery; B5 PATH/project bounds 09:27:57Z and external bounds 08:17:15Z | context_only | No callable runner was found within those historical scopes. The official catalog is the fallback; no fresh B6 or global absence claim is made. |
| source-ledger | Complete source assessment; Eleven assigned works and fifteen placements; finalized 11:26:52.303372Z | partial | Positive definition, canonical optimum and existing contextual claims are separated from the methylation overgeneralization, quotation precision and tentative rigidity interpretation. Acquired bodies are assessed only at declared windows. |
| placements | Complete citation-placement inventory; Definition, both example locations and all eleven edges; fifteen placements | supports | All assigned works and placements are accounted for. Registry identity, actual publisher access, fresh indexed fields and historical abstract reuse remain distinct. |
| snippets | Complete seven-occurrence quotation ledger; Five literal exact including one immediately qualified prefix; one abridgement and one unknown | partial | The exact reverse-gyrase substring stops before the source exception. The enzyme ellipsis is meaningful but noncontiguous. The chaperonin body quotation remains unknown; unavailable text is not falsity. |
| edge-sources | Complete nearest-edge source ledger; edges[0–10], each assessed at its actual source window | partial | The all-three GMGT abundance result is positive, while all-three methylation is contradicted. Rigidity interpretations remain tentative. Generic cDPG protective claims are background citing earlier work, not the principal new experiment. |
| metadata-definition | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111%2Fj.1574-6976.1996.tb00233.x&amp;format=json&amp;resultType=core; Actual indexed query 2026-10-21T11:23:22.073530+00:00 through 2026-10-21T11:23:22.790324+00:00 | context_only | Only returned identity, title, abstract and status fields are used. Eight queries yielded indexed articles; definition, canonical and thermal DOI misses are resolved through separate documented sources. No full-body or unrestricted status coverage is implied. |
| registry-definition | https://api.crossref.org/works/10.1111%2Fj.1574-6976.1996.tb00233.x; Actual registry query 2026-10-21T11:23:52.309518+00:00 through 2026-10-21T11:23:52.636696+00:00 | supports | Registry identity supports the citation. Actual publisher title/abstract supplies the scientific observation; registry identity alone does not establish it. |
| metadata-organism | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9348040+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Actual indexed query 2026-10-21T11:23:22.073903+00:00 through 2026-10-21T11:23:22.823148+00:00 | context_only | Only returned identity, title, abstract and status fields are used. Eight queries yielded indexed articles; definition, canonical and thermal DOI misses are resolved through separate documented sources. No full-body or unrestricted status coverage is implied. |
| metadata-canonical | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1007%2FBF00413027&amp;format=json&amp;resultType=core; Actual indexed query 2026-10-21T11:23:22.073982+00:00 through 2026-10-21T11:23:22.839849+00:00 | context_only | Only returned identity, title, abstract and status fields are used. Eight queries yielded indexed articles; definition, canonical and thermal DOI misses are resolved through separate documented sources. No full-body or unrestricted status coverage is implied. |
| registry-canonical | https://api.crossref.org/works/10.1007%2FBF00413027; Actual registry query 2026-10-21T11:23:52.360801+00:00 through 2026-10-21T11:23:52.636645+00:00 | supports | Registry identity supports the citation. Actual publisher title/abstract supplies the scientific observation; registry identity alone does not establish it. |
| metadata-proteins | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FMMBR.65.1.1-43.2001&amp;format=json&amp;resultType=core; Actual indexed query 2026-10-21T11:23:22.074024+00:00 through 2026-10-21T11:23:22.820553+00:00 | context_only | Only returned identity, title, abstract and status fields are used. Eight queries yielded indexed articles; definition, canonical and thermal DOI misses are resolved through separate documented sources. No full-body or unrestricted status coverage is implied. |
| metadata-gyrase | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffmicb.2021.661411&amp;format=json&amp;resultType=core; Actual indexed query 2026-10-21T11:23:22.790360+00:00 through 2026-10-21T11:23:23.526421+00:00 | context_only | Only returned identity, title, abstract and status fields are used. Eight queries yielded indexed articles; definition, canonical and thermal DOI misses are resolved through separate documented sources. No full-body or unrestricted status coverage is implied. |
| metadata-chaperonins | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrmicro866&amp;format=json&amp;resultType=core; Actual indexed query 2026-10-21T11:23:22.820594+00:00 through 2026-10-21T11:23:23.550500+00:00 | context_only | Only returned identity, title, abstract and status fields are used. Eight queries yielded indexed articles; definition, canonical and thermal DOI misses are resolved through separate documented sources. No full-body or unrestricted status coverage is implied. |
| metadata-thermal | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fs0300-9629%2897%2900003-0&amp;format=json&amp;resultType=core; Actual indexed query 2026-10-21T11:23:22.823185+00:00 through 2026-10-21T11:23:23.582597+00:00 | context_only | Only returned identity, title, abstract and status fields are used. Eight queries yielded indexed articles; definition, canonical and thermal DOI misses are resolved through separate documented sources. No full-body or unrestricted status coverage is implied. |
| metadata-cdpg | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffmicb.2023.1267570&amp;format=json&amp;resultType=core; Actual indexed query 2026-10-21T11:23:22.839883+00:00 through 2026-10-21T11:23:23.569740+00:00 | context_only | Only returned identity, title, abstract and status fields are used. Eight queries yielded indexed articles; definition, canonical and thermal DOI misses are resolved through separate documented sources. No full-body or unrestricted status coverage is implied. |
| metadata-gms | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073%2Fpnas.2318761121&amp;format=json&amp;resultType=core; Actual indexed query 2026-10-21T11:23:23.526463+00:00 through 2026-10-21T11:23:24.194350+00:00 | context_only | Only returned identity, title, abstract and status fields are used. Eight queries yielded indexed articles; definition, canonical and thermal DOI misses are resolved through separate documented sources. No full-body or unrestricted status coverage is implied. |
| metadata-rigidity | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-024-49650-x&amp;format=json&amp;resultType=core; Actual indexed query 2026-10-21T11:23:23.550540+00:00 through 2026-10-21T11:23:24.224127+00:00 | context_only | Only returned identity, title, abstract and status fields are used. Eight queries yielded indexed articles; definition, canonical and thermal DOI misses are resolved through separate documented sources. No full-body or unrestricted status coverage is implied. |
| metadata-macrocyclic | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2Fmsystems.01159-22&amp;format=json&amp;resultType=core; Actual indexed query 2026-10-21T11:23:23.569780+00:00 through 2026-10-21T11:23:24.404378+00:00 | context_only | Only returned identity, title, abstract and status fields are used. Eight queries yielded indexed articles; definition, canonical and thermal DOI misses are resolved through separate documented sources. No full-body or unrestricted status coverage is implied. |
| body-gyrase | DOI:10.3389/fmicb.2021.661411; PMC8185306 body paragraph31, with paragraph30 context; actual acquisition 2026-10-21T11:23:50.845127+00:00 through 2026-10-21T11:23:52.360777+00:00 | supports | Body paragraph 31 contains the literal quoted prefix and an immediate exception. Preserve the existing association wording; do not infer universal presence or necessity. |
| body-cdpg | DOI:10.3389/fmicb.2023.1267570; PMC10690619 abstract; body paragraph5; actual acquisition 2026-10-21T11:23:50.845375+00:00 through 2026-10-21T11:23:52.299701+00:00 | supports | Abstract and paragraph 5 report existing protective roles as background with earlier citations. Preserve methanogen and model biochemical context; no universal assay of every archaeal protein or new mechanism is inferred. |
| body-gms | DOI:10.1073/pnas.2318761121; PMC11214058 body paragraphs3,5,20–26; especially21,Figure5caption22,and24; actual acquisition 2026-10-21T11:23:50.845485+00:00 through 2026-10-21T11:23:52.309497+00:00 | partial | Paragraphs 21–22 positively support increased GMGT abundance in all three cultures. Paragraph 24 reports no clear methylation trend in A. profundus, contradicting the all-three methylation note. Existing enzyme-function context is supported without organism-wide indispensability. |
| body-rigidity | DOI:10.1038/s41467-024-49650-x; PMC11186832 body paragraph1; actual acquisition 2026-10-21T11:23:50.845663+00:00 through 2026-10-21T11:23:52.987146+00:00 | supports | Introduction paragraph 1 describes the rigidity contribution as proposed and reports an opposing temperature-abundance observation. It does not establish a universal directly measured physical effect. |
| body-macrocyclic | DOI:10.1128/msystems.01159-22; PMC10134847 body paragraphs45–46; actual acquisition 2026-10-21T11:23:52.299723+00:00 through 2026-10-21T11:23:53.511689+00:00 | supports | Discussion paragraphs 45–46 qualify the physical interpretation as an assumption and possibility and report contextual limits. Preserve those qualifiers without declaring the suggested effect false. |
| definition-primary | DOI:10.1111/j.1574-6976.1996.tb00233.x; Actual OUP HTML abstract line 24; root observation recorded 11:26:12.538274Z | supports | The actual publisher abstract verifies the assigned optimum-range wording and definition context. Agent PDF/HTML observations are independently retained. This hashes the browser receipt, not an uncollected article body. |
| canonical-primary | DOI:10.1007/BF00413027; Springer title and abstract lines 11/36–39; root observation recorded 11:24:10.360965Z | supports | The actual original publisher preview directly supports P. furiosus and its approximately 100 °C optimum. Subscription preview only; no full article, new cultivation conditions or strain optimization is claimed. |
| enzyme-primary | DOI:10.1128/MMBR.65.1.1-43.2001; Source-agent actual ASM Summary line 83 at 11:23:45–47Z | supports | Both selected phrase segments occur in the source sentence, with omitted intervening wording. Meaning is supported but the current snippet is not contiguous. The root separately received 403; that does not refute the agent’s actual publisher observation. Browser receipt hash is not article-body hash. |
| thermal-abstract | https://pubmed.ncbi.nlm.nih.gov/9406426/; Original indexed abstract request 09:29:00.590499–09:29:01.331044Z, second sentence | supports | The original indexed response identifies the DOI and contains the exact membrane-composition phrase. Fresh DOI zero hits do not invalidate it; this is reused abstract evidence, not a new body or global status search. |
| source-access | Actual source access, failures and historical reuse; Browser requests 11:23:45–11:25:09Z; thermal reuse 11:24:52.524426Z | context_only | Official definition PDF/HTML, canonical preview and enzyme summary were actually observed. Chaperonin publisher attempts remained unavailable; search results were leads only. Historical BioC help/error was not reused as article text. Original abstract acquisition remains 09:29. |
| root-primary-check | Independent root reads of acquired primary windows; Completed 11:25:03.683755Z; five XML hashes and exact paragraph windows | supports | Root independently read the relevant abundance/methylation, quotation exception, tentative rigidity and cDPG background windows. Acquisition hashes and zero-based ./body//p locators are preserved; this receipt is derived verification, not a primary article. |
| publication-status | Bounded publication-status audit; Eight fresh indexed article records, two Crossref records and historical thermal metadata | context_only | The PNAS relationship is a preprint version link, not a correction or expression of concern. No other corrective relation appears in the inspected fields; this is not an exhaustive global absence claim. |

## Limits And Additional Notes

- The definition is a typical growth-preference classification, not a newly imposed universal boundary. PATO supplies relative temperature meaning; source and METPO supply numeric context. The selection edge remains contextual evolutionary interpretation, not a directly measured selection experiment.
- The canonical optimum is supported by an actual original publisher title/abstract preview. No full article, new culture conditions, assay transfer or strain optimization is claimed. Other-record comparator histories do not refute this separate source.
- The five literal snippets include the reverse-gyrase prefix before an immediate exception. One enzyme quote is a supported explicit abridgement and the chaperonin body quote remains unknown. Topic/metadata alone does not validate that edge; access failure is not disproof.
- Actual publisher browser receipts have no downloaded article-body hash. The source agent observed the ASM summary while the root separately received 403; these are distinct access outcomes. Historical BioC help/error is not article text.
- PNAS positively supports GMGT abundance increasing in all three studied cultures. Its methylation result is narrower and includes a no-clear-trend case. Relative abundance and methylation are distinct outcomes; no universal temperature trend across all hyperthermophiles is inferred.
- Both rigidity sources preserve proposed/possible interpretations and contextual or conflicting observations. Existing evidence notes already retain qualifiers. No definitive false-effect claim, new causal assay or intervention follows.
- The cDPG protective statements are background citing earlier work, with methanogen/model-biochemical context. Acquiring an entire XML is not full verification of all contents or a universal assay of archaeal proteins. No additional mechanism or optimization is supplied.
- RO:0002326 material/process constraints follow its RO:0002216/0002500/0002595 branch; RO:0002329 is another branch. Current material subjects are not blanket errors. Semantic review is not an executed OWL reasoner, and native validity does not settle external meanings.
- Local selects-for/confers remain maintained provisional proposals. Free-text edges do not inherit unasserted RO constraints. The functional GO protein ground, relative-temperature closeMatch, exact chemical identity and valid rigidity QUALITY are preserved.
- Five protein classes, four label-only nodes and zero instances are permitted. Two NONMECHANISTIC components do not mandate token protein anchors, added graph connections or mechanism completion.
- The complete retained catalog has no Pyrococcus match. No alternative organism or downstream module query was substituted; catalog noncoverage is not negative phenotype evidence. Runner discovery retains historical bounds rather than a fresh whole-machine absence claim.
- Publication-status inspection covers eight fresh indexed records, two Crossref records and reused thermal metadata. The PNAS link is a preprint version, not a correction. No global absence of notices is asserted.
- Four fully read AI history contexts and the historical provider report are provenance, not independent scientific proof or human acceptance. Ignored-inclusive searches have stated exclusions and remote/private content remains unassessed.
- The initial snippet path failure, DNS failure and successful required network retry all remain. Mixed snippet statuses are retained. Reused B4/B5/B3/OLD checks preserve original times, failures, retry and skips; readiness is distinct from QC.
- No scientific record, mapping, history, generated output, environment or Git state was modified. No paid research, experiment, organism intervention or new molecular target was introduced.
- Six findings: two major and four minor; all indices are zero-based.
- All 63 captured hashes preserve the original 59 inputs. Target, parent, four histories and the 350-line provider report were fully read.
- Source ledger finalized at 11:26:52.303372Z and grounding at 11:26:16.404817Z. Original acquisition, copying, observation and integration times remain distinct.
- Nineteen events comprise eighteen explicit AI changes plus one automated seed. Five protein classes include four label-only nodes and zero instances.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T113052Z-hyperthermophilic
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of hyperthermophilic
started_at: '2026-10-21T11:22:39.905671Z'
finished_at: '2026-10-21T11:30:52Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: This session did not author or modify the captured record. Separate
    agents supplied source and grounding ledgers; the parent independently read critical
    primary windows and reads the complete builder before serialization and native
    validation. AI maintenance and this review are distinct from human scientific
    acceptance.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Active identity, the typical temperature definition and the canonical P.
  furiosus optimum have direct support. Two major findings concern four imported RO
  endpoint conflicts and a methylation claim overgeneralized from a valid three-culture
  abundance result. Four minors concern membrane-composition facet wording, quotation
  continuity/context, tentative rigidity wording and local human-acceptance attribution.
  All thirteen nodes and eleven edges are covered. Eleven works support fifteen placements;
  five of seven snippets are literal exact, one is abridged and one remains unknown.
  Valid functional grounding, optional proteins and two contextual graph components
  are retained.
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
  - path: data/traits/environment/hyperthermophilic.yaml
    sha256: e3270047a52bbd8bcfb13db0e638508eafb6983002a09a9e28a9aad1bb239890
    role: target
  - path: data/traits/environment/temperature_preference.yaml
    sha256: 124373347177201d4a2ed44d2d69d1160636e6a99aacc87b4b0ee71e73f0234f
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
  - path: history/infrastructure/canonical-examples/2026-08-19T183734Z-claude-code-44a170.yaml
    sha256: b6155e63f3c4719b794f7d71c65f9ccaa3e01030b0d5b676b33e4dd5a542cc62
    role: context
  - path: history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml
    sha256: e35d99e8285d488d98584d046aa001825527609cfd62575b3b839c4a31230642
    role: context
  - path: history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    sha256: c938f2928f2eb41505d58c2fb72d8de01d99534d766de9af400010e8778988a4
    role: context
  - path: history/records/homeoviscous_adaptation/2026-09-15T072704Z-codex-6cb554.yaml
    sha256: f82d94646e70fd82a5d3f6939339efae8ce0fe5e80fe6f50aab994de6c409fa8
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
  - path: research/traits/environment/hyperthermophilic-deep-research-falcon.md
    sha256: 67c1af157531cb2532335a5f209fafc5cc8cdc750abe6496f399ab8157eade75
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
- target_id: METPO:1000617
  path: data/traits/environment/hyperthermophilic.yaml
  label: hyperthermophilic
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained TraitRecord; scientific changes require guarded curation
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Maintained seeder for ontology identity and hierarchy
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: One complete maintained environmental TraitRecord, fully read with its
    parent, four captured AI history contexts and the 350-line historical provider
    report. The final 63-input capture preserves the original 59. All thirteen nodes,
    eleven edges, one canonical example, one top-level organism example, eleven assigned
    works, fifteen placements, seven snippets and nineteen history events are accounted
    for. Existing benign physiological claims receive source-bounded review. No new
    route, molecular target, intervention, experimental condition or optimization
    is supplied; incidental pathogen-specific biology remains unassessed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000617
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000617
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000617
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000617
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000617
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000617
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000617
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000617
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    006 byte comparison confirms all history, trait and common validation inputs unchanged.
    Other commands ran at f25; the Git delta to 8eee contains only seven added workflow/skill/infrastructure-history
    files. Original timestamps, failures and skips are retained; these are reused
    results, not new executions or certification against later ontology releases.
- check_id: hyperthermophilic-validate
  name: Focused LinkML validation
  status: passed
  required: true
  target_ids:
  - METPO:1000617
  command: just validate data/traits/environment/hyperthermophilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual execution at 11:22:56–57Z passed. Structural acceptance does not
    establish scientific support.
  evidence_ids:
  - check-hyperthermophilic-validate
- check_id: hyperthermophilic-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000617
  command: just validate-strict data/traits/environment/hyperthermophilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual execution at 11:22:56–58Z passed. Native acceptance is distinct
    from external semantic and source assessment.
  evidence_ids:
  - check-hyperthermophilic-strict
- check_id: hyperthermophilic-snippets
  name: Initial focused snippet invocation
  status: failed
  required: false
  target_ids:
  - METPO:1000617
  command: uv run python scripts/verify_evidence_snippets.py --record data/traits/environment/hyperthermophilic.yaml
    --out /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-snippet-results.tsv
  exit_code: 2
  expected_exit_code: 0
  summary: Actual invocation at 11:22:56Z exited 2 because the supplied script path
    did not exist. No source verification occurred. This optional failed invocation
    is superseded by the successful required retry.
  evidence_ids:
  - check-hyperthermophilic-snippets
- check_id: hyperthermophilic-snippets-retry
  name: Sandbox snippet retry
  status: failed
  required: false
  target_ids:
  - METPO:1000617
  command: just verify-snippets --record data/traits/environment/hyperthermophilic.yaml
    --out /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-snippets.tsv
  exit_code: 2
  expected_exit_code: 0
  summary: Actual execution at 11:23:02–45Z exited 2 with DNS failures for six references.
    It proves nothing about source support and is superseded by the network retry.
  evidence_ids:
  - check-hyperthermophilic-snippets-retry
- check_id: hyperthermophilic-snippets-network-retry
  name: Successful focused network retry
  status: passed
  required: true
  target_ids:
  - METPO:1000617
  command: just verify-snippets --record data/traits/environment/hyperthermophilic.yaml
    --out /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-snippets-network.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual execution at 11:23:52–11:24:03Z exited 0: seven snippets over six
    references, two VERIFIED, two NOT_IN_ABSTRACT and three UNRESOLVED. Manual source
    assessment is separate; successful command completion does not verify every quotation.'
  evidence_ids:
  - check-hyperthermophilic-snippets-network-retry
- check_id: corpus-protein-taxa
  name: Reused corpus protein/taxon audit
  status: passed
  required: true
  target_ids:
  - METPO:1000617
  command: just audit-graph-protein-taxa --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'B4 execution at 08:55:04–10Z passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC,
    one protected, zero gaps and zero errors. Historical corpus coverage is not a
    new focused scientific check.'
  evidence_ids:
  - check-corpus-protein-taxa
  scope_note: The source base and scientific inputs match. Five generic protein classes
    include four label-only nodes and zero instances. Two NONMECHANISTIC components
    do not require token accessions or added connections. B5 QC includes a later corpus
    audit.
- check_id: batch005-qc
  name: Reused full-corpus QC
  status: passed
  required: true
  target_ids:
  - METPO:1000617
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: B5 actual execution at 10:21:03–10:23:38Z passed. Separate B6 common/scientific
    byte comparison and environment readiness support scoped historical reuse.
  evidence_ids:
  - check-batch005-qc
  scope_note: B6 compares 1130 traits, 1278 history files and 19 common inputs. Preserve
    original warnings, baselines, execution dates and scope; B3 history and OLD product
    failures, retry and skips remain separate.
- check_id: uniprot-applicability
  name: UniProt instance audit applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000617
  summary: Five generic protein classes assert zero instances or accessions. Four
    are REVIEWED_LABEL_ONLY; the remaining functional GO grounding is allowed. Deleted
    historical UniProt grounds are not current audit targets.
  evidence_ids:
  - record
  - node-edges
  - grounding-policy
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the current 8eee source
    base; integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-hyperthermophilic-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-validate.log
  locator: Executed 2026-10-21T11:22:56Z through 2026-10-21T11:22:57Z; metadata hyperthermophilic-validate.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: Actual execution at 11:22:56–57Z passed. Structural acceptance does not
    establish scientific support.
  snapshot_sha256: 23696d50e3fbb1aa18cd8b49ae0d5b78a9ed4bedce7cf96087beb54cbc0a6d61
- evidence_id: check-hyperthermophilic-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-strict.log
  locator: Executed 2026-10-21T11:22:56Z through 2026-10-21T11:22:58Z; metadata hyperthermophilic-strict.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: Actual execution at 11:22:56–58Z passed. Native acceptance is distinct
    from external semantic and source assessment.
  snapshot_sha256: 4fd64399b8957030980ded3a83a282d131a7998575c3029667c5bd21703fe172
- evidence_id: check-hyperthermophilic-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-snippets.log
  locator: Executed 2026-10-21T11:22:56Z through 2026-10-21T11:22:56Z; metadata hyperthermophilic-snippets.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: Actual invocation at 11:22:56Z exited 2 because the supplied script path
    did not exist. No source verification occurred. This optional failed invocation
    is superseded by the successful required retry.
  snapshot_sha256: 9029a4d8301f97a64a4f72267a1a4aed4fe6080d667ada1e93314b48f0726090
- evidence_id: check-hyperthermophilic-snippets-retry
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-snippets-retry.log
  locator: Executed 2026-10-21T11:23:02Z through 2026-10-21T11:23:45Z; metadata hyperthermophilic-snippets-retry.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: Actual execution at 11:23:02–45Z exited 2 with DNS failures for six references.
    It proves nothing about source support and is superseded by the network retry.
  snapshot_sha256: e28d8f8f38863ef3778d8722b65e1c1662c331f5aa3b4509cf3b88edbba75246
- evidence_id: check-hyperthermophilic-snippets-network-retry
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-006.nq5qngor/hyperthermophilic-snippets-network-retry.log
  locator: Executed 2026-10-21T11:23:52Z through 2026-10-21T11:24:03Z; metadata hyperthermophilic-snippets-network-retry.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: 'Actual execution at 11:23:52–11:24:03Z exited 0: seven snippets over six
    references, two VERIFIED, two NOT_IN_ABSTRACT and three UNRESOLVED. Manual source
    assessment is separate; successful command completion does not verify every quotation.'
  snapshot_sha256: bea8fcf705db0e1177197fe3ff9dde21b11bc8683a4e36f31749b4f92dc34419
- evidence_id: check-corpus-protein-taxa
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log
  locator: Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: 'B4 execution at 08:55:04–10Z passed: 719 graphs, 129 PASS, 589 NONMECHANISTIC,
    one protected, zero gaps and zero errors. Historical corpus coverage is not a
    new focused scientific check.'
  snapshot_sha256: f5f1a6be7789f2b3e487fcbc354361f8f1f0d0d0f90a9ba59864d26ed7ac49ef
- evidence_id: check-batch005-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-005.klfwsp1f/batch005-qc.log
  locator: Executed 2026-10-21T10:21:03Z through 2026-10-21T10:23:38Z; metadata batch005-qc.json
  accessed_at: '2026-10-21T11:30:52Z'
  support: context_only
  summary: B5 actual execution at 10:21:03–10:23:38Z passed. Separate B6 common/scientific
    byte comparison and environment readiness support scoped historical reuse.
  snapshot_sha256: 206638ef702eef1ea64f13c4be3ef11180f9659383be68d1e492a9760c8f79be
- evidence_id: capture
  kind: validation
  reference: Native final selected-record capture
  locator: 63 inputs at 11:24:42.075849–11:24:43.536329Z
  accessed_at: '2026-10-21T11:24:43.536329Z'
  support: supports
  summary: All current captured hashes match and preserve the original 59. Parent
    and four AI histories were fully read as context, not additional review targets.
  snapshot_sha256: 64d723f3d366c7834babb528816e2ac2b2d761c119e47888d4391167f3fbd1ed
- evidence_id: preparation
  kind: validation
  reference: Whole-record and provenance preparation
  locator: Complete target, parent, four histories and 350-line provider report
  accessed_at: '2026-10-21T11:25:55.983643Z'
  support: context_only
  summary: Factual coverage was derived before adjudication. Historical report recommendations
    are provenance, not instructions or independently verified primary evidence.
  snapshot_sha256: 9f9eddd4f872314ccd5b9f5e334f3f785b1810c482aa9dba4c15a20af3cb2e34
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/hyperthermophilic.yaml
  locator: Entire current record; thirteen nodes, eleven edges and nineteen events
  accessed_at: '2026-10-21T11:26:16.404817Z'
  support: partial
  summary: The qualitative temperature class is REVIEWED with eighteen explicit AI
    changes plus seed. Current assertions are distinguished from historical deleted
    identifiers and other-record comparisons.
  snapshot_sha256: e3270047a52bbd8bcfb13db0e638508eafb6983002a09a9e28a9aad1bb239890
- evidence_id: native-policy
  kind: authority
  reference: Native field-by-field checklist
  locator: Evidence, completeness, facet consistency and Status/audit guidance
  accessed_at: '2026-10-21T11:26:16.404817Z'
  support: supports
  summary: Source support, consistent represented meanings and attributed human acceptance
    apply. Optional protein/dataset fields and NONMECHANISTIC contextual components
    do not require artificial completion.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: grounding-policy
  kind: authority
  reference: Native grounding policy
  locator: Lines 75–88, taxon-agnostic enzyme functional grounds
  accessed_at: '2026-10-21T11:26:16.404817Z'
  support: supports
  summary: An enzymatic GO molecular-function ground may describe the functional facet
    of a protein class. GO:0160097 is not an automatic protein/activity error or mandatory
    family-accession replacement.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: snippet-policy
  kind: authority
  reference: Native curation playbook
  locator: Lines 649–650 and 673–676, contiguous verbatim evidence and interpretation
  accessed_at: '2026-10-21T11:26:16.404817Z'
  support: supports
  summary: A literal excerpt must retain source wording and relevant context. An explicit
    ellipsis can preserve meaning while still falling short of the native contiguous-snippet
    convention.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: native-types
  kind: authority
  reference: Native CausalNodeTypeEnum
  locator: Component/localization and measurable-attribute definitions, lines 683–700
  accessed_at: '2026-10-21T11:26:16.404817Z'
  support: supports
  summary: CELLULAR_LOCALIZATION permits real cellular components; composition may
    denote an attribute instead. Membrane rigidity is a valid QUALITY and need not
    be forced into a process to satisfy an imported relation.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: reuse
  kind: validation
  reference: B6 common-input comparison
  locator: Original verification at 10:14:46.298715Z
  accessed_at: '2026-10-21T10:14:46.298715Z'
  support: supports
  summary: 1130 traits, 1278 history files and 19 common inputs match the preceding
    batch. This setup receipt predates B5 final QC, whose actual result is recorded
    separately.
  snapshot_sha256: 91de0fcd8f598a37b867033da1a4d732eaf5676848023a41dd6963612a78aa44
- evidence_id: reuse-supplement
  kind: validation
  reference: B5 checks and B6 readiness supplement
  locator: Original supplement 10:28:10.859819Z; QC 10:21:03–10:23:38Z
  accessed_at: '2026-10-21T10:28:10.859819Z'
  support: supports
  summary: Historical command/log hashes, readiness, failed attempts and successful
    retry remain distinct. B3 validated 1277 history records while byte comparison
    inventories 1278 files. No fresh B6 corpus execution is claimed.
  snapshot_sha256: f5e234e9de85ff4dbd486c2f4e4c9c8df915a767fb67afa4da204ab28f57a7f4
- evidence_id: identity
  kind: authority
  reference: Pinned METPO identity, hierarchy and retention policy
  locator: METPO:1000617 and parent 1000613; active-review row 124 and release-delta
    row 1292
  accessed_at: '2026-10-21T11:26:16.385665Z'
  support: supports
  summary: Active identity and related synonym agree. The local ≥80 °C typography
    is explicitly retained and semantically agrees with upstream >=80 C. Typical boundary
    wording is not a newly invented universal cutoff.
  snapshot_sha256: 840549e5a24a4a7a4d4a5295cf05c0713b1db973195d1dfc484017e193622450
- evidence_id: go-functional
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0160097
  locator: Active reverse-gyrase molecular function; original access completed 09:50:46.974059Z
  accessed_at: '2026-10-21T09:50:46.974059Z'
  support: supports
  summary: The functional ground agrees with the current named protein class under
    native policy. This identity check does not establish universal presence or organism-level
    sufficiency.
  snapshot_sha256: 5317b45ab6e8ab6ed6c175b341ae58aba6ff1919c0b66ac9cd502c31e4cfd108
- evidence_id: pato-temperature
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/pato/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPATO_0001305
  locator: Relative increased-temperature quality; original access completed 09:50:46.963303Z
  accessed_at: '2026-10-21T09:50:46.963303Z'
  support: supports
  summary: The explicit closeMatch supplies relative temperature meaning. Numeric
    context comes from the trait definition and cited source, so no PATO numeric-threshold
    finding is assigned.
  snapshot_sha256: 5adcb0394c8b682a0328f7f42791bd6b9a7e44b79d021a3ced138cad4555a0f7
- evidence_id: chemical
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/193595/
  locator: Fresh request 11:23:20.504731–11:23:21.180326Z
  accessed_at: '2026-10-21T11:23:21.180326Z'
  support: supports
  summary: The released macrocyclic-archaeol identity matches the named chemical.
    Source claims about physical effects remain a separate question.
  snapshot_sha256: 9fda6aa39c056731bd8e63d133a520bf91f043202edddf8dd90358e1c19e602d
- evidence_id: taxon
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2261&retmode=xml
  locator: Fresh request 11:23:20.505352–11:23:20.878116Z
  accessed_at: '2026-10-21T11:23:20.878116Z'
  support: supports
  summary: NCBI2261 resolves to Pyrococcus furiosus. The optimum is supported separately
    by the original publisher preview, not inferred from taxonomy.
  snapshot_sha256: 0f559803e545bf77f3a5c6556b99c4d47d48f3086290c0a7b53203645582f63a
- evidence_id: local-authority
  kind: authority
  reference: Maintained mappings, local proposals and writers
  locator: Node rows 56/68/184; predicate rows 10–11/33/65/102; v2/v8
  accessed_at: '2026-10-21T11:26:16.402872Z'
  support: supports
  summary: Functional GO and relative-temperature closeMatch mappings are permitted.
    Local selects-for/confers roles fit. Existing-ID skips and wildcard mappings explain
    recurrence; rigidity QUALITY is explicitly maintained.
  snapshot_sha256: bf53d420207171c830fb99088eafc386772de4d6e56de763ecb349000a9bbf7b
- evidence_id: predicate-authority
  kind: authority
  reference: Retained recursive RO semantics
  locator: Original RO access 08:04:46.869674Z; BFO context 09:52:45.989262Z; integration
    11:26:16.386370Z
  accessed_at: '2026-10-21T11:26:16.386370Z'
  support: supports
  summary: RO:0002326 inherits material/process roles through RO:0002216 → RO:0002500
    → RO:0002595. RO:0002329 is another superproperty branch, not itself the material/process
    constraint. RO:0002211 and RO:0002213 require process-regulation roles. Four current
    assignments conflict; this is semantic assessment, not an executed OWL failure.
  snapshot_sha256: a74e3b1948195ac415ab00f3898e533c884d7c480b8de19e1f24e2265a35bcda
- evidence_id: authority-reuse
  kind: validation
  reference: Original authority and catalog reuse chain
  locator: Hash/copy verification at 11:23:56.648415Z
  accessed_at: '2026-10-21T11:23:56.648415Z'
  support: supports
  summary: Reused GO/PATO, RO, catalog and runner receipts retain original acquisition
    bounds and hashes. Fresh ChEBI and taxonomy are separate. Copying or integration
    is not a new external request.
  snapshot_sha256: c94cf0f8c76f17c2f9e0e1fb50fcf30c5408160b6e624b0090b82e96333ca231
- evidence_id: grounding-ledger
  kind: validation
  reference: Complete documentary grounding assessment
  locator: Thirteen nodes, eleven edges, two components and 63 matching inputs
  accessed_at: '2026-10-21T11:26:16.404817Z'
  support: partial
  summary: Identity, current chemical/function grounds and optional protein scope
    are supported. One grouped RO concern and bounded membrane-composition facet concern
    remain; no new topology or accession requirement is imposed.
  snapshot_sha256: a3ccdada424825f164225dd6757c4752949238ff8fa8fe5e22a7b59780f0a499
- evidence_id: node-edges
  kind: validation
  reference: Complete current node and edge ledger
  locator: nodes[0–12] and edges[0–10], zero-based
  accessed_at: '2026-10-21T11:26:16.389628Z'
  support: partial
  summary: Every endpoint resolves. Four grounded RO assignments conflict with endpoint
    meanings; free-text edges 5–8 do not inherit unasserted RO constraints. Two contextual
    components are compatible with NONMECHANISTIC scope.
  snapshot_sha256: 5e0912f63e11f0ca69055c827c18b038b42c4078ac92a65ef2826846d2947615
- evidence_id: owners
  kind: authority
  reference: Maintained mappings, type migration and identity writers
  locator: Grounding guards 156–174/152–176; rigidity migration 110–121; typography
    retention 125–150
  accessed_at: '2026-10-21T11:26:16.394784Z'
  support: supports
  summary: Current mapping/writer owners can retain or recreate imported relation
    conflicts. Preserve valid QUALITY, material proteins and chemicals, current functional
    grounds and retained typography. Historical withdrawn grounds are not current
    defects.
  snapshot_sha256: 95faeb518aca12c45a9b61eeeeed4ab24b14e7a92f01c5a683d5731828757f81
- evidence_id: provenance
  kind: search
  reference: Bounded ignored-inclusive target and node provenance search
  locator: Completed 11:24:11.071611Z; 199 matching files, no targeted saved review
  accessed_at: '2026-10-21T11:26:16.394582Z'
  support: partial
  summary: Eighteen AI changes plus seed and four captured AI history contexts establish
    maintenance but do not attribute current-target human acceptance. Other-record
    comparator observations do not refute the present canonical example.
  snapshot_sha256: f5b899be2a6784a598cb48654b16a80c8d3791f5a72fd2de91a29b213043342f
  search_scope: Own B6 repository target ID/label/slug search includes ignored and
    hidden files, excluding .git and .venv; exact node/graph history and canonical-name/ID/DOI
    searches retain exact commands. Saved reviews were parsed by target ID/path and
    all four captured histories fully read. No remote, private or global absence claim.
- evidence_id: expression
  kind: validation
  reference: Canonical catalog applicability
  locator: Original official catalog request 07:36:12.732638–07:36:12.858149Z; twenty
    organisms and twenty-eight datasets
  accessed_at: '2026-10-21T11:26:16.403584Z'
  support: context_only
  summary: No Pyrococcus furiosus or genus match occurs in the complete retained catalog.
    No alternative archaeon is substituted, and noncoverage is not negative phenotype
    evidence. No downstream gene/module query occurred.
  snapshot_sha256: 131484c2d8526f4f0845d24860103a953616cc23f1765eb307b141a979f95d13
- evidence_id: runner
  kind: search
  reference: Retained structured-runner discovery
  locator: B5 PATH/project bounds 09:27:57Z and external bounds 08:17:15Z
  accessed_at: '2026-10-21T09:27:57.542053Z'
  support: context_only
  summary: No callable runner was found within those historical scopes. The official
    catalog is the fallback; no fresh B6 or global absence claim is made.
  snapshot_sha256: 43597ec8b007fc605fabf9069534281f331a33bda5615b9ce9c473facf744179
  search_scope: Historical B5 PATH plus ignored-inclusive project filename/manifest
    search, .git excluded; earlier external bounds retained in prior-runner-discovery-external.json.
    No fresh whole-machine or unrestricted absence search.
- evidence_id: source-ledger
  kind: validation
  reference: Complete source assessment
  locator: Eleven assigned works and fifteen placements; finalized 11:26:52.303372Z
  accessed_at: '2026-10-21T11:26:52.303372Z'
  support: partial
  summary: Positive definition, canonical optimum and existing contextual claims are
    separated from the methylation overgeneralization, quotation precision and tentative
    rigidity interpretation. Acquired bodies are assessed only at declared windows.
  snapshot_sha256: 50908ebe24af7d93b55c0502961be4fd76bf366d1a2da083703655752721c6b8
- evidence_id: placements
  kind: validation
  reference: Complete citation-placement inventory
  locator: Definition, both example locations and all eleven edges; fifteen placements
  accessed_at: '2026-10-21T11:26:52.303372Z'
  support: supports
  summary: All assigned works and placements are accounted for. Registry identity,
    actual publisher access, fresh indexed fields and historical abstract reuse remain
    distinct.
  snapshot_sha256: b231048aa0e05339709b7df8a2775decccc150e282e214e85db4c8b411f6cd73
- evidence_id: snippets
  kind: validation
  reference: Complete seven-occurrence quotation ledger
  locator: Five literal exact including one immediately qualified prefix; one abridgement
    and one unknown
  accessed_at: '2026-10-21T11:26:52.303372Z'
  support: partial
  summary: The exact reverse-gyrase substring stops before the source exception. The
    enzyme ellipsis is meaningful but noncontiguous. The chaperonin body quotation
    remains unknown; unavailable text is not falsity.
  snapshot_sha256: 7050c4a692d0732d5bef8341213bc8f124e21e7d737f133d75f0425282d8fe4a
- evidence_id: edge-sources
  kind: validation
  reference: Complete nearest-edge source ledger
  locator: edges[0–10], each assessed at its actual source window
  accessed_at: '2026-10-21T11:26:52.303372Z'
  support: partial
  summary: The all-three GMGT abundance result is positive, while all-three methylation
    is contradicted. Rigidity interpretations remain tentative. Generic cDPG protective
    claims are background citing earlier work, not the principal new experiment.
  snapshot_sha256: 60e966b35a1f01518c20b8cb0dd3e8adc8cb2aefb2770f58876f945ab4d8cc0f
- evidence_id: metadata-definition
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111%2Fj.1574-6976.1996.tb00233.x&format=json&resultType=core
  locator: Actual indexed query 2026-10-21T11:23:22.073530+00:00 through 2026-10-21T11:23:22.790324+00:00
  accessed_at: '2026-10-21T11:23:22.790324Z'
  support: context_only
  summary: Only returned identity, title, abstract and status fields are used. Eight
    queries yielded indexed articles; definition, canonical and thermal DOI misses
    are resolved through separate documented sources. No full-body or unrestricted
    status coverage is implied.
  snapshot_sha256: 0a562059fdc00f49a9221422eaf57efc12a3062c893284435b04d7a7cdb609c4
- evidence_id: registry-definition
  kind: database
  reference: https://api.crossref.org/works/10.1111%2Fj.1574-6976.1996.tb00233.x
  locator: Actual registry query 2026-10-21T11:23:52.309518+00:00 through 2026-10-21T11:23:52.636696+00:00
  accessed_at: '2026-10-21T11:23:52.636696Z'
  support: supports
  summary: Registry identity supports the citation. Actual publisher title/abstract
    supplies the scientific observation; registry identity alone does not establish
    it.
  snapshot_sha256: 34fee4af1d47c5d38d2635c6919215b4318c526cde0eb46e941503d50e88cf32
- evidence_id: metadata-organism
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9348040+AND+SRC%3AMED&format=json&resultType=core
  locator: Actual indexed query 2026-10-21T11:23:22.073903+00:00 through 2026-10-21T11:23:22.823148+00:00
  accessed_at: '2026-10-21T11:23:22.823148Z'
  support: context_only
  summary: Only returned identity, title, abstract and status fields are used. Eight
    queries yielded indexed articles; definition, canonical and thermal DOI misses
    are resolved through separate documented sources. No full-body or unrestricted
    status coverage is implied.
  snapshot_sha256: b9de27a03d7e8c154dd28c79750b314348725c205ee733840f89301863c37f7e
- evidence_id: metadata-canonical
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1007%2FBF00413027&format=json&resultType=core
  locator: Actual indexed query 2026-10-21T11:23:22.073982+00:00 through 2026-10-21T11:23:22.839849+00:00
  accessed_at: '2026-10-21T11:23:22.839849Z'
  support: context_only
  summary: Only returned identity, title, abstract and status fields are used. Eight
    queries yielded indexed articles; definition, canonical and thermal DOI misses
    are resolved through separate documented sources. No full-body or unrestricted
    status coverage is implied.
  snapshot_sha256: 2a1483d353a02f76dc68f13b40ac79b8992fde707050916acf656821bb3040bd
- evidence_id: registry-canonical
  kind: database
  reference: https://api.crossref.org/works/10.1007%2FBF00413027
  locator: Actual registry query 2026-10-21T11:23:52.360801+00:00 through 2026-10-21T11:23:52.636645+00:00
  accessed_at: '2026-10-21T11:23:52.636645Z'
  support: supports
  summary: Registry identity supports the citation. Actual publisher title/abstract
    supplies the scientific observation; registry identity alone does not establish
    it.
  snapshot_sha256: 2c91b70e1826e2750a15fbadcad07410d6b9fc37b69a8f31b0211794dde80d91
- evidence_id: metadata-proteins
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FMMBR.65.1.1-43.2001&format=json&resultType=core
  locator: Actual indexed query 2026-10-21T11:23:22.074024+00:00 through 2026-10-21T11:23:22.820553+00:00
  accessed_at: '2026-10-21T11:23:22.820553Z'
  support: context_only
  summary: Only returned identity, title, abstract and status fields are used. Eight
    queries yielded indexed articles; definition, canonical and thermal DOI misses
    are resolved through separate documented sources. No full-body or unrestricted
    status coverage is implied.
  snapshot_sha256: 7fbda4bf0eea7b0c1641d88dc150329587687249fd800726e14b7f84a9670e0c
- evidence_id: metadata-gyrase
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffmicb.2021.661411&format=json&resultType=core
  locator: Actual indexed query 2026-10-21T11:23:22.790360+00:00 through 2026-10-21T11:23:23.526421+00:00
  accessed_at: '2026-10-21T11:23:23.526421Z'
  support: context_only
  summary: Only returned identity, title, abstract and status fields are used. Eight
    queries yielded indexed articles; definition, canonical and thermal DOI misses
    are resolved through separate documented sources. No full-body or unrestricted
    status coverage is implied.
  snapshot_sha256: 54e4a9315bd8a1c9efb356999a4d9af59f7f81a980c8e4b03b5fe1e54e9f7e34
- evidence_id: metadata-chaperonins
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrmicro866&format=json&resultType=core
  locator: Actual indexed query 2026-10-21T11:23:22.820594+00:00 through 2026-10-21T11:23:23.550500+00:00
  accessed_at: '2026-10-21T11:23:23.550500Z'
  support: context_only
  summary: Only returned identity, title, abstract and status fields are used. Eight
    queries yielded indexed articles; definition, canonical and thermal DOI misses
    are resolved through separate documented sources. No full-body or unrestricted
    status coverage is implied.
  snapshot_sha256: 41f7393d8f82ff84d4d9fe84f2f89ca27d9628248c0e471fb4c2d55d70469eec
- evidence_id: metadata-thermal
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fs0300-9629%2897%2900003-0&format=json&resultType=core
  locator: Actual indexed query 2026-10-21T11:23:22.823185+00:00 through 2026-10-21T11:23:23.582597+00:00
  accessed_at: '2026-10-21T11:23:23.582597Z'
  support: context_only
  summary: Only returned identity, title, abstract and status fields are used. Eight
    queries yielded indexed articles; definition, canonical and thermal DOI misses
    are resolved through separate documented sources. No full-body or unrestricted
    status coverage is implied.
  snapshot_sha256: 25e3cf6616503721ec087dd147e11ac038f8834891e32d704a1f67074095c9cc
- evidence_id: metadata-cdpg
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3389%2Ffmicb.2023.1267570&format=json&resultType=core
  locator: Actual indexed query 2026-10-21T11:23:22.839883+00:00 through 2026-10-21T11:23:23.569740+00:00
  accessed_at: '2026-10-21T11:23:23.569740Z'
  support: context_only
  summary: Only returned identity, title, abstract and status fields are used. Eight
    queries yielded indexed articles; definition, canonical and thermal DOI misses
    are resolved through separate documented sources. No full-body or unrestricted
    status coverage is implied.
  snapshot_sha256: ef1e37abcd947f08e4ab06d9a4e78d4c33ab5ce0d169660a8c815071fd2d3547
- evidence_id: metadata-gms
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073%2Fpnas.2318761121&format=json&resultType=core
  locator: Actual indexed query 2026-10-21T11:23:23.526463+00:00 through 2026-10-21T11:23:24.194350+00:00
  accessed_at: '2026-10-21T11:23:24.194350Z'
  support: context_only
  summary: Only returned identity, title, abstract and status fields are used. Eight
    queries yielded indexed articles; definition, canonical and thermal DOI misses
    are resolved through separate documented sources. No full-body or unrestricted
    status coverage is implied.
  snapshot_sha256: bbbcff0fa3751213d3b98e8a43fd495471978b059648e7a871e7da659339847e
- evidence_id: metadata-rigidity
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-024-49650-x&format=json&resultType=core
  locator: Actual indexed query 2026-10-21T11:23:23.550540+00:00 through 2026-10-21T11:23:24.224127+00:00
  accessed_at: '2026-10-21T11:23:24.224127Z'
  support: context_only
  summary: Only returned identity, title, abstract and status fields are used. Eight
    queries yielded indexed articles; definition, canonical and thermal DOI misses
    are resolved through separate documented sources. No full-body or unrestricted
    status coverage is implied.
  snapshot_sha256: 89fb43811b17af9870e8ce2a67f307975e9fcd6d7c2a35539365753d4946df39
- evidence_id: metadata-macrocyclic
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2Fmsystems.01159-22&format=json&resultType=core
  locator: Actual indexed query 2026-10-21T11:23:23.569780+00:00 through 2026-10-21T11:23:24.404378+00:00
  accessed_at: '2026-10-21T11:23:24.404378Z'
  support: context_only
  summary: Only returned identity, title, abstract and status fields are used. Eight
    queries yielded indexed articles; definition, canonical and thermal DOI misses
    are resolved through separate documented sources. No full-body or unrestricted
    status coverage is implied.
  snapshot_sha256: 1cde4112e152ce10bb2239a981a0ebfca644a1f98525e299c2467aca38669e42
- evidence_id: body-gyrase
  kind: primary_source
  reference: DOI:10.3389/fmicb.2021.661411
  locator: PMC8185306 body paragraph31, with paragraph30 context; actual acquisition
    2026-10-21T11:23:50.845127+00:00 through 2026-10-21T11:23:52.360777+00:00
  accessed_at: '2026-10-21T11:23:52.360777Z'
  support: supports
  summary: Body paragraph 31 contains the literal quoted prefix and an immediate exception.
    Preserve the existing association wording; do not infer universal presence or
    necessity.
  snapshot_sha256: df2dd187cdfcc5b055ea472191ca4e8d648e76d8a64574e17e129875d716938c
- evidence_id: body-cdpg
  kind: primary_source
  reference: DOI:10.3389/fmicb.2023.1267570
  locator: PMC10690619 abstract; body paragraph5; actual acquisition 2026-10-21T11:23:50.845375+00:00
    through 2026-10-21T11:23:52.299701+00:00
  accessed_at: '2026-10-21T11:23:52.299701Z'
  support: supports
  summary: Abstract and paragraph 5 report existing protective roles as background
    with earlier citations. Preserve methanogen and model biochemical context; no
    universal assay of every archaeal protein or new mechanism is inferred.
  snapshot_sha256: e23cb238b9f8620d7fe4c773cc0450d5aa0def034d66eb1306205d02a8d3f33a
- evidence_id: body-gms
  kind: primary_source
  reference: DOI:10.1073/pnas.2318761121
  locator: PMC11214058 body paragraphs3,5,20–26; especially21,Figure5caption22,and24;
    actual acquisition 2026-10-21T11:23:50.845485+00:00 through 2026-10-21T11:23:52.309497+00:00
  accessed_at: '2026-10-21T11:23:52.309497Z'
  support: partial
  summary: Paragraphs 21–22 positively support increased GMGT abundance in all three
    cultures. Paragraph 24 reports no clear methylation trend in A. profundus, contradicting
    the all-three methylation note. Existing enzyme-function context is supported
    without organism-wide indispensability.
  snapshot_sha256: 2aff103f4868530c5b3885ff8a4eec043c4a903a6e0cf1111d6ad04fa10b6e65
- evidence_id: body-rigidity
  kind: primary_source
  reference: DOI:10.1038/s41467-024-49650-x
  locator: PMC11186832 body paragraph1; actual acquisition 2026-10-21T11:23:50.845663+00:00
    through 2026-10-21T11:23:52.987146+00:00
  accessed_at: '2026-10-21T11:23:52.987146Z'
  support: supports
  summary: Introduction paragraph 1 describes the rigidity contribution as proposed
    and reports an opposing temperature-abundance observation. It does not establish
    a universal directly measured physical effect.
  snapshot_sha256: f8e0522644c57c6a83cef97105a5b077fdffe22c8b888d890b346d2f3dc29d68
- evidence_id: body-macrocyclic
  kind: primary_source
  reference: DOI:10.1128/msystems.01159-22
  locator: PMC10134847 body paragraphs45–46; actual acquisition 2026-10-21T11:23:52.299723+00:00
    through 2026-10-21T11:23:53.511689+00:00
  accessed_at: '2026-10-21T11:23:53.511689Z'
  support: supports
  summary: Discussion paragraphs 45–46 qualify the physical interpretation as an assumption
    and possibility and report contextual limits. Preserve those qualifiers without
    declaring the suggested effect false.
  snapshot_sha256: 912192bb96ca05be885e3215fdf8e0cb13fc44f1daa80b493223acb747c2e81e
- evidence_id: definition-primary
  kind: primary_source
  reference: DOI:10.1111/j.1574-6976.1996.tb00233.x
  locator: Actual OUP HTML abstract line 24; root observation recorded 11:26:12.538274Z
  accessed_at: '2026-10-21T11:26:12.538274Z'
  support: supports
  summary: The actual publisher abstract verifies the assigned optimum-range wording
    and definition context. Agent PDF/HTML observations are independently retained.
    This hashes the browser receipt, not an uncollected article body.
  snapshot_sha256: e85bc711e8d537b5cb2b0ab53f20d5065d201d2bd24b8769702d39ff1f193a5d
- evidence_id: canonical-primary
  kind: primary_source
  reference: DOI:10.1007/BF00413027
  locator: Springer title and abstract lines 11/36–39; root observation recorded 11:24:10.360965Z
  accessed_at: '2026-10-21T11:24:10.360965Z'
  support: supports
  summary: The actual original publisher preview directly supports P. furiosus and
    its approximately 100 °C optimum. Subscription preview only; no full article,
    new cultivation conditions or strain optimization is claimed.
  snapshot_sha256: b37f00e2c0ac2b85e0a41ca50c429b80beef21f5184879ac13b29eeacbc90380
- evidence_id: enzyme-primary
  kind: primary_source
  reference: DOI:10.1128/MMBR.65.1.1-43.2001
  locator: Source-agent actual ASM Summary line 83 at 11:23:45–47Z
  accessed_at: '2026-10-21T11:23:47Z'
  support: supports
  summary: Both selected phrase segments occur in the source sentence, with omitted
    intervening wording. Meaning is supported but the current snippet is not contiguous.
    The root separately received 403; that does not refute the agent’s actual publisher
    observation. Browser receipt hash is not article-body hash.
  snapshot_sha256: d8fb48d87850c90ec581fd90dfa0250be223796ae58fc25ea6b4d8bb8135dad4
- evidence_id: thermal-abstract
  kind: database
  reference: https://pubmed.ncbi.nlm.nih.gov/9406426/
  locator: Original indexed abstract request 09:29:00.590499–09:29:01.331044Z, second
    sentence
  accessed_at: '2026-10-21T09:29:01.331044Z'
  support: supports
  summary: The original indexed response identifies the DOI and contains the exact
    membrane-composition phrase. Fresh DOI zero hits do not invalidate it; this is
    reused abstract evidence, not a new body or global status search.
  snapshot_sha256: 56f69a7ce2e69822ef753fec5c43716583184e45fc1a2c0cae98aa9bdb841265
- evidence_id: source-access
  kind: validation
  reference: Actual source access, failures and historical reuse
  locator: Browser requests 11:23:45–11:25:09Z; thermal reuse 11:24:52.524426Z
  accessed_at: '2026-10-21T11:25:09Z'
  support: context_only
  summary: Official definition PDF/HTML, canonical preview and enzyme summary were
    actually observed. Chaperonin publisher attempts remained unavailable; search
    results were leads only. Historical BioC help/error was not reused as article
    text. Original abstract acquisition remains 09:29.
  snapshot_sha256: d8fb48d87850c90ec581fd90dfa0250be223796ae58fc25ea6b4d8bb8135dad4
- evidence_id: root-primary-check
  kind: validation
  reference: Independent root reads of acquired primary windows
  locator: Completed 11:25:03.683755Z; five XML hashes and exact paragraph windows
  accessed_at: '2026-10-21T11:25:03.683755Z'
  support: supports
  summary: Root independently read the relevant abundance/methylation, quotation exception,
    tentative rigidity and cDPG background windows. Acquisition hashes and zero-based
    ./body//p locators are preserved; this receipt is derived verification, not a
    primary article.
  snapshot_sha256: 059d40149cace8d9850664730fbb031b3dfad3ab01a2d090eed1cd1741c9908a
- evidence_id: publication-status
  kind: validation
  reference: Bounded publication-status audit
  locator: Eight fresh indexed article records, two Crossref records and historical
    thermal metadata
  accessed_at: '2026-10-21T11:26:52.298822Z'
  support: context_only
  summary: The PNAS relationship is a preprint version link, not a correction or expression
    of concern. No other corrective relation appears in the inspected fields; this
    is not an exhaustive global absence claim.
  snapshot_sha256: cb8e9165921c9fa781e23c5b9186f3e62fa9ba26d18d7a9c0dd97ad3d598bcac
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: ID, related synonym, definition and parent'
  outcome: supported
  target_ids:
  - METPO:1000617
  summary: Active METPO:1000617 and broader temperature preference agree with the
    current record. The related synonym is literal upstream wording. Retained scientific
    typography preserves the same typically-at-least-80 boundary; no fallback, exact-equivalence
    or obsolete-replacement inference is needed.
  evidence_ids:
  - identity
  - record
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: nearest-source definition and typical boundary'
  outcome: supported
  target_ids:
  - METPO:1000617
  summary: The actual OUP abstract directly supports the assigned optimum classification
    and both literal range occurrences. PATO supplies relative temperature through
    explicit closeMatch, while numeric context comes from definition/source. The environmental
    selection relation is contextual interpretation rather than a measured evolutionary
    experiment, retained as a limitation.
  evidence_ids:
  - definition-primary
  - registry-definition
  - identity
  - pato-temperature
  - edge-sources
- assessment_id: examples
  area: evidence
  topic: 'Native checklist: canonical optimum and top organism example'
  outcome: supported
  target_ids:
  - METPO:1000617
  summary: The current taxon resolves to P. furiosus. The original Springer title/abstract
    directly supports approximately 100 °C optimum, and PMID9348040 contains the top
    organism-classification phrase in its title. Other-record rejected comparator
    measurements do not contradict this independently supported source. No new growth
    conditions or species-uniform assay is inferred.
  evidence_ids:
  - taxon
  - canonical-primary
  - registry-canonical
  - metadata-organism
  - provenance
- assessment_id: model
  area: representation
  topic: 'Native checklist: native facets and optional completeness'
  outcome: concern
  target_ids:
  - METPO:1000617
  summary: Node 5 leaves composition versus material membrane component unclear; CELLULAR_LOCALIZATION
    does permit actual components, so this is bounded facet precision. Rigidity is
    correctly a QUALITY. Five protein classes, four label-only nodes, zero instances
    and two NONMECHANISTIC components require no token accessions or invented links.
  evidence_ids:
  - native-types
  - node-edges
  - owners
  - native-policy
- assessment_id: node-grounding
  area: grounding
  topic: 'Native checklist: all thirteen nodes'
  outcome: supported
  target_ids:
  - METPO:1000617
  summary: Active trait, PATO closeMatch, allowed reverse-gyrase functional GO ground
    and exact macrocyclic-archaeol identity are supported. Other chemical and protein
    classes may remain ungrounded or label-only. Node 5 facet wording is assessed
    separately, not promoted to an unsupported identifier failure.
  evidence_ids:
  - identity
  - pato-temperature
  - go-functional
  - chemical
  - grounding-policy
  - node-edges
  details: 'Nodes 0–1: trait and temperature context. Nodes 2–4: material protein
    classes, including an allowed functional ground. Node 5: composition/component
    precision. Node 6: optional ungrounded chemical. Node 7: protein aggregate. Node
    8: oxidative-damage event/process. Nodes 9–10: material lipid and enzyme. Node
    11: valid rigidity QUALITY. Node 12: exact named chemical, with effect certainty
    assessed separately.'
- assessment_id: predicate-roles
  area: consistency
  topic: 'Native checklist: all eleven relations'
  outcome: concern
  target_ids:
  - METPO:1000617
  summary: RO assignments on edges 2, 3, 9 and 10 conflict with process endpoint meanings.
    Material subjects of RO:0002326 are not themselves invalid; its trait/quality
    objects are. Local selects-for/confers fit declared roles. Free-text edges 5–8
    carry no unasserted RO constraints, and optional IDs are not completeness defects.
  evidence_ids:
  - predicate-authority
  - local-authority
  - node-edges
  - owners
  details: 'Edges 0/1/4: compatible local proposal roles. Edge 2: trait object conflicts
    with process range. Edge 3: two material proteins conflict with regulation roles.
    Edges 5/6: free-text protective context. Edges 7/8: free-text production/function
    context. Edge 9: quality object conflicts with process range. Edge 10: chemical/quality
    endpoints conflict with process regulation. Retain valid material and quality
    facets rather than forcing retypes.'
- assessment_id: edge-sources
  area: evidence
  topic: 'Native checklist: all eleven nearest-source claims'
  outcome: concern
  target_ids:
  - METPO:1000617
  summary: Most existing contextual claims have positive inspected support with taxon
    and evidence-tier bounds. PNAS supports increased GMGT abundance in all three
    cultures, but its methylation result is species-dependent and directly contradicts
    the all-three note. Rigidity interpretations remain tentative. Chaperonin exact
    body support is unknown; cDPG protective statements are cited background, not
    the principal new experiment.
  evidence_ids:
  - edge-sources
  - placements
  - source-ledger
  - body-gms
  - body-rigidity
  - body-macrocyclic
  - body-cdpg
  - root-primary-check
- assessment_id: bibliography
  area: evidence
  topic: 'Native checklist: eleven assigned works and status scope'
  outcome: supported
  target_ids:
  - METPO:1000617
  summary: All eleven identities and fifteen placements resolve through eight fresh
    indexed articles, two registry/publisher identities and one historical indexed
    abstract. PNAS links its preprint, not a corrective notice. No global status absence
    is claimed. Metadata-only and browser-preview access remain distinct from five
    acquired JATS bodies.
  evidence_ids:
  - source-ledger
  - placements
  - publication-status
  - thermal-abstract
  - source-access
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: seven occurrences, continuity and context'
  outcome: concern
  target_ids:
  - METPO:1000617
  summary: Five occurrences are literal exact, including the reverse-gyrase prefix
    that immediately precedes an exception. One enzyme excerpt is an explicit noncontiguous
    abridgement with supported meaning; the chaperonin body quotation remains unknown.
    Group continuity/context precision as one minor without calling the exact prefix
    nonliteral or declaring a universal graph claim.
  evidence_ids:
  - snippets
  - snippet-policy
  - enzyme-primary
  - body-gyrase
  - definition-primary
  - check-hyperthermophilic-snippets-network-retry
- assessment_id: quantity
  area: quantity
  topic: 'Native checklist: optimum, abundance and methylation measures'
  outcome: concern
  target_ids:
  - METPO:1000617
  summary: The canonical optimum and typical class boundary have direct source support.
    PNAS relative abundance and degree of methylation are distinct measured outcomes
    and must not be joined as a uniform result. No unit conversion, cultivation recommendation,
    new threshold or class-wide monotonic behavior is inferred.
  evidence_ids:
  - canonical-primary
  - definition-primary
  - body-gms
  - placements
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: whole-record and contextual graph coverage'
  outcome: supported
  target_ids:
  - METPO:1000617
  summary: Thirteen nodes, eleven edges, both example locations, eleven works, fifteen
    placements, seven snippets and nineteen history events are covered. The disconnected
    protective-solute context is allowed in this NONMECHANISTIC graph. Unknown source
    access and conditional biology are explicit; no token route, accession or connector
    is required.
  evidence_ids:
  - capture
  - node-edges
  - placements
  - native-policy
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: canonical catalog applicability'
  outcome: not_applicable
  target_ids:
  - METPO:1000617
  summary: The complete retained catalog has no canonical Pyrococcus or genus entry.
    No alternative organism was substituted and no downstream module query performed.
    Catalog noncoverage is not negative phenotype evidence or a mandatory dataset
    defect.
  evidence_ids:
  - expression
  - runner
  - authority-reuse
- assessment_id: ownership
  area: ownership
  topic: 'Native checklist: mapping recurrence and maintained type decisions'
  outcome: concern
  target_ids:
  - METPO:1000617
  summary: Current record, wildcard predicate mappings and existing-ID skips own recurrence
    of relation conflicts. Preserve the explicit rigidity QUALITY decision, permitted
    GO functional ground, local proposal roles and typography retention. Wider canonical
    searches found context rather than a target-specific writer; record/history ownership
    remains and no global absence is inferred.
  evidence_ids:
  - owners
  - local-authority
  - provenance
- assessment_id: human-acceptance
  area: provenance
  topic: 'Native checklist: REVIEWED and local human attribution'
  outcome: concern
  target_ids:
  - METPO:1000617
  summary: Eighteen AI record changes plus seed and four captured AI contexts document
    maintenance. The inspected local material does not attribute a human acceptance
    decision for this target. Remote/private review is unassessed; this is bounded
    traceability rather than no-history or no-human-review-ever.
  evidence_ids:
  - provenance
  - native-policy
  - record
- assessment_id: checks
  area: schema
  topic: 'Native checklist: actual failures, successful retry and historical reuse'
  outcome: supported
  target_ids:
  - METPO:1000617
  summary: Focused validation and strict checks passed. Initial snippet script-path
    failure and DNS retry failure remain optional superseded attempts; the actual
    required network retry passed with mixed item statuses. B4/B5/B3/OLD checks retain
    original dates, failures, retry and skips. These invocation failures are not structured-review
    serialization failures.
  evidence_ids:
  - check-hyperthermophilic-validate
  - check-hyperthermophilic-strict
  - check-hyperthermophilic-snippets
  - check-hyperthermophilic-snippets-retry
  - check-hyperthermophilic-snippets-network-retry
  - check-corpus-protein-taxa
  - check-batch005-qc
  - reuse
  - reuse-supplement
findings:
- finding_id: ro-endpoint-roles
  issue_key: hyperthermophilic-ro-endpoint-roles
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Four imported RO relations conflict with represented endpoint kinds
  description: Edges 2 and 9 use RO:0002326 with trait and membrane-quality objects
    rather than processes; their material protein/chemical subjects are compatible.
    Edge 3 uses process regulation between material proteins. Edge 10 uses positive
    process regulation from a chemical to a quality. Preserve valid material, functional
    and QUALITY facets while reconciling these imported relations. The allowed GO
    functional ground is not an additional defect, and native acceptance is not external
    semantic validity.
  target_ids:
  - METPO:1000617
  field_paths:
  - causal_graphs[0].edges[2].predicate_id
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[9].predicate_id
  - causal_graphs[0].edges[10].predicate_id
  evidence_ids:
  - predicate-authority
  - node-edges
  - local-authority
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard contributes/regulates/increases mappings, rows 10–11 and 65
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Existing-ID skips and declared type gates
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: methylation-scope
  issue_key: hyperthermophilic-methylation-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The evidence note extends a three-culture abundance result to methylation
  description: Edge 7 notes combine increased GMGT production and methylation as a
    broad conclusion across three cultured archaea. PNAS paragraphs 21–22 support
    the all-three relative-abundance result, while paragraph 24 explicitly reports
    no clear methylation trend in A. profundus and a different result in another studied
    species. The combined note materially overgeneralizes the measured outcome. Retain
    the supported abundance statement and qualify only the methylation claim; no blanket
    false-chemistry or source-invalidity inference is made.
  target_ids:
  - METPO:1000617
  field_paths:
  - causal_graphs[0].edges[7].evidence[0].notes
  evidence_ids:
  - body-gms
  - edge-sources
  - placements
  - root-primary-check
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: composition-facet
  issue_key: hyperthermophilic-composition-facet
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Membrane composition and material-component wording leave the intended facet
    unclear
  description: Node 5 is CELLULAR_LOCALIZATION but names composition and describes
    lipid features. Native policy permits actual material membrane components, so
    this is a bounded attribute-versus-component clarification rather than a blanket
    prohibition on lipids in that enum. Make the intended existing referent consistent
    without prescribing a forced process retype or new mechanism.
  target_ids:
  - METPO:1000617
  field_paths:
  - causal_graphs[0].nodes[5].node_type
  - causal_graphs[0].nodes[5].label
  - causal_graphs[0].nodes[5].description
  evidence_ids:
  - native-types
  - node-edges
  - record
  - owners
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: quotation-continuity-context
  issue_key: hyperthermophilic-quotation-continuity-context
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Two snippets need contiguous wording or immediate source qualification
  description: Edge 1 visibly uses an ellipsis joining separated parts of a supported
    source sentence. Edge 2 is a literal substring, but stops just before an explicit
    exception in the same sentence. The graph prose already describes association,
    so do not infer that the entire graph asserts universal presence. Group these
    as bounded evidence continuity/context precision; the unknown chaperonin body
    quotation is not called false.
  target_ids:
  - METPO:1000617
  field_paths:
  - causal_graphs[0].edges[1].evidence[0].snippet
  - causal_graphs[0].edges[2].evidence[0].snippet
  evidence_ids:
  - snippets
  - snippet-policy
  - enzyme-primary
  - body-gyrase
  - root-primary-check
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: rigidity-certainty
  issue_key: hyperthermophilic-rigidity-certainty
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Node and edge wording is firmer than the qualified rigidity interpretation
  description: Edges 9 and 10 and node 12 describe physical rigidity/stability effects
    directly, while the nearest papers frame them as proposed or possible and discuss
    contextual limitations. Existing evidence notes already retain thought/could qualifiers.
    Align these descriptions with the supported confidence rather than treating the
    effect as disproven. This source-certainty concern is separate from imported predicate
    endpoint semantics.
  target_ids:
  - METPO:1000617
  field_paths:
  - causal_graphs[0].edges[9].description
  - causal_graphs[0].edges[10].description
  - causal_graphs[0].nodes[12].description
  evidence_ids:
  - body-rigidity
  - body-macrocyclic
  - edge-sources
  - record
  - root-primary-check
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: hyperthermophilic-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Inspected local provenance does not attribute human scientific acceptance
  description: REVIEWED is accompanied by eighteen AI changes and seed. Four fully
    read AI infrastructure/batch/other-record histories document context and maintained
    decisions, not a current-target human acceptance decision. Ignored-inclusive local
    searches have explicit bounds; remote/private content remains unassessed. This
    is a traceability concern, not a claim that no human review has ever occurred.
  target_ids:
  - METPO:1000617
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - provenance
  - native-policy
  - record
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-ro-roles
  description: Reconcile the four imported RO assignments with the current represented
    entity kinds.
  finding_ids:
  - ro-endpoint-roles
  target_ids:
  - METPO:1000617
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
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
  - Any retained identifier satisfies inherited process meanings. Preserve legitimate
    material proteins, chemicals, trait and QUALITY nodes rather than forcing retypes.
  - Keep the permitted functional GO ground and local/free-text predicates distinct;
    no replacement route or arbitrary CURIE is prescribed.
  - After separately authorized curation, use guarded writes, append-only record/repository
    history, focused validation/strict/source checks and relevant maintained audits/QC;
    regenerate affected outputs through maintained recipes. This review makes no scientific
    mutation.
- action_id: bound-methylation-claim
  description: Separate the supported abundance result from the narrower methylation
    observation.
  finding_ids:
  - methylation-scope
  target_ids:
  - METPO:1000617
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The note preserves positive all-three abundance evidence and does not claim a
    uniform all-three methylation increase contradicted by paragraph 24.
  - Retain studied-taxon and outcome scope without adding experimental conditions,
    optimization or universal extrapolation.
  - After separately authorized curation, use guarded writes, append-only record/repository
    history, focused validation/strict/source checks and relevant maintained audits/QC;
    regenerate affected outputs through maintained recipes. This review makes no scientific
    mutation.
- action_id: clarify-composition-facet
  description: Clarify whether the existing node denotes membrane material or its
    compositional attribute.
  finding_ids:
  - composition-facet
  target_ids:
  - METPO:1000617
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Label, description and native entity kind consistently express the intended existing
    facet. Native component allowance remains respected.
  - No forced pathway, protein instance or additional mechanism is required.
  - After separately authorized curation, use guarded writes, append-only record/repository
    history, focused validation/strict/source checks and relevant maintained audits/QC;
    regenerate affected outputs through maintained recipes. This review makes no scientific
    mutation.
- action_id: preserve-quotation-context
  description: Use contiguous source wording and preserve the adjacent qualification.
  finding_ids:
  - quotation-continuity-context
  target_ids:
  - METPO:1000617
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - The enzyme snippet satisfies the native contiguous-excerpt convention while retaining
    supported meaning. The literal gyrase excerpt does not silently discard its immediate
    source qualification.
  - Retain association wording and the distinct unknown chaperonin-body status; no
    universal requirement or source-falsity inference is introduced.
  - After separately authorized curation, use guarded writes, append-only record/repository
    history, focused validation/strict/source checks and relevant maintained audits/QC;
    regenerate affected outputs through maintained recipes. This review makes no scientific
    mutation.
- action_id: align-rigidity-confidence
  description: Align node and edge certainty with qualifications already retained
    in the evidence notes.
  finding_ids:
  - rigidity-certainty
  target_ids:
  - METPO:1000617
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Descriptions preserve the papers’ tentative interpretation and contextual limits,
    without presenting it as a universal direct measurement or disproven effect.
  - Relation endpoint semantics remain a separate issue; no new biological mechanism
    or experimental validation is prescribed.
  - After separately authorized curation, use guarded writes, append-only record/repository
    history, focused validation/strict/source checks and relevant maintained audits/QC;
    regenerate affected outputs through maintained recipes. This review makes no scientific
    mutation.
- action_id: attribute-human-acceptance
  description: Link existing human scientific acceptance or obtain it through the
    established process.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000617
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/hyperthermophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies the revision and scope, including unknown source text and
    qualified physical interpretations. Preserve current AI and contextual history.
  - Automated validation and this agent review do not substitute for human acceptance;
    reassess status if necessary.
limitations:
- The definition is a typical growth-preference classification, not a newly imposed
  universal boundary. PATO supplies relative temperature meaning; source and METPO
  supply numeric context. The selection edge remains contextual evolutionary interpretation,
  not a directly measured selection experiment.
- The canonical optimum is supported by an actual original publisher title/abstract
  preview. No full article, new culture conditions, assay transfer or strain optimization
  is claimed. Other-record comparator histories do not refute this separate source.
- The five literal snippets include the reverse-gyrase prefix before an immediate
  exception. One enzyme quote is a supported explicit abridgement and the chaperonin
  body quote remains unknown. Topic/metadata alone does not validate that edge; access
  failure is not disproof.
- Actual publisher browser receipts have no downloaded article-body hash. The source
  agent observed the ASM summary while the root separately received 403; these are
  distinct access outcomes. Historical BioC help/error is not article text.
- PNAS positively supports GMGT abundance increasing in all three studied cultures.
  Its methylation result is narrower and includes a no-clear-trend case. Relative
  abundance and methylation are distinct outcomes; no universal temperature trend
  across all hyperthermophiles is inferred.
- Both rigidity sources preserve proposed/possible interpretations and contextual
  or conflicting observations. Existing evidence notes already retain qualifiers.
  No definitive false-effect claim, new causal assay or intervention follows.
- The cDPG protective statements are background citing earlier work, with methanogen/model-biochemical
  context. Acquiring an entire XML is not full verification of all contents or a universal
  assay of archaeal proteins. No additional mechanism or optimization is supplied.
- RO:0002326 material/process constraints follow its RO:0002216/0002500/0002595 branch;
  RO:0002329 is another branch. Current material subjects are not blanket errors.
  Semantic review is not an executed OWL reasoner, and native validity does not settle
  external meanings.
- Local selects-for/confers remain maintained provisional proposals. Free-text edges
  do not inherit unasserted RO constraints. The functional GO protein ground, relative-temperature
  closeMatch, exact chemical identity and valid rigidity QUALITY are preserved.
- Five protein classes, four label-only nodes and zero instances are permitted. Two
  NONMECHANISTIC components do not mandate token protein anchors, added graph connections
  or mechanism completion.
- The complete retained catalog has no Pyrococcus match. No alternative organism or
  downstream module query was substituted; catalog noncoverage is not negative phenotype
  evidence. Runner discovery retains historical bounds rather than a fresh whole-machine
  absence claim.
- Publication-status inspection covers eight fresh indexed records, two Crossref records
  and reused thermal metadata. The PNAS link is a preprint version, not a correction.
  No global absence of notices is asserted.
- Four fully read AI history contexts and the historical provider report are provenance,
  not independent scientific proof or human acceptance. Ignored-inclusive searches
  have stated exclusions and remote/private content remains unassessed.
- The initial snippet path failure, DNS failure and successful required network retry
  all remain. Mixed snippet statuses are retained. Reused B4/B5/B3/OLD checks preserve
  original times, failures, retry and skips; readiness is distinct from QC.
- No scientific record, mapping, history, generated output, environment or Git state
  was modified. No paid research, experiment, organism intervention or new molecular
  target was introduced.
notes:
- 'Six findings: two major and four minor; all indices are zero-based.'
- All 63 captured hashes preserve the original 59 inputs. Target, parent, four histories
  and the 350-line provider report were fully read.
- Source ledger finalized at 11:26:52.303372Z and grounding at 11:26:16.404817Z. Original
  acquisition, copying, observation and integration times remain distinct.
- Nineteen events comprise eighteen explicit AI changes plus one automated seed. Five
  protein classes include four label-only nodes and zero instances.
tags:
- record-review
- hyperthermophilic
- environment
- needs-curation
```
